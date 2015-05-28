import lz4
import pytest
import random
import string

import arctic._compress as c


def test_roundtrip():
    _str = "hello world"
    cstr = c.compress(_str)
    assert _str == c.decompress(cstr)


@pytest.mark.parametrize("n", [1, 1e2, 1e3, 1e6])
def test_roundtrip_multi(n):
    _str = random_string(n)
    cstr = c.compress(_str)
    assert _str == c.decompress(cstr)


def test_roundtripHC():
    _str = "hello world"
    cstr = c.compressHC(_str)
    assert _str == c.decompress(cstr)


def test_roundtripLZ4():
    _str = "hello world"
    cstr = lz4.compress(_str)
    assert _str == c.decompress(cstr)


def test_roundtripLZ4Back():
    _str = "hello world"
    cstr = c.compress(_str)
    assert _str == lz4.decompress(cstr)


def test_roundtripLZ4HC():
    _str = "hello world"
    cstr = lz4.compressHC(_str)
    assert _str == c.decompress(cstr)


def test_roundtripLZ4HCBack():
    _str = "hello world"
    cstr = c.compressHC(_str)
    assert _str == lz4.decompress(cstr)


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
    return ''.join(random.choice(string.printable) for _ in range(int(N)))
