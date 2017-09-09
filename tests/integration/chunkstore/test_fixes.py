"""
Unit tests for bugfixes
"""

from datetime import datetime

import pandas as pd
from pandas import DataFrame, DatetimeIndex
from pandas.util.testing import assert_frame_equal
import numpy as np
import time

# Issue 384
def test_write_dataframe(chunkstore_lib):
    # Create dataframe of time measurements taken every 6 hours
    date_range = pd.date_range(start=datetime(2017, 5, 1, 1), periods=8, freq='6H')

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
