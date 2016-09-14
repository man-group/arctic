import logging
import pymongo
import hashlib

from bson.binary import Binary
from bson import SON
from pandas import DataFrame, Series

from ..decorators import mongo_retry
from .._util import indent
from ..serialization.numpy_arrays import FrametoArraySerializer, DATA, TYPE, METADATA, COLUMNS
from .date_chunker import DateChunker, START, END
from .passthrough_chunker import PassthroughChunker

from ..exceptions import NoDataFoundException


logger = logging.getLogger(__name__)

CHUNK_STORE_TYPE = 'ChunkStoreV1'
SYMBOL = 'sy'
SHA = 'sh'
CHUNK_SIZE = 'cs'
CHUNK_COUNT = 'cc'
SEGMENT = 'sg'
APPEND_COUNT = 'ac'
LEN = 'l'
SERIALIZER = 'se'
CHUNKER = 'ch'

MAX_CHUNK_SIZE = 15 * 1024 * 1024

SER_MAP = {FrametoArraySerializer.TYPE: FrametoArraySerializer()}

CHUNKER_MAP = {DateChunker.TYPE: DateChunker(),
               PassthroughChunker.TYPE: PassthroughChunker()}


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
                                       (END, pymongo.ASCENDING),
                                       (SEGMENT, pymongo.ASCENDING)],
                                      unique=True, background=True)

    @mongo_retry
    def __init__(self, arctic_lib):
        self._arctic_lib = arctic_lib
        self.serializer = FrametoArraySerializer()

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

    def _checksum(self, fields, data):
        """
        Checksum the passed in dictionary
        """
        sha = hashlib.sha1()
        for field in fields:
            sha.update(field)
        sha.update(data)
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
        if chunk_range is not None:
            sym = self._get_symbol_info(symbol)
            # read out chunks that fall within the range and filter out
            # data within the range
            df = self.read(symbol, chunk_range=chunk_range, filter_data=False)
            row_adjust = len(df)
            df = CHUNKER_MAP[sym[CHUNKER]].exclude(df, chunk_range)

            # remove chunks, and update any remaining data
            query = {SYMBOL: symbol}
            query.update(CHUNKER_MAP[sym[CHUNKER]].to_mongo(chunk_range))
            self._collection.delete_many(query)
            self.update(symbol, df)

            # update symbol metadata (rows and chunk count)
            sym = self._get_symbol_info(symbol)
            sym[LEN] -= row_adjust
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

    def read(self, symbol, chunk_range=None, filter_data=True, **kwargs):
        """
        Reads data for a given symbol from the database.

        Parameters
        ----------
        symbol: str
            the symbol to retrieve
        chunk_range: object
            corresponding range object for the specified chunker (for
            DateChunker it is a DateRange object or a DatetimeIndex, 
            as returned by pandas.date_range
        filter_data: boolean
            perform chunk level filtering on the data (see filter in _chunker)
            only applicable when chunk_range is specified
        kwargs: ?
            values passed to the serializer. Varies by serializer

        Returns
        -------
        DataFrame or Series
        """

        sym = self._get_symbol_info(symbol)
        if not sym:
            raise NoDataFoundException('No data found for %s' % (symbol))

        spec = {SYMBOL: symbol,
                }

        if chunk_range is not None:
            spec.update(CHUNKER_MAP[sym[CHUNKER]].to_mongo(chunk_range))

        segments = []
        parts = []
        for x in self._collection.find(spec, sort=[(START, pymongo.ASCENDING), (SEGMENT, pymongo.ASCENDING)],):
            if x[SEGMENT] > -1:
                parts.append(x[DATA])
            else:
                if parts:
                    x[DATA] = b''.join(parts)
                    parts = []
                segments.append({DATA: x[DATA], METADATA: x[METADATA]})

        if parts:
            x[DATA] = b''.join(parts)
            segments.append({DATA: x[DATA], METADATA: x[METADATA]})


        data = SER_MAP[sym[SERIALIZER]].deserialize(segments, **kwargs)

        if not filter_data or chunk_range is None:
            return data
        return CHUNKER_MAP[sym[CHUNKER]].filter(data, chunk_range)

    def write(self, symbol, item, chunker=DateChunker(), **kwargs):
        """
        Writes data from item to symbol in the database

        Parameters
        ----------
        symbol: str
            the symbol that will be used to reference the written data
        item: Dataframe or Series
            the data to write the database
        chunker: Object of type Chunker
            A chunker that chunks the data in item
        kwargs:
            optional keyword args that are passed to the chunker. Includes:
            chunk_size:
                used by chunker to break data into discrete chunks.
                see specific chunkers for more information about this param.
        """
        if not isinstance(item, (DataFrame, Series)):
            raise Exception("Can only chunk DataFrames and Series")

        previous_shas = []
        doc = {}

        doc[SYMBOL] = symbol
        doc[LEN] = len(item)
        doc[SERIALIZER] = self.serializer.TYPE
        doc[CHUNKER] = chunker.TYPE

        sym = self._get_symbol_info(symbol)
        if sym:
            previous_shas = set([Binary(x[SHA]) for x in self._collection.find({SYMBOL: symbol},
                                                                         projection={SHA: True, '_id': False},
                                                                         )])

        op = False
        bulk = self._collection.initialize_unordered_bulk_op()
        chunk_count = 0

        for start, end, chunk_size, record in chunker.to_chunks(item, **kwargs):
            chunk_count += 1
            data = self.serializer.serialize(record)
            doc[METADATA] = {'columns': data[METADATA][COLUMNS] if COLUMNS in data[METADATA] else ''}
            doc[CHUNK_SIZE] = chunk_size

            size_chunked = len(data[DATA]) > MAX_CHUNK_SIZE
            for i in xrange(int(len(data[DATA]) / MAX_CHUNK_SIZE + 1)):
                chunk = {DATA: Binary(data[DATA][i * MAX_CHUNK_SIZE : (i + 1) * MAX_CHUNK_SIZE])}
                chunk[METADATA] = data[METADATA]
                if size_chunked:
                    chunk[SEGMENT] = i
                else:
                    chunk[SEGMENT] = -1
                chunk[START] = start
                chunk[END] = end
                chunk[SYMBOL] = symbol
                dates = [chunker.chunk_to_str(start), chunker.chunk_to_str(end)]
                chunk[SHA] = self._checksum(dates, chunk[DATA])
                if chunk[SHA] not in previous_shas:
                    op = True
                    find = {SYMBOL: symbol, START: start, END: end}
                    if size_chunked:
                        find[SEGMENT] = chunk[SEGMENT]
                    bulk.find(find,).upsert().update_one({'$set': chunk})
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

    def __replace(self, old, new):
        return new

    def __update(self, sym, item, combine_method=None, chunk_range=None):
        if not isinstance(item, (DataFrame, Series)):
            raise Exception("Can only chunk DataFrames and Series")

        symbol = sym[SYMBOL]

        if chunk_range is not None:
            self.delete(symbol, chunk_range)
            sym = self._get_symbol_info(symbol)

        bulk = self._collection.initialize_unordered_bulk_op()
        op = False
        chunker = CHUNKER_MAP[sym[CHUNKER]]
        for start, end, _, record in chunker.to_chunks(item, chunk_size=sym[CHUNK_SIZE]):
            # read out matching chunks
            df = self.read(symbol, chunk_range=chunker.to_range(start, end), filter_data=False)
            # assuming they exist, update them and store the original chunk
            # range for later use
            if len(df) > 0:
                record = combine_method(df, record)
                if record is None or record.equals(df):
                    continue

                sym[APPEND_COUNT] += len(record)
                sym[LEN] += len(record) - len(df)
                new_chunk = False
            else:
                new_chunk = True
                sym[CHUNK_COUNT] += 1
                sym[LEN] += len(record)

            data = SER_MAP[sym[SERIALIZER]].serialize(record)
            op = True

            chunk = {DATA: Binary(data[DATA])}
            chunk[METADATA] = data[METADATA]
            chunk[START] = start
            chunk[END] = end
            chunk[SYMBOL] = symbol
            chunk[SEGMENT] = -1
            dates = [chunker.chunk_to_str(start), chunker.chunk_to_str(end)]
            sha = self._checksum(dates, data[DATA])
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
        sym = self._get_symbol_info(symbol)
        if not sym:
            raise NoDataFoundException("Symbol does not exist.")
        self.__update(sym, item, combine_method=SER_MAP[sym[SERIALIZER]].combine)

    def update(self, symbol, item, chunk_range=None, upsert=False, **kwargs):
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
        upsert: bool
            if True, will write the data even if the symbol does not exist.
        kwargs:
            optional keyword args passed to write during an upsert. Includes:
            chunk_size
            chunker
        """
        sym = self._get_symbol_info(symbol)
        if not sym:
            if upsert:
                return self.write(symbol, item, **kwargs)
            else:
                raise NoDataFoundException("Symbol does not exist.")
        if chunk_range is not None:
            if len(CHUNKER_MAP[sym[CHUNKER]].filter(item, chunk_range)) == 0:
                raise Exception('Range must be inclusive of data')
            self.__update(sym, item, combine_method=self.serializer.combine, chunk_range=chunk_range)
        else:
            self.__update(sym, item, combine_method=self.__replace, chunk_range=chunk_range)

    def get_info(self, symbol):
        sym = self._get_symbol_info(symbol)
        ret = {}
        ret['chunk_count'] = sym[CHUNK_COUNT]
        ret['len'] = sym[LEN]
        ret['metadata'] = sym[METADATA]
        return ret
