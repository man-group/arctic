import bson
from datetime import datetime as dt, timedelta as dtd
from mock import patch
import numpy as np
from numpy.testing import assert_equal
from pymongo.server_type import SERVER_TYPE
import pytest

from arctic.store._ndarray_store import NdarrayStore, _APPEND_COUNT
from arctic.store.version_store import register_versioned_storage

from tests.integration.store.test_version_store import _query


register_versioned_storage(NdarrayStore)


def test_save_read_simple_ndarray(library):
    ndarr = np.ones(1000)
    library.write('MYARR', ndarr)
    saved_arr = library.read('MYARR').data
    assert np.all(ndarr == saved_arr)


def test_read_simple_ndarray_from_secondary(library_secondary, library_name):
    ndarr = np.ones(1000)
    library_secondary.write('MYARR', ndarr)
    with patch('pymongo.message.query', side_effect=_query(True, library_name)) as query, \
         patch('pymongo.server_description.ServerDescription.server_type', SERVER_TYPE.Mongos):
        saved_arr = library_secondary.read('MYARR').data
    assert query.call_count > 0
    assert np.all(ndarr == saved_arr)


def test_save_read_big_1darray(library):
    ndarr = np.random.rand(5326, 6020).ravel()
    library.write('MYARR', ndarr)
    saved_arr = library.read('MYARR').data
    assert np.all(ndarr == saved_arr)


def test_save_and_resave_reuses_chunks(library):
    with patch('arctic.store._ndarray_store._CHUNK_SIZE', 1000):
        ndarr = np.random.rand(1024)
        library.write('MYARR', ndarr)
        saved_arr = library.read('MYARR').data
        assert np.all(ndarr == saved_arr)
        orig_chunks = library._collection.count()
        assert orig_chunks == 9

        # Concatenate more values
        ndarr = np.concatenate([ndarr, np.random.rand(10)])
        # And change the original values - we're not a simple append
        ndarr[0] = ndarr[1] = ndarr[2] = 0
        library.write('MYARR', ndarr)
        saved_arr = library.read('MYARR').data
        assert np.all(ndarr == saved_arr)

        # Should contain the original chunks, but not double the number
        # of chunks
        new_chunks = library._collection.count()
        assert new_chunks == 11

        # We hit the update (rather than upsert) code path
        assert library._collection.find({'parent': {'$size': 2}}).count() == 7


def test_save_read_big_2darray(library):
    ndarr = np.random.rand(5326, 6020)
    library.write('MYARR', ndarr)
    saved_arr = library.read('MYARR').data
    assert np.all(ndarr == saved_arr)


def test_get_info_bson_object(library):
    ndarr = np.ones(1000)
    library.write('MYARR', ndarr)
    assert library.get_info('MYARR')['handler'] == 'NdarrayStore'


def test_save_read_ndarray_with_array_field(library):
    ndarr = np.empty(10, dtype=[('A', 'int64'), ('B', 'float64', (2,))])
    ndarr['A'] = 1
    ndarr['B'] = 2
    library.write('MYARR', ndarr)
    saved_arr = library.read('MYARR').data
    assert np.all(ndarr == saved_arr)


def test_append_ndarray_with_field_shape(library):
    ndarr = np.empty(10, dtype=[('A', 'int64'), ('B', 'float64', (2,))])
    ndarr['A'] = 1
    ndarr['B'] = 2
    ndarr2 = np.empty(10, dtype=[('A', 'int64'), ('B', 'int64', (2,))])
    ndarr2['A'] = 1
    ndarr2['B'] = 2

    library.write('MYARR', ndarr)
    library.append('MYARR', ndarr2)
    saved_arr = library.read('MYARR').data
    ndarr3 = np.empty(20, dtype=[('A', 'int64'), ('B', 'float64', (2,))])
    ndarr3['A'] = 1
    ndarr3['B'] = 2
    assert np.all(ndarr3 == saved_arr)


def test_append_simple_ndarray(library):
    ndarr = np.ones(1000, dtype='int64')
    library.write('MYARR', ndarr)
    library.append('MYARR', np.ones(1000, dtype='int64'))
    library.append('MYARR', np.ones(1000, dtype='int64'))
    library.append('MYARR', np.ones(2005, dtype='int64'))
    saved_arr = library.read('MYARR').data
    assert np.all(np.ones(5005, dtype='int64') == saved_arr)


def test_append_simple_ndarray_promoting_types(library):
    ndarr = np.ones(100, dtype='int64')
    library.write('MYARR', ndarr)
    library.append('MYARR', np.ones(100, dtype='float64'))
    library.append('MYARR', np.ones(100, dtype='int64'))
    library.append('MYARR', np.ones(205, dtype='float64'))
    saved_arr = library.read('MYARR').data
    assert np.all(np.ones(505, dtype='float64') == saved_arr)


def test_save_read_ndarray(library):
    ndarr = np.empty(1000, dtype=[('abc', 'int64')])
    library.write('MYARR', ndarr)
    saved_arr = library.read('MYARR').data
    assert np.all(ndarr == saved_arr)


def test_multiple_write(library):
    ndarr = np.empty(1000, dtype=[('abc', 'int64')])
    foo = np.empty(900, dtype=[('abc', 'int64')])
    library.write('MYARR', foo)
    v1 = library.read('MYARR').version
    library.write('MYARR', ndarr[:900])
    v2 = library.read('MYARR').version
    library.append('MYARR', ndarr[-100:])
    v3 = library.read('MYARR').version

    assert np.all(ndarr == library.read('MYARR').data)
    assert np.all(ndarr == library.read('MYARR', as_of=v3).data)
    assert np.all(foo == library.read('MYARR', as_of=v1).data)
    assert np.all(ndarr[:900] == library.read('MYARR', as_of=v2).data)


def test_cant_write_objects():
    store = NdarrayStore()
    assert not store.can_write(None, None, np.array([object()]))


def test_promote_types(library):
    ndarr = np.empty(1000, dtype=[('abc', 'int64')])
    library.write('MYARR', ndarr[:800])
    library.append('MYARR', ndarr[-200:].astype([('abc', 'float64')]))
    saved_arr = library.read('MYARR').data
    assert np.all(ndarr.astype([('abc', 'float64')]) == saved_arr)


def test_promote_types2(library):
    ndarr = np.array(np.arange(1000), dtype=[('abc', 'float64')])
    library.write('MYARR', ndarr[:800])
    library.append('MYARR', ndarr[-200:].astype([('abc', 'int64')]))
    saved_arr = library.read('MYARR').data
    assert np.all(ndarr.astype([('abc', np.promote_types('float64', 'int64'))]) == saved_arr)


def test_save_read_large_ndarray(library):
    dtype = np.dtype([('abc', 'int64')])
    ndarr = np.arange(30 * 1024 * 1024 / dtype.itemsize).view(dtype=dtype)
    assert len(ndarr.tostring()) > 16 * 1024 * 1024
    library.write('MYARR', ndarr)
    saved_arr = library.read('MYARR').data
    assert np.all(ndarr == saved_arr)

def test_append_read_large_ndarray(library):
    dtype = np.dtype([('abc', 'int64')])
    ndarr = np.arange(50 * 1024 * 1024 / dtype.itemsize).view(dtype=dtype)
    assert len(ndarr.tostring()) > 16 * 1024 * 1024
    library.write('MYARR1', ndarr)
    # Exactly enough appends to trigger 2 re-compacts, so the result should be identical
    # to writing the whole array at once
    ndarr2 = np.arange(240).view(dtype=dtype)
    for n in np.split(ndarr2, 120):
        library.append('MYARR1', n)

    saved_arr = library.read('MYARR1').data
    assert np.all(np.concatenate([ndarr, ndarr2]) == saved_arr)

    library.write('MYARR2', np.concatenate([ndarr, ndarr2]))

    version1 = library._read_metadata('MYARR1')
    version2 = library._read_metadata('MYARR2')
    assert version1['append_count'] == version2['append_count']
    assert version1['append_size'] == version2['append_size']
    assert version1['segment_count'] == version2['segment_count']
    assert version1['up_to'] == version2['up_to']


def test_save_append_read_ndarray(library):
    dtype = np.dtype([('abc', 'int64')])
    ndarr = np.arange(30 * 1024 * 1024 / dtype.itemsize).view(dtype=dtype)
    assert len(ndarr.tostring()) > 16 * 1024 * 1024
    library.write('MYARR', ndarr)

    sliver = np.arange(30).view(dtype=dtype)
    library.append('MYARR', sliver)

    saved_arr = library.read('MYARR').data
    assert np.all(np.concatenate([ndarr, sliver]) == saved_arr)

    library.append('MYARR', sliver)
    saved_arr = library.read('MYARR').data
    assert np.all(np.concatenate([ndarr, sliver, sliver]) == saved_arr)


def test_save_append_read_1row_ndarray(library):
    dtype = np.dtype([('abc', 'int64')])
    ndarr = np.arange(30 * 1024 * 1024 / dtype.itemsize).view(dtype=dtype)
    assert len(ndarr.tostring()) > 16 * 1024 * 1024
    library.write('MYARR', ndarr)

    sliver = np.arange(1).view(dtype=dtype)
    library.append('MYARR', sliver)

    saved_arr = library.read('MYARR').data
    assert np.all(np.concatenate([ndarr, sliver]) == saved_arr)

    library.append('MYARR', sliver)
    saved_arr = library.read('MYARR').data
    assert np.all(np.concatenate([ndarr, sliver, sliver]) == saved_arr)


def test_append_too_large_ndarray(library):
    dtype = np.dtype([('abc', 'int64')])
    ndarr = np.arange(30 * 1024 * 1024 / dtype.itemsize).view(dtype=dtype)
    assert len(ndarr.tostring()) > 16 * 1024 * 1024
    library.write('MYARR', ndarr)
    library.append('MYARR', ndarr)
    saved_arr = library.read('MYARR').data
    assert np.all(np.concatenate([ndarr, ndarr]) == saved_arr)


def test_empty_append_promotes_dtype(library):
    ndarr = np.array(["a", "b", "c"])
    ndarr2 = np.array([])
    library.write('MYARR', ndarr)
    library.append('MYARR', ndarr2)
    saved_arr = library.read('MYARR').data
    assert np.all(saved_arr == ndarr)


def test_empty_append_promotes_dtype2(library):
    ndarr = np.array([])
    ndarr2 = np.array(["a", "b", "c"])
    library.write('MYARR', ndarr)
    library.append('MYARR', ndarr2)
    saved_arr = library.read('MYARR').data
    assert np.all(saved_arr == ndarr2)


def test_empty_append_promotes_dtype3(library):
    ndarr = np.array([])
    ndarr2 = np.array(["a", "b", "c"])
    library.write('MYARR', ndarr)
    library.append('MYARR', ndarr2)
    library.append('MYARR', ndarr)
    library.append('MYARR', ndarr2)
    saved_arr = library.read('MYARR').data
    assert np.all(saved_arr == np.hstack((ndarr2, ndarr2)))


def test_empty_append_concat_and_rewrite(library):
    ndarr = np.array([])
    ndarr2 = np.array(["a", "b", "c"])
    library.write('MYARR', ndarr)
    for _ in range(_APPEND_COUNT + 2):
        library.append('MYARR', ndarr)
    library.append('MYARR', ndarr2)
    saved_arr = library.read('MYARR').data
    assert np.all(saved_arr == ndarr2)


def test_empty_append_concat_and_rewrite_2(library):
    ndarr2 = np.array(["a", "b", "c"])
    library.write('MYARR', ndarr2)
    for _ in range(_APPEND_COUNT + 1):
        library.append('MYARR', ndarr2)
    saved_arr = library.read('MYARR').data
    assert np.all(saved_arr == np.hstack([ndarr2] * (_APPEND_COUNT + 2)))


def test_empty_append_concat_and_rewrite_3(library):
    ndarr = np.array([])
    ndarr2 = np.array(["a", "b", "c"])
    library.write('MYARR', ndarr2)
    for _ in range(_APPEND_COUNT + 1):
        library.append('MYARR', ndarr)
    saved_arr = library.read('MYARR').data
    assert np.all(saved_arr == ndarr2)


def test_append_with_extra_columns(library):
    ndarr = np.array([(2.1, 1, "a")], dtype=[('C', np.float), ('B', np.int), ('A', 'S1')])
    ndarr2 = np.array([("b", 2, 3.1, 'c', 4, 5.)], dtype=[('A', 'S1'), ('B', np.int), ('C', np.float),
                                                          ('D', 'S1'), ('E', np.int), ('F', np.float)])
    expected = np.array([("a", 1, 2.1, '', 0, np.nan),
                         ("b", 2, 3.1, 'c', 4, 5.)],
                        dtype=np.dtype([('A', 'S1'), ('B', np.int), ('C', np.float),
                                        ('D', 'S1'), ('E', np.int), ('F', np.float)]))
    library.write('MYARR', ndarr)
    library.append('MYARR', ndarr2)
    saved_arr = library.read('MYARR').data

    assert expected.dtype == saved_arr.dtype
    assert_equal(expected.tolist(), saved_arr.tolist())


def test_save_append_delete_append(library):
    dtype = np.dtype([('abc', 'int64')])
    ndarr = np.arange(30 / dtype.itemsize).view(dtype=dtype)
    v1 = library.write('MYARR', ndarr)

    sliver = np.arange(30).view(dtype=dtype)
    v2 = library.append('MYARR', sliver)

    # intentionally leave an orphaned chunk lying around here
    library._delete_version('MYARR', v2.version, do_cleanup=False)

    sliver2 = np.arange(start=10, stop=40).view(dtype=dtype)
    # we can't append here, as the latest version is now out of sync with version_nums.
    # This gets translated to a do_append by the handler anyway.
    v3 = library.write('MYARR', np.concatenate([ndarr, sliver2]))

    assert np.all(ndarr == library.read('MYARR', as_of=v1.version).data)

    # Check that we don't get the orphaned chunk from v2 back again.
    assert np.all(np.concatenate([ndarr, sliver2]) == library.read('MYARR', as_of=v3.version).data)


@pytest.mark.xfail(reason="delete_version not safe with append...")
def test_delete_version_shouldnt_break_read(library):
    data = np.arange(30)
    yesterday = dt.utcnow() - dtd(days=1, seconds=1)
    _id = bson.ObjectId.from_datetime(yesterday)
    with patch("bson.ObjectId", return_value=_id):
        library.write('symbol', data, prune_previous_version=False)

    # Re-Write the data again
    library.write('symbol', data, prune_previous_version=False)
    library._delete_version('symbol', 1)
    assert repr(library.read('symbol').data) == repr(data)
