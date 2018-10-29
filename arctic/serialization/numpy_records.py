import logging
import os

import numpy as np
from pandas import DataFrame, MultiIndex, Series, DatetimeIndex, Index
from ..exceptions import ArcticException
try:  # 0.21+ Compatibility
    from pandas._libs.tslib import Timestamp
    from pandas._libs.tslibs.timezones import get_timezone
except ImportError:
    try:  # 0.20.x Compatibility
        from pandas._libs.tslib import Timestamp, get_timezone
    except ImportError:  # <= 0.19 Compatibility
        from pandas.tslib import Timestamp, get_timezone


log = logging.getLogger(__name__)

DTN64_DTYPE = 'datetime64[ns]'

# TODO: Switch on by default this flag to enable the fast check once this gets thoroughly tested
_FAST_CHECK_DF_SERIALIZABLE = bool(os.environ.get('ENABLE_FAST_CHECK_DF_SERIALIZABLE'))


def set_fast_check_df_serializable(config):
    global _FAST_CHECK_DF_SERIALIZABLE
    _FAST_CHECK_DF_SERIALIZABLE = bool(config)


def _to_primitive(arr, string_max_len=None):
    if arr.dtype.hasobject:
        if len(arr) > 0 and isinstance(arr[0], Timestamp):
            return np.array([t.value for t in arr], dtype=DTN64_DTYPE)

        if string_max_len:
            str_array = np.array(arr.astype('U{:d}'.format(string_max_len)))
        else:
            str_array = np.array(list(arr))

        # Pick any unwanted data conversions (e.g. np.NaN to 'nan')
        if np.array_equal(arr, str_array):
            return str_array
    return arr


def _multi_index_to_records(index, empty_index):
    # array of tuples to numpy cols. copy copy copy
    if not empty_index:
        ix_vals = list(map(np.array, [index.get_level_values(i) for i in range(index.nlevels)]))
    else:
        # empty multi index has no size, create empty arrays for recarry..
        ix_vals = [np.array([]) for n in index.names]
    index_names = list(index.names)
    count = 0
    for i, n in enumerate(index_names):
        if n is None:
            index_names[i] = 'level_%d' % count
            count += 1
            log.info("Level in MultiIndex has no name, defaulting to %s" % index_names[i])
    index_tz = [get_timezone(i.tz) if isinstance(i, DatetimeIndex) else None for i in index.levels]
    return ix_vals, index_names, index_tz


class PandasSerializer(object):

    def _index_to_records(self, df):
        metadata = {}
        index = df.index
        index_tz = None

        if isinstance(index, MultiIndex):
            ix_vals, index_names, index_tz = _multi_index_to_records(index, len(df) == 0)
        else:
            ix_vals = [index.values]
            index_names = list(index.names)
            if index_names[0] is None:
                index_names = ['index']
                log.info("Index has no name, defaulting to 'index'")
            if isinstance(index, DatetimeIndex) and index.tz is not None:
                index_tz = get_timezone(index.tz)

        if index_tz is not None:
            metadata['index_tz'] = index_tz
        metadata['index'] = index_names

        return index_names, ix_vals, metadata

    def _index_from_records(self, recarr):
        index = recarr.dtype.metadata['index']

        if len(index) == 1:
            rtn = Index(np.copy(recarr[str(index[0])]), name=index[0])
            if isinstance(rtn, DatetimeIndex) and 'index_tz' in recarr.dtype.metadata:
                rtn = rtn.tz_localize('UTC').tz_convert(recarr.dtype.metadata['index_tz'])
        else:
            level_arrays = []
            index_tz = recarr.dtype.metadata.get('index_tz', [])
            for level_no, index_name in enumerate(index):
                # build each index level separately to ensure we end up with the right index dtype
                level = Index(np.copy(recarr[str(index_name)]))
                if level_no < len(index_tz):
                    tz = index_tz[level_no]
                    if tz is not None:
                        if not isinstance(level, DatetimeIndex) and len(level) == 0:
                            # index type information got lost during save as the index was empty, cast back
                            level = DatetimeIndex([], tz=tz)
                        else:
                            level = level.tz_localize('UTC').tz_convert(tz)
                level_arrays.append(level)
            rtn = MultiIndex.from_arrays(level_arrays, names=index)
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
        columns, column_vals, multi_column = self._column_data(df)

        if "" in columns:
            raise ArcticException("Cannot use empty string as a column name.")

        if multi_column is not None:
            metadata['multi_column'] = multi_column
        metadata['columns'] = columns
        names = index_names + columns

        arrays = []
        for arr in ix_vals + column_vals:
            arrays.append(_to_primitive(arr, string_max_len))

        dtype = np.dtype([(str(x), v.dtype) if len(v.shape) == 1 else (str(x), v.dtype, v.shape[1]) for x, v in zip(names, arrays)],
                         metadata=metadata)

        # The argument names is ignored when dtype is passed
        rtn = np.rec.fromarrays(arrays, dtype=dtype, names=names)
        # For some reason the dtype metadata is lost in the line above
        # and setting rtn.dtype to dtype does not preserve the metadata
        # see https://github.com/numpy/numpy/issues/6771

        return (rtn, dtype)

    def fast_check_serializable(self, df):
        """
        Convert efficiently the frame's object-columns/object-index/multi-index/multi-column to
        records, by creating a recarray only for the object fields instead for the whole dataframe.
        If we have no object dtypes, we can safely convert only the first row to recarray to test if serializable.
        Previously we'd serialize twice the full dataframe when it included object fields or multi-index/columns.

        Parameters
        ----------
        df: `pandas.DataFrame` or `pandas.Series`

        Returns
        -------
        `tuple[numpy.core.records.recarray, dict[str, numpy.dtype]`
            If any object dtypes are detected in columns or index will return a dict with field-name -> dtype
             mappings, and empty dict otherwise.
        """
        i_dtype, f_dtypes = df.index.dtype, df.dtypes
        index_has_object = df.index.dtype.hasobject
        fields_with_object = [f for f in df.columns if f_dtypes[f] is np.dtype('O')]
        if df.empty or (not index_has_object and not fields_with_object):
            arr, _ = self._to_records(df.iloc[:10])  # only first few rows for performance
            return arr, {}
        # If only the Index has Objects, choose a small slice (two columns if possible,
        # to avoid switching from a DataFrame to a Series)
        df_objects_only = df[fields_with_object if fields_with_object else df.columns[:2]]
        # Let any exceptions bubble up from here
        arr, dtype = self._to_records(df_objects_only)
        return arr, {f: dtype[f] for f in dtype.names}

    def can_convert_to_records_without_objects(self, df, symbol):
        # We can't easily distinguish string columns from objects
        try:
            #TODO: we can add here instead a check based on df size and enable fast-check if sz > threshold value
            if _FAST_CHECK_DF_SERIALIZABLE:
                arr, _ = self.fast_check_serializable(df)
            else:
                arr, _ = self._to_records(df)
        except Exception as e:
            # This exception will also occur when we try to write the object so we fall-back to saving using Pickle
            log.warning('Pandas dataframe %s caused exception "%s" when attempting to convert to records. '
                        'Saving as Blob.' % (symbol, repr(e)))
            return False
        else:
            if arr.dtype.hasobject:
                log.warning('Pandas dataframe %s contains Objects, saving as Blob' % symbol)
                # Fall-back to saving using Pickle
                return False
            elif any([len(x[0].shape) for x in arr.dtype.fields.values()]):
                log.warning('Pandas dataframe %s contains >1 dimensional arrays, saving as Blob' % symbol)
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
        return columns, column_vals, None

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

        if isinstance(df.columns, MultiIndex):
            ix_vals, ix_names, _ = _multi_index_to_records(df.columns, False)
            vals = [list(val) for val in ix_vals]
            str_vals = [list(map(str, val)) for val in ix_vals]
            if vals != str_vals:
                log.info("Dataframe column names converted to strings")
            return columns, column_vals, {"names": list(ix_names), "values": str_vals}
        else:
            return columns, column_vals, None

    def deserialize(self, item):
        index = self._index_from_records(item)
        column_fields = [x for x in item.dtype.names if x not in item.dtype.metadata['index']]
        multi_column = item.dtype.metadata.get('multi_column')
        if len(item) == 0:
            rdata = item[column_fields] if len(column_fields) > 0 else None
            if multi_column is not None:
                columns = MultiIndex.from_arrays(multi_column["values"], names=multi_column["names"])
                return DataFrame(rdata, index=index, columns=columns)
            else:
                return DataFrame(rdata, index=index)

        columns = item.dtype.metadata['columns']
        df = DataFrame(data=item[column_fields], index=index, columns=columns)

        if multi_column is not None:
            df.columns = MultiIndex.from_arrays(multi_column["values"], names=multi_column["names"])

        return df

    def serialize(self, item, string_max_len=None):
        return self._to_records(item, string_max_len)
