import abc
import logging

import numpy as np
import pandas as pd
from six.moves import xrange

from ..exceptions import ArcticSerializationException
from ..store._ndarray_store import MAX_DOCUMENT_SIZE, _CHUNK_SIZE


ABC = abc.ABCMeta('ABC', (object,), {})
log = logging.getLogger(__name__)


class LazyIncrementalSerializer(ABC):
    def __init__(self, serializer, input_data, chunk_size=_CHUNK_SIZE):
        if chunk_size < 1:
            raise ArcticSerializationException("LazyIncrementalSerializer can't be initialized "
                                               "with chunk_size < 1 ({})".format(chunk_size))
        if not serializer:
            raise ArcticSerializationException("LazyIncrementalSerializer can't be initialized "
                                               "with a None serializer object")
        self.input_data = input_data
        self.chunk_size = chunk_size
        self._serializer = serializer
        self._initialized = False

    @abc.abstractmethod
    def __len__(self):
        pass

    @abc.abstractproperty
    def generator(self):
        pass

    @abc.abstractproperty
    def generator_bytes(self):
        pass

    @abc.abstractproperty
    def serialize(self):
        pass


class IncrementalDataFrameToRecArraySerializer(LazyIncrementalSerializer):
    def __init__(self, serializer, input_data, chunk_size=_CHUNK_SIZE, string_max_len=None):
        super(IncrementalDataFrameToRecArraySerializer, self).__init__(serializer, input_data, chunk_size)

        if not isinstance(input_data, pd.DataFrame):
            raise ArcticSerializationException("LazyIncrementalSerializer requires a pandas DataFrame "
                                               "as data source input.")
        
        if string_max_len and string_max_len < 1:
            raise ArcticSerializationException("LazyIncrementalSerializer can't be initialized "
                                               "with string_max_len < 1 ({})".format(string_max_len))

        self.string_max_len = string_max_len
        # The state which needs to be lazily initialized
        self._dtype = None
        self._rows_per_chunk = 0
        self._first_chunk = None

    def _lazy_init(self):
        if self._initialized:
            return

        # Serialize the first row to obtain info about row size in bytes (cache first row)
        # Also raise an Exception early, if data are not serializable
        first_chunk, dtype = self._serializer.serialize(self.original_df[0:1] if len(self) > 0 else self.original_df,
                                                        string_max_len=self.string_max_len)

        # Compute the number of rows which can fit in a chunk
        rows_per_chunk = 0
        if len(self) > 0 and self.chunk_size > 1:
            rows_per_chunk = self._calculate_rows_per_chunk(first_chunk)

        # Initialize object's state
        self._first_chunk = first_chunk
        self._dtype = dtype
        self._rows_per_chunk = rows_per_chunk
        self._initialized = True

    @staticmethod
    def _calculate_rows_per_chunk(max_chunk_size, chunk):
        sze = int(chunk.dtype.itemsize * np.prod(chunk.shape[1:]))
        sze = sze if sze < max_chunk_size else max_chunk_size
        rows_per_chunk = int(max_chunk_size / sze)
        if rows_per_chunk < 1:
            # If a row size is larger than chunk_size, use the maximum document size
            logging.warning('Chunk size of {} is too small to fit a row ({}). '
                            'Using maximum document size.'.format(max_chunk_size, MAX_DOCUMENT_SIZE))
            # For huge rows, fall-back to using a very large document size, less than max-allowed by MongoDB
            rows_per_chunk = int(MAX_DOCUMENT_SIZE / sze)
            if rows_per_chunk < 1:
                raise ArcticSerializationException("Serialization failed to split data into max sized chunks.")
        return rows_per_chunk

    def __len__(self):
        return len(self.input_data)

    @property
    def shape(self):
        return self.input_data.shape

    @property
    def dtype(self):
        self._lazy_init()
        return self._dtype

    @property
    def rows_per_chunk(self):
        self._lazy_init()
        return self._rows_per_chunk

    @property
    def generator(self):
        return self._generator()

    @property
    def generator_bytes(self):
        return self._generator(get_bytes=True)

    def _generator(self, get_bytes=False):
        self._lazy_init()

        if len(self) == 0:
            return

        # Compute the total number of chunks
        total_chunks = int(np.ceil(float(len(self)) / self._rows_per_chunk))

        # Perform serialization for each chunk
        for i in xrange(total_chunks):
            chunk, dtype = self._serializer.serialize(
                self.input_data[i * self._rows_per_chunk: (i + 1) * self._rows_per_chunk],
                string_max_len=self.string_max_len)
            # Let the gc collect the intermediate serialized chunk as early as possible
            chunk = chunk.tostring() if chunk is not None and get_bytes else chunk
            yield chunk, dtype

    def serialize(self):
        return self._serializer.serialize(self.input_data, self.string_max_len)
