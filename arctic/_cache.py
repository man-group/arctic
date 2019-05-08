import logging
from datetime import datetime, timedelta

from pymongo.errors import OperationFailure

from ._config import CACHE_COLL, CACHE_DB

logger = logging.getLogger(__name__)


class Cache:
    def __init__(self, client, cache_expiry=3600, cache_db=CACHE_DB, cache_col=CACHE_COLL):
        self._client = client
        self._cachedb = client[cache_db]
        self._cachecol = None
        try:
            if cache_col not in self._cachedb.list_collection_names():
                self._cachedb.create_collection(cache_col).create_index(
                    "date", expireAfterSeconds=cache_expiry
                )
        except OperationFailure as op:
            logging.debug(
                "This is fine if you are not admin. The collection should already be created for you: %s", op
            )

        self._cachecol = self._cachedb[cache_col]

    def get(self, key, newer_than_secs=-1):
        """

        :param key: Key for the dataset. eg. list_libraries.
        :param newer_than_secs: -1 to indicate use cache if available. Used to indicate what level of staleness
        in seconds is tolerable.
        :return: None unless if there is non stale data present in the cache.
        """
        try:
            if not self._cachecol:
                # Collection not created or no permissions to read from it.
                return None
            coll_data = self._cachecol.find_one({"type": key})
            # Check that there is data in cache and it's not stale.
            if coll_data and (
                newer_than_secs == -1
                or datetime.utcnow() < coll_data["date"] + timedelta(seconds=newer_than_secs)
            ):
                return coll_data["data"]
        except OperationFailure as op:
            logging.warning(
                "Could not read from cache due to: %s. Ask your admin to give read permissions on %s:%s",
                op,
                CACHE_DB,
                CACHE_COLL,
            )

        return None

    def set(self, key, data):
        try:
            self._cachecol.update_one(
                {"type": key}, {"$set": {"type": key, "date": datetime.utcnow(), "data": data}}, upsert=True
            )
        except OperationFailure as op:
            logging.debug("This operation is to be run with admin permissions. Should be fine: %s", op)

    def append(self, key, append_data):
        try:
            self._cachecol.update_one(
                {"type": key},
                {
                    # Add to set will not add the same library again to the list unlike set.
                    "$addToSet": {"data": append_data},
                    "$setOnInsert": {"type": key, "date": datetime.utcnow()},
                },
                upsert=True,
            )
        except OperationFailure as op:
            logging.debug("Admin is required to append to the cache: %s", op)

    def delete_item_from_key(self, key, item):
        try:
            self._cachecol.update({"type": key}, {"$pull": {"data": item}})
        except OperationFailure as op:
            logging.debug("Admin is required to remove from cache: %s", op)

    def update_item_for_key(self, key, old, new):
        # This op is not atomic, but given the rarity of renaming a lib, it should not cause issues.
        self.delete_item_from_key(key, old)
        self.append(key, new)
