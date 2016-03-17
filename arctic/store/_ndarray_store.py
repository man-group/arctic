import logging
import hashlib

from bson.binary import Binary
import numpy as np
import pymongo
from pymongo.errors import OperationFailure, DuplicateKeyError

from ..decorators import mongo_retry, dump_bad_documents
from ..exceptions import UnhandledDtypeException
from ._version_store_utils import checksum

from .._compression import compress_array, decompress
from ..exceptions import ConcurrentModificationException
from six.moves import xrange


logger = logging.getLogger(__name__)

_CHUNK_SIZE = 2 * 1024 * 1024 - 2048  # ~2 MB (a bit less for usePowerOf2Sizes)
_APPEND_SIZE = 1 * 1024 * 1024  # 1MB
_APPEND_COUNT = 60  # 1 hour of 1 min data


def _promote_struct_dtypes(dtype1, dtype2):
    if not set(dtype1.names).issuperset(set(dtype2.names)):
        raise Exception("Removing columns from dtype not handled")

    def _promote(type1, type2):
        if type2 is None:
            return type1
        if type1.shape is not None:
            if not type1.shape == type2.shape:
                raise Exception("We do not handle changes to dtypes that have shape")
            return np.promote_types(type1.base, type2.base), type1.shape
        return np.promote_types(type1, type2)
    return np.dtype([(n, _promote(dtype1.fields[n][0], dtype2.fields.get(n, (None,))[0])) for n in dtype1.names])


class NumpySizeChunker(object):
    TYPE = 'numpysize'
    def __call__(self, item, **kwargs):
        sze = int(item.dtype.itemsize * np.prod(item.shape[1:]))
        length = len(item)
        chunk_size = int(_CHUNK_SIZE / sze)
        idxs = xrange(int(np.ceil(float(length) / chunk_size)))
        for i in idxs:
            yield min((i + 1) * chunk_size - 1, length - 1), item[i * chunk_size: (i + 1) * chunk_size].tostring()

    def index_range(self, version, from_version=None, **kwargs):
        """
        Tuple describing range to read from the ndarray - closed:open
        """
        from_index = None
        if from_version:
            if version['base_sha'] != from_version['base_sha']:
                # give up - the data has been overwritten, so we can't tail this
                raise ConcurrentModificationException("Concurrent modification - data has been overwritten")
            from_index = from_version['up_to']
        return from_index, None


class NdarrayStore(object):
    """Chunked store for arbitrary ndarrays, supporting append.

    for the simple example:
    dat = np.empty(10)
    library.write('test', dat) #version 1
    library.append('test', dat) #version 2

    version documents:

    [
     {u'_id': ObjectId('55fa9a7781f12654382e58b8'),
      u'symbol': u'test',
      u'version': 1
      u'type': u'ndarray',
      u'up_to': 10,  # no. of rows included in the data for this version
      u'append_count': 0,
      u'append_size': 0,
      u'base_sha': Binary('........', 0),
      u'dtype': u'float64',
      u'dtype_metadata': {},
      u'segment_count': 1, #only 1 segment included in this version
      u'sha': Binary('.........', 0),
      u'shape': [-1],
      },

     {u'_id': ObjectId('55fa9aa981f12654382e58ba'),
      u'symbol': u'test',
      u'version': 2
      u'type': u'ndarray',
      u'up_to': 20, # no. of rows included in the data for this version
      u'append_count': 1, # 1 append operation so far
      u'append_size': 80, # 80 bytes appended
      u'base_sha': Binary('.........', 0), # equal to sha for version 1
      u'base_version_id': ObjectId('55fa9a7781f12654382e58b8'), # _id of version 1
      u'dtype': u'float64',
      u'dtype_metadata': {},
      u'segment_count': 2, #2 segments included in this version
      }
      ]


    segment documents:

    [
     #first chunk written:
     {u'_id': ObjectId('55fa9a778b376a68efdd10e3'),
      u'compressed': True, #data is lz4 compressed on write()
      u'data': Binary('...........', 0),
      u'parent': [ObjectId('55fa9a7781f12654382e58b8')],
      u'segment': 9, #10 rows in the data up to this segment, so last row is 9
      u'sha': Binary('.............', 0), # checksum of (symbol, {'data':.., 'compressed':.., 'segment':...})
      u'symbol': u'test'},

     #second chunk appended:
     {u'_id': ObjectId('55fa9aa98b376a68efdd10e6'),
      u'compressed': False, # no initial compression for append()
      u'data': Binary('...........', 0),
      u'parent': [ObjectId('55fa9a7781f12654382e58b8')],
      u'segment': 19, #20 rows in the data up to this segment, so last row is 19
      u'sha': Binary('............', 0), # checksum of (symbol, {'data':.., 'compressed':.., 'segment':...})
      u'symbol': u'test'},
      ]

    """
    TYPE = 'ndarray'
    chunker_mapper = {NumpySizeChunker().TYPE: NumpySizeChunker()}

    @classmethod
    def initialize_library(cls, *args, **kwargs):
        pass

    @staticmethod
    def _ensure_index(collection):
        try:
            collection.create_index([('symbol', pymongo.HASHED)], background=True)
            collection.create_index([('symbol', pymongo.ASCENDING),
                                     ('sha', pymongo.ASCENDING)], unique=True, background=True)
            collection.create_index([('symbol', pymongo.ASCENDING),
                                     ('parent', pymongo.ASCENDING),
                                     ('segment', pymongo.ASCENDING)], unique=True, background=True)
        except OperationFailure as e:
            if "can't use unique indexes" in str(e):
                return
            raise

    @mongo_retry
    def can_delete(self, version, symbol):
        return self.can_read(version, symbol)

    def can_read(self, version, symbol):
        return version['type'] == self.TYPE

    def can_write(self, version, symbol, data):
        return isinstance(data, np.ndarray) and not data.dtype.hasobject

    def _dtype(self, string, metadata=None):
        if metadata is None:
            metadata = {}
        if string.startswith('['):
            return np.dtype(eval(string), metadata=metadata)
        return np.dtype(string, metadata=metadata)

    def get_info(self, version):
        ret = {}
        dtype = self._dtype(version['dtype'], version.get('dtype_metadata', {}))
        length = int(version['up_to'])
        ret['size'] = dtype.itemsize * length
        ret['segment_count'] = version['segment_count']
        ret['dtype'] = version['dtype']
        ret['type'] = version['type']
        ret['handler'] = self.__class__.__name__
        ret['rows'] = int(version['rows'])
        return ret

    def read(self, arctic_lib, version, symbol, read_preference=None, chunker=NumpySizeChunker(), **kwargs):
        index_range = chunker.index_range(version, **kwargs)
        collection = arctic_lib.get_top_level_collection()
        if read_preference:
            collection = collection.with_options(read_preference=read_preference)
        return self._do_read(collection, version, symbol, index_range=index_range)

    def _do_read(self, collection, version, symbol, index_range=None):
        segment_count = None

        spec = {'symbol': symbol,
                'parent': version.get('base_version_id', version['_id']),
                'segment': {'$lte': version['up_to']}
                }
        if index_range:
            if index_range[0]:
                spec['segment']['$gte'] = index_range[0]
            if index_range[1]:
                spec['segment']['$lte'] = index_range[1]
        else:
            segment_count = version.get('segment_count', None)

        segments = []
        i = -1
        for i, x in enumerate(collection.find(spec, sort=[('segment', pymongo.ASCENDING)],)):
            try:
                segments.append(decompress(x['data']) if x['compressed'] else x['data'])
            except Exception:
                dump_bad_documents(x, collection.find_one({'_id': x['_id']}),
                                      collection.find_one({'_id': x['_id']}),
                                      collection.find_one({'_id': x['_id']}))
                raise
        data = b''.join(segments)

        # Check that the correct number of segments has been returned
        if segment_count is not None and i + 1 != segment_count:
            raise OperationFailure("Incorrect number of segments returned for {}:{}.  Expected: {}, but got {}. {}".format(
                                   symbol, version['version'], segment_count, i + 1, collection.database.name + '.' + collection.name))

        dtype = self._dtype(version['dtype'], version.get('dtype_metadata', {}))
        rtn = np.fromstring(data, dtype=dtype).reshape(version.get('shape', (-1)))
        return rtn

    def _promote_types(self, dtype, dtype_str):
        if dtype_str == str(dtype):
            return dtype
        prev_dtype = self._dtype(dtype_str)
        if dtype.names is None:
            rtn = np.promote_types(dtype, prev_dtype)
        else:
            rtn = _promote_struct_dtypes(dtype, prev_dtype)
        rtn = np.dtype(rtn, metadata=dict(dtype.metadata or {}))
        return rtn

    def append(self, arctic_lib, version, symbol, item, previous_version, dtype=None):
        collection = arctic_lib.get_top_level_collection()
        if previous_version.get('shape', [-1]) != [-1, ] + list(item.shape)[1:]:
            raise UnhandledDtypeException()

        if not dtype:
            dtype = item.dtype

        if previous_version['up_to'] == 0:
            dtype = dtype
        elif len(item) == 0:
            dtype = self._dtype(previous_version['dtype'])
        else:
            dtype = self._promote_types(dtype, previous_version['dtype'])
        item = item.astype(dtype)

        if item.dtype.hasobject:
            raise UnhandledDtypeException()
        version['dtype'] = str(dtype)
        version['dtype_metadata'] = dict(dtype.metadata or {})
        version['type'] = self.TYPE

        old_arr = self._do_read(collection, previous_version, symbol).astype(dtype)
        # missing float columns should default to nan rather than zero
        old_dtype = self._dtype(previous_version['dtype'])
        if dtype.names is not None and old_dtype.names is not None:
            new_columns = set(dtype.names) - set(old_dtype.names)
            _is_float_type = lambda _dtype: _dtype.type in (np.float32, np.float64)
            _is_void_float_type = lambda _dtype: _dtype.type == np.void and _is_float_type(_dtype.subdtype[0])
            _is_float_or_void_float_type = lambda _dtype: _is_float_type(_dtype) or _is_void_float_type(_dtype)
            _is_float = lambda column: _is_float_or_void_float_type(dtype.fields[column][0])
            for new_column in filter(_is_float, new_columns):
                old_arr[new_column] = np.nan

        item = np.concatenate([old_arr, item])
        version['up_to'] = previous_version['up_to']
        version['sha'] = self.checksum(item)
        version['base_sha'] = version['sha']
        version['chunker'] = previous_version['chunker']
        version['rows'] = len(item)
        self._do_write(collection, version, symbol, item, previous_version, self.chunker_mapper[version['chunker']])

    def check_written(self, collection, symbol, version):
        # Check all the chunks are in place
        seen_chunks = collection.find({'symbol': symbol, 'parent': version['_id']},
                                      ).count()

        if seen_chunks != version['segment_count']:
            segments = [x['segment'] for x in collection.find({'symbol': symbol, 'parent': version['_id']},
                                                              projection={'segment': 1},
                                                              )]
            raise pymongo.errors.OperationFailure("Failed to write all the Chunks. Saw %s expecting %s"
                                                  "Parent: %s \n segments: %s" %
                                                  (seen_chunks, version['segment_count'], version['_id'], segments))

    def checksum(self, item):
        sha = hashlib.sha1()
        sha.update(item.tostring())
        return Binary(sha.digest())

    def write(self, arctic_lib, version, symbol, item, previous_version, chunker=NumpySizeChunker(),
              dtype=None, **kwargs):

        if item.dtype.hasobject:
            raise UnhandledDtypeException()

        collection = arctic_lib.get_top_level_collection()

        if not dtype:
            dtype = item.dtype
        version['dtype'] = str(dtype)
        version['shape'] = (-1,) + item.shape[1:]
        version['dtype_metadata'] = dict(dtype.metadata or {})
        version['type'] = self.TYPE
        version['rows'] = len(item)
        version['up_to'] = 0
        version['sha'] = self.checksum(item)
        version['chunker'] = chunker.TYPE

        if previous_version:
            if version['dtype'] == str(dtype) \
                    and 'sha' in previous_version \
                    and self.checksum(item[:previous_version['up_to']]) == previous_version['sha']:
                #The first n rows are identical to the previous version, so just append.
                self.append(collection, version, symbol, item[previous_version['up_to']:], previous_version)
                return

        version['base_sha'] = version['sha']
        self._do_write(collection, version, symbol, item, previous_version, chunker, **kwargs)

    def _do_write(self, collection, version, symbol, item, previous_version, chunker, **kwargs):
        previous_shas = []
        if previous_version:
            previous_shas = set([x['sha'] for x in
                                 collection.find({'symbol': symbol},
                                                 projection={'sha': 1, '_id': 0},
                                                 )
                                 ])

        i = -1
        chunks = []
        chunk_ranges = []
        for rng, chunk in chunker(item, **kwargs):
            chunks.append(chunk)
            chunk_ranges.append(rng)
        compressed_chunks = compress_array(chunks)

        # Write
        bulk = collection.initialize_unordered_bulk_op()
        rng = 0
        for rng, chunk in zip(chunk_ranges, compressed_chunks):
            i += 1
            segment = {'data': Binary(chunk), 'compressed': True}
            segment['segment'] = rng
            sha = checksum(symbol, segment)
            if sha not in previous_shas:
                segment['sha'] = sha
                bulk.find({'symbol': symbol, 'sha': sha, 'segment': segment['segment']}
                          ).upsert().update_one({'$set': segment, '$addToSet': {'parent': version['_id']}})
            else:
                bulk.find({'symbol': symbol, 'sha': sha, 'segment': segment['segment']}
                          ).update_one({'$addToSet': {'parent': version['_id']}})
        # update up_to with the end of the range value from chunker
        version['up_to'] = rng
        if i != -1:
            bulk.execute()

        version['segment_count'] = i + 1
        version['append_size'] = 0
        version['append_count'] = 0

        self.check_written(collection, symbol, version)
