from datetime import datetime as dt, timedelta as dtd
from dateutil.rrule import rrule, DAILY
import pytest
import pandas as pd
from pandas.util.testing import assert_frame_equal
import numpy as np

from arctic.date import DateRange, mktz
from arctic.tickstore import toplevel
from arctic.tickstore import tickstore
from arctic.exceptions import NoDataFoundException, LibraryNotFoundException, OverlappingDataException


FEED_2010_LEVEL1 = toplevel.TickStoreLibrary('FEED_2010.LEVEL1', DateRange(dt(2010, 1, 1), dt(2010, 12, 31, 23, 59, 59)))
FEED_2011_LEVEL1 = toplevel.TickStoreLibrary('FEED_2011.LEVEL1', DateRange(dt(2011, 1, 1), dt(2011, 12, 31, 23, 59, 59)))
FEED_2012_LEVEL1 = toplevel.TickStoreLibrary('FEED_2012.LEVEL1', DateRange(dt(2012, 1, 1), dt(2012, 12, 31, 23, 59, 59)))

@pytest.mark.parametrize(('start', 'end', 'expected'),
                         [(dt(2010, 2, 1), dt(2010, 4, 1), [FEED_2010_LEVEL1]),
                          (dt(2011, 2, 1), dt(2011, 4, 1), [FEED_2011_LEVEL1]),
                          (dt(2010, 2, 1), dt(2011, 4, 1), [FEED_2010_LEVEL1, FEED_2011_LEVEL1]),
                          (dt(2011, 2, 1), dt(2012, 4, 1), [FEED_2011_LEVEL1, FEED_2012_LEVEL1]),
                          (dt(2010, 2, 1), dt(2012, 4, 1), [FEED_2010_LEVEL1, FEED_2011_LEVEL1, FEED_2012_LEVEL1]),
                          (dt(2009, 2, 1), dt(2010, 12, 31), [FEED_2010_LEVEL1]),
                          (dt(2012, 2, 1), dt(2013, 12, 31), [FEED_2012_LEVEL1]),
                          (dt(2009, 2, 1), dt(2009, 12, 31), []),
                          (dt(2013, 2, 1), dt(2013, 12, 31), []),
                          ])
def should_return_libraries_for_the_given_daterange(toplevel_tickstore, start, end, expected):
    toplevel_tickstore._collection.insert_one({'start': dt(2010, 1, 1),
                                           'end': dt(2010, 12, 31, 23, 59, 59),
                                           'library_name': 'FEED_2010.LEVEL1'})
    toplevel_tickstore._collection.insert_one({'start': dt(2011, 1, 1),
                                           'end': dt(2011, 12, 31, 23, 59, 59),
                                           'library_name': 'FEED_2011.LEVEL1'})
    toplevel_tickstore._collection.insert_one({'start': dt(2012, 1, 1),
                                           'end': dt(2012, 12, 31, 23, 59, 59),
                                           'library_name': 'FEED_2012.LEVEL1'})
    libraries = toplevel_tickstore._get_library_metadata(DateRange(start=start, end=end))
    assert libraries == expected


def should_raise_exceptions_if_no_libraries_are_found_in_the_date_range_when_reading_data(toplevel_tickstore):
    toplevel_tickstore._collection.insert_one({'start': dt(2010, 1, 1),
                                           'end': dt(2010, 12, 31, 23, 59, 59),
                                           'library_name': 'FEED_2010.LEVEL1'})
    with pytest.raises(NoDataFoundException) as e:
        toplevel_tickstore.read('blah', DateRange(start=dt(2012, 1, 1), end=dt(2012, 3, 1)))
    assert "No underlying libraries exist for the given date range" in str(e)


def should_return_data_when_date_range_falls_in_a_single_underlying_library(toplevel_tickstore, arctic):
    arctic.initialize_library('FEED_2010.LEVEL1', tickstore.TICK_STORE_TYPE)
    tickstore = arctic['FEED_2010.LEVEL1']
    arctic.initialize_library('test_current.toplevel_tickstore', tickstore.TICK_STORE_TYPE)
    tickstore_current = arctic['test_current.toplevel_tickstore']
    toplevel_tickstore._collection.insert_one({'start': dt(2010, 1, 1),
                                           'end': dt(2010, 12, 31, 23, 59, 59),
                                           'library_name': 'FEED_2010.LEVEL1'})
    dates = pd.date_range('20100101', periods=6, tz=mktz('Europe/London'))
    df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))
    tickstore.write('blah', df)
    tickstore_current.write('blah', df)
    res = toplevel_tickstore.read('blah', DateRange(start=dt(2010, 1, 1), end=dt(2010, 1, 6)), list('ABCD'))

    assert_frame_equal(df, res.tz_localize(mktz('Europe/London')))


def should_return_data_when_date_range_spans_libraries(toplevel_tickstore, arctic):
    arctic.initialize_library('FEED_2010.LEVEL1', tickstore.TICK_STORE_TYPE)
    arctic.initialize_library('FEED_2011.LEVEL1', tickstore.TICK_STORE_TYPE)
    tickstore_2010 = arctic['FEED_2010.LEVEL1']
    tickstore_2011 = arctic['FEED_2011.LEVEL1']
    toplevel_tickstore._collection.insert_one({'start': dt(2010, 1, 1),
                                           'end': dt(2010, 12, 31, 23, 59, 59),
                                           'library_name': 'FEED_2010.LEVEL1'})
    toplevel_tickstore._collection.insert_one({'start': dt(2011, 1, 1),
                                           'end': dt(2011, 12, 31, 23, 59, 59),
                                           'library_name': 'FEED_2011.LEVEL1'})
    dates = pd.date_range('20100101', periods=6, tz=mktz('Europe/London'))
    df_10 = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))
    tickstore_2010.write('blah', df_10)
    dates = pd.date_range('20110101', periods=6, tz=mktz('Europe/London'))
    df_11 = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))
    tickstore_2011.write('blah', df_11)
    res = toplevel_tickstore.read('blah', DateRange(start=dt(2010, 1, 2), end=dt(2011, 1, 4)), list('ABCD'))
    expected_df = pd.concat([df_10[1:], df_11[:4]])
    assert_frame_equal(expected_df, res.tz_localize(mktz('Europe/London')))


def should_add_underlying_library_where_none_exists(toplevel_tickstore, arctic):
    arctic.initialize_library('FEED_2010.LEVEL1', tickstore.TICK_STORE_TYPE)
    toplevel_tickstore.add(DateRange(start=dt(2010, 1, 1), end=dt(2010, 12, 31, 23, 59, 59, 999000)), 'FEED_2010.LEVEL1')
    assert toplevel_tickstore._collection.find_one({'library_name': 'FEED_2010.LEVEL1'})


def should_add_underlying_library_where_another_library_exists_in_a_non_overlapping_daterange(toplevel_tickstore, arctic):
    toplevel_tickstore._collection.insert_one({'library_name': 'FEED_2011.LEVEL1', 'start': dt(2011, 1, 1), 'end': dt(2011, 12, 31)})
    arctic.initialize_library('FEED_2010.LEVEL1', tickstore.TICK_STORE_TYPE)
    toplevel_tickstore.add(DateRange(start=dt(2010, 1, 1), end=dt(2010, 12, 31, 23, 59, 59, 999000)), 'FEED_2010.LEVEL1')
    assert set([ res['library_name'] for res in toplevel_tickstore._collection.find()]) == set(['FEED_2010.LEVEL1', 'FEED_2011.LEVEL1'])


def should_raise_exception_if_library_does_not_exist(toplevel_tickstore):
    with pytest.raises(LibraryNotFoundException) as e:
        toplevel_tickstore.add(DateRange(start=dt(2010, 1, 1), end=dt(2010, 12, 31, 23, 59, 59, 999000)), 'FEED_2010.LEVEL1')
        assert toplevel_tickstore._collection.find_one({'library_name': 'FEED_2010.LEVEL1'})
    assert "Library FEED_2010.LEVEL1 was not correctly initialized" in str(e)


def should_raise_exception_if_date_range_for_library_overlaps_with_existing_libraries(toplevel_tickstore, arctic):
    toplevel_tickstore._collection.insert_one({'library_name': 'FEED_2010.LEVEL1', 'start': dt(2010, 1, 1), 'end': dt(2010, 6, 30)})
    arctic.initialize_library('FEED_2010a.LEVEL1', tickstore.TICK_STORE_TYPE)
    with pytest.raises(OverlappingDataException) as e:
        toplevel_tickstore.add(DateRange(start=dt(2010, 6, 1), end=dt(2010, 12, 31, 23, 59, 59, 999000)), 'FEED_2010a.LEVEL1')
        assert toplevel_tickstore._collection.find_one({'library_name': 'FEED_2010.LEVEL1'})
    assert "There are libraries that overlap with the date range:" in str(e)


def should_successfully_do_a_roundtrip_write_and_read_spanning_multiple_underlying_libraries(toplevel_tickstore, arctic):
    arctic.initialize_library('FEED_2010.LEVEL1', tickstore.TICK_STORE_TYPE)
    arctic.initialize_library('FEED_2011.LEVEL1', tickstore.TICK_STORE_TYPE)
    arctic.initialize_library('test_current.toplevel_tickstore', tickstore.TICK_STORE_TYPE)
    toplevel_tickstore.add(DateRange(start=dt(2010, 1, 1), end=dt(2010, 12, 31, 23, 59, 59, 999000)), 'FEED_2010.LEVEL1')
    toplevel_tickstore.add(DateRange(start=dt(2011, 1, 1), end=dt(2011, 12, 31, 23, 59, 59, 999000)), 'FEED_2011.LEVEL1')
    tickstore_current = arctic['test_current.toplevel_tickstore']
    dates = pd.date_range('20101201', periods=57, tz=mktz('Europe/London'))
    data = pd.DataFrame(np.random.randn(57, 4), index=dates, columns=list('ABCD'))
    toplevel_tickstore.write('blah', data)
    tickstore_current.write('blah', data)
    res = toplevel_tickstore.read('blah', DateRange(start=dt(2010, 12, 1), end=dt(2011, 2, 1)), columns=list('ABCD'))
    assert_frame_equal(data, res.tz_localize(mktz('Europe/London')))
    lib2010 = arctic['FEED_2010.LEVEL1']
    res = lib2010.read('blah', DateRange(start=dt(2010, 12, 1), end=dt(2011, 1, 1)), columns=list('ABCD'))
    assert_frame_equal(data[dt(2010, 12, 1): dt(2010, 12, 31)], res.tz_localize(mktz('Europe/London')))
    lib2011 = arctic['FEED_2011.LEVEL1']
    res = lib2011.read('blah', DateRange(start=dt(2011, 1, 1), end=dt(2011, 2, 1)), columns=list('ABCD'))
    assert_frame_equal(data[dt(2011, 1, 1): dt(2011, 2, 1)], res.tz_localize(mktz('Europe/London')))


@pytest.mark.parametrize(('start', 'end', 'startr', 'endr'),
                         [(dt(2010, 1, 1), dt(2011, 12, 31), 0, 10),
                          (dt(2010, 1, 1), dt(2010, 12, 31), 0, 8),
                          (dt(2011, 1, 1), dt(2011, 12, 31), 7, 10),
                          ])
def should_list_symbols_from_the_underlying_library(toplevel_tickstore, arctic, start, end, startr, endr):
    arctic.initialize_library('FEED_2010.LEVEL1', tickstore.TICK_STORE_TYPE)
    arctic.initialize_library('FEED_2011.LEVEL1', tickstore.TICK_STORE_TYPE)
    toplevel_tickstore.add(DateRange(start=dt(2010, 1, 1), end=dt(2010, 12, 31, 23, 59, 59, 999000)), 'FEED_2010.LEVEL1')
    toplevel_tickstore.add(DateRange(start=dt(2011, 1, 1), end=dt(2011, 12, 31, 23, 59, 59, 999000)), 'FEED_2011.LEVEL1')
    dtstart = dt(2010, 1, 1, tzinfo=mktz('Europe/London'))
    for i in range(10):
        dates = pd.date_range(dtstart, periods=50, tz=mktz('Europe/London'))
        df = pd.DataFrame(np.random.randn(50, 4), index=dates, columns=list('ABCD'))
        dtstart = dates[-1] + dtd(days=1)
        toplevel_tickstore.write('sym' + str(i), df)
    expected_symbols = ['sym' + str(i) for i in range(startr, endr)]
    assert expected_symbols == toplevel_tickstore.list_symbols(DateRange(start=start, end=end))


def should_add_underlying_libraries_when_intialized(arctic):
    arctic.initialize_library('FEED_2010.LEVEL1', tickstore.TICK_STORE_TYPE)
    arctic.initialize_library('FEED_2011.LEVEL1', tickstore.TICK_STORE_TYPE)
    arctic.initialize_library('FEED.LEVEL1', toplevel.TICK_STORE_TYPE)
    toplevel_tickstore = arctic['FEED.LEVEL1']
    cur = toplevel_tickstore._collection.find(projection={'_id': 0})
    results = {result['library_name']: {'start': result['start'], 'end': result['end']} for result in cur}
    expected_results = {'FEED_2010.LEVEL1': {'start': dt(2010, 1, 1), 'end': dt(2010, 12, 31, 23, 59, 59, 999000)},
                        'FEED_2011.LEVEL1': {'start': dt(2011, 1, 1), 'end': dt(2011, 12, 31, 23, 59, 59, 999000)}}
    assert expected_results == results
