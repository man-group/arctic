from datetime import datetime as dt, timedelta as dtd

import bson
import numpy as np
import numpy.testing as npt
import pytest
from arctic.s3._kv_ndarray_store import KeyValueNdarrayStore
from arctic.s3.generic_version_store import GenericVersionStore
from mock import patch
from pymongo.server_type import SERVER_TYPE
import boto3

from arctic.s3.key_value_datastore import DictBackedKeyValueStore, S3KeyValueStore
from arctic.s3.generic_version_store import register_versioned_storage
from tests.integration.store.test_version_store import _query

from moto import mock_s3

@pytest.fixture()
def kv_store():
    store = DictBackedKeyValueStore()
    return store

@pytest.fixture()
def s3_bucket():
    return 'arctic2'

@mock_s3
@pytest.fixture()
def s3_store(s3_bucket):
    store = S3KeyValueStore(bucket=s3_bucket)
    return store

@pytest.fixture()
def s3_client():
    client = boto3.client('s3')
    return client

@pytest.fixture()
def generic_version_store(library_name, s3_store):
    register_versioned_storage(KeyValueNdarrayStore)
    return GenericVersionStore(library_name, backing_store=s3_store)

def setup_bucket(s3_bucket, s3_client):
    s3_client.create_bucket(Bucket=s3_bucket)
    s3_client.put_bucket_versioning(Bucket=s3_bucket,
                                    VersioningConfiguration={'MFADelete': 'Disabled',
                                                             'Status': 'Enabled'
                                                             })


@mock_s3
def test_save_read_simple_ndarray(s3_client, s3_bucket, generic_version_store):
    setup_bucket(s3_bucket, s3_client)
    ndarr = np.ones(1000)
    generic_version_store.write('MYARR', ndarr)
    saved_arr = generic_version_store.read('MYARR').data
    assert np.all(ndarr == saved_arr)



@mock_s3
def test_save_read_big_1darray(s3_client, s3_bucket, generic_version_store):
    setup_bucket(s3_bucket, s3_client)
    ndarr = np.random.rand(5326, 6020).ravel()
    generic_version_store.write('MYARR', ndarr)
    saved_arr = generic_version_store.read('MYARR').data
    assert np.all(ndarr == saved_arr)

@mock_s3
def test_save_and_resave_reuses_chunks(s3_client, s3_bucket, s3_store, generic_version_store, library_name):
    setup_bucket(s3_bucket, s3_client)
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

        # Should contain the more chunks, but not double the number
        # of chunks
        version_doc2 = s3_store.read_version(library_name, 'MYARR')
        assert version_doc2['segment_count'] == 11

        # Total unique chunks should be less than number of chunks of each
        # chunks are shared!
        all_segments = set(version_doc1['segment_keys'] + version_doc2['segment_keys'])
        assert len(all_segments) == 13


@mock_s3
def test_save_read_big_2darray(s3_client, s3_bucket, generic_version_store):
    setup_bucket(s3_bucket, s3_client)
    ndarr = np.random.rand(5326, 6020)
    generic_version_store.write('MYARR', ndarr)
    saved_arr = generic_version_store.read('MYARR').data
    npt.assert_almost_equal(ndarr, saved_arr)


@mock_s3
def test_get_info_bson_object(s3_client, s3_bucket, generic_version_store):
    setup_bucket(s3_bucket, s3_client)
    ndarr = np.ones(1000)
    generic_version_store.write('MYARR', ndarr)
    assert generic_version_store.get_info('MYARR')['handler'] == 'KeyValueNdarrayStore'


@mock_s3
def test_save_read_ndarray_with_array_field(s3_client, s3_bucket, generic_version_store):
    setup_bucket(s3_bucket, s3_client)
    ndarr = np.empty(10, dtype=[('A', 'int64'), ('B', 'float64', (2,))])
    ndarr['A'] = 1
    ndarr['B'] = 2
    generic_version_store.write('MYARR', ndarr)
    saved_arr = generic_version_store.read('MYARR').data


@mock_s3
def test_save_read_ndarray(s3_client, s3_bucket, generic_version_store):
    setup_bucket(s3_bucket, s3_client)
    ndarr = np.empty(1000, dtype=[('abc', 'int64')])
    generic_version_store.write('MYARR', ndarr)
    saved_arr = generic_version_store.read('MYARR').data
    assert np.all(ndarr == saved_arr)


@mock_s3
def test_multiple_write(s3_client, s3_bucket, generic_version_store):
    setup_bucket(s3_bucket, s3_client)
    ndarr = np.empty(1000, dtype=[('abc', 'int64')])
    foo = np.empty(900, dtype=[('abc', 'int64')])
    generic_version_store.write('MYARR', foo)
    v1 = generic_version_store.read('MYARR').version
    generic_version_store.write('MYARR', ndarr[:900])
    v2 = generic_version_store.read('MYARR').version
#    generic_version_store.append('MYARR', ndarr[-100:])
#    v3 = generic_version_store.read('MYARR').version

    assert np.all(ndarr[:900] == generic_version_store.read('MYARR').data)
    # npt.assert_almost_equal(ndarr, generic_version_store.read('MYARR', as_of=v3).data)
    # npt.assert_almost_equal(foo, generic_version_store.read('MYARR', as_of=v1).data)
    # npt.assert_almost_equal(ndarr[:900], generic_version_store.read('MYARR', as_of=v2).data)


@mock_s3
def test_save_read_large_ndarray(s3_client, s3_bucket, generic_version_store):
    setup_bucket(s3_bucket, s3_client)
    dtype = np.dtype([('abc', 'int64')])
    ndarr = np.arange(30 * 1024 * 1024 / dtype.itemsize).view(dtype=dtype)
    assert len(ndarr.tostring()) > 16 * 1024 * 1024
    generic_version_store.write('MYARR', ndarr)
    saved_arr = generic_version_store.read('MYARR').data
    assert np.all(ndarr == saved_arr)


@mock_s3
def test_mutable_ndarray(s3_client, s3_bucket, generic_version_store):
    setup_bucket(s3_bucket, s3_client)
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
