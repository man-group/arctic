from arctic import Arctic
import pandas as pd
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


TEST_SIZES = [1000, 10000, 100000, 1000000]
df_random = [gen_dataframe_random(5, rows) for rows in TEST_SIZES]
s_random = [gen_series_random(5 * rows) for rows in TEST_SIZES]
df_compress = [gen_dataframe_compressible(10, rows) for rows in TEST_SIZES]
s_compress = [gen_series_compressible(rows) for rows in TEST_SIZES]


class TimeSuiteWrite(object):
    params = list(range(len(TEST_SIZES)))
    param_names = ['5K * 10^']
    
    def setup(self, arg):
        self.store = Arctic("127.0.0.1")
        self.store.delete_library('test.lib')
        self.store.initialize_library('test.lib')
        self.lib = self.store['test.lib']
        
    def teardown(self, arg):
        self.store.delete_library('test.lib')
        self.lib = None

    def time_write_dataframe_random(self, idx):
       self.lib.write('df_bench_random', df_random[idx])
       
    def time_write_series_random(self, idx):
        self.lib.write('series_bench_random', s_random[idx])

    def time_write_dataframe_compressible(self, idx):
        self.lib.write('df_bench_compressible', df_compress[idx])

    def time_write_series_compressible(self, idx):
        self.lib.write('series_bench_compressible', s_compress[idx])


class TimeSuiteRead(object):
    params = list(range(len(TEST_SIZES)))
    param_names = ['5K * 10^']
    
    def __init__(self):
        self.store = Arctic("127.0.0.1")

    def setup(self, idx):
        self.store.delete_library('test.lib')
        self.store.initialize_library('test.lib')
        self.lib = self.store['test.lib']

        self.lib.write('test_df', df_random[idx])

    def teardown(self, arg):
        self.store.delete_library('test.lib')
        self.lib = None 
        
    def time_read_dataframe(self, idx):
        self.lib.read('test_df')


class TimeSuiteAppend(object):
    params = list(range(len(TEST_SIZES)))
    param_names = ['5K * 10^']
    
    def __init__(self):
        self.store = Arctic("127.0.0.1")

    def setup(self, idx):
        self.store.delete_library('test.lib')
        self.store.initialize_library('test.lib')
        self.lib = self.store['test.lib']

        self.lib.write('test_df', df_random[idx])

    def teardown(self, arg):
        self.store.delete_library('test.lib')
        self.lib = None 
        
    def time_append_dataframe(self, idx):
        self.lib.append('test_df', df_random[idx])
