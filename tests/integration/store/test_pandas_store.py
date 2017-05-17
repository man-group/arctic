from six import StringIO
from datetime import datetime as dt, timedelta as dtd
import itertools
import string

from dateutil.rrule import rrule, DAILY
from mock import Mock, patch
from pandas import DataFrame, Series, DatetimeIndex, MultiIndex, read_csv, Panel, date_range, concat
from pandas.tseries.offsets import DateOffset
from pandas.util.testing import assert_frame_equal, assert_series_equal
import pytest
import pandas as pd

from arctic._compression import decompress
from arctic.date import DateRange, mktz
from arctic.store._pandas_ndarray_store import PandasDataFrameStore, PandasSeriesStore, PandasStore
from arctic.store.version_store import register_versioned_storage
import numpy as np
from tests.util import read_str_as_pandas


register_versioned_storage(PandasDataFrameStore)


def test_save_read_pandas_series(library):
    s = Series(data=[1, 2, 3], index=[4, 5, 6])
    library.write('pandas', s)
    saved = library.read('pandas').data
    assert np.all(s == saved)
    assert saved.name == "values"


def test_save_read_pandas_series_maintains_name(library):
    s = Series(data=[1, 2, 3], index=[4, 5, 6], name="ADJ")
    library.write('pandas', s)
    saved = library.read('pandas').data
    assert np.all(s == saved)
    assert saved.name == "ADJ"


def test_save_read_pandas_series_with_multiindex(library):
    df = Series(data=['A', 'BC', 'DEF'], index=MultiIndex.from_tuples([(1, 2), (1, 3), (2, 2)]))
    library.write('pandas', df)
    saved_df = library.read('pandas').data
    assert np.all(df.values == saved_df.values)


def test_save_read_pandas_series_with_multiindex_and_name(library):
    df = Series(data=['A', 'BC', 'DEF'],
                index=MultiIndex.from_tuples([(1, 2), (1, 3), (2, 2)]),
                name='Foo')
    library.write('pandas', df)
    saved_df = library.read('pandas').data
    assert np.all(df.values == saved_df.values)
    assert df.name == 'Foo'


def test_save_read_pandas_series_with_unicode_index_name(library):
    df = Series(data=['A', 'BC', 'DEF'],
                index=MultiIndex.from_tuples([(np.datetime64(dt(2013, 1, 1)),),
                                              (np.datetime64(dt(2013, 1, 2)),),
                                              (np.datetime64(dt(2013, 1, 3)),)], names=[u'DATETIME']))
    library.write('pandas', df)
    saved_df = library.read('pandas').data
    assert np.all(df.values == saved_df.values)


def test_save_read_pandas_dataframe_with_multiindex(library):
    df = DataFrame(data=['A', 'BC', 'DEF'], index=MultiIndex.from_tuples([(1, 2), (1, 3), (2, 2)]))
    library.write('pandas', df)
    saved_df = library.read('pandas').data
    assert np.all(df.values == saved_df.values)


def test_save_read_pandas_dataframe_with_none_values(library):
    df = DataFrame(data=[(1, None), (1, 3), (2, 2)])
    library.write('pandas', df)
    saved_df = library.read('pandas').data
    assert np.all((df.values == saved_df.values) | (np.isnan(df.values) & np.isnan(saved_df.values)))


def test_save_read_pandas_dataframe_with_unicode_index_name(library):
    df = DataFrame(data=['A', 'BC', 'DEF'],
                   index=MultiIndex.from_tuples([(np.datetime64(dt(2013, 1, 1)),),
                                                 (np.datetime64(dt(2013, 1, 2)),),
                                                 (np.datetime64(dt(2013, 1, 3)),)], names=[u'DATETIME']))
    library.write('pandas', df)
    saved_df = library.read('pandas').data
    assert np.all(df.values == saved_df.values)



def test_cant_write_pandas_series_with_tuple_values(library):
    df = Series(data=[('A', 'BC')], index=np.array([dt(2013, 1, 1), ]).astype('datetime64[ns]'))
    assert PandasSeriesStore().can_write(Mock(), 'FOO', df) == False


def test_save_read_pandas_series_with_datetimeindex_with_timezone(library):
    df = Series(data=['A', 'BC', 'DEF'], index=DatetimeIndex(np.array([dt(2013, 1, 1),
                                                                       dt(2013, 1, 2),
                                                                       dt(2013, 1, 3)]).astype('datetime64[ns]'),
                                                                tz="America/Chicago"))
    library.write('pandas', df)
    saved_df = library.read('pandas').data
    assert df.index.tz == saved_df.index.tz
    assert all(df.index == saved_df.index)


def test_save_read_pandas_series_with_datetimeindex(library):
    df = Series(data=['A', 'BC', 'DEF'], index=np.array([dt(2013, 1, 1),
                                                            dt(2013, 1, 2),
                                                            dt(2013, 1, 3)]).astype('datetime64[ns]'))
    library.write('pandas', df)
    saved_df = library.read('pandas').data
    assert np.all(df.index == saved_df.index)
    assert np.all(df.values == saved_df.values)


def test_save_read_pandas_dataframe_with_datetimeindex_with_timezone(library):
    df = DataFrame(data=['A', 'BC', 'DEF'], index=DatetimeIndex(np.array([dt(2013, 1, 1),
                                                                       dt(2013, 1, 2),
                                                                       dt(2013, 1, 3)]).astype('datetime64[ns]'),
                                                                tz="America/Chicago"))
    library.write('pandas', df)
    saved_df = library.read('pandas').data
    assert df.index.tz == saved_df.index.tz
    assert all(df.index == saved_df.index)


def test_save_read_pandas_dataframe_with_datetimeindex(library):
    df = DataFrame(data=['A', 'BC', 'DEF'], index=np.array([dt(2013, 1, 1),
                                                            dt(2013, 1, 2),
                                                            dt(2013, 1, 3)]).astype('datetime64[ns]'))
    library.write('pandas', df)
    saved_df = library.read('pandas').data
    assert np.all(df.index == saved_df.index)
    assert np.all(df.values == saved_df.values)


def test_save_read_pandas_dataframe_with_strings(library):
    df = DataFrame(data=['A', 'BC', 'DEF'], index=[4, 5, 6])
    library.write('pandas', df)
    saved_df = library.read('pandas').data
    assert np.all(df.values == saved_df.values)


def test_save_read_pandas_dataframe(library):
    df = DataFrame(data=[1, 2, 3], index=[4, 5, 6])
    library.write('pandas', df)
    saved_df = library.read('pandas').data
    assert np.all(df.values == saved_df.values)


def test_save_read_empty_dataframe(library):
    df = DataFrame({'a': [], 'b': []})
    library.write('pandas', df)
    saved_df = library.read('pandas').data
    assert np.all(df.values == saved_df.values)


def test_save_read_pandas_dataframe2(library):
    df = DataFrame(data=[1, 2, 3], index=DatetimeIndex(start='1/1/2011', periods=3, freq='H'))
    library.write('pandas', df)
    saved_df = library.read('pandas').data
    assert np.all(df.values == saved_df.values)


def test_save_read_pandas_dataframe_strings(library):
    df = DataFrame(data=['a', 'b', 'c'], index=DatetimeIndex(start='1/1/2011', periods=3, freq='H'))
    library.write('pandas', df)
    saved_df = library.read('pandas').data
    assert np.all(df.values == saved_df.values)


def test_save_read_pandas_dataframe_empty_multiindex(library):
    expected = read_csv(StringIO(u'''\
STRATEGY MAC INSTRUMENT CONTRACT $Price $Delta $Gamma $Vega $Theta $Notional uDelta uGamma uVega uTheta Delta Gamma Vega Theta'''),
                        delimiter=' ').set_index(['STRATEGY', 'MAC', 'INSTRUMENT', 'CONTRACT'])
    library.write('pandas', expected)
    saved_df = library.read('pandas').data
    assert np.all(expected.values == saved_df.values)
    assert np.all(expected.index.names == saved_df.index.names)


def test_save_read_pandas_dataframe_empty_multiindex_and_no_columns(library):
    expected = read_csv(StringIO(u'''STRATEGY MAC INSTRUMENT CONTRACT'''),
                        delimiter=' ').set_index(['STRATEGY', 'MAC', 'INSTRUMENT', 'CONTRACT'])
    library.write('pandas', expected)
    saved_df = library.read('pandas').data
    assert np.all(expected.values == saved_df.values)
    assert np.all(expected.index.names == saved_df.index.names)


def test_save_read_pandas_dataframe_multiindex_and_no_columns(library):
    expected = read_csv(StringIO(u'''\
STRATEGY MAC INSTRUMENT CONTRACT
STRAT F22 ASD 201312'''),
                        delimiter=' ').set_index(['STRATEGY', 'MAC', 'INSTRUMENT', 'CONTRACT'])
    library.write('pandas', expected)
    saved_df = library.read('pandas').data
    assert np.all(expected.values == saved_df.values)
    assert np.all(expected.index.names == saved_df.index.names)


def test_append_pandas_dataframe(library):
    df = DataFrame(data=[1, 2, 3], index=DatetimeIndex(start='1/1/2011', periods=3, freq='H'))
    df2 = DataFrame(data=[4, 5, 6], index=DatetimeIndex(start='2/1/2011', periods=3, freq='H'))
    library.write('pandas', df)
    library.append('pandas', df2)
    saved_df = library.read('pandas').data
    assert np.all(df.append(df2).values == saved_df.values)


def test_empty_dataframe_multindex(library):
    df = DataFrame({'a': [], 'b': [], 'c': []})
    df = df.groupby(['a', 'b']).sum()
    library.write('pandas', df)
    saved_df = library.read('pandas').data
    assert np.all(df.values == saved_df.values)
    assert np.all(df.index.names == df.index.names)


def test_dataframe_append_empty(library):
    df = DataFrame(data=[1, 2, 3], index=DatetimeIndex(start='1/1/2011', periods=3, freq='H'))
    df2 = DataFrame(data=[], index=[])
    library.write('pandas', df)
    library.append('pandas', df2)
    saved_df = library.read('pandas').data
    assert np.all(df.append(df2).values == saved_df.values)


def test_empy_dataframe_append(library):
    df = DataFrame(data=[], index=[])
    df2 = DataFrame(data=[1, 2, 3], index=DatetimeIndex(start='1/1/2011', periods=3, freq='H'))
    library.write('pandas', df)
    library.append('pandas', df2)
    saved_df = library.read('pandas').data
    assert np.all(df.append(df2).values == saved_df.values)


def test_dataframe_append_empty_multiindex(library):
    df = DataFrame({'a': [1, 1, 1], 'b': [1, 1, 2], 'c': [1, 2, 3]}).groupby(['a', 'b']).sum()
    df2 = DataFrame({'a': [], 'b': [], 'c': []}).groupby(['a', 'b']).sum()
    library.write('pandas', df)
    library.append('pandas', df2)
    saved_df = library.read('pandas').data
    assert np.all(df.append(df2).values == saved_df.values)
    assert np.all(df.index.names == saved_df.index.names)


def test_empty_dataframe_append_multiindex(library):
    df = DataFrame({'a': [], 'b': [], 'c': []}).groupby(['a', 'b']).sum()
    df2 = DataFrame({'a': [1, 1, 1], 'b': [1, 1, 2], 'c': [1, 2, 3]}).groupby(['a', 'b']).sum()
    library.write('pandas', df)
    library.append('pandas', df2)
    saved_df = library.read('pandas').data
    assert np.all(df.append(df2).values == saved_df.values)
    assert np.all(df.index.names == saved_df.index.names)


def test_empty_dataframe_should_ignore_dtype(library):
    df = DataFrame({'a': [], 'b': [], 'c': []}).groupby(['a', 'b']).sum()
    df2 = DataFrame({'a': [1, 1, 1], 'b': [1, 1, 2], 'c': [1, 2, 3]}).groupby(['a']).sum()
    library.write('pandas', df)
    library.append('pandas', df2)
    saved_df = library.read('pandas').data
    assert np.all(df2.index.names == saved_df.index.names)


def test_empty_dataframe_should_ignore_dtype2(library):
    df = DataFrame({'a': []})
    df2 = DataFrame({'a': [1, 1, 1], 'b': [1, 1, 2], 'c': [1, 2, 3]}).groupby(['a']).sum()
    library.write('pandas', df)
    library.append('pandas', df2)
    saved_df = library.read('pandas').data
    assert np.all(df2.values == saved_df.values)
    assert np.all(df2.index.names == saved_df.index.names)


def test_dataframe_append_should_promote_string_column(library):
    data = np.zeros((2,), dtype=[('A', 'i4'), ('B', 'f4'), ('C', 'a10')])
    data[:] = [(1, 2., 'Hello'), (2, 3., "World")]
    df = DataFrame(data, index=MultiIndex.from_tuples([(np.datetime64(dt(2013, 1, 1)),),
                                                       (np.datetime64(dt(2013, 1, 2)),), ], names=[u'DATETIME']))
    data2 = np.zeros((1,), dtype=[('A', 'i4'), ('B', 'f4'), ('C', 'a30')])
    data2[:] = [(3, 4., 'Hello World - Good Morning')]
    df2 = DataFrame(data2, index=MultiIndex.from_tuples([(np.datetime64(dt(2013, 1, 3)),)], names=[u'DATETIME']))
    expected_data = np.zeros((3,), dtype=[('A', 'i4'), ('B', 'f4'), ('C', 'a30')])
    expected_data[:] = [(1, 2., 'Hello'), (2, 3., "World"), (3, 4., 'Hello World - Good Morning')]
    expected = DataFrame(expected_data, MultiIndex.from_tuples([(np.datetime64(dt(2013, 1, 1)),),
                                                                (np.datetime64(dt(2013, 1, 2)),),
                                                                (np.datetime64(dt(2013, 1, 3)),)],
                                                               names=[u'DATETIME']))

    library.write('pandas', df)
    library.append('pandas', df2)
    actual = library.read('pandas').data

    assert_frame_equal(expected, actual)


def test_dataframe_append_should_add_new_column(library):
    data = np.zeros((2,), dtype=[('A', 'i4'), ('B', 'f4'), ('C', 'a10')])
    data[:] = [(1, 2., 'Hello'), (2, 3., "World")]
    df = DataFrame(data, index=MultiIndex.from_tuples([(np.datetime64(dt(2013, 1, 1)),),
                                                       (np.datetime64(dt(2013, 1, 2)),), ], names=[u'DATETIME']))
    data2 = np.zeros((1,), dtype=[('A', 'i4'), ('B', 'f4'), ('C', 'a10'), ('D', 'f4')])
    data2[:] = [(4, 5., 'Hi', 6.)]
    df2 = DataFrame(data2, index=MultiIndex.from_tuples([(np.datetime64(dt(2013, 1, 3)),)], names=[u'DATETIME']))
    expected_data = np.zeros((3,), dtype=[('A', 'i4'), ('B', 'f4'), ('C', 'a10'), ('D', 'f4')])
    expected_data[:] = [(1, 2., 'Hello', np.nan), (2, 3., "World", np.nan), (4, 5., 'Hi', 6.)]
    expected = DataFrame(expected_data, MultiIndex.from_tuples([(np.datetime64(dt(2013, 1, 1)),),
                                                                (np.datetime64(dt(2013, 1, 2)),),
                                                                (np.datetime64(dt(2013, 1, 3)),)],
                                                               names=[u'DATETIME']))

    library.write('pandas', df)
    library.append('pandas', df2)
    actual = library.read('pandas').data

    assert_frame_equal(expected, actual)


def test_dataframe_append_should_add_new_columns_and_reorder(library):
    data = np.zeros((2,), dtype=[('A', 'i4'), ('B', 'f4'), ('C', 'a10')])
    data[:] = [(1, 2., 'Hello'), (2, 3., "World")]
    df = DataFrame(data, index=MultiIndex.from_tuples([(np.datetime64(dt(2013, 1, 1)),),
                                                       (np.datetime64(dt(2013, 1, 2)),), ], names=[u'DATETIME']))
    data2 = np.zeros((1,), dtype=[('C', 'a10'), ('A', 'i4'), ('E', 'a1'), ('B', 'f4'), ('D', 'f4'), ('F', 'i4')])
    data2[:] = [('Hi', 4, 'Y', 5., 6., 7)]
    df2 = DataFrame(data2, index=MultiIndex.from_tuples([(np.datetime64(dt(2013, 1, 3)),)], names=[u'DATETIME']))
    expected_data = np.zeros((3,), dtype=[('C', 'a10'), ('A', 'i4'), ('E', 'a1'),
                                          ('B', 'f4'), ('D', 'f4'), ('F', 'i4')])
    expected_data[:] = [('Hello', 1, '', 2., np.nan, 0), ("World", 2, '', 3., np.nan, 0), ('Hi', 4, 'Y', 5., 6., 7)]
    expected = DataFrame(expected_data, MultiIndex.from_tuples([(np.datetime64(dt(2013, 1, 1)),),
                                                                (np.datetime64(dt(2013, 1, 2)),),
                                                                (np.datetime64(dt(2013, 1, 3)),)],
                                                               names=[u'DATETIME']))

    library.write('pandas', df)
    library.append('pandas', df2)
    actual = library.read('pandas').data

    assert_frame_equal(expected, actual)


# -- auto generated tests --- #
def dataframe(columns, length, index):
    df = DataFrame(np.ones((length, columns)), columns=list(string.ascii_lowercase[:columns]))
    index = min(index, columns)
    if index:
        df = df.set_index(list(string.ascii_lowercase[:index]))
    return df



@pytest.mark.parametrize("df_size", list(itertools.combinations_with_replacement([0, 1, 2, 4], r=3)))
def test_dataframe_save_read(library, df_size):
    df = dataframe(*df_size)
    library.write('pandas', df)
    result = library.read('pandas').data
    assert np.all(df.values == result.values), str(df.values) + "!=" + str(result.values)
    if None not in df.index.names:  # saved as 'index' or 'level'
        assert np.all(df.index.names == result.index.names), str(df.index.names) + "!=" + str(result.index.names)
    assert np.all(df.index.values == result.index.values), str(df.index.values) + "!=" + str(result.index.values)
    assert np.all(df.columns.values == result.columns.values), str(df.columns.values) + "!=" + str(result.columns.values)


@pytest.mark.parametrize("df_size", list(itertools.combinations_with_replacement([0, 1, 2, 4], r=3)))
def test_dataframe_save_append_read(library, df_size):
    df = dataframe(*df_size)
    library.write('pandas', df)
    library.append('pandas', df)
    result = library.read('pandas').data
    assert len(result) == len(df) * 2
    if None not in df.index.names:  # saved as 'index' or 'level'
        assert np.all(df.index.names == result.index.names), str(df.index.names) + "!=" + str(result.index.names)
    assert np.all(df.columns.values == result.columns.values), str(df.columns.values) + "!=" + str(result.columns.values)



def test_large_dataframe_append_rewrite_same_item(library):
    csv = \
"""index, f1, f2, f3, f4, f5, f6, f7, f8, iVol, tau, uPrice, uDelta, uGamma, uVega, uTheta, Delta, Gamma, Vega, Theta, $Price, $Delta, $Gamma, $Vega, $Theta, $Time_Value, $Notional, FX, f9
0, 201401, 2013 - 12 - 20 16:15:00, 15.0, F1, CALL, STRAT, 140.0, 140.345, 0.07231398622706062, 0.008813407863715872, 0.5768068954653813, 0.6427860135978315, 0.391592427081917, 4.915801583071703, -20.166163353481476, 9.641790203967473, 5.873886406228755, 73.73702374607555, -302.49245030222215, 11909.274289984183, 18625.940769791625, 15925.131550993763, 1014.9606370552315, -1601.4183005499872, 4786.093789984206, 2897689.1805000002, 1.37646, SYM
1, 201401, 2013 - 12 - 20 16:15:00, 15.0, F1, PUT, STRAT, 140.0, 140.345, 0.07231398622706062, 0.008813407863715872, 0.2318116692147143, -0.357200149447554, 0.391592427081917, 4.915801583071703, -20.16670499598669, -5.358002241713311, 5.873886406228755, 73.73702374607555, -302.50057493980034, 4786.192353109285, -10350.550083271604, 15925.131550993763, 1014.9606370552315, -1601.4613130062987, 4786.192353109285, 2897689.1805000002, 1.37646, SYM
2, 201401, 2013 - 12 - 20 16:15:00, -48.0, F22, CALL, STRAT, 141.5, 140.345, 0.0739452718231504, 0.008813407863715872, 0.05709601681178711, 0.11956012929302556, 0.20479158314197934, 2.628816497069195, -11.027911868706408, -5.738886206065227, -9.829995990815009, -126.18319185932137, 529.3397696979075, -3772.3383984361194, -11086.338978290602, -26650.835319775462, -1736.8611626668148, 2802.3654592245452, -3772.3383984361194, -9272605.3776, 1.37646, SYM
3, 201402, 2014 - 01 - 24 16:15:00, -286.0, F22, CALL, STRAT, 141.5, 140.345, 0.045487609195962696, 0.10463818541333941, 0.3747457492377393, 0.29120692771365, 0.1660598823861943, 15.56832633851715, -3.3830120036011397, -83.2851813261039, -47.49312636245157, -4452.541332815905, 967.541433029926, -147525.24472279268, -160889.7125497546, -128762.15724702866, -61287.4504296778, 5122.238772724507, -147525.24472279268, -55249273.7082, 1.37646, SYM
4, 201402, 2014 - 01 - 24 16:15:00, -264.0, F22, CALL, STRAT, 142.0, 140.345, 0.044822991783170785, 0.10463818541333941, 0.24229877494137142, 0.21142760067302388, 0.14217904830463807, 13.134711351643713, -2.812643033008342, -55.816886577678304, -37.53526875242445, -3467.56379683394, 742.5377607142022, -88047.84694353123, -107826.65888355605, -101764.66675460352, -47729.62863790045, 3931.052023510272, -88047.84694353123, -50999329.576799996, 1.37646, SYM
5, 201401, 2013 - 12 - 20 16:15:00, -350.0, F22, CALL, STRAT, 142.0, 140.345, 0.07732984880519912, 0.008813407863715872, 0.022997617617102506, 0.053564485523868555, 0.10692101346714668, 1.4353175202195965, -6.296783951449458, -18.747569933353994, -37.422354713501335, -502.3611320768588, 2203.8743830073104, -11079.355260832921, -36216.420371031316, -101458.53708176922, -6914.80003858513, 11667.480512439395, -11079.355260832921, -67612747.545, 1.37646, SYM
6, 201402, 2014 - 01 - 24 16:15:00, -43.0, F22, CALL, STRAT, 142.5, 140.345, 0.04429193547308161, 0.10463818541333941, 0.14930517833206025, 0.14535540627931182, 0.11352765189447668, 10.36359429711007, -2.1930395074393734, -6.250282470010408, -4.881689031462497, -445.634554775733, 94.30069881989306, -8837.042047978748, -12074.25059227865, -13235.111243323556, -6133.9813926660545, 499.23515345242305, -8837.042047978748, -8306708.9841, 1.37646, SYM
7, 201401, 2013 - 12 - 20 16:15:00, -557.0, F22, CALL, STRAT, 142.5, 140.345, 0.0814452531405243, 0.008813407863715872, 0.009355428262274312, 0.02334242880598363, 0.05141464658820557, 0.7269263150873877, -3.358771076933658, -13.001732844932882, -28.637958149630503, -404.89795750367495, 1870.8354898520474, -7172.696641740786, -25116.653728342328, -77642.50435641785, -5573.258425855083, 9904.346993699035, -7172.696641740786, -107600858.2359, 1.37646, SYM
8, 201401, 2013 - 12 - 20 16:15:00, -607.0, F22, CALL, STRAT, 143.0, 140.345, 0.08598678226600448, 0.008813407863715872, 0.003929576582252237, 0.010236258301012439, 0.024009328219809185, 0.35838470316321597, -1.748258969026736, -6.21340878871455, -14.573662229424174, -217.5395148200721, 1061.1931941992289, -3283.2053243209966, -12003.018280721177, -39511.74267470002, -2994.344405692364, 5618.038400336425, -3283.2053243209966, -117259822.1709, 1.37646, SYM
9, 201401, 2013 - 12 - 20 16:15:00, -799.0, F22, CALL, STRAT, 143.5, 140.345, 0.09076344895187359, 0.008813407863715872, 0.0017194411099074047, 0.004596451952699387, 0.01121737082629775, 0.1767420247600966, -0.9100718136522263, -3.67256511020681, -8.962679290211902, -141.2168777833172, 727.1473791081288, -1891.026786204374, -7094.634789685377, -24299.388322293227, -1943.793835936248, 3849.574159412212, -1891.026786204374, -154350243.6813, 1.37646, SYM
10, 201401, 2013 - 12 - 20 16:15:00, -377.0, F22, CALL, STRAT, 144.0, 140.345, 0.09566038240450792, 0.008813407863715872, 0.0007852689424384662, 0.0021295289144923784, 0.005324993197820229, 0.08842782200919548, -0.47989481865526434, -0.8028324007636266, -2.007522435578226, -33.3372888974667, 180.92034663303465, -407.4960157678369, -1550.905840965067, -5442.743810001693, -458.87444675807006, 957.8062320250265, -407.4960157678369, -72828588.06989999, 1.37646, SYM
11, 201402, 2014 - 01 - 24 16:15:00, -43.0, F22, PUT, STRAT, 137.5, 140.345, 0.05414565513055749, 0.10463818541333941, 0.14529132959784974, -0.11936326135136956, 0.08106840033227831, 9.046889913827847, -2.3403474666535415, 5.132620238108891, -3.4859412142879673, -389.0162662945974, 100.63494106610229, -8599.471252145018, 9915.158754388978, -9450.995231657676, -5354.653299038616, 532.7691191532583, -8599.471252145018, -8306708.9841, 1.37646, SYM
12, 201402, 2014 - 01 - 24 16:15:00, -264.0, F22, PUT, STRAT, 138.0, 140.345, 0.052853182910226726, 0.10463818541333941, 0.20369081242765574, -0.16004607860136968, 0.10141337819029916, 11.047155968410756, -2.789510903380204, 42.252164750761594, -26.77313184223898, -2916.44917566044, 736.4308784923738, -74018.27549798116, 81622.4271006569, -72586.63466280713, -40143.75632329569, 3898.7217192677417, -74018.27549798116, -50999329.576799996, 1.37646, SYM
13, 201401, 2013 - 12 - 20 16:15:00, -376.0, F22, PUT, STRAT, 138.0, 140.345, 0.08897789701177691, 0.008813407863715872, 0.009425028910330369, -0.021620830082859088, 0.04411750741642045, 0.6814450839280415, -3.43983227630679, 8.129432111155017, -16.588182788574088, -256.2233515569436, 1293.376935891353, -4877.913910511415, 15704.378314735444, -44973.45961948536, -3526.811944840706, 6847.236989142353, -4877.913910511415, -72635408.7912, 1.37646, SYM
14, 201401, 2013 - 12 - 20 16:15:00, -301.0, F22, PUT, STRAT, 138.5, 140.345, 0.08383267513417192, 0.008813407863715872, 0.020991265826436845, -0.045956251827941025, 0.08727871921287762, 1.2701629715541363, -6.0408289559434, 13.832831800210249, -26.270894483076166, -382.319054437795, 1818.2895157389635, -8696.984965596635, 26722.164695430383, -71224.98149804553, -5262.468856714474, 9626.164564746361, -8696.984965596635, -58146962.8887, 1.37646, SYM
15, 201402, 2014 - 01 - 24 16:15:00, -286.0, F22, PUT, STRAT, 138.5, 140.345, 0.051599724402617266, 0.10463818541333941, 0.28321473137770425, -0.21146513081873966, 0.12351912253075312, 13.136076509490826, -3.2382097361444653, 60.479027414159546, -35.32646904379539, -3756.917881714376, 926.127984537317, -111492.45225751627, 116832.94892344868, -95776.22511698281, -51712.4718746457, 4902.992790754752, -111492.45225751627, -55249273.7082, 1.37646, SYM
16, 201401, 2013 - 12 - 20 16:15:00, -739.0, F22, PUT, STRAT, 139.0, 140.345, 0.0791166184474159, 0.008813407863715872, 0.047581495319667155, -0.0967612790459439, 0.16434769983129724, 2.257195133461944, -10.131173555213623, 71.50658521495254, -121.45295017532867, -1668.0672036283765, 7486.937257302868, -48400.084510256995, 138135.90554124617, -329280.15202122304, -22960.277831063155, 39636.42175841195, -48400.084510256995, -142759486.9593, 1.37646, SYM
17, 201401, 2013 - 12 - 20 16:15:00, -669.0, F22, PUT, STRAT, 139.5, 140.345, 0.07513349054261133, 0.008813407863715872, 0.10733307441031315, -0.1949726645282245, 0.27848967340302655, 3.6322892048663644, -15.482297001088007, 130.4367125693822, -186.30959150662477, -2430.001478055598, 10357.656693727877, -98837.84833028633, 251976.70050152476, -505117.8297913038, -33447.99834484408, 54834.231279417974, -98837.84833028633, -129236937.4503, 1.37646, SYM
18, 201401, 2013 - 12 - 20 16:15:00, -471.0, F22, PUT, STRAT, 140.0, 140.345, 0.07231398622706062, 0.008813407863715872, 0.2318116692147143, -0.357200149447554, 0.391592427081917, 4.915801583071703, -20.16670499598669, 168.24127038979793, -184.4400331555829, -2315.3425456267723, 9498.518053109732, -150286.43988763154, 325007.2726147283, -500049.1307012041, -31869.76400353427, 50285.885228397776, -150286.43988763154, -90987440.2677, 1.37646, SYM
19, 201401, 2013 - 12 - 20 16:15:00, -364.0, F22, PUT, STRAT, 141.0, 140.345, 0.07172143045750252, 0.008813407863715872, 0.7922715181315709, -0.7543151841866509, 0.333159035321538, 4.147995696473539, -16.876460506586433, 274.5707270439409, -121.26988885703983, -1509.8704335163682, 6143.031624397461, -396952.9396004471, 530413.7500248309, -328783.8408272312, -20782.762569179402, 32521.681960454345, -68777.34640044652, -70317257.4468, 1.37646, SYM
20, 201401, 2013 - 12 - 20 16:15:00, -394.0, F22, PUT, STRAT, 141.5, 140.345, 0.0739452718231504, 0.008813407863715872, 1.212080035129219, -0.88042603375236, 0.20479158314197934, 2.628816497069195, -11.026098543797652, 346.8878572984298, -80.68788375793986, -1035.7536998452629, 4344.282826256274, -657341.595950662, 670115.460626992, -218758.93991649026, -14256.735376890107, 22998.967457802737, -30955.94375066146, -76112635.8078, 1.37646, SYM
21, 201402, 2014 - 01 - 24 16:15:00, -40.0, GEE1, CALL, STRAT, 141.5, 140.345, 0.045487609195962696, 0.10463818541333941, 0.3747457492377393, 0.29120692771365, 0.1660598823861943, 15.56832633851715, -3.3830120036011397, -11.648277108545999, -6.642395295447772, -622.733053540686, 135.32048014404558, -20632.901359831147, -22502.057699266377, -18008.69332126275, -8571.671388766126, 716.3970311502808, -20632.901359831147, -7727171.148, 1.37646, SYM
22, 201401, 2013 - 12 - 20 16:15:00, -12.0, GEE1, CALL, STRAT, 141.5, 140.345, 0.0739452718231504, 0.008813407863715872, 0.05709601681178711, 0.11956012929302556, 0.20479158314197934, 2.628816497069195, -11.027911868706408, -1.4347215515163068, -2.4574989977037522, -31.545797964830342, 132.33494242447688, -943.0845996090299, -2771.5847445726504, -6662.708829943866, -434.2152906667037, 700.5913648061363, -943.0845996090299, -2318151.3444, 1.37646, SYM
23, 201402, 2014 - 01 - 24 16:15:00, -45.0, GEE1, CALL, STRAT, 142.0, 140.345, 0.044822991783170785, 0.10463818541333941, 0.24229877494137142, 0.21142760067302388, 0.14217904830463807, 13.134711351643713, -2.812643033008342, -9.514242030286075, -6.398057173708713, -591.0620108239671, 126.56893648537539, -15008.155729011005, -18379.544127878875, -17346.250014989233, -8135.732154187577, 670.0656858256148, -15008.155729011005, -8693067.5415, 1.37646, SYM
24, 201401, 2013 - 12 - 20 16:15:00, -57.0, GEE1, CALL, STRAT, 142.0, 140.345, 0.07732984880519912, 0.008813407863715872, 0.022997617617102506, 0.053564485523868555, 0.10692101346714668, 1.4353175202195965, -6.296783951449458, -3.0531756748605074, -6.09449776762736, -81.813098652517, 358.9166852326191, -1804.3521424785042, -5898.102746139386, -16523.247467602414, -1126.1245777124357, 1900.1325405972727, -1804.3521424785042, -11011218.8859, 1.37646, SYM
25, 201401, 2013 - 12 - 20 16:15:00, -68.0, GEE1, CALL, STRAT, 142.5, 140.345, 0.0814452531405243, 0.008813407863715872, 0.009355428262274312, 0.02334242880598363, 0.05141464658820557, 0.7269263150873877, -3.358771076933658, -1.5872851588068868, -3.496195967997979, -49.430989425942364, 228.39643323148874, -875.6613494405268, -3066.306020695293, -9478.797659311334, -680.3977970523262, 1209.1482864839038, -875.6613494405268, -13136190.9516, 1.37646, SYM
26, 201402, 2014 - 01 - 24 16:15:00, -19.0, GEE1, CALL, STRAT, 142.5, 140.345, 0.04429193547308161, 0.10463818541333941, 0.14930517833206025, 0.14535540627931182, 0.11352765189447668, 10.36359429711007, -2.1930395074393734, -2.7617527193069247, -2.1570253859950568, -196.90829164509134, 41.66775064134809, -3904.7395095720058, -5335.133982634753, -5848.072409840642, -2710.3638711780245, 220.5922771068846, -3904.7395095720058, -3670406.2953000003, 1.37646, SYM
27, 201401, 2013 - 12 - 20 16:15:00, -91.0, GEE1, CALL, STRAT, 143.0, 140.345, 0.08598678226600448, 0.008813407863715872, 0.003929576582252237, 0.010236258301012439, 0.024009328219809185, 0.35838470316321597, -1.748258969026736, -0.9314995053921319, -2.1848488680026357, -32.613007987852654, 159.091566181433, -492.21035339902915, -1799.464025610588, -5923.5067271790795, -448.9050097495967, 842.2429891772894, -492.21035339902915, -17579314.3617, 1.37646, SYM
28, 201401, 2013 - 12 - 20 16:15:00, -117.0, GEE1, CALL, STRAT, 143.5, 140.345, 0.09076344895187359, 0.008813407863715872, 0.0017194411099074047, 0.004596451952699387, 0.01121737082629775, 0.1767420247600966, -0.9100718136522263, -0.5377848784658282, -1.3124323866768368, -20.678816896931302, 106.47840219731049, -276.9088034867481, -1038.8889491779587, -3558.233333802638, -284.63564305950064, 563.7048518788846, -276.9088034867481, -22601975.6079, 1.37646, SYM
29, 201401, 2013 - 12 - 20 16:15:00, -126.0, GEE1, CALL, STRAT, 144.0, 140.345, 0.09566038240450792, 0.008813407863715872, 0.0007852689424384662, 0.0021295289144923784, 0.005324993197820229, 0.08842782200919548, -0.47989481865526434, -0.26832064322603966, -0.6709491429253489, -11.141905573158631, 60.46674715056331, -136.19230235211526, -518.3398831872638, -1819.0602654117067, -153.3638734522993, 320.1156107033245, -136.19230235211526, -24340589.1162, 1.37646, SYM
30, 201402, 2014 - 01 - 24 16:15:00, -19.0, GEE1, PUT, STRAT, 137.5, 140.345, 0.05414565513055749, 0.10463818541333941, 0.14529132959784974, -0.11936326135136956, 0.08106840033227831, 9.046889913827847, -2.3403474666535415, 2.2679019656760215, -1.5402996063132879, -171.8909083627291, 44.46660186641729, -3799.766367226869, 4381.11665891606, -4176.021148871998, -2366.009597249621, 235.40961078864902, -3799.766367226869, -3670406.2953000003, 1.37646, SYM
31, 201401, 2013 - 12 - 20 16:15:00, -64.0, GEE1, PUT, STRAT, 138.0, 140.345, 0.08897789701177691, 0.008813407863715872, 0.009425028910330369, -0.021620830082859088, 0.04411750741642045, 0.6814450839280415, -3.43983227630679, 1.3837331253029816, -2.8235204746509086, -43.612485371394655, 220.14926568363455, -830.2832188104537, 2673.0856705932674, -7655.056956508147, -600.3084161430988, 1165.48714708806, -830.2832188104537, -12363473.8368, 1.37646, SYM
32, 201402, 2014 - 01 - 24 16:15:00, -45.0, GEE1, PUT, STRAT, 138.0, 140.345, 0.052853182910226726, 0.10463818541333941, 0.20369081242765574, -0.16004607860136968, 0.10141337819029916, 11.047155968410756, -2.789510903380204, 7.2020735370616356, -4.563602018563462, -497.122018578484, 125.52799065210918, -12616.751505337697, 13912.913710339246, -12372.721817523941, -6842.685736925402, 664.5548385115469, -12616.751505337697, -8693067.5415, 1.37646, SYM
33, 201401, 2013 - 12 - 20 16:15:00, -51.0, GEE1, PUT, STRAT, 138.5, 140.345, 0.08383267513417192, 0.008813407863715872, 0.020991265826436845, -0.045956251827941025, 0.08727871921287762, 1.2701629715541363, -6.0408289559434, 2.3437688432249923, -4.451214679856759, -64.77831154926095, 308.08227675311343, -1473.5755257323203, 4527.675745737374, -12068.020120931302, -891.6475471509574, 1631.011271767656, -1473.5755257323203, -9852143.2137, 1.37646, SYM
34, 201402, 2014 - 01 - 24 16:15:00, -40.0, GEE1, PUT, STRAT, 138.5, 140.345, 0.051599724402617266, 0.10463818541333941, 0.28321473137770425, -0.21146513081873966, 0.12351912253075312, 13.136076509490826, -3.2382097361444653, 8.458605232749587, -4.940764901230125, -525.443060379633, 129.5283894457786, -15593.349966086193, 16340.27257670611, -13395.276240137457, -7232.5135489014965, 685.733257448217, -15593.349966086193, -7727171.148, 1.37646, SYM
35, 201401, 2013 - 12 - 20 16:15:00, -98.0, GEE1, PUT, STRAT, 139.0, 140.345, 0.0791166184474159, 0.008813407863715872, 0.047581495319667155, -0.0967612790459439, 0.16434769983129724, 2.257195133461944, -10.131173555213623, 9.4826053465025, -16.10607458346713, -221.20512307927052, 992.855008410935, -6418.414454675487, 18318.42861034117, -43666.38010565609, -3044.8000371369267, 5256.250787989675, -6418.414454675487, -18931569.312599998, 1.37646, SYM
36, 201401, 2013 - 12 - 20 16:15:00, -111.0, GEE1, PUT, STRAT, 139.5, 140.345, 0.07513349054261133, 0.008813407863715872, 0.10733307441031315, -0.1949726645282245, 0.27848967340302655, 3.6322892048663644, -15.482297001088007, 21.64196576263292, -30.912353747735946, -403.18410174016645, 1718.5349671207687, -16399.10487991298, 41807.79335675523, -83808.78790259302, -5549.667886812695, 9098.05631093482, -16399.10487991298, -21442899.9357, 1.37646, SYM
37, 201401, 2013 - 12 - 20 16:15:00, -108.0, GEE1, PUT, STRAT, 140.0, 140.345, 0.07231398622706062, 0.008813407863715872, 0.2318116692147143, -0.357200149447554, 0.391592427081917, 4.915801583071703, -20.16670499598669, 38.577616140335834, -42.29198212484704, -530.9065709717439, 2178.0041395665626, -34460.58494238685, 74523.96059955555, -114660.94716715509, -7307.7165867976655, 11530.52145364535, -34460.58494238685, -20863362.0996, 1.37646, SYM
38, 201401, 2013 - 12 - 20 16:15:00, -83.0, GEE1, PUT, STRAT, 141.0, 140.345, 0.07172143045750252, 0.008813407863715872, 0.7922715181315709, -0.7543151841866509, 0.333159035321538, 4.147995696473539, -16.876460506586433, 62.608160287492026, -27.652199931687655, -344.28364280730375, 1400.746222046674, -90513.99446933273, 120945.99245071695, -74969.94172708844, -4738.926629785414, 7415.658249224481, -15682.746569332587, -16033880.132100001, 1.37646, SYM
39, 201401, 2013 - 12 - 20 16:15:00, -56.0, GEE1, PUT, STRAT, 141.5, 140.345, 0.0739452718231504, 0.008813407863715872, 1.212080035129219, -0.88042603375236, 0.20479158314197934, 2.628816497069195, -11.026098543797652, 49.30385789013216, -11.468328655950843, -147.21372383587493, 617.4615184526685, -93429.26236862202, 95244.83704343032, -31092.641206404707, -2026.3380231112837, 3268.888775728308, -4399.8295686219335, -10818039.607199999, 1.37646, SYM"""
    csv = StringIO(csv)
    df = read_csv(csv).set_index(['index'])
    for _ in range(10):
        library.write('pandas', df[:-2])
        result = library.read('pandas').data
        assert len(result) == len(df[:-2])
        assert np.all(df[:-2].values == result.values)
        assert np.all(df[:-2].columns.values == result.columns.values)
    for _ in range(10):
        library.write('pandas', df[:-1])
        result = library.read('pandas').data
        assert len(result) == len(df[:-1])
        assert np.all(df[:-1].values == result.values)
        assert np.all(df[:-1].columns.values == result.columns.values)
    for _ in range(10):
        library.write('pandas', df)
        result = library.read('pandas').data
        assert len(result) == len(df)
        assert np.all(df.values == result.values)
        assert np.all(df.columns.values == result.columns.values)


def test_large_dataframe_rewrite_same_item(library):
    csv = \
"""index, f1, f2, f3, f4, f5, f6, f7, f8, iVol, tau, uPrice, uDelta, uGamma, uVega, uTheta, Delta, Gamma, Vega, Theta, $Price, $Delta, $Gamma, $Vega, $Theta, $Time_Value, $Notional, FX, f9
0, 201401, 2013 - 12 - 20 16:15:00, 15.0, F1, CALL, STRAT, 140.0, 140.345, 0.07231398622706062, 0.008813407863715872, 0.5768068954653813, 0.6427860135978315, 0.391592427081917, 4.915801583071703, -20.166163353481476, 9.641790203967473, 5.873886406228755, 73.73702374607555, -302.49245030222215, 11909.274289984183, 18625.940769791625, 15925.131550993763, 1014.9606370552315, -1601.4183005499872, 4786.093789984206, 2897689.1805000002, 1.37646, SYM
1, 201401, 2013 - 12 - 20 16:15:00, 15.0, F1, PUT, STRAT, 140.0, 140.345, 0.07231398622706062, 0.008813407863715872, 0.2318116692147143, -0.357200149447554, 0.391592427081917, 4.915801583071703, -20.16670499598669, -5.358002241713311, 5.873886406228755, 73.73702374607555, -302.50057493980034, 4786.192353109285, -10350.550083271604, 15925.131550993763, 1014.9606370552315, -1601.4613130062987, 4786.192353109285, 2897689.1805000002, 1.37646, SYM
2, 201401, 2013 - 12 - 20 16:15:00, -48.0, F22, CALL, STRAT, 141.5, 140.345, 0.0739452718231504, 0.008813407863715872, 0.05709601681178711, 0.11956012929302556, 0.20479158314197934, 2.628816497069195, -11.027911868706408, -5.738886206065227, -9.829995990815009, -126.18319185932137, 529.3397696979075, -3772.3383984361194, -11086.338978290602, -26650.835319775462, -1736.8611626668148, 2802.3654592245452, -3772.3383984361194, -9272605.3776, 1.37646, SYM
3, 201402, 2014 - 01 - 24 16:15:00, -286.0, F22, CALL, STRAT, 141.5, 140.345, 0.045487609195962696, 0.10463818541333941, 0.3747457492377393, 0.29120692771365, 0.1660598823861943, 15.56832633851715, -3.3830120036011397, -83.2851813261039, -47.49312636245157, -4452.541332815905, 967.541433029926, -147525.24472279268, -160889.7125497546, -128762.15724702866, -61287.4504296778, 5122.238772724507, -147525.24472279268, -55249273.7082, 1.37646, SYM
4, 201402, 2014 - 01 - 24 16:15:00, -264.0, F22, CALL, STRAT, 142.0, 140.345, 0.044822991783170785, 0.10463818541333941, 0.24229877494137142, 0.21142760067302388, 0.14217904830463807, 13.134711351643713, -2.812643033008342, -55.816886577678304, -37.53526875242445, -3467.56379683394, 742.5377607142022, -88047.84694353123, -107826.65888355605, -101764.66675460352, -47729.62863790045, 3931.052023510272, -88047.84694353123, -50999329.576799996, 1.37646, SYM
5, 201401, 2013 - 12 - 20 16:15:00, -350.0, F22, CALL, STRAT, 142.0, 140.345, 0.07732984880519912, 0.008813407863715872, 0.022997617617102506, 0.053564485523868555, 0.10692101346714668, 1.4353175202195965, -6.296783951449458, -18.747569933353994, -37.422354713501335, -502.3611320768588, 2203.8743830073104, -11079.355260832921, -36216.420371031316, -101458.53708176922, -6914.80003858513, 11667.480512439395, -11079.355260832921, -67612747.545, 1.37646, SYM
6, 201402, 2014 - 01 - 24 16:15:00, -43.0, F22, CALL, STRAT, 142.5, 140.345, 0.04429193547308161, 0.10463818541333941, 0.14930517833206025, 0.14535540627931182, 0.11352765189447668, 10.36359429711007, -2.1930395074393734, -6.250282470010408, -4.881689031462497, -445.634554775733, 94.30069881989306, -8837.042047978748, -12074.25059227865, -13235.111243323556, -6133.9813926660545, 499.23515345242305, -8837.042047978748, -8306708.9841, 1.37646, SYM
7, 201401, 2013 - 12 - 20 16:15:00, -557.0, F22, CALL, STRAT, 142.5, 140.345, 0.0814452531405243, 0.008813407863715872, 0.009355428262274312, 0.02334242880598363, 0.05141464658820557, 0.7269263150873877, -3.358771076933658, -13.001732844932882, -28.637958149630503, -404.89795750367495, 1870.8354898520474, -7172.696641740786, -25116.653728342328, -77642.50435641785, -5573.258425855083, 9904.346993699035, -7172.696641740786, -107600858.2359, 1.37646, SYM
8, 201401, 2013 - 12 - 20 16:15:00, -607.0, F22, CALL, STRAT, 143.0, 140.345, 0.08598678226600448, 0.008813407863715872, 0.003929576582252237, 0.010236258301012439, 0.024009328219809185, 0.35838470316321597, -1.748258969026736, -6.21340878871455, -14.573662229424174, -217.5395148200721, 1061.1931941992289, -3283.2053243209966, -12003.018280721177, -39511.74267470002, -2994.344405692364, 5618.038400336425, -3283.2053243209966, -117259822.1709, 1.37646, SYM
9, 201401, 2013 - 12 - 20 16:15:00, -799.0, F22, CALL, STRAT, 143.5, 140.345, 0.09076344895187359, 0.008813407863715872, 0.0017194411099074047, 0.004596451952699387, 0.01121737082629775, 0.1767420247600966, -0.9100718136522263, -3.67256511020681, -8.962679290211902, -141.2168777833172, 727.1473791081288, -1891.026786204374, -7094.634789685377, -24299.388322293227, -1943.793835936248, 3849.574159412212, -1891.026786204374, -154350243.6813, 1.37646, SYM
10, 201401, 2013 - 12 - 20 16:15:00, -377.0, F22, CALL, STRAT, 144.0, 140.345, 0.09566038240450792, 0.008813407863715872, 0.0007852689424384662, 0.0021295289144923784, 0.005324993197820229, 0.08842782200919548, -0.47989481865526434, -0.8028324007636266, -2.007522435578226, -33.3372888974667, 180.92034663303465, -407.4960157678369, -1550.905840965067, -5442.743810001693, -458.87444675807006, 957.8062320250265, -407.4960157678369, -72828588.06989999, 1.37646, SYM
11, 201402, 2014 - 01 - 24 16:15:00, -43.0, F22, PUT, STRAT, 137.5, 140.345, 0.05414565513055749, 0.10463818541333941, 0.14529132959784974, -0.11936326135136956, 0.08106840033227831, 9.046889913827847, -2.3403474666535415, 5.132620238108891, -3.4859412142879673, -389.0162662945974, 100.63494106610229, -8599.471252145018, 9915.158754388978, -9450.995231657676, -5354.653299038616, 532.7691191532583, -8599.471252145018, -8306708.9841, 1.37646, SYM
12, 201402, 2014 - 01 - 24 16:15:00, -264.0, F22, PUT, STRAT, 138.0, 140.345, 0.052853182910226726, 0.10463818541333941, 0.20369081242765574, -0.16004607860136968, 0.10141337819029916, 11.047155968410756, -2.789510903380204, 42.252164750761594, -26.77313184223898, -2916.44917566044, 736.4308784923738, -74018.27549798116, 81622.4271006569, -72586.63466280713, -40143.75632329569, 3898.7217192677417, -74018.27549798116, -50999329.576799996, 1.37646, SYM
13, 201401, 2013 - 12 - 20 16:15:00, -376.0, F22, PUT, STRAT, 138.0, 140.345, 0.08897789701177691, 0.008813407863715872, 0.009425028910330369, -0.021620830082859088, 0.04411750741642045, 0.6814450839280415, -3.43983227630679, 8.129432111155017, -16.588182788574088, -256.2233515569436, 1293.376935891353, -4877.913910511415, 15704.378314735444, -44973.45961948536, -3526.811944840706, 6847.236989142353, -4877.913910511415, -72635408.7912, 1.37646, SYM
14, 201401, 2013 - 12 - 20 16:15:00, -301.0, F22, PUT, STRAT, 138.5, 140.345, 0.08383267513417192, 0.008813407863715872, 0.020991265826436845, -0.045956251827941025, 0.08727871921287762, 1.2701629715541363, -6.0408289559434, 13.832831800210249, -26.270894483076166, -382.319054437795, 1818.2895157389635, -8696.984965596635, 26722.164695430383, -71224.98149804553, -5262.468856714474, 9626.164564746361, -8696.984965596635, -58146962.8887, 1.37646, SYM
15, 201402, 2014 - 01 - 24 16:15:00, -286.0, F22, PUT, STRAT, 138.5, 140.345, 0.051599724402617266, 0.10463818541333941, 0.28321473137770425, -0.21146513081873966, 0.12351912253075312, 13.136076509490826, -3.2382097361444653, 60.479027414159546, -35.32646904379539, -3756.917881714376, 926.127984537317, -111492.45225751627, 116832.94892344868, -95776.22511698281, -51712.4718746457, 4902.992790754752, -111492.45225751627, -55249273.7082, 1.37646, SYM
16, 201401, 2013 - 12 - 20 16:15:00, -739.0, F22, PUT, STRAT, 139.0, 140.345, 0.0791166184474159, 0.008813407863715872, 0.047581495319667155, -0.0967612790459439, 0.16434769983129724, 2.257195133461944, -10.131173555213623, 71.50658521495254, -121.45295017532867, -1668.0672036283765, 7486.937257302868, -48400.084510256995, 138135.90554124617, -329280.15202122304, -22960.277831063155, 39636.42175841195, -48400.084510256995, -142759486.9593, 1.37646, SYM
17, 201401, 2013 - 12 - 20 16:15:00, -669.0, F22, PUT, STRAT, 139.5, 140.345, 0.07513349054261133, 0.008813407863715872, 0.10733307441031315, -0.1949726645282245, 0.27848967340302655, 3.6322892048663644, -15.482297001088007, 130.4367125693822, -186.30959150662477, -2430.001478055598, 10357.656693727877, -98837.84833028633, 251976.70050152476, -505117.8297913038, -33447.99834484408, 54834.231279417974, -98837.84833028633, -129236937.4503, 1.37646, SYM
18, 201401, 2013 - 12 - 20 16:15:00, -471.0, F22, PUT, STRAT, 140.0, 140.345, 0.07231398622706062, 0.008813407863715872, 0.2318116692147143, -0.357200149447554, 0.391592427081917, 4.915801583071703, -20.16670499598669, 168.24127038979793, -184.4400331555829, -2315.3425456267723, 9498.518053109732, -150286.43988763154, 325007.2726147283, -500049.1307012041, -31869.76400353427, 50285.885228397776, -150286.43988763154, -90987440.2677, 1.37646, SYM
19, 201401, 2013 - 12 - 20 16:15:00, -364.0, F22, PUT, STRAT, 141.0, 140.345, 0.07172143045750252, 0.008813407863715872, 0.7922715181315709, -0.7543151841866509, 0.333159035321538, 4.147995696473539, -16.876460506586433, 274.5707270439409, -121.26988885703983, -1509.8704335163682, 6143.031624397461, -396952.9396004471, 530413.7500248309, -328783.8408272312, -20782.762569179402, 32521.681960454345, -68777.34640044652, -70317257.4468, 1.37646, SYM
20, 201401, 2013 - 12 - 20 16:15:00, -394.0, F22, PUT, STRAT, 141.5, 140.345, 0.0739452718231504, 0.008813407863715872, 1.212080035129219, -0.88042603375236, 0.20479158314197934, 2.628816497069195, -11.026098543797652, 346.8878572984298, -80.68788375793986, -1035.7536998452629, 4344.282826256274, -657341.595950662, 670115.460626992, -218758.93991649026, -14256.735376890107, 22998.967457802737, -30955.94375066146, -76112635.8078, 1.37646, SYM
21, 201402, 2014 - 01 - 24 16:15:00, -40.0, GEE1, CALL, STRAT, 141.5, 140.345, 0.045487609195962696, 0.10463818541333941, 0.3747457492377393, 0.29120692771365, 0.1660598823861943, 15.56832633851715, -3.3830120036011397, -11.648277108545999, -6.642395295447772, -622.733053540686, 135.32048014404558, -20632.901359831147, -22502.057699266377, -18008.69332126275, -8571.671388766126, 716.3970311502808, -20632.901359831147, -7727171.148, 1.37646, SYM
22, 201401, 2013 - 12 - 20 16:15:00, -12.0, GEE1, CALL, STRAT, 141.5, 140.345, 0.0739452718231504, 0.008813407863715872, 0.05709601681178711, 0.11956012929302556, 0.20479158314197934, 2.628816497069195, -11.027911868706408, -1.4347215515163068, -2.4574989977037522, -31.545797964830342, 132.33494242447688, -943.0845996090299, -2771.5847445726504, -6662.708829943866, -434.2152906667037, 700.5913648061363, -943.0845996090299, -2318151.3444, 1.37646, SYM
23, 201402, 2014 - 01 - 24 16:15:00, -45.0, GEE1, CALL, STRAT, 142.0, 140.345, 0.044822991783170785, 0.10463818541333941, 0.24229877494137142, 0.21142760067302388, 0.14217904830463807, 13.134711351643713, -2.812643033008342, -9.514242030286075, -6.398057173708713, -591.0620108239671, 126.56893648537539, -15008.155729011005, -18379.544127878875, -17346.250014989233, -8135.732154187577, 670.0656858256148, -15008.155729011005, -8693067.5415, 1.37646, SYM
24, 201401, 2013 - 12 - 20 16:15:00, -57.0, GEE1, CALL, STRAT, 142.0, 140.345, 0.07732984880519912, 0.008813407863715872, 0.022997617617102506, 0.053564485523868555, 0.10692101346714668, 1.4353175202195965, -6.296783951449458, -3.0531756748605074, -6.09449776762736, -81.813098652517, 358.9166852326191, -1804.3521424785042, -5898.102746139386, -16523.247467602414, -1126.1245777124357, 1900.1325405972727, -1804.3521424785042, -11011218.8859, 1.37646, SYM
25, 201401, 2013 - 12 - 20 16:15:00, -68.0, GEE1, CALL, STRAT, 142.5, 140.345, 0.0814452531405243, 0.008813407863715872, 0.009355428262274312, 0.02334242880598363, 0.05141464658820557, 0.7269263150873877, -3.358771076933658, -1.5872851588068868, -3.496195967997979, -49.430989425942364, 228.39643323148874, -875.6613494405268, -3066.306020695293, -9478.797659311334, -680.3977970523262, 1209.1482864839038, -875.6613494405268, -13136190.9516, 1.37646, SYM
26, 201402, 2014 - 01 - 24 16:15:00, -19.0, GEE1, CALL, STRAT, 142.5, 140.345, 0.04429193547308161, 0.10463818541333941, 0.14930517833206025, 0.14535540627931182, 0.11352765189447668, 10.36359429711007, -2.1930395074393734, -2.7617527193069247, -2.1570253859950568, -196.90829164509134, 41.66775064134809, -3904.7395095720058, -5335.133982634753, -5848.072409840642, -2710.3638711780245, 220.5922771068846, -3904.7395095720058, -3670406.2953000003, 1.37646, SYM
27, 201401, 2013 - 12 - 20 16:15:00, -91.0, GEE1, CALL, STRAT, 143.0, 140.345, 0.08598678226600448, 0.008813407863715872, 0.003929576582252237, 0.010236258301012439, 0.024009328219809185, 0.35838470316321597, -1.748258969026736, -0.9314995053921319, -2.1848488680026357, -32.613007987852654, 159.091566181433, -492.21035339902915, -1799.464025610588, -5923.5067271790795, -448.9050097495967, 842.2429891772894, -492.21035339902915, -17579314.3617, 1.37646, SYM
28, 201401, 2013 - 12 - 20 16:15:00, -117.0, GEE1, CALL, STRAT, 143.5, 140.345, 0.09076344895187359, 0.008813407863715872, 0.0017194411099074047, 0.004596451952699387, 0.01121737082629775, 0.1767420247600966, -0.9100718136522263, -0.5377848784658282, -1.3124323866768368, -20.678816896931302, 106.47840219731049, -276.9088034867481, -1038.8889491779587, -3558.233333802638, -284.63564305950064, 563.7048518788846, -276.9088034867481, -22601975.6079, 1.37646, SYM
29, 201401, 2013 - 12 - 20 16:15:00, -126.0, GEE1, CALL, STRAT, 144.0, 140.345, 0.09566038240450792, 0.008813407863715872, 0.0007852689424384662, 0.0021295289144923784, 0.005324993197820229, 0.08842782200919548, -0.47989481865526434, -0.26832064322603966, -0.6709491429253489, -11.141905573158631, 60.46674715056331, -136.19230235211526, -518.3398831872638, -1819.0602654117067, -153.3638734522993, 320.1156107033245, -136.19230235211526, -24340589.1162, 1.37646, SYM
30, 201402, 2014 - 01 - 24 16:15:00, -19.0, GEE1, PUT, STRAT, 137.5, 140.345, 0.05414565513055749, 0.10463818541333941, 0.14529132959784974, -0.11936326135136956, 0.08106840033227831, 9.046889913827847, -2.3403474666535415, 2.2679019656760215, -1.5402996063132879, -171.8909083627291, 44.46660186641729, -3799.766367226869, 4381.11665891606, -4176.021148871998, -2366.009597249621, 235.40961078864902, -3799.766367226869, -3670406.2953000003, 1.37646, SYM
31, 201401, 2013 - 12 - 20 16:15:00, -64.0, GEE1, PUT, STRAT, 138.0, 140.345, 0.08897789701177691, 0.008813407863715872, 0.009425028910330369, -0.021620830082859088, 0.04411750741642045, 0.6814450839280415, -3.43983227630679, 1.3837331253029816, -2.8235204746509086, -43.612485371394655, 220.14926568363455, -830.2832188104537, 2673.0856705932674, -7655.056956508147, -600.3084161430988, 1165.48714708806, -830.2832188104537, -12363473.8368, 1.37646, SYM
32, 201402, 2014 - 01 - 24 16:15:00, -45.0, GEE1, PUT, STRAT, 138.0, 140.345, 0.052853182910226726, 0.10463818541333941, 0.20369081242765574, -0.16004607860136968, 0.10141337819029916, 11.047155968410756, -2.789510903380204, 7.2020735370616356, -4.563602018563462, -497.122018578484, 125.52799065210918, -12616.751505337697, 13912.913710339246, -12372.721817523941, -6842.685736925402, 664.5548385115469, -12616.751505337697, -8693067.5415, 1.37646, SYM
33, 201401, 2013 - 12 - 20 16:15:00, -51.0, GEE1, PUT, STRAT, 138.5, 140.345, 0.08383267513417192, 0.008813407863715872, 0.020991265826436845, -0.045956251827941025, 0.08727871921287762, 1.2701629715541363, -6.0408289559434, 2.3437688432249923, -4.451214679856759, -64.77831154926095, 308.08227675311343, -1473.5755257323203, 4527.675745737374, -12068.020120931302, -891.6475471509574, 1631.011271767656, -1473.5755257323203, -9852143.2137, 1.37646, SYM
34, 201402, 2014 - 01 - 24 16:15:00, -40.0, GEE1, PUT, STRAT, 138.5, 140.345, 0.051599724402617266, 0.10463818541333941, 0.28321473137770425, -0.21146513081873966, 0.12351912253075312, 13.136076509490826, -3.2382097361444653, 8.458605232749587, -4.940764901230125, -525.443060379633, 129.5283894457786, -15593.349966086193, 16340.27257670611, -13395.276240137457, -7232.5135489014965, 685.733257448217, -15593.349966086193, -7727171.148, 1.37646, SYM
35, 201401, 2013 - 12 - 20 16:15:00, -98.0, GEE1, PUT, STRAT, 139.0, 140.345, 0.0791166184474159, 0.008813407863715872, 0.047581495319667155, -0.0967612790459439, 0.16434769983129724, 2.257195133461944, -10.131173555213623, 9.4826053465025, -16.10607458346713, -221.20512307927052, 992.855008410935, -6418.414454675487, 18318.42861034117, -43666.38010565609, -3044.8000371369267, 5256.250787989675, -6418.414454675487, -18931569.312599998, 1.37646, SYM
36, 201401, 2013 - 12 - 20 16:15:00, -111.0, GEE1, PUT, STRAT, 139.5, 140.345, 0.07513349054261133, 0.008813407863715872, 0.10733307441031315, -0.1949726645282245, 0.27848967340302655, 3.6322892048663644, -15.482297001088007, 21.64196576263292, -30.912353747735946, -403.18410174016645, 1718.5349671207687, -16399.10487991298, 41807.79335675523, -83808.78790259302, -5549.667886812695, 9098.05631093482, -16399.10487991298, -21442899.9357, 1.37646, SYM
37, 201401, 2013 - 12 - 20 16:15:00, -108.0, GEE1, PUT, STRAT, 140.0, 140.345, 0.07231398622706062, 0.008813407863715872, 0.2318116692147143, -0.357200149447554, 0.391592427081917, 4.915801583071703, -20.16670499598669, 38.577616140335834, -42.29198212484704, -530.9065709717439, 2178.0041395665626, -34460.58494238685, 74523.96059955555, -114660.94716715509, -7307.7165867976655, 11530.52145364535, -34460.58494238685, -20863362.0996, 1.37646, SYM
38, 201401, 2013 - 12 - 20 16:15:00, -83.0, GEE1, PUT, STRAT, 141.0, 140.345, 0.07172143045750252, 0.008813407863715872, 0.7922715181315709, -0.7543151841866509, 0.333159035321538, 4.147995696473539, -16.876460506586433, 62.608160287492026, -27.652199931687655, -344.28364280730375, 1400.746222046674, -90513.99446933273, 120945.99245071695, -74969.94172708844, -4738.926629785414, 7415.658249224481, -15682.746569332587, -16033880.132100001, 1.37646, SYM
39, 201401, 2013 - 12 - 20 16:15:00, -56.0, GEE1, PUT, STRAT, 141.5, 140.345, 0.0739452718231504, 0.008813407863715872, 1.212080035129219, -0.88042603375236, 0.20479158314197934, 2.628816497069195, -11.026098543797652, 49.30385789013216, -11.468328655950843, -147.21372383587493, 617.4615184526685, -93429.26236862202, 95244.83704343032, -31092.641206404707, -2026.3380231112837, 3268.888775728308, -4399.8295686219335, -10818039.607199999, 1.37646, SYM"""
    csv = StringIO(csv)
    df = read_csv(csv).set_index(['index'])
    for _ in range(100):
        library.write('pandas', df)
        result = library.read('pandas').data
        assert len(result) == len(df)
        assert np.all(df.values == result.values)
        assert np.all(df.columns.values == result.columns.values)


def test_append_after_truncate_after_append(library):
    columns = ['MAIN_UPPER', 'MAIN_LOWER', 'AUX_UPPER', 'AUX_LOWER', 'TARGET_HEDGE_POSITION']
    empty_df = DataFrame(columns=columns, dtype=np.float64)
    library.write('sym', empty_df)
    full_df = DataFrame(data=[np.zeros(5)], columns=columns)
    library.write('sym', full_df)
    library.write('sym', empty_df)
    full_df = DataFrame(data=[np.zeros(5)], columns=columns)
    library.write('sym', full_df)
    assert len(library.read('sym', 1).data) == 0
    assert len(library.read('sym', 2).data) == 1
    assert len(library.read('sym', 3).data) == 0
    assert len(library.read('sym', 4).data) == 1


def test_can_write_pandas_df_with_object_columns(library):
    expected = DataFrame(data=dict(A=['a', 'b', None, 'c'], B=[1., 2., 3., 4.]), index=range(4))
    library.write('objects', expected)
    saved_df = library.read('objects').data

    assert_frame_equal(saved_df, expected)


def panel(i1, i2, i3):
    return Panel(np.random.randn(i1, i2, i3), range(i1), ['A%d' % i for i in range(i2)],
                 list(rrule(DAILY, count=i3, dtstart=dt(1970, 1, 1), interval=1)))


@pytest.mark.xfail(pd.__version__ >= '0.18.0', reason="see issue #115")
@pytest.mark.parametrize("df_size", list(itertools.combinations_with_replacement([1, 2, 4], r=3)))
def test_panel_save_read(library, df_size):
    '''Note - empties are not tested here as they don't work!'''
    pn = panel(*df_size)
    library.write('pandas', pn)
    result = library.read('pandas').data
    assert np.all(pn.values == result.values), str(pn.values) + "!=" + str(result.values)
    for i in range(3):
        assert np.all(pn.axes[i] == result.axes[i])
        if None not in pn.axes[i].names:
            assert np.all(pn.axes[i].names == result.axes[i].names), \
                str(pn.axes[i].names) + "!=" + str(pn.axes[i].names)


@pytest.mark.xfail(pd.__version__ >= '0.20.0', reason='Panel is deprecated')
def test_panel_save_read_with_nans(library):
    '''Ensure that nan rows are not dropped when calling to_frame.'''
    df1 = DataFrame(data=np.arange(4).reshape((2, 2)), index=['r1', 'r2'], columns=['c1', 'c2'])
    df2 = DataFrame(data=np.arange(6).reshape((3, 2)), index=['r1', 'r2', 'r3'], columns=['c1', 'c2'])
    p_in = Panel(data=dict(i1=df1, i2=df2))

    library.write('pandas', p_in)
    p_out = library.read('pandas').data

    assert p_in.shape == p_out.shape
    # check_names is False because pandas helpfully names the axes for us.
    assert_frame_equal(p_in.iloc[0], p_out.iloc[0], check_names=False)  
    assert_frame_equal(p_in.iloc[1], p_out.iloc[1], check_names=False)  


def test_save_read_ints(library):
    ts1 = DataFrame(index=[dt(2012, 1, 1) + dtd(hours=x) for x in range(5)],
                    data={'col1':np.arange(5), 'col2':np.arange(5)})
    ts1.index.name = 'index'
    library.write('TEST_1', ts1)
    ts2 = library.read('TEST_1').data
    assert_frame_equal(ts1, ts2)


def test_save_read_datetimes(library):
    # FEF symbols have datetimes in the CLOSE_REVISION field.  Handle specially.
    ts1 = DataFrame(index=[dt(2012, 1, 1) + dtd(hours=x) for x in range(3)],
                    data={'field1': [1, 2, 3],
                          'revision': [dt(2013, 1, 1), dt(2013, 1, 2), dt(2013, 1, 3)],
                          'field2': [4, 5, 6]},
                    )
    ts1.index.name = 'index'
    library.write('TEST_1', ts1)
    ts2 = library.read('TEST_1').data
    assert_frame_equal(ts1, ts2)


def test_labels(library):
    ts1 = DataFrame(index=[dt(2012, 1, 1), dt(2012, 1, 2)],
                    data={'data': [1., 2.]})
    ts1.index.name = 'some_index'
    library.write('TEST_1', ts1)
    ts2 = library.read('TEST_1').data
    assert_frame_equal(ts1, ts2)


def test_duplicate_labels(library):
    ts1 = DataFrame(index=[dt(2012, 1, 1) + dtd(hours=x) for x in range(5)],
                    data=[[np.arange(5), np.arange(5, 10)]],
                    columns=['a', 'a']
                    )
    library.write('TEST_1', ts1)
    ts2 = library.read('TEST_1').data
    assert_frame_equal(ts1, ts2)


def test_no_labels(library):
    ts1 = DataFrame(index=[dt(2012, 1, 1) + dtd(hours=x) for x in range(5)],
                    data=[[np.arange(5), np.arange(5, 10)]])
    library.write('TEST_1', ts1)
    ts2 = library.read('TEST_1').data
    assert_frame_equal(ts1, ts2)


@pytest.mark.xfail(reason='needs investigating')
def test_no_index_labels(library):
    ts1 = DataFrame(index=[dt(2012, 1, 1), dt(2012, 1, 2)],
                    data={'data': [1., 2.]})
    library.write('TEST_1', ts1)
    ts2 = library.read('TEST_1').data
    assert_frame_equal(ts1, ts2)


def test_not_unique(library):
    d = dt.now()
    ts = DataFrame(index=[d, d], data={'near': [1., 2.]})
    ts.index.name = 'index'
    library.write('ts', ts)
    ts2 = library.read('ts').data
    assert_frame_equal(ts, ts2)


def test_daterange_end(library):
    df = DataFrame(index=date_range(dt(2001, 1, 1), freq='S', periods=30 * 1024),
                   data=np.tile(np.arange(30 * 1024), 100).reshape((-1, 100)))
    df.columns = [str(c) for c in df.columns]
    library.write('MYARR', df)
    mdecompressALL = Mock(side_effect=decompress)
    with patch('arctic.store._ndarray_store.decompress', mdecompressALL):
        library.read('MYARR').data
    mdecompressLR = Mock(side_effect=decompress)
    with patch('arctic.store._ndarray_store.decompress', mdecompressLR):
        result = library.read('MYARR', date_range=DateRange(df.index[-1], df.index[-1])).data
    assert len(result) == 1
    assert mdecompressLR.call_count < mdecompressALL.call_count


def test_daterange_start(library):
    df = DataFrame(index=date_range(dt(2001, 1, 1), freq='S', periods=30 * 1024),
                   data=np.tile(np.arange(30 * 1024), 100).reshape((-1, 100)))
    df.columns = [str(c) for c in df.columns]
    library.write('MYARR', df)
    mdecompressALL = Mock(side_effect=decompress)
    with patch('arctic.store._ndarray_store.decompress', mdecompressALL):
        library.read('MYARR').data
    mdecompressLR = Mock(side_effect=decompress)
    with patch('arctic.store._ndarray_store.decompress', mdecompressLR):
        result = library.read('MYARR', date_range=DateRange(end=df.index[0])).data
    assert len(result) == 1
    assert mdecompressLR.call_count < mdecompressALL.call_count
    end = df.index[0] + dtd(milliseconds=1)
    result = library.read('MYARR', date_range=DateRange(end=end)).data
    assert len(result) == 1


def test_daterange_large_DataFrame(library):
    df = DataFrame(index=date_range(dt(2001, 1, 1), freq='S', periods=30 * 1024),
                   data=np.tile(np.arange(30 * 1024), 100).reshape((-1, 100)))
    df.columns = [str(c) for c in df.columns]
    library.write('MYARR', df)
    # assert saved
    saved_arr = library.read('MYARR').data
    assert_frame_equal(df, saved_arr, check_names=False)
    # first 100
    result = library.read('MYARR', date_range=DateRange(df.index[0], df.index[100])).data
    assert_frame_equal(df[df.index[0]:df.index[100]], result, check_names=False)
    # second 100
    result = library.read('MYARR', date_range=DateRange(df.index[100], df.index[200])).data
    assert_frame_equal(df[df.index[100]:df.index[200]], result, check_names=False)
    # first row
    result = library.read('MYARR', date_range=DateRange(df.index[0], df.index[0])).data
    assert_frame_equal(df[df.index[0]:df.index[0]], result, check_names=False)
    # last 100
    result = library.read('MYARR', date_range=DateRange(df.index[-100])).data
    assert_frame_equal(df[df.index[-100]:], result, check_names=False)
    # last 200-100
    result = library.read('MYARR', date_range=DateRange(df.index[-200], df.index[-100])).data
    assert_frame_equal(df[df.index[-200]:df.index[-100]], result, check_names=False)
    # last row
    result = library.read('MYARR', date_range=DateRange(df.index[-1], df.index[-1])).data
    assert_frame_equal(df[df.index[-1]:df.index[-1]], result, check_names=False)
    # beyond last row
    result = library.read('MYARR', date_range=DateRange(df.index[-1], df.index[-1] + dtd(days=1))).data
    assert_frame_equal(df[df.index[-1]:df.index[-1]], result, check_names=False)
    # somewhere in time
    result = library.read('MYARR', date_range=DateRange(dt(2020, 1, 1), dt(2031, 9, 1))).data
    assert_frame_equal(df[dt(2020, 1, 1):dt(2031, 9, 1)], result, check_names=False)


def test_daterange_large_DataFrame_middle(library):
    df = DataFrame(index=date_range(dt(2001, 1, 1), freq='S', periods=30 * 1024),
                   data=np.tile(np.arange(30 * 1024), 100).reshape((-1, 100)))
    df.columns = [str(c) for c in df.columns]
    library.write('MYARR', df)
    # middle
    start = 100
    for end in np.arange(200, 30000, 1000):
        result = library.read('MYARR', date_range=DateRange(df.index[start], df.index[end])).data
        assert_frame_equal(df[df.index[start]:df.index[end]], result, check_names=False)
    # middle following
    for start in np.arange(200, 30000, 1000):
        for offset in (100, 300, 500):
            end = start + offset
            result = library.read('MYARR', date_range=DateRange(df.index[start], df.index[end])).data
            assert_frame_equal(df[df.index[start]:df.index[end]], result, check_names=False)


@pytest.mark.parametrize("df,assert_equal", [
    (DataFrame(index=date_range(dt(2001, 1, 1), freq='D', periods=30000),
               data=list(range(30000)), columns=['A']), assert_frame_equal),
    (Series(index=date_range(dt(2001, 1, 1), freq='D', periods=30000),
            data=range(30000)), assert_series_equal),
])
def test_daterange(library, df, assert_equal):
    df.index.name = 'idx'
    df.name = 'FOO'
    library.write('MYARR', df)
    # whole array
    saved_arr = library.read('MYARR').data
    assert_equal(df, saved_arr)
    assert_equal(df, library.read('MYARR', date_range=DateRange(df.index[0])).data)
    assert_equal(df, library.read('MYARR', date_range=DateRange(df.index[0], df.index[-1])).data)
    assert_equal(df, library.read('MYARR', date_range=DateRange()).data)
    assert_equal(df[df.index[10]:], library.read('MYARR', date_range=DateRange(df.index[10])).data)
    assert_equal(df[:df.index[10]], library.read('MYARR', date_range=DateRange(end=df.index[10])).data)
    assert_equal(df[df.index[-1]:], library.read('MYARR', date_range=DateRange(df.index[-1])).data)
    assert_equal(df[df.index[-1]:], library.read('MYARR', date_range=DateRange(df.index[-1], df.index[-1])).data)
    assert_equal(df[df.index[0]:df.index[0]], library.read('MYARR', date_range=DateRange(df.index[0], df.index[0])).data)
    assert_equal(df[:df.index[0]], library.read('MYARR', date_range=DateRange(end=df.index[0])).data)
    assert_equal(df[df.index[0] - DateOffset(days=1):],
                 library.read('MYARR', date_range=DateRange(df.index[0] - DateOffset(days=1))).data)
    assert_equal(df[df.index[-1] + DateOffset(days=1):],
                 library.read('MYARR', date_range=DateRange(df.index[-1] + DateOffset(days=1))).data)
    assert len(library.read('MYARR', date_range=DateRange(dt(1950, 1, 1), dt(1951, 1, 1))).data) == 0
    assert len(library.read('MYARR', date_range=DateRange(dt(2091, 1, 1), dt(2091, 1, 1))).data) == 0


def test_daterange_append(library):
    df = DataFrame(index=date_range(dt(2001, 1, 1), freq='S', periods=30 * 1024),
                   data=np.tile(np.arange(30 * 1024), 100).reshape((-1, 100)))
    df.columns = [str(c) for c in df.columns]
    df.index.name = 'idx'
    library.write('MYARR', df)
    # assert saved
    saved_arr = library.read('MYARR').data
    assert_frame_equal(df, saved_arr, check_names=False)
    # append two more rows
    rows = df.iloc[-2:].copy()
    rows.index = rows.index + dtd(days=1)
    library.append('MYARR', rows)
    # assert we can rows back out
    assert_frame_equal(rows, library.read('MYARR', date_range=DateRange(rows.index[0])).data)
    # assert we can read back the first array
    assert_frame_equal(df, library.read('MYARR', date_range=DateRange(df.index[0], df.index[-1])).data)
    # append two more rows
    rows1 = df.iloc[-2:].copy()
    rows1.index = rows1.index + dtd(days=2)
    library.append('MYARR', rows1)
    # assert we can read a mix of data
    assert_frame_equal(rows1, library.read('MYARR', date_range=DateRange(rows1.index[0])).data)
    assert_frame_equal(concat((df, rows, rows1)), library.read('MYARR').data)
    assert_frame_equal(concat((rows, rows1)), library.read('MYARR', date_range=DateRange(start=rows.index[0])).data)
    assert_frame_equal(concat((df, rows, rows1))[df.index[50]:rows1.index[-2]],
                       library.read('MYARR', date_range=DateRange(start=df.index[50], end=rows1.index[-2])).data)


def assert_range_slice(library, expected, date_range, **kwargs):
    assert_equals = assert_series_equal if isinstance(expected, Series) else assert_frame_equal
    assert_equals(expected, library.read('MYARR', date_range=date_range).data, **kwargs)


def test_daterange_single_chunk(library):
    df = read_csv(StringIO("""2015-08-10 00:00:00,200005,1.0
                              2015-08-10 00:00:00,200012,2.0
                              2015-08-10 00:00:00,200016,3.0
                              2015-08-11 00:00:00,200005,1.0
                              2015-08-11 00:00:00,200012,2,0
                              2015-08-11 00:00:00,200016,3.0"""), parse_dates=[0],
                  names=['date', 'security_id', 'value']).set_index(['date', 'security_id'])
    library.write('MYARR', df)
    assert_range_slice(library, df[dt(2015, 8, 11):], DateRange(dt(2015, 8, 11), dt(2015, 8, 11)))


def test_daterange_when_end_beyond_chunk_index(library):
    df = read_csv(StringIO("""2015-08-10 00:00:00,200005,1.0
                              2015-08-10 00:00:00,200012,2.0
                              2015-08-10 00:00:00,200016,3.0
                              2015-08-11 00:00:00,200005,1.0
                              2015-08-11 00:00:00,200012,2,0
                              2015-08-11 00:00:00,200016,3.0"""), parse_dates=[0],
                  names=['date', 'security_id', 'value']).set_index(['date', 'security_id'])
    library.write('MYARR', df)
    assert_range_slice(library, df[dt(2015, 8, 11):], DateRange(dt(2015, 8, 11), dt(2015, 8, 12)))


def test_daterange_when_end_beyond_chunk_index_no_start(library):
    df = read_csv(StringIO("""2015-08-10 00:00:00,200005,1.0
                              2015-08-10 00:00:00,200012,2.0
                              2015-08-10 00:00:00,200016,3.0
                              2015-08-11 00:00:00,200005,1.0
                              2015-08-11 00:00:00,200012,2,0
                              2015-08-11 00:00:00,200016,3.0"""), parse_dates=[0],
                  names=['date', 'security_id', 'value']).set_index(['date', 'security_id'])
    library.write('MYARR', df)
    assert_range_slice(library, df, DateRange(end=dt(2015, 8, 12)))


def test_daterange_fails_with_timezone_start(library):
    df = read_csv(StringIO("""2015-08-10 00:00:00,200005,1.0
                              2015-08-11 00:00:00,200016,3.0"""), parse_dates=[0],
                  names=['date', 'security_id', 'value']).set_index(['date', 'security_id'])
    library.write('MYARR', df)
    with pytest.raises(ValueError):
        library.read('MYARR', date_range=DateRange(start=dt(2015, 1, 1, tzinfo=mktz())))


def test_data_info_series(library):
    s = Series(data=[1, 2, 3], index=[4, 5, 6])
    library.write('pandas', s)
    md = library.get_info('pandas')
    assert md == {'dtype': [('index', '<i8'), ('values', '<i8')],
                  'col_names': {u'index': [u'index'], u'columns': [u'values']},
                  'type': u'pandasseries',
                  'handler': 'PandasSeriesStore',
                  'rows': 3,
                  'segment_count': 1,
                  'size': 48}


def test_data_info_df(library):
    s = DataFrame(data=[1, 2, 3], index=[4, 5, 6])
    library.write('pandas', s)
    md = library.get_info('pandas')
    assert md == {'dtype': [('index', '<i8'), ('0', '<i8')],
                  'col_names': {u'index': [u'index'], u'columns': [u'0']},
                  'type': u'pandasdf',
                  'handler': 'PandasDataFrameStore',
                  'rows': 3,
                  'segment_count': 1,
                  'size': 48}


def test_data_info_cols(library):
    i = MultiIndex.from_tuples([(1, "ab"), (2, "bb"), (3, "cb")])
    s = DataFrame(data=[100, 200, 300], index=i)
    library.write('test_data', s)
    md = library.get_info('test_data')
    # {'dtype': [('level_0', '<i8'), ('level_1', 'S2'), ('0', '<i8')],
    #                  'col_names': {u'index': [u'level_0', u'level_1'], u'columns': [u'0'], 'index_tz': [None, None]},
    #                  'type': u'pandasdf',
    #                  'handler': 'PandasDataFrameStore',
    #                  'rows': 3,
    #                  'segment_count': 1,
    #                  'size': 50}
    assert 'size' in md
    assert md['segment_count'] == 1
    assert md['rows'] == 3
    assert md['handler'] == 'PandasDataFrameStore'
    assert md['type'] == 'pandasdf'
    assert md['col_names'] == {'index': ['level_0', u'level_1'], 'columns': [u'0'], 'index_tz': [None, None]}
    assert len(md['dtype']) == 3
    assert md['dtype'][0][0] == 'level_0'
    assert md['dtype'][1][0] == 'level_1'
    assert md['dtype'][2][0] == '0'


def test_read_write_multiindex_store_keeps_timezone(library):
    """If I write a multi-index dataframe and reads it, the timezone of the index shouldn't change, right?"""
    hk, ny, ldn = mktz('Asia/Hong_Kong'), mktz('America/New_York'), mktz('Europe/London')
    row0 = [dt(2015, 1, 1, tzinfo=hk), dt(2015, 1, 1, tzinfo=ny), dt(2015, 1, 1, tzinfo=ldn), 0, 42]
    row1 = [dt(2015, 1, 2, tzinfo=hk), dt(2015, 1, 2, tzinfo=ny), dt(2015, 1, 2, tzinfo=ldn), 1, 43]
    df = DataFrame([row0, row1], columns=['dt_a', 'dt_b', 'dt_c', 'index_0', 'data'])
    df = df.set_index(['dt_a', 'dt_b', 'dt_c', 'index_0'])
    library.write('spam', df)
    assert list(library.read('spam').data.index[0]) == row0[:-1]
    assert list(library.read('spam').data.index[1]) == row1[:-1]

