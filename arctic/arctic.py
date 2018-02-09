import logging
import os

import pymongo
from pymongo.errors import OperationFailure, AutoReconnect
import threading

from ._util import indent
from .auth import authenticate, get_auth
from .decorators import mongo_retry
from .exceptions import LibraryNotFoundException, ArcticException, QuotaExceededException
from .hooks import get_mongodb_uri
from .store import version_store, bson_store, metadata_store
from .tickstore import tickstore, toplevel
from .chunkstore import chunkstore
from six import string_types


__all__ = ['Arctic', 'VERSION_STORE', 'METADATA_STORE', 'TICK_STORE', 'CHUNK_STORE', 'register_library_type']

logger = logging.getLogger(__name__)

# Default Arctic application name: 'arctic'
APPLICATION_NAME = 'arctic'
VERSION_STORE = version_store.VERSION_STORE_TYPE
METADATA_STORE = metadata_store.METADATA_STORE_TYPE
TICK_STORE = tickstore.TICK_STORE_TYPE
CHUNK_STORE = chunkstore.CHUNK_STORE_TYPE
LIBRARY_TYPES = {version_store.VERSION_STORE_TYPE: version_store.VersionStore,
                 tickstore.TICK_STORE_TYPE: tickstore.TickStore,
                 toplevel.TICK_STORE_TYPE: toplevel.TopLevelTickStore,
                 chunkstore.CHUNK_STORE_TYPE: chunkstore.ChunkStore,
                 bson_store.BSON_STORE_TYPE: bson_store.BSONStore,
                 metadata_store.METADATA_STORE_TYPE: metadata_store.MetadataStore
                 }


def register_library_type(name, type_):
    """
    Register a Arctic Library Type handler
    """
    if name in LIBRARY_TYPES:
        raise ArcticException("Library %s already registered as %s" % (name, LIBRARY_TYPES[name]))
    LIBRARY_TYPES[name] = type_


class Arctic(object):
    """
    The Arctic class is a top-level God object, owner of all arctic_<user> databases
    accessible in Mongo.
    Each database contains one or more ArcticLibrarys which may have implementation
    specific functionality.

    Current Mongo Library types:
       - arctic.VERSION_STORE - Versioned store for chunked Pandas and numpy objects
                                (other Python types are pickled)
       - arctic.TICK_STORE - Tick specific library. Supports 'snapshots', efficiently
                             stores updates, not versioned.
       - arctic.METADATA_STORE - Stores metadata with timestamps

    Arctic and ArcticLibrary are responsible for Connection setup, authentication,
    dispatch to the appropriate library implementation, and quotas.
    """
    DB_PREFIX = 'arctic'
    METADATA_COLL = "ARCTIC"
    METADATA_DOC_ID = "ARCTIC_META"

    _MAX_CONNS = 4
    __conn = None

    def __init__(self, mongo_host, app_name=APPLICATION_NAME, allow_secondary=False,
                 socketTimeoutMS=10 * 60 * 1000, connectTimeoutMS=2 * 1000,
                 serverSelectionTimeoutMS=30 * 1000):
        """
        Constructs a Arctic Datastore.

        Parameters:
        -----------
        mongo_host: A MongoDB hostname, alias or Mongo Connection

        app_name: `str` is the name of application used for resolving credentials when
            authenticating against the mongo_host.
            We will fetch credentials using the authentication hook.
            Teams should override this such that different applications don't accidentally
            run with privileges to other applications' databases

        allow_secondary: `bool` indicates if we allow reads against
             secondary members in the cluster.  These reads may be
             a few seconds behind (but are usually split-second up-to-date).

        serverSelectionTimeoutMS: `int` the main tunable used for configuring how long
            the pymongo driver will spend on MongoDB cluster discovery.  This parameter
            takes precedence over connectTimeoutMS: https://jira.mongodb.org/browse/DRIVERS-222

        """
        self._application_name = app_name
        self._library_cache = {}
        self._allow_secondary = allow_secondary
        self._socket_timeout = socketTimeoutMS
        self._connect_timeout = connectTimeoutMS
        self._server_selection_timeout = serverSelectionTimeoutMS
        self._lock = threading.RLock()
        self._pid = os.getpid()

        if isinstance(mongo_host, string_types):
            self.mongo_host = mongo_host
        else:
            self.__conn = mongo_host
            # Workaround for: https://jira.mongodb.org/browse/PYTHON-927
            mongo_host.server_info()
            self.mongo_host = ",".join(["{}:{}".format(x[0], x[1]) for x in mongo_host.nodes])
            self._adminDB = self._conn.admin

    @property
    @mongo_retry
    def _conn(self):
        with self._lock:
            # We must make sure that no MongoClient instances are used from parent after fork:
            #    http://api.mongodb.com/python/current/faq.html#using-pymongo-with-multiprocessing
            curr_pid = os.getpid()
            if curr_pid != self._pid:
                self._pid = curr_pid  # this line has to precede reset() otherwise we get to eternal recursion
                self.reset()  # also triggers re-auth

            if self.__conn is None:
                host = get_mongodb_uri(self.mongo_host)
                logger.info("Connecting to mongo: {0} ({1})".format(self.mongo_host, host))
                self.__conn = pymongo.MongoClient(host=host,
                                                   maxPoolSize=self._MAX_CONNS,
                                                   socketTimeoutMS=self._socket_timeout,
                                                   connectTimeoutMS=self._connect_timeout,
                                                   serverSelectionTimeoutMS=self._server_selection_timeout)
                self._adminDB = self.__conn.admin

                # Authenticate against admin for the user
                auth = get_auth(self.mongo_host, self._application_name, 'admin')
                if auth:
                    authenticate(self._adminDB, auth.user, auth.password)

                # Accessing _conn is synchronous. The new PyMongo driver may be lazier than the previous.
                # Force a connection.
                self.__conn.server_info()

            return self.__conn

    def reset(self):
        logger.debug("Arctic.reset()")
        with self._lock:
            if self.__conn is not None:
                self.__conn.close()
                self.__conn = None
            for _, l in self._library_cache.items():
                if hasattr(l, '_reset') and callable(l._reset):
                    logger.debug("Library reset() %s" % l)
                    l._reset()  # the existence of _reset() is not guaranteed/enforced, it also triggers re-auth

    def __str__(self):
        return "<Arctic at %s, connected to %s>" % (hex(id(self)), str(self._conn))

    def __repr__(self):
        return str(self)

    def __getstate__(self):
        return {'mongo_host': self.mongo_host,
                'app_name': self._application_name,
                'allow_secondary': self._allow_secondary,
                'socketTimeoutMS': self._socket_timeout,
                'connectTimeoutMS': self._connect_timeout,
                'serverSelectionTimeoutMS': self._server_selection_timeout}

    def __setstate__(self, state):
        return Arctic.__init__(self, **state)

    @mongo_retry
    def list_libraries(self):
        """
        Returns
        -------
        list of Arctic library names
        """
        libs = []
        for db in self._conn.database_names():
            if db.startswith(self.DB_PREFIX + '_'):
                for coll in self._conn[db].collection_names():
                    if coll.endswith(self.METADATA_COLL):
                        libs.append(db[len(self.DB_PREFIX) + 1:] + "." + coll[:-1 * len(self.METADATA_COLL) - 1])
            elif db == self.DB_PREFIX:
                for coll in self._conn[db].collection_names():
                    if coll.endswith(self.METADATA_COLL):
                        libs.append(coll[:-1 * len(self.METADATA_COLL) - 1])
        return libs

    @mongo_retry
    def initialize_library(self, library, lib_type=VERSION_STORE, **kwargs):
        """
        Create an Arctic Library or a particular type.

        Parameters
        ----------
        library : `str`
            The name of the library. e.g. 'library' or 'user.library'

        lib_type : `str`
            The type of the library.  e.g. arctic.VERSION_STORE or arctic.TICK_STORE
            Or any type registered with register_library_type
            Default: arctic.VERSION_STORE

        kwargs :
            Arguments passed to the Library type for initialization.
        """
        l = ArcticLibraryBinding(self, library)
        # check that we don't create too many namespaces
        # can be disabled check_library_count=False
        check_library_count = kwargs.pop('check_library_count', True)
        if len(self._conn[l.database_name].collection_names()) > 5000 and check_library_count:
            raise ArcticException("Too many namespaces %s, not creating: %s" %
                                  (len(self._conn[l.database_name].collection_names()), library))
        l.set_library_type(lib_type)
        LIBRARY_TYPES[lib_type].initialize_library(l, **kwargs)
        # Add a 10G quota just in case the user is calling this with API.
        if not l.get_quota():
            l.set_quota(10 * 1024 * 1024 * 1024)

    @mongo_retry
    def delete_library(self, library):
        """
        Delete an Arctic Library, and all associated collections in the MongoDB.

        Parameters
        ----------
        library : `str`
            The name of the library. e.g. 'library' or 'user.library'
        """
        l = ArcticLibraryBinding(self, library)
        colname = l.get_top_level_collection().name
        logger.info('Dropping collection: %s' % colname)
        l._db.drop_collection(colname)
        for coll in l._db.collection_names():
            if coll.startswith(colname + '.'):
                logger.info('Dropping collection: %s' % coll)
                l._db.drop_collection(coll)
        if library in self._library_cache:
            del self._library_cache[library]
            del self._library_cache[l.get_name()]

    def get_library(self, library):
        """
        Return the library instance.  Can generally use slicing to return the library:
            arctic_store[library]

        Parameters
        ----------
        library : `str`
            The name of the library. e.g. 'library' or 'user.library'
        """
        if library in self._library_cache:
            return self._library_cache[library]

        try:
            error = None
            l = ArcticLibraryBinding(self, library)
            lib_type = l.get_library_type()
        except (OperationFailure, AutoReconnect) as e:
            error = e

        if error:
            raise LibraryNotFoundException("Library %s was not correctly initialized in %s.\nReason: %r)" %
                                           (library, self, error))
        elif not lib_type:
            raise LibraryNotFoundException("Library %s was not correctly initialized in %s." %
                                           (library, self))
        elif lib_type not in LIBRARY_TYPES:
            raise LibraryNotFoundException("Couldn't load LibraryType '%s' for '%s' (has the class been registered?)" %
                                           (lib_type, library))
        instance = LIBRARY_TYPES[lib_type](l)
        self._library_cache[library] = instance
        # The library official name may be different from 'library': e.g. 'library' vs 'user.library'
        self._library_cache[l.get_name()] = instance
        return self._library_cache[library]

    def __getitem__(self, key):
        if isinstance(key, string_types):
            return self.get_library(key)
        else:
            raise ArcticException("Unrecognised library specification - use [libraryName]")

    def set_quota(self, library, quota):
        """
        Set a quota (in bytes) on this user library.  The quota is 'best effort',
        and should be set conservatively.

        Parameters
        ----------
        library : `str`
            The name of the library. e.g. 'library' or 'user.library'

        quota : `int`
            Advisory quota for the library - in bytes
        """
        l = ArcticLibraryBinding(self, library)
        l.set_quota(quota)

    def get_quota(self, library):
        """
        Return the quota currently set on the library.

        Parameters
        ----------
        library : `str`
            The name of the library. e.g. 'library' or 'user.library'
        """
        l = ArcticLibraryBinding(self, library)
        return l.get_quota()

    def check_quota(self, library):
        """
        Check the quota on the library, as would be done during normal writes.

        Parameters
        ----------
        library : `str`
            The name of the library. e.g. 'library' or 'user.library'

        Raises
        ------
        arctic.exceptions.QuotaExceededException if the quota has been exceeded
        """
        l = ArcticLibraryBinding(self, library)
        l.check_quota()

    def rename_library(self, from_lib, to_lib):
        """
        Renames a library

        Parameters
        ----------
        from_lib: str
            The name of the library to be renamed
        to_lib: str
            The new name of the library
        """
        to_colname = to_lib
        if '.' in from_lib and '.' in to_lib:
            if from_lib.split('.')[0] != to_lib.split('.')[0]:
                raise ValueError("Collection can only be renamed in the same database")
            to_colname = to_lib.split('.')[1]

        l = ArcticLibraryBinding(self, from_lib)
        colname = l.get_top_level_collection().name

        logger.info('Renaming collection: %s' % colname)
        l._db[colname].rename(to_colname)
        for coll in l._db.collection_names():
            if coll.startswith(colname + '.'):
                l._db[coll].rename(coll.replace(colname, to_colname))

        if from_lib in self._library_cache:
            del self._library_cache[from_lib]
            del self._library_cache[l.get_name()]

    def get_library_type(self, lib):
        """
        Returns the type of the library

        Parameters
        ----------
        lib: str
            the library
        """
        l = ArcticLibraryBinding(self, lib)
        return l.get_library_type()


class ArcticLibraryBinding(object):
    """
    The ArcticLibraryBinding type holds the binding between the library name and the
    concrete implementation of the library.

    Also provides access to additional metadata about the library
        - Access to the library's top-level collection
        - Enforces quota on the library
        - Access to custom metadata about the library
    """
    DB_PREFIX = Arctic.DB_PREFIX
    TYPE_FIELD = "TYPE"
    QUOTA = 'QUOTA'

    quota = None
    quota_countdown = 0

    @classmethod
    def _parse_db_lib(clz, library):
        """
        Returns the canonical (database_name, library) for the passed in
        string 'library'.
        """
        database_name = library.split('.', 2)
        if len(database_name) == 2:
            library = database_name[1]
            if database_name[0].startswith(clz.DB_PREFIX):
                database_name = database_name[0]
            else:
                database_name = clz.DB_PREFIX + '_' + database_name[0]
        else:
            database_name = clz.DB_PREFIX
        return database_name, library

    def __init__(self, arctic, library):
        self.arctic = arctic
        self._curr_conn = self.arctic._conn
        self._lock = threading.RLock()
        database_name, library = self._parse_db_lib(library)
        self.library = library
        self.database_name = database_name
        self._auth(self.arctic._conn[self.database_name])

    @property
    def _db(self):
        with self._lock:
            arctic_conn = self.arctic._conn
            if arctic_conn is not self._curr_conn:
                self._auth(arctic_conn[self.database_name])  # trigger re-authentication if Arctic has been reset
                self._curr_conn = arctic_conn
        return self.arctic._conn[self.database_name]

    @property
    def _library_coll(self):
        return self._db[self.library]

    def __str__(self):
        return """<ArcticLibrary at %s, %s.%s>
%s""" % (hex(id(self)), self._db.name, self._library_coll.name, indent(str(self.arctic), 4))

    def __repr__(self):
        return str(self)

    def __getstate__(self):
        return {'arctic': self.arctic, 'library': '.'.join([self.database_name, self.library])}

    def __setstate__(self, state):
        return ArcticLibraryBinding.__init__(self, state['arctic'], state['library'])

    @mongo_retry
    def _auth(self, database):
        #Get .mongopass details here
        if not hasattr(self.arctic, 'mongo_host'):
            return

        auth = get_auth(self.arctic.mongo_host, self.arctic._application_name, database.name)
        if auth:
            authenticate(database, auth.user, auth.password)

    def reset_auth(self):
        logger.debug("reset_auth() %s" % self)
        self._auth(self._db)

    def get_name(self):
        return self._db.name + '.' + self._library_coll.name

    def get_top_level_collection(self):
        """
        Return the top-level collection for the Library.  This collection is to be used
        for storing data.

        Note we expect (and callers require) this collection to have default read-preference: primary
        The read path may choose to reduce this if secondary reads are allowed.
        """
        return self._library_coll

    def set_quota(self, quota_bytes):
        """
        Set a quota (in bytes) on this user library.  The quota is 'best effort',
        and should be set conservatively.

        A quota of 0 is 'unlimited'
        """
        self.set_library_metadata(ArcticLibraryBinding.QUOTA, quota_bytes)
        self.quota = quota_bytes
        self.quota_countdown = 0

    def get_quota(self):
        """
        Get the current quota on this user library.
        """
        return self.get_library_metadata(ArcticLibraryBinding.QUOTA)

    def check_quota(self):
        """
        Check whether the user is within quota.  Should be called before
        every write.  Will raise() if the library has exceeded its allotted
        quota.
        """
        # Don't check on every write, that would be slow
        if self.quota_countdown > 0:
            self.quota_countdown -= 1
            return

        # Re-cache the quota after the countdown
        self.quota = self.get_library_metadata(ArcticLibraryBinding.QUOTA)
        if self.quota is None or self.quota == 0:
            self.quota = 0
            return

        # Figure out whether the user has exceeded their quota
        library = self.arctic[self.get_name()]
        stats = library.stats()

        def to_gigabytes(bytes_):
            return bytes_ / 1024. / 1024. / 1024.

        # Have we exceeded our quota?
        size = stats['totals']['size']
        count = stats['totals']['count']
        if size >= self.quota:
            raise QuotaExceededException("Mongo Quota Exceeded: %s %.3f / %.0f GB used" % (
                                         '.'.join([self.database_name, self.library]),
                                         to_gigabytes(size),
                                         to_gigabytes(self.quota)))

        # Quota not exceeded, print an informational message and return
        try:
            avg_size = size // count if count > 1 else 100 * 1024
            remaining = self.quota - size
            remaining_count = remaining / avg_size
            if remaining_count < 100 or float(remaining) / self.quota < 0.1:
                logger.warning("Mongo Quota: %s %.3f / %.0f GB used" % (
                                '.'.join([self.database_name, self.library]),
                                to_gigabytes(size),
                                to_gigabytes(self.quota)))
            else:
                logger.info("Mongo Quota: %s %.3f / %.0f GB used" % (
                                '.'.join([self.database_name, self.library]),
                                to_gigabytes(size),
                                to_gigabytes(self.quota)))

            # Set-up a timer to prevent us for checking for a few writes.
            # This will check every average half-life
            self.quota_countdown = int(max(remaining_count // 2, 1))
        except Exception as e:
            logger.warning("Encountered an exception while calculating quota statistics: %s" % str(e))

    def get_library_type(self):
        return self.get_library_metadata(ArcticLibraryBinding.TYPE_FIELD)

    def set_library_type(self, lib_type):
        self.set_library_metadata(ArcticLibraryBinding.TYPE_FIELD, lib_type)

    @mongo_retry
    def get_library_metadata(self, field):
        lib_metadata = self._library_coll[self.arctic.METADATA_COLL].find_one({"_id": self.arctic.METADATA_DOC_ID})
        if lib_metadata is not None:
            return lib_metadata.get(field)
        else:
            return None

    @mongo_retry
    def set_library_metadata(self, field, value):
        self._library_coll[self.arctic.METADATA_COLL].update_one({'_id': self.arctic.METADATA_DOC_ID},
                                                                 {'$set': {field: value}}, upsert=True)
