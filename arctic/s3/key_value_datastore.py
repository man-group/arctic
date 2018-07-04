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



class S3KeyValueStore(object):
    # TODO should KV Stores be responsible for ID creation?

    def __init__(self, bucket, chunk_size=_CHUNK_SIZE):
        self.client = boto3.client('s3')
        # TODO validate bucket exists and has versioning switched on
        self.bucket = bucket
        self.chunk_size = chunk_size

    def write_version(self, library_name, symbol, version_doc):
        version_path = self._make_version_path(library_name, symbol)
        encoded_version_doc = BSON.encode(version_doc)
        self.client.put_object(Body=encoded_version_doc, Bucket=self.bucket, Key=version_path)

    def list_versions(self, library_name, symbol):
        version_path = self._make_version_path(library_name, symbol)
        # TODO handle prefix issue and truncated responses
        version = self.client.list_object_versions(Bucket=self.bucket, Prefix=version_path)
        # TODO decide appropriate generic response format
        return pd.DataFrame(version['Versions'])

    def read_version(self, library_name, symbol, as_of=None):
        #TODO handle as_of
        version_path = self._make_version_path(library_name, symbol)
        try:
            encoded_version_doc = self.client.get_object(Bucket=self.bucket, Key=version_path)
        except self.client.exceptions.NoSuchKey:
            return None
        return BSON.decode(encoded_version_doc['Body'].read())

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

    def _make_version_path(self, library_name, symbol):
        return '{}/symbols/{}/version_doc/version_doc.bson'.format(library_name, symbol)

    def _make_segment_path(self, library_name, symbol, segment_hash):
        return '{}/symbols/{}/segments/{}'.format(library_name, symbol, segment_hash)

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
