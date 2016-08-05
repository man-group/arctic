import logging
import pymongo
import hashlib

from bson.binary import Binary
from pandas import concat, DataFrame, Series

from ..decorators import mongo_retry
from .._util import indent
from ..serialization.numpy_arrays import FrametoArraySerializer, DATA, VALUES, COLUMNS, TYPE

from .date_chunker import DateChunker, START, END
from ..exceptions import NoDataFoundException


logger = logging.getLogger(__name__)

CHUNK_STORE_TYPE = 'ChunkStoreV1'
SYMBOL = 'sy'
SHA = 'sh'
CHUNK_SIZE = 'cs'
CHUNK_COUNT = 'cc'
APPEND_COUNT = 'ac'
ROWS = 'r'


class ChunkStore(object):
    @classmethod
    def initialize_library(cls, arctic_lib, **kwargs):
        ChunkStore(arctic_lib)._ensure_index()

    @mongo_retry
    def _ensure_index(self):
        self._symbols.create_index([(SYMBOL, pymongo.ASCENDING)],
                                   unique=True,
                                   background=True)

        self._collection.create_index([(SYMBOL, pymongo.HASHED)],
                                      background=True)
        self._collection.create_index([(SYMBOL, pymongo.ASCENDING),
                                      (SHA, pymongo.ASCENDING)],
                                      unique=True,
                                      background=True)
        self._collection.create_index([(SYMBOL, pymongo.ASCENDING),
                                       (START, pymongo.ASCENDING),
                                       (END, pymongo.ASCENDING)],
                                      unique=True, background=True)

    @mongo_retry
    def __init__(self, arctic_lib, chunker=DateChunker(), serializer=FrametoArraySerializer()):
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

    def _checksum(self, doc):
        """
        Checksum the passed in dictionary
        """
        sha = hashlib.sha1()
        sha.update(self.chunker.chunk_to_str(doc[START]).encode('ascii'))
        sha.update(self.chunker.chunk_to_str(doc[END]).encode('ascii'))
        for k in doc[DATA][COLUMNS]:
            sha.update(doc[DATA][DATA][k][VALUES])
        return Binary(sha.digest())

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
            row_adjust = len(df)
            df = self.chunker.exclude(df, chunk_range)

            # remove chunks, and update any remaining data
            query = {SYMBOL: symbol}
            query.update(self.chunker.to_mongo(chunk_range))
            self._collection.delete_many(query)
            self.update(symbol, df)

            # update symbol metadata (rows and chunk count)
            sym = self._get_symbol_info(symbol)
            sym[ROWS] -= row_adjust
            sym[CHUNK_COUNT] = self._collection.count({SYMBOL: symbol})
            self._symbols.replace_one({SYMBOL: symbol}, sym)

        else:
            query = {SYMBOL: symbol}
            self._collection.delete_many(query)
            self._collection.symbols.delete_many(query)

    def list_symbols(self):
        """
        Returns all symbols in the library

        Returns
        -------
        list of str
        """
        return self._symbols.distinct(SYMBOL)

    def _get_symbol_info(self, symbol):
        return self._symbols.find_one({SYMBOL: symbol})

    def rename(self, from_symbol, to_symbol):
        """
        Rename a symbol

        Parameters
        ----------
        from_symbol: str
            the existing symbol that will be renamed
        to_symbol: str
            the new symbol name
        """

        sym = self._get_symbol_info(from_symbol)
        if not sym:
            raise NoDataFoundException('No data found for %s' % (from_symbol))

        if self._get_symbol_info(to_symbol) is not None:
            raise Exception('Symbol %s already exists' % (to_symbol))

        mongo_retry(self._collection.update_many)({SYMBOL: from_symbol},
                                                  {'$set': {SYMBOL: to_symbol}})

        mongo_retry(self._symbols.update_one)({SYMBOL: from_symbol},
                                              {'$set': {SYMBOL: to_symbol}})

    def read(self, symbol, chunk_range=None, columns=None, filter_data=True):
        """
        Reads data for a given symbol from the database.

        Parameters
        ----------
        symbol: str
            the symbol to retrieve
        chunk_range: object
            corresponding range object for the specified chunker (for
            DateChunker it is a DateRange object)
        columns: list of str
            subset of columns to read back (index will always be included, if
            one exists)
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

        spec = {SYMBOL: symbol,
                }

        if chunk_range:
            spec.update(self.chunker.to_mongo(chunk_range))

        segments = []
        for x in self._collection.find(spec, sort=[(START, pymongo.ASCENDING)],):
            segments.append(x[DATA])

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

        doc[SYMBOL] = symbol
        doc[CHUNK_SIZE] = chunk_size
        doc[ROWS] = len(item)
        doc[TYPE] = 'dataframe' if isinstance(item, DataFrame) else 'series'

        sym = self._get_symbol_info(symbol)
        if sym:
            previous_shas = set([Binary(x[SHA]) for x in self._collection.find({SYMBOL: symbol},
                                                                         projection={SHA: True, '_id': False},
                                                                         )])

        op = False
        bulk = self._collection.initialize_unordered_bulk_op()
        chunk_count = 0

        for start, end, record in self.chunker.to_chunks(item, chunk_size):
            chunk_count += 1
            data = self.serializer.serialize(record)
            doc[COLUMNS] = data[COLUMNS]

            chunk = {DATA: data}
            chunk[START] = start
            chunk[END] = end
            chunk[SYMBOL] = symbol
            chunk[SHA] = self._checksum(chunk)

            if chunk[SHA] not in previous_shas:
                op = True
                bulk.find({SYMBOL: symbol, START: start, END: end},
                          ).upsert().update_one({'$set': chunk})
            else:
                # already exists, dont need to update in mongo
                previous_shas.remove(chunk[SHA])

        if op:
            bulk.execute()

        doc[CHUNK_COUNT] = chunk_count
        doc[APPEND_COUNT] = 0

        if previous_shas:
            mongo_retry(self._collection.delete_many)({SYMBOL: symbol, SHA: {'$in': list(previous_shas)}})

        mongo_retry(self._symbols.update_one)({SYMBOL: symbol},
                                              {'$set': doc},
                                              upsert=True)

    def __concat(self, a, b):
        return concat([a, b]).sort_index()

    def __take_new(self, a, b):
        return a

    def __update(self, symbol, item, combine_method=None, chunk_range=None):
        if not isinstance(item, (DataFrame, Series)):
            raise Exception("Can only chunk DataFrames and Series")

        sym = self._get_symbol_info(symbol)
        if not sym:
            raise NoDataFoundException("Symbol does not exist.")

        if sym[TYPE] == 'series' and not isinstance(item, Series):
            raise Exception("Cannot combine Series and DataFrame")
        if sym[TYPE] == 'dataframe' and not isinstance(item, DataFrame):
            raise Exception("Cannot combine DataFrame and Series")

        if chunk_range:
            self.delete(symbol, chunk_range)
            sym = self._get_symbol_info(symbol)

        bulk = self._collection.initialize_unordered_bulk_op()
        op = False
        for start, end, record in self.chunker.to_chunks(item, sym[CHUNK_SIZE]):
            # read out matching chunks
            df = self.read(symbol, chunk_range=self.chunker.to_range(start, end), filter_data=False)

            # assuming they exist, update them and store the original chunk
            # range for later use
            if not df.empty:
                record = combine_method(record, df)
                if record is None or record.equals(df):
                    continue

                sym[APPEND_COUNT] += len(record)
                sym[ROWS] += len(record) - len(df)
                new_chunk = False
            else:
                new_chunk = True
                sym[CHUNK_COUNT] += 1
                sym[ROWS] += len(record)

            data = self.serializer.serialize(record)
            op = True

            chunk = {DATA: data}
            chunk[TYPE] = 'dataframe' if isinstance(record, DataFrame) else 'series'
            chunk[START] = start
            chunk[END] = end
            sha = self._checksum(chunk)
            chunk[SHA] = sha
            if new_chunk:
                # new chunk
                bulk.find({SYMBOL: symbol, SHA: sha}
                          ).upsert().update_one({'$set': chunk})
            else:
                bulk.find({SYMBOL: symbol, START: start, END: end}
                          ).update_one({'$set': chunk})

        if op:
            bulk.execute()

        self._symbols.replace_one({SYMBOL: symbol}, sym)

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

    def update(self, symbol, item, chunk_range=None):
        """
        Overwrites data in DB with data in item for the given symbol.

        Is idempotent

        Parameters
        ----------
        symbol: str
            the symbol for the given item in the DB
        item: DataFrame or Series
            the data to update
        chunk_range: None, or a range object
            If a range is specified, it will clear/delete the data within the
            range and overwrite it with the data in item. This allows the user
            to update with data that might only be a subset of the
            original data.
        """

        if chunk_range:
            if self.chunker.filter(item, chunk_range).empty:
                raise Exception('Range must be inclusive of data')
            self.__update(symbol, item, combine_method=self.__concat, chunk_range=chunk_range)
        else:
            self.__update(symbol, item, combine_method=self.__take_new, chunk_range=chunk_range)

    def get_info(self, symbol):
        sym = self._get_symbol_info(symbol)
        ret = {}
        ret['chunk_count'] = sym[CHUNK_COUNT]
        ret['rows'] = sym[ROWS]
        ret['col_names'] = sym[COLUMNS]
        return ret
