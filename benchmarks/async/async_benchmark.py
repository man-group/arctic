import time
from six.moves import xrange

import arctic
from tests.integration.chunkstore.test_utils import create_test_data

#----------------------------------------------
#  Configure hooks for the benchmark
#----------------------------------------------
import arctic._compression as aclz4
import arctic.store._pandas_ndarray_store as pnds
import arctic.store._ndarray_store as nds
# from arctic.async import ASYNC_ARCTIC, async_arctic_submit, async_wait_request, async_join_all
#----------------------------------------------


# a = arctic.Arctic('jenkins-2el7b-9.cn.ada.res.ahl:37917')
# a = arctic.Arctic('dpediaditakis.hn.ada.res.ahl:27117')
a = arctic.Arctic('dpediaditakis.hn.ada.res.ahl:27217')
# a = arctic.Arctic('dlonapahls229:37917')
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
    pass
    # Trigger lazy init
    # data = get_cached_random_df(num_chunks)
    # lib = a[library_name]
    # reqs = [async_arctic_submit(lib, lib.write, False, symbol='sym_{}'.format(x), data=data) for x in xrange(num_requests)]
    # async_join_all()


def serial_bench(num_requests, num_chunks):
    # Trigger lazy init
    data = get_cached_random_df(num_chunks)
    lib = a[library_name]
    for x in xrange(num_requests):
        lib.write(symbol='sym_{}'.format(x), data=data)


def run_scenario(result_text,
                 rounds, num_requests, num_chunks,
                 use_async,
                 parallel_lz4, parallel_lz4_nthreads, lz4_use_async_pool, min_n_parallel,
                 use_incremental_serializer,
                 mongo_use_async_writes=None, mongo_batch_size=None, mongo_num_batches=None,
                 async_pool_size=None, internal_async_pool_size=None):
    aclz4.enable_parallel_lz4(parallel_lz4)
    aclz4.set_use_async_pool(lz4_use_async_pool)
    aclz4.LZ4_MIN_N_PARALLEL = int(min_n_parallel)
    aclz4.set_compression_pool_size(int(parallel_lz4_nthreads))
    pnds.USE_INCREMENTAL_SERIALIZER = use_incremental_serializer
    if mongo_batch_size is not None:
        nds.MONGO_BATCH_SIZE = int(mongo_batch_size)
    if mongo_use_async_writes is not None:
        nds.USE_ASYNC_MONGO_WRITES = bool(mongo_use_async_writes)
    if mongo_num_batches is not None:
        nds.MONGO_CONCURRENT_BATCHES = int(mongo_num_batches)
    if async_pool_size is not None:
        ASYNC_ARCTIC.reset(block=True, pool_size=int(async_pool_size))
    if internal_async_pool_size is not None:
        pass
        # INTERNAL_ASYNC.reset(block=True, pool_size=int(internal_async_pool_size))
    measurements = []
    for round in xrange(rounds):
        # print("Running round {}".format(round))
        clean_lib()
        start = time.time()
        if use_async:
            async_bench(num_requests, num_chunks)
        else:
            serial_bench(num_requests, num_chunks)
        measurements.append(time.time() - start)
    print("{}: "
          "async={}, chunks/write={}, writes/round={}, rounds={}, "
          "parallel_lz4={}, lz4_async_pool={}, "
          "incremental={}, "
          "mongo_async={}, mongo_batch={}, mongo_batches={}, "
          "pool_size={}, internal_pool_size={}: {}".format(
        result_text,
        use_async, num_chunks, num_requests, rounds,
        parallel_lz4, lz4_use_async_pool,
        use_incremental_serializer,
        mongo_use_async_writes, mongo_batch_size, mongo_num_batches,
        async_pool_size, internal_async_pool_size,
        ["{:.3f}".format(x) for x in get_stats(measurements[1:] if len(measurements) > 1 else measurements)]))



def main():
    n_use_async = (False,)

    n_rounds = (1,)
    n_num_requests = (1,)
    n_num_chunks = (128,)

    n_parallel_lz4 = (False,)
    n_parallel_lz4_nthreads = (1,)

    n_use_incremental_serializer = (True,)
    n_mongo_batch_size = (4,)
    n_internal_serializer_pool_threads = (2,)
    n_internal_mongo_pool_threads = (6,)

    for use_async in n_use_async:
        for use_incremental_serializer in n_use_incremental_serializer:
            for parallel_lz4 in n_parallel_lz4:
                for parallel_lz4_nthreads in n_parallel_lz4_nthreads:
                    for num_chunks in n_num_chunks:
                        for num_requests in n_num_requests:
                            for mongo_batch_size in (n_mongo_batch_size if use_incremental_serializer else (4,)):
                                for rounds in n_rounds:
                                    run_scenario(result_text="Experiment results",
                                                 use_async=use_async,
                                                 rounds=rounds, num_requests=num_requests,
                                                 num_chunks=num_chunks,
                                                 parallel_lz4=parallel_lz4,
                                                 parallel_lz4_nthreads=parallel_lz4_nthreads,
                                                 min_n_parallel=mongo_batch_size,
                                                 use_incremental_serializer=use_incremental_serializer,
                                                 mongo_batch_size=mongo_batch_size
                                                 )


if __name__ == '__main__':
    main()
