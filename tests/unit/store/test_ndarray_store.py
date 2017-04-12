from mock import create_autospec, sentinel
import numpy as np
from pymongo.collection import Collection
import pytest
from pytest import raises

from arctic.exceptions import DataIntegrityException
from arctic.store._ndarray_store import NdarrayStore, _promote_struct_dtypes
from pymongo.results import UpdateResult


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


def test_concat_and_rewrite_checks_chunk_count():
    self = create_autospec(NdarrayStore)
    collection = create_autospec(Collection)
    version = {}
    previous_version = {'_id': sentinel.id,
                        'base_version_id': sentinel.base_version_id,
                        'version': sentinel.version,
                        'segment_count' : 3,
                        'append_count' : 1,
                        'up_to': sentinel.up_to}
    symbol = sentinel.symbol
    item = sentinel.item

    collection.find.return_value = [{'compressed': True},
                                    {'compressed': False}]
    with pytest.raises(DataIntegrityException) as e:
        NdarrayStore._concat_and_rewrite(self, collection, version, symbol, item, previous_version)
    assert str(e.value) == 'Symbol: sentinel.symbol:sentinel.version expected 1 segments but found 0'


def test_concat_and_rewrite_checks_written():
    self = create_autospec(NdarrayStore)
    collection = create_autospec(Collection)
    version = {'_id': sentinel.version_id,
               'segment_count': 1}
    previous_version = {'_id': sentinel.id,
                       'up_to': sentinel.up_to,
                        'base_version_id': sentinel.base_version_id,
                        'version': sentinel.version,
                        'segment_count' : 5,
                        'append_count' : 3}
    symbol = sentinel.symbol
    item = []

    collection.find.return_value = [{'_id': sentinel.id,
                                     'segment' : 47, 'compressed': True},
                                    {'compressed': True},
                                    # 3 appended items
                                    {'compressed': False}, {'compressed': False}, {'compressed': False}]
    collection.update_many.return_value = create_autospec(UpdateResult, matched_count=1)
    NdarrayStore._concat_and_rewrite(self, collection, version, symbol, item, previous_version)
    assert self.check_written.call_count == 1


def test_concat_and_rewrite_checks_updated():
    self = create_autospec(NdarrayStore)
    collection = create_autospec(Collection)
    version = {'_id': sentinel.version_id,
               'segment_count': 1}
    previous_version = {'_id': sentinel.id,
                        'up_to': sentinel.up_to,
                        'base_version_id': sentinel.base_version_id,
                        'version': sentinel.version,
                        'segment_count' : 5,
                        'append_count' : 3}
    symbol = sentinel.symbol
    item = []

    collection.find.return_value = [{'_id': sentinel.id,
                                     'segment' : 47, 'compressed': True},
                                    {'compressed': True},
                                    # 3 appended items
                                    {'compressed': False}, {'compressed': False}, {'compressed': False}]
    collection.update_many.return_value = create_autospec(UpdateResult, matched_count=0)
    with pytest.raises(DataIntegrityException) as e:
        NdarrayStore._concat_and_rewrite(self, collection, version, symbol, item, previous_version)
    assert str(e.value) == 'Symbol: sentinel.symbol:sentinel.version update_many updated 0 segments instead of 1'
