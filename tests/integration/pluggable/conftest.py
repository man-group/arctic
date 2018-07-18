import pytest
import boto3

from moto import mock_s3

from arctic.pluggable.key_value_datastore import S3KeyValueStore
from arctic.pluggable.generic_version_store import register_versioned_storage, GenericVersionStore
from arctic.pluggable._kv_ndarray_store import KeyValueNdarrayStore
from arctic.pluggable._parquet_store import ParquetStore
from arctic.pluggable._pandas_ndarray_store import PandasDataFrameStore, PandasSeriesStore, PandasPanelStore


@pytest.fixture
def s3_mock():
    with mock_s3():
        yield


@pytest.fixture()
def s3_bucket():
    return 'arctic2'


@pytest.fixture()
def s3_client(s3_mock):
    return boto3.client('s3')


@pytest.fixture()
def s3_store(s3_bucket, s3_client):
    s3_client.create_bucket(Bucket=s3_bucket)
    s3_client.put_bucket_versioning(Bucket=s3_bucket,
                                    VersioningConfiguration={'MFADelete': 'Disabled',
                                                             'Status': 'Enabled'})
    return S3KeyValueStore(bucket=s3_bucket)


@pytest.fixture()
def generic_version_store(library_name, s3_store):
    register_versioned_storage(KeyValueNdarrayStore)
    register_versioned_storage(PandasPanelStore)
    register_versioned_storage(PandasSeriesStore)
    register_versioned_storage(PandasDataFrameStore)
    return GenericVersionStore(library_name, backing_store=s3_store)


@pytest.fixture()
def parquet_version_store(library_name, s3_store):
    return GenericVersionStore(library_name, backing_store=s3_store, bson_handler=ParquetStore())
