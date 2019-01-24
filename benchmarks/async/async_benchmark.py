import time

from six.moves import xrange

import arctic._compression as aclz4
from arctic import Arctic
from arctic.async import ASYNC_ARCTIC, async_arctic_submit, async_wait_requests
from tests.integration.chunkstore.test_utils import create_test_data

a = Arctic('localhost:27017')
library_name = 'asyncbench.test'

TEST_DATA_CACHE = {}


def get_cached_random_df(num_chunks):
    if num_chunks < 1:
        raise ValueError("num_chunks must be > 1")
    if num_chunks not in TEST_DATA_CACHE:
        TEST_DATA_CACHE[num_chunks] = get_random_df(num_chunks)
    return TEST_DATA_CACHE[num_chunks]


def get_random_df(num_chunks):
    num_chunks = num_chunks
    data_to_write = create_test_data(size=25000, index=True, multiindex=False, random_data=True, random_ids=True,
                                     use_hours=True, date_offset=0, cols=10)
    data_to_write = data_to_write.append([data_to_write] * (num_chunks - 1))
    return data_to_write


def get_stats(measurements):
    import numpy as np
    mean = np.mean(measurements)
    stdev = np.std(measurements)
    min = np.min(measurements)
    max = np.max(measurements)
    return mean, stdev, min, max


def clean_lib():
    a.delete_library(library_name)
    a.initialize_library(library_name)


def async_bench(num_requests, num_chunks):
    data = get_cached_random_df(num_chunks)
    lib = a[library_name]
    requests = [async_arctic_submit(lib, lib.write, True, symbol='sym_{}'.format(x), data=data)
                for x in xrange(num_requests)]
    async_wait_requests(requests, do_raise=True)


def serial_bench(num_requests, num_chunks):
    data = get_cached_random_df(num_chunks)
    lib = a[library_name]
    for x in xrange(num_requests):
        lib.write(symbol='sym_{}'.format(x), data=data)


def run_scenario(result_text, rounds, num_requests, num_chunks, parallel_lz4,
                 use_async, async_arctic_pool_workers=None):
    aclz4.enable_parallel_lz4(parallel_lz4)
    if async_arctic_pool_workers is not None:
        ASYNC_ARCTIC.reset(pool_size=int(async_arctic_pool_workers), timeout=10)
    measurements = []
    for curr_round in xrange(rounds):
        # print("Running round {}".format(curr_round))
        clean_lib()
        start = time.time()
        if use_async:
            async_bench(num_requests, num_chunks)
        else:
            serial_bench(num_requests, num_chunks)
        measurements.append(time.time() - start)
    print("{}: async={}, chunks/write={}, writes/round={}, rounds={}, "
          "parallel_lz4={}, async_arctic_pool_workers={}: {}".format(
        result_text, use_async, num_chunks, num_requests, rounds, parallel_lz4, async_arctic_pool_workers,
        ["{:.3f}".format(x) for x in get_stats(measurements[1:] if len(measurements) > 1 else measurements)]))


def main():
    n_use_async = (False, True)

    n_rounds = (1,)
    n_num_requests = (8,)
    n_num_chunks = (4,)

    n_parallel_lz4 = (False,)

    n_async_arctic_pool_workers = (2, 4, 8)

    for num_chunks in n_num_chunks:
        for use_async in n_use_async:
            for async_arctic_pool_workers in (n_async_arctic_pool_workers if use_async else (4,)):
                for parallel_lz4 in n_parallel_lz4:
                    for num_requests in n_num_requests:
                        for rounds in n_rounds:
                            run_scenario(
                                result_text="Experiment results",
                                use_async=use_async,
                                rounds=rounds,
                                num_requests=num_requests,
                                num_chunks=num_chunks,
                                parallel_lz4=parallel_lz4,
                                async_arctic_pool_workers=async_arctic_pool_workers)


if __name__ == '__main__':
    main()

# Experiment results: async=False, chunks/write=2, writes/round=64, rounds=2, parallel_lz4=False, async_arctic_pool_workers=4: ['10.109', '0.000', '10.109', '10.109']
# Experiment results: async=True, chunks/write=2, writes/round=64, rounds=2, parallel_lz4=False, async_arctic_pool_workers=2: ['7.169', '0.000', '7.169', '7.169']
# Experiment results: async=True, chunks/write=2, writes/round=64, rounds=2, parallel_lz4=False, async_arctic_pool_workers=4: ['5.327', '0.000', '5.327', '5.327']
# Experiment results: async=True, chunks/write=2, writes/round=64, rounds=2, parallel_lz4=False, async_arctic_pool_workers=8: ['5.410', '0.000', '5.410', '5.410']
