import logging
from datetime import datetime as dt, timedelta

import bson
import pymongo
from pymongo import ReadPreference
from pymongo.errors import OperationFailure, AutoReconnect, DuplicateKeyError

from ._pickle_store import PickleStore
from ._version_store_utils import cleanup, get_symbol_alive_shas, _get_symbol_pointer_cfgs
from .versioned_item import VersionedItem
from .._config import STRICT_WRITE_HANDLER_MATCH, FW_POINTERS_REFS_KEY, FW_POINTERS_CONFIG_KEY, FwPointersCfg
from .._util import indent, enable_sharding, mongo_count, get_fwptr_config
from ..date import mktz, datetime_to_ms, ms_to_datetime
from ..decorators import mongo_retry
from ..exceptions import NoDataFoundException, DuplicateSnapshotException, \
    ArcticException
from ..hooks import log_exception

logger = logging.getLogger(__name__)

VERSION_STORE_TYPE = 'VersionStore'
_TYPE_HANDLERS = []
ARCTIC_VERSION = None
ARCTIC_VERSION_NUMERICAL = None


def register_version(version, numerical):
    global ARCTIC_VERSION, ARCTIC_VERSION_NUMERICAL
    ARCTIC_VERSION = version
    ARCTIC_VERSION_NUMERICAL = numerical


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
    def initialize_library(cls, arctic_lib, hashed=True, **kwargs):
        c = arctic_lib.get_top_level_collection()

        if 'strict_write_handler' in kwargs:
            arctic_lib.set_library_metadata('STRICT_WRITE_HANDLER_MATCH',
                                            bool(kwargs.pop('strict_write_handler')))

        for th in _TYPE_HANDLERS:
            th.initialize_library(arctic_lib, **kwargs)
        VersionStore._bson_handler.initialize_library(arctic_lib, **kwargs)
        VersionStore(arctic_lib)._ensure_index()

        logger.info("Trying to enable sharding...")
        try:
            enable_sharding(arctic_lib.arctic, arctic_lib.get_name(), hashed=hashed)
        except OperationFailure as e:
            logger.warning("Library created, but couldn't enable sharding: %s. This is OK if you're not 'admin'" % str(e))

    @mongo_retry
    def _last_version_seqnum(self, symbol):
        last_seq = self._version_nums.find_one({'symbol': symbol})
        return last_seq['version'] if last_seq else 0

    # new index named because of 127 char restriction on fully qualified index names
    @mongo_retry
    def _ensure_index(self):
        collection = self._collection
        collection.snapshots.create_index([('name', pymongo.ASCENDING)], unique=True,
                                          background=True)
        collection.versions.create_index([('symbol', pymongo.ASCENDING), ('_id', pymongo.DESCENDING)],
                                         background=True)
        collection.versions.create_index([('symbol', pymongo.ASCENDING), ('version', pymongo.DESCENDING)], unique=True,
                                         background=True)
        collection.versions.create_index([('symbol', pymongo.ASCENDING), ('version', pymongo.DESCENDING),
                                          ('metadata.deleted', pymongo.ASCENDING)],
                                         name='versionstore_idx',
                                         background=True)
        # Issue #987 slow snapshot delete
        collection.versions.create_index([('parent', pymongo.ASCENDING)], background=True)
        collection.version_nums.create_index('symbol', unique=True, background=True)
        for th in _TYPE_HANDLERS:
            th._ensure_index(collection)

    def __init__(self, arctic_lib):
        self._arctic_lib = arctic_lib
        # Do we allow reading from secondaries
        self._allow_secondary = self._arctic_lib.arctic._allow_secondary
        self._reset()
        self._with_strict_handler = None

    @property
    def _with_strict_handler_match(self):
        if self._with_strict_handler is None:
            strict_meta = self._arctic_lib.get_library_metadata('STRICT_WRITE_HANDLER_MATCH')
            self._with_strict_handler = STRICT_WRITE_HANDLER_MATCH if strict_meta is None else strict_meta
        return self._with_strict_handler

    @mongo_retry
    def _reset(self):
        # The default collections
        self._collection = self._arctic_lib.get_top_level_collection()
        self._audit = self._collection.audit
        self._snapshots = self._collection.snapshots
        self._versions = self._collection.versions
        self._version_nums = self._collection.version_nums

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
            query['symbol'] = {'$regex': regex}
        if kwargs:
            for k, v in kwargs.items():
                # TODO: this doesn't work as expected as it ignores the versions with metadata.deleted set
                #       as a result it will return symbols with matching metadata which have been deleted
                #       Maybe better add a match step in the pipeline instead of making it part of the query
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
            {'$sort': bson.SON([('symbol', pymongo.ASCENDING), ('version', pymongo.DESCENDING)])},
            {'$group': {
                '_id': '$symbol',
                'deleted': {'$first': '$metadata.deleted'}
            }},
            {'$match': {'deleted': {'$ne': True}}}
        ])
        # We may hit the group memory limit (100MB), so use allowDiskUse to circumvent this
        #  - https://docs.mongodb.com/manual/reference/operator/aggregation/group/#group-memory-limit
        return sorted([x['_id'] for x in self._versions.aggregate(pipeline, allowDiskUse=True)])

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

    def read_audit_log(self, symbol=None, message=None):
        """
        Return the audit log associated with a given symbol

        Parameters
        ----------
        symbol : `str`
            symbol name for the item
        """
        query = {}
        if symbol:
            if isinstance(symbol, str):
                query['symbol'] = {'$regex': symbol}
            else:
                query['symbol'] = {'$in': list(symbol)}

        if message is not None:
            query['message'] = message

        def _pop_id(x):
            x.pop('_id')
            return x

        return [_pop_id(x) for x in self._audit.find(query, sort=[('_id', -1)])]

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
            symbols = self.list_symbols(snapshot=snapshot)
        else:
            symbols = [symbol]

        query = {}

        if snapshot is not None:
            try:
                query['parent'] = self._snapshots.find_one({'name': snapshot})['_id']
            except TypeError:
                raise NoDataFoundException('No snapshot %s in library %s' % (snapshot, self._arctic_lib.get_name()))

        versions = []
        snapshots = {ss.get('_id'): ss.get('name') for ss in self._snapshots.find()}
        for symbol in symbols:
            query['symbol'] = symbol
            seen_symbols = set()
            for version in self._versions.find(query, projection=['symbol', 'version', 'parent', 'metadata.deleted'], sort=[('version', -1)]):
                if latest_only and version['symbol'] in seen_symbols:
                    continue
                seen_symbols.add(version['symbol'])
                meta = version.get('metadata')
                versions.append({'symbol': version['symbol'], 'version': version['version'],
                                 'deleted': meta.get('deleted', False) if meta else False,
                                 # We return offset-aware datetimes in Local Time.
                                 'date': ms_to_datetime(datetime_to_ms(version['_id'].generation_time)),
                                 'snapshots': [snapshots[s] for s in version.get('parent', []) if s in snapshots]})
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

    @staticmethod
    def handler_can_write_type(handler, data):
        type_method = getattr(handler, "can_write_type", None)
        if callable(type_method):
            return type_method(data)
        return False

    def _write_handler(self, version, symbol, data, **kwargs):
        handler = None
        for h in _TYPE_HANDLERS:
            if h.can_write(version, symbol, data, **kwargs):
                handler = h
                break
            if self._with_strict_handler_match and self.handler_can_write_type(h, data):
                raise ArcticException("Not falling back to default handler for %s" % symbol)
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
        as_of : `str` or `int` or `datetime.datetime`
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
        except Exception as e:
            log_exception('read', e, 1)
            raise

    @mongo_retry
    def get_info(self, symbol, as_of=None):
        """
        Reads and returns information about the data stored for symbol

        Parameters
        ----------
        symbol : `str`
            symbol name for the item
        as_of : `str` or int or `datetime.datetime`
            Return the data as it was as_of the point in time.
            `int` : specific version number
            `str` : snapshot name which contains the version
            `datetime.datetime` : the version of the data that existed as_of the requested point in time

        Returns
        -------
        dictionary of the information (specific to the type of data)
        """
        version = self._read_metadata(symbol, as_of=as_of, read_preference=None)
        handler = self._read_handler(version, symbol)
        if handler and hasattr(handler, 'get_info'):
            return handler.get_info(version)
        return {}

    @staticmethod
    def handler_supports_read_option(handler, option):
        options_method = getattr(handler, "read_options", None)
        if callable(options_method):
            return option in options_method()

        # If the handler doesn't support interrogation of its read options assume
        # that it does support this option (i.e. fail-open)
        return True

    def get_arctic_version(self, symbol, as_of=None):
        """
        Return the numerical representation of the arctic version used to write the last (or as_of) version for
        the given symbol.

        Parameters
        ----------
        symbol : `str`
            symbol name for the item
        as_of : `str` or int or `datetime.datetime`
            Return the data as it was as_of the point in time.
            `int` : specific version number
            `str` : snapshot name which contains the version
            `datetime.datetime` : the version of the data that existed as_of the requested point in time

        Returns
        -------
        arctic_version : int
            The numerical representation of Arctic version, used to create the specified symbol version
        """
        return self._read_metadata(symbol, as_of=as_of).get('arctic_version', 0)

    def _do_read(self, symbol, version, from_version=None, **kwargs):
        if version.get('deleted'):
            raise NoDataFoundException("No data found for %s in library %s" % (symbol, self._arctic_lib.get_name()))
        handler = self._read_handler(version, symbol)
        # We don't push the date_range check in the handler's code, since the "_with_strict_handler_match"
        #    value is configured on a per-library basis, and is part of the VersionStore instance.
        if self._with_strict_handler_match and \
                kwargs.get('date_range') and \
                not self.handler_supports_read_option(handler, 'date_range'):
            raise ArcticException("Date range arguments not supported by handler in %s" % symbol)

        data = handler.read(self._arctic_lib, version, symbol, from_version=from_version, **kwargs)
        return VersionedItem(symbol=symbol, library=self._arctic_lib.get_name(), version=version['version'],
                             metadata=version.pop('metadata', None), data=data,
                             host=self._arctic_lib.arctic.mongo_host)
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
                             metadata=_version.pop('metadata', None), data=None,
                             host=self._arctic_lib.arctic.mongo_host)

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
        elif isinstance(as_of, str):
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
                                              sort=[('symbol', pymongo.DESCENDING), ('version', pymongo.DESCENDING)])
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

    def _insert_version(self, version):
        try:
            # Keep here the mongo_retry to avoid incrementing versions and polluting the DB with garbage segments,
            # upon intermittent Mongo errors
            # If, however, we get a DuplicateKeyError, suppress it and raise OperationFailure, so that the method-scoped
            # mongo_retry re-tries and creates a new version, to overcome the issue.
            mongo_retry(self._versions.insert_one)(version)
        except DuplicateKeyError as err:
            logger.exception(err)
            raise OperationFailure("A version with the same _id exists, force a clean retry")

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
        self._arctic_lib.check_quota()
        version = {'_id': bson.ObjectId()}
        version['arctic_version'] = ARCTIC_VERSION_NUMERICAL
        version['symbol'] = symbol
        spec = {'symbol': symbol}
        previous_version = self._versions.find_one(spec,
                                                   sort=[('version', pymongo.DESCENDING)])

        if len(data) == 0 and previous_version is not None:
            return VersionedItem(symbol=symbol, library=self._arctic_lib.get_name(), version=previous_version['version'],
                                 metadata=version.pop('metadata', None), data=None,
                                 host=self._arctic_lib.arctic.mongo_host)

        if upsert and previous_version is None:
            return self.write(symbol=symbol, data=data, prune_previous_version=prune_previous_version, metadata=metadata)

        assert previous_version is not None
        dirty_append = False

        # Take a version number for this append.
        # If the version numbers of this and the previous version aren't sequential,
        # then we've either had a failed append in the past,
        # we're in the midst of a concurrent update, we've deleted a version in-between
        # or are somehow 'forking' history
        next_ver = self._version_nums.find_one_and_update({'symbol': symbol, },
                                                          {'$inc': {'version': 1}},
                                                          upsert=False, new=True)['version']

        # This is a very important check, do not remove/modify as it is a guard-dog preventing potential data corruption
        if next_ver != previous_version['version'] + 1:
            dirty_append = True
            logger.debug('''version_nums is out of sync with previous version document.
            This probably means that either a version document write has previously failed, or the previous version has been deleted.''')

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

        if handler and hasattr(handler, 'append') and callable(handler.append):
            handler.append(self._arctic_lib, version, symbol, data,
                           previous_version, dirty_append=dirty_append, **kwargs)
        else:
            raise Exception("Append not implemented for handler %s" % handler)

        if prune_previous_version and previous_version:
            # Does not allow prune to remove the base of the new version
            self._prune_previous_versions(
                symbol,
                keep_version=version.get('base_version_id'),
                new_version_shas=version.get(FW_POINTERS_REFS_KEY),
                keep_mins=kwargs.get('keep_mins', 120)
            )

        # Insert the new version into the version DB
        version['version'] = next_ver
        self._insert_version(version)

        return VersionedItem(symbol=symbol, library=self._arctic_lib.get_name(), version=version['version'],
                             metadata=version.pop('metadata', None), data=None,
                             host=self._arctic_lib.arctic.mongo_host)

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
        VersionedItem named tuple containing the metadata and version number
        of the written symbol in the store.
        """
        self._arctic_lib.check_quota()
        version = {'_id': bson.ObjectId()}
        version['arctic_version'] = ARCTIC_VERSION_NUMERICAL
        version['symbol'] = symbol
        version['version'] = self._version_nums.find_one_and_update({'symbol': symbol},
                                                                    {'$inc': {'version': 1}},
                                                                    upsert=True, new=True)['version']
        version['metadata'] = metadata

        previous_version = self._versions.find_one({'symbol': symbol, 'version': {'$lt': version['version']}},
                                                   sort=[('version', pymongo.DESCENDING)])

        handler = self._write_handler(version, symbol, data, **kwargs)
        handler.write(self._arctic_lib, version, symbol, data, previous_version, **kwargs)

        if prune_previous_version and previous_version:
            self._prune_previous_versions(
                symbol,
                keep_mins=kwargs.get('keep_mins', 120),
                new_version_shas=version.get(FW_POINTERS_REFS_KEY)
            )

        # Insert the new version into the version DB
        self._insert_version(version)

        logger.debug('Finished writing versions for %s', symbol)

        return VersionedItem(symbol=symbol, library=self._arctic_lib.get_name(), version=version['version'],
                             metadata=version.pop('metadata', None), data=None,
                             host=self._arctic_lib.arctic.mongo_host)

    def _add_new_version_using_reference(self, symbol, new_version, reference_version, prune_previous_version):
        # Attention: better not use this method following an append.
        # It is dangerous because if it deletes the version at the last_look, the segments added by the
        # append are dangling (if prune_previous_version is False) and can cause potentially corruption.
        constraints = new_version and \
                      reference_version and \
                      new_version['symbol'] == reference_version['symbol'] and \
                      new_version['_id'] != reference_version['_id'] and \
                      new_version['base_version_id']
        assert constraints
        # There is always a small risk here another process in between these two calls (above/below)
        # to delete the reference_version, which may happen to be the last parent entry in the data segments.
        # In this case the segments will be deleted by the other process,
        # and the new version's "base_version_id" won't be referenced by any segments.
        # Do a naive check for concurrent mods
        lastv_seqn = self._last_version_seqnum(symbol)
        if lastv_seqn != new_version['version']:
            raise OperationFailure("The symbol {} has been modified concurrently ({} != {})".format(
                symbol, lastv_seqn, new_version['version']))

        # Insert the new version into the version DB
        # (must come before the pruning, otherwise base version won't be preserved)
        self._insert_version(new_version)

        # Check if in the meanwhile the reference version (based on which we updated incrementally) has been removed
        last_look = self._versions.find_one({'_id': reference_version['_id']})
        if last_look is None or last_look.get('deleted'):
            # Revert the change
            mongo_retry(self._versions.delete_one)({'_id': new_version['_id']})
            # Indicate the failure
            raise OperationFailure("Failed to write metadata for symbol %s. "
                                   "The previous version (%s, %d) has been removed during the update" %
                                   (symbol, str(reference_version['_id']), reference_version['version']))

        if prune_previous_version and reference_version:
            self._prune_previous_versions(symbol, new_version_shas=new_version.get(FW_POINTERS_REFS_KEY))

        logger.debug('Finished updating versions with new metadata for %s', symbol)

        return VersionedItem(symbol=symbol, library=self._arctic_lib.get_name(), version=new_version['version'],
                             metadata=new_version.get('metadata'), data=None,
                             host=self._arctic_lib.arctic.mongo_host)

    @mongo_retry
    def write_metadata(self, symbol, metadata, prune_previous_version=True, **kwargs):
        """
        Write 'metadata' under the specified 'symbol' name to this library.
        The data will remain unchanged. A new version will be created.
        If the symbol is missing, it causes a write with empty data (None, pickled, can't append)
        and the supplied metadata.
        Returns a VersionedItem object only with a metadata element.
        Fast operation: Zero data/segment read/write operations.

        Parameters
        ----------
        symbol : `str`
            symbol name for the item
        metadata : `dict` or `None`
            dictionary of metadata to persist along with the symbol
        prune_previous_version : `bool`
            Removes previous (non-snapshotted) versions from the database.
            Default: True
        kwargs :
            passed through to the write handler (only used if symbol does not already exist or is deleted)

        Returns
        -------
        `VersionedItem`
            VersionedItem named tuple containing the metadata of the written symbol's version document in the store.
        """
        # Make a normal write with empty data and supplied metadata if symbol does not exist
        try:
            previous_version = self._read_metadata(symbol)
        except NoDataFoundException:
            return self.write(symbol, data=None, metadata=metadata,
                              prune_previous_version=prune_previous_version, **kwargs)

        # Reaching here means that and/or metadata exist and we are set to update the metadata
        new_version_num = self._version_nums.find_one_and_update({'symbol': symbol},
                                                                 {'$inc': {'version': 1}},
                                                                 upsert=True, new=True)['version']

        # Populate the new version entry, preserving existing data, and updating with the supplied metadata
        version = {k: previous_version[k] for k in previous_version.keys() if k != 'parent'}   # don't copy snapshots
        version['_id'] = bson.ObjectId()
        version['version'] = new_version_num
        version['metadata'] = metadata
        version['base_version_id'] = previous_version.get('base_version_id', previous_version['_id'])

        return self._add_new_version_using_reference(symbol, version, previous_version, prune_previous_version)

    @mongo_retry
    def restore_version(self, symbol, as_of, prune_previous_version=True):
        """
        Restore the specified 'symbol' data and metadata to the state of a given version/snapshot/date.
        Returns a VersionedItem object only with a metadata element.
        Fast operation: Zero data/segment read/write operations.

        Parameters
        ----------
        symbol : `str`
            symbol name for the item
        as_of : `str` or `int` or `datetime.datetime`
            Return the data as it was as_of the point in time.
            `int` : specific version number
            `str` : snapshot name which contains the version
            `datetime.datetime` : the version of the data that existed as_of the requested point in time
        prune_previous_version : `bool`
            Removes previous (non-snapshotted) versions from the database.
            Default: True

        Returns
        -------
        `VersionedItem`
            VersionedItem named tuple containing the metadata of the written symbol's version document in the store.
        """
        # TODO: This operation is tricky as it may create history branches and lead to corrupted symbols.
        #       To avoid this we do concat_rewrite (see Issue #579)
        #       Investigate how this can be optimized and maintain safety (i.e. avoid read/write with serialization
        #       and compression costs, but instead:
        #       clone segments (server-side?) / crate new (base) version / update segments' parent).

        version_to_restore = self._read_metadata(symbol, as_of=as_of)

        # At this point it is guaranteed that the as_of version exists and doesn't have the symbol marked as deleted.
        # If we try to restore the last version, do nothing (No-Op) and return the associated VesionedItem.
        if self._last_version_seqnum(symbol) == version_to_restore['version']:
            return VersionedItem(symbol=symbol, library=self._arctic_lib.get_name(),
                                 version=version_to_restore['version'],
                                 host=self._arctic_lib.arctic.mongo_host,
                                 metadata=version_to_restore.pop('metadata', None), data=None)

        # Read the existing data from as_of
        item = self.read(symbol, as_of=as_of)

        # Write back, creating a new base version
        new_item = self.write(symbol,
                              data=item.data, metadata=item.metadata, prune_previous_version=prune_previous_version)
        return new_item

    @mongo_retry
    def _find_prunable_version_ids(self, symbol, keep_mins):
        """
        Find all non-snapshotted versions of a symbol that are older than a version that's at least keep_mins
        minutes old.

        Based on documents available on the secondary.
        """
        read_preference = ReadPreference.SECONDARY_PREFERRED if keep_mins > 0 else ReadPreference.PRIMARY
        versions = self._versions.with_options(read_preference=read_preference)
        query = {'symbol': symbol,
                 # Not snapshotted
                 '$or': [{'parent': {'$exists': False}}, {'parent': []}],
                 # At least 'keep_mins' old
                 '_id': {'$lt': bson.ObjectId.from_datetime(dt.utcnow()
                                                            # Add one second as the ObjectId
                                                            # str has random fuzz
                                                            + timedelta(seconds=1)
                                                            - timedelta(minutes=keep_mins)
                                                            )
                         }
                 }
        cursor = versions.find(query,
                               # Using version number here instead of _id as there's a very unlikely case
                               # where the versions are created on different hosts or processes at exactly
                               # the same time.
                               sort=[('version', pymongo.DESCENDING)],
                               # Guarantees at least one version is kept
                               skip=1,
                               projection={'_id': 1, FW_POINTERS_REFS_KEY: 1, FW_POINTERS_CONFIG_KEY: 1},
                               )
        return {v['_id']: ([bson.binary.Binary(x) for x in v.get(FW_POINTERS_REFS_KEY, [])], get_fwptr_config(v))
                for v in cursor}

    @mongo_retry
    def _find_base_version_ids(self, symbol, version_ids):
        """
        Return all base_version_ids for a symbol that are not bases of version_ids
        """
        cursor = self._versions.find({'symbol': symbol,
                                      '_id': {'$nin': version_ids},
                                      'base_version_id': {'$exists': True},
                                      },
                                     projection={'base_version_id': 1})
        return [version["base_version_id"] for version in cursor]

    def _prune_previous_versions(self, symbol, keep_mins=120, keep_version=None, new_version_shas=None):
        """
        Prune versions, not pointed at by snapshots which are at least keep_mins old. Prune will never
        remove all versions.
        """
        new_version_shas = new_version_shas if new_version_shas else []
        prunable_ids_to_shas = self._find_prunable_version_ids(symbol, keep_mins)
        prunable_ids = list(prunable_ids_to_shas.keys())
        if keep_version is not None:
            try:
                prunable_ids.remove(keep_version)
            except ValueError:
                pass
        if not prunable_ids:
            return

        base_version_ids = self._find_base_version_ids(symbol, prunable_ids)
        version_ids = list(set(prunable_ids) - set(base_version_ids))
        if not version_ids:
            return

        # Delete the version documents
        mongo_retry(self._versions.delete_many)({'_id': {'$in': version_ids}})

        prunable_ids_to_shas = {k: prunable_ids_to_shas[k] for k in version_ids}

        # The new version has not been written yet, so make sure that any SHAs pointed by it are preserved
        shas_to_delete = [sha for v in prunable_ids_to_shas.values() for sha in v[0] if sha not in new_version_shas]

        # Cleanup any chunks
        mongo_retry(cleanup)(self._arctic_lib, symbol, version_ids, self._versions,
                             shas_to_delete=shas_to_delete,
                             pointers_cfgs=[v[1] for v in prunable_ids_to_shas.values()])

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
        # TODO: for FW pointers, if the above statement fails, they we have no way to delete the orphaned segments.
        #       This would be possible only via FSCK, or by moving the above statement at the end of this method,
        #       but with the risk of failing to delelte the version catastrophically, and ending up with a corrupted v.
        if do_cleanup:
            cleanup(self._arctic_lib, symbol, [version['_id']], self._versions,
                    shas_to_delete=tuple(bson.binary.Binary(s) for s in version.get(FW_POINTERS_REFS_KEY, [])),
                    pointers_cfgs=(get_fwptr_config(version), ))

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
        logger.info("Deleting data item: %r from %r" % (symbol, self._arctic_lib.get_name()))
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

    @mongo_retry
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

    @mongo_retry
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

    @mongo_retry
    def list_snapshots(self):
        """
        List the snapshots in the library

        Returns
        -------
        string list of snapshot names
        """
        return dict((i['name'], i['metadata']) for i in self._snapshots.find())

    @mongo_retry
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
        # Cleanup unreachable SHAs (forward pointers)
        self._cleanup_unreachable_shas(dry_run)
        # Cleanup Orphaned Snapshots
        self._cleanup_orphaned_versions(dry_run)

    def _cleanup_unreachable_shas(self, dry_run):
        lib = self
        chunks_coll = lib._collection
        versions_coll = chunks_coll.versions

        for symbol in chunks_coll.distinct('symbol'):
            logger.debug('Checking %s (forward pointers)' % symbol)

            all_symbol_pointers_cfgs = _get_symbol_pointer_cfgs(symbol, versions_coll)

            if FwPointersCfg.DISABLED not in all_symbol_pointers_cfgs:
                # Obtain the SHAs which are no longer pointed to by any version
                symbol_alive_shas = get_symbol_alive_shas(symbol, versions_coll)
                all_symbol_shas = set(chunks_coll.distinct('sha', {'symbol': symbol}))
                unreachable_shas = all_symbol_shas - symbol_alive_shas

                logger.info("Cleaning up {} SHAs for symbol {}".format(len(unreachable_shas), symbol))
                if not dry_run:
                    # Be liberal with the generation time.
                    id_time_constraint = {'$lt': bson.ObjectId.from_datetime(dt.now() - timedelta(days=1))}
                    # Do delete the data segments
                    chunks_coll.delete_many({
                        '_id': id_time_constraint,  # can't rely on the parent field only for fw-pointers
                        'symbol': symbol,
                        'parent': id_time_constraint,
                        'sha': {'$in': list(unreachable_shas)}})

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
                chunk_count = mongo_count(chunks_coll, filter={'symbol': symbol, 'parent': x})
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
                # This is now able to handle safely symbols which have both forward and legacy/parent pointers
                cleanup(lib._arctic_lib, symbol, leaked_versions, versions_coll)

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
            ver_count = mongo_count(versions_coll, filter={'parent': x})
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
