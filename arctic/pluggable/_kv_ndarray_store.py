import logging
import hashlib

from bson.binary import Binary
import numpy as np

from arctic.exceptions import UnhandledDtypeException, DataIntegrityException, ArcticException
from arctic.store._version_store_utils import checksum

from arctic._compression import compress_array, decompress
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


def _resize_with_dtype(arr, dtype):
    """
    This function will transform arr into an array with the same type as dtype. It will do this by
    filling new columns with zeros (or NaNs, if it is a float column). Also, columns that are not
    in the new dtype will be dropped.
    """
    structured_arrays = dtype.names is not None and arr.dtype.names is not None
    old_columns = set(arr.dtype.names or [])
    new_columns = set(dtype.names or [])

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
    else:
        new_arr = arr.astype(dtype)

    return new_arr


class KeyValueNdarrayStore(object):
    """Chunked store for arbitrary ndarrays, supporting append. Using an arbitrary kv store backend.

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
      u'segment_keys': [] # sha
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
        pass

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

    def read(self, backing_store, library_name, version, symbol, **kwargs):
        index_range = self._index_range(version, symbol, **kwargs)
        return self._do_read(backing_store, library_name, version, symbol, index_range=index_range)

    def _do_read(self, backing_store, library_name, version, symbol, index_range=None):
        '''
        index_range is a 2-tuple of integers - a [from, to) range of segments to be read.
            Either from or to can be None, indicating no bound.
        '''
        from_index = index_range[0] if index_range else None
        to_index = version['up_to']
        if index_range and index_range[1] and index_range[1] < version['up_to']:
            to_index = index_range[1]

        segment_keys = version['segment_keys']
        filtered_segment_keys = []
        for i, segment_index in enumerate(version['raw_segment_index']):
            if (from_index is None or segment_index >= from_index) and \
                    (to_index is None or segment_index <= to_index):
                filtered_segment_keys.append(segment_keys[i])

        data = bytearray()
        for segment in backing_store.read_segments(library_name, filtered_segment_keys):
            data.extend(decompress(segment))

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

    def check_written(self, collection, symbol, version):
        # Check all the chunks are in place
        seen_chunks = collection.find({'symbol': symbol, 'parent': version['_id']},
                                      ).count()

        if seen_chunks != version['segment_count']:
            segments = [x['segment'] for x in collection.find({'symbol': symbol, 'parent': version['_id']},
                                                              projection={'segment': 1},
                                                              )]
            raise ArcticException("Failed to write all the Chunks. Saw %s expecting %s"
                                  "Parent: %s \n segments: %s" %
                                  (seen_chunks, version['segment_count'], version['_id'], segments))

    def checksum(self, item):
        sha = hashlib.sha1()
        sha.update(item.tostring())
        return Binary(sha.digest())

    def write(self, backing_store, library_name, version, symbol, item, previous_version, dtype=None):
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
                    and previous_version['dtype'] == version['dtype'] \
                    and self.checksum(item[:previous_version['up_to']]) == previous_version['sha']:
                # TODO handle appends!, currently segments will be reused to but all hashes will be recomputed
                pass
                # The first n rows are identical to the previous version, so just append.
                # Do a 'dirty' append (i.e. concat & start from a new base version) for safety
                # self._do_append(backing_store, collection, version, symbol, item[previous_version['up_to']:],
                #                previous_version, dirty_append=True)

        version['base_sha'] = version['sha']
        self._do_write(backing_store, library_name, version, symbol, item, previous_version)

    def _do_write(self, backing_store, library_name, version, symbol, item, previous_version, segment_offset=0):

        previous_segment_keys = []
        if previous_version:
            previous_segment_keys = previous_version['segment_keys']

        if segment_offset > 0 and 'segment_index' in previous_version:
            existing_index = previous_version['segment_index']
        else:
            existing_index = None

        sze = int(item.dtype.itemsize * np.prod(item.shape[1:]))
        length = len(item)

        # chunk and store the data by (uncompressed) size
        chunk_size = int(backing_store.chunk_size / sze)

        # Compress
        idxs = xrange(int(np.ceil(float(length) / chunk_size)))
        chunks = [(item[i * chunk_size: (i + 1) * chunk_size]).tostring() for i in idxs]
        compressed_segments = compress_array(chunks)

        segment_keys = []
        raw_segment_index = []
        for i, segment_data in zip(idxs, compressed_segments):
            segment_idx = min((i + 1) * chunk_size - 1, length - 1) + segment_offset
            segment_key = backing_store.write_segment(library_name, symbol,
                                                      segment_data, previous_segment_keys)
            raw_segment_index.append(segment_idx)
            segment_keys.append(segment_key)

        segment_index = self._segment_index(item, existing_index=existing_index, start=segment_offset,
                                            new_segments=raw_segment_index)
        if segment_index:
            version['segment_index'] = segment_index
        version['raw_segment_index'] = raw_segment_index
        version['segment_count'] = len(segment_keys)  # on appends this value is incorrect but is updated later on
        version['append_size'] = 0
        version['append_count'] = 0
        version['segment_keys'] = segment_keys

        #TODO add write check
        #self.check_written(collection, symbol, version)

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
