from datetime import datetime as dt
from mock import patch
import numpy as np
from pandas.util.testing import assert_frame_equal
import pytest

from arctic import arctic as m
from arctic.date import mktz
from arctic.exceptions import OverlappingDataException, \
    NoDataFoundException
from arctic.tickstore.tickstore import SYMBOL, START, END, COUNT, COLUMNS
from tests.util import read_str_as_pandas


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
               'index': dt(2013, 7, 5, tzinfo=mktz('Europe/London'))
               },
              ]


def test_ts_write_simple(tickstore_lib):
    assert tickstore_lib.stats()['chunks']['count'] == 0
    tickstore_lib.write('SYM', DUMMY_DATA)
    assert tickstore_lib.stats()['chunks']['count'] == 1
    assert len(tickstore_lib.read('SYM')) == 5
    assert tickstore_lib.list_symbols() == ['SYM']


def test_overlapping_load(tickstore_lib):
    data = DUMMY_DATA
    tickstore_lib.write('SYM', DUMMY_DATA)
    with pytest.raises(OverlappingDataException):
        tickstore_lib.write('SYM', data)

    data = DUMMY_DATA[2:]
    with pytest.raises(OverlappingDataException):
        tickstore_lib.write('SYM', data)

    data = DUMMY_DATA[2:3]
    with pytest.raises(OverlappingDataException):
        tickstore_lib.write('SYM', data)

    # overlapping at the beginning is ok
    data = [DUMMY_DATA[0]]
    tickstore_lib.write('SYM', data)

    # overlapping at the end is ok
    data = [DUMMY_DATA[-1]]
    tickstore_lib.write('SYM', data)


def test_ts_write_pandas(tickstore_lib):
    data = DUMMY_DATA
    tickstore_lib.write('SYM', data)

    data = tickstore_lib.read('SYM', columns=None)
    assert data.index[0] == dt(2013, 1, 1, tzinfo=mktz('Europe/London'))
    assert data.a[0] == 1
    tickstore_lib.delete('SYM')
    tickstore_lib.write('SYM', data)

    read = tickstore_lib.read('SYM', columns=None)
    assert_frame_equal(read, data, check_names=False)


def test_to_bucket(tickstore_lib):
    bucket = tickstore_lib._to_bucket(DUMMY_DATA, 'SYM')
    assert bucket[SYMBOL] == 'SYM'
    assert bucket[START] == dt(2013, 1, 1, tzinfo=mktz('Europe/London'))
    assert bucket[END] == dt(2013, 7, 5, tzinfo=mktz('Europe/London'))
    assert bucket[COUNT] == 5


def test_pandas_to_bucket(tickstore_lib):
    df = read_str_as_pandas("""             index | near
                   2012-09-08 17:06:11 |  1.0
                   2012-10-08 17:06:11 |  2.0
                   2012-10-09 17:06:11 |  2.5
                   2012-11-08 17:06:11 |  3.0""")
    df = df.tz_localize('UTC')
    bucket = tickstore_lib._pandas_to_bucket(df, 'SYM')
    assert bucket[SYMBOL] == 'SYM'
    assert bucket[START] == dt(2012, 9, 8, 17, 6, 11, tzinfo=mktz('UTC'))
    assert bucket[END] == dt(2012, 11, 8, 17, 6, 11, tzinfo=mktz('UTC'))
    assert bucket[COUNT] == 4
    assert bucket[COLUMNS].keys() == ['near']

