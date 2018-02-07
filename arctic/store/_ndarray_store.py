import logging
import hashlib

from bson.binary import Binary
import numpy as np
import pymongo
from pymongo.errors import OperationFailure, DuplicateKeyError

from ..decorators import mongo_retry
from ..exceptions import UnhandledDtypeException, DataIntegrityException
from ._version_store_utils import checksum

from .._compression import compress_array, decompress
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


def _attempt_update_unchanged(symbol, unchanged_segment_ids, collection, version, previous_version):
    if not unchanged_segment_ids or not collection or not version:
        return
    # Update the parent set of the unchanged/compressed segments
    result = collection.update_many({
                                        'symbol': symbol,  # hit only the right shard
                                                           # update_many is a broadcast query otherwise
                                        '_id': {'$in': [x['_id'] for x in unchanged_segment_ids]}
                                    },
                                    {'$addToSet': {'parent': version['_id']}})
    # Fast check for success without extra query
    if result.matched_count == len(unchanged_segment_ids):
        return
    # update_many is tricky sometimes wrt matched_count across replicas when balancer runs. Check based on _id.
    unchanged_ids = set([x['_id'] for x in unchanged_segment_ids])
    spec = {'symbol': symbol,
            'parent': version['_id'],
            'segment': {'$lte': unchanged_segment_ids[-1]['segment']}}
    matched_segments_ids = set([x['_id'] for x in collection.find(spec)])
    if unchanged_ids != matched_segments_ids:
        logger.error("Mismatched unchanged segments for {}: {} != {} (query spec={})".format(
                        symbol, unchanged_ids, matched_segments_ids, spec))
        raise DataIntegrityException("Symbol: {}:{} update_many updated {} segments instead of {}".format(
            symbol, previous_version['version'], result.matched_count, len(unchanged_segment_ids)))


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

    def _index_range(self, version, symbol, from_version=None, **kwargs):
        """
        Tuple describing range to read from the ndarray - closed:open
        """
        from_index = None
        if from_version:
            from_index = from_version['up_to']
        return from_index, None

    def get_info(self, version):
        ret = {}
        dtype = self._dtype(version['dtype'], version.get('dtype_metadata', {}))
        length = int(version['up_to'])
        ret['size'] = dtype.itemsize * length
        ret['segment_count'] = version['segment_count']
        ret['dtype'] = version['dtype']
        ret['type'] = version['type']
        ret['handler'] = self.__class__.__name__
        ret['rows'] = int(version['up_to'])
        return ret

    def read(self, arctic_lib, version, symbol, read_preference=None, **kwargs):
        index_range = self._index_range(version, symbol, **kwargs)
        collection = arctic_lib.get_top_level_collection()
        if read_preference:
            collection = collection.with_options(read_preference=read_preference)
        return self._do_read(collection, version, symbol, index_range=index_range)

    def _do_read(self, collection, version, symbol, index_range=None):
        '''
        index_range is a 2-tuple of integers - a [from, to) range of segments to be read. 
            Either from or to can be None, indicating no bound.
        '''
        from_index = index_range[0] if index_range else None
        to_index = version['up_to']
        if index_range and index_range[1] and index_range[1] < version['up_to']:
            to_index = index_range[1]
        segment_count = None

        spec = {'symbol': symbol,
                'parent': version.get('base_version_id', version['_id']),
                'segment': {'$lt': to_index}
                }
        if from_index is not None:
            spec['segment']['$gte'] = from_index
        else:
            segment_count = version.get('segment_count', None)

        segments = []
        i = -1
        for i, x in enumerate(collection.find(spec, sort=[('segment', pymongo.ASCENDING)],)):
            segments.append(decompress(x['data']) if x['compressed'] else x['data'])

        data = b''.join(segments)

        # free up memory from initial copy of data
        del segments

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

    def append(self, arctic_lib, version, symbol, item, previous_version, dtype=None, dirty_append=True):
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
        if str(dtype) != previous_version['dtype']:
            logger.debug('Converting %s from %s to %s' % (symbol, previous_version['dtype'], str(dtype)))
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
            version['up_to'] = len(item)
            version['sha'] = self.checksum(item)
            version['base_sha'] = version['sha']
            self._do_write(collection, version, symbol, item, previous_version)
        else:
            version['dtype'] = previous_version['dtype']
            version['dtype_metadata'] = previous_version['dtype_metadata']
            version['type'] = self.TYPE
            self._do_append(collection, version, symbol, item, previous_version, dirty_append)

    def _do_append(self, collection, version, symbol, item, previous_version, dirty_append):

        data = item.tostring()
        # Compatibility with Arctic 1.22.0 that didn't write base_sha into the version document
        version['base_sha'] = previous_version.get('base_sha', Binary(b''))
        version['up_to'] = previous_version['up_to'] + len(item)
        if len(item) > 0:
            version['segment_count'] = previous_version['segment_count'] + 1
            version['append_count'] = previous_version['append_count'] + 1
            version['append_size'] = previous_version['append_size'] + len(data)
        else:
            version['segment_count'] = previous_version['segment_count']
            version['append_count'] = previous_version['append_count']
            version['append_size'] = previous_version['append_size']

        #_CHUNK_SIZE is probably too big if we're only appending single rows of data - perhaps something smaller,
        #or also look at number of appended segments?
        if not dirty_append and version['append_count'] < _APPEND_COUNT and version['append_size'] < _APPEND_SIZE:
            version['base_version_id'] = previous_version.get('base_version_id', previous_version['_id'])

            if len(item) > 0:

                segment = {'data': Binary(data), 'compressed': False}
                segment['segment'] = version['up_to'] - 1
                try:
                    collection.update_one({'symbol': symbol,
                                           'sha': checksum(symbol, segment)},
                                          {'$set': segment,
                                           '$addToSet': {'parent': version['base_version_id']}},
                                          upsert=True)
                except DuplicateKeyError:
                    '''If we get a duplicate key error here, this segment has the same symbol/parent/segment
                       as another chunk, but a different sha. This means that we have 'forked' history.
                       If we concat_and_rewrite here, new chunks will have a different parent id (the _id of this version doc)
                       ...so we can safely write them. 
                       '''
                    self._concat_and_rewrite(collection, version, symbol, item, previous_version)
                    return

                if 'segment_index' in previous_version:
                    segment_index = self._segment_index(item,
                                                        existing_index=previous_version.get('segment_index'),
                                                        start=previous_version['up_to'],
                                                        new_segments=[segment['segment'], ])
                    if segment_index:
                        version['segment_index'] = segment_index
                logger.debug("Appended segment %d for parent %s" % (segment['segment'], version['_id']))
            else:
                if 'segment_index' in previous_version:
                    version['segment_index'] = previous_version['segment_index']

        else:  # Too much data has been appended now, so rewrite (and compress/chunk).
            self._concat_and_rewrite(collection, version, symbol, item, previous_version)

    def _concat_and_rewrite(self, collection, version, symbol, item, previous_version):

        version.pop('base_version_id', None)

        # Figure out which is the last 'full' chunk
        spec = {'symbol': symbol,
                'parent': previous_version.get('base_version_id', previous_version['_id']),
                'segment': {'$lt': previous_version['up_to']}}

        read_index_range = [0, None]
        # The unchanged segments are the compressed ones (apart from the last compressed)
        unchanged_segment_ids = []
        for segment in collection.find(spec, projection={'_id':1,
                                                         'segment':1,
                                                         'compressed': 1
                                                         },
                                       sort=[('segment', pymongo.ASCENDING)]):
            # We want to stop iterating when we find the first uncompressed chunks
            if not segment['compressed']:
                # We include the last compressed chunk in the recompression
                if unchanged_segment_ids:
                    unchanged_segment_ids.pop()
                break
            unchanged_segment_ids.append(segment)

        # Found all the chunks which aren't part of an append
        if len(unchanged_segment_ids) < previous_version['segment_count'] - previous_version['append_count'] - 1:
            raise DataIntegrityException("Symbol: %s:%s expected %s segments but found %s" %
                                         (symbol, previous_version['version'],
                                          previous_version['segment_count'] - previous_version['append_count'] - 1,
                                          len(unchanged_segment_ids)
                                          ))
        if unchanged_segment_ids:
            read_index_range[0] = unchanged_segment_ids[-1]['segment'] + 1

        # Only read back the section that needs to be compressed here (index_range=...)
        old_arr = self._do_read(collection, previous_version, symbol, index_range=read_index_range)
        if len(item) == 0:
            logger.debug('Rewrite and compress/chunk item %s, rewrote old_arr' % symbol)
            self._do_write(collection, version, symbol, old_arr, previous_version, segment_offset=read_index_range[0])
        elif len(old_arr) == 0:
            logger.debug('Rewrite and compress/chunk item %s, wrote item' % symbol)
            self._do_write(collection, version, symbol, item, previous_version, segment_offset=read_index_range[0])
        else:
            logger.debug("Rewrite and compress/chunk %s, np.concatenate %s to %s" % (symbol,
                                                                                     item.dtype, old_arr.dtype))
            self._do_write(collection, version, symbol, np.concatenate([old_arr, item]), previous_version,
                           segment_offset=read_index_range[0])
        if unchanged_segment_ids:
            _attempt_update_unchanged(symbol, unchanged_segment_ids, collection, version, previous_version)
            version['segment_count'] = version['segment_count'] + len(unchanged_segment_ids)
            self.check_written(collection, symbol, version)

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

    def write(self, arctic_lib, version, symbol, item, previous_version, dtype=None):
        collection = arctic_lib.get_top_level_collection()
        if item.dtype.hasobject:
            raise UnhandledDtypeException()

        if not dtype:
            dtype = item.dtype
        version['dtype'] = str(dtype)
        version['shape'] = (-1,) + item.shape[1:]
        version['dtype_metadata'] = dict(dtype.metadata or {})
        version['type'] = self.TYPE
        version['up_to'] = len(item)
        version['sha'] = self.checksum(item)

        if previous_version:
            if 'sha' in previous_version \
                    and self.checksum(item[:previous_version['up_to']]) == previous_version['sha']:
                # The first n rows are identical to the previous version, so just append.
                # Do a 'dirty' append (i.e. concat & start from a new base version) for safety
                self._do_append(collection, version, symbol, item[previous_version['up_to']:], previous_version, dirty_append=True)
                return

        version['base_sha'] = version['sha']
        self._do_write(collection, version, symbol, item, previous_version)

    def _do_write(self, collection, version, symbol, item, previous_version, segment_offset=0):

        sze = int(item.dtype.itemsize * np.prod(item.shape[1:]))

        # chunk and store the data by (uncompressed) size
        chunk_size = int(_CHUNK_SIZE / sze)

        previous_shas = []
        if previous_version:
            previous_shas = set([Binary(x['sha']) for x in
                                 collection.find({'symbol': symbol},
                                                 projection={'sha': 1, '_id': 0},
                                                 )
                                 ])

        length = len(item)

        if segment_offset > 0 and 'segment_index' in previous_version:
            existing_index = previous_version['segment_index']
        else:
            existing_index = None

        segment_index = []
        i = -1

        # Compress
        idxs = xrange(int(np.ceil(float(length) / chunk_size)))
        chunks = [(item[i * chunk_size: (i + 1) * chunk_size]).tostring() for i in idxs]
        compressed_chunks = compress_array(chunks)

        # Write
        bulk = []
        for i, chunk in zip(idxs, compressed_chunks):
            segment = {'data': Binary(chunk), 'compressed': True}
            segment['segment'] = min((i + 1) * chunk_size - 1, length - 1) + segment_offset
            segment_index.append(segment['segment'])
            sha = checksum(symbol, segment)
            if sha not in previous_shas:
                segment['sha'] = sha
                bulk.append(pymongo.UpdateOne({'symbol': symbol, 'sha': sha, 'segment': segment['segment']},
                                              {'$set': segment, '$addToSet': {'parent': version['_id']}},
                                              upsert=True))
            else:
                bulk.append(pymongo.UpdateOne({'symbol': symbol, 'sha': sha, 'segment': segment['segment']},
                                              {'$addToSet': {'parent': version['_id']}}))
        if i != -1:
            collection.bulk_write(bulk, ordered=False)

        segment_index = self._segment_index(item, existing_index=existing_index, start=segment_offset,
                                            new_segments=segment_index)
        if segment_index:
            version['segment_index'] = segment_index
        version['segment_count'] = i + 1
        version['append_size'] = 0
        version['append_count'] = 0

        self.check_written(collection, symbol, version)

    def _segment_index(self, new_data, existing_index, start, new_segments):
        """
        Generate a segment index which can be used in subselect data in _index_range.
        This function must handle both generation of the index and appending to an existing index

        Parameters:
        -----------
        new_data: new data being written (or appended)
        existing_index: index field from the versions document of the previous version
        start: first (0-based) offset of the new data
        segments: list of offsets. Each offset is the row index of the
                  the last row of a particular chunk relative to the start of the _original_ item.
                  array(new_data) - segments = array(offsets in item)

        Returns:
        --------
        Library specific index metadata to be stored in the version document.
        """
        pass  # numpy arrays have no index
