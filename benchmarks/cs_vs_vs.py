import pandas as pd
from datetime import datetime as dt
import numpy as np
from contextlib import contextmanager
from arctic import Arctic
import arctic as a


results = []


for nstocks in (100, 1000, 5000):
    for random_switch in (0,1,2,3):
        for drange in (pd.date_range(dt(2017,1,1),dt(2017,12,31)), pd.date_range(dt(2017,1,1),dt(2019,12,31)), pd.date_range(dt(2015,1,1),dt(2019,12,31))):
            print('====== Range: {} {}'.format(drange[0], drange[-1]))
            if random_switch == 0:
                ss = 'same data'
            if random_switch == 1:
                ss = 'random data per day'
            if random_switch == 2:
                ss = 'random data per day per security'
            if random_switch == 3:
                ss = 'random of all three'
            print('Random data: {}'.format(ss))
            stocks = range(nstocks)
            dates = drange
            rows = []
            random_data_all_same = list(np.random.random_sample(5))
            for d in dates:
                random_data_per_date = list(np.random.random_sample(5))
                for s in stocks:
                    random_data_per_stock = list(np.random.random_sample(5))
                    if random_switch == 3:
                        _switch = np.random.randint(0,4)
                    else:
                        _switch = random_switch
                    if _switch == 0:
                        data = random_data_all_same
                    if _switch == 1:
                        data = random_data_per_date
                    if _switch == 2:
                        data = random_data_per_stock
                    rows.append([d, s] + data)
            df = pd.DataFrame(rows, columns=['date','id','v1','v2','v3','v4','v5']).set_index(['date','id'])

            print(df.memory_usage(index=True).sum() / 1e6, 'mb dataframe size')

            a = Arctic('localhost')
            a.delete_library('test.vs')
            a.delete_library('test.cs')
            a.initialize_library('test.vs')
            a.initialize_library('test.cs', type='CHUNK_STORE_TYPE')
            vs = a['test.vs']
            cs = a['test.cs']

            size = df.memory_usage(index=True).sum() / 1e6
            res = [drange[0], drange[-1], nstocks, ss, size]

            @contextmanager
            def timeit():
                now = dt.now()
                yield
                elap = (dt.now() - now).total_seconds()
                print('Took: {}'.format(elap))
                res.append(elap)

            # time to save whole item
            print('-- write all --')
            with timeit():
                vs.write('foo', df)

            with timeit():
                cs.write('foo', df)

            # time to read whole item
            print('-- r all --')
            with timeit():
                vs.read('foo')

            with timeit():
                cs.read('foo')

            # time to read single day
            print('-- single day --')
            from arctic.date import DateRange
            with timeit():
                vs.read('foo', date_range=DateRange('20170728','20170728'))

            with timeit():
                cs.read('foo', date_range=DateRange('20170728','20170728'))

            # time to read 1 year
            print('-- single year --')
            with timeit():
                vs.read('foo', date_range=DateRange('20170101','20180101'))

            with timeit():
                cs.read('foo', date_range=DateRange('20170101','20180101'))

            # time to append single day
            print('-- a single day --')
            s = df[df.index.get_level_values('date') == df.index.get_level_values('date')[-1]]
            with timeit():
                vs.append('foo', s)

            with timeit():
                cs.append('foo', s)

            results.append(res)

print(results)

df = pd.DataFrame(results,
             columns=['start_date',
                      'end_date',
                      'stocks per day',
                      'random-style',
                      'size (mb)',
                      'vs write all',
                      'cs write all',
                      'vs read all',
                      'cs read all',
                      'vs read 1 day',
                      'cs read 1 day',
                      'vs read 1 year',
                      'cs read 1 year',
                      'vs append 1 day',
                      'cs append 1 day'])