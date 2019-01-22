from __future__ import print_function

import argparse
import random
from datetime import datetime as dt
from datetime import timedelta as td
from pprint import pprint

import numpy as np
import pandas as pd
from dateutil.rrule import rrule, DAILY, MINUTELY

import arctic
from arctic import Arctic
from arctic._config import FwPointersCfg


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


def gen_column(size, dense):
    return gen_dense_col_data(size) if dense else gen_sparse_col_data(size)


def gen_dense_col_data(size):
    return [random.uniform(0.0, 1.0) for _ in range(size)]


def gen_sparse_col_data(size):
    sparse_data = []
    for val in gen_dense_col_data(size):
        sparse_data.append(val if val > 0.7 else np.NaN)

    return sparse_data


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

    print('lensparse=', len(rows))
    return rows


def gen_one_minute_rows(n_rows, dense):
    price_template = (800.0, 1200.0)
    header_attributes = {
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
        'VOLUME': (0.0, 1000.0)
    }

    data = {}
    for header, header_range in header_attributes.iteritems():
        data[header] = gen_sparse_rows_for_range(n_rows, header_range[0], header_range[1], dense)

    print(len(data), len(data['BID']))
    return data


def gen_broad_dataset(size, dense):
    timestamps = list(rrule(DAILY, count=size, dtstart=dt(1970, 1, 1), interval=1))
    df = pd.DataFrame(
        index=timestamps,
        data={'BENCH' + str(i): gen_column(size, dense) for i in range(size)},
    )
    df.index.name = 'index'
    return df


def gen_oneminute_dataset(size, dense):
    timestamps = []
    active_minutes_daily = 120
    # 6 months of 2 hour data minute each
    for day in range(0, size // 120):
        timestamps.extend(list(rrule(MINUTELY, count=active_minutes_daily, dtstart=dt(2005, 1, 1) + td(days=day))))

    timestamps.extend(list(rrule(MINUTELY, count=size % active_minutes_daily, dtstart=dt(2006, 1, 1))))
    rows = len(timestamps)
    print('len n_rows=', rows)

    return pd.DataFrame(
        index=timestamps,
        data=gen_one_minute_rows(rows, dense)
    )


def initialize_random_data(config, args, data_gen):
    store = Arctic(args.mongodb, app_name="benchmark")
    lib_name = 'bench' + str(config.name)
    store.delete_library(lib_name)
    store.initialize_library(lib_name, segment='month')
    lib = store[lib_name]

    for sym in range(args.symbols):
        lib.write('sym' + str(sym), data_gen(args.ndim, args.dense))


def append_random_rows(config, args):
    store = Arctic(args.mongodb, app_name="benchmark")
    lib_name = 'bench' + config.name
    lib = store[lib_name]

    timestamps = list(rrule(DAILY, count=args.appends, dtstart=dt(1980, 1, 1), interval=1))

    for day in range(args.appends):
        for sym in range(args.symbols):
            df = pd.DataFrame(
                index=[timestamps[day]],
                data={'BENCH' + str(i): gen_sparse_col_data(1) for i in range(args.ndim)},
            )
            lib.append('sym' + str(sym), df)


def append_random_rows_2(config, args):
    store = Arctic(args.mongodb, app_name="benchmark")
    lib_name = 'bench' + config.name
    lib = store[lib_name]

    # timestamps = list(rrule(DAILY, count=args.appends, dtstart=dt(1980, 1, 1), interval=1))

    for day in range(args.appends):
        for sym in range(args.symbols):
            df = gen_oneminute_dataset(1, False)
            lib.append('sym' + str(sym), df)


def read_all_symbols(config, args):
    store = Arctic(args.mongodb, app_name="benchmark")
    lib_name = 'bench' + config.name
    lib = store[lib_name]

    for sym in range(args.symbols):
        lib.read('sym' + str(sym))


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
    print('args=', args)
    for rounds in range(1, args.rounds + 1):
        for fwd_ptr in [FwPointersCfg.DISABLED, FwPointersCfg.ENABLED]:
            for data_gen in (gen_oneminute_dataset, gen_broad_dataset):
                with FwPointersCtx(fwd_ptr):
                    w_start = dt.now()
                    # Writes data to lib with above config.
                    initialize_random_data(fwd_ptr, args, data_gen)
                    w_end = dt.now()
                    # Appends multiple rows to each symbol
                    append_random_rows_2(fwd_ptr, args)
                    a_end = dt.now()
                    # Read everything.
                    read_all_symbols(fwd_ptr, args)
                    r_end = dt.now()
                    out = "Config: {fwd_ptr} Data Type: {data_gen} write: {wtime} append: {atime} read: {rtime}".format(
                        fwd_ptr=fwd_ptr,
                        data_gen=data_gen,
                        wtime=w_end - w_start,
                        atime=a_end - w_end,
                        rtime=r_end - a_end,
                    )
                    pprint(out)


if __name__ == '__main__':
    main(parse_args())
