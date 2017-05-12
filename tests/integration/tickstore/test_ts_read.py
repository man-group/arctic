from datetime import datetime as dt
from mock import patch, call, Mock
import numpy as np
from numpy.testing.utils import assert_array_equal
from pandas.util.testing import assert_frame_equal
import pandas as pd
from pandas import DatetimeIndex
from pymongo import ReadPreference
import pytest
import pytz

from arctic.date import DateRange, mktz, CLOSED_CLOSED, CLOSED_OPEN, OPEN_CLOSED, OPEN_OPEN
from arctic.exceptions import NoDataFoundException


def test_read(tickstore_lib):
    data = [{'ASK': 1545.25,
                  'ASKSIZE': 1002.0,
                  'BID': 1545.0,
                  'BIDSIZE': 55.0,
                  'CUMVOL': 2187387.0,
                  'DELETED_TIME': 0,
                  'INSTRTYPE': 'FUT',
                  'PRICE': 1545.0,
                  'SIZE': 1.0,
                  'TICK_STATUS': 0,
                  'TRADEHIGH': 1561.75,
                  'TRADELOW': 1537.25,
                  'index': 1185076787070},
                 {'CUMVOL': 354.0,
                  'DELETED_TIME': 0,
                  'PRICE': 1543.75,
                  'SIZE': 354.0,
                  'TRADEHIGH': 1543.75,
                  'TRADELOW': 1543.75,
                  'index': 1185141600600}]
    tickstore_lib.write('FEED::SYMBOL', data)

    df = tickstore_lib.read('FEED::SYMBOL', columns=['BID', 'ASK', 'PRICE'])

    assert_array_equal(df['ASK'].values, np.array([1545.25, np.nan]))
    assert_array_equal(df['BID'].values, np.array([1545, np.nan]))
    assert_array_equal(df['PRICE'].values, np.array([1545, 1543.75]))
    assert_array_equal(df.index.values.astype('object'), np.array([1185076787070000000, 1185141600600000000]))
    assert tickstore_lib._collection.find_one()['c'] == 2


def test_read_allow_secondary(tickstore_lib):
    data = [{'ASK': 1545.25,
                  'ASKSIZE': 1002.0,
                  'BID': 1545.0,
                  'BIDSIZE': 55.0,
                  'CUMVOL': 2187387.0,
                  'DELETED_TIME': 0,
                  'INSTRTYPE': 'FUT',
                  'PRICE': 1545.0,
                  'SIZE': 1.0,
                  'TICK_STATUS': 0,
                  'TRADEHIGH': 1561.75,
                  'TRADELOW': 1537.25,
                  'index': 1185076787070},
                 {'CUMVOL': 354.0,
                  'DELETED_TIME': 0,
                  'PRICE': 1543.75,
                  'SIZE': 354.0,
                  'TRADEHIGH': 1543.75,
                  'TRADELOW': 1543.75,
                  'index': 1185141600600}]
    tickstore_lib.write('FEED::SYMBOL', data)


    with patch('pymongo.collection.Collection.find', side_effect=tickstore_lib._collection.find) as find:
        with patch('pymongo.collection.Collection.with_options', side_effect=tickstore_lib._collection.with_options) as with_options:
            with patch.object(tickstore_lib, '_read_preference', side_effect=tickstore_lib._read_preference) as read_pref:
                df = tickstore_lib.read('FEED::SYMBOL', columns=['BID', 'ASK', 'PRICE'], allow_secondary=True)
    assert read_pref.call_args_list == [call(True)]
    assert with_options.call_args_list == [call(read_preference=ReadPreference.NEAREST)]
    assert find.call_args_list == [call({'sy': 'FEED::SYMBOL'}, sort=[('s', 1)], projection={'s': 1, '_id': 0}),
                                   call({'sy': 'FEED::SYMBOL', 's': {'$lte': dt(2007, 8, 21, 3, 59, 47, 70000)}}, 
                                        projection={'sy': 1, 'cs.PRICE': 1, 'i': 1, 'cs.BID': 1, 's': 1, 'im': 1, 'v': 1, 'cs.ASK': 1})]

    assert_array_equal(df['ASK'].values, np.array([1545.25, np.nan]))
    assert tickstore_lib._collection.find_one()['c'] == 2


def test_read_symbol_as_column(tickstore_lib):
    data = [{'ASK': 1545.25,
             'index': 1185076787070},
            {'CUMVOL': 354.0,
             'index': 1185141600600}]
    tickstore_lib.write('FEED::SYMBOL', data)

    df = tickstore_lib.read('FEED::SYMBOL', columns=['SYMBOL', 'CUMVOL'])
    assert all(df['SYMBOL'].values == ['FEED::SYMBOL'])


def test_read_multiple_symbols(tickstore_lib):
    data1 = [{'ASK': 1545.25,
                  'ASKSIZE': 1002.0,
                  'BID': 1545.0,
                  'BIDSIZE': 55.0,
                  'CUMVOL': 2187387.0,
                  'DELETED_TIME': 0,
                  'INSTRTYPE': 'FUT',
                  'PRICE': 1545.0,
                  'SIZE': 1.0,
                  'TICK_STATUS': 0,
                  'TRADEHIGH': 1561.75,
                  'TRADELOW': 1537.25,
                  'index': 1185076787070}, ]
    data2 = [{'CUMVOL': 354.0,
                  'DELETED_TIME': 0,
                  'PRICE': 1543.75,
                  'SIZE': 354.0,
                  'TRADEHIGH': 1543.75,
                  'TRADELOW': 1543.75,
                  'index': 1185141600600}]

    tickstore_lib.write('BAR', data2)
    tickstore_lib.write('FOO', data1)

    df = tickstore_lib.read(['FOO', 'BAR'], columns=['BID', 'ASK', 'PRICE'])

    assert all(df['SYMBOL'].values == ['FOO', 'BAR'])
    assert_array_equal(df['ASK'].values, np.array([1545.25, np.nan]))
    assert_array_equal(df['BID'].values, np.array([1545, np.nan]))
    assert_array_equal(df['PRICE'].values, np.array([1545, 1543.75]))
    assert_array_equal(df.index.values.astype('object'), np.array([1185076787070000000, 1185141600600000000]))
    assert tickstore_lib._collection.find_one()['c'] == 1



@pytest.mark.parametrize('chunk_size', [1, 100])
def test_read_all_cols_all_dtypes(tickstore_lib, chunk_size):
    data = [{'f': 0.1,
            'of': 0.2,
            's': 's',
            'os': 'os',
            'l': 1,
            'ol': 2,
            'index': dt(1970, 1, 1, tzinfo=mktz('UTC')),
            },
            {'f': 0.3,
            'nf': 0.4,
            's': 't',
            'ns': 'ns',
            'l': 3,
            'nl': 4,
            'index': dt(1970, 1, 1, 0, 0, 1, tzinfo=mktz('UTC')),
            },
            ]
    tickstore_lib._chunk_size = chunk_size
    tickstore_lib.write('sym', data)
    df = tickstore_lib.read('sym', columns=None)

    # The below is probably more trouble than it's worth, but we *should*
    # be able to roundtrip data and get the same answer...

    # Ints become floats
    data[0]['l'] = float(data[0]['l'])
    # Treat missing strings as None
    data[0]['ns'] = None
    data[1]['os'] = None
    index = DatetimeIndex([dt(1970, 1, 1, tzinfo=mktz('UTC')),
                         dt(1970, 1, 1, 0, 0, 1, tzinfo=mktz('UTC'))],
                        )
    index.tz = mktz()
    expected = pd.DataFrame(data, index=index)
    expected = expected[df.columns]
    assert_frame_equal(expected, df, check_names=False)


DUMMY_DATA = [
              {'a': 1.,
               'b': 2.,
               'index': dt(2013, 1, 1, tzinfo=mktz('Europe/London'))
               },
              {'b': 3.,
               'c': 4.,
               'index': dt(2013, 1, 2, tzinfo=mktz('Europe/London'))
               },
              {'b': 5.,
               'c': 6.,
               'index': dt(2013, 1, 3, tzinfo=mktz('Europe/London'))
               },
              {'b': 7.,
               'c': 8.,
               'index': dt(2013, 1, 4, tzinfo=mktz('Europe/London'))
               },
              {'b': 9.,
               'c': 10.,
               'index': dt(2013, 1, 5, tzinfo=mktz('Europe/London'))
               },
              ]


def test_date_range(tickstore_lib):
    tickstore_lib.write('SYM', DUMMY_DATA)
    df = tickstore_lib.read('SYM', date_range=DateRange(20130101, 20130103), columns=None)
    assert_array_equal(df['a'].values, np.array([1, np.nan, np.nan]))
    assert_array_equal(df['b'].values, np.array([2., 3., 5.]))
    assert_array_equal(df['c'].values, np.array([np.nan, 4., 6.]))

    tickstore_lib.delete('SYM')

    # Chunk every 3 symbols and lets have some fun
    tickstore_lib._chunk_size = 3
    tickstore_lib.write('SYM', DUMMY_DATA)

    with patch('pymongo.collection.Collection.find', side_effect=tickstore_lib._collection.find) as f:
        df = tickstore_lib.read('SYM', date_range=DateRange(20130101, 20130103), columns=None)
        assert_array_equal(df['b'].values, np.array([2., 3., 5.]))
        assert tickstore_lib._collection.find(f.call_args_list[-1][0][0]).count() == 1
        df = tickstore_lib.read('SYM', date_range=DateRange(20130102, 20130103), columns=None)
        assert_array_equal(df['b'].values, np.array([3., 5.]))
        assert tickstore_lib._collection.find(f.call_args_list[-1][0][0]).count() == 1
        df = tickstore_lib.read('SYM', date_range=DateRange(20130103, 20130103), columns=None)
        assert_array_equal(df['b'].values, np.array([5.]))
        assert tickstore_lib._collection.find(f.call_args_list[-1][0][0]).count() == 1

        df = tickstore_lib.read('SYM', date_range=DateRange(20130102, 20130104), columns=None)
        assert_array_equal(df['b'].values, np.array([3., 5., 7.]))
        assert tickstore_lib._collection.find(f.call_args_list[-1][0][0]).count() == 2
        df = tickstore_lib.read('SYM', date_range=DateRange(20130102, 20130105), columns=None)
        assert_array_equal(df['b'].values, np.array([3., 5., 7., 9.]))
        assert tickstore_lib._collection.find(f.call_args_list[-1][0][0]).count() == 2

        df = tickstore_lib.read('SYM', date_range=DateRange(20130103, 20130104), columns=None)
        assert_array_equal(df['b'].values, np.array([5., 7.]))
        assert tickstore_lib._collection.find(f.call_args_list[-1][0][0]).count() == 2
        df = tickstore_lib.read('SYM', date_range=DateRange(20130103, 20130105), columns=None)
        assert_array_equal(df['b'].values, np.array([5., 7., 9.]))
        assert tickstore_lib._collection.find(f.call_args_list[-1][0][0]).count() == 2

        df = tickstore_lib.read('SYM', date_range=DateRange(20130104, 20130105), columns=None)
        assert_array_equal(df['b'].values, np.array([7., 9.]))
        assert tickstore_lib._collection.find(f.call_args_list[-1][0][0]).count() == 1

        # Test the different open-closed behaviours
        df = tickstore_lib.read('SYM', date_range=DateRange(20130104, 20130105, CLOSED_CLOSED), columns=None)
        assert_array_equal(df['b'].values, np.array([7., 9.]))
        df = tickstore_lib.read('SYM', date_range=DateRange(20130104, 20130105, CLOSED_OPEN), columns=None)
        assert_array_equal(df['b'].values, np.array([7.]))
        df = tickstore_lib.read('SYM', date_range=DateRange(20130104, 20130105, OPEN_CLOSED), columns=None)
        assert_array_equal(df['b'].values, np.array([9.]))
        df = tickstore_lib.read('SYM', date_range=DateRange(20130104, 20130105, OPEN_OPEN), columns=None)
        assert_array_equal(df['b'].values, np.array([]))


def test_date_range_end_not_in_range(tickstore_lib):
    DUMMY_DATA = [
                  {'a': 1.,
                   'b': 2.,
                   'index': dt(2013, 1, 1, tzinfo=mktz('Europe/London'))
                   },
                  {'b': 3.,
                   'c': 4.,
                   'index': dt(2013, 1, 2, 10, 1, tzinfo=mktz('Europe/London'))
                   },
                  ]

    tickstore_lib._chunk_size = 1
    tickstore_lib.write('SYM', DUMMY_DATA)
    with patch.object(tickstore_lib._collection, 'find', side_effect=tickstore_lib._collection.find) as f:
        df = tickstore_lib.read('SYM', date_range=DateRange(20130101, dt(2013, 1, 2, 9, 0)), columns=None)
        assert_array_equal(df['b'].values, np.array([2.]))
        assert tickstore_lib._collection.find(f.call_args_list[-1][0][0]).count() == 1


@pytest.mark.parametrize('tz_name', ['UTC',
                                     'Europe/London',  # Sometimes ahead of UTC
                                     'America/New_York',  # Behind UTC
                                      ])
def test_date_range_default_timezone(tickstore_lib, tz_name):
    """
    We assume naive datetimes are user-local
    """
    DUMMY_DATA = [
                  {'a': 1.,
                   'b': 2.,
                   'index': dt(2013, 1, 1, tzinfo=mktz(tz_name))
                   },
                  # Half-way through the year
                  {'b': 3.,
                   'c': 4.,
                   'index': dt(2013, 7, 1, tzinfo=mktz(tz_name))
                   },
                  ]

    with patch('tzlocal.get_localzone', return_value=Mock(zone=tz_name)):
        tickstore_lib._chunk_size = 1
        tickstore_lib.write('SYM', DUMMY_DATA)
        df = tickstore_lib.read('SYM', date_range=DateRange(20130101, 20130701), columns=None)
        assert len(df) == 2
        assert df.index[1] == dt(2013, 7, 1, tzinfo=mktz(tz_name))
        assert df.index.tz == mktz(tz_name)

        df = tickstore_lib.read('SYM', date_range=DateRange(20130101, 20130101), columns=None)
        assert len(df) == 1

        df = tickstore_lib.read('SYM', date_range=DateRange(20130701, 20130701), columns=None)
        assert len(df) == 1


def test_date_range_no_bounds(tickstore_lib):
    DUMMY_DATA = [
                  {'a': 1.,
                   'b': 2.,
                   'index': dt(2013, 1, 1, tzinfo=mktz('Europe/London'))
                   },
                  {'a': 3.,
                   'b': 4.,
                   'index': dt(2013, 1, 30, tzinfo=mktz('Europe/London'))
                   },
                  {'b': 5.,
                   'c': 6.,
                   'index': dt(2013, 2, 2, 10, 1, tzinfo=mktz('Europe/London'))
                   },
                  ]

    tickstore_lib._chunk_size = 1
    tickstore_lib.write('SYM', DUMMY_DATA)

    # 1) No start, no end
    df = tickstore_lib.read('SYM', columns=None)
    assert_array_equal(df['b'].values, np.array([2., 4.]))
    # 1.2) Start before the real start
    df = tickstore_lib.read('SYM', date_range=DateRange(20121231), columns=None)
    assert_array_equal(df['b'].values, np.array([2., 4.]))
    # 2.1) Only go one month out
    df = tickstore_lib.read('SYM', date_range=DateRange(20130101), columns=None)
    assert_array_equal(df['b'].values, np.array([2., 4.]))
    # 2.2) Only go one month out
    df = tickstore_lib.read('SYM', date_range=DateRange(20130102), columns=None)
    assert_array_equal(df['b'].values, np.array([4.]))
    # 3) No start
    df = tickstore_lib.read('SYM', date_range=DateRange(end=20130102), columns=None)
    assert_array_equal(df['b'].values, np.array([2.]))
    # 4) Outside bounds
    df = tickstore_lib.read('SYM', date_range=DateRange(end=20131212), columns=None)
    assert_array_equal(df['b'].values, np.array([2., 4., 5.]))


def test_date_range_BST(tickstore_lib):
    DUMMY_DATA = [
                  {'a': 1.,
                   'b': 2.,
                   'index': dt(2013, 6, 1, 12, 00, tzinfo=mktz('Europe/London'))
                   },
                  {'a': 3.,
                   'b': 4.,
                   'index': dt(2013, 6, 1, 13, 00, tzinfo=mktz('Europe/London'))
                   },
                  ]
    tickstore_lib._chunk_size = 1
    tickstore_lib.write('SYM', DUMMY_DATA)

    df = tickstore_lib.read('SYM', columns=None)
    assert_array_equal(df['b'].values, np.array([2., 4.]))

#     df = tickstore_lib.read('SYM', columns=None, date_range=DateRange(dt(2013, 6, 1, 12),
#                                                                       dt(2013, 6, 1, 13)))
#     assert_array_equal(df['b'].values, np.array([2., 4.]))
    df = tickstore_lib.read('SYM', columns=None, date_range=DateRange(dt(2013, 6, 1, 12, tzinfo=mktz('Europe/London')),
                                                                            dt(2013, 6, 1, 13, tzinfo=mktz('Europe/London'))))
    assert_array_equal(df['b'].values, np.array([2., 4.]))

    df = tickstore_lib.read('SYM', columns=None, date_range=DateRange(dt(2013, 6, 1, 12, tzinfo=mktz('UTC')),
                                                                            dt(2013, 6, 1, 13, tzinfo=mktz('UTC'))))
    assert_array_equal(df['b'].values, np.array([4., ]))


def test_read_no_data(tickstore_lib):
    with pytest.raises(NoDataFoundException):
        tickstore_lib.read('missing_sym', DateRange(20131212, 20131212))


def test_write_no_tz(tickstore_lib):
    DUMMY_DATA = [
                  {'a': 1.,
                   'b': 2.,
                   'index': dt(2013, 6, 1, 12, 00)
                   }]
    with pytest.raises(ValueError):
        tickstore_lib.write('SYM', DUMMY_DATA)


def test_read_out_of_order(tickstore_lib):
    data = [{'A': 120, 'D': 1}, {'A': 122, 'B': 2.0}, {'A': 3, 'B': 3.0, 'D': 1}]
    tick_index = [dt(2013, 6, 1, 12, 00, tzinfo=mktz('UTC')),
                  dt(2013, 6, 1, 11, 00, tzinfo=mktz('UTC')),  # Out-of-order
                  dt(2013, 6, 1, 13, 00, tzinfo=mktz('UTC'))]
    data = pd.DataFrame(data, index=tick_index)

    tickstore_lib._chunk_size = 3
    tickstore_lib.write('SYM', data)
    tickstore_lib.read('SYM', columns=None)
    assert len(tickstore_lib.read('SYM', columns=None, date_range=DateRange(dt(2013, 6, 1, tzinfo=mktz('UTC')), dt(2013, 6, 2, tzinfo=mktz('UTC'))))) == 3
    assert len(tickstore_lib.read('SYM', columns=None, date_range=DateRange(dt(2013, 6, 1, tzinfo=mktz('UTC')), dt(2013, 6, 1, 12, tzinfo=mktz('UTC'))))) == 2


def test_read_chunk_boundaries(tickstore_lib):
    SYM1_DATA = [
                  {'a': 1.,
                   'b': 2.,
                   'index': dt(2013, 6, 1, 12, 00, tzinfo=mktz('UTC'))
                   },
                   {'a': 3.,
                   'b': 4.,
                   'index': dt(2013, 6, 1, 13, 00, tzinfo=mktz('UTC'))
                   },
                 # Chunk boundary here
                   {'a': 5.,
                   'b': 6.,
                   'index': dt(2013, 6, 1, 14, 00, tzinfo=mktz('UTC'))
                   }
                  ]
    SYM2_DATA = [
                  {'a': 7.,
                   'b': 8.,
                   'index': dt(2013, 6, 1, 12, 30, tzinfo=mktz('UTC'))
                   },
                   {'a': 9.,
                   'b': 10.,
                   'index': dt(2013, 6, 1, 13, 30, tzinfo=mktz('UTC'))
                   },
                 # Chunk boundary here
                   {'a': 11.,
                   'b': 12.,
                   'index': dt(2013, 6, 1, 14, 30, tzinfo=mktz('UTC'))
                   }
                  ]
    tickstore_lib._chunk_size = 2
    tickstore_lib.write('SYM1', SYM1_DATA)
    tickstore_lib.write('SYM2', SYM2_DATA)

    assert len(tickstore_lib.read('SYM1', columns=None, date_range=DateRange(dt(2013, 6, 1, 12, 45, tzinfo=mktz('UTC')), dt(2013, 6, 1, 15, 00, tzinfo=mktz('UTC'))))) == 2
    assert len(tickstore_lib.read('SYM2', columns=None, date_range=DateRange(dt(2013, 6, 1, 12, 45, tzinfo=mktz('UTC')), dt(2013, 6, 1, 15, 00, tzinfo=mktz('UTC'))))) == 2

    assert len(tickstore_lib.read(['SYM1', 'SYM2'], columns=None, date_range=DateRange(dt(2013, 6, 1, 12, 45, tzinfo=mktz('UTC')), dt(2013, 6, 1, 15, 00, tzinfo=mktz('UTC'))))) == 4


def test_read_spanning_chunks(tickstore_lib):
    SYM1_DATA = [
              {'a': 1.,
               'b': 2.,
               'index': dt(2013, 6, 1, 11, 00, tzinfo=mktz('UTC'))
               },
               {'a': 3.,
               'b': 4.,
               'index': dt(2013, 6, 1, 12, 00, tzinfo=mktz('UTC'))
               },
             # Chunk boundary here
               {'a': 5.,
               'b': 6.,
               'index': dt(2013, 6, 1, 14, 00, tzinfo=mktz('UTC'))
               }
              ]
    SYM2_DATA = [
                  {'a': 7.,
                   'b': 8.,
                   'index': dt(2013, 6, 1, 12, 30, tzinfo=mktz('UTC'))
                   },
                   {'a': 9.,
                   'b': 10.,
                   'index': dt(2013, 6, 1, 13, 30, tzinfo=mktz('UTC'))
                   },
                 # Chunk boundary here
                   {'a': 11.,
                   'b': 12.,
                   'index': dt(2013, 6, 1, 14, 30, tzinfo=mktz('UTC'))
                   }
                  ]
    tickstore_lib._chunk_size = 2
    tickstore_lib.write('SYM1', SYM1_DATA)
    tickstore_lib.write('SYM2', SYM2_DATA)
    
    # Even though the latest chunk that's the closest to the start point for SYM1 starts at 11:00, it ends before the start point,
    # so we want to ignore it and start from SYM2 (12:30) instead.
    assert tickstore_lib._mongo_date_range_query(
                                                 ['SYM1', 'SYM2'],
                                                 date_range=DateRange(dt(2013, 6, 1, 12, 45, tzinfo=mktz('UTC')),
                                                                      dt(2013, 6, 1, 15, 00, tzinfo=mktz('UTC')))) == \
        {'s': {'$gte': dt(2013, 6, 1, 12, 30, tzinfo=mktz('UTC')), '$lte': dt(2013, 6, 1, 15, 0, tzinfo=mktz('UTC'))}}


def test_read_inside_range(tickstore_lib):
    SYM1_DATA = [
              {'a': 1.,
               'b': 2.,
               'index': dt(2013, 6, 1, 0, 00, tzinfo=mktz('UTC'))
               },
               {'a': 3.,
               'b': 4.,
               'index': dt(2013, 6, 1, 1, 00, tzinfo=mktz('UTC'))
               },
             # Chunk boundary here
               {'a': 5.,
               'b': 6.,
               'index': dt(2013, 6, 1, 14, 00, tzinfo=mktz('UTC'))
               }
              ]
    SYM2_DATA = [
                  {'a': 7.,
                   'b': 8.,
                   'index': dt(2013, 6, 1, 12, 30, tzinfo=mktz('UTC'))
                   },
                   {'a': 9.,
                   'b': 10.,
                   'index': dt(2013, 6, 1, 13, 30, tzinfo=mktz('UTC'))
                   },
                 # Chunk boundary here
                   {'a': 11.,
                   'b': 12.,
                   'index': dt(2013, 6, 1, 14, 30, tzinfo=mktz('UTC'))
                   }
                  ]
    tickstore_lib._chunk_size = 2
    tickstore_lib.write('SYM1', SYM1_DATA)
    tickstore_lib.write('SYM2', SYM2_DATA)

    # If there are no chunks spanning the range, we still cap the start range so that we don't
    # fetch SYM1's 0am--1am chunk
    assert tickstore_lib._mongo_date_range_query(
                                                 ['SYM1', 'SYM2'],
                                                 date_range=DateRange(dt(2013, 6, 1, 10, 0, tzinfo=mktz('UTC')),
                                                                      dt(2013, 6, 1, 15, 0, tzinfo=mktz('UTC')))) == \
        {'s': {'$gte': dt(2013, 6, 1, 10, 0, tzinfo=mktz('UTC')), '$lte': dt(2013, 6, 1, 15, 0, tzinfo=mktz('UTC'))}}

def test_read_longs(tickstore_lib):
    DUMMY_DATA = [
                  {'a': 1,
                   'index': dt(2013, 6, 1, 12, 00, tzinfo=mktz('Europe/London'))
                   },
                  {
                   'b': 4,
                   'index': dt(2013, 6, 1, 13, 00, tzinfo=mktz('Europe/London'))
                   },
                  ]
    tickstore_lib._chunk_size = 3
    tickstore_lib.write('SYM', DUMMY_DATA)
    tickstore_lib.read('SYM', columns=None)
    read = tickstore_lib.read('SYM', columns=None, date_range=DateRange(dt(2013, 6, 1), dt(2013, 6, 2)))
    assert read['a'][0] == 1
    assert np.isnan(read['b'][0])


def test_read_with_image(tickstore_lib):
    DUMMY_DATA = [
              {'a': 1.,
               'index': dt(2013, 1, 1, 11, 00, tzinfo=mktz('Europe/London'))
               },
              {
               'b': 4.,
               'index': dt(2013, 1, 1, 12, 00, tzinfo=mktz('Europe/London'))
               },
              ]
    # Add an image
    tickstore_lib.write('SYM', DUMMY_DATA)
    tickstore_lib._collection.update_one({},
                                     {'$set':
                                      {'im': {'i':
                                              {'a': 37.,
                                               'c': 2.,
                                               },
                                              't': dt(2013, 1, 1, 10, tzinfo=mktz('Europe/London'))
                                              }
                                       }
                                      }
                                     )

    dr = DateRange(dt(2013, 1, 1), dt(2013, 1, 2))
    # tickstore_lib.read('SYM', columns=None)
    df = tickstore_lib.read('SYM', columns=None, date_range=dr)
    assert df['a'][0] == 1

    # Read with the image as well - all columns
    df = tickstore_lib.read('SYM', columns=None, date_range=dr, include_images=True)
    assert set(df.columns) == set(('a', 'b', 'c'))
    assert_array_equal(df['a'].values, np.array([37, 1, np.nan]))
    assert_array_equal(df['b'].values, np.array([np.nan, np.nan, 4]))
    assert_array_equal(df['c'].values, np.array([2, np.nan, np.nan]))
    assert df.index[0] == dt(2013, 1, 1, 10, tzinfo=mktz('Europe/London'))
    assert df.index[1] == dt(2013, 1, 1, 11, tzinfo=mktz('Europe/London'))
    assert df.index[2] == dt(2013, 1, 1, 12, tzinfo=mktz('Europe/London'))

    # Read just columns from the updates
    df = tickstore_lib.read('SYM', columns=('a', 'b'), date_range=dr, include_images=True)
    assert set(df.columns) == set(('a', 'b'))
    assert_array_equal(df['a'].values, np.array([37, 1, np.nan]))
    assert_array_equal(df['b'].values, np.array([np.nan, np.nan, 4]))
    assert df.index[0] == dt(2013, 1, 1, 10, tzinfo=mktz('Europe/London'))
    assert df.index[1] == dt(2013, 1, 1, 11, tzinfo=mktz('Europe/London'))
    assert df.index[2] == dt(2013, 1, 1, 12, tzinfo=mktz('Europe/London'))
    
    # Read one column from the updates
    df = tickstore_lib.read('SYM', columns=('a',), date_range=dr, include_images=True)
    assert set(df.columns) == set(('a',))
    assert_array_equal(df['a'].values, np.array([37, 1]))
    assert df.index[0] == dt(2013, 1, 1, 10, tzinfo=mktz('Europe/London'))
    assert df.index[1] == dt(2013, 1, 1, 11, tzinfo=mktz('Europe/London'))

    # Read just the image column
    df = tickstore_lib.read('SYM', columns=['c'], date_range=dr, include_images=True)
    assert set(df.columns) == set(['c'])
    assert_array_equal(df['c'].values, np.array([2]))
    assert df.index[0] == dt(2013, 1, 1, 10, tzinfo=mktz('Europe/London'))
