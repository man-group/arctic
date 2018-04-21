from arctic.exceptions import ArcticException
from arctic.backends.mongo import MongoBackend
from arctic.backends.backends import LIBRARY_TYPES, VERSION_STORE, METADATA_STORE, TICK_STORE, CHUNK_STORE


__all__ = ['Arctic', 'VERSION_STORE', 'METADATA_STORE', 'TICK_STORE', 'CHUNK_STORE', 'register_library_type']


def register_library_type(name, type_):
    """
    Register a Arctic Library Type handler
    """
    if name in LIBRARY_TYPES:
        raise ArcticException("Library %s already registered as %s" % (name, LIBRARY_TYPES[name]))
    LIBRARY_TYPES[name] = type_


class Arctic(object):
    """
    The Arctic class is a top-level God object, owner of all arctic_<user> databases.
    Each database contains one or more ArcticLibrarys which may have implementation
    specific functionality.
    """

    def __init__(self, *args, **kwargs):
        """
        Constructs a Arctic Datastore.

        Parameters:
        -----------
        backend: Specifies a backend to use for data storage. Current backends:
                 - mongo
        args, kwargs: passed to backend
        """
        backend = kwargs.get('backend', 'mongo')
        if 'backend' in kwargs:
            del kwargs['backend']

        self.backend = None
        if backend == 'mongo':
            self.backend = MongoBackend(*args, **kwargs)

    @property
    def _conn(self):
        return self.backend._conn
    
    def __getattr__(self, attr):
        return getattr(self.backend, attr)

    def reset(self):
        self.backend.reset()

    def __str__(self):
        return "<Arctic at %s, connected to %s>" % (hex(id(self)), str(self._conn))

    def __repr__(self):
        return str(self)

    def __getstate__(self):
        return self.backend.__getstate__()

    def __setstate__(self, state):
        return self.backend.__setstate__(state)

    def __getitem__(self, key):
        return self.backend.__getitem__(key)

    def list_libraries(self):
        return self.backend.list_libraries()

    def initialize_library(self, library, lib_type=VERSION_STORE, **kwargs):
       return self.backend.initialize_library(library, lib_type, **kwargs)

    def delete_library(self, library):
        return self.backend.delete_library(library)

    def get_library(self, library):
        return self.backend.get_library(library)

    def set_quota(self, library, quota):
        return self.backend.set_quota(library, quota)

    def get_quota(self, library):
        return self.backend.get_quota(library)

    def check_quota(self, library):
       return self.backend.check_quota(library)

    def rename_library(self, from_lib, to_lib):
        return self.backend.rename_library(from_lib, to_lib)

    def get_library_type(self, lib):
        return self.backend.get_library_type(lib)
