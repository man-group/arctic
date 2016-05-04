from pandas import DataFrame, MultiIndex, Index, Series
from datetime import datetime as dt
from pandas.util.testing import assert_frame_equal, assert_series_equal
from arctic.date import DateRange
import pandas as pd
import numpy as np
import random
import pytest


def test_write_dataframe(chunkstore_lib):
    df = DataFrame(data={'data': [1, 2, 3]},
                   index=MultiIndex.from_tuples([(dt(2016, 1, 1), 1),
                                                 (dt(2016, 1, 2), 1),
                                                 (dt(2016, 1, 3), 1)],
                                                names=['date', 'id'])
                   )
    chunkstore_lib.write('test_df', df, 'D')
    read_df = chunkstore_lib.read('test_df')
    assert_frame_equal(df, read_df)


def test_overwrite_dataframe(chunkstore_lib):
    df = DataFrame(data={'data': [1, 2, 3, 4]},
                   index=MultiIndex.from_tuples([(dt(2016, 1, 1), 1),
                                                 (dt(2016, 1, 2), 1),
                                                 (dt(2016, 1, 3), 1),
                                                 (dt(2016, 1, 4), 1)],
                                                names=['date', 'id'])
                   )

    dg = DataFrame(data={'data': [1, 2, 3]},
                   index=MultiIndex.from_tuples([(dt(2016, 1, 1), 1),
                                                 (dt(2016, 1, 2), 1),
                                                 (dt(2016, 1, 3), 1)],
                                                names=['date', 'id'])
                   )
    chunkstore_lib.write('test_df', df, 'D')
    chunkstore_lib.write('test_df', dg, 'D')
    read_df = chunkstore_lib.read('test_df')
    assert_frame_equal(dg, read_df)


def test_write_read_with_daterange(chunkstore_lib):
    df = DataFrame(data={'data': [1, 2, 3]},
                   index=MultiIndex.from_tuples([(dt(2016, 1, 1), 1),
                                                 (dt(2016, 1, 2), 1),
                                                 (dt(2016, 1, 3), 1)],
                                                names=['date', 'id'])
                   )
    chunkstore_lib.write('test_df', df, 'D')
    read_df = chunkstore_lib.read('test_df', chunk_range=DateRange(dt(2016, 1, 1), dt(2016, 1, 2)))
    assert(len(read_df.index.get_level_values('date')) == 2)


def test_store_single_index_df(chunkstore_lib):
    df = DataFrame(data=[1, 2, 3],
                   index=Index(data=[dt(2016, 1, 1),
                                     dt(2016, 1, 2),
                                     dt(2016, 1, 3)],
                               name='date'),
                   columns=['data'])

    chunkstore_lib.write('chunkstore_test', df, chunk_size='D')
    ret = chunkstore_lib.read('chunkstore_test', chunk_range=DateRange(dt(2016, 1, 1), dt(2016, 1, 3)))
    assert_frame_equal(df, ret)


def test_no_range(chunkstore_lib):
    df = DataFrame(data=[1, 2, 3],
                   index=Index(data=[dt(2016, 1, 1),
                                     dt(2016, 1, 2),
                                     dt(2016, 1, 3)],
                               name='date'),
                   columns=['data'])

    chunkstore_lib.write('chunkstore_test', df, chunk_size='D')
    ret = chunkstore_lib.read('chunkstore_test')
    assert_frame_equal(df, ret)


def test_closed_open(chunkstore_lib):
    df = DataFrame(data=[1, 2, 3],
                   index=Index(data=[dt(2016, 1, 1),
                                     dt(2016, 1, 2),
                                     dt(2016, 1, 3)],
                               name='date'),
                   columns=['data'])

    chunkstore_lib.write('chunkstore_test', df, chunk_size='D')
    ret = chunkstore_lib.read('chunkstore_test', chunk_range=DateRange(dt(2016, 1, 1), None))
    assert_frame_equal(df, ret)


def test_open_closed(chunkstore_lib):
    df = DataFrame(data=[1, 2, 3],
                   index=Index(data=[dt(2016, 1, 1),
                                     dt(2016, 1, 2),
                                     dt(2016, 1, 3)],
                               name='date'),
                   columns=['data'])

    chunkstore_lib.write('chunkstore_test', df, chunk_size='D')
    ret = chunkstore_lib.read('chunkstore_test', chunk_range=DateRange(None, dt(2017, 1, 1)))
    assert_frame_equal(df, ret)


def test_pandas_datetime_index_store_series(chunkstore_lib):
    df = Series(data=[1, 2, 3],
                index=Index(data=[dt(2016, 1, 1),
                                  dt(2016, 1, 2),
                                  dt(2016, 1, 3)],
                            name='date'),
                name='data')
    chunkstore_lib.write('chunkstore_test', df, chunk_size='D')
    s = chunkstore_lib.read('chunkstore_test', chunk_range=DateRange(dt(2016, 1, 1), dt(2016, 1, 3)))
    assert_series_equal(s, df)


def test_monthly_df(chunkstore_lib):
    df = DataFrame(data=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                   index=Index(data=[dt(2016, 1, 1),
                                     dt(2016, 1, 2),
                                     dt(2016, 1, 3),
                                     dt(2016, 1, 4),
                                     dt(2016, 1, 5),
                                     dt(2016, 2, 1),
                                     dt(2016, 2, 2),
                                     dt(2016, 2, 3),
                                     dt(2016, 2, 4),
                                     dt(2016, 3, 1)],
                               name='date'),
                   columns=['data'])

    chunkstore_lib.write('chunkstore_test', df, chunk_size='M')
    ret = chunkstore_lib.read('chunkstore_test', chunk_range=DateRange(dt(2016, 1, 1), dt(2016, 1, 2)))
    assert len(ret) == 2
    # assert_frame_equal(df, chunkstore_lib.read('chunkstore_test') )


def test_yearly_df(chunkstore_lib):
    df = DataFrame(data=[1, 2, 3],
                   index=Index(data=[dt(2016, 1, 1),
                                     dt(2016, 2, 1),
                                     dt(2016, 3, 3)],
                               name='date'),
                   columns=['data'])

    chunkstore_lib.write('chunkstore_test', df, chunk_size='Y')
    ret = chunkstore_lib.read('chunkstore_test', chunk_range=DateRange(dt(2016, 1, 1), dt(2016, 3, 3)))
    assert_frame_equal(df, ret)


def test_yearly_series(chunkstore_lib):
    df = Series(data=[1, 2, 3],
                index=Index(data=[dt(2016, 1, 1),
                                  dt(2016, 2, 1),
                                  dt(2016, 3, 3)],
                            name='date'),
                name='data')

    chunkstore_lib.write('chunkstore_test', df, chunk_size='Y')
    ret = chunkstore_lib.read('chunkstore_test', chunk_range=DateRange(dt(2016, 1, 1), dt(2016, 3, 3)))
    assert_series_equal(df, ret)


def test_append_daily(chunkstore_lib):
    df = DataFrame(data=[1, 2, 3],
                   index=Index(data=[dt(2016, 1, 1),
                                     dt(2016, 1, 2),
                                     dt(2016, 1, 3)],
                               name='date'),
                   columns=['data'])

    chunkstore_lib.write('chunkstore_test', df, chunk_size='D')
    df2 = DataFrame(data=[4, 5, 6],
                    index=Index(data=[dt(2016, 1, 4),
                                      dt(2016, 1, 5),
                                      dt(2016, 1, 6)],
                                name='date'),
                    columns=['data'])
    chunkstore_lib.append('chunkstore_test', df2)
    ret = chunkstore_lib.read('chunkstore_test', chunk_range=DateRange(dt(2016, 1, 1), dt(2016, 1, 6)))
    assert_frame_equal(ret, pd.concat([df, df2]))


def test_append_monthly(chunkstore_lib):
    df = DataFrame(data=[1, 2, 3],
                   index=Index(data=[dt(2016, 1, 1),
                                     dt(2016, 2, 1),
                                     dt(2016, 3, 1)],
                               name='date'),
                   columns=['data'])

    chunkstore_lib.write('chunkstore_test', df, chunk_size='M')
    df2 = DataFrame(data=[4, 5, 6],
                    index=Index(data=[dt(2016, 4, 1),
                                      dt(2016, 5, 1),
                                      dt(2016, 6, 1)],
                                name='date'),
                    columns=['data'])
    chunkstore_lib.append('chunkstore_test', df2)
    ret = chunkstore_lib.read('chunkstore_test', chunk_range=DateRange(dt(2016, 1, 1), dt(2016, 12, 31)))
    assert_frame_equal(ret, pd.concat([df, df2]))


def test_append_yearly(chunkstore_lib):
    df = DataFrame(data=[1, 2, 3],
                   index=Index(data=[dt(2010, 1, 1),
                                     dt(2011, 1, 1),
                                     dt(2012, 1, 1)],
                               name='date'),
                   columns=['data'])

    chunkstore_lib.write('chunkstore_test', df, chunk_size='Y')
    df2 = DataFrame(data=[4, 5, 6],
                    index=Index(data=[dt(2013, 1, 1),
                                      dt(2014, 1, 1),
                                      dt(2015, 1, 1)],
                                name='date'),
                    columns=['data'])
    chunkstore_lib.append('chunkstore_test', df2)
    ret = chunkstore_lib.read('chunkstore_test', chunk_range=DateRange(dt(2000, 1, 1), dt(2100, 12, 31)))
    assert_frame_equal(ret, pd.concat([df, df2]))


def test_append_existing_chunk(chunkstore_lib):
    df = DataFrame(data=[1, 2, 3],
                   index=Index(data=[dt(2016, 1, 1),
                                     dt(2016, 1, 2),
                                     dt(2016, 1, 3)],
                               name='date'),
                   columns=['data'])

    chunkstore_lib.write('chunkstore_test', df, chunk_size='M')
    df2 = DataFrame(data=[4, 5, 6],
                    index=Index(data=[dt(2016, 1, 4),
                                      dt(2016, 1, 5),
                                      dt(2016, 1, 6)],
                                name='date'),
                    columns=['data'])
    chunkstore_lib.append('chunkstore_test', df2)
    ret = chunkstore_lib.read('chunkstore_test', chunk_range=DateRange(dt(2016, 1, 1), dt(2016, 1, 31)))
    assert_frame_equal(ret, pd.concat([df, df2]))


def test_append_exceptions(chunkstore_lib):
    df = DataFrame(data=[1, 2, 3],
                   index=Index(data=[dt(2016, 1, 1),
                                     dt(2016, 1, 2),
                                     dt(2016, 1, 3)],
                               name='date'),
                   columns=['data'])
    s = Series(data=[1, 2, 3],
               index=Index(data=[dt(2016, 1, 1),
                                 dt(2016, 2, 1),
                                 dt(2016, 3, 3)],
                           name='date'),
               name='data')

    chunkstore_lib.write('df', df, chunk_size='D')
    chunkstore_lib.write('s', s, chunk_size='D')

    with pytest.raises(Exception) as e:
        chunkstore_lib.append('df', s)

    assert("cannot append a series to a dataframe" in str(e))

    with pytest.raises(Exception) as e:
        chunkstore_lib.append('s', df)

    assert("cannot append a dataframe to a series" in str(e))


def test_store_objects_df(chunkstore_lib):
    df = DataFrame(data=['1', '2', '3'],
                   index=Index(data=[dt(2016, 1, 1),
                                     dt(2016, 1, 2),
                                     dt(2016, 1, 3)],
                               name='date'),
                   columns=['data'])

    chunkstore_lib.write('chunkstore_test', df, chunk_size='D')
    ret = chunkstore_lib.read('chunkstore_test', chunk_range=DateRange(dt(2016, 1, 1), dt(2016, 1, 3)))
    assert_frame_equal(df, ret)


def test_store_objects_series(chunkstore_lib):
    df = Series(data=['1', '2', '3'],
                index=Index(data=[dt(2016, 1, 1),
                                  dt(2016, 1, 2),
                                  dt(2016, 1, 3)],
                            name='date'),
                name='data')

    chunkstore_lib.write('chunkstore_test', df, chunk_size='D')
    ret = chunkstore_lib.read('chunkstore_test', chunk_range=DateRange(dt(2016, 1, 1), dt(2016, 1, 3)))
    assert_series_equal(df, ret)


def test_empty_range(chunkstore_lib):
    df = DataFrame(data={'data': [1], 'values': [10]},
                   index=Index(data=[dt(2016, 1, 1)], name='date'))
    chunkstore_lib.write('chunkstore_test', df, chunk_size='D')
    df = chunkstore_lib.read('chunkstore_test', chunk_range=DateRange(dt(2016, 1, 2)))
    assert(df.empty)


def test_update(chunkstore_lib):
    df = DataFrame(data={'data': [1, 2, 3]},
                   index=pd.Index(data=[dt(2016, 1, 1),
                                        dt(2016, 1, 2),
                                        dt(2016, 1, 3)], name='date'))
    df2 = DataFrame(data={'data': [20, 30, 40]},
                    index=pd.Index(data=[dt(2016, 1, 2),
                                         dt(2016, 1, 3),
                                         dt(2016, 1, 4)], name='date'))

    equals = DataFrame(data={'data': [1, 20, 30, 40]},
                       index=pd.Index(data=[dt(2016, 1, 1),
                                            dt(2016, 1, 2),
                                            dt(2016, 1, 3),
                                            dt(2016, 1, 4)], name='date'))

    chunkstore_lib.write('chunkstore_test', df, chunk_size='D')
    chunkstore_lib.update('chunkstore_test', df2)
    assert_frame_equal(chunkstore_lib.read('chunkstore_test'), equals)


def test_update_no_overlap(chunkstore_lib):
    df = DataFrame(data={'data': [1, 2, 3]},
                   index=pd.Index(data=[dt(2016, 1, 1),
                                        dt(2016, 1, 2),
                                        dt(2016, 1, 3)], name='date'))
    df2 = DataFrame(data={'data': [20, 30, 40]},
                    index=pd.Index(data=[dt(2015, 1, 2),
                                         dt(2015, 1, 3),
                                         dt(2015, 1, 4)], name='date'))

    equals = DataFrame(data={'data': [20, 30, 40, 1, 2, 3]},
                       index=pd.Index(data=[dt(2015, 1, 2),
                                            dt(2015, 1, 3),
                                            dt(2015, 1, 4),
                                            dt(2016, 1, 1),
                                            dt(2016, 1, 2),
                                            dt(2016, 1, 3)], name='date'))

    chunkstore_lib.write('chunkstore_test', df, chunk_size='D')
    chunkstore_lib.update('chunkstore_test', df2)
    assert_frame_equal(chunkstore_lib.read('chunkstore_test') , equals)


def test_append_before(chunkstore_lib):
    df = DataFrame(data={'data': [1, 2, 3]},
                   index=pd.Index(data=[dt(2016, 1, 1),
                                        dt(2016, 1, 2),
                                        dt(2016, 1, 3)], name='date'))
    df2 = DataFrame(data={'data': [20, 30, 40]},
                    index=pd.Index(data=[dt(2015, 1, 2),
                                         dt(2015, 1, 3),
                                         dt(2015, 1, 4)], name='date'))

    equals = DataFrame(data={'data': [20, 30, 40, 1, 2, 3]},
                       index=pd.Index(data=[dt(2015, 1, 2),
                                            dt(2015, 1, 3),
                                            dt(2015, 1, 4),
                                            dt(2016, 1, 1),
                                            dt(2016, 1, 2),
                                            dt(2016, 1, 3)], name='date'))

    chunkstore_lib.write('chunkstore_test', df, chunk_size='D')
    chunkstore_lib.append('chunkstore_test', df2)
    assert_frame_equal(chunkstore_lib.read('chunkstore_test') , equals)


def test_append_and_update(chunkstore_lib):
    df = DataFrame(data={'data': [1, 2, 3]},
                   index=pd.Index(data=[dt(2016, 1, 1),
                                        dt(2016, 1, 2),
                                        dt(2016, 1, 3)], name='date'))
    df2 = DataFrame(data={'data': [20, 30, 40]},
                    index=pd.Index(data=[dt(2015, 1, 2),
                                         dt(2015, 1, 3),
                                         dt(2015, 1, 4)], name='date'))

    df3 = DataFrame(data={'data': [100, 300]},
                    index=pd.Index(data=[dt(2015, 1, 2),
                                         dt(2016, 1, 2)], name='date'))

    equals = DataFrame(data={'data': [100, 30, 40, 1, 300, 3]},
                       index=pd.Index(data=[dt(2015, 1, 2),
                                            dt(2015, 1, 3),
                                            dt(2015, 1, 4),
                                            dt(2016, 1, 1),
                                            dt(2016, 1, 2),
                                            dt(2016, 1, 3)], name='date'))

    chunkstore_lib.write('chunkstore_test', df, chunk_size='D')
    chunkstore_lib.append('chunkstore_test', df2)
    chunkstore_lib.update('chunkstore_test', df3)
    assert_frame_equal(chunkstore_lib.read('chunkstore_test') , equals)


def test_update_same_df(chunkstore_lib):
    df = DataFrame(data={'data': [1, 2, 3]},
                   index=pd.Index(data=[dt(2016, 1, 1),
                                        dt(2016, 1, 2),
                                        dt(2016, 1, 3)], name='date'))
    chunkstore_lib.write('chunkstore_test', df, chunk_size='D')

    sym = chunkstore_lib._get_symbol_info('chunkstore_test')
    chunkstore_lib.update('chunkstore_test', df)
    assert(sym == chunkstore_lib._get_symbol_info('chunkstore_test'))


def test_update_series(chunkstore_lib):
    df = Series(data=[1, 2, 3],
                index=pd.Index(data=[dt(2016, 1, 1),
                                     dt(2016, 1, 2),
                                     dt(2016, 1, 3)], name='date'),
                name='data')
    df2 = Series(data=[20, 30, 40],
                 index=pd.Index(data=[dt(2016, 1, 2),
                                      dt(2016, 1, 3),
                                      dt(2016, 1, 4)], name='date'),
                 name='data')

    equals = Series(data=[1, 20, 30, 40],
                    index=pd.Index(data=[dt(2016, 1, 1),
                                         dt(2016, 1, 2),
                                         dt(2016, 1, 3),
                                         dt(2016, 1, 4)], name='date'),
                    name='data')

    chunkstore_lib.write('chunkstore_test', df, chunk_size='D')
    chunkstore_lib.update('chunkstore_test', df2)
    assert_series_equal(chunkstore_lib.read('chunkstore_test') , equals)


def test_update_same_series(chunkstore_lib):
    df = Series(data=[1, 2, 3],
                index=pd.Index(data=[dt(2016, 1, 1),
                                     dt(2016, 1, 2),
                                     dt(2016, 1, 3)], name='date'),
                name='data')
    chunkstore_lib.write('chunkstore_test', df, chunk_size='D')

    sym = chunkstore_lib._get_symbol_info('chunkstore_test')
    chunkstore_lib.update('chunkstore_test', df)
    assert(sym == chunkstore_lib._get_symbol_info('chunkstore_test'))


def test_df_with_multiindex(chunkstore_lib):
    df = DataFrame(data=[1, 2, 3],
                   index=MultiIndex.from_tuples([(dt(2016, 1, 1), 2),
                                                 (dt(2016, 1, 2), 3),
                                                 (dt(2016, 1, 3), 2)],
                                                names=['date', 'security']))
    chunkstore_lib.write('pandas', df, chunk_size='D')
    saved_df = chunkstore_lib.read('pandas')
    assert np.all(df.values == saved_df.values)


def test_with_strings(chunkstore_lib):
    df = DataFrame(data={'data': ['A', 'B', 'C']},
                   index=pd.Index(data=[dt(2016, 1, 1),
                                        dt(2016, 1, 2),
                                        dt(2016, 1, 3)], name='date'))
    chunkstore_lib.write('chunkstore_test', df, chunk_size='D')
    read_df = chunkstore_lib.read('chunkstore_test')
    assert_frame_equal(read_df, df)


def test_with_strings_multiindex_append(chunkstore_lib):
    df = DataFrame(data={'data': ['A', 'BBB', 'CC']},
                   index=MultiIndex.from_tuples([(dt(2016, 1, 1), 2),
                                                 (dt(2016, 1, 1), 3),
                                                 (dt(2016, 1, 2), 2)],
                                                names=['date', 'security']))
    chunkstore_lib.write('chunkstore_test', df, chunk_size='D')
    read_df = chunkstore_lib.read('chunkstore_test')
    assert_frame_equal(read_df, df)
    df2 = DataFrame(data={'data': ['AAAAAAA']},
                    index=MultiIndex.from_tuples([(dt(2016, 1, 2), 4)],
                                                 names=['date', 'security']))
    chunkstore_lib.append('chunkstore_test', df2)
    df = DataFrame(data={'data': ['A', 'BBB', 'CC', 'AAAAAAA']},
                   index=MultiIndex.from_tuples([(dt(2016, 1, 1), 2),
                                                 (dt(2016, 1, 1), 3),
                                                 (dt(2016, 1, 2), 2),
                                                 (dt(2016, 1, 2), 4)],
                                                names=['date', 'security']))
    assert_frame_equal(chunkstore_lib.read('chunkstore_test') , df)


def gen_daily_data(month, days, securities):
    for day in days:
        openp = [round(random.uniform(50.0, 100.0), 1) for x in securities]
        closep = [round(x + random.uniform(-5.0, 5.0), 1) for x in openp]

        index_list = [(dt(2016, month, day), s) for s in securities]
        yield DataFrame(data={'open': openp, 'close':closep},
                        index=MultiIndex.from_tuples(index_list,
                                                     names=['date', 'security']))


def write_random_data(chunkstore_lib, name, month, days, securities, chunk_size='D', update=False, append=False):
    '''
    will generate daily data and write it in daily chunks
    regardless of what the chunk_size is set to.
    month: integer
    days: list of integers
    securities: list of integers
    chunk_size: one of 'D', 'M', 'Y'
    update: force update for each daily write
    append: force append for each daily write
    '''
    df_list = []
    for df in gen_daily_data(month, days, securities):
        if update:
            chunkstore_lib.update(name, df)
        elif append or len(df_list) > 0:
            chunkstore_lib.append(name, df)
        else:
            chunkstore_lib.write(name, df, chunk_size=chunk_size)
        df_list.append(df)

    return pd.concat(df_list)


def test_multiple_actions(chunkstore_lib):
    def helper(chunkstore_lib, name, chunk_size):
        written_df = write_random_data(chunkstore_lib, name, 1, list(range(1, 31)), list(range(1, 101)), chunk_size=chunk_size)

        read_info = chunkstore_lib.read(name)
        assert_frame_equal(written_df, read_info)

        df = write_random_data(chunkstore_lib, name, 1, [1], list(range(1, 11)), update=True, chunk_size=chunk_size)

        read_info = chunkstore_lib.read(name, chunk_range=DateRange(dt(2016, 1, 2), dt(2016, 1, 30)))
        assert_frame_equal(written_df['2016-01-02':], read_info ['2016-01-02':])

        read_info = chunkstore_lib.read(name, chunk_range=DateRange(dt(2016, 1, 1), dt(2016, 1, 1)))
        written_df = df.combine_first(written_df)
        assert_frame_equal(written_df[:'2016-01-01'], read_info [:'2016-01-01'])

        df = write_random_data(chunkstore_lib, name, 2, list(range(1, 29)), list(range(1, 501)), append=True, chunk_size=chunk_size)
        read_info = chunkstore_lib.read(name)
        assert_frame_equal(pd.concat([written_df, df]), read_info)

    for chunk_size in ['D', 'M', 'Y']:
        helper(chunkstore_lib, 'test_data_' + chunk_size, chunk_size)


def test_multiple_actions_monthly_data(chunkstore_lib):
    def helper(chunkstore_lib, chunk_size, name, df, append):
        chunkstore_lib.write(name, df, chunk_size=chunk_size)

        assert_frame_equal(chunkstore_lib.read(name) , df)
        
        chunkstore_lib.append(name, append)

        assert_frame_equal(chunkstore_lib.read(name), pd.concat([df, append]))

        chunkstore_lib.update(name, append)

        assert_frame_equal(chunkstore_lib.read(name), pd.concat([df, append]))

    df = []
    for month in range(1, 4):
        df.extend(list(gen_daily_data(month, list(range(1, 21)), list(range(1, 11)))))

    df = pd.concat(df)

    append = []
    for month in range(6, 10):
        append.extend(list(gen_daily_data(month, list(range(1, 21)), list(range(1, 11)))))

    append = pd.concat(append)

    for chunk_size in ['D', 'M', 'Y']:
        helper(chunkstore_lib, chunk_size, 'test_monthly_' + chunk_size, df, append)


def test_delete(chunkstore_lib):
    df = DataFrame(data={'data': [1, 2, 3]},
                   index=MultiIndex.from_tuples([(dt(2016, 1, 1), 1),
                                                 (dt(2016, 1, 2), 1),
                                                 (dt(2016, 1, 3), 1)],
                                                names=['date', 'id'])
                   )
    chunkstore_lib.write('test_df', df, 'D')
    read_df = chunkstore_lib.read('test_df')
    assert_frame_equal(df, read_df)
    assert ('test_df' in chunkstore_lib.list_symbols())
    chunkstore_lib.delete('test_df')
    assert (chunkstore_lib.list_symbols() == [])
