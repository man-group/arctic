import logging
import numpy as np

from pandas import DataFrame, MultiIndex, Series, DatetimeIndex
try:
    from pandas._libs.tslib import Timestamp, get_timezone
except ImportError:
    from pandas.tslib import Timestamp, get_timezone


log = logging.getLogger(__name__)

DTN64_DTYPE = 'datetime64[ns]'


def _to_primitive(arr, string_max_len=None):
    if arr.dtype.hasobject:
        if len(arr) > 0:
            if isinstance(arr[0], Timestamp):
                return np.array([t.value for t in arr], dtype=DTN64_DTYPE)
        if string_max_len:
            return np.array(arr.astype('U{:d}'.format(string_max_len)))
        return np.array(list(arr))
    return arr


class PandasSerializer(object):
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
                    log.info("Level in MultiIndex has no name, defaulting to %s" % index_names[i])
        elif index_names[0] is None:
            index_names = ['index']
            log.info("Index has no name, defaulting to 'index'")

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

    def _to_records(self, df, string_max_len=None):
        """
        Similar to DataFrame.to_records()
        Differences:
            Attempt type conversion for pandas columns stored as objects (e.g. strings),
            as we can only store primitives in the ndarray.
            Use dtype metadata to store column and index names.
        
        string_max_len: integer - enforces a string size on the dtype, if any
                                  strings exist in the record
        """

        index_names, ix_vals, metadata = self._index_to_records(df)
        columns, column_vals = self._column_data(df)

        metadata['columns'] = columns
        names = index_names + columns

        arrays = []
        for arr in ix_vals + column_vals:
            arrays.append(_to_primitive(arr, string_max_len))

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
            arr, _ = self._to_records(df)
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

    def serialize(self, item):
        raise NotImplementedError

    def deserialize(self, item):
        raise NotImplementedError


class SeriesSerializer(PandasSerializer):
    TYPE = 'series'

    def _column_data(self, s):
        if s.name is None:
            log.info("Series has no name, defaulting to 'values'")
        columns = [s.name if s.name else 'values']
        column_vals = [s.values]
        return columns, column_vals

    def deserialize(self, item):
        index = self._index_from_records(item)
        name = item.dtype.names[-1]
        return Series.from_array(item[name], index=index, name=name)

    def serialize(self, item, string_max_len=None):
        return self._to_records(item, string_max_len)


class DataFrameSerializer(PandasSerializer):
    TYPE = 'df'

    def _column_data(self, df):
        columns = list(map(str, df.columns))
        if columns != list(df.columns):
            log.info("Dataframe column names converted to strings")
        column_vals = [df[c].values for c in df.columns]
        return columns, column_vals

    def deserialize(self, item):
        index = self._index_from_records(item)
        column_fields = [x for x in item.dtype.names if x not in item.dtype.metadata['index']]
        if len(item) == 0:
            rdata = item[column_fields] if len(column_fields) > 0 else None
            return DataFrame(rdata, index=index)

        columns = item.dtype.metadata['columns']
        return DataFrame(data=item[column_fields], index=index, columns=columns)

    def serialize(self, item, string_max_len=None):
        return self._to_records(item, string_max_len)
