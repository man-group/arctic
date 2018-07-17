import hashlib
import six
from six.moves import cPickle
import io
from six.moves import xrange

import numpy as np
import boto3
from bson import BSON
import pandas as pd

from arctic._compression import compress_array, decompress


_CHUNK_SIZE = 2 * 1024 * 1024 - 2048  # ~2 MB (a bit less for usePowerOf2Sizes)


#TODO Error handling - duplicate keys etc.
class DictBackedKeyValueStore(object):

    def __init__(self, chunk_size=_CHUNK_SIZE):
        self.store = {}
        self.versions = {}
        self.chunk_size = chunk_size

    def write_version(self, library_name, symbol, version_doc):
        #TODO write with s3 versioning
        self.versions.setdefault(symbol, []).append(version_doc)

    def read_version(self, library_name, symbol, as_of=None):
        #TODO handle as_of
        if symbol in self.versions:
            return self.versions[symbol][-1]
        else:
            return None

    def write_segment(self, library_name, symbol, segment_data, previous_segment_keys=set()):
        segment_hash = checksum(symbol, segment_data)
        segment_key = _segment_key(library_name, symbol, segment_hash)

        # optimisation so we don't rewrite identical segments
        # checking if segment already exists might be expensive.
        if segment_key not in previous_segment_keys:
            self.store[segment_key] = segment_data
        return segment_key

    def read_segments(self, library_name, segment_keys):
        return (self.store[k] for k in segment_keys)


def _check_bucket(client, bucket_name):
    response = client.get_bucket_versioning(Bucket=bucket_name)
    if 'Status' in response and response['Status'] == 'Enabled':
        return
    else:
        raise ValueError("Bucket {} is not setup correctly."
                         " Does it exist and is versioning enabled?".format(bucket_name))

class S3KeyValueStore(object):
    """S3 Store for use with GenericVersionStore.

    Uses object key format:

    /{library_name}/symbols/{symbol}.bson - version documents
    /{library_name}/segments/{symbol}/{segment_hash} - segment documents
    /{library_name}/snapshots/{snapname}.bson - snapshot documents

    """
    # TODO should KV Stores be responsible for ID creation?

    def __init__(self, bucket, chunk_size=_CHUNK_SIZE):
        self.client = boto3.client('s3')
        # TODO validate bucket exists and has versioning switched on
        self.bucket = bucket
        self.chunk_size = chunk_size

    def write_version(self, library_name, symbol, version_doc):
        version_path = self._make_version_path(library_name, symbol)
        encoded_version_doc = BSON.encode(version_doc)
        put_result = self.client.put_object(Body=encoded_version_doc, Bucket=self.bucket, Key=version_path)
        version_doc['version'] = put_result['VersionId']

    def list_versions(self, library_name, symbol):
        version_path = self._make_version_path(library_name, symbol)
        paginator = self.client.get_paginator("list_object_versions")
        results = []
        for page in paginator.paginate(Bucket=self.bucket, Prefix=version_path):
            results.append(pd.DataFrame(page['Versions']))
        # TODO decide appropriate generic response format
        return pd.concat(results)

    def list_symbols(self, library_name):
        base_symbols_path = self._make_base_symbols_path(library_name)
        # TODO handle snapshots etc.
        results = []
        paginator = self.client.get_paginator("list_objects_v2")
        for page in paginator.paginate(Bucket=self.bucket, Delimiter='/', Prefix=base_symbols_path):
            results.extend((self._extract_symbol_from_path(base_symbols_path, p['Key']) for p in page['Contents']))
        return results

    def delete_symbol(self, library_name, symbol):
        """Soft deletes a symbol - no data is removed, snapshots still work.

        Other cleanup jobs needed to reclaim the storage.
        """
        version_path = self._make_version_path(library_name, symbol)
        self.client.delete_object(Bucket=self.bucket, Key=version_path)

    def delete_snapshot(self, library_name, snap_name):
        """Soft deletes a snapshot. Versions in the snapshot are unaffected"""
        snapshot_path = self._make_snaphot_path(library_name, snap_name)
        self.client.delete_object(Bucket=self.bucket, Key=snapshot_path)

    def read_version(self, library_name, symbol, as_of=None, version_id=None, snapshot_id=None):
        version_path = self._make_version_path(library_name, symbol)
        get_object_args = dict(Bucket=self.bucket, Key=version_path)
        if any([as_of, version_id, snapshot_id]):
            get_object_args['VersionId'] = self._find_version(library_name, symbol, as_of, version_id, snapshot_id)
        try:
            encoded_version_doc = self.client.get_object(**get_object_args)
        except self.client.exceptions.NoSuchKey:
            return None
        version_doc = BSON(encoded_version_doc['Body'].read()).decode()
        version_doc['version'] = encoded_version_doc['VersionId']
        return version_doc

    def write_segment(self, library_name, symbol, segment_data, previous_segment_keys=set()):
        segment_hash = checksum(symbol, segment_data)
        segment_path = self._make_segment_path(library_name, symbol, segment_hash)

        # optimisation so we don't rewrite identical segments
        # checking if segment already exists might be expensive.
        if segment_path not in previous_segment_keys:
            self.client.put_object(Body=segment_data, Bucket=self.bucket, Key=segment_path)
        return segment_path

    def read_segments(self, library_name, segment_keys):
        for k in segment_keys:
            yield self.client.get_object(Bucket=self.bucket, Key=k)['Body'].read()

    def snapshot(self, library_name, snap_name, metadata=None, skip_symbols=None, versions=None):
        snapshot_path = self._make_snaphot_path(library_name, snap_name)
        symbols_path = self._make_base_symbols_path(library_name)
        latest_versions_df = self._list_all_versions(library_name)

        symbols = latest_versions_df.loc[:, 'Key'].apply(lambda x: self._extract_symbol_from_path(symbols_path, x))
        latest_versions = latest_versions_df.set_index(symbols).loc[:, 'VersionId']
        if skip_symbols:
            latest_versions = latest_versions.drop(labels=skip_symbols, errors='ignore')
        key_version_mapping = latest_versions.to_dict()
        if versions:
            key_version_mapping.update(versions)

        snapshot_dict = {'versions': key_version_mapping, 'metadata': metadata or {}}
        encoded_snap = BSON.encode(snapshot_dict)
        self.client.put_object(Body=encoded_snap, Bucket=self.bucket, Key=snapshot_path)

    def _read_snapshot(self, library_name, snap_name):
        snapshot_path = self._make_snaphot_path(library_name, snap_name)
        get_object_args = dict(Bucket=self.bucket, Key=snapshot_path)
        encoded_snapshot = self.client.get_object(**get_object_args)
        snapshot = BSON(encoded_snapshot['Body'].read()).decode()
        return snapshot

    def list_snapshots(self, library_name):
        base_snaphot_path = self._make_base_snaphot_path(library_name)
        results = []
        paginator = self.client.get_paginator("list_objects_v2")
        for page in paginator.paginate(Bucket=self.bucket, Delimiter='/', Prefix=base_snaphot_path):
            results.extend((self._extract_symbol_from_path(base_snaphot_path, p['Key']) for p in page['Contents']))
        return results

    def _list_all_versions(self, library_name):
        symbols_path = self._make_base_symbols_path(library_name)
        results = []

        paginator = self.client.get_paginator("list_object_versions")
        version_iterator = paginator.paginate(Bucket=self.bucket, Prefix=symbols_path)
        filtered_iterator = version_iterator.search("Versions[?IsLatest][]")
        results.extend(filtered_iterator)
        # TODO decide appropriate generic response format
        return pd.DataFrame(results)

    def _find_version(self, library_name, symbol, as_of, version_id, snapshot_id):
        if sum(v is not None for v in [as_of, version_id, snapshot_id]) > 1:
            raise ValueError('Only one of as_of, version_id, snapshot_id should be specified')

        if version_id:
            return version_id
        elif as_of:
            # getting all versions will get slow with many versions - look into filtering in S3 using as_of date
            versions = self.list_versions(library_name, symbol)
            valid_versions = versions.loc[versions['LastModified'] <= as_of, 'VersionId']
            if len(valid_versions) == 0:
                raise KeyError('No versions found for as_of {} for symbol: {}, library {}'.format(as_of,
                                                                                                  symbol,
                                                                                                  library_name))
            else:
                return valid_versions.iloc[-1]
        elif snapshot_id:
            return self._read_snapshot(library_name, snapshot_id)['versions'][symbol]
        else:
            raise ValueError('One of as_of, version_id, snapshot_id should be specified')

    def _make_base_symbols_path(self, library_name):
        return '{}/symbols/'.format(library_name)

    def _make_version_path(self, library_name, symbol):
        return '{}/symbols/{}.bson'.format(library_name, symbol)

    def _extract_symbol_from_path(self, base_symbols_path, symbol_path):
        return symbol_path.replace(base_symbols_path, '').replace('/', '').replace('.bson', '')

    def _make_segment_path(self, library_name, symbol, segment_hash):
        return '{}/segments/{}/{}'.format(library_name, symbol, segment_hash)

    def _make_snaphot_path(self, library_name, snapshot_name):
        return '{}/snapshots/{}.bson'.format(library_name, snapshot_name)

    def _make_base_snaphot_path(self, library_name):
        return '{}/snapshots/'.format(library_name)


def checksum(symbol, data):
    sha = hashlib.sha1()
    sha.update(symbol.encode('ascii'))

    if isinstance(data, six.binary_type):
        sha.update(data)
    else:
        sha.update(str(data).encode('ascii'))
    return sha.hexdigest()


def _segment_key(library_name, symbol, segment_hash):
    # TODO handle slashes in symbols
    return "{}/{}/{}".format(library_name, symbol, segment_hash)
