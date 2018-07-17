from datetime import datetime as dt, timedelta as dtd

import bson
import numpy as np
import numpy.testing as npt
import pytest
from mock import patch


def test_save_read_simple_ndarray(generic_version_store):
    ndarr = np.ones(1000)
    generic_version_store.write('MYARR', ndarr)
    saved_arr = generic_version_store.read('MYARR').data
    assert np.all(ndarr == saved_arr)


def test_save_read_big_1darray(generic_version_store):
    ndarr = np.random.rand(5326, 6020).ravel()
    generic_version_store.write('MYARR', ndarr)
    saved_arr = generic_version_store.read('MYARR').data
    assert np.all(ndarr == saved_arr)


def test_save_and_resave_reuses_chunks(s3_store, generic_version_store, library_name):
    with patch.object(s3_store, 'chunk_size', 1000):
        ndarr = np.random.rand(1024)
        generic_version_store.write('MYARR', ndarr)
        saved = generic_version_store.read('MYARR')
        assert np.all(ndarr == saved.data)
        version_doc1 = s3_store.read_version(library_name, 'MYARR')
        assert version_doc1['segment_count'] == 9

        # Concatenate more values
        ndarr = np.concatenate([ndarr, np.random.rand(250)])
        # And change the original values - we're not a simple append
        ndarr[0] = ndarr[1] = ndarr[2] = 0
        generic_version_store.write('MYARR', ndarr)
        saved_arr = generic_version_store.read('MYARR').data
        npt.assert_almost_equal(ndarr, saved_arr)

        # Key should now have two versions
        versions = s3_store.list_versions(library_name, 'MYARR')
        assert len(versions) == 2
        # only one symbol though
        assert generic_version_store.list_symbols() == ['MYARR']

        # Should contain the more chunks, but not double the number
        # of chunks
        version_doc2 = s3_store.read_version(library_name, 'MYARR')
        assert version_doc2['segment_count'] == 11

        # Total unique chunks should be less than number of chunks of each
        # chunks are shared!
        all_segments = set(version_doc1['segment_keys'] + version_doc2['segment_keys'])
        assert len(all_segments) == 13


def test_save_read_big_2darray(generic_version_store):
    ndarr = np.random.rand(5326, 6020)
    generic_version_store.write('MYARR', ndarr)
    saved_arr = generic_version_store.read('MYARR').data
    npt.assert_almost_equal(ndarr, saved_arr)


def test_get_info_bson_object(generic_version_store):
    ndarr = np.ones(1000)
    generic_version_store.write('MYARR', ndarr)
    assert generic_version_store.get_info('MYARR')['handler'] == 'KeyValueNdarrayStore'


def test_save_read_ndarray_with_array_field(generic_version_store):
    ndarr = np.empty(10, dtype=[('A', 'int64'), ('B', 'float64', (2,))])
    ndarr['A'] = 1
    ndarr['B'] = 2
    generic_version_store.write('MYARR', ndarr)
    saved_arr = generic_version_store.read('MYARR').data


def test_save_read_ndarray(generic_version_store):
    ndarr = np.empty(1000, dtype=[('abc', 'int64')])
    generic_version_store.write('MYARR', ndarr)
    saved_arr = generic_version_store.read('MYARR').data
    assert np.all(ndarr == saved_arr)


def test_multiple_write(generic_version_store):
    ndarr = np.empty(1000, dtype=[('abc', 'int64')])
    foo = np.empty(900, dtype=[('abc', 'int64')])
    generic_version_store.write('MYARR', foo)
    v1 = generic_version_store.read('MYARR').version
    generic_version_store.write('MYARR', ndarr[:900])
    v2 = generic_version_store.read('MYARR').version
    generic_version_store.write('MYARR', ndarr)
    v3 = generic_version_store.read('MYARR').version

    assert np.all(foo == generic_version_store.read('MYARR', version_id=v1).data)
    assert np.all(ndarr[:900] == generic_version_store.read('MYARR', version_id=v2).data)
    assert np.all(ndarr == generic_version_store.read('MYARR', version_id=v3).data)
    assert np.all(ndarr == generic_version_store.read('MYARR').data)


def test_save_read_large_ndarray(generic_version_store):
    dtype = np.dtype([('abc', 'int64')])
    ndarr = np.arange(30 * 1024 * 1024 / dtype.itemsize).view(dtype=dtype)
    assert len(ndarr.tostring()) > 16 * 1024 * 1024
    generic_version_store.write('MYARR', ndarr)
    saved_arr = generic_version_store.read('MYARR').data
    assert np.all(ndarr == saved_arr)


def test_mutable_ndarray(generic_version_store):
    dtype = np.dtype([('abc', 'int64')])
    ndarr = np.arange(32).view(dtype=dtype)
    ndarr.setflags(write=True)
    generic_version_store.write('MYARR', ndarr)
    saved_arr = generic_version_store.read('MYARR').data
    assert saved_arr.flags['WRITEABLE']


@pytest.mark.xfail(reason="delete_version not safe with append...")
def xtest_delete_version_shouldnt_break_read(library):
    data = np.arange(30)
    yesterday = dt.utcnow() - dtd(days=1, seconds=1)
    _id = bson.ObjectId.from_datetime(yesterday)
    with patch("bson.ObjectId", return_value=_id):
        library.write('symbol', data, prune_previous_version=False)

    # Re-Write the data again
    library.write('symbol', data, prune_previous_version=False)
    library._delete_version('symbol', 1)
    assert repr(library.read('symbol').data) == repr(data)
