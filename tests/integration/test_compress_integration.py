from __future__ import print_function
import random
try:
    from lz4 import compress as lz4_compress, compressHC as lz4_compressHC, decompress as lz4_decompress
except ImportError as e:
    from lz4.frame import compress as lz4_compress, decompress as lz4_decompress

import string
import pytest
import six
from datetime import datetime as dt

import arctic._compress as c


@pytest.mark.parametrize("n, length", [(300, 5e4),  # micro TS
                                       (5, 2e6),  # Futures TS
                                       (10, 2e6),  # Futures TS
                                       (100, 2e6),  # Large TS
                                       (250, 2e6)])  # Even Bigger TS
def test_performance_sequential(n, length):
    _str = random_string(length)
    _strarr = [_str for _ in range(n)]
    now = dt.now()
    [c.decompress(y) for y in [c.compressHC(x) for x in _strarr]]
    clz4_time = (dt.now() - now).total_seconds()
    now = dt.now()
    c.decompressarr(c.compressarrHC(_strarr))
    clz4_time_p = (dt.now() - now).total_seconds()
    now = dt.now()
    [lz4_decompress(y) for y in [lz4_compressHC(x) for x in _strarr]]
    lz4_time = (dt.now() - now).total_seconds()
    print()
    print("LZ4 Test %sx len:%s" % (n, length))
    print("    Cython LZ4 %s s" % clz4_time)
    print("    Cython LZ4 Parallel %s s" % clz4_time_p)
    print("    LZ4 %s s" % lz4_time)


@pytest.mark.parametrize("n, length", [(300, 5e4),  # micro TS
                                       (16, 2e6)])  # Futures TS
def test_bench_compression_comparison(n, length):
    _str = random_string(length)
    _strarr = [_str for _ in range(n)]

    now = dt.now()
    [c.compress(x) for x in _strarr]
    arctic_old_lz4_time = (dt.now() - now).total_seconds()

    now = dt.now()
    c.compressarr(_strarr)
    arctic_old_lz4Arr_time = (dt.now() - now).total_seconds()

    now = dt.now()
    [c.compressHC(x) for x in _strarr]
    arctic_old_lz4HC_time = (dt.now() - now).total_seconds()

    now = dt.now()
    c.compressarrHC(_strarr)
    arctic_old_lz4HCArr_time = (dt.now() - now).total_seconds()

    now = dt.now()
    [lz4_compress(x) for x in _strarr]
    lz4_frame_time = (dt.now() - now).total_seconds()

    now = dt.now()
    [c.compressFrame(x) for x in _strarr]
    arctic_lz4Frame_time = (dt.now() - now).total_seconds()

    now = dt.now()
    c.compressarrFrame(_strarr)
    arctic_lz4ArrFrame_time = (dt.now() - now).total_seconds()

    print()
    print("LZ4 Test %sx len:%s" % (n, length))
    print("    Arctic Cython old LZ4 (single thread) %s s" % arctic_old_lz4_time)
    print("    Arctic Cython old LZ4 (parallel) %s s" % arctic_old_lz4Arr_time)
    print("    Arctic Cython old LZ4 High Compression (single thread) %s s" % arctic_old_lz4HC_time)
    print("    Arctic Cython old LZ4 High Compression (parallel)%s s" % arctic_old_lz4HCArr_time)
    print("    New LZ4 (frame) %s s" % lz4_frame_time)
    print("    Arctic Cython new LZ4 Frame (single thread) %s s" % arctic_lz4Frame_time)
    print("    Arctic Cython new LZ4 Frame (parallel) %s s" % arctic_lz4ArrFrame_time)


@pytest.mark.parametrize("n, length", [(10, 5e2),
                                       (10, 5e3),
                                       (10, 5e4)])
def test_lz4frame_compression(n, length):
    for test_str in (random_string(length) for _ in range(n)):
        compressed = c.compressFrame(test_str)
        assert lz4_decompress(compressed) == test_str


@pytest.mark.parametrize("n, length", [(10, 5e2),
                                       (10, 5e3),
                                       (10, 5e4)])
def test_lz4frame_parallel_compression(n, length):
    arr_of_str = [random_string(length) for _ in range(n)]
    compressed_arr = c.compressarrFrame(arr_of_str)
    for i in range(n):
        assert lz4_decompress(compressed_arr[i]) == arr_of_str[i]


def test_compatibility():
    test_str = random_string(100)

    # This fails (Exception: Error decompressing)
    # assert c.decompress(c.compressFrame(test_str)) == test_str

    # This fails with python lz4 0.7.0 (corrupt input)
    # This is passing with lz4 1.1.0
    # assert lz4_decompress(c.compressFrame(test_str)) == test_str

    # This passes with python lz4 0.7.0
    # This fails with python lz4 1.1.0 (Exception: Error decompressing)
    # assert c.decompress(lz4_compress(test_str)) == test_str

    # This passes with python lz4 0.7.0
    # This fails with python lz4 1.1.0 (ERROR_frameType_unknown)
    # assert lz4_decompress(c.compress(test_str)) == test_str



def random_string(N):
    _str = ''.join(random.choice(list(string.printable) + ['hello', 'world', 'hellworld', 'Hello', 'w0rld']) for _ in six.moves.xrange(int(N)))
    return _str.encode('ascii')


def test_exceptions():
    data = c.compress(b'1010101010100000000000000000000000000000000000000000000000000000000011111111111111111111111111111')
    data = data[0:16]
    with pytest.raises(Exception) as e:
        c.decompress(data)
    assert("decompressing" in str(e))

    data = c.compress(b'1010101010100000000000000000000000000000000000000000000000000000000011111111111111111111111111111')
    data = [data[0:16] for x in (1, 2, 3)]
    with pytest.raises(Exception) as e:
        c.decompressarr(data)
    assert("decompressing" in str(e))

@pytest.mark.parametrize("n, length", [(300, 5e4),  # micro TS
                                       (16, 2e6)])  # Futures TS
def test_bench_compression_comparison(n, length):
    _str = random_string(length)
    _strarr = [_str for _ in range(n)]

    now = dt.now()
    [c.compress(x) for x in _strarr]
    arctic_old_lz4_time = (dt.now() - now).total_seconds()

    now = dt.now()
    c.compressarr(_strarr)
    arctic_old_lz4Arr_time = (dt.now() - now).total_seconds()

    now = dt.now()
    [c.compressHC(x) for x in _strarr]
    arctic_old_lz4HC_time = (dt.now() - now).total_seconds()

    now = dt.now()
    c.compressarrHC(_strarr)
    arctic_old_lz4HCArr_time = (dt.now() - now).total_seconds()

    now = dt.now()
    [lz4_compress(x) for x in _strarr]
    lz4_frame_time = (dt.now() - now).total_seconds()

    # now = dt.now()
    # [c.compressFrame(x) for x in _strarr]
    # arctic_lz4Frame_time = (dt.now() - now).total_seconds()
    #
    # now = dt.now()
    # c.compressarrFrame(_strarr)
    # arctic_lz4ArrFrame_time = (dt.now() - now).total_seconds()

    print()
    print("LZ4 Test %sx len:%s" % (n, length))
    print("    Arctic Cython old LZ4 (single thread) %s s" % arctic_old_lz4_time)
    print("    Arctic Cython old LZ4 (parallel) %s s" % arctic_old_lz4Arr_time)
    print("    Arctic Cython old LZ4 High Compression (single thread) %s s" % arctic_old_lz4HC_time)
    print("    Arctic Cython old LZ4 High Compression (parallel)%s s" % arctic_old_lz4HCArr_time)
    print("    New LZ4 (frame) %s s" % lz4_frame_time)
    # print("    Arctic Cython new LZ4 Frame (single thread) %s s" % arctic_lz4Frame_time)
    # print("    Arctic Cython new LZ4 Frame (parallel) %s s" % arctic_lz4ArrFrame_time)


@pytest.mark.parametrize("n, length", [(300, 5e4),  # micro TS
                                       (16, 2e6)])  # Futures TS
def test_bench_decompression_comparison(n, length):
    _str = random_string(length)
    _strarr = [_str for _ in range(n)]

    compressed = [c.compress(x) for x in _strarr]

    now = dt.now()
    [c.decompress(x) for x in compressed]
    arctic_old_lz4_time = (dt.now() - now).total_seconds()

    now = dt.now()
    c.decompressarr(compressed)
    arctic_old_lz4Arr_time = (dt.now() - now).total_seconds()

    compressed = [lz4_compress(x) for x in _strarr]

    now = dt.now()
    [lz4_decompress(x) for x in compressed]
    lz4_frame_time = (dt.now() - now).total_seconds()

    # now = dt.now()
    # [c.compressFrame(x) for x in _strarr]
    # arctic_lz4Frame_time = (dt.now() - now).total_seconds()
    #
    # now = dt.now()
    # c.compressarrFrame(_strarr)
    # arctic_lz4ArrFrame_time = (dt.now() - now).total_seconds()

    print()
    print("LZ4 Test %sx len:%s" % (n, length))
    print("    Decompress Arctic Cython old LZ4 (single thread) %s s" % arctic_old_lz4_time)
    print("    Decompress Arctic Cython old LZ4 (parallel) %s s" % arctic_old_lz4Arr_time)
    print("    Decompress New LZ4 (frame) %s s" % lz4_frame_time)


@pytest.mark.parametrize("n, length", [(300, 5e4),  # micro TS
                                       (16, 2e6)])  # Futures TS
def test_bench_decompressionHC_comparison(n, length):
    _str = random_string(length)
    _strarr = [_str for _ in range(n)]

    compressed = [c.compressHC(x) for x in _strarr]

    now = dt.now()
    [c.decompress(x) for x in compressed]
    arctic_old_lz4_time = (dt.now() - now).total_seconds()

    now = dt.now()
    c.decompressarr(compressed)
    arctic_old_lz4Arr_time = (dt.now() - now).total_seconds()

    compressed = [lz4_compress(x) for x in _strarr]

    now = dt.now()
    [lz4_decompress(x) for x in compressed]
    lz4_frame_time = (dt.now() - now).total_seconds()

    # now = dt.now()
    # [c.compressFrame(x) for x in _strarr]
    # arctic_lz4Frame_time = (dt.now() - now).total_seconds()
    #
    # now = dt.now()
    # c.compressarrFrame(_strarr)
    # arctic_lz4ArrFrame_time = (dt.now() - now).total_seconds()

    print()
    print("LZ4 Test %sx len:%s" % (n, length))
    print("    Decompress HC Arctic Cython old LZ4 (single thread) %s s" % arctic_old_lz4_time)
    print("    Decompress HC Arctic Cython old LZ4 (parallel) %s s" % arctic_old_lz4Arr_time)
    print("    Decompress HC New LZ4 (frame) %s s" % lz4_frame_time)
