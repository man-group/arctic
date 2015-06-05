import pytest
import pytz

from datetime import datetime as dt
from arctic.date import datetime_to_ms, ms_to_datetime, mktz, to_pandas_closed_closed, DateRange, OPEN_OPEN, CLOSED_CLOSED
from arctic.date._mktz import DEFAULT_TIME_ZONE_NAME


@pytest.mark.parametrize('pdt', [
                            dt(2007, 3, 25, 1, tzinfo=mktz('Europe/London')),
                            dt(2004, 10, 31, 23, 3, tzinfo=mktz('Europe/London')),
                            dt(1990, 4, 5, 0, 0, tzinfo=mktz('Europe/London')),
                            dt(2007, 3, 25, 1, tzinfo=mktz('EST')),
                            dt(2004, 10, 31, 23, 3, tzinfo=mktz('EST')),
                            dt(1990, 4, 5, 0, 0, tzinfo=mktz('EST')),
                            ]
)
def test_datetime_to_ms_and_back(pdt):
    i = datetime_to_ms(pdt)
    pdt = pdt.astimezone(mktz())
    pdt = pdt.replace(tzinfo=None)
    pdt2 = ms_to_datetime(i)
    assert pdt == pdt2


def test_datetime_to_ms_and_back_microseconds():
    pdt = dt(2012, 8, 1, 12, 34, 56, 999999, tzinfo=mktz(DEFAULT_TIME_ZONE_NAME))
    i = datetime_to_ms(pdt)
    pdt = pdt.replace(tzinfo=None)
    pdt2 = ms_to_datetime(i)

    assert pdt != pdt2
    assert pdt.year == pdt2.year
    assert pdt.month == pdt2.month
    assert pdt.day == pdt2.day
    assert pdt.hour == pdt2.hour
    assert pdt.minute == pdt2.minute
    assert pdt.second == pdt2.second
    #   Microsecond precision loss inevitable.
    assert pdt.microsecond // 1000 == pdt2.microsecond // 1000
    assert pdt.tzinfo is None


def test_daterange_closedclosed_None():
    assert to_pandas_closed_closed(None) is None


def test_daterange_closedclosed():
    date_range = DateRange(dt(2013, 1, 1, tzinfo=mktz('Europe/London')),
                           dt(2014, 2, 1, tzinfo=mktz('Europe/London')), OPEN_OPEN)
    expected = DateRange(dt(2013, 1, 1, 0, 0, 0, 1000, tzinfo=mktz('Europe/London')),
                         dt(2014, 1, 31, 23, 59, 59, 999000, tzinfo=mktz('Europe/London')),
                         CLOSED_CLOSED)
    act = to_pandas_closed_closed(date_range)
    assert act == expected
