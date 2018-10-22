import hashlib
import logging
import os


from bson.binary import Binary
import numpy as np
import pymongo
from pymongo.errors import OperationFailure, DuplicateKeyError

from arctic._util import mongo_count
from ..async.async_arctic import INTERNAL_ASYNC
from ..async.async_utils import USE_ASYNC_MONGO_WRITES, ARCTIC_SERIALIZER_NTHREADS, ARCTIC_MONGO_NTHREADS
from ..decorators import mongo_retry
from ..exceptions import UnhandledDtypeException, DataIntegrityException, AsyncArcticException
from ..serialization.incremental import LazyIncrementalSerializer
from ._version_store_utils import checksum, version_base_or_id, _fast_check_corruption
from .._compression import compress_array, compress, decompress
from six.moves import xrange


from six.moves import queue
import math
import time
from ..async.async_arctic import INTERNAL_SERIALIZATION_POOL, INTERNAL_MONGO_POOL
import threading



logger = logging.getLogger(__name__)

_CHUNK_SIZE = 2 * 1024 * 1024 - 2048  # ~2 MB (a bit less for usePowerOf2Sizes)
_APPEND_SIZE = 1 * 1024 * 1024  # 1MB
_APPEND_COUNT = 60  # 1 hour of 1 min data

MONGO_BATCH_SIZE = os.environ.get('MONGO_BATCH_SIZE', 16)
MONGO_CONCURRENT_BATCHES = os.environ.get('MONGO_CONCURRENT_BATCHES', 2)

# Enabling the following has roughly a 5-7% performance hit (off by default)
_CHECK_CORRUPTION_ON_APPEND = bool(os.environ.get('CHECK_CORRUPTION_ON_APPEND'))


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

    # Currenlty it is called only from _concat_and_rewrite, with "base_version_id" always empty
    # Use version_base_or_id() instead, to make the method safe going forward, called form anywhere
    parent_id = version_base_or_id(version)

    # Update the parent set of the unchanged/compressed segments
    result = collection.update_many({
                                        'symbol': symbol,  # hit only the right shard
                                                           # update_many is a broadcast query otherwise
                                        '_id': {'$in': [x['_id'] for x in unchanged_segment_ids]}
                                    },
                                    {'$addToSet': {'parent': parent_id}})
    # Fast check for success without extra query
    if result.matched_count == len(unchanged_segment_ids):
        return
    # update_many is tricky sometimes wrt matched_count across replicas when balancer runs. Check based on _id.
    unchanged_ids = set([x['_id'] for x in unchanged_segment_ids])
    spec = {'symbol': symbol,
            'parent': parent_id,
            'segment': {'$lte': unchanged_segment_ids[-1]['segment']}}
    matched_segments_ids = set([x['_id'] for x in collection.find(spec)])
    if unchanged_ids != matched_segments_ids:
        logger.error("Mismatched unchanged segments for {}: {} != {} (query spec={})".format(
                        symbol, unchanged_ids, matched_segments_ids, spec))
        raise DataIntegrityException("Symbol: {}:{} update_many updated {} segments instead of {}".format(
            symbol, previous_version['version'], result.matched_count, len(unchanged_segment_ids)))


def _resize_with_dtype(arr, dtype):
    """
    This function will transform arr into an array with the same type as dtype. It will do this by
    filling new columns with zeros (or NaNs, if it is a float column). Also, columns that are not
    in the new dtype will be dropped.
    """
    structured_arrays = dtype.names is not None and arr.dtype.names is not None
    old_columns = arr.dtype.names or []
    new_columns = dtype.names or []

    # In numpy 1.9 the ndarray.astype method used to handle changes in number of fields. The code below
    # should replicate the same behaviour the old astype used to have.
    #
    # One may be tempted to use np.lib.recfunctions.stack_arrays to implement both this step and the
    # concatenate that follows but it 2x slower and it requires providing your own default values (instead
    # of np.zeros).
    #
    # Numpy 1.14 supports doing new_arr[old_columns] = arr[old_columns], which is faster than the code below
    # (in benchmarks it seems to be even slightly faster than using the old astype). However, that is not
    # supported by numpy 1.9.2.
    if structured_arrays and (old_columns != new_columns):
        old_columns = set(old_columns)
        new_columns = set(new_columns)

        new_arr = np.zeros(arr.shape, dtype)
        for c in old_columns & new_columns:
            new_arr[c] = arr[c]

        # missing float columns should default to nan rather than zero
        _is_float_type = lambda _dtype: _dtype.type in (np.float32, np.float64)
        _is_void_float_type = lambda _dtype: _dtype.type == np.void and _is_float_type(_dtype.subdtype[0])
        _is_float_or_void_float_type = lambda _dtype: _is_float_type(_dtype) or _is_void_float_type(_dtype)
        _is_float = lambda column: _is_float_or_void_float_type(dtype.fields[column][0])
        for new_column in filter(_is_float, new_columns - old_columns):
            new_arr[new_column] = np.nan

        return new_arr.astype(dtype)
    else:
        return arr.astype(dtype)


def set_corruption_check_on_append(enable):
    global _CHECK_CORRUPTION_ON_APPEND
    _CHECK_CORRUPTION_ON_APPEND = bool(enable)


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
                'parent': version_base_or_id(version),
                'segment': {'$lt': to_index}
                }
        if from_index is not None:
            spec['segment']['$gte'] = from_index
        else:
            segment_count = version.get('segment_count', None)

        data = bytearray()
        i = -1
        for i, x in enumerate(collection.find(spec, sort=[('segment', pymongo.ASCENDING)],)):
            data.extend(decompress(x['data']) if x['compressed'] else x['data'])

        # Check that the correct number of segments has been returned
        if segment_count is not None and i + 1 != segment_count:
            raise OperationFailure("Incorrect number of segments returned for {}:{}.  Expected: {}, but got {}. {}".format(
                                   symbol, version['version'], segment_count, i + 1, collection.database.name + '.' + collection.name))

        dtype = self._dtype(version['dtype'], version.get('dtype_metadata', {}))
        rtn = np.frombuffer(data, dtype=dtype).reshape(version.get('shape', (-1)))
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

        if (self._dtype(previous_version['dtype']).fields is None) != (dtype.fields is None):
            raise ValueError("type changes to or from structured array not supported")
        
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

            # This function will drop columns read from the previous version if they are not found in the
            # new append. However, the promote_types will raise an exception in that case and this code
            # will not be reached.
            old_arr = _resize_with_dtype(self._do_read(collection, previous_version, symbol), dtype)

            item = np.concatenate([old_arr, item])
            version['up_to'] = len(item)
            version['sha'] = self.checksum(item)
            version['base_sha'] = version['sha']
            self._do_write(collection, version, symbol, item, previous_version)
        else:
            version['dtype'] = previous_version['dtype']
            version['dtype_metadata'] = previous_version['dtype_metadata']
            version['type'] = self.TYPE
            
            # Verify (potential) corruption with append
            if _CHECK_CORRUPTION_ON_APPEND and _fast_check_corruption(
                    collection, symbol, previous_version,
                    check_count=False, check_last_segment=True, check_append_safe=True):
                logging.warning("Found mismatched segments for {} (version={}). "
                                "Converting append to concat and rewrite".format(symbol, previous_version['version']))
                dirty_append = True  # force a concat and re-write (use new base version id)

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
            version['base_version_id'] = version_base_or_id(previous_version)

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
                'parent': version_base_or_id(previous_version),
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
        # Currently only called from methods which guarantee 'base_version_id' is not populated.
        # Make it nonetheless safe for the general case.
        parent_id = version_base_or_id(version)

        # Check all the chunks are in place
        seen_chunks = mongo_count(collection, filter={'symbol': symbol, 'parent': parent_id})

        if seen_chunks != version['segment_count']:
            segments = [x['segment'] for x in collection.find({'symbol': symbol, 'parent': parent_id},
                                                              projection={'segment': 1},
                                                              )]
            raise pymongo.errors.OperationFailure("Failed to write all the Chunks. Saw %s expecting %s"
                                                  "Parent: %s \n segments: %s" %
                                                  (seen_chunks, version['segment_count'], parent_id, segments))

    @staticmethod
    def checksum(item):
        sha = hashlib.sha1()
        sha.update(item.tostring())
        return Binary(sha.digest())

    @staticmethod
    def incremental_checksum(item, curr_sha=None, is_bytes=False):
        curr_sha = hashlib.sha1() if curr_sha is None else curr_sha
        curr_sha.update(item if is_bytes else item.tostring())
        return curr_sha

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

        is_incremental_serializer = isinstance(item, LazyIncrementalSerializer)

        if previous_version:
            if is_incremental_serializer:
                # TODO: for now fall back to non-incremental serialization
                #       to compute the checksum we serialize once anyway (non mem footprint-friendly though)
                item, dtype = item.serialize()
                version['dtype'] = str(dtype)
                is_incremental_serializer = False
                # overlapping_checksum = item.checksum(0, previous_version['up_to'])
                # # TODO: pass an incremental serializer with an offset at "previous_version['up_to']:"
                # new_rows = item.input_data[previous_version['up_to']:]

            if 'sha' in previous_version \
                    and previous_version['dtype'] == version['dtype']:
                overlapping_checksum = self.checksum(item[:previous_version['up_to']])
                if overlapping_checksum == previous_version['sha']:
                    # The first n rows are identical to the previous version, so just append.
                    # Do a 'dirty' append (i.e. concat & start from a new base version) for safety
                    # TODO: do not recompute from scratch, rather do incremental checksum
                    version['sha'] = self.checksum(item)
                    # TODO: Enable incremental serialization also for appends
                    new_rows = item[previous_version['up_to']:]
                    self._do_append(collection, version, symbol, new_rows, previous_version,
                                    dirty_append=True)
                    return

        if is_incremental_serializer:
            version['sha'], version['up_to'] = self._do_write_generator(collection, version,
                                                                        symbol, item, previous_version)
        else:
            # TODO: do not recompute from scratch, rather do incremental checksum
            version['sha'] = self.checksum(item)
            self._do_write(collection, version, symbol, item, previous_version)
        version['base_sha'] = version['sha']

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

        # TODO: Delete me
        start_time = time.time()

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
        # TODO: why write the whole bulk and not write in smaller batches?
        #       This would reduce the memory footprint for large items.
        #       Also, mongo_retry could be used here
        if i != -1:
            collection.bulk_write(bulk, ordered=False)

        # TODO: Delete me
        end_time = time.time()
        print('Total time: {:.4f}, '
              'total batches {}, '
              'total segments {}'
              '(workers: {} {})'.format(
            end_time - start_time,
            len(bulk),
            len(bulk),
            INTERNAL_SERIALIZATION_POOL._workers_pool._max_workers, INTERNAL_MONGO_POOL._workers_pool._max_workers))

        segment_index = self._segment_index(item, existing_index=existing_index, start=segment_offset,
                                            new_segments=segment_index)
        if segment_index:
            version['segment_index'] = segment_index
        version['segment_count'] = i + 1
        version['append_size'] = 0
        version['append_count'] = 0

        self.check_written(collection, symbol, version)

    @staticmethod
    def _request_record_time(request):
        print("{:.3f} \t {:.3f} \t {:.3f} \t {:.3f}".format(request.create_time, request.execution_duration, request.schedule_delay, request.total_time))

    MEASUREMENTS = {
        'execution_duration': [],
        'schedule_delay': [],
        'total_time': []
    }
    @staticmethod
    def _register_measurements(request):
        NdarrayStore.MEASUREMENTS['execution_duration'].append(request.execution_duration)
        NdarrayStore.MEASUREMENTS['schedule_delay'].append(request.schedule_delay)
        NdarrayStore.MEASUREMENTS['total_time'].append(request.total_time)

    @staticmethod
    def get_stats(measurements):
        import numpy as np
        mean = np.mean(measurements)
        stdev = np.std(measurements)
        min = np.min(measurements)
        max = np.max(measurements)
        return mean, stdev, min, max

    def _serialization_worker(self, my_symbol, version, previous_shas, segment_offset, items_lazy_ser, serialize_tasks_q, mongo_tasks_q):
        # tid = threading._get_ident()
        while True:
            task_todo = serialize_tasks_q.get(block=True, timeout=None)
            # print("{} undertaking serialization work: {}".format(tid, task_todo))
            if task_todo is None:
                continue
            from_idx, to_idx = task_todo

            segment_index = []
            bulk = []
            total_sha = None
            length = len(items_lazy_ser)

            for chunk_bytes, dtype, starting_row, ending_row in items_lazy_ser.generator_bytes(from_idx, to_idx):
                compressed_chunk = compress(chunk_bytes)
                total_sha = self.incremental_checksum(compressed_chunk, curr_sha=total_sha, is_bytes=True)
                segment = {'data': Binary(compressed_chunk),
                           'compressed': True,
                           'segment': ending_row + segment_offset - 1}
                # print("segment: {} ({}, {}) [{}]".format(segment['segment'], starting_row, ending_row, tid))
                segment_index.append(segment['segment'])
                segment_sha = checksum(my_symbol, segment)

                if segment_sha not in previous_shas:
                    segment['sha'] = segment_sha
                    op = pymongo.UpdateOne(
                        {'symbol': my_symbol,
                         'sha': segment_sha,
                         'segment': segment['segment']},
                        {'$set': segment,
                         '$addToSet': {'parent': version['_id']}},
                        upsert=True)
                else:
                    op = pymongo.UpdateOne(
                        {'symbol': my_symbol,
                         'sha': segment_sha,
                         'segment': segment['segment']},
                        {'$addToSet': {'parent': version['_id']}})

                bulk.append(op)

            if bulk:
                mongo_tasks_q.put((bulk, from_idx, to_idx), block=True, timeout=None)
                serialize_tasks_q.task_done()
                # print("SER: Put to mongo task: {}/{}/{} of {}".format(len(bulk), from_idx, to_idx, length))

    def _mongo_worker(self, collection, mongo_tasks_q, done_tasks_q):
        while True:
            try:
                bulk, from_idx, to_idx = mongo_tasks_q.get(block=True, timeout=None)
                # print("MONGO: Wring: {}/{}/{}".format(len(bulk), from_idx, to_idx))
                collection.bulk_write(bulk, ordered=False)
                # print("MONGO: Wrote: {}/{}/{}".format(len(bulk), from_idx, to_idx))
                done_tasks_q.put((len(bulk), from_idx, to_idx))
            except Exception as e:
                # pass
                logger.exception("Failed")
            finally:
                mongo_tasks_q.task_done()

    @staticmethod
    def _do_generate_serialization_tasks(items_lazy_ser):
        rows_per_chunk = items_lazy_ser.rows_per_chunk
        total_rows = len(items_lazy_ser)
        step = MONGO_BATCH_SIZE*rows_per_chunk
        serialization_tasks = [(i, min(i+step, total_rows)) for i in range(0, total_rows, step)]
        return serialization_tasks

    def _do_write_generator(self, collection, version, symbol, items_lazy_ser, previous_version, segment_offset=0):
        previous_shas = []
        if previous_version:
            previous_shas = set([Binary(x['sha']) for x in
                                 collection.find({'symbol': symbol},
                                                 projection={'sha': 1, '_id': 0},
                                                 )
                                 ])

        start_time = time.time()

        serialize_tasks_q = queue.Queue()
        mongo_tasks_q = queue.Queue()
        done_tasks_q = queue.Queue()

        # Serializers
        serialization_workers = []
        for i in range(ARCTIC_SERIALIZER_NTHREADS):
            req = INTERNAL_SERIALIZATION_POOL.submit_request(
                self._serialization_worker,
                is_modifier=False,
                my_symbol=symbol, version=version, previous_shas=previous_shas, segment_offset=segment_offset, items_lazy_ser=items_lazy_ser, serialize_tasks_q=serialize_tasks_q, mongo_tasks_q=mongo_tasks_q,
                # async_callback=NdarrayStore._register_measurements
            )
            serialization_workers.append(req)

        # Mongo Writers
        mongo_workers = []
        for i in range(ARCTIC_MONGO_NTHREADS):
            req = INTERNAL_MONGO_POOL.submit_request(
                self._mongo_worker,
                is_modifier=False,
                collection=collection, mongo_tasks_q=mongo_tasks_q, done_tasks_q=done_tasks_q,
                # async_callback=NdarrayStore._register_measurements
            )
            mongo_workers.append(req)

        serialization_tasks = NdarrayStore._do_generate_serialization_tasks(items_lazy_ser)
        for next_task in serialization_tasks:
            serialize_tasks_q.put(next_task, block=True, timeout=None)
            # print('Added {}'.format(next_task))
        # print("Finished adding.")

        serialize_tasks_q.join()
        print(mongo_tasks_q.qsize())

        mongo_tasks_q.join()

        total_batches, total_segments = 0, 0
        serialization_tasks = set(serialization_tasks)
        while serialization_tasks:
            segments_in_batch, from_row, to_row = done_tasks_q.get(block=True, timeout=None)
            serialization_tasks.remove((from_row, to_row))
            total_batches += 1
            total_segments += segments_in_batch

        end_time = time.time()

        print('Total time: {:.4f}, '
              'total batches {}, '
              'total segments {}'
              '(workers: {} {})'.format(
            end_time - start_time,
            total_batches,
            total_segments,
            INTERNAL_SERIALIZATION_POOL._workers_pool._max_workers, INTERNAL_MONGO_POOL._workers_pool._max_workers))

        return 'sadfsadf', 10

    def _do_write_generator_orig(self, collection, version, symbol, items_lazy_ser, previous_version, segment_offset=0):
        previous_shas = []
        if previous_version:
            previous_shas = set([Binary(x['sha']) for x in
                                 collection.find({'symbol': symbol},
                                                 projection={'sha': 1, '_id': 0},
                                                 )
                                 ])

        if segment_offset > 0 and 'segment_index' in previous_version:
            existing_index = previous_version['segment_index']
        else:
            existing_index = None

        segment_index = []
        i = -1
        total_sha = None
        length = len(items_lazy_ser)
        bulk = []
        requests = []

        for v in NdarrayStore.MEASUREMENTS.values():
            del v[:]

        import time
        import math
        rows_per_chunk = items_lazy_ser.rows_per_chunk
        expected_chunks = int(math.ceil(float(length)/rows_per_chunk))
        # start = time.time()
        # from_row = 0
        # while from_row < length:
        #     until_row = from_row + MONGO_BATCH_SIZE * rows_per_chunk
        #
        #     req = INTERNAL_ASYNC.submit_request(
        #         self.test_serialization,
        #         is_modifier=False,
        #         my_symbol=symbol, version=version, previous_shas=previous_shas, segment_offset=segment_offset,
        #         items_lazy_ser=items_lazy_ser,
        #         from_idx=from_row, to_idx=until_row,
        #         # async_callback=NdarrayStore._register_measurements
        #     )
        #     requests.append(req)
        #
        #     from_row = until_row
        #
        #     alive, done = INTERNAL_ASYNC.filter_finished_requests(requests)
        #     if len(alive) >= MONGO_CONCURRENT_BATCHES:
        #         INTERNAL_ASYNC.wait_any_request(alive)

        _, bulk = self.test_serialization(
            my_symbol=symbol, version=version, previous_shas=previous_shas, segment_offset=segment_offset,
            items_lazy_ser=items_lazy_ser,
            from_idx=0, to_idx=MONGO_BATCH_SIZE * items_lazy_ser.rows_per_chunk)
        start = time.time()
        for i in range(expected_chunks/len(bulk)):
            req = INTERNAL_ASYNC.submit_request(
                self.test_mongo,
                is_modifier=False,
                collection=collection, bulk=bulk,
                async_callback=NdarrayStore._register_measurements
            )
            requests.append(req)
            # alive, done = INTERNAL_ASYNC.filter_finished_requests(requests)
            # if len(alive) >= MONGO_CONCURRENT_BATCHES:
            #     INTERNAL_ASYNC.wait_any_request(alive)
            # self.test_mongo(collection, bulk)
        total_segments = expected_chunks


        INTERNAL_ASYNC.join()
        total_time = time.time() - start


        requests, done_requests = INTERNAL_ASYNC.filter_finished_requests(requests)
        assert not requests
        # total_segments = 0
        # for r in done_requests:
        #     total_segments += len(r.data[1])

        # for k, v in NdarrayStore.MEASUREMENTS.items():
        #     print("{}: {}".format(k, ["{:.3f}".format(x) for x in NdarrayStore.get_stats(v)]))
        pool = INTERNAL_ASYNC._workers_pool
        print('Total time: {:.4f}, total segments {} {}, {:.4f}sec/segment (workers: {} {})'.format(total_time, total_segments, expected_chunks, total_time/total_segments, pool._max_workers, len(pool._threads)))

        return 'sdfsdfsdf', length

        # measurements = []
        # import time
        # start = time.time()
        # for chunk_bytes, dtype in items_lazy_ser.generator_bytes():
        #     i += 1
        #     compressed_chunk = compress(chunk_bytes)
        #     total_sha = self.incremental_checksum(compressed_chunk, curr_sha=total_sha, is_bytes=True)
        #     segment = {'data': Binary(compressed_chunk),
        #                'compressed': True,
        #                'segment': min((i + 1) * items_lazy_ser.rows_per_chunk - 1, length - 1) + segment_offset}
        #     segment_index.append(segment['segment'])
        #     segment_sha = checksum(symbol, segment)
        #
        #     if segment_sha not in previous_shas:
        #         segment['sha'] = segment_sha
        #         op = pymongo.UpdateOne({'symbol': symbol, 'sha': segment_sha, 'segment': segment['segment']},
        #                                {'$set': segment, '$addToSet': {'parent': version['_id']}},
        #                                upsert=True)
        #     else:
        #         op = pymongo.UpdateOne({'symbol': symbol, 'sha': segment_sha, 'segment': segment['segment']},
        #                                {'$addToSet': {'parent': version['_id']}})
        #
        #     bulk.append(op)
        #
        #     if len(bulk) >= MONGO_BATCH_SIZE:
        #         # requests = self._write_bulk(collection, bulk, requests)
        #         bulk = []
        #         measurements.append((time.time() - start)/float(MONGO_BATCH_SIZE))
        #         start = time.time()
        #
        # def get_stats(measurements):
        #     import numpy as np
        #     mean = np.mean(measurements)
        #     stdev = np.std(measurements)
        #     min = np.min(measurements)
        #     max = np.max(measurements)
        #     return mean, stdev, min, max
        #
        # print("\t ".join(["{:.3f}".format(x) for x in get_stats(measurements[1:] if len(measurements) > 1 else measurements)]))

        # for chunk_bytes, dtype in items_lazy_ser.generator_bytes():
        #     i += 1
        #     compressed_chunk = compress(chunk_bytes)
        #     total_sha = self.incremental_checksum(compressed_chunk, curr_sha=total_sha, is_bytes=True)
        #     segment = {'data': Binary(compressed_chunk),
        #                'compressed': True,
        #                'segment': min((i + 1) * items_lazy_ser.rows_per_chunk - 1, length - 1) + segment_offset}
        #     segment_index.append(segment['segment'])
        #     segment_sha = checksum(symbol, segment)
        #
        #     if segment_sha not in previous_shas:
        #         segment['sha'] = segment_sha
        #         op = pymongo.UpdateOne({'symbol': symbol, 'sha': segment_sha, 'segment': segment['segment']},
        #                                {'$set': segment, '$addToSet': {'parent': version['_id']}},
        #                                upsert=True)
        #     else:
        #         op = pymongo.UpdateOne({'symbol': symbol, 'sha': segment_sha, 'segment': segment['segment']},
        #                                {'$addToSet': {'parent': version['_id']}})
        #
        #     bulk.append(op)
        #
        #     if len(bulk) >= MONGO_BATCH_SIZE:
        #         # requests = self._write_bulk(collection, bulk, requests)
        #         bulk = []
        #
        # if bulk:
        #     requests = self._write_bulk(collection, bulk, requests)
        #
        # Wait all requests to finish
        # if USE_ASYNC_MONGO_WRITES:
        #     INTERNAL_ASYNC.wait_requests(requests)
        #     alive_requests, _ = INTERNAL_ASYNC.filter_finished_requests(requests)
        #     if len(alive_requests) != 0:
        #         raise AsyncArcticException("Failed to complete all async mongo writes for {} / {}".format(
        #             symbol, version))

        if i != -1:
            total_sha = Binary(total_sha.digest())
        else:
            # Zero sized data
            emptyser, _ = items_lazy_ser.serialize()
            total_sha = self.checksum(emptyser)

        orig_data = items_lazy_ser.input_data
        segment_index = self._segment_index(orig_data, existing_index=existing_index, start=segment_offset,
                                            new_segments=segment_index)
        if segment_index:
            version['segment_index'] = segment_index
        version['segment_count'] = i + 1
        version['append_size'] = 0
        version['append_count'] = 0

        self.check_written(collection, symbol, version)

        return total_sha, length

    def _write_bulk(self, collection, bulk, requests):
        if USE_ASYNC_MONGO_WRITES:
            alive_requests, done_requests = INTERNAL_ASYNC.filter_finished_requests(requests)
            # Wait until at least one requests finishes
            if len(alive_requests) >= MONGO_CONCURRENT_BATCHES:
                INTERNAL_ASYNC.wait_any_request(alive_requests)
                alive_requests, done_requests = INTERNAL_ASYNC.filter_finished_requests(requests)
            # Submit the batch
            request = INTERNAL_ASYNC.submit_request(collection.bulk_write, is_modifier=True, requests=bulk,
                                                    # async_callback=NdarrayStore._request_record_time
                                                    )
            alive_requests.append(request)
            return alive_requests
        else:
            collection.bulk_write(bulk, ordered=False)
            return requests

    def _do_write_generator_first(self, collection, version, symbol, items_lazy_ser, previous_version, segment_offset=0):
        previous_shas = []
        if previous_version:
            previous_shas = set([Binary(x['sha']) for x in
                                 collection.find({'symbol': symbol},
                                                 projection={'sha': 1, '_id': 0},
                                                 )
                                 ])

        if segment_offset > 0 and 'segment_index' in previous_version:
            existing_index = previous_version['segment_index']
        else:
            existing_index = None

        start_time = time.time()
        total_batches = 0
        total_segments = 0

        segment_index = []
        i = -1
        total_sha = None
        length = len(items_lazy_ser)
        bulk = []
        requests = []

        for chunk_bytes, dtype, _, _ in items_lazy_ser.generator_bytes():
            i += 1
            compressed_chunk = compress(chunk_bytes)
            total_sha = self.incremental_checksum(compressed_chunk, curr_sha=total_sha, is_bytes=True)
            segment = {'data': Binary(compressed_chunk),
                       'compressed': True,
                       'segment': min((i + 1) * items_lazy_ser.rows_per_chunk - 1, length - 1) + segment_offset}
            segment_index.append(segment['segment'])
            segment_sha = checksum(symbol, segment)

            if segment_sha not in previous_shas:
                segment['sha'] = segment_sha
                op = pymongo.UpdateOne({'symbol': symbol, 'sha': segment_sha, 'segment': segment['segment']},
                                       {'$set': segment, '$addToSet': {'parent': version['_id']}},
                                       upsert=True)
            else:
                op = pymongo.UpdateOne({'symbol': symbol, 'sha': segment_sha, 'segment': segment['segment']},
                                       {'$addToSet': {'parent': version['_id']}})

            bulk.append(op)

            total_segments += 1

            if len(bulk) >= MONGO_BATCH_SIZE:
                requests = self._write_bulk(collection, bulk, requests)
                bulk = []
                total_batches += 1

        if bulk:
            requests = self._write_bulk(collection, bulk, requests)
            total_batches += 1

        # Wait all requests to finish
        if USE_ASYNC_MONGO_WRITES:
            INTERNAL_ASYNC.wait_requests(requests)
            alive_requests, _ = INTERNAL_ASYNC.filter_finished_requests(requests)
            if len(alive_requests) != 0:
                raise AsyncArcticException("Failed to complete all async mongo writes for {} / {}".format(
                    symbol, version))

        end_time = time.time()
        print('Total time: {:.4f}, '
              'total batches {}, '
              'total segments {}'
              '(workers: {} {})'.format(
            end_time - start_time,
            total_batches,
            total_segments,
            INTERNAL_SERIALIZATION_POOL._workers_pool._max_workers, INTERNAL_MONGO_POOL._workers_pool._max_workers))

        if i != -1:
            total_sha = Binary(total_sha.digest())
        else:
            # Zero sized data
            emptyser, _ = items_lazy_ser.serialize()
            total_sha = self.checksum(emptyser)

        orig_data = items_lazy_ser.input_data
        segment_index = self._segment_index(orig_data, existing_index=existing_index, start=segment_offset,
                                            new_segments=segment_index)
        if segment_index:
            version['segment_index'] = segment_index
        version['segment_count'] = i + 1
        version['append_size'] = 0
        version['append_count'] = 0

        self.check_written(collection, symbol, version)

        return total_sha, length

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
