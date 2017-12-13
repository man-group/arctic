import pytest
import time
import numpy as np
import pandas as pd
from datetime import datetime as dt
from mock import patch
from pandas.util.testing import assert_frame_equal

from arctic.arctic import Arctic, VERSION_STORE
from arctic.exceptions import LibraryNotFoundException, QuotaExceededException, NoDataFoundException

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
    c = arctic._conn
    assert arctic[library_name]._arctic_lib._curr_conn is c
    arctic.reset()
    assert c is not arctic._conn
    assert len(c.nodes) == 0
    assert arctic[library_name]._arctic_lib._curr_conn is c


def test_re_authenticate_on_arctic_reset(mongo_host, library_name):
    from collections import namedtuple
    Cred = namedtuple('Cred', 'user, password')
    with patch('arctic.arctic.authenticate') as auth_mock, \
            patch('arctic.arctic.get_auth') as get_auth_mock:
        auth_mock.return_value = True
        get_auth_mock.return_value = Cred(user='a_username', password='a_passwd')
        arctic = Arctic(mongo_host=mongo_host)
        arctic.initialize_library(library_name, VERSION_STORE)
        vstore = arctic[library_name]
        vstore.list_symbols()
        auth_mock.reset_mock()
        arctic.reset()
        assert auth_mock.call_count > 0
        auth_mock.reset_mock()
        vstore.list_symbols()
        assert auth_mock.call_count == 0


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


def test_lib_rename_namespace(arctic):
    arctic.initialize_library('namespace.test')
    l = arctic['namespace.test']
    l.write('test_data', 'abc')

    with pytest.raises(ValueError) as e:
        arctic.rename_library('namespace.test', 'new_namespace.test')
    assert('Collection can only be renamed in the same database' in str(e))

    arctic.rename_library('namespace.test', 'namespace.newlib')
    l = arctic['namespace.newlib']
    assert(l.read('test_data').data == 'abc')

    with pytest.raises(LibraryNotFoundException) as e:
        l = arctic['namespace.test']
    assert('Library namespace.test' in str(e))
    assert('namespace.test' not in arctic.list_libraries())


def test_lib_type(arctic):
    arctic.initialize_library('test')
    assert(arctic.get_library_type('test') == VERSION_STORE)


def _rnd_df(nrows, ncols):
    ret_df = pd.DataFrame(np.random.randn(nrows, ncols),
                          index=pd.date_range('20170101',
                          periods=nrows, freq='S'),
                          columns=[chr(i) for i in range(ord('a'), ord('a')+ncols)])
    ret_df.index.name = 'index'
    return ret_df


def test_check_write_metadata(arctic, library, library_name):
    symbol = 'FTL'
    mydf_a, mydf_b = _rnd_df(10, 5), _rnd_df(10, 5)
    with patch('arctic.arctic.logger.info') as info:
        library.write(symbol, data=mydf_a, metadata={'field_a': 1})  # creates version 1
        library.write(symbol, data=mydf_b, metadata={'field_a': 2})  # creates version 2
        library.write_metadata(symbol, metadata={'field_b': 1})  # creates version 3 (only metadata)
        v = library.read(symbol)
        assert_frame_equal(v.data, mydf_b)
        assert v.metadata == {'field_b': 1}
        assert library._read_metadata(symbol).get('version') == 3
        assert_frame_equal(library.read(symbol, as_of=1).data, mydf_a)


def test_check_write_metadata_new_symbol(arctic, library, library_name):
    symbol = 'FTL'
    with patch('arctic.arctic.logger.info') as info:
        library.write_metadata(symbol, metadata={'field_b': 1})  # creates version 1 (only metadata)
        v = library.read(symbol)
        assert v.data == None
        assert v.metadata == {'field_b': 1}
        assert library._read_metadata(symbol).get('version') == 1


def test_check_write_metadata_after_append(arctic, library, library_name):
    symbol = 'FTL'
    mydf_a, mydf_b = _rnd_df(10, 5), _rnd_df(10, 5)
    with patch('arctic.arctic.logger.info') as info:
        library.write(symbol, data=mydf_a, metadata={'field_a': 1})  # creates version 1
        library.append(symbol, data=mydf_b, metadata={'field_a': 2})  # creates version 2
        library.write_metadata(symbol, metadata={'field_b': 1})  # creates version 3
        v = library.read(symbol)
        assert_frame_equal(v.data, mydf_a.append(mydf_b))
        assert v.metadata == {'field_b': 1}
        assert library._read_metadata(symbol).get('version') == 3


def test_check_write_metadata_purge_previous_versions(arctic, library, library_name):
    symbol = 'FTL'
    mydf_a, mydf_b, mydf_c = _rnd_df(10, 5), _rnd_df(10, 5), _rnd_df(10, 5)
    with patch('arctic.arctic.logger.info') as info:
        library.write(symbol, data=mydf_a, metadata={'field_a': 1})  # creates version 1
        library.write(symbol, data=mydf_b, metadata={'field_a': 2})  # creates version 2
        assert library._read_metadata(symbol).get('version') == 2
        library.write_metadata(symbol, metadata={'field_b': 1})  # creates version 3 (only metadata)

        # Trigger GC now
        library._prune_previous_versions(symbol, 0)
        time.sleep(2)

        # Assert the data
        v = library.read(symbol)
        assert_frame_equal(v.data, mydf_b)
        assert v.metadata == {'field_b': 1}

        # Check if after snapshot and deleting the symbol, the data/metadata survive
        library.snapshot('SNAP_1')
        library.delete(symbol)
        v = library.read(symbol, as_of='SNAP_1')
        assert_frame_equal(v.data, mydf_b)
        assert library._read_metadata(symbol, as_of='SNAP_1').get('version') == 3
        assert v.metadata == {'field_b': 1}


def test_check_write_metadata_delete_symbol(arctic, library, library_name):
    symbol = 'FTL'
    mydf_a = _rnd_df(10, 5)
    mydf_b = _rnd_df(10, 5)
    with patch('arctic.arctic.logger.info') as info:
        library.write(symbol, data=mydf_a, metadata={'field_a': 1})  # creates version 1
        library.write_metadata(symbol, metadata={'field_b': 1})  # creates version 2 (only metadata)

        library.delete(symbol)

        with pytest.raises(NoDataFoundException):
            library.read(symbol)

        library.write(symbol, data=mydf_b, metadata={'field_a': 1})  # creates version 1
        assert_frame_equal(library.read(symbol).data, mydf_b)


def test_check_write_metadata_snapshots(arctic, library, library_name):
    symbol = 'FTL'
    mydf_a, mydf_b = _rnd_df(10, 5), _rnd_df(10, 5)
    with patch('arctic.arctic.logger.info') as info:
        library.write(symbol, data=mydf_a, metadata={'field_a': 1})  # creates version 1
        library.snapshot('SNAP_1')
        library.write_metadata(symbol, metadata={'field_b': 1})  # creates version 2 (only metadata)
        library.snapshot('SNAP_2')
        library.write(symbol, data=mydf_b, metadata={'field_c': 1})  # creates version 3
        library.snapshot('SNAP_3')

        library._prune_previous_versions(symbol, keep_mins=0)

        v = library.read(symbol)
        assert_frame_equal(v.data, mydf_b)
        assert v.metadata == {'field_c': 1}

        v = library.read(symbol, as_of='SNAP_1')
        assert_frame_equal(v.data, mydf_a)
        assert v.metadata == {'field_a': 1}

        v = library.read(symbol, as_of='SNAP_2')
        assert_frame_equal(v.data, mydf_a)
        assert v.metadata == {'field_b': 1}


def test_restore_version(arctic, library, library_name):
    symbol = 'FTL'
    mydf_a = _rnd_df(10, 5)
    mydf_b = _rnd_df(10, 5)
    with patch('arctic.arctic.logger.info') as info:
        library.write(symbol, data=mydf_a, metadata={'field_a': 1})  # creates version 1
        library.write(symbol, data=mydf_b, metadata={'field_a': 2})  # creates version 2

        v = library.read(symbol)
        assert_frame_equal(v.data, mydf_b)
        assert v.metadata == {'field_a': 2}
        assert library._read_metadata(symbol).get('version') == 2

        library.restore_version(symbol, as_of=1)  # creates version 3

        #library._delete_version(symbol, 1)  # delete the original version to test further the robustness/dependency

        v = library.read(symbol)
        assert_frame_equal(v.data, mydf_a)
        assert v.metadata == {'field_a': 1}
        assert library._read_metadata(symbol).get('version') == 3


def test_restore_version_purging_previous_versions(arctic, library, library_name):
    symbol = 'FTL'
    mydf_a = _rnd_df(10, 5)
    mydf_b = _rnd_df(10, 5)
    with patch('arctic.arctic.logger.info') as info:
        library.write(symbol, data=mydf_a, metadata={'field_a': 1})  # creates version 1
        library.write(symbol, data=mydf_b, metadata={'field_a': 2})  # creates version 2

        library.restore_version(symbol, as_of=1)  # creates version 3

        # Trigger GC now
        library._prune_previous_versions(symbol, 0)
        time.sleep(2)

        # library._delete_version(symbol, 1)  # delete the original version to test further the robustness/dependency

        v = library.read(symbol)
        assert_frame_equal(v.data, mydf_a)
        assert v.metadata == {'field_a': 1}
        assert library._read_metadata(symbol).get('version') == 3


def test_restore_version_non_existent_version(arctic, library, library_name):
    symbol = 'FTL'
    mydf_a = _rnd_df(10, 5)
    with patch('arctic.arctic.logger.info') as info:
        library.write(symbol, data=mydf_a, metadata={'field_a': 1})  # creates version 1

        with pytest.raises(NoDataFoundException):
            library.restore_version(symbol, as_of=3)

        v = library.read(symbol)
        assert_frame_equal(v.data, mydf_a)
        assert v.metadata == {'field_a': 1}
        assert library._read_metadata(symbol).get('version') == 1


def test_restore_version_which_updated_only_metadata(arctic, library, library_name):
    symbol = 'FTL'
    mydf_a = _rnd_df(10, 5)
    mydf_b = _rnd_df(10, 5)
    with patch('arctic.arctic.logger.info') as info:
        library.write(symbol, data=mydf_a, metadata={'field_a': 1})  # creates version 1
        library.write_metadata(symbol, metadata={'field_b': 1})  # creates version 2
        library.write(symbol, data=mydf_b)  # creates version 3

        library.restore_version(symbol, as_of=2)  # creates version 4

        v = library.read(symbol)
        assert_frame_equal(v.data, mydf_a)
        assert v.metadata == {'field_b': 1}
        assert library._read_metadata(symbol).get('version') == 4


def test_restore_version_snapshot(arctic, library, library_name):
    symbol = 'FTL'
    mydf_a = _rnd_df(10, 5)
    mydf_b = _rnd_df(10, 5)
    with patch('arctic.arctic.logger.info') as info:
        library.write(symbol, data=mydf_a, metadata={'field_a': 1})  # creates version 1
        library.write_metadata(symbol, metadata={'field_b': 1})  # creates version 2
        library.restore_version(symbol, as_of=2)  # creates version 3
        library.snapshot('SNAP_1')
        library.write(symbol, data=mydf_b)  # creates version 3

        v = library.read(symbol, as_of='SNAP_1')
        assert_frame_equal(v.data, mydf_a)
        assert v.metadata == {'field_b': 1}
        assert library._read_metadata(symbol, as_of='SNAP_1').get('version') == 3
