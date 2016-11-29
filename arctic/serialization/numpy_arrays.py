import logging
import numpy as np
import numpy.ma as ma
import pandas as pd

from bson import Binary, SON

from .._compression import compress, decompress, compress_array
from ._serializer import Serializer


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

        if pd.lib.infer_dtype(a) == 'mixed':
            a = np.array([s.encode('ascii') for s in a])
            a = a.astype('O')

        type_ = pd.lib.infer_dtype(a)
        if type_ in ['unicode', 'string']:
            max_len = pd.lib.max_len_string_array(a)
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
                typ = pd.lib.infer_dtype(df[c])
                msg = "Column '{}' type is {}".format(str(c), typ)
                logging.info(msg)
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

    def objify(self, doc, columns=None):
        """
        Decode a Pymongo SON object into an Pandas DataFrame
        """
        cols = columns or doc[METADATA][COLUMNS]
        data = {}

        for col in cols:
            d = decompress(doc[DATA][doc[METADATA][LENGTHS][col][0]: doc[METADATA][LENGTHS][col][1] + 1])
            d = np.fromstring(d, doc[METADATA][DTYPE][col])

            if MASK in doc[METADATA] and col in doc[METADATA][MASK]:
                mask_data = decompress(doc[METADATA][MASK][col])
                mask = np.fromstring(mask_data, 'bool')
                d = ma.masked_array(d, mask)
            data[col] = d

        return pd.DataFrame(data, columns=cols)[cols]


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
        '''
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
        '''
        if data == []:
            return pd.DataFrame()

        meta = data[0][METADATA] if isinstance(data, list) else data[METADATA]
        index = INDEX in meta

        if columns:
            if index:
                columns.extend(meta[INDEX])
            if len(columns) > len(set(columns)):
                raise Exception("Duplicate columns specified, cannot de-serialize")

        if not isinstance(data, list):
            df = self.converter.objify(data, columns)
        else:
            df = pd.concat([self.converter.objify(d, columns) for d in data], ignore_index=not index)

        if index:
            df = df.set_index(meta[INDEX])
        if meta[TYPE] == 'series':
            return df[df.columns[0]]
        return df

    def combine(self, a, b):
        if a.index.names != [None]:
            return pd.concat([a, b]).sort_index()
        return pd.concat([a, b])
