import logging

from _ndarray_store import NdarrayStore
from pandas import DataFrame, MultiIndex, Series, DatetimeIndex, Panel
from pandas.tslib import Timestamp, get_timezone
import numpy as np

log = logging.getLogger(__name__)


def _to_primitive(arr):
    if arr.dtype.hasobject:
        if len(arr) > 0:
            if isinstance(arr[0], Timestamp):
                return arr.astype('datetime64[ns]')
        return np.array(list(arr))
    return arr


class PandasStore(NdarrayStore):

    def _index_to_records(self, df):
        metadata = {}
        index = df.index

        if isinstance(index, MultiIndex):
            # array of tuples to numpy cols. copy copy copy
            if len(df) > 0:
                ix_vals = map(np.array, zip(*index.values))
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

        return index_names, ix_vals, metadata

    def _index_from_records(self, recarr):
        index = recarr.dtype.metadata['index']
        rtn = MultiIndex.from_arrays([recarr[str(i)] for i in index], names=index)

        if isinstance(rtn, DatetimeIndex) and 'index_tz' in recarr.dtype.metadata:
            rtn = rtn.tz_localize('UTC').tz_convert(recarr.dtype.metadata['index_tz'])

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
        arrays = map(_to_primitive, arrays)
        dtype = np.dtype([(str(x), v.dtype) if len(v.shape) == 1 else (str(x), v.dtype, v.shape[1]) for x, v in zip(names, arrays)],
                         metadata=metadata)
        rtn = np.rec.fromarrays(arrays, dtype=dtype, names=names)
        #For some reason the dtype metadata is lost in the line above.
        rtn.dtype = dtype
        return rtn

    def can_convert_to_records_without_objects(self, df, symbol):
        # We can't easily distinguish string columns from objects
        try:
            arr = self.to_records(df)
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
        item = self.to_records(item)
        super(PandasSeriesStore, self).write(arctic_lib, version, symbol, item, previous_version)

    def append(self, arctic_lib, version, symbol, item, previous_version):
        item = self.to_records(item)
        super(PandasSeriesStore, self).append(arctic_lib, version, symbol, item, previous_version)

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
        item = self.to_records(item)
        super(PandasDataFrameStore, self).write(arctic_lib, version, symbol, item, previous_version)

    def append(self, arctic_lib, version, symbol, item, previous_version):
        item = self.to_records(item)
        super(PandasDataFrameStore, self).append(arctic_lib, version, symbol, item, previous_version)

    def read(self, arctic_lib, version, symbol, **kwargs):
        item = super(PandasDataFrameStore, self).read(arctic_lib, version, symbol, **kwargs)
        return self.from_records(item)


class PandasPanelStore(PandasDataFrameStore):
    TYPE = 'pandaspan'

    def can_write(self, version, symbol, data):
        if isinstance(data, Panel):
            frame = data.to_frame()
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
        item = item.to_frame()
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
