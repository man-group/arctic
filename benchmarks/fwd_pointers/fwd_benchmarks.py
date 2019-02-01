from __future__ import print_function

import argparse
import random
from collections import defaultdict
from datetime import datetime as dt
from datetime import timedelta as td

import numpy as np
import pandas as pd
from dateutil.rrule import rrule, MINUTELY

import arctic
from arctic import Arctic
from arctic._config import FwPointersCfg
# import matplotlib.pyplot as plt

price_template = (800.0, 1200.0)

ONE_MIN_ATTRIBUTES = {
    'BID': price_template,
    'BID_TWAP': price_template,
    'ASK': price_template,
    'ASK_TWAP': price_template,
    'HIGH': price_template,
    'LOW': price_template,
    'CLOSE': price_template,
    'TWAP': price_template,
    'ASKSIZE': (0.0, 400.0),
    'BIDSIZE': (0.0, 400.0),
    'TICK_COUNT': (1.0, 50.0),
    'VOLUME': (0.0, 1000.0),
}

APPEND_NROWS = 10


class FwPointersCtx:
    def __init__(self, value_to_test, do_reconcile=False):
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


def gen_sparse_rows_for_range(n_rows, low, high, dense):
    if dense:
        return [random.uniform(low, high) for _ in range(n_rows)]
    current = 0
    rows = []
    while current < n_rows:
        value = float(random.randrange(low, high))
        repetitions = min(random.randint(0, 20), n_rows - current)
        rows.extend([value] * repetitions)
        current += repetitions

    return rows


def gen_one_minute_rows(n_rows, dense):
    data = {}
    for header, header_range in ONE_MIN_ATTRIBUTES.iteritems():
        data[header] = gen_sparse_rows_for_range(n_rows, header_range[0], header_range[1], dense)

    return data


def gen_oneminute_dataset(n_row, n_col, dense):
    timestamps = []
    active_minutes_daily = 120
    for day in range(0, n_row // 120):
        timestamps.extend(list(rrule(MINUTELY, count=active_minutes_daily, dtstart=dt(2005, 1, 1) + td(days=day))))

    timestamps.extend(list(rrule(
        MINUTELY,
        count=n_row % active_minutes_daily,
        dtstart=dt(random.randrange(2006, 2016), 1, 1)),
    ))

    return pd.DataFrame(
        index=timestamps,
        data=gen_one_minute_rows(n_row, dense)
    )


def lib_name_from_args(config):
    return 'bench2_{cfg}'.format(
        cfg=config.name,
    )


def insert_random_data(config, args, n_rows):
    store = Arctic(args.mongodb, app_name="benchmark")
    lib_name = lib_name_from_args(config)
    store.delete_library(lib_name)
    store.initialize_library(lib_name, segment='month')
    lib = store[lib_name]

    for sym in range(args.symbols):
        df = gen_oneminute_dataset(n_row=n_rows, n_col=n_rows, dense=args.dense)
        lib.write('sym' + str(sym), df)


def append_random_rows(config, args, n_rows):
    store = Arctic(args.mongodb, app_name="benchmark")
    lib_name = lib_name_from_args(config)

    lib = store[lib_name]

    for _ in range(args.appends):
        for sym in range(args.symbols):
            df = gen_oneminute_dataset(n_row=APPEND_NROWS, n_col=n_rows, dense=False)
            lib.append('sym' + str(sym), df)


def read_all_symbols(config, args):
    store = Arctic(args.mongodb, app_name="benchmark")
    lib_name = lib_name_from_args(config)

    lib = store[lib_name]

    symbol_df = []
    for sym in range(args.symbols):
        symbol_df.append(lib.read('sym' + str(sym)))

    # Basic sanity checks while reading back
    sample_df = symbol_df[0].data
    assert sorted(sample_df.dtypes) == ['float64'] * len(ONE_MIN_ATTRIBUTES)
    assert 800.0 <= sample_df['BID'][0] <= 1200.0


def mean_timedelta(timedelta_list):
    return np.sum(timedelta_list) / len(timedelta_list)


def parse_args():
    parser = argparse.ArgumentParser()

    parser.add_argument('-r', '--rounds', type=int, help="number of rounds to run benchmarks", default=2)
    parser.add_argument('-a', '--appends', type=int, help="number of appends for each symbol", default=75)
    parser.add_argument('-n', '--ndim', type=int, help="dimension of dataframe = size * size", default=500)
    parser.add_argument('-e', '--dense', help="Use dense or sparse (70 ish Nans) data", action="store_true")
    parser.add_argument('-d', '--mongodb', help="Mongo db endpoint.", default="127.0.0.1")
    parser.add_argument('-y', '--symbols', type=int, help="Total number of symbols to use", default=5)

    return parser.parse_args()


def main(args):
    measure = defaultdict(list)
    data_size = [
        100,
        500,
        1000,
        # 5000,
        # 10000,
        # 200000
    ]
    print('Arguments=', args)

    for fwd_ptr in [FwPointersCfg.ENABLED, FwPointersCfg.DISABLED, FwPointersCfg.HYBRID]:
        for n_rows in data_size:
            for rounds in range(1, args.rounds + 1):
                with FwPointersCtx(fwd_ptr):
                    w_start = dt.now()
                    # Writes data to lib with above config.
                    insert_random_data(fwd_ptr, args, n_rows)
                    w_end = dt.now()
                    # Appends multiple rows to each symbol
                    append_random_rows(fwd_ptr, args, n_rows)
                    a_end = dt.now()
                    # Read everything.
                    read_all_symbols(fwd_ptr, args)
                    r_end = dt.now()
                    print('read time=', r_end - a_end)
                    measure[n_rows].append(
                        {
                            'dfsize': (n_rows, len(ONE_MIN_ATTRIBUTES)),
                            'wtime': w_end - w_start,
                            'atime': a_end - w_end,
                            'rtime': r_end - a_end,
                            'fwd': fwd_ptr
                        }
                    )

    enabled_reads = {}
    disabled_reads = {}

    for dsize in data_size:
        enabled_reads[dsize] = mean_timedelta(
            [data['rtime'] for data in measure[dsize] if data['fwd'] == FwPointersCfg.ENABLED])
        disabled_reads[dsize] = mean_timedelta(
            [data['rtime'] for data in measure[dsize] if data['fwd'] == FwPointersCfg.DISABLED])

    print('enabled read times=', enabled_reads)
    print('disabled read times=', disabled_reads)


if __name__ == '__main__':
    main(parse_args())
