from datetime import datetime as dt
import logging

import pandas as pd

import bson
import pymongo
from ..decorators import mongo_retry
from ..exceptions import NoDataFoundException

from .bson_store import BSONStore

logger = logging.getLogger(__name__)

METADATA_STORE_TYPE = 'MetadataStore'

class MetadataStore(BSONStore):
    """
    Metadata Store. This stores metadata with timestamps to allow temporal queries.

    Entries are stored in the following format:
        'symbol': symbol name
        'metadata': metadata to be persisted
        'start_time': when entry becomes effective
        'end_time': (Optional) when entry expires. If not set, it is still in effect

    For each symbol end_time of a entry should match start_time of the next one except for the current entry.
    """

    @classmethod
    def initialize_library(cls, arctic_lib, hashed=True, **kwargs):
        MetadataStore(arctic_lib)._ensure_index()
        BSONStore.initialize_library(arctic_lib, hashed, **kwargs)

    @mongo_retry
    def _ensure_index(self):
        self.create_index([('symbol', pymongo.ASCENDING), ('start_time', pymongo.DESCENDING)],
                          unique=True, background=True)

    def __init__(self, arctic_lib):
        self._arctic_lib = arctic_lib
        self._collection = self._arctic_lib.get_top_level_collection()

    @mongo_retry
    def find_one(self, *args, **kwargs):
        """
        See http://api.mongodb.com/python/current/api/pymongo/collection.html#pymongo.collection.Collection.find_one
        """
        return self._collection.find_one(*args, **kwargs)

    @mongo_retry
    def find_one_and_update(self, filter, update, **kwargs):
        """
        See http://api.mongodb.com/python/current/api/pymongo/collection.html#pymongo.collection.Collection.find_one_and_update
        """
        self._arctic_lib.check_quota()
        return self._collection.find_one_and_update(filter, update, **kwargs)

    def find_one_and_delete(self, filter, **kwargs):
        """
        See http://api.mongodb.com/python/current/api/pymongo/collection.html#pymongo.collection.Collection.find_one_and_delete
        """
        return self._collection.find_one_and_delete(filter, **kwargs)

    def list_symbols(self):
        return self.distinct('symbol')

    def has_symbol(self, symbol):
        return self.find_one({'symbol': symbol}) is not None

    def read_metadata(self, symbol, history=False):
        """
        Return the metadata saved for a symbol

        Parameters
        ----------
        symbol : `str`
            symbol name for the item
        history: `bool`
            False: Returns current metadata (Default)
            True: Returns all metadata entries

        Returns
        -------
        metadata document if history=False
        pandas.DateFrame containing timestamps and metadata entries if history=True
        """
        if not history:
            res = self.find_one({'symbol': symbol}, sort=[('start_time', pymongo.DESCENDING)])
            return res and res['metadata']
        find = self.find({'symbol': symbol}, sort=[('start_time', pymongo.ASCENDING)])
        times = []
        entries = []
        for item in find:
            times.append(item['start_time'])
            entries.append(item['metadata'])
        return pd.DataFrame({'metadata': entries}, times)

    def _write_metadata_entry(self, symbol, metadata, start_time):
        """
        Create a new metadata entry

        Parameters
        ----------
        symbol : `str`
            symbol name for the item
        metadata : `dict`
            to be persisted
        start_time : `datetime.datetime`
            when entry becomes effective

        Returns
        -------
        Document written
        """
        document = {'_id': bson.ObjectId()}
        document['symbol'] = symbol
        document['metadata'] = metadata
        document['start_time'] = start_time

        self.insert_one(document)

        logger.debug('Finished writing metadata for %s', symbol)

        return document

    def write_metadata_history(self, collection):
        """
        Manually overwrite entire metadata history for symbols in `collection`

        Parameters
        ----------
        collection : `dict`
            {symbol: (list of metadata, list of timestamps)}
            symbol : `str`
                symbol name for the item
            metadata : `dict`
                to be persisted
            timestamp : `datetime.datetime`
                start_time of the corresponding metadata
            Example:
                {'example': ([{}], [datetime.utcnow()])
        """
        if not isinstance(collection, dict):
            raise TypeError('collection must be a dictionary.')
        documents = []
        for symbol, (entries, times) in collection.items():
            if len(entries) != len(times):
                raise ValueError('Number of entries and number of time stamps do not match.')
            if self.has_symbol(symbol):
                self.delete_all_metadata(symbol)
            doc = {'symbol': symbol, 'metadata': entries[0], 'start_time': times[0]}
            for metadata, start_time in zip(entries[1:], times[1:]):
                if metadata == doc['metadata']:
                    continue
                doc['end_time'] = start_time
                documents.append(doc)
                doc = {'symbol': symbol, 'metadata': metadata, 'start_time': start_time}
            else:
                documents.append(doc)

        self.insert_many(documents)

    def write_metadata(self, symbol, metadata, start_time=None):
        """
        Update metadata entry for `symbol`

        Parameters
        ----------
        symbol : `str`
            symbol name for the item
        metadata : `dict`
            to be persisted
        start_time : `datetime.datetime`
            when metadata becomes effective
            Default: datetime.utcnow()
        """
        if start_time is None:
            start_time = dt.utcnow()
        old_metadata = self.find_one({'symbol': symbol}, sort=[('start_time', pymongo.DESCENDING)])
        if old_metadata is not None:
            if old_metadata['start_time'] >= start_time:
                raise ValueError('start_time={} is earlier than the last metadata @{}'.format(start_time,
                                                                                              old_metadata['start_time']))
            if old_metadata['metadata'] == metadata:
                logger.warning('No change to metadata')
                return metadata
        elif metadata is None:
            return

        self.find_one_and_update({'symbol': symbol}, {'$set': {'end_time': start_time}},
                                  sort=[('start_time', pymongo.DESCENDING)])
        return self._write_metadata_entry(symbol, metadata, start_time)

    def delete_last_metadata(self, symbol):
        """
        Delete current metadata of `symbol`

        Parameters
        ----------
        symbol : `str`
            symbol name to delete

        Returns
        -------
        Deleted metadata
        """
        last_metadata = self.find_one({'symbol': symbol}, sort=[('start_time', pymongo.DESCENDING)])
        if last_metadata is None:
            raise NoDataFoundException('No metadata found for symbo {}'.format(symbol))

        self.find_one_and_delete({'symbol': symbol}, sort=[('start_time', pymongo.DESCENDING)])
        mongo_retry(self.find_one_and_update)({'symbol': symbol}, {'$unset': {'end_time': ''}},
                                              sort=[('start_time', pymongo.DESCENDING)])

        return last_metadata

    def delete_all_metadata(self, symbol):
        """
        Delete all metadata of `symbol`

        Parameters
        ----------
        symbol : `str`
            symbol name to delete
        """
        logger.warning("Deleting entire metadata history for %r from %r" % (symbol, self._arctic_lib.get_name()))
        self.delete_many({'symbol': symbol})
        assert not self.has_symbol(symbol)
