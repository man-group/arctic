from datetime import datetime as dt
from mock import patch
from pandas.util.testing import assert_frame_equal
import pytest
import time


from arctic.arctic import Arctic, VERSION_STORE
from arctic.exceptions import LibraryNotFoundException, QuotaExceededException

from ..util import get_large_ts


def test_connect_to_Arctic_string(mongo_host):
    arctic = Arctic(mongo_host=mongo_host)
    assert arctic.list_libraries() == []
    assert arctic.mongo_host == mongo_host


def test_connect_to_Arctic_connection(mongo_server, mongo_host):
    arctic = Arctic(mongo_server.api)
    assert arctic.list_libraries() == []
    assert arctic.mongo_host == mongo_host


def test_reset_Arctic(mongo_host, library_name):
    arctic = Arctic(mongo_host=mongo_host)
    arctic.list_libraries()
    arctic.initialize_library(library_name, VERSION_STORE)
    arctic[library_name]
    c = arctic._conn
    arctic.reset()
    assert len(c.nodes) == 0


def test_simple(library):
    sym = 'symbol'
    data = get_large_ts(100)

    library.write(sym, data)
    orig = dt.now()
    time.sleep(1)  # Move the timestamp on 1ms
    data2 = get_large_ts(100)
    library.write(sym, data2, prune_previous_version=False)

    # Get the timeseries, it should be the same
    read2 = library.read(sym).data
    assert_frame_equal(read2, data2)

    # Ensure we can get the previous version
    read = library.read(sym, as_of=orig).data
    assert_frame_equal(read, data)


def test_indexes(arctic):
    c = arctic._conn
    arctic.initialize_library("library", VERSION_STORE, segment='month')
    chunk = c.arctic.library.index_information()
    assert chunk == {u'_id_': {u'key': [(u'_id', 1)], u'ns': u'arctic.library', u'v': 1},
                             u'symbol_1_parent_1_segment_1': {u'background': True,
                                                              u'key': [(u'symbol', 1),
                                                                       (u'parent', 1),
                                                                       (u'segment', 1)],
                                                              u'ns': u'arctic.library',
                                                              u'unique': True,
                                                              u'v': 1},
                             u'symbol_1_sha_1': {u'background': True,
                                                 u'key': [(u'symbol', 1), (u'sha', 1)],
                                                 u'ns': u'arctic.library',
                                                 u'unique': True,
                                                 u'v': 1},
                             u'symbol_hashed': {u'background': True,
                                                u'key': [(u'symbol', u'hashed')],
                                                u'ns': u'arctic.library',
                                                u'v': 1}}
    snapshots = c.arctic.library.snapshots.index_information()
    assert snapshots == {u'_id_': {u'key': [(u'_id', 1)],
                                               u'ns': u'arctic.library.snapshots',
                                               u'v': 1},
                                     u'name_1': {u'background': True,
                                                 u'key': [(u'name', 1)],
                                                 u'ns': u'arctic.library.snapshots',
                                                 u'unique': True,
                                                 u'v': 1}}
    versions = c.arctic.library.versions.index_information()
    assert versions == {u'_id_': {u'key': [(u'_id', 1)],
                                           u'ns': u'arctic.library.versions',
                                           u'v': 1},
                                 u'symbol_1__id_-1': {u'background': True,
                                                      u'key': [(u'symbol', 1), (u'_id', -1)],
                                                      u'ns': u'arctic.library.versions',
                                                      u'v': 1},
                                 u'symbol_1_version_-1': {u'background': True,
                                                          u'key': [(u'symbol', 1), (u'version', -1)],
                                                          u'ns': u'arctic.library.versions',
                                                          u'unique': True,
                                                          u'v': 1}}
    version_nums = c.arctic.library.version_nums.index_information()
    assert version_nums == {u'_id_': {u'key': [(u'_id', 1)],
                                               u'ns': u'arctic.library.version_nums',
                                               u'v': 1},
                                     u'symbol_1': {u'background': True,
                                                   u'key': [(u'symbol', 1)],
                                                   u'ns': u'arctic.library.version_nums',
                                                   u'unique': True,
                                                   u'v': 1}}


def test_delete_library(arctic, library, library_name):
    mongo = arctic._conn
    # create a library2 library too - ensure that this isn't deleted
    arctic.initialize_library('user.library2', VERSION_STORE, segment='month')
    library.write('asdf', get_large_ts(1))
    assert 'TEST' in mongo.arctic_test.collection_names()
    assert 'TEST.versions' in mongo.arctic_test.collection_names()
    assert 'library2' in mongo.arctic_user.collection_names()
    assert 'library2.versions' in mongo.arctic_user.collection_names()

    arctic.delete_library(library_name)
    assert 'TEST' not in mongo.arctic_user.collection_names()
    assert 'TEST.versions' not in mongo.arctic_user.collection_names()
    with pytest.raises(LibraryNotFoundException):
        arctic[library_name]
    with pytest.raises(LibraryNotFoundException):
        arctic['arctic_{}'.format(library_name)]
    assert 'library2' in mongo.arctic_user.collection_names()
    assert 'library2.versions' in mongo.arctic_user.collection_names()


def test_quota(arctic, library, library_name):
    thing = list(range(100))
    library._arctic_lib.set_quota(10)
    assert arctic.get_quota(library_name) == 10
    assert library._arctic_lib.get_quota() == 10
    library.write('thing', thing)
    with pytest.raises(QuotaExceededException):
        library.write('ts', thing)
        library.write('ts', thing)
        library.write('ts', thing)
        library.write('ts', thing)
    with pytest.raises(QuotaExceededException):
        arctic.check_quota(library_name)


def test_check_quota(arctic, library, library_name):
    with patch('arctic.arctic.logger.info') as info:
        arctic.check_quota(library_name)
    assert info.call_count == 1


def test_default_mongo_retry_timout():
    now = time.time()
    with pytest.raises(LibraryNotFoundException):
        Arctic('unresolved-host', serverSelectionTimeoutMS=0)['some.lib']
    assert time.time() - now < 1.


def test_lib_rename(arctic):
    arctic.initialize_library('test')
    l = arctic['test']
    l.write('test_data', 'abc')
    arctic.rename_library('test', 'new_name')
    l = arctic['new_name']
    assert(l.read('test_data').data == 'abc')
    with pytest.raises(LibraryNotFoundException) as e:
        l = arctic['test']
    assert('Library test' in str(e))
    assert('test' not in arctic.list_libraries())


def test_lib_type(arctic):
    arctic.initialize_library('test')
    assert(arctic.get_library_type('test') == VERSION_STORE)
