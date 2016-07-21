import logging
import pymongo
import numpy as np
import ast

from bson.binary import Binary
from pandas import concat, DataFrame, Series

from ..store._version_store_utils import checksum
from ..decorators import mongo_retry
from .._util import indent

from arctic.serialization.numpy_strings import NumpyString

from .date_chunker import DateChunker
from ..exceptions import NoDataFoundException


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
    def __init__(self, arctic_lib, chunker=DateChunker(), serializer=NumpyString()):
        self.chunker = chunker
        self.serializer = serializer
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
        symbol : str
            symbol name for the item
        chunk_range: range object
            a date range to delete
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

    def read(self, symbol, columns=None, chunk_range=None, filter_data=True):
        """
        Reads data for a given symbol from the database.

        Parameters
        ----------
        symbol: str
            the symbol to retrieve
        columns: list of str
            subset of columns to read back (index will always be included, if
            one exists)
        chunk_range: object
            corresponding range object for the specified chunker (for
            DateChunker it is a DateRange object)
        filter: boolean
            perform chunk level filtering on the data (see filter in _chunker)
            only applicable when chunk_range is specified

        Returns
        -------
        DataFrame or Series
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
            segments.append(x['data'])

        data = self.serializer.deserialize(segments, columns)

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
        item: Dataframe or Series
            the data to write the database
        chunk_size: ?
            A chunk size that is understood by the specified chunker
        """
        if not isinstance(item, (DataFrame, Series)):
            raise Exception("Can only chunk DataFrames and Series")

        previous_shas = []
        doc = {}

        doc['symbol'] = symbol
        doc['chunk_size'] = chunk_size
        doc['rows'] = len(item)
        doc['type'] = 'dataframe' if isinstance(item, DataFrame) else 'series'
        
        sym = self._get_symbol_info(symbol)
        if sym:
            previous_shas = set([Binary(x['sha']) for x in self._collection.find({'symbol': symbol},
                                                                         projection={'sha': True, '_id': False},
                                                                         )])

        op = False
        bulk = self._collection.initialize_unordered_bulk_op()
        chunk_count = 0

        for start, end, record in self.chunker.to_chunks(item, chunk_size):
            chunk_count += 1
            data = self.serializer.serialize(record)
            doc['col_names'] = data['columns']

            chunk = {'data': data}
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

        doc['chunk_count'] = chunk_count
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
        if not isinstance(item, (DataFrame, Series)):
            raise Exception("Can only chunk DataFrames and Series")

        sym = self._get_symbol_info(symbol)
        if not sym:
            raise NoDataFoundException("Symbol does not exist.")
        
        if sym['type'] == 'series' and not isinstance(item, Series):
            raise Exception("Cannot combine Series and DataFrame")
        if sym['type'] == 'dataframe' and not isinstance(item, DataFrame):
            raise Exception("Cannot combine DataFrame and Series")


        bulk = self._collection.initialize_unordered_bulk_op()
        op = False
        for start, end, record in self.chunker.to_chunks(item, sym['chunk_size']):
            # read out matching chunks
            df = self.read(symbol, chunk_range=self.chunker.to_range(start, end), filter_data=False)
            # assuming they exist, update them and store the original chunk
            # range for later use
            if not df.empty:
                record = combine_method(record, df)
                if record is None or record.equals(df):
                    continue

                sym['append_count'] += len(record)
                sym['rows'] += len(record) - len(df)
                new_chunk = False
            else:
                new_chunk = True
                sym['chunk_count'] += 1
                sym['rows'] += len(record)

            data = self.serializer.serialize(record)
            op = True

            segment = {'data': data}
            segment['type'] = 'dataframe' if isinstance(record, DataFrame) else 'series'
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

        if op:
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
        item: DataFrame or Series
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
        item: DataFrame or Series
            the data to update
        """

        self.__update(symbol, item, combine_method=self.__combine)

    def get_info(self, symbol):
        sym = self._get_symbol_info(symbol)
        ret = {}
        ret['chunk_count'] = sym['chunk_count']
        ret['rows'] = sym['rows']
        ret['col_names'] = sym['col_names']
        return ret
