import bson
import logging
from bson.binary import Binary
from bson.errors import InvalidDocument
from six.moves import cPickle, xrange
import io
from .._compression import decompress, compress_array
import pymongo

from arctic.store._version_store_utils import checksum, pickle_compat_load
from ..exceptions import UnsupportedPickleStoreVersion


# new versions of chunked pickled objects MUST begin with __chunked__
_MAGIC_CHUNKED = '__chunked__'
_MAGIC_CHUNKEDV2 = '__chunked__V2'
_CHUNK_SIZE = 15 * 1024 * 1024  # 15MB
_MAX_BSON_ENCODE = 256 * 1024  # 256K - don't fill up the version document with encoded bson

logger = logging.getLogger(__name__)


class PickleStore(object):

    @classmethod
    def initialize_library(cls, *args, **kwargs):
        pass

    def get_info(self, version):
        ret = {}
        ret['type'] = 'blob'
        ret['handler'] = self.__class__.__name__
        return ret

    def read(self, backing_store, library_name, version, symbol, **kwargs):
        segment_keys = version['segment_keys']
        data = b''.join(decompress(s) for s in backing_store.read_segments(library_name, segment_keys))
        return pickle_compat_load(io.BytesIO(data))

    def write(self, backing_store, library_name, version, symbol, item, previous_version):

        # Try to pickle it. This is best effort
        version['blob'] = _MAGIC_CHUNKEDV2
        pickled = cPickle.dumps(item, protocol=cPickle.HIGHEST_PROTOCOL)
        chunk_size = backing_store.chunk_size

        data = compress_array([pickled[i * chunk_size: (i + 1) * chunk_size] for i in xrange(int(len(pickled) / chunk_size + 1))])

        if previous_version:
            previous_segment_keys = previous_version['segment_keys']
        else:
            previous_segment_keys = set()

        segment_keys = []
        for segment_data in data:
            segment_key = backing_store.write_segment(library_name, symbol,
                                                      segment_data, previous_segment_keys)
            segment_keys.append(segment_key)
        version['segment_keys'] = segment_keys

        #TODO Check written?
