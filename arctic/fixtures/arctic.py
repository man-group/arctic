import getpass
import logging

import pytest as pytest

from .. import arctic as m
from ..store.bitemporal_store import BitemporalStore
from ..tickstore.tickstore import TICK_STORE_TYPE
from ..chunkstore.chunkstore import CHUNK_STORE_TYPE

logger = logging.getLogger(__name__)


@pytest.fixture(scope="function")
def mongo_host(mongo_server):
    return str(mongo_server.hostname) + ":" + str(mongo_server.port)


@pytest.fixture(scope="function")
def arctic(mongo_server):
    logger.info('arctic.fixtures: arctic init()')
    mongo_server.api.drop_database('arctic')
    mongo_server.api.drop_database('arctic_{}'.format(getpass.getuser()))
    arctic = m.Arctic(mongo_host=mongo_server.api)
    # Do not add global libraries here: use specific fixtures below.
    # Remember, for testing it does not usually matter what your libraries are called.
    return arctic


# A arctic which allows reads to hit the secondary
@pytest.fixture(scope="function")
def arctic_secondary(mongo_server, arctic):
    arctic = m.Arctic(mongo_host=mongo_server.api, allow_secondary=True)
    return arctic


@pytest.fixture(scope="function")
def library_name():
    return 'test.TEST'


@pytest.fixture(scope="function")
def user_library_name():
    return "{}.TEST".format(getpass.getuser())


@pytest.fixture(scope="function")
def overlay_library_name():
    return "test.OVERLAY"


@pytest.fixture(scope="function")
def library(arctic, library_name):
    # Add a single test library
    arctic.initialize_library(library_name, m.VERSION_STORE, segment='month')
    return arctic.get_library(library_name)


@pytest.fixture(scope="function")
def bitemporal_library(arctic, library_name):
    arctic.initialize_library(library_name, m.VERSION_STORE, segment='month')
    return BitemporalStore(arctic.get_library(library_name))


@pytest.fixture(scope="function")
def library_secondary(arctic_secondary, library_name):
    arctic_secondary.initialize_library(library_name, m.VERSION_STORE, segment='month')
    return arctic_secondary.get_library(library_name)


@pytest.fixture(scope="function")
def user_library(arctic, user_library_name):
    arctic.initialize_library(user_library_name, m.VERSION_STORE, segment='month')
    return arctic.get_library(user_library_name)


@pytest.fixture(scope="function")
def overlay_library(arctic, overlay_library_name):
    """ Overlay library fixture, returns a pair of libs, read-write: ${name} and read-only: ${name}_RAW
    """
    rw_name = overlay_library_name
    ro_name = '{}_RAW'.format(overlay_library_name)
    arctic.initialize_library(rw_name, m.VERSION_STORE, segment='year')
    arctic.initialize_library(ro_name, m.VERSION_STORE, segment='year')
    return arctic.get_library(rw_name), arctic.get_library(ro_name)


@pytest.fixture(scope="function")
def tickstore_lib(arctic, library_name):
    arctic.initialize_library(library_name, TICK_STORE_TYPE)
    return arctic.get_library(library_name)


@pytest.fixture(scope="function")
def chunkstore_lib(arctic, library_name):
    arctic.initialize_library(library_name, CHUNK_STORE_TYPE)
    return arctic.get_library(library_name)


@pytest.fixture(scope="function")
def ms_lib(arctic, library_name):
    arctic.initialize_library(library_name, m.METADATA_STORE)
    return arctic.get_library(library_name)
