from six.moves import xrange

import arctic
from tests.integration.chunkstore.test_utils import create_test_data


#----------------------------------------------
#  Configure the benchmark
#----------------------------------------------
from arctic.async import ASYNC_ARCTIC, INTERNAL_ASYNC, async_arctic_submit, async_wait_request
from arctic._compression import enable_parallel_lz4, set_use_async_pool
import arctic.store._pandas_ndarray_store as pnds
import arctic.store._ndarray_store as nds
import arctic.async.async_utils as asu
ASYNC_ARCTIC.reset(block=True, pool_size=4)
INTERNAL_ASYNC.reset(block=True, pool_size=4)
enable_parallel_lz4(True)
set_use_async_pool(True)
pnds.USE_INCREMENTAL_SERIALIZER = True
nds.MONGO_BATCH_SIZE = 8
nds.MONGO_CONCURRENT_BATCHES = 2
asu.USE_ASYNC_MONGO_WRITES = True
#----------------------------------------------


a = arctic.Arctic('jenkins-2el7b-9.cn.ada.res.ahl:37917')
# a = arctic.Arctic('localhost:27116')
library_name = 'asyncbench.test'

data_to_write = create_test_data(size=500000, index=True, multiindex=False, random_data=True, random_ids=True,
                                 use_hours=True, date_offset=0, cols=10)


def clean_lib():
    a.delete_library(library_name)
    a.initialize_library(library_name)


def async_bench(num_requests):
    lib = a[library_name]
    reqs = [async_arctic_submit(lib, lib.write, False, symbol='sym_{}'.format(x), data=data_to_write) for x in xrange(num_requests)]
    [async_wait_request(r) for r in reqs]


def serial_bench(num_requests):
    lib = a[library_name]
    for x in xrange(num_requests):
        lib.write(symbol='sym_{}'.format(x), data=data_to_write)


def main():
    import time
    rounds = 5
    num_requests = 1

    # clean_lib()
    #
    # enable_parallel_lz4(True)
    # set_use_async_pool(False)
    # pnds.USE_INCREMENTAL_SERIALIZER = False
    # start = time.time()
    # for _ in xrange(rounds):
    #     serial_bench(num_requests)  # 1 loop, best of 5: 14.2 s per loop
    # print("Serial time per iteration: {}".format((time.time() - start) / rounds))
    #
    # clean_lib()
    #
    # enable_parallel_lz4(True)
    # set_use_async_pool(False)
    # pnds.USE_INCREMENTAL_SERIALIZER = False
    # # nds.MONGO_BATCH_SIZE = 8
    # # nds.MONGO_CONCURRENT_BATCHES = 2
    # # asu.USE_ASYNC_MONGO_WRITES = True
    # start = time.time()
    # for _ in xrange(rounds):
    #     async_bench(num_requests)  # 1 loop, best of 5: 6.54 s per loop
    # print("Async time per iteration: {}".format((time.time() - start) / rounds))
    #
    clean_lib()

    enable_parallel_lz4(True)
    set_use_async_pool(True)
    pnds.USE_INCREMENTAL_SERIALIZER = False
    start = time.time()
    for _ in xrange(rounds):
        async_bench(num_requests)  # 1 loop, best of 5: 6.54 s per loop
    print("Async time per iteration: {}".format((time.time() - start) / rounds))

    clean_lib()

    enable_parallel_lz4(True)
    set_use_async_pool(True)
    pnds.USE_INCREMENTAL_SERIALIZER = True
    nds.MONGO_BATCH_SIZE = 8
    nds.MONGO_CONCURRENT_BATCHES = 2
    asu.USE_ASYNC_MONGO_WRITES = False
    start = time.time()
    for _ in xrange(rounds):
        async_bench(num_requests)  # 1 loop, best of 5: 6.54 s per loop
    print("Async time per iteration: {}".format((time.time() - start) / rounds))

    clean_lib()

    enable_parallel_lz4(True)
    set_use_async_pool(True)
    pnds.USE_INCREMENTAL_SERIALIZER = True
    nds.MONGO_BATCH_SIZE = 8
    nds.MONGO_CONCURRENT_BATCHES = 2
    asu.USE_ASYNC_MONGO_WRITES = True
    start = time.time()
    for _ in xrange(rounds):
        async_bench(num_requests)  # 1 loop, best of 5: 6.54 s per loop
    print("Async time per iteration: {}".format((time.time() - start) / rounds))

    # clean_lib()
    #
    # enable_parallel_lz4(True)
    # set_use_async_pool(False)
    # pnds.USE_INCREMENTAL_SERIALIZER = True
    # start = time.time()
    # for _ in xrange(rounds):
    #     async_bench(num_requests)  # 1 loop, best of 5: 6.54 s per loop
    # print("Async time per iteration: {}".format((time.time() - start) / rounds))




if __name__ == '__main__':
    main()

# Async time per iteration: 10.8640662193
# Serial time per iteration: 24.5076581955
