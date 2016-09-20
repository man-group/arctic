import bson
import logging
from bson.binary import Binary
from bson.errors import InvalidDocument
from six.moves import cPickle, xrange
import io
from .._compression import decompress, compress_array
import pymongo

from ._version_store_utils import checksum, pickle_compat_load
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

    def read(self, mongoose_lib, version, symbol, **kwargs):
        blob = version.get("blob")
        if blob is not None:
            if blob == _MAGIC_CHUNKEDV2:
                collection = mongoose_lib.get_top_level_collection()
                data = b''.join(decompress(x['data']) for x in collection.find({'symbol': symbol,
                                                                                'parent': version['_id']},
                                                                               sort=[('segment', pymongo.ASCENDING)]))
            elif blob == _MAGIC_CHUNKED:
                collection = mongoose_lib.get_top_level_collection()
                data = b''.join(x['data'] for x in collection.find({'symbol': symbol,
                                                                    'parent': version['_id']},
                                                                   sort=[('segment', pymongo.ASCENDING)]))
                data = decompress(data)
            else:
                if blob[:len(_MAGIC_CHUNKED)] == _MAGIC_CHUNKED:
                    logger.error("Data was written by unsupported version of pickle store for symbol %s. Upgrade Arctic and try again" % symbol)
                    raise UnsupportedPickleStoreVersion("Data was written by unsupported version of pickle store")
                try:
                    data = decompress(blob)
                except:
                    logger.error("Failed to read symbol %s" % symbol)
            return pickle_compat_load(io.BytesIO(data))
        return version['data']

    def write(self, arctic_lib, version, symbol, item, previous_version):
        try:
            # If it's encodeable, then ship it
            b = bson.BSON.encode({'data': item})
            if len(b) < _MAX_BSON_ENCODE:
                version['data'] = item
                return
        except InvalidDocument:
            pass

        # Pickle, chunk and store the data
        collection = arctic_lib.get_top_level_collection()
        # Try to pickle it. This is best effort
        version['blob'] = _MAGIC_CHUNKEDV2
        pickled = cPickle.dumps(item, protocol=cPickle.HIGHEST_PROTOCOL)

        data = compress_array([pickled[i * _CHUNK_SIZE: (i + 1) * _CHUNK_SIZE] for i in xrange(int(len(pickled) / _CHUNK_SIZE + 1))])

        for seg, d in enumerate(data):
            segment = {'data': Binary(d)}
            segment['segment'] = seg
            seg += 1
            sha = checksum(symbol, segment)
            collection.update_one({'symbol': symbol, 'sha': sha},
                                  {'$set': segment, '$addToSet': {'parent': version['_id']}},
                                  upsert=True)
