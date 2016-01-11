import pytest
import numpy as np
import binascii

from arctic.store._version_store_utils import _split_arrs, checksum


def test_split_arrs_empty():
    split = _split_arrs(np.empty(0), [])
    assert np.all(split == np.empty(0, dtype=np.object))


def test_split_arrs():
    to_split = np.ones(10)
    split = _split_arrs(to_split, [3])
    assert len(split) == 2
    assert np.all(split[0] == np.ones(3))
    assert np.all(split[1] == np.ones(7))


def test_checksum():
    digest = checksum('test_my_market_data_$ymB0l', {})
    expected = b"""4OZ*3DO'$>XV['VW1MT4I^+7-3H,"""
    assert binascii.b2a_uu(digest).strip() == expected


def test_checksum_handles_p3strs_and_binary():
    digest = checksum('test_my_market_data_$ymB0l', {'key1': u'unicode',
                                                     'key2': b'binary_data'})
    expected = b'4O11 ;<A@C1.0W(JRB1.?D[ZEN!8'
    assert binascii.b2a_uu(digest).strip() == expected

