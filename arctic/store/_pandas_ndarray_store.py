import ast
import logging

from bson.binary import Binary
from pandas import DataFrame, MultiIndex, Series, DatetimeIndex, Panel
from pandas.tseries.index import DatetimeIndex
from pandas.tslib import Timestamp, get_timezone

import numpy as np
import pandas as pd

from .._compression import compress, decompress
from ..date._util import to_pandas_closed_closed
from ..exceptions import ArcticException
from ._ndarray_store import NdarrayStore


log = logging.getLogger(__name__)

DTN64_DTYPE = 'datetime64[ns]'

INDEX_DTYPE = [('datetime', DTN64_DTYPE), ('index', 'i8')]


def _to_primitive(arr):
    if arr.dtype.hasobject:
        if len(arr) > 0:
            if isinstance(arr[0], Timestamp):
                return np.array([t.value for t in arr], dtype=DTN64_DTYPE)
        return np.array(list(arr))
    return arr


class PandasDateChunker(object):
    TYPE = 'pandasdate'

    def __call__(self, item, **kwargs):
        if 'chunk' not in kwargs or kwargs['chunk'] not in ('D', 'M', 'Y'):
            raise Exception('Must specify a chunk size of D, M or Y when using a date chunker')

        if 'dates' in item:
            dates = [pd.to_datetime(d) for d in item.date.unique()]
        else:
            try:
                dates = [pd.to_datetime(d) for d in item.get_level_values('date').unique()]
            except:
                raise Exception('Dataframe/Series must be date indexed')
        key_map = {d: self.get_key_for_date(d) for d in dates}

        if 'dates' in item:
            g = item.groupby(item.date.map(key_map))
        else:
            g = item.groupby(item.get_level_values('date').map(key_map))

        for group in g:
            yield str(g.date.max()), PandasStore().to_records(group)[0]

    def index_range(self, version, from_version=None, **kwargs):
        from_index = None
        if from_version:
            if version['base_sha'] != from_version['base_sha']:
                # give up - the data has been overwritten, so we can't tail this
                raise ConcurrentModificationException("Concurrent modification - data has been overwritten")
            from_index = from_version['up_to']
        return from_index, None


class PandasStore(NdarrayStore):

    def _index_to_records(self, df):
        metadata = {}
        index = df.index

        if isinstance(index, MultiIndex):
            # array of tuples to numpy cols. copy copy copy
            if len(df) > 0:
                ix_vals = list(map(np.array, [index.get_level_values(i) for i in range(index.nlevels)]))
            else:
                # empty multi index has no size, create empty arrays for recarry..
                ix_vals = [np.array([]) for n in index.names]
        else:
            ix_vals = [index.values]

        count = 0
        index_names = list(index.names)
        if isinstance(index, MultiIndex):
            for i, n in enumerate(index_names):
                if n is None:
                    index_names[i] = 'level_%d' % count
                    count += 1
        elif index_names[0] is None:
            index_names = ['index']

        metadata['index'] = index_names

        if isinstance(index, DatetimeIndex) and index.tz is not None:
            metadata['index_tz'] = get_timezone(index.tz)
        elif isinstance(index, MultiIndex):
            metadata['index_tz'] = [get_timezone(i.tz) if isinstance(i, DatetimeIndex) else None for i in index.levels]

        return index_names, ix_vals, metadata

    def _index_from_records(self, recarr):
        index = recarr.dtype.metadata['index']
        rtn = MultiIndex.from_arrays([recarr[str(i)] for i in index], names=index)

        if isinstance(rtn, DatetimeIndex) and 'index_tz' in recarr.dtype.metadata:
            rtn = rtn.tz_localize('UTC').tz_convert(recarr.dtype.metadata['index_tz'])
        elif isinstance(rtn, MultiIndex):
            for i, tz in enumerate(recarr.dtype.metadata.get('index_tz', [])):
                if tz is not None:
                    rtn.set_levels(rtn.levels[i].tz_localize('UTC').tz_convert(tz), i, inplace=True)

        return rtn

    def to_records(self, df):
        """
        Similar to DataFrame.to_records()
        Differences:
            Attempt type conversion for pandas columns stored as objects (e.g. strings),
            as we can only store primitives in the ndarray.
            Use dtype metadata to store column and index names.
        """

        index_names, ix_vals, metadata = self._index_to_records(df)
        columns, column_vals = self._column_data(df)

        metadata['columns'] = columns
        names = index_names + columns
        arrays = ix_vals + column_vals
        arrays = list(map(_to_primitive, arrays))
        dtype = np.dtype([(str(x), v.dtype) if len(v.shape) == 1 else (str(x), v.dtype, v.shape[1]) for x, v in zip(names, arrays)],
                         metadata=metadata)

        rtn = np.rec.fromarrays(arrays, dtype=dtype, names=names)
        # For some reason the dtype metadata is lost in the line above
        # and setting rtn.dtype to dtype does not preserve the metadata
        # see https://github.com/numpy/numpy/issues/6771

        return (rtn, dtype)

    def can_convert_to_records_without_objects(self, df, symbol):
        # We can't easily distinguish string columns from objects
        try:
            arr, _ = self.to_records(df)
        except Exception as e:
            # This exception will also occur when we try to write the object so we fall-back to saving using Pickle
            log.info('Pandas dataframe %s caused exception "%s" when attempting to convert to records. Saving as Blob.'
                     % (symbol, repr(e)))
            return False
        else:
            if arr.dtype.hasobject:
                log.info('Pandas dataframe %s contains Objects, saving as Blob' % symbol)
                # Will fall-back to saving using Pickle
                return False
            elif any([len(x[0].shape) for x in arr.dtype.fields.values()]):
                log.info('Pandas dataframe %s contains >1 dimensional arrays, saving as Blob' % symbol)
                return False
            else:
                return True

    def read(self, arctic_lib, version, symbol, read_preference=None, date_range=None, **kwargs):
        item = super(PandasStore, self).read(arctic_lib, version, symbol, read_preference,
                                             date_range=date_range, **kwargs)
        return item

    def get_info(self, version):
        """
        parses out the relevant information in version
        and returns it to the user in a dictionary
        """
        ret = super(PandasStore, self).get_info(version)
        ret['col_names'] = version['dtype_metadata']
        ret['handler'] = self.__class__.__name__
        ret['dtype'] = ast.literal_eval(version['dtype'])
        return ret


def _assert_no_timezone(date_range):
    for _dt in (date_range.start, date_range.end):
        if _dt and _dt.tzinfo is not None:
            raise ValueError("DateRange with timezone not supported")


class PandasSeriesStore(PandasStore):
    TYPE = 'pandasseries'

    def _column_data(self, s):
        columns = [s.name if s.name else 'values']
        column_vals = [s.values]
        return columns, column_vals

    def from_records(self, recarr):
        index = self._index_from_records(recarr)
        name = recarr.dtype.names[-1]
        return Series.from_array(recarr[name], index=index, name=name)

    def can_write(self, version, symbol, data):
        if isinstance(data, Series):
            if data.dtype == np.object_ or data.index.dtype == np.object_:
                return self.can_convert_to_records_without_objects(data, symbol)
            return True
        return False

    def write(self, arctic_lib, version, symbol, item, previous_version):
        _, md = self.to_records(item)
        super(PandasSeriesStore, self).write(arctic_lib, version, symbol, item, previous_version, chunker=PandasDateChunker(), dtype=md)

    def append(self, arctic_lib, version, symbol, item, previous_version):
        item, md = self.to_records(item)
        super(PandasSeriesStore, self).append(arctic_lib, version, symbol, item, previous_version, dtype=md)

    def read(self, arctic_lib, version, symbol, **kwargs):
        item = super(PandasSeriesStore, self).read(arctic_lib, version, symbol, **kwargs)
        return self.from_records(item)


class PandasDataFrameStore(PandasStore):
    TYPE = 'pandasdf'

    def _column_data(self, df):
        columns = list(map(str, df.columns))
        column_vals = [df[c].values for c in df.columns]
        return columns, column_vals

    def from_records(self, recarr):
        index = self._index_from_records(recarr)
        column_fields = [x for x in recarr.dtype.names if x not in recarr.dtype.metadata['index']]
        if len(recarr) == 0:
            rdata = recarr[column_fields] if len(column_fields) > 0 else None
            return DataFrame(rdata, index=index)

        columns = recarr.dtype.metadata['columns']
        return DataFrame(data=recarr[column_fields], index=index, columns=columns)

    def can_write(self, version, symbol, data):
        if isinstance(data, DataFrame):
            if np.any(data.dtypes.values == 'object'):
                return self.can_convert_to_records_without_objects(data, symbol)
            return True
        return False

    def write(self, arctic_lib, version, symbol, item, previous_version):
        _, md = self.to_records(item)
        super(PandasDataFrameStore, self).write(arctic_lib, version, symbol, item, previous_version, chunker=PandasDateChunker(), dtype=md)

    def append(self, arctic_lib, version, symbol, item, previous_version):
        item, md = self.to_records(item)
        super(PandasDataFrameStore, self).append(arctic_lib, version, symbol, item, previous_version, dtype=md)

    def read(self, arctic_lib, version, symbol, **kwargs):
        item = super(PandasDataFrameStore, self).read(arctic_lib, version, symbol, **kwargs)
        return self.from_records(item)


class PandasPanelStore(PandasDataFrameStore):
    TYPE = 'pandaspan'

    def can_write(self, version, symbol, data):
        if isinstance(data, Panel):
            frame = data.to_frame(filter_observations=False)
            if np.any(frame.dtypes.values == 'object'):
                return self.can_convert_to_records_without_objects(frame, symbol)
            return True
        return False

    def write(self, arctic_lib, version, symbol, item, previous_version):
        if np.product(item.shape) == 0:
            # Currently not supporting zero size panels as they drop indices when converting to dataframes
            # Plan is to find a better solution in due course.
            raise ValueError('Cannot insert a zero size panel into mongo.')
        if not np.all(len(i.names) == 1 for i in item.axes):
            raise ValueError('Cannot insert panels with multiindexes')
        item = item.to_frame(filter_observations=False)
        if len(set(item.dtypes)) == 1:
            # If all columns have the same dtype, we support non-string column names.
            # We know from above check that columns is not a multiindex.
            item = DataFrame(item.stack())
        elif item.columns.dtype != np.dtype('object'):
            raise ValueError('Cannot support non-object dtypes for columns')
        super(PandasPanelStore, self).write(arctic_lib, version, symbol, item, previous_version)

    def read(self, arctic_lib, version, symbol, **kwargs):
        item = super(PandasPanelStore, self).read(arctic_lib, version, symbol, **kwargs)
        if len(item.index.names) == 3:
            return item.iloc[:, 0].unstack().to_panel()
        return item.to_panel()

    def append(self, arctic_lib, version, symbol, item, previous_version):
        raise ValueError('Appending not supported for pandas.Panel')
