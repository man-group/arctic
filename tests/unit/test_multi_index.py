from datetime import timedelta
import itertools

from pandas.tseries.tools import to_datetime as dt
from pandas.util.testing import assert_frame_equal

from arctic.multi_index import groupby_asof, fancy_group_by, insert_at
import numpy as np
import pandas as pd
from tests.util import read_str_as_pandas
import pytest


def get_bitemporal_test_data():
    # Create an index of 8 sample dates, 2 rows per date
    sample_dates = pd.date_range('1/1/2014', periods=4, freq='D')
    sample_dates = pd.DatetimeIndex(data=sorted(itertools.chain(sample_dates, sample_dates)))

    # Create a list of insert dates. These are a year later than sample date, to show
    # that they don't necessarily have to be related
    insert_dates = pd.date_range('1/1/2015', periods=8, freq='D')

    # Build the bitemporal index
    index = pd.MultiIndex.from_arrays([sample_dates, insert_dates], names=['sample_dt', 'observed_dt'])

    # Create the dataframe with a couple of column, each value incrementing by 0.1 on the successive updates so
    # we can tell them apart
    prices = [[1.0, 10.0],
              [1.1, 10.1],
              [2.0, 20.0],
              [2.1, 20.1],
              [3.0, 30.0],
              [3.1, 30.1],
              [4.0, 40.0],
              [4.1, 40.1]]

    df = pd.DataFrame(prices, index=index, columns=['OPEN', 'CLOSE'])

    #                         OPEN  CLOSE
    # sample_dt  observed_dt
    # 2014-01-01 2015-01-01   1.0   10.0
    #            2015-01-02   1.1   10.1
    # 2014-01-02 2015-01-03   2.0   20.0
    #            2015-01-04   2.1   20.1
    # 2014-01-03 2015-01-05   3.0   30.0
    #            2015-01-06   3.1   30.1
    # 2014-01-04 2015-01-07   4.0   40.0
    #            2015-01-08   4.1   40.1
    return df


def test__can_create_df_with_multiple_index():
    """ I can make a Pandas DF with an multi-index on sampled_dt and observed_dt
    """
    df = get_bitemporal_test_data()

    # Our index has 2 levels
    assert df.index.names == ['sample_dt', 'observed_dt']
    assert all(df.columns == ['OPEN', 'CLOSE'])

    # We should have 8 rows
    assert len(df) == 8

    # .. or 4, when we only count sample date
    assert len(df.groupby(level='sample_dt').sum()) == 4


def test__get_ts__asof_latest():
    """ I can get the latest known value for each sample date
    """
    df = groupby_asof(get_bitemporal_test_data())
    assert len(df) == 4
    assert all(df['OPEN'] == [1.1, 2.1, 3.1, 4.1])
    assert all(df['CLOSE'] == [10.1, 20.1, 30.1, 40.1])


def test__get_ts__asof_datetime():
    """  I can get a timeseries as-of a particular point in time
    """
    df = groupby_asof(get_bitemporal_test_data(), as_of=dt('2015-01-05'))
    assert len(df) == 3
    assert all(df['OPEN'] == [1.1, 2.1, 3.0])
    assert all(df['CLOSE'] == [10.1, 20.1, 30.0])


def test__get_ts__unsorted_index():
    """ I can get a timeseries as-of a date when the index isn't sorted properly
    """
    df = get_bitemporal_test_data()
    # Swap the third and fourth rows around. This would break the group-by if we didn't check
    # for sortedness
    df = df.reindex(df.index[[0, 1, 3, 2, 4, 5, 6, 7]])
    df = groupby_asof(df)
    assert len(df) == 4
    assert all(df['OPEN'] == [1.1, 2.1, 3.1, 4.1])
    assert all(df['CLOSE'] == [10.1, 20.1, 30.1, 40.1])


def test_fancy_group_by_multi_index():
    ts = read_str_as_pandas("""      index 1 |    index 2 | observed_dt | near
                     2012-09-08 17:06:11.040 | SPAM Index | 2015-01-01 |  1.0
                     2012-09-08 17:06:11.040 |  EGG Index | 2015-01-01 |  1.6
                     2012-10-08 17:06:11.040 | SPAM Index | 2015-01-01 |  2.0
                     2012-10-08 17:06:11.040 | SPAM Index | 2015-01-05 |  4.2
                     2012-10-08 17:06:11.040 |  EGG Index | 2015-01-01 |  2.1
                     2012-10-09 17:06:11.040 | SPAM Index | 2015-01-01 |  2.5
                     2012-10-09 17:06:11.040 |  EGG Index | 2015-01-01 |  2.6
                     2012-11-08 17:06:11.040 | SPAM Index | 2015-01-01 |  3.0""", num_index=3)
    expected_ts = read_str_as_pandas("""  index 1 |    index 2 | near
                          2012-09-08 17:06:11.040 |  EGG Index |  1.6
                          2012-09-08 17:06:11.040 | SPAM Index |  1.0
                          2012-10-08 17:06:11.040 |  EGG Index |  2.1
                          2012-10-08 17:06:11.040 | SPAM Index |  4.2
                          2012-10-09 17:06:11.040 |  EGG Index |  2.6
                          2012-10-09 17:06:11.040 | SPAM Index |  2.5
                          2012-11-08 17:06:11.040 | SPAM Index |  3.0""", num_index=2)
    assert_frame_equal(expected_ts, groupby_asof(ts, dt_col=['index 1', 'index 2'], asof_col='observed_dt'))


# --------- Min/Max using numeric index ----------- #

def get_numeric_index_test_data():
    group_idx = sorted(4 * list(range(4)))
    agg_idx = list(range(16))
    prices = np.arange(32).reshape(16, 2) * 10
    df = pd.DataFrame(prices, index=[group_idx, agg_idx], columns=['OPEN', 'CLOSE'])
    #           OPEN  CLOSE
    # 0 0      0     10
    #   1     20     30
    #   2     40     50
    #   3     60     70
    # 1 4     80     90
    #   5    100    110
    #   6    120    130
    #   7    140    150
    # 2 8    160    170
    #   9    180    190
    #   10   200    210
    #   11   220    230
    # 3 12   240    250
    #   13   260    270
    #   14   280    290
    #   15   300    310
    return df


def test__minmax_last():
    df = get_numeric_index_test_data()
    df = fancy_group_by(df, min_=3, max_=10, method='last')
    assert all(df['OPEN'] == [60, 140, 200])
    assert all(df['CLOSE'] == [70, 150, 210])


def test__minmax_first():
    df = get_numeric_index_test_data()
    df = fancy_group_by(df, min_=3, max_=10, method='first')
    assert all(df['OPEN'] == [60, 80, 160])
    assert all(df['CLOSE'] == [70, 90, 170])


def test__within_numeric_first():
    df = get_numeric_index_test_data()
    df = fancy_group_by(df, within=5, method='first')
    assert all(df['OPEN'] == [0, 80])
    assert all(df['CLOSE'] == [10, 90])


def test__within_numeric_last():
    df = get_numeric_index_test_data()
    df = fancy_group_by(df, within=5, method='last')
    assert all(df['OPEN'] == [60, 120])
    assert all(df['CLOSE'] == [70, 130])


# --------- Datetime index ----------- #


def get_datetime_index_test_data():
    sample_dates = pd.DatetimeIndex(4 * [dt('1/1/2014 21:30')] +
                                    4 * [dt('2/1/2014 21:30')] +
                                    4 * [dt('3/1/2014 21:30')])
    observed_dates = [dt('1/1/2014 22:00'), dt('1/1/2014 22:30'), dt('2/1/2014 00:00'), dt('1/1/2015 21:30'),
                      dt('2/1/2014 23:00'), dt('2/1/2014 23:30'), dt('3/1/2014 00:00'), dt('2/1/2015 21:30'),
                      dt('3/1/2014 21:30'), dt('3/1/2014 22:30'), dt('4/1/2014 00:00'), dt('3/1/2015 21:30'),
                      ]
    index = pd.MultiIndex.from_arrays([sample_dates, observed_dates], names=['sample_dt', 'observed_dt'])

    prices = np.arange(24).reshape(12, 2) * 10
    df = pd.DataFrame(prices, index=index, columns=['OPEN', 'CLOSE'])

    #                                          OPEN  CLOSE
    # sample_dt           observed_dt                     
    # 2014-01-01 21:30:00 2014-01-01 22:00:00     0     10
    #                     2014-01-01 22:30:00    20     30
    #                     2014-02-01 00:00:00    40     50
    #                     2015-01-01 21:30:00    60     70
    # 2014-02-01 21:30:00 2014-02-01 23:00:00    80     90
    #                     2014-02-01 23:30:00   100    110
    #                     2014-03-01 00:00:00   120    130
    #                     2015-02-01 21:30:00   140    150
    # 2014-03-01 21:30:00 2014-03-01 21:30:00   160    170
    #                     2014-03-01 22:30:00   180    190
    #                     2014-04-01 00:00:00   200    210
    #                     2015-03-01 21:30:00   220    230
    return df


def test__first_within_datetime():
    ''' This shows the groupby function can give you a timeseries of points that were observed
        within a rolling window of the sample time.
        This is like saying 'give me the timeseries as it was on the day'.
        It usually makes sense I think for the window to be the same as the sample period.
    '''
    df = get_datetime_index_test_data()
    df = fancy_group_by(df, within=timedelta(hours=1), method='first')
    assert all(df['OPEN'] == [0, 160])
    assert all(df['CLOSE'] == [10, 170])


def test__last_within_datetime():
    ''' Last-observed variant of the above.
    '''
    df = get_datetime_index_test_data()
    df = fancy_group_by(df, within=timedelta(hours=1), method='last')
    assert all(df['OPEN'] == [20, 180])
    assert all(df['CLOSE'] == [30, 190])


# ----------------------- Row Insertion ---------------------------- #

def test__can_insert_row():
    """ I can insert a new row into a bitemp ts and it comes back when selecting the latest data
    """
    df = get_bitemporal_test_data()
    df = insert_at(df, dt('2014-01-03'), [[9, 90]])
    assert len(df) == 9
    df = groupby_asof(df)
    assert len(df) == 4
    assert df.loc[dt('2014-01-03')]['OPEN'] == 9
    assert df.loc[dt('2014-01-03')]['CLOSE'] == 90


def test__can_append_row():
    """ I can append a new row to a bitemp ts and it comes back when selecting the latest data
    """
    df = get_bitemporal_test_data()
    df = insert_at(df, dt('2014-01-05'), [[9, 90]])

    assert len(df) == 9

    df = groupby_asof(df)
    assert len(df) == 5
    assert df.loc[dt('2014-01-05')]['OPEN'] == 9
    assert df.loc[dt('2014-01-05')]['CLOSE'] == 90


def test_fancy_group_by_raises():
    with pytest.raises(ValueError):
        assert(fancy_group_by(None, method=None))

