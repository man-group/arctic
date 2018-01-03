"""
Unit tests for bugfixes
"""

from datetime import datetime as dt

import pandas as pd
from pandas import DataFrame, DatetimeIndex
from pandas.util.testing import assert_frame_equal
import numpy as np
from arctic.date import DateRange, CLOSED_OPEN, CLOSED_CLOSED, OPEN_OPEN, OPEN_CLOSED


# Issue 384
def test_write_dataframe(chunkstore_lib):
    # Create dataframe of time measurements taken every 6 hours
    date_range = pd.date_range(start=dt(2017, 5, 1, 1), periods=8, freq='6H')

    df = DataFrame(data={'something': [100, 200, 300, 400, 500, 600, 700, 800]},
                   index=DatetimeIndex(date_range, name='date'))


    chunkstore_lib.write('test', df, chunk_size='D')

    # Iterate
    for chunk in chunkstore_lib.iterator('test'):
        assert(len(chunk) > 0)


def test_compression(chunkstore_lib):
    """
    Issue 407 - Chunkstore was not removing the 1st segment, with segment id -1
    so on an append it would append new chunks with id 0 and 1, and a subsequent read
    would still pick up -1 (which should have been removed or overwritten).
    Since the -1 segment (which previously indicated a standalone segment) is no
    longer needed, the special -1 segment id is now removed
    """
    def generate_data(date):
        """
        Generates a dataframe that is almost exactly the size of
        a segment in chunkstore
        """
        df = pd.DataFrame(np.random.randn(10000*16, 12),
                          columns=['beta', 'btop', 'earnyild', 'growth', 'industry', 'leverage',
                                   'liquidty', 'momentum', 'resvol', 'sid', 'size', 'sizenl'])
        df['date'] = date

        return df

    date = pd.Timestamp('2000-01-01')
    df = generate_data(date)
    chunkstore_lib.write('test', df, chunk_size='A')
    date += pd.Timedelta(1, unit='D')
    df2 = generate_data(date)
    chunkstore_lib.append('test', df2)
    read = chunkstore_lib.read('test')
    assert_frame_equal(read, pd.concat([df, df2], ignore_index=True))


# issue #420 - ChunkStore doesnt respect DateRange interval
def test_date_interval(chunkstore_lib):
    date_range = pd.date_range(start=dt(2017, 5, 1), periods=8, freq='D')

    df = DataFrame(data={'data': range(8)},
                   index=DatetimeIndex(date_range, name='date'))


    # test with index
    chunkstore_lib.write('test', df, chunk_size='D')

    ret = chunkstore_lib.read('test', chunk_range=DateRange(dt(2017,5,2), dt(2017,5,5), CLOSED_OPEN))
    assert_frame_equal(ret, df[1:4])
    ret = chunkstore_lib.read('test', chunk_range=DateRange(dt(2017,5,2), dt(2017,5,5), OPEN_OPEN))
    assert_frame_equal(ret, df[2:4])
    ret = chunkstore_lib.read('test', chunk_range=DateRange(dt(2017,5,2), dt(2017,5,5), OPEN_CLOSED))
    assert_frame_equal(ret, df[2:5])
    ret = chunkstore_lib.read('test', chunk_range=DateRange(dt(2017,5,2), dt(2017,5,5), CLOSED_CLOSED))
    assert_frame_equal(ret, df[1:5])
    ret = chunkstore_lib.read('test', chunk_range=DateRange(dt(2017,5,2), None, CLOSED_OPEN))
    assert_frame_equal(ret, df[1:8])

    # test without index
    df = DataFrame(data={'data': range(8),
                         'date': date_range})

    chunkstore_lib.write('test2', df, chunk_size='D')

    ret = chunkstore_lib.read('test2', chunk_range=DateRange(dt(2017,5,2), dt(2017,5,5), CLOSED_OPEN))
    assert(len(ret) == 3)
    ret = chunkstore_lib.read('test2', chunk_range=DateRange(dt(2017,5,2), dt(2017,5,5), OPEN_OPEN))
    assert(len(ret) == 2)
    ret = chunkstore_lib.read('test2', chunk_range=DateRange(dt(2017,5,2), dt(2017,5,5), OPEN_CLOSED))
    assert(len(ret) == 3)
    ret = chunkstore_lib.read('test2', chunk_range=DateRange(dt(2017,5,2), dt(2017,5,5), CLOSED_CLOSED))
    assert(len(ret) == 4)
    ret = chunkstore_lib.read('test2', chunk_range=DateRange(dt(2017,5,2), None, CLOSED_OPEN))
    assert(len(ret) == 7)


def test_rewrite(chunkstore_lib):
    """
    Issue 427
    incorrectly storing and updating metadata. dataframes without an index
    have no "index" field in their metadata, so updating existing 
    metadata does not remove the index field. 
    Also, metadata was incorrectly being stored. symbol, start, and end
    are the index for the collection, but metadata was being
    stored without an index (so it was defaulting to null,null,null)
    """
    date_range = pd.date_range(start=dt(2017, 5, 1, 1), periods=8, freq='6H')

    df = DataFrame(data={'something': [100, 200, 300, 400, 500, 600, 700, 800]},
                   index=DatetimeIndex(date_range, name='date'))


    chunkstore_lib.write('test', df, chunk_size='D')

    df2 = DataFrame(data={'something': [100, 200, 300, 400, 500, 600, 700, 800],
                          'date': date_range})

    chunkstore_lib.write('test', df2, chunk_size='D')
    ret = chunkstore_lib.read('test')
    assert_frame_equal(ret, df2)


def test_iterator(chunkstore_lib):
    """
    Fixes issue #431 - iterator methods were not taking into account
    the fact that symbols can have multiple segments
    """
    def generate_data(date):
        """
        Generates a dataframe that is larger than one segment
        a segment in chunkstore
        """
        df = pd.DataFrame(np.random.randn(200000, 12),
                          columns=['beta', 'btop', 'earnyild', 'growth', 'industry', 'leverage',
                                   'liquidty', 'momentum', 'resvol', 'sid', 'size', 'sizenl'])
        df['date'] = date

        return df

    date = pd.Timestamp('2000-01-01')
    df = generate_data(date)
    chunkstore_lib.write('test', df, chunk_size='A')
    ret = chunkstore_lib.get_chunk_ranges('test')
    assert(len(list(ret)) == 1)
