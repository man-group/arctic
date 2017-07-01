"""
Unit tests for bugfixes
"""

from datetime import datetime

import pandas as pd
from pandas import DataFrame, DatetimeIndex


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
