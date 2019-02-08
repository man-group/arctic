import base64
import getpass
import logging

import bson
import pytest as pytest

from .. import arctic as m
from ..chunkstore.chunkstore import CHUNK_STORE_TYPE
from ..store.bitemporal_store import BitemporalStore
from ..tickstore.tickstore import TICK_STORE_TYPE

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
def multicolumn_store_with_uncompressed_write(mongo_server):
    """
    The database state created by this fixture is equivalent to the following operations using arctic 1.40
    or previous:

        arctic.initialize_library('arctic_test.TEST', m.VERSION_STORE, segment='month')
        library = arctic.get_library('arctic_test.TEST')
        df = pd.DataFrame([[1,2], [3,4]], index=['x','y'], columns=[['a','w'], ['a','v']])
        library.write('pandas', df)

    different from newer versions, the last write creates a uncompressed chunk.
    """
    mongo_server.api.drop_database('arctic_test')

    library_name = 'arctic_test.TEST'
    arctic = m.Arctic(mongo_host=mongo_server.api)
    arctic.initialize_library(library_name, m.VERSION_STORE, segment='month')

    db = mongo_server.api.arctic_test
    db.TEST.insert_many([
        {
            'parent': [bson.ObjectId('5ad0dc065c911d1188b512d8')],
            'data': bson.Binary(b'\x11\x00\x00\x002x\x01\x00\x01\x00\x80\x02\x00\x00\x00\x00\x00\x00\x00', 0),
            'symbol': 'pandas',
            'sha': bson.Binary(b'\xaa\\`\x0e\xc2D-\xc1_\xf7\xfd\x12\xfa\xd2\x17\x05`\x00\x98\xe2', 0),
            'compressed': True,
            '_id': bson.ObjectId('5ad0dc067934ecad404070be'),
            'segment': 0
        },
        {
            'parent': [bson.ObjectId('5ad0dc065c911d1188b512d8')],
            'data': bson.Binary(b'y\x03\x00\x00\x00\x00\x00\x00\x00\x04\x00\x00\x00\x00\x00\x00\x00', 0),
            'symbol': 'pandas',
            'sha': bson.Binary(b'\xfe=WQ\xb5\xfdL\xb7\xcavd\x85o\x04]\x04\xdb\xa8]3', 0),
            'compressed': False,
            '_id': bson.ObjectId('5ad0dc077934ecad404070bf'),
            'segment': 1
        }
    ])
    db.TEST.ARCTIC.update_one({"_id": "ARCTIC_META"}, {"$set": {"_id": "ARCTIC_META", "TYPE": "VersionStore", "QUOTA": 10737418240}})
    db.TEST.version_nums.insert_one({'symbol': 'pandas', '_id': bson.ObjectId('5ad0dc067934ecad404070bd'), 'version': 2})
    db.TEST.versions.insert_many([
        {
            'append_count': 0,
            'dtype_metadata': {
                'index': ['index'],
                'columns': ["('a', 'a')", "('w', 'v')"]
            },
            'segment_count': 1,
            'dtype': '[(\'index\', \'S1\'), ("(\'a\', \'a\')", \'<i8\'), ("(\'w\', \'v\')", \'<i8\')]',
            'symbol': 'pandas',
            'up_to': 1,
            'metadata': None,
            'sha': bson.Binary(b'\xf2\x15h\x9d\x925\x95\xa5\x0e\x95J\xc4x\xfc\xfc\xd5\x80\xe0\x1d\xef', 0),
            'shape': [-1],
            'version': 1,
            'base_sha': bson.Binary(b'\xf2\x15h\x9d\x925\x95\xa5\x0e\x95J\xc4x\xfc\xfc\xd5\x80\xe0\x1d\xef', 0),
            '_id': bson.ObjectId('5ad0dc065c911d1188b512d8'),
            'type': 'pandasdf',
            'append_size': 0
        },
        {
            'append_count': 1,
            'dtype_metadata': {
                'index': ['index'],
                'columns': ["('a', 'a')", "('w', 'v')"]
            },
            'segment_count': 2,
            'sha': bson.Binary(b'1\x83[ZO\xec\x080D\x80f\xe4@\xe4\xd3\x94yG\xe2\x08', 0),
            'dtype': '[(\'index\', \'S1\'), ("(\'a\', \'a\')", \'<i8\'), ("(\'w\', \'v\')", \'<i8\')]',
            'symbol': 'pandas',
            'up_to': 2,
            'metadata': None,
            'base_version_id': bson.ObjectId('5ad0dc065c911d1188b512d8'),
            'shape': [-1],
            'version': 2,
            'base_sha': bson.Binary(b'\xf2\x15h\x9d\x925\x95\xa5\x0e\x95J\xc4x\xfc\xfc\xd5\x80\xe0\x1d\xef', 0),
            '_id': bson.ObjectId('5ad0dc075c911d1188b512d9'),
            'type': 'pandasdf',
            'append_size': 17
        }
    ])

    return {'symbol': 'pandas', 'store': arctic.get_library('arctic_test.TEST')}


@pytest.fixture(scope="function")
def ndarray_store_with_uncompressed_write(mongo_server):
    """
    The database state created by this fixture is equivalent to the following operations using arctic 1.40
    or previous:

        arctic.initialize_library('arctic_test.TEST', m.VERSION_STORE, segment='month')
        library = arctic.get_library('arctic_test.TEST')
        arr = np.arange(2).astype([('abc', 'int64')])
        library.write('MYARR', arr[:1])
        library.write('MYARR', arr)

    different from newer versions, the last write creates a uncompressed chunk.
    """
    mongo_server.api.drop_database('arctic_test')

    library_name = 'arctic_test.TEST'
    arctic = m.Arctic(mongo_host=mongo_server.api)
    arctic.initialize_library(library_name, m.VERSION_STORE, segment='month')

    db = mongo_server.api.arctic_test
    db.TEST.insert_many([
        {
            "_id": bson.ObjectId("5ad0742ca0949de6727cf994"),
            "segment": 0,
            "sha": bson.Binary(base64.b64decode("Fk+quqPVSDfaajYJkOAvnDyXtGQ="), 0),
            "symbol": "MYARR",
            "data": bson.Binary(base64.b64decode("CAAAAIAAAAAAAAAAAA=="), 0),
            "compressed": True,
            "parent": [bson.ObjectId("5ad0742c5c911d4d80ee2ea3")]
        },
        {
            "_id": bson.ObjectId("5ad0742ca0949de6727cf995"),
            "sha": bson.Binary(base64.b64decode("eqpp8VOJBttTz0j5H+QGtOQ+r44="), 0),
            "symbol": "MYARR",
            "segment": 1,
            "data": bson.Binary(base64.b64decode("AQAAAAAAAAA="), 0),
            "compressed": False,
            "parent": [bson.ObjectId("5ad0742c5c911d4d80ee2ea3")]
        }
    ])
    db.TEST.ARCTIC.update_one({"_id": "ARCTIC_META"}, {"$set": {"_id": "ARCTIC_META", "TYPE": "VersionStore", "QUOTA": 10737418240}})
    db.TEST.versions_nums.insert_one({"_id": bson.ObjectId("5ad0742ca0949de6727cf993"), "symbol": "MYARR", "version": 2})
    db.TEST.versions.insert_many([
        {
            "_id": bson.ObjectId("5ad0742c5c911d4d80ee2ea3"),
            "append_count": 0,
            "dtype_metadata": {},
            "segment_count": 1,
            "dtype": "[('abc', '<i8')]",
            "symbol": "MYARR",
            "up_to": 1,
            "append_size": 0,
            "sha": bson.Binary(base64.b64decode("Bf5AV1MWbxJVWefJrFWGVPEHx+k="), 0),
            "shape": [-1],
            "version": 1,
            "base_sha": bson.Binary(base64.b64decode("Bf5AV1MWbxJVWefJrFWGVPEHx+k="), 0),
            "type": "ndarray",
            "metadata": None
        },
        {
            "_id": bson.ObjectId("5ad0742c5c911d4d80ee2ea4"),
            "append_count": 1,
            "dtype_metadata": {},
            "segment_count": 2,
            "base_version_id": bson.ObjectId("5ad0742c5c911d4d80ee2ea3"),
            "dtype": "[('abc', '<i8')]",
            "symbol": "MYARR",
            "up_to": 2,
            "append_size": 8,
            "sha": bson.Binary(base64.b64decode("Ax7oBxVFw1/9wKog2gfOLjbOVD8="), 0),
            "shape": [-1],
            "version": 2,
            "base_sha": bson.Binary(base64.b64decode("Bf5AV1MWbxJVWefJrFWGVPEHx+k="), 0),
            "type": "ndarray",
            "metadata": None
        }
    ])

    return {'symbol': 'MYARR', 'store': arctic.get_library('arctic_test.TEST')}


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
    # Call _create_overlay_library to avoid:
    #  RemovedInPytest4Warning: Fixture overlay_library called directly. Fixtures are not meant to be called directly
    return _overlay_library(arctic, overlay_library)


def _overlay_library(arctic, overlay_library_name):
    rw_name = overlay_library_name
    ro_name = '{}_RAW'.format(overlay_library_name)
    arctic.initialize_library(rw_name, m.VERSION_STORE, segment='year')
    arctic.initialize_library(ro_name, m.VERSION_STORE, segment='year')
    return arctic.get_library(rw_name), arctic.get_library(ro_name)


@pytest.fixture(scope="function")
def tickstore_lib(arctic, library_name):
    # Call _create_overlay_library to avoid:
    #  RemovedInPytest4Warning: Fixture overlay_library called directly. Fixtures are not meant to be called directly
    return _tickstore_lib(arctic, library_name)


def _tickstore_lib(arctic, library_name):
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
