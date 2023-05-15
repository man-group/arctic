from datetime import datetime as dt

import tzlocal
from mock import patch
from pytest import raises

from arctic.date import mktz, TimezoneError

#DK_TEST = tzlocal.get_localzone() # 5.0 tzlocal.ZoneInfo # 4.2 pytzShim
DEFAULT_TIME_ZONE_NAME = str(tzlocal.get_localzone()) # just make a string
#DEFAULT_TIME_ZONE_NAME = tzlocal.get_localzone().zone  # old str('Europe/London')


def test_mktz():
    tz = mktz("Europe/London")
    d = dt(2012, 2, 2, tzinfo=tz)
    assert d.tzname() == 'GMT'
    d = dt(2012, 7, 2, tzinfo=tz)
    assert d.tzname() == 'BST'

    tz = mktz('UTC')
    d = dt(2012, 2, 2, tzinfo=tz)
    assert d.tzname() == 'UTC'
    d = dt(2012, 7, 2, tzinfo=tz)
    assert d.tzname() == 'UTC'  # --------replace_empty_timezones_with_default -----------------


def test_mktz_noarg():
    tz = mktz()
    assert DEFAULT_TIME_ZONE_NAME in str(tz)


def test_mktz_zone():
    tz = mktz('UTC')
    assert tz.zone == "UTC"
    tz = mktz('/usr/share/zoneinfo/UTC')
    assert tz.zone == "UTC"


def test_mktz_fails_if_invalid_timezone():
    with patch('os.path.exists') as file_exists:
        file_exists.return_value = False
        with raises(TimezoneError):
            mktz('junk')
