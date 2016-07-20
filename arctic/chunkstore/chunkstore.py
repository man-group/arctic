import logging
import pymongo
import numpy as np
import ast

from bson.binary import Binary
from pandas import Series, DataFrame, concat

from ..store._version_store_utils import checksum
from ..decorators import mongo_retry
from .._util import indent
from ..serialization.pandas_serializer import (serialize, deserialize,
                                               DataFrameSerializer,
                                               SeriesSerializer,
                                               PandasSerializer)
from .date_chunker import DateChunker
from ..exceptions import UnhandledDtypeException, NoDataFoundException
from .._compression import compress_array, decompress


logger = logging.getLogger(__name__)

CHUNK_STORE_TYPE = 'ChunkStoreV1'


class ChunkStore(object):
    STRING_MAX = 16

    @classmethod
    def initialize_library(cls, arctic_lib, **kwargs):
        ChunkStore(arctic_lib)._ensure_index()

    @mongo_retry
    def _ensure_index(self):
        self._symbols.create_index([("symbol", pymongo.ASCENDING)],
                                   unique=True,
                                   background=True)

        self._collection.create_index([('symbol', pymongo.HASHED)],
                                      background=True)
        self._collection.create_index([('symbol', pymongo.ASCENDING),
                                      ('sha', pymongo.ASCENDING)],
                                      unique=True,
                                      background=True)
        self._collection.create_index([('symbol', pymongo.ASCENDING),
                                       ('start', pymongo.ASCENDING),
                                       ('end', pymongo.ASCENDING)],
                                      unique=True, background=True)

    @mongo_retry
    def __init__(self, arctic_lib, chunker=DateChunker()):
        self.chunker = chunker
        self._arctic_lib = arctic_lib

        # Do we allow reading from secondaries
        self._allow_secondary = self._arctic_lib.arctic._allow_secondary

        # The default collection
        self._collection = arctic_lib.get_top_level_collection()
        self._symbols = self._collection.symbols

    def __getstate__(self):
        return {'arctic_lib': self._arctic_lib}

    def __setstate__(self, state):
        return ChunkStore.__init__(self, state['arctic_lib'])

    def __str__(self):
        return """<%s at %s>\n%s""" % (self.__class__.__name__, hex(id(self)),
                                       indent(str(self._arctic_lib), 4))

    def __repr__(self):
        return str(self)

    def delete(self, symbol, chunk_range=None):
        """
        Delete all chunks for a symbol, or optionally, chunks within a range

        Parameters
        ----------
        symbol : `str`
            symbol name for the item
        """
        if chunk_range:
            # read out chunks that fall within the range and filter out
            # data within the range
            df = self.read(symbol, chunk_range=chunk_range, filter_data=False)
            df = self.chunker.exclude(df, chunk_range)

            # remove chunks, and update any remaining data
            query = {'symbol': symbol}
            query.update(self.chunker.to_mongo(chunk_range))
            self._collection.delete_many(query)
            self.update(symbol, df)

        else:
            query = {"symbol": symbol}
            self._collection.delete_many(query)
            self._collection.symbols.delete_many(query)

    def list_symbols(self):
        """
        Returns all symbols in the library

        Returns
        -------
        list of str
        """
        return self._symbols.distinct("symbol")

    def _get_symbol_info(self, symbol):
        return self._symbols.find_one({'symbol': symbol})

    def read(self, symbol, chunk_range=None, filter_data=True):
        """
        Reads data for a given symbol from the database.

        Parameters
        ----------
        symbol: str
            the symbol to retrieve
        chunk_range: object
            corresponding range object for the specified chunker (for
            DateChunker it is a DateRange object)
        filter: boolean
            perform chunk level filtering on the data (see filter() in _chunker)
            only applicable when chunk_range is specified

        Returns
        -------
        A dataframe or series
        """

        sym = self._get_symbol_info(symbol)
        if not sym:
            raise NoDataFoundException('No data found for %s' % (symbol))

        spec = {'symbol': symbol,
                }

        if chunk_range:
            spec.update(self.chunker.to_mongo(chunk_range))

        segments = []
        for _, x in enumerate(self._collection.find(spec, sort=[('start', pymongo.ASCENDING)],)):
            segments.append(decompress(x['data']))

        data = b''.join(segments)

        dtype = PandasSerializer._dtype(sym['dtype'], sym.get('dtype_metadata', {}))
        records = np.fromstring(data, dtype=dtype).reshape(sym.get('shape', (-1)))

        data = deserialize(records, sym['type'])

        if not filter_data or chunk_range is None:
            return data
        return self.chunker.filter(data, chunk_range)

    def write(self, symbol, item, chunk_size):
        """
        Writes data from item to symbol in the database

        Parameters
        ----------
        symbol: str
            the symbol that will be used to reference the written data
        item: dataframe or series
            the data to write the database
        chunk_size: ?
            A chunk size that is understood by the specified chunker
        """

        doc = {}
        doc['symbol'] = symbol
        doc['chunk_size'] = chunk_size

        if isinstance(item, Series):
            doc['type'] = SeriesSerializer.TYPE
        elif isinstance(item, DataFrame):
            doc['type'] = DataFrameSerializer.TYPE
        else:
            raise Exception("Can only chunk Series and DataFrames")

        previous_shas = []
        sym = self._get_symbol_info(symbol)
        if sym:
            previous_shas = set([Binary(x['sha']) for x in self._collection.find({'symbol': symbol},
                                                                         projection={'sha': True, '_id': False},
                                                                         )])
        records = []
        ranges = []
        dtype = None

        for start, end, record in self.chunker.to_chunks(item, chunk_size):
            r, dtype = serialize(record, string_max_len=self.STRING_MAX)
            # if symbol exists, dtypes better match
            if sym and str(dtype) != sym['dtype']:
                raise Exception('Dtype mismatch - cannot write chunk')
            records.append(r)
            ranges.append((start, end))

        item = np.array([r for record in records for r in record]).flatten()
        for record in records:
            if record.dtype.hasobject:
                raise UnhandledDtypeException()

        doc['dtype'] = str(dtype)
        doc['shape'] = (-1,) + item.shape[1:]
        doc['dtype_metadata'] = dict(dtype.metadata or {})
        doc['len'] = len(item)

        chunks = [r.tostring() for r in records]
        chunks = compress_array(chunks)

        op = False
        bulk = self._collection.initialize_unordered_bulk_op()
        for chunk, rng in zip(chunks, ranges):
            start = rng[0]
            end = rng[1]
            chunk = {'data': Binary(chunk)}
            chunk['start'] = start
            chunk['end'] = end
            chunk['symbol'] = symbol
            chunk['sha'] = checksum(symbol, chunk)

            if chunk['sha'] not in previous_shas:
                op = True
                bulk.find({'symbol': symbol, 'start': start, 'end': end},
                          ).upsert().update_one({'$set': chunk})
            else:
                # already exists, dont need to update in mongo
                previous_shas.remove(chunk['sha'])

        if op:
            bulk.execute()

        doc['chunk_count'] = len(chunks)
        doc['append_size'] = 0
        doc['append_count'] = 0

        if previous_shas:
            mongo_retry(self._collection.delete_many)({'symbol': symbol, 'sha': {'$in': list(previous_shas)}})

        mongo_retry(self._symbols.update_one)({'symbol': symbol},
                                              {'$set': doc},
                                              upsert=True)

    def __concat(self, a, b):
        return concat([a, b]).sort()

    def __combine(self, a, b):
        return a.combine_first(b)

    def __update(self, symbol, item, combine_method=None):
        sym = self._get_symbol_info(symbol)
        if not sym:
            raise NoDataFoundException("Symbol does not exist.")

        if isinstance(item, Series) and sym['type'] == 'df':
            raise Exception("Symbol types do not match")
        if isinstance(item, DataFrame) and sym['type'] == 'series':
            raise Exception("Symbol types do not match")

        records = []
        ranges = []
        new_chunks = []
        for start, end, record in self.chunker.to_chunks(item, sym['chunk_size']):
            # read out matching chunks
            df = self.read(symbol, chunk_range=self.chunker.to_range(start, end), filter_data=False)
            # assuming they exist, update them and store the original chunk
            # range for later use
            if not df.empty:
                record = combine_method(record, df)
                if record is None or record.equals(df):
                    continue

                new_chunks.append(False)
                sym['append_count'] += len(record)
                sym['len'] -= len(df)
            else:
                new_chunks.append(True)
                sym['chunk_count'] += 1

            r, dtype = serialize(record, string_max_len=self.STRING_MAX)
            if str(dtype) != sym['dtype']:
                raise Exception('Dtype mismatch.')
            records.append(r)
            ranges.append((start, end))

        if len(records) > 0:
            item = np.array([r for record in records for r in record]).flatten()

            if sym.get('shape', [-1]) != [-1, ] + list(item.shape)[1:]:
                raise UnhandledDtypeException()

            item = item.astype(dtype)

            data = item.tostring()
            sym['len'] += len(item)
            if len(item) > 0:
                sym['append_size'] += len(data)

            chunks = [r.tostring() for r in records]
            chunks = compress_array(chunks)

            bulk = self._collection.initialize_unordered_bulk_op()
            for chunk, rng, new_chunk in zip(chunks, ranges, new_chunks):
                start = rng[0]
                end = rng[1]

                segment = {'data': Binary(chunk)}
                segment['start'] = start
                segment['end'] = end
                sha = checksum(symbol, segment)
                segment['sha'] = sha
                if new_chunk:
                    # new chunk
                    bulk.find({'symbol': symbol, 'sha': sha}
                              ).upsert().update_one({'$set': segment})
                else:
                    bulk.find({'symbol': symbol, 'start': start, 'end': end}
                              ).update_one({'$set': segment})
            if len(chunks) > 0:
                    bulk.execute()

            self._symbols.replace_one({'symbol': symbol}, sym)

    def append(self, symbol, item):
        """
        Appends data from item to symbol's data in the database.

        Is not idempotent

        Parameters
        ----------
        symbol: str
            the symbol for the given item in the DB
        item:
            the data to append
        """
        self.__update(symbol, item, combine_method=self.__concat)

    def update(self, symbol, item):
        """
        Merges data from item onto existing data in the database for symbol
        data that exists in symbol and item for the same index/multiindex will
        be overwritten by the data in item.

        Is idempotent

        Parameters
        ----------
        symbol: str
            the symbol for the given item in the DB
        item:
            the data to update
        """

        self.__update(symbol, item, combine_method=self.__combine)

    def get_info(self, symbol):
        sym = self._get_symbol_info(symbol)
        ret = {}
        dtype = PandasSerializer._dtype(sym['dtype'], sym['dtype_metadata'])
        length = sym['len']
        ret['size'] = dtype.itemsize * length
        ret['chunk_count'] = sym['chunk_count']
        ret['dtype'] = sym['dtype']
        ret['type'] = sym['type']
        ret['rows'] = length
        ret['col_names'] = sym['dtype_metadata']
        ret['dtype'] = ast.literal_eval(sym['dtype'])
        return ret
