import logging
from pymongo.errors import OperationFailure
from ..decorators import mongo_retry
from .._util import enable_sharding

logger = logging.getLogger(__name__)

BSON_STORE_TYPE = 'BSONStore'

class BSONStore(object):
    """
    BSON Data Store. This stores any Python object that encodes to BSON correctly,
    and offers a vanilla pymongo interface. Note that strings myst be valid UTF-8.

    See: https://api.mongodb.com/python/3.4.0/api/bson/index.html

    Note that this neither defines nor ensures any indices, they are left to the user
    to create and manage according to the effective business schema applicable to their data.

    Likewise, _id is left to the user to populate if they wish, and is exposed in documents. As
    is normally the case with pymongo, _id is set to unique ObjectId if left unspecified at
    document insert time.
    """

    def __init__(self, arctic_lib):
        self._arctic_lib = arctic_lib
        self._collection = self._arctic_lib.get_top_level_collection()

    @classmethod
    def initialize_library(cls, arctic_lib, hashed=True, **kwargs):
        logger.info("Trying to enable sharding...")
        try:
            if not hashed:
                logger.warning("Ignored hashed=False when enabling sharding, only hashed=True "
                               " makes sense when they key is an ObjectId")
            enable_sharding(arctic_lib.arctic, arctic_lib.get_name(), hashed=True, key='_id')
        except OperationFailure as exception:
            logger.warning(("Library created, but couldn't enable sharding: "
                            "%s. This is OK if you're not 'admin'"), exception)

    @mongo_retry
    def stats(self):
        """
        Store stats, necessary for quota to work.
        """
        res = {}
        db = self._collection.database
        res['dbstats'] = db.command('dbstats')
        res['data'] = db.command('collstats', self._collection.name)
        res['totals'] = {'count': res['data']['count'],
                         'size': res['data']['size']}
        return res

    @mongo_retry
    def find(self, *args, **kwargs):
        """
        See http://api.mongodb.com/python/current/api/pymongo/collection.html#pymongo.collection.Collection.find
        """
        return self._collection.find(*args, **kwargs)

    @mongo_retry
    def insert_one(self, document, **kwargs):
        """
        See http://api.mongodb.com/python/current/api/pymongo/collection.html#pymongo.collection.Collection.insert_one
        """
        self._arctic_lib.check_quota()
        return self._collection.insert_one(document, **kwargs)

    @mongo_retry
    def insert_many(self, documents, **kwargs):
        """
        See http://api.mongodb.com/python/current/api/pymongo/collection.html#pymongo.collection.Collection.insert_many
        """
        self._arctic_lib.check_quota()
        return self._collection.insert_many(documents, **kwargs)

    def delete_one(self, filter, **kwargs):
        """
        See http://api.mongodb.com/python/current/api/pymongo/collection.html#pymongo.collection.Collection.delete_one
        """
        return self._collection.delete_one(filter, **kwargs)

    @mongo_retry
    def delete_many(self, filter, **kwargs):
        """
        See http://api.mongodb.com/python/current/api/pymongo/collection.html#pymongo.collection.Collection.delete_many
        """
        return self._collection.delete_many(filter, **kwargs)

    @mongo_retry
    def update_one(self, filter, update, **kwargs):
        """
        See http://api.mongodb.com/python/current/api/pymongo/collection.html#pymongo.collection.Collection.update_one
        """
        self._arctic_lib.check_quota()
        return self._collection.update_one(filter, update, **kwargs)

    @mongo_retry
    def update_many(self, filter, update, **kwargs):
        """
        See http://api.mongodb.com/python/current/api/pymongo/collection.html#pymongo.collection.Collection.update_many
        """
        self._arctic_lib.check_quota()
        return self._collection.update_many(filter, update, **kwargs)

    @mongo_retry
    def replace_one(self, filter, replacement, **kwargs):
        """
        See http://api.mongodb.com/python/current/api/pymongo/collection.html#pymongo.collection.Collection.replace_one
        """
        self._arctic_lib.check_quota()
        return self._collection.update_one(filter, replacement, **kwargs)

    @mongo_retry
    def replace_many(self, filter, replacement, **kwargs):
        """
        See http://api.mongodb.com/python/current/api/pymongo/collection.html#pymongo.collection.Collection.replace_many
        """
        self._arctic_lib.check_quota()
        return self._collection.replace_many(filter, replacement, **kwargs)

    @mongo_retry
    def find_one_and_replace(self, filter, replacement, **kwargs):
        """
        See http://api.mongodb.com/python/current/api/pymongo/collection.html#pymongo.collection.Collection.find_one_and_replace
        """
        self._arctic_lib.check_quota()
        return self._collection.find_one_and_replace(filter, replacement, **kwargs)

    @mongo_retry
    def count(self, filter, **kwargs):
        """
        See http://api.mongodb.com/python/current/api/pymongo/collection.html#pymongo.collection.Collection.count
        """
        return self._collection.count(filter, **kwargs)

    @mongo_retry
    def distinct(self, key, **kwargs):
        """
        See http://api.mongodb.com/python/current/api/pymongo/collection.html#pymongo.collection.Collection.distinct
        """
        return self._collection.distinct(key, **kwargs)
    
    @mongo_retry
    def create_index(self, keys, **kwargs):
        """
        See http://api.mongodb.com/python/current/api/pymongo/collection.html#pymongo.collection.Collection.create_index
        """
        return self._collection.create_index(keys, **kwargs)

    @mongo_retry
    def drop_index(self, index_or_name):
        """
        See http://api.mongodb.com/python/current/api/pymongo/collection.html#pymongo.collection.Collection.drop_index
        """
        return self._collection.drop_index(index_or_name)

    @mongo_retry
    def index_information(self):
        """
        See http://api.mongodb.com/python/current/api/pymongo/collection.html#pymongo.collection.Collection.index_information
        """
        return self._collection.index_information()
