from datetime import datetime as dt
import operator
import pytest
import itertools
import six

from arctic.date import DateRange, string_to_daterange, CLOSED_CLOSED, CLOSED_OPEN, OPEN_CLOSED, OPEN_OPEN


test_ranges_for_bounding = {
    "unbounded":         (DateRange(),
                          None, None, True, None, None),
    "unbounded_right":   (DateRange('20110101'),
                          dt(2011, 1, 1), None, True, True, None),
    "unbounded_left":    (DateRange(None, '20111231'),
                          None, dt(2011, 12, 31), True, None, True),
    "closed_by_default": (DateRange('20110101', '20111231'),
                          dt(2011, 1, 1), dt(2011, 12, 31), False, True, True),
    "closed_explicitly": (DateRange('20110101', '20111231', CLOSED_CLOSED),
                          dt(2011, 1, 1), dt(2011, 12, 31), False, True, True),
    "closed_open":       (DateRange('20110101', '20111231', CLOSED_OPEN),
                          dt(2011, 1, 1), dt(2011, 12, 31), False, True, False),
    "open_closed":       (DateRange('20110101', '20111231', OPEN_CLOSED),
                          dt(2011, 1, 1), dt(2011, 12, 31), False, False, True),
    "open_open":         (DateRange('20110101', '20111231', OPEN_OPEN),
                          dt(2011, 1, 1), dt(2011, 12, 31), False, False, False),
}
test_ranges_for_bounding = sorted(six.iteritems(test_ranges_for_bounding), key=operator.itemgetter(1))


def eq_nan(*args):
    if all(arg is None for arg in args):
        return True
    return all(arg == args[0] for arg in args[1:])


@pytest.mark.parametrize(("dt_range", "start", "end", "is_unbounded", "start_in_range", "end_in_range"),
                         [i[1] for i in test_ranges_for_bounding],
                         ids=[i[0] for i in test_ranges_for_bounding])
def test_daterange_bounding(dt_range, start, end, is_unbounded, start_in_range, end_in_range):
    assert eq_nan(start, dt_range.start)
    assert eq_nan(end, dt_range.end)
    assert dt_range.unbounded is is_unbounded
    assert dt_range.start is None or (start_in_range is (dt_range.start in dt_range))
    assert dt_range.end is None or (end_in_range is (dt_range.end in dt_range))


test_ranges_for_parse = [
    [20110102, 20111231],
    ['20110102', '20111231'],
    ['2011-01-02', '2011-12-31'],
    [dt(2011, 1, 2), dt(2011, 12, 31)],
]

@pytest.mark.parametrize("date_range", test_ranges_for_parse)
def test_daterange_arg_parsing(date_range):
    d1 = DateRange(date_range[0], date_range[1])
    assert d1.start == dt(2011, 1, 2)
    assert d1.end == dt(2011, 12, 31)
    assert d1.unbounded is False


def test_daterange_eq():
    d1 = DateRange('20110101', '20111231')
    d2 = DateRange('20110101', '20111231')
    assert d1 == d2
    d1 = DateRange(None, '20111231')
    d2 = DateRange(None, '20111231')
    assert d1 == d2
    d1 = DateRange('20111231', None)
    d2 = DateRange('20111231', None)
    assert d1 == d2
    d1 = DateRange(None, None)
    d2 = DateRange(None, None)
    assert d1 == d2
    d1 = DateRange('20110102', '20111231')
    d2 = DateRange('20110101', '20111231')
    assert not d1 == d2


def test_daterange_hash():
    d1 = DateRange('20110101', '20111231')
    d2 = DateRange('20110101', '20111231')
    assert hash(d1) == hash(d2)
    d1 = DateRange(None, '20111231')
    d2 = DateRange(None, '20111231')
    assert hash(d1) == hash(d2)
    d1 = DateRange('20111231', None)
    d2 = DateRange('20111231', None)
    assert hash(d1) == hash(d2)
    d1 = DateRange(None, None)
    d2 = DateRange(None, None)
    assert hash(d1) == hash(d2)
    d1 = DateRange('20110102', '20111231')
    d2 = DateRange('20110101', '20111231')
    assert not hash(d1) == hash(d2)


def test_daterange_invalid_start():
    with pytest.raises(TypeError) as ex:
        DateRange(1.1, None)
    assert "unsupported type for start" in str(ex.value)


def test_daterange_invalid_end():
    with pytest.raises(TypeError) as ex:
        DateRange(None, object())
    assert "unsupported type for end" in str(ex.value)


def test_daterange_index():
    start, end = dt(2000, 1, 1), dt(3000, 1, 1)
    dr = DateRange(start, end)
    assert dr[0] == start
    assert dr[1] == end


def test_daterange_index_error():
    start, end = dt(2000, 1, 1), dt(3000, 1, 1)
    dr = DateRange(start, end)
    with pytest.raises(IndexError):
        dr[None]
    with pytest.raises(IndexError):
        dr[3]


def test_as_dates():
    """Various permutations of datetime/None, and date/None values."""
    dtime = dt(2010, 12, 13, 10, 30)
    for testdt in [dtime, dtime.date()]:
        vals = [testdt, None]
        for start, end in itertools.product(vals, vals):
            dr = DateRange(start, end)
            dad = dr.as_dates()
            if dr.start:
                assert dad.start == dr.start.date() if isinstance(dr.start, dt) else dr.start
            else:
                assert not dad.start
            if dr.end:
                assert dad.end == dr.end.date() if isinstance(dr.end, dt) else dr.end
            else:
                assert not dad.end


DR1 = DateRange('20110101', '20110102')
DR2 = DateRange('201101011030', '201101021030')
DR3 = DateRange('201101011030')
DR4 = DateRange(None, '201101011030')
DR5 = DateRange('201101011030')
DR6 = DateRange('20110101', '20110102', OPEN_OPEN)
DR7 = DateRange('20110101', '20110102', OPEN_CLOSED)
DR7 = DateRange('20110101', '20110102', CLOSED_OPEN)

STRING_DR_TESTS = [('20110101', DR1, DateRange(DR1.start.date(), DR1.end.date())),
                   ('20110101-20110102', DR1, DateRange(DR1.start.date(), DR1.end.date())),
                   ('201101011030', DR2, DateRange(DR2.start.date(), DR2.end.date())),
                   ('-201101011030', DR4, DateRange(None, DR2.start.date())),
                   ('201101011030-', DR5, DateRange(DR2.start.date())),
                   ('(20110101-20110102)', DR6, DateRange(DR6.start.date(), DR6.end.date(), DR6.interval)),
                   ('(20110101-20110102]', DR6, DateRange(DR6.start.date(), DR6.end.date(), DR6.interval)),
                   ('[20110101-20110102)', DR6, DateRange(DR6.start.date(), DR6.end.date(), DR6.interval)),
                   ('[20110101-20110102]', DR1, DateRange(DR1.start.date(), DR1.end.date(), DR1.interval)),
                   ]


@pytest.mark.parametrize(['instr', 'expected_ts', 'expected_dt'], STRING_DR_TESTS)
def test_string_to_daterange(instr, expected_ts, expected_dt):
    assert string_to_daterange(instr) == expected_ts
    assert string_to_daterange(instr, as_dates=True) == expected_dt


def test_string_to_daterange_raises():
    with pytest.raises(ValueError) as e:
        string_to_daterange('20120101-20130101-20140101')
    assert str(e.value) == "Too many dates in input string [20120101-20130101-20140101] with delimiter (-)"

QUERY_TESTS = [(DateRange('20110101', '20110102'), {'$gte': dt(2011, 1, 1), '$lte': dt(2011, 1, 2)}),
               (DateRange('20110101', '20110102', OPEN_OPEN), {'$gt': dt(2011, 1, 1), '$lt': dt(2011, 1, 2)}),
               (DateRange('20110101', '20110102', OPEN_CLOSED), {'$gt': dt(2011, 1, 1), '$lte': dt(2011, 1, 2)}),
               (DateRange('20110101', '20110102', CLOSED_OPEN), {'$gte': dt(2011, 1, 1), '$lt': dt(2011, 1, 2)}),
               (DateRange('20110101', '20110102'), {'$gte': dt(2011, 1, 1), '$lte': dt(2011, 1, 2)}),
               (DateRange('20110101', None), {'$gte': dt(2011, 1, 1)}),
               (DateRange(None, '20110102'), {'$lte': dt(2011, 1, 2)}),
               (DateRange(), {})]


@pytest.mark.parametrize(['date_range', 'expected'], QUERY_TESTS)
def test_mongo_query(date_range, expected):
    assert date_range.mongo_query() == expected


QUERY_TESTS_DB = [(DateRange('20110101', '20110102'), ('>=', dt(2011, 1, 1), '<=', dt(2011, 1, 2))),
               (DateRange('20110101', '20110102', OPEN_OPEN), ('>', dt(2011, 1, 1), '<', dt(2011, 1, 2))),
               (DateRange('20110101', '20110102', OPEN_CLOSED), ('>', dt(2011, 1, 1), '<=', dt(2011, 1, 2))),
               (DateRange('20110101', '20110102', CLOSED_OPEN), ('>=', dt(2011, 1, 1), '<', dt(2011, 1, 2))),
               (DateRange('20110101', '20110102'), ('>=', dt(2011, 1, 1), '<=', dt(2011, 1, 2))),
               (DateRange('20110101', None), ('>=', dt(2011, 1, 1), '<=' , None)),
               (DateRange(None, '20110102'), ('>=', None, '<=', dt(2011, 1, 2))),
               (DateRange(), ('>=', None , '<=' , None))]
@pytest.mark.parametrize(['date_range', 'expected'], QUERY_TESTS_DB)
def test_get_date_bounds(date_range, expected):
    assert date_range.get_date_bounds() == expected


@pytest.mark.parametrize(["dr"], [(DR1,), (DR2,), (DR3,), (DR4,), (DR5,), (DR6,), (DR7,)])
def test_intersection_with_self(dr):
    assert dr == dr.intersection(dr)


def test_intersection_returns_inner_boundaries():
    # #start:
    assert DateRange('20110103',).intersection(DateRange('20110102')).start == dt(2011, 1, 3)
    assert DateRange('20110102',).intersection(DateRange('20110103')).start == dt(2011, 1, 3)
    assert DateRange(None,).intersection(DateRange('20110103')).start == dt(2011, 1, 3)
    assert DateRange('20110103').intersection(DateRange(None)).start == dt(2011, 1, 3)

    # #end:
    assert DateRange(None, '20110103',).intersection(DateRange(None, '20110102')).end == dt(2011, 1, 2)
    assert DateRange(None, '20110102',).intersection(DateRange(None, '20110103')).end == dt(2011, 1, 2)
    assert DateRange(None, None,).intersection(DateRange(None, '20110103')).end == dt(2011, 1, 3)
    assert DateRange(None, '20110103').intersection(DateRange(None, None)).end == dt(2011, 1, 3)


def test_intersection_preserves_boundaries():
    # Non-matching boundaries
    assert DateRange('20110101', '20110102', OPEN_OPEN) == DateRange('20110101', '20110103', OPEN_CLOSED).intersection(DateRange('20110101', '20110102', OPEN_OPEN))
    assert DateRange('20110101', '20110102', OPEN_OPEN) == DateRange('20110101', '20110102', OPEN_OPEN).intersection(DateRange('20110101', '20110103', OPEN_CLOSED))
    assert DateRange('20110102', '20110103', OPEN_OPEN) == DateRange('20110102', '20110103', OPEN_OPEN).intersection(DateRange('20110101', '20110103', CLOSED_OPEN))

    assert DateRange('20110102', '20110103', CLOSED_OPEN) == DateRange('20110102', '20110103', CLOSED_OPEN).intersection(DateRange('20110101', '20110103', CLOSED_OPEN))
    assert DateRange('20110102', '20110103', CLOSED_OPEN) == DateRange('20110101', '20110103', CLOSED_OPEN).intersection(DateRange('20110102', '20110103', CLOSED_OPEN))

    # Matching boundaries
    assert DateRange('20110101', '20110102', OPEN_OPEN) == DateRange('20110101', '20110102', CLOSED_OPEN).intersection(DateRange('20110101', '20110102', OPEN_OPEN))
    assert DateRange('20110101', '20110102', OPEN_OPEN) == DateRange('20110101', '20110102', OPEN_OPEN).intersection(DateRange('20110101', '20110102', OPEN_CLOSED))

