import logging
import pymongo
import hashlib
import bson

from bson.binary import Binary
from pandas import DataFrame, Series
from six.moves import xrange
from itertools import groupby
from pymongo.errors import OperationFailure

from ..decorators import mongo_retry
from .._util import indent
from ..serialization.numpy_arrays import FrametoArraySerializer, DATA, METADATA, COLUMNS
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
USERMETA = 'u'

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
        self._collection.create_index([(SYMBOL, pymongo.ASCENDING),
                                       (START, pymongo.ASCENDING),
                                       (SEGMENT, pymongo.ASCENDING)],
                                      unique=True, background=True)
        self._mdata.create_index([(SYMBOL, pymongo.ASCENDING),
                                  (START, pymongo.ASCENDING),
                                  (END, pymongo.ASCENDING)],
                                 unique=True, background=True)

    def __init__(self, arctic_lib):
        self._arctic_lib = arctic_lib
        self.serializer = FrametoArraySerializer()

        # Do we allow reading from secondaries
        self._allow_secondary = self._arctic_lib.arctic._allow_secondary
        self._reset()

    @mongo_retry
    def _reset(self):
        # The default collection
        self._collection = self._arctic_lib.get_top_level_collection()
        self._symbols = self._collection.symbols
        self._mdata = self._collection.metadata
        self._audit = self._collection.audit

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

    def delete(self, symbol, chunk_range=None, audit=None):
        """
        Delete all chunks for a symbol, or optionally, chunks within a range

        Parameters
        ----------
        symbol : str
            symbol name for the item
        chunk_range: range object
            a date range to delete
        audit: dict
            dict to store in the audit log
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
            self._mdata.delete_many(query)
            self.update(symbol, df)

            # update symbol metadata (rows and chunk count)
            sym = self._get_symbol_info(symbol)
            sym[LEN] -= row_adjust
            sym[CHUNK_COUNT] = self._collection.count({SYMBOL: symbol})
            self._symbols.replace_one({SYMBOL: symbol}, sym)

        else:
            query = {SYMBOL: symbol}
            self._collection.delete_many(query)
            self._symbols.delete_many(query)
            self._mdata.delete_many(query)
        
        if audit is not None:
            audit['symbol'] = symbol
            if chunk_range is not None:
                audit['rows_deleted'] = row_adjust
                audit['action'] = 'range delete'
            else:
                audit['action'] = 'symbol delete'
            
            self._audit.insert_one(audit)

    def list_symbols(self, partial_match=None):
        """
        Returns all symbols in the library

        Parameters
        ----------
        partial: None or str
            if not none, use this string to do a partial match on symbol names

        Returns
        -------
        list of str
        """
        symbols = self._symbols.distinct(SYMBOL)
        if partial_match is None:
            return symbols
        return [x for x in symbols if partial_match in x]

    def _get_symbol_info(self, symbol):
        return self._symbols.find_one({SYMBOL: symbol})

    def rename(self, from_symbol, to_symbol, audit=None):
        """
        Rename a symbol

        Parameters
        ----------
        from_symbol: str
            the existing symbol that will be renamed
        to_symbol: str
            the new symbol name
        audit: dict
            audit information
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
        mongo_retry(self._mdata.update_many)({SYMBOL: from_symbol},
                                             {'$set': {SYMBOL: to_symbol}})
        mongo_retry(self._audit.update_many)({'symbol': from_symbol},
                                             {'$set': {'symbol': to_symbol}})
        if audit is not None:
            audit['symbol'] = to_symbol
            audit['action'] = 'symbol rename'
            audit['old_symbol'] = from_symbol
            self._audit.insert_one(audit)
        

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

        by_start_segment = [(START, pymongo.ASCENDING),
                            (SEGMENT, pymongo.ASCENDING)]
        segment_cursor = self._collection.find(spec, sort=by_start_segment)

        chunks = []
        for _, segments in groupby(segment_cursor, key=lambda x: x[START]):
            segments = list(segments)
            mdata = self._mdata.find_one({SYMBOL: symbol, START: segments[0][START], END: segments[0][END]})

            # when len(segments) == 1, this is essentially a no-op
            # otherwise, take all segments and reassemble the data to one chunk
            chunk_data = b''.join([doc[DATA] for doc in segments])

            chunks.append({DATA: chunk_data, METADATA: mdata})

        data = SER_MAP[sym[SERIALIZER]].deserialize(chunks, **kwargs)

        if not filter_data or chunk_range is None:
            return data
        return CHUNKER_MAP[sym[CHUNKER]].filter(data, chunk_range)
    
    def read_audit_log(self, symbol=None):
        """
        Reads the audit log
        
        Parameters
        ----------
        symbol: str
            optionally only retrieve specific symbol's audit information
            
        Returns
        -------
        list of dicts
        """
        if symbol:
            return [x for x in self._audit.find({'symbol': symbol}, {'_id': False})]
        return [x for x in self._audit.find({}, {'_id': False})]

    def write(self, symbol, item, metadata=None, chunker=DateChunker(), audit=None, **kwargs):
        """
        Writes data from item to symbol in the database

        Parameters
        ----------
        symbol: str
            the symbol that will be used to reference the written data
        item: Dataframe or Series
            the data to write the database
        metadata: ?
            optional per symbol metadata
        chunker: Object of type Chunker
            A chunker that chunks the data in item
        audit: dict
            audit information
        kwargs:
            optional keyword args that are passed to the chunker. Includes:
            chunk_size:
                used by chunker to break data into discrete chunks.
                see specific chunkers for more information about this param.
        """
        if not isinstance(item, (DataFrame, Series)):
            raise Exception("Can only chunk DataFrames and Series")

        self._arctic_lib.check_quota()

        previous_shas = []
        doc = {}
        meta = {}

        doc[SYMBOL] = symbol
        doc[LEN] = len(item)
        doc[SERIALIZER] = self.serializer.TYPE
        doc[CHUNKER] = chunker.TYPE
        doc[USERMETA] = metadata

        sym = self._get_symbol_info(symbol)
        if sym:
            previous_shas = set([Binary(x[SHA]) for x in self._collection.find({SYMBOL: symbol},
                                                                               projection={SHA: True, '_id': False},
                                                                               )])
        op = False
        bulk = self._collection.initialize_unordered_bulk_op()
        meta_bulk = self._mdata.initialize_unordered_bulk_op()
        chunk_count = 0

        for start, end, chunk_size, record in chunker.to_chunks(item, **kwargs):
            chunk_count += 1
            data = self.serializer.serialize(record)
            doc[CHUNK_SIZE] = chunk_size
            doc[METADATA] = {'columns': data[METADATA][COLUMNS] if COLUMNS in data[METADATA] else ''}
            meta = data[METADATA]

            size_chunked = len(data[DATA]) > MAX_CHUNK_SIZE
            for i in xrange(int(len(data[DATA]) / MAX_CHUNK_SIZE + 1)):
                chunk = {DATA: Binary(data[DATA][i * MAX_CHUNK_SIZE: (i + 1) * MAX_CHUNK_SIZE])}
                if size_chunked:
                    chunk[SEGMENT] = i
                else:
                    chunk[SEGMENT] = -1
                chunk[START] = start
                chunk[END] = end
                chunk[SYMBOL] = symbol
                dates = [chunker.chunk_to_str(start), chunker.chunk_to_str(end), str(chunk[SEGMENT]).encode('ascii')]
                chunk[SHA] = self._checksum(dates, chunk[DATA])
                if chunk[SHA] not in previous_shas:
                    op = True
                    find = {SYMBOL: symbol,
                            START: start,
                            END: end,
                            SEGMENT: chunk[SEGMENT]}
                    bulk.find(find).upsert().update_one({'$set': chunk})
                    meta_bulk.find({SYMBOL: symbol,
                                    START: start,
                                    END: end}).upsert().update_one({'$set': meta})
                else:
                    # already exists, dont need to update in mongo
                    previous_shas.remove(chunk[SHA])
        if op:
            bulk.execute()
            meta_bulk.execute()

        doc[CHUNK_COUNT] = chunk_count
        doc[APPEND_COUNT] = 0

        if previous_shas:
            mongo_retry(self._collection.delete_many)({SYMBOL: symbol, SHA: {'$in': list(previous_shas)}})

        mongo_retry(self._symbols.update_one)({SYMBOL: symbol},
                                              {'$set': doc},
                                              upsert=True)
        if audit is not None:
            audit['symbol'] = symbol
            audit['action'] = 'write'
            audit['chunks'] = chunk_count
            self._audit.insert_one(audit)

    def __update(self, sym, item, metadata=None, combine_method=None, chunk_range=None, audit=None):
        '''
        helper method used by update and append since they very closely
        resemble eachother. Really differ only by the combine method.
        append will combine existing date with new data (within a chunk),
        whereas update will replace existing data with new data (within a
        chunk).
        '''
        if not isinstance(item, (DataFrame, Series)):
            raise Exception("Can only chunk DataFrames and Series")

        self._arctic_lib.check_quota()

        symbol = sym[SYMBOL]

        if chunk_range is not None:
            self.delete(symbol, chunk_range)
            sym = self._get_symbol_info(symbol)

        bulk = self._collection.initialize_unordered_bulk_op()
        meta_bulk = self._mdata.initialize_unordered_bulk_op()
        op = False
        chunker = CHUNKER_MAP[sym[CHUNKER]]

        appended = 0
        new_chunks = 0
        for start, end, _, record in chunker.to_chunks(item, chunk_size=sym[CHUNK_SIZE]):
            # read out matching chunks
            df = self.read(symbol, chunk_range=chunker.to_range(start, end), filter_data=False)
            # assuming they exist, update them and store the original chunk
            # range for later use
            if len(df) > 0:
                record = combine_method(df, record)
                if record is None or record.equals(df):
                    continue

                sym[APPEND_COUNT] += len(record) - len(df)
                appended += len(record) - len(df)
                sym[LEN] += len(record) - len(df)
            else:
                sym[CHUNK_COUNT] += 1
                new_chunks += 1
                sym[LEN] += len(record)

            data = SER_MAP[sym[SERIALIZER]].serialize(record)
            meta = data[METADATA]
            op = True

            # remove old segments for this chunk in case we now have less
            # segments than we did before

            chunk_count = int(len(data[DATA]) / MAX_CHUNK_SIZE + 1)
            seg_count = self._collection.count({SYMBOL: symbol, START: start, END: end})
            if seg_count > chunk_count:
                # if chunk count is 1, the segment id will be -1, not 1
                self._collection.delete_many({SYMBOL: symbol,
                                              START: start,
                                              END: end,
                                              SEGMENT: {'$gt': seg_count if chunk_count > 1 else -1}})

            size_chunked = chunk_count > 1
            for i in xrange(chunk_count):
                chunk = {DATA: Binary(data[DATA][i * MAX_CHUNK_SIZE: (i + 1) * MAX_CHUNK_SIZE])}
                if size_chunked:
                    chunk[SEGMENT] = i
                else:
                    chunk[SEGMENT] = -1
                chunk[START] = start
                chunk[END] = end
                chunk[SYMBOL] = symbol
                dates = [chunker.chunk_to_str(start), chunker.chunk_to_str(end), str(chunk[SEGMENT]).encode('ascii')]
                sha = self._checksum(dates, data[DATA])
                chunk[SHA] = sha
                bulk.find({SYMBOL: symbol,
                           START: start,
                           END: end,
                           SEGMENT: chunk[SEGMENT]}).upsert().update_one({'$set': chunk})
                meta_bulk.find({SYMBOL: symbol,
                                START: start,
                                END: end}).upsert().update_one({'$set': meta})

        if op:
            bulk.execute()
            meta_bulk.execute()

        sym[USERMETA] = metadata
        self._symbols.replace_one({SYMBOL: symbol}, sym)
        if audit is not None:
            if new_chunks > 0:
                audit['new_chunks'] = new_chunks
            if appended > 0:
                audit['appended_rows'] = appended
            self._audit.insert_one(audit)

    def append(self, symbol, item, metadata=None, audit=None):
        """
        Appends data from item to symbol's data in the database.

        Is not idempotent

        Parameters
        ----------
        symbol: str
            the symbol for the given item in the DB
        item: DataFrame or Series
            the data to append
        metadata: ?
            optional per symbol metadata
        audit: dict
            optional audit information
        """
        sym = self._get_symbol_info(symbol)
        if not sym:
            raise NoDataFoundException("Symbol does not exist.")
        if audit is not None:
            audit['symbol'] = symbol
            audit['action'] = 'append'
        self.__update(sym, item, metadata=metadata, combine_method=SER_MAP[sym[SERIALIZER]].combine, audit=audit)

    def update(self, symbol, item, metadata=None, chunk_range=None, upsert=False, audit=None, **kwargs):
        """
        Overwrites data in DB with data in item for the given symbol.

        Is idempotent

        Parameters
        ----------
        symbol: str
            the symbol for the given item in the DB
        item: DataFrame or Series
            the data to update
        metadata: ?
            optional per symbol metadata
        chunk_range: None, or a range object
            If a range is specified, it will clear/delete the data within the
            range and overwrite it with the data in item. This allows the user
            to update with data that might only be a subset of the
            original data.
        upsert: bool
            if True, will write the data even if the symbol does not exist.
        audit: dict
            optional audit information
        kwargs:
            optional keyword args passed to write during an upsert. Includes:
            chunk_size
            chunker
        """
        sym = self._get_symbol_info(symbol)
        if not sym:
            if upsert:
                return self.write(symbol, item, metadata=metadata, audit=audit, **kwargs)
            else:
                raise NoDataFoundException("Symbol does not exist.")
        if audit is not None:
            audit['symbol'] = symbol
            audit['action'] = 'update'
        if chunk_range is not None:
            if len(CHUNKER_MAP[sym[CHUNKER]].filter(item, chunk_range)) == 0:
                raise Exception('Range must be inclusive of data')
            self.__update(sym, item, metadata=metadata, combine_method=self.serializer.combine, chunk_range=chunk_range, audit=audit)
        else:
            self.__update(sym, item, metadata=metadata, combine_method=lambda old, new: new, chunk_range=chunk_range, audit=audit)

    def get_info(self, symbol):
        """
        Returns information about the symbol, in a dictionary

        Parameters
        ----------
        symbol: str
            the symbol for the given item in the DB

        Returns
        -------
        dictionary
        """
        sym = self._get_symbol_info(symbol)
        if not sym:
            raise NoDataFoundException("Symbol does not exist.")
        ret = {}
        ret['chunk_count'] = sym[CHUNK_COUNT]
        ret['len'] = sym[LEN]
        ret['appended_rows'] = sym[APPEND_COUNT]
        ret['metadata'] = sym[METADATA]
        ret['chunker'] = sym[CHUNKER]
        ret['chunk_size'] = sym[CHUNK_SIZE]
        ret['serializer'] = sym[SERIALIZER]
        return ret

    def read_metadata(self, symbol):
        '''
        Reads user defined metadata out for the given symbol
        
        Parameters
        ----------
        symbol: str
            symbol for the given item in the DB
        
        Returns
        -------
        ?
        '''
        sym = self._get_symbol_info(symbol)
        if not sym:
            raise NoDataFoundException("Symbol does not exist.")
        x = self._symbols.find_one({SYMBOL: symbol})
        return x[USERMETA] if USERMETA in x else None

    def write_metadata(self, symbol, metadata):
        '''
        writes user defined metadata for the given symbol

        Parameters
        ----------
        symbol: str
            symbol for the given item in the DB
        metadata: ?
            metadata to write
        '''
        sym = self._get_symbol_info(symbol)
        if not sym:
            raise NoDataFoundException("Symbol does not exist.")

        sym[USERMETA] = metadata
        self._symbols.replace_one({SYMBOL: symbol}, sym)

    def get_chunk_ranges(self, symbol, chunk_range=None, reverse=False):
        """
        Returns a generator of (Start, End) tuples for each chunk in the symbol

        Parameters
        ----------
        symbol: str
            the symbol for the given item in the DB
        chunk_range: None, or a range object
            allows you to subset the chunks by range
        reverse: boolean
            return the chunk ranges in reverse order

        Returns
        -------
        generator
        """
        sym = self._get_symbol_info(symbol)
        if not sym:
            raise NoDataFoundException("Symbol does not exist.")
        c = CHUNKER_MAP[sym[CHUNKER]]

        spec = {SYMBOL: symbol}
        if chunk_range is not None:
            spec.update(CHUNKER_MAP[sym[CHUNKER]].to_mongo(chunk_range))

        for x in self._collection.find(spec,
                                       projection=[START, END],
                                       sort=[(START, pymongo.ASCENDING if not reverse else pymongo.DESCENDING)]):
            yield (c.chunk_to_str(x[START]), c.chunk_to_str(x[END]))

    def iterator(self, symbol, chunk_range=None):
        """
        Returns a generator that accesses each chunk in ascending order

        Parameters
        ----------
        symbol: str
            the symbol for the given item in the DB
        chunk_range: None, or a range object
            allows you to subset the chunks by range

        Returns
        -------
        generator
        """
        sym = self._get_symbol_info(symbol)
        if not sym:
            raise NoDataFoundException("Symbol does not exist.")

        c = CHUNKER_MAP[sym[CHUNKER]]
        chunks = list(self.get_chunk_ranges(symbol, chunk_range=chunk_range))

        for chunk in chunks:
            yield self.read(symbol, chunk_range=c.to_range(chunk[0], chunk[1]))

    def reverse_iterator(self, symbol, chunk_range=None):
        """
        Returns a generator that accesses each chunk in descending order

        Parameters
        ----------
        symbol: str
            the symbol for the given item in the DB
        chunk_range: None, or a range object
            allows you to subset the chunks by range

        Returns
        -------
        generator
        """
        sym = self._get_symbol_info(symbol)
        if not sym:
            raise NoDataFoundException("Symbol does not exist.")

        c = CHUNKER_MAP[sym[CHUNKER]]
        chunks = list(self.get_chunk_ranges(symbol, chunk_range=chunk_range, reverse=True))

        for chunk in chunks:
            yield self.read(symbol, chunk_range=c.to_range(chunk[0], chunk[1]))

    def stats(self):
        """
        Return storage statistics about the library

        Returns
        -------
        dictionary of storage stats
        """

        res = {}
        db = self._collection.database
        conn = db.connection
        res['sharding'] = {}
        try:
            sharding = conn.config.databases.find_one({'_id': db.name})
            if sharding:
                res['sharding'].update(sharding)
            res['sharding']['collections'] = list(conn.config.collections.find({'_id': {'$regex': '^' + db.name + r"\..*"}}))
        except OperationFailure:
            # Access denied
            pass
        res['dbstats'] = db.command('dbstats')
        res['chunks'] = db.command('collstats', self._collection.name)
        res['symbols'] = db.command('collstats', self._symbols.name)
        res['metadata'] = db.command('collstats', self._mdata.name)
        res['totals'] = {'count': res['chunks']['count'],
                         'size': res['chunks']['size'] + res['symbols']['size'] + res['metadata']['size'],
                         }
        return res

    def has_symbol(self, symbol):
        '''
        Check if symbol exists in collection

        Parameters
        ----------
        symbol: str
            The symbol to look up in the collection

        Returns
        -------
        bool
        '''
        return self._get_symbol_info(symbol) is not None
