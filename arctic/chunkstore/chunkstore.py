import logging
import pymongo
import numpy as np
import bson

from bson.binary import Binary
from pandas import Series, DataFrame

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

    def delete(self, symbol):
        """
        Delete all chunks for a symbol.

        Parameters
        ----------
        symbol : `str`
            symbol name for the item
        """
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

    def read(self, symbol, chunk_range=None):
        """
        Reads data for a given symbol from the database.

        Parameters
        ----------
        symbol: str
            the symbol to retrieve
        chunk_range: object
            corresponding range object for the specified chunker (for
            DateChunker it is a DateRange object)

        Returns
        -------
        A dataframe or series
        """

        sym = self._get_symbol_info(symbol)
        if not sym:
            raise NoDataFoundException('No data found for %s in library %s' % (symbol, self._collection.get_name()))

        spec = {'symbol': symbol,
                }

        if chunk_range:
            spec['start'] = self.chunker.to_mongo(chunk_range)

        segments = []
        for _, x in enumerate(self._collection.find(spec, sort=[('start', pymongo.ASCENDING)],)):
            segments.append(decompress(x['data']))

        data = b''.join(segments)

        dtype = PandasSerializer()._dtype(sym['dtype'], sym.get('dtype_metadata', {}))
        records = np.fromstring(data, dtype=dtype).reshape(sym.get('shape', (-1)))

        data = deserialize(records, sym['type'])

        if chunk_range is None:
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
        if self._get_symbol_info(symbol):
            previous_shas = set([Binary(x['sha']) for x in self._collection.find({'symbol': symbol},
                                                                         projection={'sha': True, '_id': False},
                                                                         )])
        records = []
        ranges = []
        dtype = None

        for start, end, record in self.chunker.to_chunks(item, chunk_size):
            r, dtype = serialize(record, string_max_len=self.STRING_MAX)
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
                bulk.find({'symbol': symbol, 'sha': chunk['sha']},
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
            mongo_retry(self._collection.delete_many)({'sha': {'$in': list(previous_shas)}})

        mongo_retry(self._symbols.update_one)({'symbol': symbol},
                                              {'$set': doc},
                                              upsert=True)

    def append(self, symbol, item):
        """
        Appends data from item to symbol's data in the database

        Parameters
        ----------
        symbol: str
            the symbol for the given item in the DB
        item:
            the data to append
        """

        sym = self._get_symbol_info(symbol)
        if not sym:
            raise NoDataFoundException("Symbol does not exist. Cannot append")

        if isinstance(item, Series) and sym['type'] == 'df':
            raise Exception("cannot append a series to a dataframe")
        if isinstance(item, DataFrame) and sym['type'] == 'series':
            raise Exception("cannot append a dataframe to a series")

        records = []
        ranges = []
        dtype = None

        for start, end, record in self.chunker.to_chunks(item, sym['chunk_size']):
            '''
            if we have a multiindex there is a chance that part of the append
            will overlap an already written chunk, so we need to update
            where the date part of the index overlaps
            '''
            if item.index.nlevels > 1:
                df = self.read(symbol, chunk_range=self.chunker.to_range(start, end))
                if not df.empty:
                    if df.equals(record):
                        continue
                    record = record.combine_first(df)
                    self.update(symbol, record)
                    sym = self._get_symbol_info(symbol)
                    continue
            r, dtype = serialize(record, string_max_len=self.STRING_MAX)
            records.append(r)
            ranges.append((start, end))

        if len(records) > 0:
            item = np.array([r for record in records for r in record]).flatten()

            if sym.get('shape', [-1]) != [-1, ] + list(item.shape)[1:]:
                raise UnhandledDtypeException()

            item = item.astype(dtype)

            if str(dtype) != sym['dtype']:
                raise Exception("Dtype mismatch - cannot append")

            data = item.tostring()
            sym['len'] += len(item)
            if len(item) > 0:
                sym['chunk_count'] += len(records)
                sym['append_count'] += len(records)
                sym['append_size'] += len(data)

            chunks = [r.tostring() for r in records]
            chunks = compress_array(chunks)

            for chunk, rng in zip(chunks, ranges):
                start = rng[0]
                end = rng[-1]

                segment = {'data': Binary(chunk)}
                segment['start'] = start
                segment['end'] = end
                self._collection.update_one({'symbol': symbol, 'sha': checksum(symbol, segment)},
                                            {'$set': segment},
                                            upsert=True)

            self._symbols.replace_one({'symbol': symbol}, sym)

    def update(self, symbol, item):
        """
        Merges data from item onto existing data in the database for symbol
        data that exists in symbol and item for the same index/multiindex will
        be overwritten by the data in item.

        Parameters
        ----------
        symbol: str
            the symbol for the given item in the DB
        item:
            the data to update
        """

        sym = self._get_symbol_info(symbol)
        if not sym:
            raise NoDataFoundException("Symbol does not exist. Cannot update")

        records = []
        ranges = []
        orig_ranges = []
        for start, end, record in self.chunker.to_chunks(item, sym['chunk_size']):
            # read out matching chunks
            df = self.read(symbol, chunk_range=self.chunker.to_range(start, end))
            # assuming they exist, update them and store the original chunk
            # range for later use
            if not df.empty:
                if df.equals(record):
                    continue
                record = record.combine_first(df)
                orig_ranges.append((self.chunker.to_start_end(record)))
            else:
                orig_ranges.append((None, None))

            r, _ = serialize(record, string_max_len=self.STRING_MAX)
            records.append(r)
            ranges.append((start, end))

        if len(records) > 0:
            chunks = [r.tostring() for r in records]
            lens = [len(i) for i in chunks]
            chunks = compress_array(chunks)

            seg_count = 0
            seg_len = 0

            bulk = self._collection.initialize_unordered_bulk_op()
            for chunk, rng, orig_rng, rec_len in zip(chunks, ranges, orig_ranges, lens):
                start = rng[0]
                end = rng[1]
                orig_start = orig_rng[0]
                if orig_start is None:
                    sym['len'] += rec_len
                    seg_count += 1
                    seg_len += rec_len
                segment = {'data': Binary(chunk)}
                segment['start'] = start
                segment['end'] = end
                sha = checksum(symbol, segment)
                segment['sha'] = sha
                if orig_start is None:
                    # new chunk
                    bulk.find({'symbol': symbol, 'sha': sha, 'start': segment['start']}
                              ).upsert().update_one({'$set': segment})
                else:
                    bulk.find({'symbol': symbol, 'start': orig_start}
                              ).update_one({'$set': segment})
            if len(chunks) > 0:
                    bulk.execute()

            if seg_count != 0:
                sym['chunk_count'] += seg_count
                sym['append_size'] += seg_len
                sym['append_count'] += seg_count
            self._symbols.replace_one({'symbol': symbol}, sym)
