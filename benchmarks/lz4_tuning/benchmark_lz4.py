from __future__ import print_function

import random
from datetime import datetime as dt
from multiprocessing.pool import ThreadPool

import numpy as np
import pandas as pd

import arctic._compression as c
from arctic.serialization.numpy_records import DataFrameSerializer

c.enable_parallel_lz4(True)
c.BENCHMARK_MODE = True


def get_random_df(nrows, ncols):
    ret_df = pd.DataFrame(np.random.randn(nrows, ncols),
                          index=pd.date_range('20170101',
                                              periods=nrows, freq='S'),
                          columns=["".join([chr(random.randint(ord('A'), ord('Z'))) for _ in range(8)]) for _ in
                                   range(ncols)])
    ret_df.index.name = 'index'
    ret_df.index = ret_df.index.tz_localize('UTC')
    return ret_df


def construct_test_data(df_length, append_mul):
    serializer = DataFrameSerializer()
    tmp_df = get_random_df(df_length, 10)
    recs = serializer.serialize(tmp_df)[0]
    _str = recs.tostring()
    if append_mul > 1:
        _str = "".join([_str] * append_mul)
    return _str


def bench_compression_comparison(n_chunks, df_length, append_mul, pool_size, pool_step, repeats,
                                 use_raw_lz4, use_HC):
    _str = construct_test_data(df_length, append_mul)
    chunk_size = len(_str) / 1024 ** 2.0
    _strarr = [_str] * n_chunks

    # Single threaded
    # ---------------
    measurements = bench_single(repeats, _strarr, use_HC)
    print_results(1, chunk_size, n_chunks, chunk_size*n_chunks, measurements)
    single_mean = np.mean(measurements)

    # Multi-threaded
    # --------------
    for sz in range(2, pool_size + 1, pool_step):
        if use_raw_lz4:
            pool = ThreadPool(sz)
        else:
            pool = None
            c.set_compression_pool_size(sz)
        measurements = bench_multi(repeats, _strarr, use_HC, pool=pool)
        print_results(sz, chunk_size, n_chunks, chunk_size * n_chunks, measurements, compare=single_mean)
        if pool:
            pool.close()
            pool.join()
    print("")


def bench_single(repeats, _strarr, use_HC):
    # Arctic compress single
    measurements = []
    for i in range(repeats):
        now = dt.now()
        if use_HC:
            res = [c.compressHC(x) for x in _strarr]
        else:
            res = [c.compress(x) for x in _strarr]
        sample = (dt.now() - now).total_seconds()
        assert all(res)
        measurements.append(sample)
    return measurements


def bench_multi(repeats, _strarr, use_HC, pool=None):
    measurements = []
    for j in range(repeats):
        now = dt.now()
        if pool:
            # Raw LZ4 lib
            if use_HC:
                res = pool.map(c.lz4_compressHC, _strarr)
            else:
                res = pool.map(c.lz4_compress, _strarr)
        else:
            # Arctic's compression layer
            if use_HC:
                res = c.compressHC_array(_strarr)
            else:
                res = c.compress_array(_strarr, withHC=False)
        sample = (dt.now() - now).total_seconds()
        assert len(res) == len(_strarr)
        assert all(res)
        measurements.append(sample)
    return measurements


def print_results(n_threads, chunk_size, n_chunks, total_mb, measurements, compare=None):
    mymean = np.mean(measurements)
    xfaster = (compare/float(mymean)) if compare is not None else 0
    measurements = n_threads, chunk_size, n_chunks, total_mb, \
                   mymean, np.min(measurements), np.max(measurements), np.std(measurements), \
                   ("{:.2f}x faster than single threaded".format(xfaster) if xfaster > 1 else "")
    print("(x{:<3}threads) ({:.1f} MB/chunk, x{:<4} chunks, total {:.1f} MB) \t "
          "mean={:.6f} min={:.6f} max={:.6f} std={:.8f} {}".format(*measurements))


def main():
    use_HC = False
    for df_length in (1000, 3000, 10000, 30000):
        for n_chunks in (1, 2, 4, 8, 16, 32, 64, 128):
            print("\n\n----------- High compression: {}, Chunks: {}, DataFrame size: {} ------------".format(use_HC, n_chunks, df_length))
            bench_compression_comparison(
                n_chunks=n_chunks,
                df_length=df_length,
                append_mul=1,
                pool_size=10,
                pool_step=2,
                repeats=30,
                use_raw_lz4=False,
                use_HC=use_HC)


if __name__ == '__main__':
    main()
