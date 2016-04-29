import bson
from bson.binary import Binary
from bson.errors import InvalidDocument
from six.moves import cPickle, xrange
import io
import lz4
import pymongo

from arctic.store._version_store_utils import checksum, pickle_compat_load

_MAGIC_CHUNKED = '__chunked__'
_CHUNK_SIZE = 15 * 1024 * 1024  # 15MB
_MAX_BSON_ENCODE = 256 * 1024  # 256K - don't fill up the version document with encoded bson


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
            if blob == _MAGIC_CHUNKED:
                collection = mongoose_lib.get_top_level_collection()
                data = b''.join(x['data'] for x in collection.find({'symbol': symbol,
                                                                   'parent': version['_id']},
                                                                   sort=[('segment', pymongo.ASCENDING)]))
            else:
                data = blob
            # Backwards compatibility
            data = lz4.decompress(data)
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
        version['blob'] = _MAGIC_CHUNKED
        pickled = lz4.compressHC(cPickle.dumps(item, protocol=cPickle.HIGHEST_PROTOCOL))

        for i in xrange(int(len(pickled) / _CHUNK_SIZE + 1)):
            segment = {'data': Binary(pickled[i * _CHUNK_SIZE : (i + 1) * _CHUNK_SIZE])}
            sha = checksum(symbol, segment)
            segment['segment'] = i
            collection.update_one({'symbol': symbol, 'sha': sha}, {'$set': segment,
                                                               '$addToSet': {'parent': version['_id']}},
                                       upsert=True)
