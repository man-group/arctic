from datetime import datetime as dt, timedelta
import pprint
import logging

import bson
from pymongo import ReadPreference
import pymongo
from pymongo.errors import OperationFailure, AutoReconnect

from .._util import indent, enable_powerof2sizes, \
    enable_sharding
from ..date import mktz, datetime_to_ms, ms_to_datetime
from ..decorators import mongo_retry
from ..exceptions import NoDataFoundException, DuplicateSnapshotException, \
    OptimisticLockException, ArcticException
from ..hooks import log_exception
from ._pickle_store import PickleStore
from ._version_store_utils import cleanup
from .versioned_item import VersionedItem

logger = logging.getLogger(__name__)

VERSION_STORE_TYPE = 'VersionStore'
_TYPE_HANDLERS = []


def register_versioned_storage(storageClass):
    existing_instances = [i for i, v in enumerate(_TYPE_HANDLERS) if str(v.__class__) == str(storageClass)]
    if existing_instances:
        for i in existing_instances:
            _TYPE_HANDLERS[i] = storageClass()
    else:
        _TYPE_HANDLERS.append(storageClass())
    return storageClass


class VersionStore(object):

    _bson_handler = PickleStore()

    @classmethod
    def initialize_library(cls, arctic_lib, hashed=False, **kwargs):
        c = arctic_lib.get_top_level_collection()

        if '%s.changes' % c.name not in mongo_retry(c.database.collection_names)():
            # 32MB buffer for change notifications
            mongo_retry(c.database.create_collection)('%s.changes' % c.name, capped=True, size=32 * 1024 * 1024)

        for th in _TYPE_HANDLERS:
            th.initialize_library(arctic_lib, **kwargs)
        VersionStore._bson_handler.initialize_library(arctic_lib, **kwargs)
        VersionStore(arctic_lib)._ensure_index()

        logger.info("Trying to enable usePowerOf2Sizes...")
        try:
            enable_powerof2sizes(arctic_lib.arctic, arctic_lib.get_name())
        except OperationFailure, e:
            logger.error("Library created, but couldn't enable usePowerOf2Sizes: %s" % str(e))

        logger.info("Trying to enable sharding...")
        try:
            enable_sharding(arctic_lib.arctic, arctic_lib.get_name(), hashed=hashed)
        except OperationFailure, e:
            logger.warn("Library created, but couldn't enable sharding: %s. This is OK if you're not 'admin'" % str(e))

    @mongo_retry
    def _ensure_index(self):
        collection = self._collection
        collection.snapshots.create_index([('name', pymongo.ASCENDING)], unique=True,
                                          background=True)
        collection.versions.create_index([('symbol', pymongo.ASCENDING), ('_id', pymongo.DESCENDING)],
                                         background=True)
        collection.versions.create_index([('symbol', pymongo.ASCENDING), ('version', pymongo.DESCENDING)], unique=True,
                                         background=True)
        collection.version_nums.create_index('symbol', unique=True, background=True)
        for th in _TYPE_HANDLERS:
            th._ensure_index(collection)

    @mongo_retry
    def __init__(self, arctic_lib):
        self._arctic_lib = arctic_lib

        # Do we allow reading from secondaries
        self._allow_secondary = self._arctic_lib.arctic._allow_secondary

        # The default collections
        self._collection = arctic_lib.get_top_level_collection()
        self._audit = self._collection.audit
        self._snapshots = self._collection.snapshots
        self._versions = self._collection.versions
        self._version_nums = self._collection.version_nums
        self._publish_changes = '%s.changes' % self._collection.name in self._collection.database.collection_names()
        if self._publish_changes:
            self._changes = self._collection.changes

    def __getstate__(self):
        return {'arctic_lib': self._arctic_lib}

    def __setstate__(self, state):
        return VersionStore.__init__(self, state['arctic_lib'])

    def __str__(self):
        return """<%s at %s>
%s""" % (self.__class__.__name__, hex(id(self)), indent(str(self._arctic_lib), 4))

    def __repr__(self):
        return str(self)
    
    def _read_preference(self, allow_secondary):
        """ Return the mongo read preference given an 'allow_secondary' argument
        """
        allow_secondary = self._allow_secondary if allow_secondary is None else allow_secondary
        return ReadPreference.NEAREST if allow_secondary else ReadPreference.PRIMARY

    @mongo_retry
    def list_symbols(self, all_symbols=False, snapshot=None, regex=None, **kwargs):
        """
        Return the symbols in this library.

        Parameters
        ----------
        all_symbols : `bool`
            If True returns all symbols under all snapshots, even if the symbol has been deleted
            in the current version (i.e. it exists under a snapshot... Default: False
        snapshot : `str`
            Return the symbols available under the snapshot.
        regex : `str`
            filter symbols by the passed in regular expression
        kwargs :
            kwarg keys are used as fields to query for symbols with metadata matching
            the kwargs query

        Returns
        -------
        String list of symbols in the library
        """
        query = {}
        if regex is not None:
            query ['symbol'] = {'$regex' : regex}
        if kwargs:
            for k, v in kwargs.iteritems():
                query['metadata.' + k] = v
        if snapshot is not None:
            try:
                query['parent'] = self._snapshots.find_one({'name': snapshot})['_id']
            except TypeError:
                raise NoDataFoundException('No snapshot %s in library %s' % (snapshot, self._arctic_lib.get_name()))
        elif all_symbols:
            return self._versions.find(query).distinct('symbol')

        # Return just the symbols which aren't deleted in the 'trunk' of this library
        pipeline = []
        if query:
            # Match based on user criteria first
            pipeline.append({'$match': query})
        pipeline.extend([
                         # Id is by insert time which matches version order
                         {'$sort': {'_id':-1}},
                         # Group by 'symbol'
                         {'$group': {'_id': '$symbol',
                                     'deleted': {'$first': '$metadata.deleted'},
                                     },
                          },
                         # Don't include symbols which are part of some snapshot, but really deleted...
                         {'$match': {'deleted': {'$ne': True}}},
                         {'$project': {'_id': 0,
                                       'symbol':  '$_id',
                                       }
                          }])

        results = self._versions.aggregate(pipeline)
        return sorted([x['symbol'] for x in results])

    @mongo_retry
    def has_symbol(self, symbol, as_of=None):
        """
        Return True if the 'symbol' exists in this library AND the symbol
        isn't deleted in the specified as_of.

        It's possible for a deleted symbol to exist in older snapshots.

        Parameters
        ----------
        symbol : `str`
            symbol name for the item
        as_of : `str` or int or `datetime.datetime`
            Return the data as it was as_of the point in time.
            `int` : specific version number
            `str` : snapshot name which contains the version
            `datetime.datetime` : the version of the data that existed as_of the requested point in time
        """
        try:
            # Always use the primary for has_symbol, it's safer
            self._read_metadata(symbol, as_of=as_of, read_preference=ReadPreference.PRIMARY)
            return True
        except NoDataFoundException:
            return False

    def read_audit_log(self, symbol):
        """
        Return the audit log associated with a given symbol

        Parameters
        ----------
        symbol : `str`
            symbol name for the item
        """
        query = {'symbol': symbol}
        return list(self._audit.find(query, sort=[('_id', -1)],
                                     projection={'_id': False}))

    def list_versions(self, symbol=None, snapshot=None, latest_only=False):
        """
        Return a list of versions filtered by the passed in parameters.

        Parameters
        ----------
        symbol : `str`
            Symbol to return versions for.  If None returns versions across all
            symbols in the library.
        snapshot : `str`
            Return the versions contained in the named snapshot
        latest_only : `bool`
            Only include the latest version for a specific symbol

        Returns
        -------
        List of dictionaries describing the discovered versions in the library
        """
        if symbol is None:
            symbols = self.list_symbols()
        else:
            symbols = [symbol]

        query = {}

        if snapshot is not None:
            try:
                query['parent'] = self._snapshots.find_one({'name': snapshot})['_id']
            except TypeError:
                raise NoDataFoundException('No snapshot %s in library %s' % (snapshot, self._arctic_lib.get_name()))

        versions = []
        for symbol in symbols:
            query['symbol'] = symbol
            seen_symbols = set()
            for version in self._versions.find(query, projection=['symbol', 'version', 'parent'], sort=[('version', -1)]):
                if latest_only and version['symbol'] in seen_symbols:
                    continue
                seen_symbols.add(version['symbol'])
                versions.append({'symbol': version['symbol'], 'version': version['version'],
                       # We return naive datetimes in Local Time.
                       'date': ms_to_datetime(datetime_to_ms(version['_id'].generation_time)),
                       'snapshots': self._find_snapshots(version.get('parent', []))})
        return versions

    def _find_snapshots(self, parent_ids):
        snapshots = []
        for p in parent_ids:
            snap = self._snapshots.find_one({'_id': p})
            if snap:
                snapshots.append(snap['name'])
            else:
                snapshots.append(str(p))
        return snapshots

    def _read_handler(self, version, symbol):
        handler = None
        for h in _TYPE_HANDLERS:
            if h.can_read(version, symbol):
                handler = h
                break
        if handler is None:
            handler = self._bson_handler
        return handler

    def _write_handler(self, version, symbol, data, **kwargs):
        handler = None
        for h in _TYPE_HANDLERS:
            if h.can_write(version, symbol, data, **kwargs):
                handler = h
                break
        if handler is None:
            version['type'] = 'default'
            handler = self._bson_handler
        return handler

    def read(self, symbol, as_of=None, date_range=None, from_version=None, allow_secondary=None, **kwargs):
        """
        Read data for the named symbol.  Returns a VersionedItem object with
        a data and metdata element (as passed into write).

        Parameters
        ----------
        symbol : `str`
            symbol name for the item
        as_of : `str` or int or `datetime.datetime`
            Return the data as it was as_of the point in time.
            `int` : specific version number
            `str` : snapshot name which contains the version
            `datetime.datetime` : the version of the data that existed as_of the requested point in time
        date_range: `arctic.date.DateRange`
            DateRange to read data for.  Applies to Pandas data, with a DateTime index
            returns only the part of the data that falls in the DateRange.
        allow_secondary : `bool` or `None`
            Override the default behavior for allowing reads from secondary members of a cluster:
            `None` : use the settings from the top-level `Arctic` object used to query this version store.
            `True` : allow reads from secondary members
            `False` : only allow reads from primary members

        Returns
        -------
        VersionedItem namedtuple which contains a .data and .metadata element
        """
        try:
            read_preference = self._read_preference(allow_secondary)
            _version = self._read_metadata(symbol, as_of=as_of, read_preference=read_preference)
            return self._do_read(symbol, _version, from_version,
                                 date_range=date_range, read_preference=read_preference, **kwargs)
        except (OperationFailure, AutoReconnect) as e:
            # Log the exception so we know how often this is happening
            log_exception('read', e, 1)
            # If we've failed to read from the secondary, then it's possible the
            # secondary has lagged.  In this case direct the query to the primary.
            _version = mongo_retry(self._read_metadata)(symbol, as_of=as_of,
                                                        read_preference=ReadPreference.PRIMARY)
            return self._do_read_retry(symbol, _version, from_version,
                                       date_range=date_range,
                                       read_preference=ReadPreference.PRIMARY,
                                       **kwargs)
        except Exception, e:
            log_exception('read', e, 1)
            raise

    @mongo_retry
    def _show_info(self, symbol, as_of=None):
        """
        Print details on the stored symbol: the underlying storage handler
        and the version_document corresponding to the specified version.

        Parameters
        ----------
        symbol : `str`
            symbol name for the item
        as_of : `str` or int or `datetime.datetime`
            Return the data as it was as_of the point in time.
            `int` : specific version number
            `str` : snapshot name which contains the version
            `datetime.datetime` : the version of the data that existed as_of the requested point in time
        """
        print self._get_info(symbol, as_of)

    def _get_info(self, symbol, as_of=None):
        _version = self._read_metadata(symbol, as_of=as_of)
        handler = self._read_handler(_version, symbol)
        if hasattr(handler, "get_info"):
            return handler.get_info(self._arctic_lib, _version, symbol)
        else:
            return """Handler: %s\n\nVersion document:\n%s""" % (handler.__class__.__name__, pprint.pformat(_version))

    def _do_read(self, symbol, version, from_version=None, **kwargs):
        handler = self._read_handler(version, symbol)
        data = handler.read(self._arctic_lib, version, symbol, from_version=from_version, **kwargs)
        if data is None:
            raise NoDataFoundException("No data found for %s in library %s" % (symbol, self._arctic_lib.get_name()))
        return VersionedItem(symbol=symbol, library=self._arctic_lib.get_name(), version=version['version'],
                             metadata=version.pop('metadata', None), data=data)
    _do_read_retry = mongo_retry(_do_read)

    @mongo_retry
    def read_metadata(self, symbol, as_of=None, allow_secondary=None):
        """
        Return the metadata saved for a symbol.  This method is fast as it doesn't
        actually load the data.

        Parameters
        ----------
        symbol : `str`
            symbol name for the item
        as_of : `str` or int or `datetime.datetime`
            Return the data as it was as_of the point in time.
            `int` : specific version number
            `str` : snapshot name which contains the version
            `datetime.datetime` : the version of the data that existed as_of the requested point in time
        allow_secondary : `bool` or `None`
            Override the default behavior for allowing reads from secondary members of a cluster:
            `None` : use the settings from the top-level `Arctic` object used to query this version store.
            `True` : allow reads from secondary members
            `False` : only allow reads from primary members
        """
        _version = self._read_metadata(symbol, as_of=as_of, read_preference=self._read_preference(allow_secondary))
        return VersionedItem(symbol=symbol, library=self._arctic_lib.get_name(), version=_version['version'],
                             metadata=_version.pop('metadata', None), data=None)

    def _read_metadata(self, symbol, as_of=None, read_preference=None):
        if read_preference is None:
            # We want to hit the PRIMARY if querying secondaries is disabled.  If we're allowed to query secondaries,
            # then we want to hit the secondary for metadata.  We maintain ordering of chunks vs. metadata, such that
            # if metadata is available, we guarantee that chunks will be available. (Within a 10 minute window.)
            read_preference = ReadPreference.PRIMARY_PREFERRED if not self._allow_secondary else ReadPreference.SECONDARY_PREFERRED

        versions_coll = self._versions.with_options(read_preference=read_preference)

        _version = None
        if as_of is None:
            _version = versions_coll.find_one({'symbol': symbol}, sort=[('version', pymongo.DESCENDING)])
        elif isinstance(as_of, basestring):
            # as_of is a snapshot
            snapshot = self._snapshots.find_one({'name': as_of})
            if snapshot:
                _version = versions_coll.find_one({'symbol': symbol, 'parent': snapshot['_id']})
        elif isinstance(as_of, dt):
            # as_of refers to a datetime
            if not as_of.tzinfo:
                as_of = as_of.replace(tzinfo=mktz())
            _version = versions_coll.find_one({'symbol': symbol,
                                                '_id': {'$lt': bson.ObjectId.from_datetime(as_of + timedelta(seconds=1))}},
                                               sort=[('_id', pymongo.DESCENDING)])
        else:
            # Backward compatibility - as of is a version number
            _version = versions_coll.find_one({'symbol': symbol, 'version': as_of})

        if not _version:
            raise NoDataFoundException("No data found for %s in library %s" % (symbol, self._arctic_lib.get_name()))

        # if the item has been deleted, don't return any metadata
        metadata = _version.get('metadata', None)
        if metadata is not None and metadata.get('deleted', False) is True:
            raise NoDataFoundException("No data found for %s in library %s" % (symbol, self._arctic_lib.get_name()))

        return _version

    @mongo_retry
    def append(self, symbol, data, metadata=None, prune_previous_version=True, upsert=True, **kwargs):
        """
        Append 'data' under the specified 'symbol' name to this library.
        The exact meaning of 'append' is left up to the underlying store implementation.

        Parameters
        ----------
        symbol : `str`
            symbol name for the item
        data :
            to be persisted
        metadata : `dict`
            an optional dictionary of metadata to persist along with the symbol.
        prune_previous_version : `bool`
            Removes previous (non-snapshotted) versions from the database.
            Default: True
        upsert : `bool`
            Write 'data' if no previous version exists.
        """
        self._ensure_index()
        self._arctic_lib.check_quota()
        version = {'_id': bson.ObjectId()}
        version['symbol'] = symbol
        spec = {'symbol': symbol}
        previous_version = self._versions.find_one(spec,
                                                   sort=[('version', pymongo.DESCENDING)])

        if len(data) == 0 and previous_version is not None:
            return VersionedItem(symbol=symbol, library=self._arctic_lib.get_name(), version=previous_version,
                                 metadata=version.pop('metadata', None), data=None)

        if upsert and previous_version is None:
            return self.write(symbol=symbol, data=data, prune_previous_version=prune_previous_version, metadata=metadata)

        assert previous_version is not None

        next_ver = self._version_nums.find_one({'symbol': symbol, 'version': previous_version['version']})

        if next_ver is None:
            raise ArcticException('''version_nums is out of sync with previous version document. 
            This probably means that either a version document write has previously failed, or the previous version has been deleted.
            Append not possible - please call write() to get versions back in sync''')

        # if the symbol has previously been deleted then overwrite
        previous_metadata = previous_version.get('metadata', None)
        if upsert and previous_metadata is not None and previous_metadata.get('deleted', False) is True:
            return self.write(symbol=symbol, data=data, prune_previous_version=prune_previous_version,
                              metadata=metadata)

        handler = self._read_handler(previous_version, symbol)

        if metadata is not None:
            version['metadata'] = metadata
        elif 'metadata' in previous_version:
            version['metadata'] = previous_version['metadata']

        if handler and hasattr(handler, 'append'):
            mongo_retry(handler.append)(self._arctic_lib, version, symbol, data, previous_version, **kwargs)
        else:
            raise Exception("Append not implemented for handler %s" % handler)

        next_ver = self._version_nums.find_one_and_update({'symbol': symbol, 'version': previous_version['version']},
                                                      {'$inc': {'version': 1}},
                                                      upsert=False, new=True)

        if next_ver is None:
            #Latest version has changed during this operation
            raise OptimisticLockException()

        version['version'] = next_ver['version']

        # Insert the new version into the version DB
        mongo_retry(self._versions.insert_one)(version)

        self._publish_change(symbol, version)

        if prune_previous_version and previous_version:
            self._prune_previous_versions(symbol)

        return VersionedItem(symbol=symbol, library=self._arctic_lib.get_name(), version=version['version'],
                             metadata=version.pop('metadata', None), data=None)

    def _publish_change(self, symbol, version):
        if self._publish_changes:
            mongo_retry(self._changes.insert_one)(version)

    @mongo_retry
    def write(self, symbol, data, metadata=None, prune_previous_version=True, **kwargs):
        """
        Write 'data' under the specified 'symbol' name to this library.

        Parameters
        ----------
        symbol : `str`
            symbol name for the item
        data :
            to be persisted
        metadata : `dict`
            an optional dictionary of metadata to persist along with the symbol.
            Default: None
        prune_previous_version : `bool`
            Removes previous (non-snapshotted) versions from the database.
            Default: True
        kwargs :
            passed through to the write handler
            
        Returns
        -------
        VersionedItem named tuple containing the metadata and verison number
        of the written symbol in the store.
        """
        self._ensure_index()
        self._arctic_lib.check_quota()
        version = {'_id': bson.ObjectId()}
        version['symbol'] = symbol
        version['version'] = self._version_nums.find_one_and_update({'symbol': symbol},
                                                                {'$inc': {'version': 1}},
                                                                upsert=True, new=True)['version']
        version['metadata'] = metadata

        previous_version = self._versions.find_one({'symbol': symbol, 'version': {'$lt': version['version']}},
                                                  sort=[('version', pymongo.DESCENDING)],
                                                  )

        handler = self._write_handler(version, symbol, data, **kwargs)
        mongo_retry(handler.write)(self._arctic_lib, version, symbol, data, previous_version, **kwargs)

        # Insert the new version into the version DB
        mongo_retry(self._versions.insert_one)(version)

        if prune_previous_version and previous_version:
            self._prune_previous_versions(symbol)

        logger.debug('Finished writing versions for %s', symbol)

        self._publish_change(symbol, version)

        return VersionedItem(symbol=symbol, library=self._arctic_lib.get_name(), version=version['version'],
                             metadata=version.pop('metadata', None), data=None)

    def _prune_previous_versions(self, symbol, keep_mins=120):
        """
        Prune versions, not pointed at by snapshots which are at least keep_mins old.
        """
        # Find all non-snapshotted versions older than a version that's at least keep_mins minutes old
        # Based on documents available on the secondary
        versions_find = mongo_retry(self._versions.with_options(read_preference=ReadPreference.SECONDARY_PREFERRED if keep_mins > 0 else
                                                                                ReadPreference.PRIMARY)
                                    .find)
        versions = list(versions_find({  # Find versions of this symbol
                                        'symbol': symbol,
                                        # Not snapshotted
                                        '$or': [{'parent': {'$exists': False}}, {'parent': {'$size': 0}}],
                                        # At least 'keep_mins' old
                                        '_id': {'$lt': bson.ObjectId.from_datetime(
                                                        dt.utcnow()
                                                        # Add one second as the ObjectId str has random fuzz 
                                                        + timedelta(seconds=1)
                                                        - timedelta(minutes=keep_mins))
                                                }
                                        },
                                        # Using version number here instead of _id as there's a very unlikely case
                                        # where the versions are created on different hosts or processes at exactly
                                        # the same time.
                                        sort=[('version', pymongo.DESCENDING)],
                                        # Keep one, that's at least 10 mins old, around
                                        # (cope with replication delay)
                                        skip=1,
                                        projection=['_id', 'type'],
                                        ))
        if not versions:
            return
        version_ids = [v['_id'] for v in versions]

        #Find any version_ids that are the basis of other, 'current' versions - don't prune these.
        base_versions = set([x['base_version_id'] for x in mongo_retry(self._versions.find)({
                                            'symbol': symbol,
                                            '_id': {'$nin': version_ids},
                                            'base_version_id':{'$exists':True},
                                           },
                                           projection=['base_version_id'],
                                           )])

        version_ids = list(set(version_ids) - base_versions)

        if not version_ids:
            return

        # Delete the version documents
        mongo_retry(self._versions.delete_many)({'_id': {'$in': version_ids}})
        # Cleanup any chunks
        cleanup(self._arctic_lib, symbol, version_ids)

    @mongo_retry
    def _delete_version(self, symbol, version_num, do_cleanup=True):
        """
        Delete the n'th version of this symbol from the historical collection.
        """
        version = self._versions.find_one({'symbol': symbol, 'version': version_num})
        if not version:
            logger.error("Can't delete %s:%s as not found in DB" % (symbol, version_num))
            return
        # If the version is pointed to by a snapshot, then can't delete
        if version.get('parent', None):
            for parent in version['parent']:
                snap_name = self._snapshots.find_one({'_id': parent})
                if snap_name:
                    snap_name = snap_name['name']
                logger.error("Can't delete: %s:%s as pointed to by snapshot: %s" % (symbol, version['version'],
                                                                                    snap_name))
                return
        self._versions.delete_one({'_id': version['_id']})
        if do_cleanup:
            cleanup(self._arctic_lib, symbol, [version['_id']])

    @mongo_retry
    def delete(self, symbol):
        """
        Delete all versions of the item from the current library which aren't
        currently part of some snapshot.

        Parameters
        ----------
        symbol : `str`
            symbol name to delete
        """
        logger.warn("Deleting data item: %r from %r" % (symbol, self._arctic_lib.get_name()))
        # None is the magic sentinel value that indicates an item has been deleted.
        sentinel = self.write(symbol, None, prune_previous_version=False, metadata={'deleted': True})
        self._prune_previous_versions(symbol, 0)

        # If there aren't any other versions, then we don't need the sentinel empty value
        # so delete the sentinel version altogether
        snapped_version = self._versions.find_one({'symbol': symbol,
                                                   'metadata.deleted': {'$ne': True}})
        if not snapped_version:
            self._delete_version(symbol, sentinel.version)
        assert not self.has_symbol(symbol)

    def _write_audit(self, user, message, changed_version):
        """
        Creates an audit entry, which is much like a snapshot in that
        it references versions and provides some history of the changes made.
        """
        audit = {'_id': bson.ObjectId(),
                 'user': user,
                 'message': message,
                 'symbol': changed_version.symbol
                 }
        orig_version = changed_version.orig_version.version
        new_version = changed_version.new_version.version
        audit['orig_v'] = orig_version
        audit['new_v'] = new_version
        # Update the versions to contain the audit
        mongo_retry(self._versions.update_many)({'symbol': changed_version.symbol,
                                                 'version': {'$in': [orig_version, new_version]}
                                                 },
                                                {'$addToSet': {'parent': audit['_id']}})
        # Create the audit entry
        mongo_retry(self._audit.insert_one)(audit)

    def snapshot(self, snap_name, metadata=None, skip_symbols=None, versions=None):
        """
        Snapshot versions of symbols in the library.  Can be used like:

        Parameters
        ----------
        snap_name : `str`
            name of the snapshot
        metadata : `dict`
            an optional dictionary of metadata to persist along with the symbol.
        skip_symbols : `collections.Iterable`
            optional symbols to be excluded from the snapshot
        versions: `dict`
            an optional dictionary of versions of the symbols to be snapshot
        """
        # Ensure the user doesn't insert duplicates
        snapshot = self._snapshots.find_one({'name': snap_name})
        if snapshot:
            raise DuplicateSnapshotException("Snapshot '%s' already exists." % snap_name)

        # Create a snapshot version document
        snapshot = {'_id': bson.ObjectId()}
        snapshot['name'] = snap_name
        snapshot['metadata'] = metadata
        
        skip_symbols = set() if skip_symbols is None else set(skip_symbols) 

        if versions is None:
            versions = {sym: None for sym in set(self.list_symbols()) - skip_symbols}

        # Loop over, and snapshot all versions except those we've been asked to skip
        for sym in versions:
            try:
                sym = self._read_metadata(sym, read_preference=ReadPreference.PRIMARY, as_of=versions[sym])
                # Update the parents field of the version document
                mongo_retry(self._versions.update_one)({'_id': sym['_id']},
                                                       {'$addToSet': {'parent': snapshot['_id']}})
            except NoDataFoundException:
                # Version has been deleted, not included in the snapshot
                pass

        mongo_retry(self._snapshots.insert_one)(snapshot)

    def delete_snapshot(self, snap_name):
        """
        Delete a named snapshot

        Parameters
        ----------
        symbol : `str`
            The snapshot name to delete
        """
        snapshot = self._snapshots.find_one({'name': snap_name})
        if not snapshot:
            raise NoDataFoundException("Snapshot %s not found!" % snap_name)

        # Remove the snapshot Id as a parent of versions
        self._versions.update_many({'parent': snapshot['_id']},
                                   {'$pull': {'parent': snapshot['_id']}})

        self._snapshots.delete_one({'name': snap_name})

    def list_snapshots(self):
        """
        List the snapshots in the library

        Returns
        -------
        string list of snapshot names
        """
        return dict((i['name'], i['metadata']) for i in self._snapshots.find())

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
            res['sharding']['collections'] = list(conn.config.collections.find({'_id': {'$regex': '^' + db.name + "\..*"}}))
        except OperationFailure:
            # Access denied
            pass
        res['dbstats'] = db.command('dbstats')
        res['chunks'] = db.command('collstats', self._collection.name)
        res['versions'] = db.command('collstats', self._versions.name)
        res['snapshots'] = db.command('collstats', self._snapshots.name)
        res['totals'] = {'count': res['chunks']['count'],
                         'size': res['chunks']['size'] + res['versions']['size'] + res['snapshots']['size'],
                         }
        return res

    def _fsck(self, dry_run):
        """
        Run a consistency check on this VersionStore library.
        """
        # Cleanup Orphaned Chunks
        self._cleanup_orphaned_chunks(dry_run)
        # Cleanup Orphaned Snapshots
        self._cleanup_orphaned_versions(dry_run)

    def _cleanup_orphaned_chunks(self, dry_run):
        """
        Fixes any chunks who have parent pointers to missing versions.
        Removes the broken parent pointer and, if there are no other parent pointers for the chunk,
        removes the chunk.
        """
        lib = self
        chunks_coll = lib._collection
        versions_coll = chunks_coll.versions

        logger.info("ORPHANED CHUNK CHECK: %s" % self._arctic_lib.get_name())
        for symbol in chunks_coll.distinct('symbol'):
            logger.debug('Checking %s' % symbol)
            # Be liberal with the generation time.
            gen_time = dt.now() - timedelta(days=1)
            parent_id_constraint = {'$lt': bson.ObjectId.from_datetime(gen_time)}

            # For each symbol, grab all 'real' versions
            versions = set(versions_coll.find({'symbol': symbol,
                                               '_id': parent_id_constraint}).distinct('_id'))
            # Using aggregate so we can unwind, and pull out 'parent', where 'parent' is older than a day.
            parents = chunks_coll.aggregate([{'$match': {'symbol': symbol}},
                                             {'$project': {'parent': True}},
                                             {'$unwind': '$parent'},
                                             {'$match': {'parent': parent_id_constraint}},
                                             {'$group': {'_id': '$parent'}},
                                             ])
            parent_ids = set([x['_id'] for x in parents])

            leaked_versions = sorted(parent_ids - versions)
            if len(leaked_versions):
                logger.info("%s leaked %d versions" % (symbol, len(leaked_versions)))
            for x in leaked_versions:
                chunk_count = chunks_coll.find({'symbol': symbol, 'parent': x}).count()
                logger.info("%s: Missing Version %s (%s) ; %s chunks ref'd" % (symbol,
                                                                               x.generation_time,
                                                                               x,
                                                                               chunk_count
                                                                               ))
                if versions_coll.find_one({'symbol': symbol, '_id': x}) is not None:
                    raise Exception("Error: version (%s) is found for (%s), but shouldn't be!" %
                                    (x, symbol))
            # Now cleanup the leaked versions
            if not dry_run:
                cleanup(lib._arctic_lib, symbol, leaked_versions)

    def _cleanup_orphaned_versions(self, dry_run):
        """
        Fixes any versions who have parent pointers to missing snapshots.
        Note, doesn't delete the versions, just removes the parent pointer if it no longer
        exists in snapshots.
        """
        lib = self
        versions_coll = lib._collection.versions
        snapshots_coll = lib._collection.snapshots

        logger.info("ORPHANED SNAPSHOT CHECK: %s" % self._arctic_lib.get_name())

        # Be liberal with the generation time.
        gen_time = dt.now() - timedelta(days=1)
        parent_id_constraint = {'$lt': bson.ObjectId.from_datetime(gen_time)}

        # For each symbol, grab all 'real' snapshots and audit entries
        snapshots = set(snapshots_coll.distinct('_id'))
        snapshots |= set(lib._audit.distinct('_id'))
        # Using aggregate so we can unwind, and pull out 'parent', where 'parent' is older than a day.
        parents = versions_coll.aggregate([{'$project': {'parent': True}},
                                           {'$unwind': '$parent'},
                                           {'$match': {'parent': parent_id_constraint}},
                                           {'$group': {'_id': '$parent'}},
                                           ])
        parent_ids = set([x['_id'] for x in parents])

        leaked_snaps = sorted(parent_ids - snapshots)
        if len(leaked_snaps):
            logger.info("leaked %d snapshots" % (len(leaked_snaps)))
        for x in leaked_snaps:
            ver_count = versions_coll.find({'parent': x}).count()
            logger.info("Missing Snapshot %s (%s) ; %s versions ref'd" % (x.generation_time,
                                                                          x,
                                                                          ver_count
                                                                          ))
            if snapshots_coll.find_one({'_id': x}) is not None:
                raise Exception("Error: snapshot (%s) is found, but shouldn't be!" %
                                (x))
            # Now cleanup the leaked snapshots
            if not dry_run:
                versions_coll.update_many({'parent': x},
                                          {'$pull': {'parent': x}})
