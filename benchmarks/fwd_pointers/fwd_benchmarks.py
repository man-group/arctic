from __future__ import print_function

import random
from datetime import datetime as dt

import pandas as pd
import pytest
from dateutil.rrule import rrule, DAILY

import arctic
from arctic import Arctic
from arctic._config import FwPointersCfg

DATAFRAME_DIM = 1000
N_SYMBOLS = 5
N_APPENDS = 10


class FwPointersCtx:
    def __init__(self, value_to_test, do_reconcile=True):
        self.value_to_test = value_to_test
        self.do_reconcile = do_reconcile

    def __enter__(self):
        self.orig_value = arctic.store._ndarray_store.ARCTIC_FORWARD_POINTERS_CFG
        arctic.store._ndarray_store.ARCTIC_FORWARD_POINTERS_CFG = self.value_to_test

        self.reconcile_orig_value = arctic.store._ndarray_store.ARCTIC_FORWARD_POINTERS_RECONCILE
        arctic.store._ndarray_store.ARCTIC_FORWARD_POINTERS_RECONCILE = self.do_reconcile

    def __exit__(self, *args):
        arctic.store._ndarray_store.ARCTIC_FORWARD_POINTERS_CFG = self.orig_value
        arctic.store._ndarray_store.ARCTIC_FORWARD_POINTERS_RECONCILE = self.reconcile_orig_value


def gen_sparse_col_data(size):
    return [random.uniform(0.0, 1.0) for _ in range(size)]


def get_large_sparse_df(size=DATAFRAME_DIM):
    timestamps = list(rrule(DAILY, count=size, dtstart=dt(1970, 1, 1), interval=1))
    df = pd.DataFrame(index=timestamps, data={'BENCH' + str(i): gen_sparse_col_data(size) for i in range(size)})
    df.index.name = 'index'
    return df


def initialize_random_data(config, n_symbols=N_SYMBOLS):
    store = Arctic("127.0.0.1", app_name="benchmark")
    lib_name = 'bench' + str(config.name)
    store.delete_library(lib_name)
    store.initialize_library(lib_name, segment='month')
    lib = store[lib_name]
    start_time = dt.now()

    for sym in range(n_symbols):
        lib.write('sym' + str(sym), get_large_sparse_df(DATAFRAME_DIM))

    print(lib_name, 'time taken for writing', n_symbols, 'symbols=', str(dt.now() - start_time))


def append_random_rows(config, n_symbols=N_SYMBOLS, n_appends=N_APPENDS):
    store = Arctic("127.0.0.1", app_name="benchmark")
    lib_name = 'bench' + config.name
    lib = store[lib_name]

    timestamps = list(rrule(DAILY, count=n_appends, dtstart=dt(1980, 1, 1), interval=1))

    start = dt.now()
    for day in range(n_appends):
        for sym in range(n_symbols):
            df = pd.DataFrame(index=[timestamps[day]],
                              data={'BENCH' + str(i): gen_sparse_col_data(1) for i in range(DATAFRAME_DIM)})
            lib.append('sym' + str(sym), df)

    print(config, 'time for appends=', dt.now() - start)


def read_all_symbols(config, n_symbols=N_SYMBOLS):
    store = Arctic("127.0.0.1", app_name="benchmark")
    lib_name = 'bench' + config.name
    lib = store[lib_name]

    start = dt.now()
    for sym in range(n_symbols):
        lib.read('sym' + str(sym))

    print(config, 'time for reads=', dt.now() - start)


@pytest.mark.parametrize('fw_pointers_cfg', [FwPointersCfg.DISABLED, FwPointersCfg.ENABLED])
def test_benchmark_initial_writes(benchmark, fw_pointers_cfg):
    with FwPointersCtx(fw_pointers_cfg):
        benchmark(initialize_random_data, fw_pointers_cfg)


@pytest.mark.parametrize('fw_pointers_cfg', [FwPointersCfg.DISABLED, FwPointersCfg.ENABLED])
def test_benchmark_appends(benchmark, fw_pointers_cfg):
    with FwPointersCtx(fw_pointers_cfg):
        benchmark(append_random_rows, fw_pointers_cfg)


@pytest.mark.parametrize('fw_pointers_cfg', [FwPointersCfg.DISABLED, FwPointersCfg.ENABLED])
def test_benchmark_reads(benchmark, fw_pointers_cfg):
    with FwPointersCtx(fw_pointers_cfg):
        benchmark(read_all_symbols, fw_pointers_cfg)

# For 10 symbols, 400 * 400 dataframe of dense non compressible floats
# ------------------------------------------------------------------------------------------------------------- benchmark: 6 tests ------------------------------------------------------------------------------------------------------------
# Name (time in ms)                                                Min                    Max                   Mean              StdDev                 Median                   IQR            Outliers     OPS            Rounds  Iterations
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# test_benchmark_reads[FwPointersCfg.DISABLED]                450.5870 (1.0)         761.6360 (1.0)         613.6972 (1.0)      142.5660 (1.78)        672.2870 (1.0)        256.6150 (2.06)          2;0  1.6295 (1.0)           5           1
# test_benchmark_reads[FwPointersCfg.ENABLED]                 643.4429 (1.43)        842.4399 (1.11)        727.9922 (1.19)      79.9812 (1.0)         710.1989 (1.06)       124.3826 (1.0)           2;0  1.3736 (0.84)          5           1
# test_benchmark_initial_writes[FwPointersCfg.DISABLED]     3,005.1329 (6.67)      3,923.0299 (5.15)      3,460.2518 (5.64)     364.0607 (4.55)      3,560.9770 (5.30)       552.6620 (4.44)          2;0  0.2890 (0.18)          5           1
# test_benchmark_initial_writes[FwPointersCfg.ENABLED]      3,045.5260 (6.76)      3,922.6911 (5.15)      3,576.7886 (5.83)     383.0169 (4.79)      3,723.5370 (5.54)       647.0396 (5.20)          1;0  0.2796 (0.17)          5           1
# test_benchmark_appends[FwPointersCfg.ENABLED]             8,752.4891 (19.42)    10,737.2870 (14.10)     9,828.6706 (16.02)    787.2417 (9.84)     10,135.1271 (15.08)    1,160.0124 (9.33)          2;0  0.1017 (0.06)          5           1
# test_benchmark_appends[FwPointersCfg.DISABLED]            9,571.1629 (21.24)    10,461.5810 (13.74)    10,037.6498 (16.36)    428.2198 (5.35)     10,121.5491 (15.06)      830.3056 (6.68)          1;0  0.0996 (0.06)          5           1
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# For 5 symbols, 1000 * 1000 dataframes
# Name (time in ms)                                                 Min                    Max                   Mean                StdDev                 Median                   IQR            Outliers     OPS            Rounds  Iterations
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# test_benchmark_reads[FwPointersCfg.DISABLED]                 749.7921 (1.0)       1,248.1289 (1.0)       1,111.1230 (1.0)        206.1699 (2.08)      1,198.9460 (1.0)        188.7886 (2.18)          1;1  0.9000 (1.0)           5           1
# test_benchmark_reads[FwPointersCfg.ENABLED]                1,102.4671 (1.47)      1,381.5191 (1.11)      1,234.2305 (1.11)        99.2820 (1.0)       1,234.3352 (1.03)        86.5338 (1.0)           2;0  0.8102 (0.90)          5           1
# test_benchmark_initial_writes[FwPointersCfg.ENABLED]       7,951.3612 (10.60)     8,759.4709 (7.02)      8,397.5395 (7.56)       350.7886 (3.53)      8,563.1211 (7.14)       586.5314 (6.78)          2;0  0.1191 (0.13)          5           1
# test_benchmark_initial_writes[FwPointersCfg.DISABLED]      8,508.2960 (11.35)     9,951.0078 (7.97)      9,357.5314 (8.42)       527.2797 (5.31)      9,452.2710 (7.88)       497.9144 (5.75)          2;0  0.1069 (0.12)          5           1
# test_benchmark_appends[FwPointersCfg.DISABLED]            13,871.8622 (18.50)    17,470.3519 (14.00)    15,393.9694 (13.85)    1,458.8612 (14.69)    15,252.0301 (12.72)    2,314.6288 (26.75)         2;0  0.0650 (0.07)          5           1
# test_benchmark_appends[FwPointersCfg.ENABLED]             14,742.6510 (19.66)    18,822.4950 (15.08)    16,123.7998 (14.51)    1,566.8014 (15.78)    15,768.5201 (13.15)    1,231.3927 (14.23)         1;1  0.0620 (0.07)          5           1
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
