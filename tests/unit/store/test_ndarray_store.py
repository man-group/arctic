import numpy as np
from pytest import raises
from arctic.store._ndarray_store import NdarrayStore, _promote_struct_dtypes


def test_dtype_parsing():
    store = NdarrayStore()
    dtypes = []

    dtypes.append(np.dtype(np.object_))
    dtypes.append(np.dtype(np.float128))
    dtypes.append(np.dtype('int64'))
    dtypes.append(np.dtype([('A', 'int64')]))
    dtypes.append(np.dtype([('A', 'int64'), ('B', '<f8')]))
    dtypes.append(np.dtype([('A', 'int64'), ('B', '<f8', (2,))]))

    for d in dtypes:
        assert d == store._dtype(str(d), None)


def test_promote_dtype_handles_string_increase():
    dtype1 = np.dtype([('A', 'i4'), ('B', 'f4'), ('C', 'a10')])
    dtype2 = np.dtype([('A', 'i4'), ('B', 'f4'), ('C', 'a20')])
    expected = np.dtype([('A', 'i4'), ('B', 'f4'), ('C', 'a20')])

    actual = _promote_struct_dtypes(dtype1, dtype2)

    assert expected == actual


def test_promote_dtype_handles_string_decrease():
    dtype1 = np.dtype([('A', 'i4'), ('B', 'f4'), ('C', 'a20')])
    dtype2 = np.dtype([('A', 'i4'), ('B', 'f4'), ('C', 'a10')])
    expected = np.dtype([('A', 'i4'), ('B', 'f4'), ('C', 'a20')])

    actual = _promote_struct_dtypes(dtype1, dtype2)

    assert expected == actual


def test_promote_dtype_handles_new_column():
    dtype1 = np.dtype([('A', 'i4'), ('B', 'f4'), ('C', 'a10')])
    dtype2 = np.dtype([('A', 'i4'), ('B', 'f4')])
    expected = np.dtype([('A', 'i4'), ('B', 'f4'), ('C', 'a10')])

    actual = _promote_struct_dtypes(dtype1, dtype2)

    assert expected == actual


def test_promote_dtype_handles_rearrangement_of_columns_favouring_dtype1():
    dtype1 = np.dtype([('A', 'i4'), ('B', 'f4'), ('C', 'a10')])
    dtype2 = np.dtype([('A', 'i4'), ('C', 'a10'), ('B', 'f4')])
    expected = np.dtype([('A', 'i4'), ('B', 'f4'), ('C', 'a10')])

    actual = _promote_struct_dtypes(dtype1, dtype2)

    assert expected == actual


def test_promote_dtype_throws_if_column_is_removed():
    dtype1 = np.dtype([('A', 'i4'), ('B', 'f4')])
    dtype2 = np.dtype([('A', 'i4'), ('C', 'a10'), ('B', 'f4')])

    with raises(Exception):
        _promote_struct_dtypes(dtype1, dtype2)
