import logging

from bson.binary import Binary
from pandas import DataFrame, MultiIndex, Series, DatetimeIndex, Panel
from pandas.tslib import Timestamp, get_timezone
import numpy as np

from .._compression import compress, decompress
from ..exceptions import ArcticException
from ._ndarray_store import NdarrayStore
from ..date._util import to_pandas_closed_closed

log = logging.getLogger(__name__)

DTN64_DTYPE = 'datetime64[ns]'

INDEX_DTYPE = [('datetime', DTN64_DTYPE), ('index', 'i8')]


def _to_primitive(arr):
    if arr.dtype.hasobject:
        if len(arr) > 0:
            if isinstance(arr[0], Timestamp):
                return arr.astype(DTN64_DTYPE)
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
                idxstart = min(np.searchsorted(dts, start), len(dts))
                idxend = min(np.searchsorted(dts, end), len(dts))
                return index['index'][idxstart], index['index'][idxend] + 1
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


def _start_end(date_range, dts):
    """
    Return tuple: [start, end] of np.datetime64 dates that are inclusive of the passed
    in datetimes.
    """
    # FIXME: timezones
    assert len(dts)
    date_range = to_pandas_closed_closed(date_range)
    start = np.datetime64(date_range.start) if date_range.start else dts[0]
    end = np.datetime64(date_range.end) if date_range.end else dts[-1]
    return start, end


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
