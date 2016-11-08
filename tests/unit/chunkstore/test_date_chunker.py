from arctic.chunkstore.date_chunker import DateChunker
from pandas import DataFrame, MultiIndex
from datetime import datetime as dt
from arctic.date import DateRange
from pandas.util.testing import assert_frame_equal
import pandas as pd
import pytest
import six


def test_date_filter():
    c = DateChunker()
    df = DataFrame(data={'data': [1, 2, 3]},
                   index=MultiIndex.from_tuples([(dt(2016, 1, 1), 1),
                                                 (dt(2016, 1, 2), 1),
                                                 (dt(2016, 1, 3), 1)],
                                                names=['date', 'id'])
                   )

    # OPEN - CLOSED
    assert_frame_equal(c.filter(df, DateRange(None, dt(2016, 1, 3))), df)
    # CLOSED - OPEN
    assert_frame_equal(c.filter(df, DateRange(dt(2016, 1, 1), None)), df)
    # OPEN - OPEN
    assert_frame_equal(c.filter(df, DateRange(None, None)), df)
    # CLOSED - OPEN (far before data range)
    assert_frame_equal(c.filter(df, DateRange(dt(2000, 1, 1), None)), df)
    # CLOSED - OPEN (far after range)
    assert(c.filter(df, DateRange(dt(2020, 1, 2), None)).empty)
    # OPEN - CLOSED
    assert_frame_equal(c.filter(df, DateRange(None, dt(2020, 1, 1))), df)
    # CLOSED - CLOSED (after range)
    assert(c.filter(df, DateRange(dt(2017, 1, 1), dt(2018, 1, 1))).empty)


def test_date_filter_no_index():
    c = DateChunker()
    df = DataFrame(data={'data': [1, 2, 3],
                         'date': [dt(2016, 1, 1),
                                  dt(2016, 1, 2),
                                  dt(2016, 1, 3)]
                         }
                   )

    # OPEN - CLOSED
    assert_frame_equal(c.filter(df, DateRange(None, dt(2016, 1, 3))), df)
    # CLOSED - OPEN
    assert_frame_equal(c.filter(df, DateRange(dt(2016, 1, 1), None)), df)
    # OPEN - OPEN
    assert_frame_equal(c.filter(df, DateRange(None, None)), df)
    # CLOSED - OPEN (far before data range)
    assert_frame_equal(c.filter(df, DateRange(dt(2000, 1, 1), None)), df)
    # CLOSED - OPEN (far after range)
    assert(c.filter(df, DateRange(dt(2020, 1, 2), None)).empty)
    # OPEN - CLOSED
    assert_frame_equal(c.filter(df, DateRange(None, dt(2020, 1, 1))), df)
    # CLOSED - CLOSED (after range)
    assert(c.filter(df, DateRange(dt(2017, 1, 1), dt(2018, 1, 1))).empty)


def test_date_filter_with_pd_date_range():
    c = DateChunker()
    df = DataFrame(data={'data': [1, 2, 3]},
                   index=MultiIndex.from_tuples([(dt(2016, 1, 1), 1),
                                                 (dt(2016, 1, 2), 1),
                                                 (dt(2016, 1, 3), 1)],
                                                names=['date', 'id'])
                   )

    assert(c.filter(df, pd.date_range(dt(2017, 1, 1), dt(2018, 1, 1))).empty)
    assert_frame_equal(c.filter(df, pd.date_range(dt(2016, 1, 1), dt(2017, 1, 1))), df)


def test_to_chunks_exceptions():
    df = DataFrame(data={'data': [1, 2, 3]})
    c = DateChunker()

    with pytest.raises(Exception) as e:
        six.next(c.to_chunks(df, 'D'))
    assert('datetime indexed' in str(e))

    df.columns = ['date']
    with pytest.raises(Exception) as e:
        six.next(c.to_chunks(df, 'ZSDFG'))
    assert('Unknown freqstr' in str(e) or 'Invalid frequency' in str(e))


def test_exclude():
    c = DateChunker()
    df = DataFrame(data={'data': [1, 2, 3]},
                   index=MultiIndex.from_tuples([(dt(2016, 1, 1), 1),
                                                 (dt(2016, 1, 2), 1),
                                                 (dt(2016, 1, 3), 1)],
                                                names=['date', 'id'])
                   )

    df2 = DataFrame(data={'data': [1, 2, 3]})

    assert(c.exclude(df, DateRange(dt(2016, 1, 1), dt(2016, 1, 1))).equals(c.exclude(df, pd.date_range(dt(2016, 1, 1), dt(2016, 1, 1)))))
    assert(c.exclude(df2, None).equals(df2))


def test_exclude_no_index():
    c = DateChunker()
    df = DataFrame(data={'data': [1, 2, 3],
                         'date': [dt(2016, 1, 1),
                                  dt(2016, 1, 2),
                                  dt(2016, 1, 3)]
                         }
                   )

    df2 = DataFrame(data={'data': [1, 2, 3]})

    assert(c.exclude(df, DateRange(dt(2016, 1, 1), dt(2016, 1, 1))).equals(c.exclude(df, pd.date_range(dt(2016, 1, 1), dt(2016, 1, 1)))))
    assert(c.exclude(df2, None).equals(df2))


def test_with_tuples():
    c = DateChunker()
    df = DataFrame(data={'data': [1, 2, 3],
                         'date': [dt(2016, 1, 1),
                                  dt(2016, 1, 2),
                                  dt(2016, 1, 3)]
                         }
                   )

    # OPEN - CLOSED
    assert_frame_equal(c.filter(df, (None, dt(2016, 1, 3))), df)
    # CLOSED - OPEN
    assert_frame_equal(c.filter(df, (dt(2016, 1, 1), None)), df)
    # OPEN - OPEN
    assert_frame_equal(c.filter(df, (None, None)), df)
    # CLOSED - OPEN (far before data range)
    assert_frame_equal(c.filter(df, (dt(2000, 1, 1), None)), df)
    # CLOSED - OPEN (far after range)
    assert(c.filter(df, (dt(2020, 1, 2), None)).empty)
    # OPEN - CLOSED
    assert_frame_equal(c.filter(df, (None, dt(2020, 1, 1))), df)
    # CLOSED - CLOSED (after range)
    assert(c.filter(df, (dt(2017, 1, 1), dt(2018, 1, 1))).empty)
