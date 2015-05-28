import pytest
import numpy as np

from arctic.store._version_store_utils import _split_arrs


def test_split_arrs_empty():
    split = _split_arrs(np.empty(0), [])
    assert np.all(split == np.empty(0, dtype=np.object))


def test_split_arrs():
    to_split = np.ones(10)
    split = _split_arrs(to_split, [3])
    assert len(split) == 2
    assert np.all(split[0] == np.ones(3))
    assert np.all(split[1] == np.ones(7))
