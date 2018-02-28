import random
from datetime import datetime as dt
from datetime import timedelta

import pandas as pd
from pandas import DataFrame, Index, MultiIndex
from pandas.util.testing import assert_frame_equal

from arctic.chunkstore.utils import read_apply


def create_test_data(size=5, index=True, multiindex=True, random_data=True, random_ids=True, date_offset=0, cols=1):
    data = {}
    for i in range(cols):
        if random_data:
            data['data' + str(i)] = [random.random() * random.randint(-100, 100) for _ in range(size)]
        else:
            data['data' + str(i)] = range(size)
    dates = [dt(2016, 1, 1) + timedelta(days=n+date_offset) for n in range(size)]
    if index:
        if multiindex:
            if random_ids:
                idx = [(date, random.randint(1, size)) for date in dates]
            else:
                idx = [(date, 1) for date in dates]
            index = MultiIndex.from_tuples(idx, names=['date', 'id'])
            return DataFrame(data=data, index=index)
        return DataFrame(data=data, index=Index(data=dates, name='date'))
    data.update({'date': dates})
    return DataFrame(data=data)


def test_read_apply(chunkstore_lib):
    df = create_test_data(index=False, size=20)
    chunkstore_lib.write('test', df, chunk_size='M')

    def func(df):
        df['data0'] += 1.0
        return df

    for data in read_apply(chunkstore_lib, 'test', func):
        assert_frame_equal(data, func(df))