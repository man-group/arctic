from __future__ import print_function
import random
import lz4
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
    [lz4.decompress(y) for y in [lz4.compressHC(x) for x in _strarr]]
    lz4_time = (dt.now() - now).total_seconds()
    print()
    print("LZ4 Test %sx len:%s" % (n, length))
    print("    Cython LZ4 %s s" % clz4_time)
    print("    Cython LZ4 Parallel %s s" % clz4_time_p)
    print("    LZ4 %s s" % lz4_time)


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
