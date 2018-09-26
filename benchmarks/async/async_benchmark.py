import time
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

num_chunks = 32
data_to_write = create_test_data(size=25000, index=True, multiindex=False, random_data=True, random_ids=True,
                                 use_hours=True, date_offset=0, cols=10)
data_to_write = data_to_write.append([data_to_write] * (num_chunks - 1))


def clean_lib():
    a.delete_library(library_name)
    a.initialize_library(library_name)


def async_bench(num_requests):
    lib = a[library_name]
    reqs = [async_arctic_submit(lib, lib.write, False, symbol='sym_{}'.format(x), data=data_to_write) for x in xrange(num_requests)]
    [async_wait_request(r) for r in reqs]

    # request = async_arctic_submit(
    #     store=mylib,
    #     fun=mylib.write,
    #     is_modifier=True,
    #     async_callback=my_callback,
    #     # async_block=False,
    # )
    #
    # async_wait_request(request)
    #
    # request.



def serial_bench(num_requests):
    lib = a[library_name]
    for x in xrange(num_requests):
        lib.write(symbol='sym_{}'.format(x), data=data_to_write)



def run_sceanrio(result_text, rounds, num_requests, use_async,
                 parallel_lz4, lz4_use_async_pool,
                 use_incremental_serializer, mongo_batch_size=None,
                 mongo_use_async_writes=None, mongo_num_batches=None,
                 async_pool_size=None, internal_async_pool_size=None):
    clean_lib()
    enable_parallel_lz4(parallel_lz4)
    set_use_async_pool(lz4_use_async_pool)
    pnds.USE_INCREMENTAL_SERIALIZER = use_incremental_serializer
    if mongo_batch_size is not None:
        nds.MONGO_BATCH_SIZE = int(mongo_batch_size)
    if mongo_use_async_writes is not None:
        asu.USE_ASYNC_MONGO_WRITES = bool(mongo_use_async_writes)
    if mongo_num_batches is not None:
        nds.MONGO_CONCURRENT_BATCHES = int(mongo_num_batches)
    if async_pool_size is not None:
        ASYNC_ARCTIC.reset(block=True, pool_size=int(async_pool_size))
    if internal_async_pool_size is not None:
        INTERNAL_ASYNC.reset(block=True, pool_size=int(internal_async_pool_size))
    start = time.time()
    for _ in xrange(rounds):
        if use_async:
            async_bench(num_requests)
        else:
            serial_bench(num_requests)
    print("{}: {}".format(result_text, (time.time() - start) / rounds))


def main():
    rounds = 5
    num_requests = 1

    print("Experimenting with {} chunks per write".format(num_chunks))

    run_sceanrio(result_text="Serial time per iteration", use_async=False, rounds=rounds, num_requests=num_requests,
                 parallel_lz4=True, lz4_use_async_pool=False,
                 use_incremental_serializer=False,
                 mongo_use_async_writes=False)

    # run_sceanrio(result_text="Async time per iteration", use_async=True, rounds=rounds, num_requests=num_requests,
    #              parallel_lz4=True, lz4_use_async_pool=True,
    #              use_incremental_serializer=True, mongo_batch_size=8,
    #              mongo_use_async_writes=True, mongo_num_batches=2,
    #              async_pool_size=4, internal_async_pool_size=4)

    # run_sceanrio(result_text="Serial time per iteration (incremental serializer)", rounds=rounds, num_requests=num_requests,
    #              parallel_lz4=True, lz4_use_async_pool=False,
    #              use_incremental_serializer=True, mongo_batch_size=8,
    #              mongo_use_async_writes=False)
    #
    # run_sceanrio(result_text="Serial/internal-async time per iteration (incremental serializer, batch=8)", rounds=rounds, num_requests=num_requests,
    #              parallel_lz4=True, lz4_use_async_pool=False,
    #              use_incremental_serializer=True, mongo_batch_size=8,
    #              mongo_use_async_writes=True, mongo_num_batches=2)
    #
    # run_sceanrio(result_text="Serial/internal-async time per iteration (incremental serializer, common internal async pool, batch=8)", rounds=rounds,
    #              num_requests=num_requests,
    #              parallel_lz4=True, lz4_use_async_pool=True,
    #              use_incremental_serializer=True, mongo_batch_size=8,
    #              mongo_use_async_writes=True, mongo_num_batches=2)
    #
    # run_sceanrio(result_text="Serial/internal-async time per iteration (incremental serializer, common internal async pool, batch=16)",
    #              rounds=rounds,
    #              num_requests=num_requests,
    #              parallel_lz4=True, lz4_use_async_pool=True,
    #              use_incremental_serializer=True, mongo_batch_size=16,
    #              mongo_use_async_writes=True, mongo_num_batches=2)
    #
    # run_sceanrio(result_text="Serial/internal-async time per iteration (incremental serializer, common internal async pool, batch=16, num_batches=4)",
    #              rounds=rounds,
    #              num_requests=num_requests,
    #              parallel_lz4=True, lz4_use_async_pool=True,
    #              use_incremental_serializer=True, mongo_batch_size=16,
    #              mongo_use_async_writes=True, mongo_num_batches=4)


    # clean_lib()
    # enable_parallel_lz4(True)
    # set_use_async_pool(False)
    # pnds.USE_INCREMENTAL_SERIALIZER = False
    # start = time.time()
    # for _ in xrange(rounds):
    #     serial_bench(num_requests)
    # print("Serial time per iteration: {}".format((time.time() - start) / rounds))
    #
    # clean_lib()
    # enable_parallel_lz4(True)
    # set_use_async_pool(False)
    # pnds.USE_INCREMENTAL_SERIALIZER = True
    # nds.MONGO_BATCH_SIZE = 8
    # asu.USE_ASYNC_MONGO_WRITES = False
    # start = time.time()
    # for _ in xrange(rounds):
    #     serial_bench(num_requests)
    # print("Serial time per iteration (incremental serializer): {}".format((time.time() - start) / rounds))
    #
    # clean_lib()
    # enable_parallel_lz4(True)
    # set_use_async_pool(False)
    # pnds.USE_INCREMENTAL_SERIALIZER = True
    # nds.MONGO_BATCH_SIZE = 8
    # asu.USE_ASYNC_MONGO_WRITES = True
    # start = time.time()
    # for _ in xrange(rounds):
    #     serial_bench(num_requests)
    # print("Serial/internal-async time per iteration (incremental serializer): {}".format((time.time() - start) / rounds))
    #
    # clean_lib()
    # enable_parallel_lz4(True)
    # set_use_async_pool(True)
    # pnds.USE_INCREMENTAL_SERIALIZER = True
    # nds.MONGO_BATCH_SIZE = 8
    # asu.USE_ASYNC_MONGO_WRITES = True
    # nds.MONGO_CONCURRENT_BATCHES = 2
    # start = time.time()
    # for _ in xrange(rounds):
    #     serial_bench(num_requests)
    # print("Serial/internal-async time per iteration (incremental serializer, common internal async pool, batch=8): {}".format((time.time() - start) / rounds))
    #
    # clean_lib()
    # enable_parallel_lz4(True)
    # set_use_async_pool(True)
    # pnds.USE_INCREMENTAL_SERIALIZER = True
    # nds.MONGO_BATCH_SIZE = 16
    # asu.USE_ASYNC_MONGO_WRITES = True
    # nds.MONGO_CONCURRENT_BATCHES = 2
    # start = time.time()
    # for _ in xrange(rounds):
    #     serial_bench(num_requests)
    # print("Serial/internal-async time per iteration (incremental serializer, common internal async pool, batch=16): {}".format(
    #     (time.time() - start) / rounds))
    #
    # clean_lib()
    # enable_parallel_lz4(True)
    # set_use_async_pool(True)
    # pnds.USE_INCREMENTAL_SERIALIZER = True
    # nds.MONGO_BATCH_SIZE = 16
    # asu.USE_ASYNC_MONGO_WRITES = True
    # nds.MONGO_CONCURRENT_BATCHES = 4
    # start = time.time()
    # for _ in xrange(rounds):
    #     serial_bench(num_requests)
    # print(
    # "Serial/internal-async time per iteration (incremental serializer, common internal async pool, batch=16, num_batches=4): {}".format(
    #     (time.time() - start) / rounds))

    clean_lib()

    enable_parallel_lz4(True)
    set_use_async_pool(False)
    pnds.USE_INCREMENTAL_SERIALIZER = False
    nds.MONGO_BATCH_SIZE = 8
    nds.MONGO_CONCURRENT_BATCHES = 2
    asu.USE_ASYNC_MONGO_WRITES = True
    start = time.time()
    for _ in xrange(rounds):
        async_bench(num_requests)  # 1 loop, best of 5: 6.54 s per loop
    print("Async time per iteration: {}".format((time.time() - start) / rounds))
    #
    # clean_lib()
    #
    # enable_parallel_lz4(True)
    # set_use_async_pool(True)
    # pnds.USE_INCREMENTAL_SERIALIZER = False
    # start = time.time()
    # for _ in xrange(rounds):
    #     async_bench(num_requests)  # 1 loop, best of 5: 6.54 s per loop
    # print("Async time per iteration: {}".format((time.time() - start) / rounds))
    #
    # clean_lib()
    #
    # enable_parallel_lz4(True)
    # set_use_async_pool(True)
    # pnds.USE_INCREMENTAL_SERIALIZER = True
    # nds.MONGO_BATCH_SIZE = 8
    # nds.MONGO_CONCURRENT_BATCHES = 2
    # asu.USE_ASYNC_MONGO_WRITES = False
    # start = time.time()
    # for _ in xrange(rounds):
    #     async_bench(num_requests)  # 1 loop, best of 5: 6.54 s per loop
    # print("Async time per iteration: {}".format((time.time() - start) / rounds))
    #
    # clean_lib()
    #
    # enable_parallel_lz4(True)
    # set_use_async_pool(False)
    # pnds.USE_INCREMENTAL_SERIALIZER = True
    # nds.MONGO_BATCH_SIZE = 8
    # nds.MONGO_CONCURRENT_BATCHES = 1
    # asu.USE_ASYNC_MONGO_WRITES = True
    # start = time.time()
    # for _ in xrange(rounds):
    #     async_bench(num_requests)  # 1 loop, best of 5: 6.54 s per loop
    # print("Async time per iteration: {}".format((time.time() - start) / rounds))

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
