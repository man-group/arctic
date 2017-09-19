try:
    import cPickle as pickle
except ImportError:
    import pickle
from datetime import datetime as dt
import pandas as pd
from pandas.util.testing import assert_frame_equal
import pytest

from arctic.exceptions import NoDataFoundException

symbol1 = 'symbol1'
symbol2 = 'symbol2'
start_time0 = dt(2000, 1, 1)
start_time1 = dt(2001, 1, 1)
start_time2 = dt(2001, 4, 1)
metadata1 = {'key1': 'value1'}
metadata2 = {'key2': 'value2'}
dataframe1 = pd.DataFrame({symbol1: [metadata1]}, [start_time1])
dataframe2 = pd.DataFrame({symbol2: [metadata1, metadata2]}, [start_time1, start_time2])
dataframe3 = pd.DataFrame({symbol1: [metadata1, metadata2]}, [start_time1, start_time2])
dataframe4 = pd.DataFrame({symbol1: [metadata2]}, [start_time2])
dataframe5 = pd.DataFrame({symbol1: [metadata1, metadata2]}, [start_time0, start_time2])


def integrity_check(ms_lib, symbol):
    # Lower level checks to ensure end_time is set correctly
    start_time = 'start'
    metadata = None
    for item in ms_lib.find({'symbol': symbol}, sort=[('start_time', 1)]):
        if start_time != 'start' and item['start_time'] != start_time:
            raise ValueError('end_time not set correctly')
        start_time = item.get('end_time')
        if item['metadata'] == metadata:
            raise ValueError('consecutive duplicate metadata')
        metadata = item['metadata']
    assert start_time == None, 'end_time of the last entry should be unset'


def test_pickle(ms_lib):
    buff = pickle.dumps(ms_lib)
    mnew = pickle.loads(buff)
    assert ms_lib._arctic_lib.get_name() == mnew._arctic_lib.get_name()

    assert "arctic_test.TEST" in str(ms_lib)
    assert str(ms_lib) == repr(ms_lib)


def test_has_symbol(ms_lib):
    assert not ms_lib.has_symbol(symbol1)
    ms_lib.append(symbol1, metadata1)
    assert ms_lib.has_symbol(symbol1)


def test_list_symbols(ms_lib):
    ms_lib.append(symbol1, metadata1)
    assert symbol1 in ms_lib.list_symbols()


def test_read_history(ms_lib):
    assert_frame_equal(ms_lib.read_history(symbol1), pd.DataFrame({symbol1: []}, []))

    ms_lib.append(symbol1, metadata1, start_time1)
    assert_frame_equal(ms_lib.read_history(symbol1), dataframe1)


def test_read(ms_lib):
    assert ms_lib.read(symbol1) == None

    ms_lib.append(symbol1, metadata1, start_time1)
    assert ms_lib.read(symbol1) == metadata1

    ms_lib.append(symbol1, metadata2, start_time2)
    assert ms_lib.read(symbol1, as_of=start_time1) == metadata1


def test_write_history(ms_lib):
    collection = [pd.DataFrame({symbol1: [metadata1, metadata1]}, [start_time1, start_time2]),
                  pd.DataFrame({symbol2: [metadata1, metadata2]}, [start_time1, start_time2])]
    ms_lib.write_history(collection)

    integrity_check(ms_lib, symbol1)
    integrity_check(ms_lib, symbol2)
    assert_frame_equal(ms_lib.read_history(symbol1), dataframe1)
    assert_frame_equal(ms_lib.read_history(symbol2), dataframe2)


def test_append(ms_lib):
    ret1 = ms_lib.append(symbol1, None)
    assert not ms_lib.has_symbol(symbol1)
    assert ret1 is None

    ret2 = ms_lib.append(symbol1, metadata1, start_time1)
    assert ms_lib.read(symbol1) == metadata1
    assert ret2['symbol'] == symbol1
    assert ret2['start_time'] == start_time1
    assert ret2['metadata'] == metadata1

    # ensure writing same metadata does not create new entry
    ret3 = ms_lib.append(symbol1, metadata1, start_time2)
    assert ms_lib.read(symbol1) == metadata1
    assert_frame_equal(ms_lib.read_history(symbol1), dataframe1)
    assert ret3 == ret2

    ret4 = ms_lib.append(symbol1, metadata2, start_time2)
    assert_frame_equal(ms_lib.read_history(symbol1), dataframe3)
    assert ret4['metadata'] == metadata2

    with pytest.raises(ValueError):
        ms_lib.append(symbol1, metadata1, start_time1)

    integrity_check(ms_lib, symbol1)


def test_prepend(ms_lib):
    ret1 = ms_lib.prepend(symbol1, None)
    assert not ms_lib.has_symbol(symbol1)
    assert ret1 is None

    ret2 = ms_lib.prepend(symbol1, metadata2, start_time2)
    assert ms_lib.read(symbol1) == metadata2
    assert_frame_equal(ms_lib.read_history(symbol1), dataframe4)
    assert ret2['symbol'] == symbol1
    assert ret2['start_time'] == start_time2
    assert ret2['metadata'] == metadata2

    ret3 = ms_lib.prepend(symbol1, metadata1, start_time1)
    assert_frame_equal(ms_lib.read_history(symbol1), dataframe3)
    assert ret3['metadata'] == metadata1

    # ensure writing same metadata does not create new entry
    ret4 = ms_lib.prepend(symbol1, metadata1, start_time0)
    assert_frame_equal(ms_lib.read_history(symbol1), dataframe5)
    ret3['start_time'] = start_time0
    assert ret4 == ret3

    with pytest.raises(ValueError):
        ms_lib.append(symbol1, metadata2, start_time2)

    integrity_check(ms_lib, symbol1)


def test_pop(ms_lib):
    ms_lib.write_history([pd.DataFrame({symbol1: [metadata1, metadata2]}, [start_time1, start_time2])])
    ms_lib.pop(symbol1)
    assert_frame_equal(ms_lib.read_history(symbol1), dataframe1)
    integrity_check(ms_lib, symbol1)


def test_purge(ms_lib):
    ms_lib.write_history([pd.DataFrame({symbol1: [metadata1, metadata2]}, [start_time1, start_time2])])
    ms_lib.purge(symbol1)

    assert not ms_lib.has_symbol(symbol1)
