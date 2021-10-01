import logging

import numpy as np
import numpy.ma as ma
import pandas as pd
from bson import Binary, SON

from .._compression import compress, decompress, compress_array
from ._serializer import Serializer
from collections import defaultdict
try:
    from pandas.api.types import infer_dtype
except ImportError:
    from pandas.lib import infer_dtype

try:
    # pandas >= 0.23.0
    from pandas._libs.writers import max_len_string_array
except ImportError:
    try:
        # pandas [0.20.0, 0.22.x]
        from pandas._libs.lib import max_len_string_array
    except ImportError:
        # pandas <=  0.19.x
        from pandas.lib import max_len_string_array

if int(pd.__version__.split('.')[1]) > 22:
    from functools import partial
    pd.concat = partial(pd.concat, sort=False)


DATA = 'd'
MASK = 'm'
TYPE = 't'
DTYPE = 'dt'
COLUMNS = 'c'
INDEX = 'i'
METADATA = 'md'
LENGTHS = 'ln'


class FrameConverter(object):
    """
    Converts a Pandas Dataframe to and from PyMongo SON representation:

        {
          METADATA: {
                      COLUMNS: [col1, col2, ...]             list of str
                      MASKS: {col1: mask, col2: mask, ...}   dict of str: Binary
                      INDEX: [idx1, idx2, ...]               list of str
                      TYPE: 'series' or 'dataframe'
                      LENGTHS: {col1: len, col2: len, ...}   dict of str: int
                    }
          DATA: BINARY(....)      Compressed columns concatenated together
        }
    """

    def _convert_types(self, a):
        """
        Converts object arrays of strings to numpy string arrays
        """
        # No conversion for scalar type
        if a.dtype != 'object':
            return a, None

        # We can't infer the type of an empty array, so just
        # assume strings
        if len(a) == 0:
            return a.astype('U1'), None

        # Compute a mask of missing values. Replace NaNs and Nones with
        # empty strings so that type inference has a chance.
        mask = pd.isnull(a)
        if mask.sum() > 0:
            a = a.copy()
            np.putmask(a, mask, '')
        else:
            mask = None

        if infer_dtype(a, skipna=False) == 'mixed':
            # assume its a string, otherwise raise an error
            try:
                a = np.array([s.encode('ascii') for s in a])
                a = a.astype('O')
            except:
                raise ValueError("Column of type 'mixed' cannot be converted to string")

        type_ = infer_dtype(a, skipna=False)
        if type_ in ['unicode', 'string']:
            max_len = max_len_string_array(a)
            return a.astype('U{:d}'.format(max_len)), mask
        else:
            raise ValueError('Cannot store arrays with {} dtype'.format(type_))

    def docify(self, df):
        """
        Convert a Pandas DataFrame to SON.

        Parameters
        ----------
        df:  DataFrame
            The Pandas DataFrame to encode
        """
        dtypes = {}
        masks = {}
        lengths = {}
        columns = []
        data = Binary(b'')
        start = 0

        arrays = []
        for c in df:
            try:
                columns.append(str(c))
                arr, mask = self._convert_types(df[c].values)
                dtypes[str(c)] = arr.dtype.str
                if mask is not None:
                    masks[str(c)] = Binary(compress(mask.tostring()))
                arrays.append(arr.tostring())
            except Exception as e:
                typ = infer_dtype(df[c], skipna=False)
                msg = "Column '{}' type is {}".format(str(c), typ)
                logging.warning(msg)
                raise e

        arrays = compress_array(arrays)
        for index, c in enumerate(df):
            d = Binary(arrays[index])
            lengths[str(c)] = (start, start + len(d) - 1)
            start += len(d)
            data += d

        doc = SON({DATA: data, METADATA: {}})
        doc[METADATA] = {COLUMNS: columns,
                         MASK: masks,
                         LENGTHS: lengths,
                         DTYPE: dtypes
                         }

        return doc

    def objify(self, doc, columns=None, as_df=True):
        """
        Decode a Pymongo SON object into an Pandas DataFrame
        """
        cols = columns or doc[METADATA][COLUMNS]
        data = {}
        valid_columns = set(cols).intersection(doc[METADATA][LENGTHS])
        missing_columns = set(cols).difference(valid_columns)
        for col in valid_columns:
            d = decompress(doc[DATA][doc[METADATA][LENGTHS][col][0]: doc[METADATA][LENGTHS][col][1] + 1])
            # d is ready-only but that's not an issue since DataFrame will copy the data anyway.
            d = np.frombuffer(d, doc[METADATA][DTYPE][col])

            if MASK in doc[METADATA] and col in doc[METADATA][MASK]:
                mask_data = decompress(doc[METADATA][MASK][col])
                mask = np.frombuffer(mask_data, 'bool')
                d = ma.masked_array(d, mask)
            data[col] = d

        if data:
            for col in missing_columns:
                # if there is missing data in a chunk, we can default to NaN and
                empty = np.empty(len(d))
                empty[:] = np.nan
                data[col] = empty

        if as_df:
            return pd.DataFrame(data)

        return data


class FrametoArraySerializer(Serializer):
    TYPE = 'FrameToArray'

    def __init__(self):
        self.converter = FrameConverter()

    def serialize(self, df):
        if isinstance(df, pd.Series):
            dtype = 'series'
            df = df.to_frame()
        else:
            dtype = 'dataframe'

        if (len(df.index.names) > 1 and None in df.index.names) or None in list(df.columns.values):
            raise Exception("All columns and indexes must be named")

        if df.index.names != [None]:
            index = df.index.names
            df = df.reset_index()
            ret = self.converter.docify(df)
            ret[METADATA][INDEX] = index
            ret[METADATA][TYPE] = dtype
            return ret
        ret = self.converter.docify(df)
        ret[METADATA][TYPE] = dtype
        return ret

    def deserialize(self, data, columns=None):
        """
        Deserializes SON to a DataFrame

        Parameters
        ----------
        data: SON data
        columns: None, or list of strings
            optionally you can deserialize a subset of the data in the SON. Index
            columns are ALWAYS deserialized, and should not be specified

        Returns
        -------
        pandas dataframe or series
        """
        if not data:
            return pd.DataFrame()

        meta = data[0][METADATA] if isinstance(data, list) else data[METADATA]
        index = INDEX in meta

        if not isinstance(data, list):
            data = [data]

        if columns:
            if index:
                columns = columns[:]
                columns.extend(meta[INDEX])
            if len(columns) > len(set(columns)):
                raise Exception("Duplicate columns specified, cannot de-serialize")
        else:
            columns = [col for doc in data for col in doc[METADATA][COLUMNS]]

        df = defaultdict(list)

        for d in data:
            for k, v in self.converter.objify(d, columns, as_df=False).items():
                df[k].append(v)

        idx_cols = meta[INDEX] if index else []
        if len(idx_cols) > 1:
            idx = pd.MultiIndex.from_arrays([np.concatenate(df[k]) for k in idx_cols], names=idx_cols)
        elif len(idx_cols) == 1:
            idx = pd.Index(np.concatenate(df[idx_cols[0]]), name=idx_cols[0])
        else:
            idx = None

        df = pd.DataFrame({k: np.concatenate(v) for k, v in df.items() if k not in idx_cols}, index=idx)

        if meta[TYPE] == 'series':
            return df[df.columns[0]]
        return df

    def combine(self, a, b):
        if a.index.names != [None]:
            return pd.concat([a, b]).sort_index()
        return pd.concat([a, b])
