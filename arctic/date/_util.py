import calendar
import datetime
from datetime import timedelta

from ._daterange import DateRange
from ._generalslice import OPEN_OPEN, CLOSED_CLOSED, OPEN_CLOSED, CLOSED_OPEN
from ._parse import parse
from ._mktz import mktz
import sys
if sys.version_info > (3,):
    long = int

    
# Support standard brackets syntax for open/closed ranges.
Ranges = {'()': OPEN_OPEN,
          '(]': OPEN_CLOSED,
          '[)': CLOSED_OPEN,
          '[]': CLOSED_CLOSED}


def string_to_daterange(str_range, delimiter='-', as_dates=False, interval=CLOSED_CLOSED):
    """
    Convert a string to a DateRange type. If you put only one date, it generates the
    relevant range for just that date or datetime till 24 hours later. You can optionally
    use mixtures of []/() around the DateRange for OPEN/CLOSED interval behaviour.

    Parameters
    ----------
    str_range : `String`
        The range as a string of dates separated by one delimiter.

    delimiter : `String`
        The separator between the dates, using '-' as default.

    as_dates : `Boolean`
        True if you want the date-range to use datetime.date rather than datetime.datetime.

    interval : `int`
               CLOSED_CLOSED, OPEN_CLOSED, CLOSED_OPEN or OPEN_OPEN.
               **Default is CLOSED_CLOSED**.

    Returns
    -------
        `arctic.date.DateRange` : the DateRange parsed from the string.

    Examples
    --------
    >>> from arctic.date import string_to_daterange
    >>> string_to_daterange('20111020', as_dates=True)
    DateRange(start=datetime.date(2011, 10, 20), end=datetime.date(2011, 10, 21))

    >>> string_to_daterange('201110201030')
    DateRange(start=datetime.datetime(2011, 10, 20, 10, 30), end=datetime.datetime(2011, 10, 21, 10, 30))

    >>> string_to_daterange('20111020-20120120', as_dates=True)
    DateRange(start=datetime.date(2011, 10, 20), end=datetime.date(2012, 1, 20))

    >>> string_to_daterange('[20111020-20120120)', as_dates=True)
    DateRange(start=datetime.date(2011, 10, 20), end=datetime.date(2012, 1, 20))
    """
    num_dates = str_range.count(delimiter) + 1
    if num_dates > 2:
        raise ValueError('Too many dates in input string [%s] with delimiter (%s)' % (str_range, delimiter))

    # Allow the user to use the [date-date), etc. range syntax to specify the interval.
    range_mode = Ranges.get(str_range[0] + str_range[-1], None)
    if range_mode:
        return string_to_daterange(str_range[1:-1], delimiter, as_dates, interval=range_mode)

    if as_dates:
        parse_dt = lambda s: parse(s).date() if s else None
    else:
        parse_dt = lambda s: parse(s) if s else None
    if num_dates == 2:
        d = [parse_dt(x) for x in str_range.split(delimiter)]
        oc = interval
    else:
        start = parse_dt(str_range)
        d = [start, start + datetime.timedelta(1)]
        oc = CLOSED_OPEN  # Always use closed-open for a single date/datetime.
    return DateRange(d[0], d[1], oc)


def to_dt(date, default_tz=None):
    """
    Returns a non-naive datetime.datetime.
    
    Interprets numbers as ms-since-epoch.

    Parameters
    ----------
    date : `int` or `datetime.datetime`
        The datetime to convert

    default_tz : tzinfo
        The TimeZone to use if none is found.  If not supplied, and the
        datetime doesn't have a timezone, then we raise ValueError

    Returns
    -------
    Non-naive datetime
    """
    if isinstance(date, (int, long)):
        return ms_to_datetime(date, default_tz)
    elif date.tzinfo is None:
        if default_tz is None:
            raise ValueError("Must specify a TimeZone on incoming data")
        return date.replace(tzinfo=default_tz)
    return date


def to_pandas_closed_closed(date_range, add_tz=True):
    """
    Pandas DateRange slicing is CLOSED-CLOSED inclusive at both ends.

    Parameters
    ----------
    date_range : `DateRange` object 
        converted to CLOSED_CLOSED form for Pandas slicing

    add_tz : `bool`
        Adds a TimeZone to the daterange start and end if it doesn't
        have one.

    Returns
    -------
    Returns a date_range with start-end suitable for slicing in pandas.
    """
    if not date_range:
        return None

    start = date_range.start
    end = date_range.end
    if start:
        start = to_dt(start, mktz()) if add_tz else start
        if date_range.startopen:
            start += timedelta(milliseconds=1)

    if end:
        end = to_dt(end, mktz()) if add_tz else end
        if date_range.endopen:
            end -= timedelta(milliseconds=1)
    return DateRange(start, end)


def ms_to_datetime(ms, tzinfo=None):
    """Convert a millisecond time value to an offset-aware Python datetime object."""
    if not isinstance(ms, (int, long)):
        raise TypeError('expected integer, not %s' % type(ms))

    if tzinfo is None:
        tzinfo = mktz()

    return datetime.datetime.fromtimestamp(ms * 1e-3, tzinfo)


def _add_tzone(dtm):
    if dtm.tzinfo is None:
        dtm = dtm.replace(tzinfo=mktz())
    return dtm


def datetime_to_ms(d):
    """Convert a Python datetime object to a millisecond epoch (UTC) time value."""
    try:
        return long((calendar.timegm(_add_tzone(d).utctimetuple()) + d.microsecond / 1000000.0) * 1e3)
    except AttributeError:
        raise TypeError('expect Python datetime object, not %s' % type(d))


def utc_dt_to_local_dt(dtm):
    """Convert a UTC datetime to datetime in local timezone"""
    utc_zone = mktz("UTC")
    if dtm.tzinfo is not None and dtm.tzinfo != utc_zone:
        raise ValueError(
            "Expected dtm without tzinfo or with UTC, not %r" % (
                dtm.tzinfo
            )
        )

    if dtm.tzinfo is None:
        dtm = dtm.replace(tzinfo=utc_zone)
    return dtm.astimezone(mktz())
