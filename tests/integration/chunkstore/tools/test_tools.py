import numpy as np
import pandas as pd
from pandas.util.testing import assert_frame_equal

from arctic.chunkstore.tools import segment_id_repair
from ..test_fixes import assert_frame_equal_


def test_segment_repair_tool(chunkstore_lib):
    """
    Issue 442 - Data already written with -1 as the segment needs to be updated on update and appends
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

    def get_segments():
        return sorted(chunkstore_lib._collection.distinct('sg', {'sy': 'test'}))

    date = pd.Timestamp('2000-01-01')
    df = generate_data(date)
    chunkstore_lib.write('test', df, chunk_size='A')

    chunkstore_lib.write('other_data', generate_data(date), chunk_size='D')
    other_data = chunkstore_lib.read('other_data')
    chunkstore_lib.write('more_data', generate_data(date), chunk_size='Q')
    more_data = chunkstore_lib.read('more_data')

    assert(get_segments() == [0])
    chunkstore_lib._collection.update_one({'sy': 'test'}, {'$set': {'sg': -1}})
    assert(get_segments() == [-1])

    symbols = segment_id_repair(chunkstore_lib)
    assert(symbols == ['test'])
    assert(get_segments() == [0])

    date += pd.Timedelta(1, unit='D')
    df2 = generate_data(date)

    chunkstore_lib.append('test', df2)
    assert(get_segments() == [0, 1])

    read = chunkstore_lib.read('test')

    assert_frame_equal_(read, pd.concat([df, df2], ignore_index=True))

    chunkstore_lib._collection.update_one({'sy': 'test', 'sg': 0}, {'$set': {'sg': -1}})
    chunkstore_lib._collection.update_one({'sy': 'test', 'sg': 1}, {'$set': {'sg': 0}})
    assert(get_segments() == [-1, 0])

    symbols = segment_id_repair(chunkstore_lib, 'test')
    assert(get_segments() == [0, 1])
    assert(symbols == ['test'])

    assert_frame_equal_(chunkstore_lib.read('more_data'), more_data)
    assert_frame_equal_(chunkstore_lib.read('other_data'), other_data)
