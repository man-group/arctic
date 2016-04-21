from arctic import Arctic
import pandas as pd
from datetime import datetime as dt
import random


def gen_dataframe_random(cols, rows):
    c = {}
    for col in range(cols):
        c[str(col)] = [round(random.uniform(-10000.0, 10000.0), 1) for r in range(rows)]
    index = [range(rows)]

    return pd.DataFrame(data=c, index=index)


def gen_series_random(rows):
    col = [round(random.uniform(-10000.0, 10000.0), 1) for r in range(rows)]
    return pd.Series(data=col, index=list(range(rows)))


def gen_dataframe_compressible(cols, rows):
    row = [round(random.uniform(-100.0, 100.0), 1) for r in range(cols)]
    data = [row] * rows
    index = [range(rows)]

    return pd.DataFrame(data=data, index=index)


def gen_series_compressible(rows):
    d = round(random.uniform(-100.0, 100.0), 1)
    data = [d * rows]
        
    index = [range(rows)]

    return pd.Series(data=data, index=index)


class TimeSuite(object):
    def __init__(self):
        self.df_random = gen_dataframe_random(5, 10000)
        self.s_random = gen_series_random(50000)
        self.df_random_big = gen_dataframe_random(10, 1000000)
        self.s_random_big = gen_series_random(10000000)
        self.df_compress = gen_dataframe_compressible(10, 1000000)
        self.s_compress = gen_series_compressible(10000000)

    def setup(self):
        self.store = Arctic("127.0.0.1")
        self.store.delete_library('test.lib')
        self.store.initialize_library('test.lib')
        self.lib = self.store['test.lib']
        
    def teardown(self):
        self.store.delete_library('test.lib')
        self.lib = None

    def time_write_dataframe_random(self):
       self.lib.write('df_bench_random', self.df_random)

    def time_write__series_random(self):
        self.lib.write('series_bench_random', self.s_random)

    def time_write_dataframe_random_massive(self):
       self.lib.write('df_bench_random_massive', self.df_random_big)

    def time_write_series_random_massive(self):
        self.lib.write('series_bench_random_massive', self.s_random_big)

    def time_write_dataframe_compressible(self):
        self.lib.write('df_bench_compressible', self.df_compress)

    def time_write_series_compressible(self):
        self.lib.write('series_bench_compressible', self.s_compress)
        

