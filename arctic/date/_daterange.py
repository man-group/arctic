import datetime

from ._generalslice import OPEN_OPEN, CLOSED_CLOSED, OPEN_CLOSED, CLOSED_OPEN, GeneralSlice
from ._parse import parse


INTERVAL_LOOKUP = {(True, True): OPEN_OPEN,
                   (False, False): CLOSED_CLOSED,
                   (True, False): OPEN_CLOSED,
                   (False, True): CLOSED_OPEN
                   }


class DateRange(GeneralSlice):
    """
    Represents a bounded datetime range.

    Ranges may be bounded on either end if a date is
    specified for the start or end of the range, or unbounded
    if None is specified for either value. Unbounded ranges will allow
    all available data to pass through when used as a filter argument
    on function or method.

    =====  ====  ============================  ===============================
    start  end  interval                      Meaning
    -----  ----  ----------------------------  -------------------------------
    None   None                                any date
    a      None  CLOSED_CLOSED or CLOSED_OPEN  date >= a
    a      None  OPEN_CLOSED or OPEN_OPEN      date > a
    None   b     CLOSED_CLOSED or OPEN_CLOSED  date <= b
    None   b     CLOSED_OPEN or OPEN_OPEN      date < b
    a      b     CLOSED_CLOSED                 date >= a and date <= b
    a      b     OPEN_CLOSED                   date > a and date <= b
    a      b     CLOSED_OPEN                   date >= a and date < b
    a      b     OPEN_OPEN                     date > a and date < b
    =====  ====  ============================  ===============================

    Parameters
    ----------
    start : `int`, `str` or `datetime.datetime`
        lower bound date value as an integer, string or datetime object.

    end : `int`, `str` or `datetime.datetime`
        upper bound date value as an integer, string or datetime object.

    interval : `int`
               CLOSED_CLOSED, OPEN_CLOSED, CLOSED_OPEN or OPEN_OPEN.
               **Default is CLOSED_CLOSED**.
    """
    def __init__(self, start=None, end=None, interval=CLOSED_CLOSED):

        def _is_dt_type(x):
            return isinstance(x, (datetime.datetime, datetime.date))

        def _compute_bound(value, desc):
            if isinstance(value, (int, str)):
                return parse(str(value))
            elif _is_dt_type(value):
                return value
            elif value is None:
                return None
            else:
                raise TypeError('unsupported type for %s: %s' % (desc, type(value)))

        super(DateRange, self).__init__(_compute_bound(start, "start"), _compute_bound(end, "end"), 1, interval)

        if _is_dt_type(self.start) and _is_dt_type(self.end):
            if self.start > self.end:
                raise ValueError('start date (%s) cannot be greater than end date (%s)!'
                                 % (self.start, self.end))

    @property
    def unbounded(self):
        """True if range is unbounded on either or both ends, False otherwise."""
        return self.start is None or self.end is None

    def intersection(self, other):
        """
        Create a new DateRange representing the maximal range enclosed by this range and other
        """
        startopen = other.startopen if self.start is None \
                    else self.startopen if other.start is None \
                    else other.startopen if self.start < other.start \
                    else self.startopen if self.start > other.start \
                    else (self.startopen and other.startopen)
        endopen = other.endopen if self.end is None \
                   else self.endopen if other.end is None \
                   else other.endopen if self.end > other.end \
                   else self.endopen if self.end < other.end \
                   else (self.endopen and other.endopen)

        new_start = self.start if other.start is None \
                    else other.start if self.start is None \
                    else max(self.start, other.start)
        new_end = self.end if other.end is None \
                   else other.end if self.end is None \
                   else min(self.end, other.end)

        interval = INTERVAL_LOOKUP[(startopen, endopen)]

        return DateRange(new_start, new_end, interval)

    def as_dates(self):
        """
        Create a new DateRange with the datetimes converted to dates and changing to CLOSED/CLOSED.
        """
        new_start = self.start.date() if self.start and isinstance(self.start, datetime.datetime) else self.start
        new_end = self.end.date() if self.end and isinstance(self.end, datetime.datetime) else self.end
        return DateRange(new_start, new_end, CLOSED_CLOSED)

    def mongo_query(self):
        """
        Convert a DateRange into a MongoDb query string. FIXME: Mongo can only handle
        datetimes in queries, so we should make this handle the case where start/end are
        datetime.date and extend accordingly (being careful about the interval logic).
        """
        comps = {OPEN_CLOSED: ('t', 'te'), OPEN_OPEN: ('t', 't'),
                 CLOSED_OPEN: ('te', 't'), CLOSED_CLOSED: ('te', 'te')}
        query = {}
        comp = comps[self.interval]
        if self.start:
            query['$g' + comp[0]] = self.start
        if self.end:
            query['$l' + comp[1]] = self.end
        return query

    def get_date_bounds(self):
        """
        Return the upper and lower bounds along
        with operators that are needed to do an 'in range' test.
        Useful for SQL commands.

        Returns
        -------
        tuple: (`str`, `date`, `str`, `date`)
                (date_gt, start, date_lt, end)
        e.g.:
                ('>=', start_date, '<', end_date)
        """
        start = end = None
        date_gt = '>='
        date_lt = '<='
        if self:
            if self.start:
                start = self.start
            if self.end:
                end = self.end
            if self.startopen:
                date_gt = '>'
            if self.endopen:
                date_lt = '<'

        return date_gt, start, date_lt, end

    def __contains__(self, d):
        if self.interval == CLOSED_CLOSED:
            return (self.start is None or d >= self.start) and (self.end is None or d <= self.end)
        elif self.interval == CLOSED_OPEN:
            return (self.start is None or d >= self.start) and (self.end is None or d < self.end)
        elif self.interval == OPEN_CLOSED:
            return (self.start is None or d > self.start) and (self.end is None or d <= self.end)

        return (self.start is None or d > self.start) and (self.end is None or d < self.end)

    def __repr__(self):
        return 'DateRange(start=%r, end=%r)' % (self.start, self.end)

    def __eq__(self, rhs):
        if rhs is None or not (hasattr(rhs, "end") and hasattr(rhs, "start")):
            return False
        return self.end == rhs.end and self.start == rhs.start

    def __lt__(self, other):
        if self.start is None:
            return True
        if other.start is None:
            return False
        return self.start < other.start

    def __hash__(self):
        return hash((self.start, self.end, self.step, self.interval))

    def __getitem__(self, key):
        if key == 0:
            return self.start
        elif key == 1:
            return self.end
        else:
            raise IndexError('Index %s not in range (0:1)' % key)

    __str__ = __repr__

    def __setstate__(self, state):
        """Called by pickle, PyYAML etc to set state."""
        self.start = state['start']
        self.end = state['end']
        self.interval = state.get('interval') or CLOSED_CLOSED
        self.step = 1
