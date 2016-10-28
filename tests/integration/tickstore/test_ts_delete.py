from datetime import datetime as dt
from mock import patch
import numpy as np
from pandas.util.testing import assert_frame_equal
import pytest

from arctic import arctic as m
from arctic.date import DateRange, CLOSED_OPEN, mktz
from arctic.exceptions import OverlappingDataException, \
    NoDataFoundException


def test_delete(tickstore_lib):
    DUMMY_DATA = [
              {'a': 1.,
               'b': 2.,
               'index': dt(2013, 1, 1, tzinfo=mktz('Europe/London'))
               },
              {'a': 3.,
               'b': 4.,
               'index': dt(2013, 1, 30, tzinfo=mktz('Europe/London'))
               },
              ]
    tickstore_lib._chunk_size = 1
    tickstore_lib.write('SYM', DUMMY_DATA)
    deleted = tickstore_lib.delete('SYM')
    assert deleted.deleted_count == 2
    with pytest.raises(NoDataFoundException):
        tickstore_lib.read('SYM', date_range=DateRange(20130102), columns=None)

    # Delete with a date-range
    tickstore_lib.write('SYM', DUMMY_DATA)
    deleted = tickstore_lib.delete(
        'SYM',
        DateRange(
            dt(2013, 1, 1, tzinfo=mktz('Europe/London')),
            dt(2013, 1, 2, tzinfo=mktz('Europe/London'))
        )
    )
    assert deleted.deleted_count == 1
    df = tickstore_lib.read('SYM', columns=None)
    assert np.allclose(df['b'].values, np.array([4.]))


def test_delete_daterange(tickstore_lib):
    DUMMY_DATA = [
              {'a': 1.,
               'b': 2.,
               'index': dt(2013, 1, 1, tzinfo=mktz('Europe/London'))
               },
              {'a': 3.,
               'b': 4.,
               'index': dt(2013, 2, 1, tzinfo=mktz('Europe/London'))
               },
              ]
    tickstore_lib._chunk_size = 1
    tickstore_lib.write('SYM', DUMMY_DATA)

    # Delete with a date-range
    deleted = tickstore_lib.delete(
        'SYM',
        DateRange(
            dt(2013, 1, 1, tzinfo=mktz('Europe/London')),
            dt(2013, 2, 1, tzinfo=mktz('Europe/London')),
            CLOSED_OPEN
        )
    )
    assert deleted.deleted_count == 1
    df = tickstore_lib.read('SYM', columns=None)
    assert np.allclose(df['b'].values, np.array([4.]))
