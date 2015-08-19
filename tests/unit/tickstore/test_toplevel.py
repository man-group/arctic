from mock import Mock, patch, MagicMock, create_autospec, sentinel, call
import pytest
from datetime import datetime as dt
import pandas as pd
from pandas.util.testing import assert_frame_equal
import numpy as np
from mockextras import when

from arctic.date import DateRange, mktz
from arctic.exceptions import OverlappingDataException
from arctic.tickstore.toplevel import TopLevelTickStore, TickStoreLibrary
from dateutil.rrule import rrule, DAILY
from arctic.tickstore.tickstore import TickStore


def test_raise_exception_if_daterange_is_not_provided():
    store = TopLevelTickStore(Mock())
    with pytest.raises(Exception) as e:
        store._get_library_metadata(None)
    assert "A date range must be provided" in str(e)


def test_raise_exception_if_date_range_does_not_contain_start_date():
    store = TopLevelTickStore(Mock())
    dr = DateRange(start=None, end=dt(2011, 1, 1))
    with pytest.raises(Exception) as e:
        store._get_library_metadata(dr)
    assert "The date range {0} must contain a start and end date".format(dr) in str(e)


def test_raise_exception_if_date_range_does_not_contain_end_date():
    store = TopLevelTickStore(Mock())
    dr = DateRange(start=dt(2011, 1, 1), end=None)
    with pytest.raises(Exception) as e:
        store._get_library_metadata(dr)
    assert "The date range {0} must contain a start and end date".format(dr) in str(e)


def test_raise_exception_if_date_range_does_not_contain_start_and_end_date():
    store = TopLevelTickStore(Mock())
    dr = DateRange(start=None, end=None)
    with pytest.raises(Exception) as e:
        store._get_library_metadata(dr)
    assert "The date range {0} must contain a start and end date".format(dr) in str(e)


def test_raise_exception_and_log_an_error_if_an_invalid_library_name_is_added():
    arctic_lib = MagicMock()
    arctic_lib.arctic.__getitem__.side_effect = Exception()
    store = TopLevelTickStore(arctic_lib)
    with patch("arctic.tickstore.toplevel.logger") as mock_logger:
        with pytest.raises(Exception):
            store.add(None, "blah")
    mock_logger.error.assert_called_once_with("Could not load library")


def test_raise_exception_if_date_range_overlaps():
    self = create_autospec(TopLevelTickStore, _arctic_lib=MagicMock())
    self._get_library_metadata.return_value = [TickStoreLibrary('lib1', None), ]
    with pytest.raises(OverlappingDataException) as e:
        TopLevelTickStore.add(self, DateRange(start=dt(2010, 1, 1), end=dt(2011, 1, 1, 23, 59, 59, 999000)), "blah")
    assert "There are libraries that overlap with the date range:" in str(e)


@pytest.mark.parametrize(('start', 'end', 'expected_start', 'expected_end'),
                         [(dt(2010, 1, 1, tzinfo=mktz('UTC')), dt(2010, 12, 31, 23, 59, 59, 999000, tzinfo=mktz('UTC')),
                           dt(2010, 1, 1, tzinfo=mktz('UTC')), dt(2010, 12, 31, 23, 59, 59, 999000, tzinfo=mktz('UTC'))),
                          (dt(2010, 1, 1), dt(2010, 12, 31, 23, 59, 59, 999000), dt(2010, 1, 1, tzinfo=mktz('UTC')),
                           dt(2010, 12, 31, 23, 59, 59, 999000, tzinfo=mktz('UTC'))),
                          (dt(2009, 12, 31, 19, tzinfo=mktz('America/New_York')), dt(2010, 12, 31, 18, 59, 59, 999000, tzinfo=mktz('America/New_York')),
                           dt(2010, 1, 1, tzinfo=mktz('UTC')), dt(2010, 12, 31, 23, 59, 59, 999000, tzinfo=mktz('UTC')))
                          ])
def test_add_library_to_colllection_if_date_range_is_on_UTC_or_naive_day_boundaries(start, end, expected_start, expected_end):
    self = create_autospec(TopLevelTickStore, _arctic_lib=MagicMock(), _collection=MagicMock())
    self._get_library_metadata.return_value = []
    TopLevelTickStore.add(self, DateRange(start=start, end=end), "blah")
    self._collection.update_one.assert_called_once_with({'library_name': "blah"},
                                                        {'$set':
                                                         {'start': expected_start,
                                                          'end': expected_end}}, upsert=True)


@pytest.mark.parametrize(('start', 'end'),
                         [(dt(2010, 1, 1, 2, tzinfo=mktz('UTC')), dt(2011, 1, 1, tzinfo=mktz('UTC'))),
                          (dt(2010, 1, 1, tzinfo=mktz('UTC')), dt(2011, 1, 1, 2, tzinfo=mktz('UTC'))),
                          (dt(2010, 1, 1, 2, tzinfo=mktz('UTC')), dt(2011, 1, 1, 2, tzinfo=mktz('UTC'))),
                          (dt(2010, 1, 1, 2), dt(2011, 1, 1)),
                          (dt(2010, 1, 1), dt(2011, 1, 1, 2)),
                          (dt(2010, 1, 1, 2), dt(2011, 1, 1, 2)),
                          (dt(2009, 12, 31, 21, 10, tzinfo=mktz('America/New_York')), dt(2010, 12, 31, tzinfo=mktz('America/New_York'))),
                          (dt(2009, 12, 31, tzinfo=mktz('America/New_York')), dt(2010, 12, 31, tzinfo=mktz('America/New_York'))),
                          (dt(2009, 12, 31, 21, 10, tzinfo=mktz('America/New_York')), dt(2010, 12, 31, 9, 21, tzinfo=mktz('America/New_York')))
                          ])
def test_raise_error_add_library_is_called_with_a_date_range_not_on_day_boundaries(start, end):
    with pytest.raises(AssertionError) as e:
        self = create_autospec(TopLevelTickStore, _arctic_lib=MagicMock(), _collection=MagicMock())
        self._get_library_metadata.return_value = []
        TopLevelTickStore.add(self, DateRange(start=start, end=end), "blah")
    assert "Date range should fall on UTC day boundaries" in str(e)


@pytest.mark.parametrize(('start', 'end', 'expected_start_index', 'expected_end_index'),
                         [(dt(2010, 1, 1), dt(2010, 1, 5), 0, 3),
                          (dt(2010, 1, 1), dt(2010, 1, 6), 0, 3),
                          (dt(2010, 1, 1, 1), dt(2010, 1, 6), 1, 3),
                          (dt(2010, 1, 1, 1), dt(2010, 1, 4, 2), 1, 2),
                          (dt(2009, 1, 1), dt(2010, 1, 5), 0, 3),
                          ])
def test_slice_pandas_dataframe(start, end, expected_start_index, expected_end_index):
    top_level_tick_store = TopLevelTickStore(Mock())
    dates = pd.date_range('20100101', periods=5, freq='2D')
    data = pd.DataFrame(np.random.randn(5, 4), index=dates, columns=list('ABCD'))
    expected = data.ix[expected_start_index:expected_end_index]
    result = top_level_tick_store._slice(data, start, end)
    assert_frame_equal(expected, result), '{}\n{}'.format(expected, result)


@pytest.mark.parametrize(('start', 'end', 'expected_start_index', 'expected_end_index'),
                         [(dt(2010, 1, 1), dt(2010, 1, 5), 0, 3),
                          (dt(2010, 1, 1), dt(2010, 1, 6), 0, 3),
                          (dt(2010, 1, 1, 1), dt(2010, 1, 6), 1, 3),
                          (dt(2010, 1, 1, 1), dt(2010, 1, 4, 2), 1, 2),
                          (dt(2009, 1, 1), dt(2010, 1, 5), 0, 3),
                          ])
def test_slice_list_of_dicts(start, end, expected_start_index, expected_end_index):
    top_level_tick_store = TopLevelTickStore(Mock())
    dates = list(rrule(DAILY, count=5, dtstart=dt(2010, 1, 1), interval=2))
    data = [{'index': date, 'A': val} for date, val in zip(dates, range(5))]
    expected = data[expected_start_index:expected_end_index]
    result = top_level_tick_store._slice(data, start, end)
    assert expected == result


def test_write_pandas_data_to_right_libraries():
    self = create_autospec(TopLevelTickStore, _arctic_lib=MagicMock(), _collection=MagicMock())
    self._collection.find.return_value = [{'library_name': sentinel.libname1, 'start': sentinel.st1, 'end': sentinel.end1},
                                          {'library_name': sentinel.libname2, 'start': sentinel.st2, 'end': sentinel.end2}]
    slice1 = range(2)
    slice2 = range(4)
    when(self._slice).called_with(sentinel.data, sentinel.st1, sentinel.end1).then(slice1)
    when(self._slice).called_with(sentinel.data, sentinel.st2, sentinel.end2).then(slice2)
    mock_lib1 = Mock()
    mock_lib2 = Mock()
    when(self._arctic_lib.arctic.__getitem__).called_with(sentinel.libname1).then(mock_lib1)
    when(self._arctic_lib.arctic.__getitem__).called_with(sentinel.libname2).then(mock_lib2)
    TopLevelTickStore.write(self, 'blah', sentinel.data)
    mock_lib1.write.assert_called_once_with('blah', slice1)
    mock_lib2.write.assert_called_once_with('blah', slice2)


def test_read():
    self = create_autospec(TopLevelTickStore)
    tsl = TickStoreLibrary(create_autospec(TickStore), create_autospec(DateRange))
    self._get_libraries.return_value = [tsl, tsl]
    dr = create_autospec(DateRange)
    with patch('pandas.concat') as concat:
        res = TopLevelTickStore.read(self, sentinel.symbol, dr,
                                     columns=sentinel.include_columns,
                                     include_images=sentinel.include_images)
    assert concat.call_args_list == [call([tsl.library.read.return_value,
                                           tsl.library.read.return_value])]
    assert res == concat.return_value
    assert tsl.library.read.call_args_list == [call(sentinel.symbol, tsl.date_range.intersection.return_value,
                                                    sentinel.include_columns, include_images=sentinel.include_images),
                                               call(sentinel.symbol, tsl.date_range.intersection.return_value,
                                                    sentinel.include_columns, include_images=sentinel.include_images)]
