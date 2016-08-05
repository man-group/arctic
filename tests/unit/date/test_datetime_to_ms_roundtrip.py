import pytest
import datetime
import pytz
from arctic.date import mktz, datetime_to_ms, ms_to_datetime


def assert_roundtrip(tz):
    ts = datetime.datetime(1982, 7, 1, 16, 5)

    ts1 = ts.replace(tzinfo=tz)
    ts2 = ms_to_datetime(datetime_to_ms(ts1.astimezone(mktz("UTC"))), tz)

    assert(ts2.hour == ts1.hour)
    assert ts2 == ts1


def get_tz():
    tz = pytz.timezone("Europe/London")
    tmp = ms_to_datetime(0, tz)
    tz = tmp.tzinfo
    return tz


def test_UTC_roundtrip():
    tz = pytz.timezone("UTC")
    assert_roundtrip(tz)


def test_weird_get_tz_local():
    tz = get_tz()
    assert_roundtrip(tz)


@pytest.mark.xfail
def test_pytz_London():
    # Don't use pytz
    tz = pytz.timezone("Europe/London")
    assert_roundtrip(tz)


def test_mktz_London():
    tz = mktz("Europe/London")
    assert_roundtrip(tz)


def test_datetime_roundtrip_local_no_tz():
    pdt = datetime.datetime(2012, 6, 12, 12, 12, 12, 123000)
    pdt2 = ms_to_datetime(datetime_to_ms(pdt)).replace(tzinfo=None)
    assert pdt2 == pdt

    pdt = datetime.datetime(2012, 1, 12, 12, 12, 12, 123000)
    pdt2 = ms_to_datetime(datetime_to_ms(pdt)).replace(tzinfo=None)
    assert pdt2 == pdt


def test_datetime_roundtrip_local_tz():
    pdt = datetime.datetime(2012, 6, 12, 12, 12, 12, 123000, tzinfo=mktz())
    pdt2 = ms_to_datetime(datetime_to_ms(pdt))
    assert pdt2 == pdt

    pdt = datetime.datetime(2012, 1, 12, 12, 12, 12, 123000, tzinfo=mktz())
    pdt2 = ms_to_datetime(datetime_to_ms(pdt))
    assert pdt2 == pdt


def test_datetime_roundtrip_est_tz():
    pdt = datetime.datetime(2012, 6, 12, 12, 12, 12, 123000, tzinfo=mktz('EST'))
    pdt2 = ms_to_datetime(datetime_to_ms(pdt))
    assert pdt2.replace(tzinfo=mktz()) == pdt

    pdt = datetime.datetime(2012, 1, 12, 12, 12, 12, 123000, tzinfo=mktz('EST'))
    pdt2 = ms_to_datetime(datetime_to_ms(pdt))
    assert pdt2.replace(tzinfo=mktz()) == pdt
