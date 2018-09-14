from six.moves import xrange

import arctic
from arctic.async import ASYNC_ARCTIC, async_arctic_submit, async_join_request
from tests.integration.chunkstore.test_chunkstore import create_test_data

ASYNC_ARCTIC.reset(block=True, pool_size=8)

a = arctic.Arctic('localhost:37917')
library_name = 'dimos.test'

data_to_write = create_test_data(size=1000000, index=True, multiindex=False, random_data=True, random_ids=True,
                                 date_offset=0, cols=10)


def clean_lib():
    a.delete_library(library_name)
    a.initialize_library(library_name)


def async_bench(num_requests):
    lib = a[library_name]
    reqs = [async_arctic_submit(lib, lib.write, False, symbol='sym' + str(x), data=data_to_write) for x in xrange(num_requests)]
    [async_join_request(r) for r in reqs]


def serial_bench(num_requests):
    lib = a[library_name]
    for x in xrange(num_requests):
        lib.write(symbol='sym' + str(x), data=data_to_write)


def main():
    import time
    clean_lib()
    rounds = 5

    start = time.time()
    for _ in xrange(rounds):
        async_bench(16)  # 1 loop, best of 5: 6.54 s per loop
    print("Async time per iteration: {}".format((time.time() - start) / rounds))

    clean_lib()

    start = time.time()
    for _ in xrange(rounds):
        serial_bench(16)  # 1 loop, best of 5: 14.2 s per loop
    print("Serial time per iteration: {}".format((time.time() - start) / rounds))


if __name__ == '__main__':
    main()

# Async time per iteration: 10.8640662193
# Serial time per iteration: 24.5076581955