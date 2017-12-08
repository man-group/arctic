from datetime import datetime as dt
import logging

import pandas as pd
import bson
import pymongo

from .._util import indent
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
        self._reset()

    def _reset(self):
        self._collection = self._arctic_lib.get_top_level_collection().metadata

    def __getstate__(self):
        return {'arctic_lib': self._arctic_lib}

    def __setstate__(self, state):
        return MetadataStore.__init__(self, state['arctic_lib'])

    def __str__(self):
        return """<%s at %s>\n%s""" % (self.__class__.__name__, hex(id(self)), indent(str(self._arctic_lib), 4))

    def __repr__(self):
        return str(self)

    @mongo_retry
    def list_symbols(self):
        return self.distinct('symbol')

    @mongo_retry
    def has_symbol(self, symbol):
        return self.find_one({'symbol': symbol}) is not None

    @mongo_retry
    def read_history(self, symbol):
        """
        Return all metadata saved for `symbol`

        Parameters
        ----------
        symbol : `str`
            symbol name for the item

        Returns
        -------
        pandas.DateFrame containing timestamps and metadata entries
        """
        find = self.find({'symbol': symbol}, sort=[('start_time', pymongo.ASCENDING)])
        times = []
        entries = []
        for item in find:
            times.append(item['start_time'])
            entries.append(item['metadata'])
        return pd.DataFrame({symbol: entries}, times)

    @mongo_retry
    def read(self, symbol, as_of=None):
        """
        Return current metadata saved for `symbol`

        Parameters
        ----------
        symbol : `str`
            symbol name for the item
        as_of : `datetime.datetime`
            return entry valid at given time

        Returns
        -------
        metadata
        """
        if as_of is not None:
            res = self.find_one({'symbol': symbol, 'start_time': {'$lte': as_of}},
                                sort=[('start_time', pymongo.DESCENDING)])
        else:
            res = self.find_one({'symbol': symbol}, sort=[('start_time', pymongo.DESCENDING)])
        return res['metadata'] if res is not None else None

    def write_history(self, collection):
        """
        Manually overwrite entire metadata history for symbols in `collection`

        Parameters
        ----------
        collection : `list of pandas.DataFrame`
            with symbol names as headers and timestamps as indices
            (the same format as output of read_history)
            Example:
                [pandas.DataFrame({'symbol': [{}]}, [datetime.datetime.utcnow()])]
        """
        documents = []
        for dataframe in collection:
            if len(dataframe.columns) != 1:
                raise ValueError('More than one symbol found in a DataFrame')
            symbol = dataframe.columns[0]
            times = dataframe.index
            entries = dataframe[symbol].values
            if self.has_symbol(symbol):
                self.purge(symbol)
            doc = {'symbol': symbol, 'metadata': entries[0], 'start_time': times[0]}
            for metadata, start_time in zip(entries[1:], times[1:]):
                if metadata == doc['metadata']:
                    continue
                doc['end_time'] = start_time
                documents.append(doc)
                doc = {'symbol': symbol, 'metadata': metadata, 'start_time': start_time}
            documents.append(doc)

        self.insert_many(documents)

    def append(self, symbol, metadata, start_time=None):
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
            Default: datetime.datetime.utcnow()
        """
        if start_time is None:
            start_time = dt.utcnow()
        old_metadata = self.find_one({'symbol': symbol}, sort=[('start_time', pymongo.DESCENDING)])
        if old_metadata is not None:
            if old_metadata['start_time'] >= start_time:
                raise ValueError('start_time={} is earlier than the last metadata @{}'.format(start_time,
                                                                                              old_metadata['start_time']))
            if old_metadata['metadata'] == metadata:
                return old_metadata
        elif metadata is None:
            return

        self.find_one_and_update({'symbol': symbol}, {'$set': {'end_time': start_time}},
                                  sort=[('start_time', pymongo.DESCENDING)])
        document = {'_id': bson.ObjectId(), 'symbol': symbol, 'metadata': metadata, 'start_time': start_time}
        mongo_retry(self.insert_one)(document)

        logger.debug('Finished writing metadata for %s', symbol)
        return document

    def prepend(self, symbol, metadata, start_time=None):
        """
        Prepend a metadata entry for `symbol`

        Parameters
        ----------
        symbol : `str`
            symbol name for the item
        metadata : `dict`
            to be persisted
        start_time : `datetime.datetime`
            when metadata becomes effective
            Default: datetime.datetime.min
        """
        if metadata is None:
            return
        if start_time is None:
            start_time = dt.min
        old_metadata = self.find_one({'symbol': symbol}, sort=[('start_time', pymongo.ASCENDING)])
        if old_metadata is not None:
            if old_metadata['start_time'] <= start_time:
                raise ValueError('start_time={} is later than the first metadata @{}'.format(start_time,
                                                                                             old_metadata['start_time']))
            if old_metadata['metadata'] == metadata:
                self.find_one_and_update({'symbol': symbol}, {'$set': {'start_time': start_time}},
                                         sort=[('start_time', pymongo.ASCENDING)])
                old_metadata['start_time'] = start_time
                return old_metadata
            end_time = old_metadata.get('start_time')
        else:
            end_time = None

        document = {'_id': bson.ObjectId(), 'symbol': symbol, 'metadata': metadata, 'start_time': start_time}
        if end_time is not None:
            document['end_time'] = end_time
        mongo_retry(self.insert_one)(document)

        logger.debug('Finished writing metadata for %s', symbol)
        return document

    def pop(self, symbol):
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
            raise NoDataFoundException('No metadata found for symbol {}'.format(symbol))

        self.find_one_and_delete({'symbol': symbol}, sort=[('start_time', pymongo.DESCENDING)])
        mongo_retry(self.find_one_and_update)({'symbol': symbol}, {'$unset': {'end_time': ''}},
                                              sort=[('start_time', pymongo.DESCENDING)])

        return last_metadata

    @mongo_retry
    def purge(self, symbol):
        """
        Delete all metadata of `symbol`

        Parameters
        ----------
        symbol : `str`
            symbol name to delete
        """
        logger.warning("Deleting entire metadata history for %r from %r" % (symbol, self._arctic_lib.get_name()))
        self.delete_many({'symbol': symbol})
