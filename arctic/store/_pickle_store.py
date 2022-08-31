import io
import logging
from operator import itemgetter

import bson
from bson.binary import Binary
from bson.errors import InvalidDocument
import pickle

from ._version_store_utils import checksum, pickle_compat_load, version_base_or_id
from .._compression import decompress, compress_array
from ..exceptions import UnsupportedPickleStoreVersion
from .._config import SKIP_BSON_ENCODE_PICKLE_STORE, MAX_BSON_ENCODE


# new versions of chunked pickled objects MUST begin with __chunked__
_MAGIC_CHUNKED = '__chunked__'
_MAGIC_CHUNKEDV2 = '__chunked__V2'
_CHUNK_SIZE = 15 * 1024 * 1024  # 15MB
_HARD_MAX_BSON_ENCODE = 10 * 1024 * 1024  # 10MB

logger = logging.getLogger(__name__)


class PickleStore(object):

    @classmethod
    def initialize_library(cls, *args, **kwargs):
        pass

    def get_info(self, _version):
        return {
            'type': 'blob',
            'handler': self.__class__.__name__,
        }

    def read(self, mongoose_lib, version, symbol, **kwargs):
        blob = version.get("blob")
        if blob is not None:
            if blob == _MAGIC_CHUNKEDV2:
                collection = mongoose_lib.get_top_level_collection()
                data = b''.join(decompress(x['data']) for x in sorted(
                    collection.find({'symbol': symbol, 'parent': version_base_or_id(version)}),
                    key=itemgetter('segment')))
            elif blob == _MAGIC_CHUNKED:
                collection = mongoose_lib.get_top_level_collection()
                data = b''.join(x['data'] for x in sorted(
                    collection.find({'symbol': symbol, 'parent': version_base_or_id(version)}),
                    key=itemgetter('segment')))
                data = decompress(data)
            else:
                if blob[:len(_MAGIC_CHUNKED)] == _MAGIC_CHUNKED:
                    logger.error("Data was written by unsupported version of pickle store for symbol %s. Upgrade Arctic and try again" % symbol)
                    raise UnsupportedPickleStoreVersion("Data was written by unsupported version of pickle store")
                try:
                    data = decompress(blob)
                except:
                    logger.error("Failed to read symbol %s" % symbol)

            try:
                # The default encoding is ascii.
                return pickle_compat_load(io.BytesIO(data))
            except UnicodeDecodeError as ue:
                # Using encoding='latin1' is required for unpickling NumPy arrays and instances of datetime, date
                # and time pickled by Python 2: https://docs.python.org/3/library/pickle.html#pickle.load
                logger.info("Could not Unpickle with ascii, Using latin1.")
                encoding = kwargs.get('encoding', 'latin_1')  # Check if someone has manually specified encoding.
                return pickle_compat_load(io.BytesIO(data), encoding=encoding)
        return version['data']

    @staticmethod
    def read_options():
        return []

    def write(self, arctic_lib, version, symbol, item, _previous_version):
        # Currently we try to bson encode if the data is less than a given size and store it in
        # the version collection, but pickling might be preferable if we have characters that don't
        # play well with the bson encoder or if you always want your data in the data collection.
        if not SKIP_BSON_ENCODE_PICKLE_STORE:
            try:
                # If it's encodeable, then ship it
                b = bson.BSON.encode({'data': item})
                if len(b) < min(MAX_BSON_ENCODE, _HARD_MAX_BSON_ENCODE):
                    version['data'] = item
                    return
            except InvalidDocument:
                pass

        # Pickle, chunk and store the data
        collection = arctic_lib.get_top_level_collection()
        # Try to pickle it. This is best effort
        version['blob'] = _MAGIC_CHUNKEDV2
        # Python 3.8 onwards uses protocol 5 which cannot be unpickled in Python versions below that, so limiting
        # it to use a maximum of protocol 4 in Python which is understood by 3.4 onwards and is still fairly efficient.
        # pickle version 4 is introduced with  python 3.4 and default with 3.8 onward
        pickle_protocol = min(pickle.HIGHEST_PROTOCOL, 4)
        pickled = pickle.dumps(item, protocol=pickle_protocol)

        data = compress_array([pickled[i * _CHUNK_SIZE: (i + 1) * _CHUNK_SIZE] for i in range(int(len(pickled) / _CHUNK_SIZE + 1))])

        for seg, d in enumerate(data):
            segment = {'data': Binary(d)}
            segment['segment'] = seg
            seg += 1
            sha = checksum(symbol, segment)
            collection.update_one({'symbol': symbol, 'sha': sha},
                                  {'$set': segment, '$addToSet': {'parent': version['_id']}},
                                  upsert=True)
