import ast
import logging

from bson.binary import Binary
from pandas import DataFrame, Series, Panel
from pandas.tslib import Timestamp, get_timezone

import numpy as np

from arctic.serialization.pandas_serializer import SeriesSerializer, DataFrameSerializer
from .._compression import compress, decompress
from ..date._util import to_pandas_closed_closed
from ..exceptions import ArcticException
from ._ndarray_store import NdarrayStore


log = logging.getLogger(__name__)

DTN64_DTYPE = 'datetime64[ns]'

INDEX_DTYPE = [('datetime', DTN64_DTYPE), ('index', 'i8')]


class PandasStore(NdarrayStore):

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
    SERIALIZER = SeriesSerializer()

    def can_write(self, version, symbol, data):
        if isinstance(data, Series):
            if data.dtype == np.object_ or data.index.dtype == np.object_:
                return self.SERIALIZER.can_convert_to_records_without_objects(data, symbol)
            return True
        return False

    def write(self, arctic_lib, version, symbol, item, previous_version):
        item, md = self.SERIALIZER.serialize(item)
        super(PandasSeriesStore, self).write(arctic_lib, version, symbol, item, previous_version, dtype=md)

    def append(self, arctic_lib, version, symbol, item, previous_version):
        item, md = self.SERIALIZER.serialize(item)
        super(PandasSeriesStore, self).append(arctic_lib, version, symbol, item, previous_version, dtype=md)

    def read(self, arctic_lib, version, symbol, **kwargs):
        item = super(PandasSeriesStore, self).read(arctic_lib, version, symbol, **kwargs)
        return self.SERIALIZER.deserialize(item)


class PandasDataFrameStore(PandasStore):
    TYPE = 'pandasdf'
    SERIALIZER = DataFrameSerializer()

    def can_write(self, version, symbol, data):
        if isinstance(data, DataFrame):
            if np.any(data.dtypes.values == 'object'):
                return self.SERIALIZER.can_convert_to_records_without_objects(data, symbol)
            return True
        return False

    def write(self, arctic_lib, version, symbol, item, previous_version):
        item, md = self.SERIALIZER.serialize(item)
        super(PandasDataFrameStore, self).write(arctic_lib, version, symbol, item, previous_version, dtype=md)

    def append(self, arctic_lib, version, symbol, item, previous_version):
        item, md = self.SERIALIZER.serialize(item)
        super(PandasDataFrameStore, self).append(arctic_lib, version, symbol, item, previous_version, dtype=md)

    def read(self, arctic_lib, version, symbol, **kwargs):
        item = super(PandasDataFrameStore, self).read(arctic_lib, version, symbol, **kwargs)
        return self.SERIALIZER.deserialize(item)


class PandasPanelStore(PandasDataFrameStore):
    TYPE = 'pandaspan'

    def can_write(self, version, symbol, data):
        if isinstance(data, Panel):
            frame = data.to_frame(filter_observations=False)
            if np.any(frame.dtypes.values == 'object'):
                return self.SERIALIZER.can_convert_to_records_without_objects(frame, symbol)
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
