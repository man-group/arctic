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


def test_save_read_large_ndarray(library):
    dtype = np.dtype([('abc', 'int64')])
    ndarr = np.arange(30 * 1024 * 1024 / dtype.itemsize).view(dtype=dtype)
    assert len(ndarr.tostring()) > 16 * 1024 * 1024
    library.write('MYARR', ndarr)
    saved_arr = library.read('MYARR').data
    assert np.all(ndarr == saved_arr)


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
