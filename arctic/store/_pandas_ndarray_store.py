import ast
import logging

from bson.binary import Binary
from pandas import DataFrame, MultiIndex, Series, DatetimeIndex, Panel
from pandas.tseries.index import DatetimeIndex
from pandas.tslib import Timestamp, get_timezone
import pandas as pd
import numpy as np

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

    def can_convert_to_records_without_objects(self, df, symbol, func=None):
        # We can't easily distinguish string columns from objects
        try:
            if func:
                arr, _ = func(df)
            else:
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

    def _segment_index(self, recarr, existing_index, start, new_segments):
        """
        Generate index of datetime64 -> item offset.

        Parameters:
        -----------
        new_data: new data being written (or appended)
        existing_index: index field from the versions document of the previous version
        start: first (0-based) offset of the new data
        segments: list of offsets. Each offset is the row index of the
                  the last row of a particular chunk relative to the start of the _original_ item.
                  array(new_data) - segments = array(offsets in item)

        Returns:
        --------
        Binary(compress(array([(index, datetime)]))
            Where index is the 0-based index of the datetime in the DataFrame
        """
        # find the index of the first datetime64 column
        idx_col = self._datetime64_index(recarr)
        # if one exists let's create the index on it
        if idx_col is not None:
            new_segments = np.array(new_segments, dtype='i8')
            last_rows = recarr[new_segments - start]
            # create numpy index
            index = np.core.records.fromarrays([last_rows[idx_col]]
                                               + [new_segments, ],
                                               dtype=INDEX_DTYPE)
            # append to existing index if exists
            if existing_index:
                existing_index_arr = np.fromstring(decompress(existing_index), dtype=INDEX_DTYPE)
                if start > 0:
                    existing_index_arr = existing_index_arr[existing_index_arr['index'] < start]
                index = np.concatenate((existing_index_arr, index))
            return Binary(compress(index.tostring()))
        elif existing_index:
            raise ArcticException("Could not find datetime64 index in item but existing data contains one")
        return None

    def _datetime64_index(self, recarr):
        """ Given a np.recarray find the first datetime64 column """
        # TODO: Handle multi-indexes
        names = recarr.dtype.names
        for name in names:
            if recarr[name].dtype == DTN64_DTYPE:
                return name
        return None

    def _index_range(self, version, symbol, date_range=None, **kwargs):
        """ Given a version, read the segment_index and return the chunks associated
        with the date_range. As the segment index is (id -> last datetime)
        we need to take care in choosing the correct chunks. """
        if date_range and 'segment_index' in version:
            index = np.fromstring(decompress(version['segment_index']), dtype=INDEX_DTYPE)
            dtcol = self._datetime64_index(index)
            if dtcol and len(index):
                dts = index[dtcol]
                start, end = _start_end(date_range, dts)
                if start > dts[-1]:
                    return -1, -1
                idxstart = min(np.searchsorted(dts, start), len(dts) - 1)
                idxend = min(np.searchsorted(dts, end), len(dts) - 1)
                return int(index['index'][idxstart]), int(index['index'][idxend] + 1)
        return super(PandasStore, self)._index_range(version, symbol, **kwargs)

    def _daterange(self, recarr, date_range):
        """ Given a recarr, slice out the given artic.date.DateRange if a
        datetime64 index exists """
        idx = self._datetime64_index(recarr)
        if idx and len(recarr):
            dts = recarr[idx]
            mask = Series(np.zeros(len(dts)), index=dts)
            start, end = _start_end(date_range, dts)
            mask[start:end] = 1.0
            return recarr[mask.values.astype(bool)]
        return recarr

    def read(self, arctic_lib, version, symbol, read_preference=None, date_range=None, **kwargs):
        item = super(PandasStore, self).read(arctic_lib, version, symbol, read_preference,
                                             date_range=date_range, **kwargs)
        if date_range:
            item = self._daterange(item, date_range)
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


def _start_end(date_range, dts):
    """
    Return tuple: [start, end] of np.datetime64 dates that are inclusive of the passed
    in datetimes.
    """
    # FIXME: timezones
    assert len(dts)
    _assert_no_timezone(date_range)
    date_range = to_pandas_closed_closed(date_range, add_tz=False)
    start = np.datetime64(date_range.start) if date_range.start else dts[0]
    end = np.datetime64(date_range.end) if date_range.end else dts[-1]
    return start, end


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

    def can_write(self, version, symbol, data, **kwargs):
        if isinstance(data, Series) and 'chunk_size' not in version:
            if data.dtype == np.object_ or data.index.dtype == np.object_:
                return self.can_convert_to_records_without_objects(data, symbol)
            return True
        return False

    def write(self, arctic_lib, version, symbol, item, previous_version):
        item, md = self.to_records(item)
        super(PandasSeriesStore, self).write(arctic_lib, version, symbol, item, previous_version, dtype=md)

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

    def can_write(self, version, symbol, data, **kwargs):
        if isinstance(data, DataFrame) and 'chunk_size' not in version:
            if np.any(data.dtypes.values == 'object'):
                return self.can_convert_to_records_without_objects(data, symbol)
            return True
        return False

    def write(self, arctic_lib, version, symbol, item, previous_version):
        item, md = self.to_records(item)
        super(PandasDataFrameStore, self).write(arctic_lib, version, symbol, item, previous_version, dtype=md)

    def append(self, arctic_lib, version, symbol, item, previous_version):
        item, md = self.to_records(item)
        super(PandasDataFrameStore, self).append(arctic_lib, version, symbol, item, previous_version, dtype=md)

    def read(self, arctic_lib, version, symbol, **kwargs):
        item = super(PandasDataFrameStore, self).read(arctic_lib, version, symbol, **kwargs)
        return self.from_records(item)


class PandasPanelStore(PandasDataFrameStore):
    TYPE = 'pandaspan'

    def can_write(self, version, symbol, data, **kwargs):
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


class PandasDateTimeIndexedStore(PandasStore):
    TYPE = 'pandasdti'

    def _column_data(self, df):
        if isinstance(df, DataFrame):
            return PandasDataFrameStore()._column_data(df)
        else:
            return PandasSeriesStore()._column_data(df)

    def can_write(self, version, symbol, data, **kwargs):
        if isinstance(data, (DataFrame, Series)):
            if 'date' in data.index.names and 'chunk_size' in version and version['chunk_size'] in ('D', 'M', 'Y'):
                if isinstance(data, DataFrame) and np.any(data.dtypes.values == 'object'):
                    return self.can_convert_to_records_without_objects(data, symbol, PandasDataFrameStore().to_records)
                elif isinstance(data, Series) and (data.dtype == np.object_ or data.index.dtype == np.object_):
                    return self.can_convert_to_records_without_objects(data, symbol, PandasSeriesStore().to_records)
                return True
        return False

    def get_date_chunk(self, date, chunk_size):
        fmt = ""
        if chunk_size == 'Y':
            fmt = '%Y'
        elif chunk_size == 'M':
            fmt = '%Y-%m'
        elif chunk_size == 'D':
            fmt = '%Y-%m-%d'
        return date.strftime(fmt)

    def get_range(self, df):
        dates = df.reset_index()['date']
        # return dates.min().strftime('%Y-%m-%d'), dates.max().strftime('%Y-%m-%d')
        return dates.min(), dates.max()

    def to_records(self, df, chunk_size):
        """
        chunks the dataframe/series by dates

        returns
        -------
        A list of tuples - (date, dataframe/series)
        """

        dates = [pd.to_datetime(d) for d in df.index.get_level_values('date').drop_duplicates()]
        key_array = [self.get_date_chunk(d, chunk_size) for d in dates]
        for g in df.groupby(key_array):
            start, end = self.get_range(g[1])
            yield start, end, g[1]

    def write(self, arctic_lib, version, symbol, item, previous_version, chunk_size=None):
        if isinstance(item, Series):
            version['pandas_type'] = 'series'
        else:
            version['pandas_type'] = 'df'

        records = []
        ranges = []
        dtype = None

        for start, end, record in self.to_records(item, chunk_size):
            r, dtype = super(PandasDateTimeIndexedStore, self).to_records(record)
            records.append(r)
            ranges.append((start, end))

        super(PandasDateTimeIndexedStore, self).chunked_write(arctic_lib,
                                                              version,
                                                              symbol,
                                                              records,
                                                              ranges,
                                                              previous_version,
                                                              dtype)

    def read(self, arctic_lib, version, symbol, date_range=None, **kwargs):
        item = super(PandasDateTimeIndexedStore, self).chunked_read(arctic_lib,
                                                                    version,
                                                                    symbol,
                                                                    date_range)

        if version['pandas_type'] == 'series':
            df = PandasSeriesStore().from_records(item)
        else:
            df = PandasDataFrameStore().from_records(item)

        if date_range is None:
            return df
        return df.ix[date_range[0]:date_range[1]]

    def append(self, arctic_lib, version, symbol, item, previous_version):
        if isinstance(item, Series) and previous_version['pandas_type'] == 'df':
            raise Exception("cannot append a series to a dataframe")
        if isinstance(item, DataFrame) and previous_version['pandas_type'] == 'series':
            raise Exception("cannot append a dataframe to a series")

        version['pandas_type'] = previous_version['pandas_type']
        version['chunk_size'] = previous_version['chunk_size']

        records = []
        ranges = []
        dtype = None

        for start, end, record in self.to_records(item, version['chunk_size']):
            r, dtype = super(PandasDateTimeIndexedStore, self).to_records(record)
            records.append(r)
            ranges.append((start, end))

        super(PandasDateTimeIndexedStore, self).chunked_append(arctic_lib,
                                                               version,
                                                               symbol,
                                                               records,
                                                               ranges,
                                                               previous_version,
                                                               dtype)
