import hashlib
import six
from six.moves import xrange

import numpy as np

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

    def read_segments(self, library_name, chunk_keys):
        return (self.store[k] for k in chunk_keys)


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
