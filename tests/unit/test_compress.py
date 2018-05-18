import pytest
import random
import string

import arctic._compress as c


@pytest.mark.parametrize("compress",
                         [c.compress, c.compressHC],
                         ids=('arctic', 'arcticHC'))
def test_roundtrip(compress):
    _str = b"hello world"
    cstr = compress(_str)
    assert _str == c.decompress(cstr)


@pytest.mark.parametrize("n", [1, 1e2, 1e3, 1e6])
def test_roundtrip_multi(n):
    _str = random_string(n)
    cstr = c.compress(_str)
    assert _str == c.decompress(cstr)



@pytest.mark.parametrize("n, length", [(1, 10), (100, 10), (1000, 10)])
def test_roundtrip_arr(n, length):
    _strarr = [random_string(length) for _ in range(n)]
    cstr = c.compressarr(_strarr)
    assert _strarr == c.decompressarr(cstr)


@pytest.mark.parametrize("n, length", [(1, 10), (100, 10), (1000, 10)])
def test_roundtrip_arrHC(n, length):
    _strarr = [random_string(length) for _ in range(n)]
    cstr = c.compressarrHC(_strarr)
    assert _strarr == c.decompressarr(cstr)


def test_arr_zero():
    assert [] == c.compressarrHC([])
    assert [] == c.decompressarr([])


def random_string(N):
    _str = ''.join(random.choice(string.printable) for _ in range(int(N)))
    return _str.encode('ascii')
