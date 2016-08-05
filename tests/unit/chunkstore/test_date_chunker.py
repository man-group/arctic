from arctic.chunkstore.date_chunker import DateChunker
from pandas import DataFrame, MultiIndex
from datetime import datetime as dt
from arctic.date import DateRange
from pandas.util.testing import assert_frame_equal


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
