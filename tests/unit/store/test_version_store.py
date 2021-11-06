import datetime
from datetime import datetime as dt, timedelta as dtd

import bson
import pymongo
import pytest
from bson import ObjectId
from mock import patch, MagicMock, sentinel, create_autospec, Mock, call
from pymongo import ReadPreference
from pymongo.collection import Collection
from pymongo.errors import OperationFailure, DuplicateKeyError

from arctic.arctic import ArcticLibraryBinding, Arctic
from arctic.date import mktz
from arctic.exceptions import DuplicateSnapshotException, NoDataFoundException
from arctic.store import version_store
from arctic.store.version_store import VersionStore, VersionedItem


def test_delete_version_version_not_found():
    with patch('arctic.store.version_store.VersionStore.__init__', return_value=None, autospec=True):
        with patch('arctic.store.version_store.logger') as logger:
            vs = version_store.VersionStore(sentinel.connection)
            vs._versions = MagicMock()
            with patch.object(vs._versions, 'find_one', return_value=None, autospec=True):
                vs._delete_version(sentinel.symbol, sentinel.version)
    logger.error.assert_called_once_with("Can't delete sentinel.symbol:sentinel.version as not found in DB")


def test_list_versions_localTime():
    # Object ID's are stored in UTC. We need to ensure that the returned times
    # for versions are in the local  TimeZone
    vs = create_autospec(VersionStore, instance=True, _versions=Mock(), _snapshots=Mock())
    mocked_snap_resp = [{'_id': 'abcde', 'name': 'snap'}]
    vs._snapshots.find.return_value = mocked_snap_resp
    vs._snapshots.find_one.return_value = mocked_snap_resp
    date = dt(2013, 4, 1, 9, 0)
    vs._versions.find.return_value = [{'_id': bson.ObjectId.from_datetime(date),
                                       'symbol': 's',
                                       'version': 10,
                                       'metadata': None,
                                       'parent': [mocked_snap_resp[0]['_id']]}]
    version = list(VersionStore.list_versions(vs, "symbol"))[0]
    local_date = date.replace(tzinfo=mktz("UTC"))
    assert version == {'symbol': version['symbol'], 'version': version['version'],
                       # We return naive datetimes in 'default' time, which is London for us
                       'date': local_date,
                       'snapshots': ['snap'],
                       'deleted': False}


def test_list_versions_no_snapshot():
    vs = create_autospec(VersionStore, instance=True, _versions=Mock(), _snapshots=Mock())
    vs._snapshots.find.return_value = []
    vs._snapshots.find_one.return_value = []
    date = dt(2013, 4, 1, 9, 0)
    vs._versions.find.return_value = [{'_id': bson.ObjectId.from_datetime(date),
                                       'symbol': 's',
                                       'version': 10,
                                       'metadata': None,
                                       'parent': []}]
    version = list(VersionStore.list_versions(vs, "symbol"))[0]
    local_date = date.replace(tzinfo=mktz("UTC"))
    assert version == {'symbol': version['symbol'],
                       'version': version['version'],
                       'date': local_date,
                       'snapshots': [],
                       'deleted': False}


def test__read_preference__allow_secondary_true():
    self = create_autospec(VersionStore)
    assert VersionStore._read_preference(self, True) == ReadPreference.NEAREST


def test__read_preference__allow_secondary_false():
    self = create_autospec(VersionStore)
    assert VersionStore._read_preference(self, False) == ReadPreference.PRIMARY


def test__read_preference__default_true():
    self = create_autospec(VersionStore, _allow_secondary=True)
    assert VersionStore._read_preference(self, None) == ReadPreference.NEAREST


def test__read_preference__default_false():
    self = create_autospec(VersionStore, _allow_secondary=False)
    assert VersionStore._read_preference(self, None) == ReadPreference.PRIMARY


def test_get_version_allow_secondary_True():
    vs = create_autospec(VersionStore, instance=True,
                         _versions=Mock())
    vs._read_preference.return_value = sentinel.read_preference
    vs._find_snapshots.return_value = 'snap'
    vs._versions.find.return_value = [{'_id': bson.ObjectId.from_datetime(dt(2013, 4, 1, 9, 0)),
                       'symbol': 's', 'version': 10}]

    VersionStore.read(vs, "symbol")
    assert vs._read_metadata.call_args_list == [call('symbol', as_of=None, read_preference=sentinel.read_preference)]
    assert vs._do_read.call_args_list == [call('symbol', vs._read_metadata.return_value, None, 
                                               date_range=None,
                                               read_preference=sentinel.read_preference)]


def test_get_version_allow_secondary_user_override_False():
    """Ensure user can override read preference when calling read"""
    vs = create_autospec(VersionStore, instance=True,
                         _versions=Mock())
    vs._read_preference.return_value = sentinel.read_preference
    vs._find_snapshots.return_value = 'snap'
    vs._versions.find.return_value = [{'_id': bson.ObjectId.from_datetime(dt(2013, 4, 1, 9, 0)),
                       'symbol': 's', 'version': 10}]

    VersionStore.read(vs, "symbol", allow_secondary=False)
    assert vs._read_metadata.call_args_list == [call('symbol', as_of=None, read_preference=sentinel.read_preference)]
    assert vs._do_read.call_args_list == [call('symbol', vs._read_metadata.return_value, None,
                                               date_range=None, 
                                               read_preference=sentinel.read_preference)]
    vs._read_preference.assert_called_once_with(False)


def test_read_as_of_LondonTime():
    # When we do a read, with naive as_of, that as_of is treated in London Time.
    vs = create_autospec(VersionStore, instance=True,
                     _versions=Mock(), _allow_secondary=False)
    VersionStore._read_metadata(vs, 'symbol', dt(2013, 4, 1, 9, 0))
    versions = vs._versions.with_options.return_value
    versions.find_one.assert_called_once_with({'symbol': 'symbol', '_id':
                                              {'$lt': bson.ObjectId.from_datetime(dt(2013, 4, 1, 9, 0, tzinfo=mktz()) + dtd(seconds=1))}},
                                             sort=[('symbol', pymongo.DESCENDING), ('version', pymongo.DESCENDING)])


def test_read_as_of_NotNaive():
    # When we do a read, with naive as_of, that as_of is treated in London Time.
    vs = create_autospec(VersionStore, instance=True,
                     _versions=Mock(), _allow_secondary=False)
    VersionStore._read_metadata(vs, 'symbol', dt(2013, 4, 1, 9, 0, tzinfo=mktz('Europe/Paris')))
    versions = vs._versions.with_options.return_value
    versions.find_one.assert_called_once_with({'symbol': 'symbol', '_id':
                                              {'$lt': bson.ObjectId.from_datetime(dt(2013, 4, 1, 9, 0, tzinfo=mktz('Europe/Paris')) + dtd(seconds=1))}},
                                             sort=[('symbol', pymongo.DESCENDING), ('version', pymongo.DESCENDING)])


def test_read_metadata_no_asof():
    # When we do a read, with naive as_of, that as_of is treated in London Time.
    vs = create_autospec(VersionStore, instance=True,
                     _versions=Mock(), _allow_secondary=False)
    VersionStore._read_metadata(vs, sentinel.symbol)
    versions = vs._versions.with_options.return_value
    assert versions.find_one.call_args_list == [call({'symbol': sentinel.symbol},
                                                         sort=[('version', pymongo.DESCENDING)])]


def test_write_check_quota():
    write_handler = Mock(write=Mock(__name__=""))
    vs = create_autospec(VersionStore, instance=True,
                     _collection=Mock(),
                     _version_nums=Mock(find_one_and_update=Mock(return_value={'version': 1})),
                     _versions=Mock(insert_one=lambda x: None),
                     _arctic_lib=create_autospec(ArcticLibraryBinding,
                                                 arctic=create_autospec(Arctic, mongo_host='some_host')))
    vs._collection.database.connection.nodes = []
    vs._write_handler.return_value = write_handler
    VersionStore.write(vs, 'sym', sentinel.data, prune_previous_version=False)
    assert vs._arctic_lib.check_quota.call_count == 1


def test_initialize_library():
    arctic_lib = create_autospec(ArcticLibraryBinding)
    arctic_lib.arctic = create_autospec(Arctic, _allow_secondary=False)
    with patch('arctic.store.version_store.enable_sharding', autospec=True) as enable_sharding:
        arctic_lib.get_top_level_collection.return_value.database.create_collection.__name__ = 'some_name'
        arctic_lib.get_top_level_collection.return_value.database.collection_names.__name__ = 'some_name'
        arctic_lib.get_top_level_collection.__name__ = 'get_top_level_collection'
        arctic_lib.get_top_level_collection.return_value.database.list_collection_names.__name__ = 'list_collection_names'
        VersionStore.initialize_library(arctic_lib, hashed=sentinel.hashed)
    assert enable_sharding.call_args_list == [call(arctic_lib.arctic, arctic_lib.get_name(), hashed=sentinel.hashed)]


def test_ensure_index():
    th = Mock()
    vs = create_autospec(VersionStore, _collection=Mock())
    with patch('arctic.store.version_store._TYPE_HANDLERS', [th]):
        VersionStore._ensure_index(vs)
    assert vs._collection.snapshots.create_index.call_args_list == [call([('name', 1)], unique=True, background=True)]
    assert vs._collection.versions.create_index.call_args_list == [
        call([('symbol', 1), ('_id', -1)], background=True),
        call([('symbol', 1), ('version', -1)], unique=True, background=True),
        call([('symbol', 1), ('version', -1), ('metadata.deleted', 1)], background=True),
    ]
    assert vs._collection.version_nums.create_index.call_args_list == [call('symbol', unique=True, background=True)]
    th._ensure_index.assert_called_once_with(vs._collection)


def test_prune_previous_versions_0_timeout():
    self = create_autospec(VersionStore, _versions=Mock())
    self.name = sentinel.name
    self._versions = create_autospec(Collection)
    self._versions.with_options.return_value.find.__name__ = 'find'
    self._versions.with_options.return_value.find.return_value = []
    with patch('arctic.store.version_store.dt') as dt:
        dt.utcnow.return_value = datetime.datetime(2013, 10, 1)
        VersionStore._find_prunable_version_ids(self, sentinel.symbol, keep_mins=0)
    assert self._versions.with_options.call_args_list == [call(read_preference=ReadPreference.PRIMARY)]
    assert self._versions.with_options.return_value.find.call_args_list == [
                                                  call({'$or': [{'parent': {'$exists': False}},
                                                                {'parent': []}],
                                                        'symbol': sentinel.symbol,
                                                        '_id': {'$lt': bson.ObjectId('524a10810000000000000000')}},
                                                       sort=[('version', -1)],
                                                       skip=1,
                                                       projection={'FW_POINTERS_CONFIG': 1, '_id': 1, 'SEGMENT_SHAS': 1}
                                                       )]


def test_read_handles_operation_failure():
    self = Mock(spec=VersionStore)
    self._read_preference.return_value = sentinel.read_preference
    self._collection = create_autospec(Collection)
    self._read_metadata.side_effect = [sentinel.meta1, sentinel.meta2]
    self._read_metadata.__name__ = 'name'
    self._do_read.__name__ = 'name'  # feh: mongo_retry decorator cares about this
    self._do_read.side_effect = [OperationFailure('error'), sentinel.read]
    VersionStore.read(self, sentinel.symbol, sentinel.as_of,
                      from_version=sentinel.from_version,
                      date_range=sentinel.date_range,
                      other_kwarg=sentinel.other_kwarg)
    # Assert that, for the two read calls, the second uses the new metadata
    assert self._do_read.call_args_list == [call(sentinel.symbol, sentinel.meta1, 
                                                 sentinel.from_version,
                                                 date_range=sentinel.date_range,
                                                 other_kwarg=sentinel.other_kwarg,
                                                 read_preference=sentinel.read_preference)]
    assert self._do_read_retry.call_args_list == [call(sentinel.symbol, sentinel.meta2,
                                                       sentinel.from_version,
                                                       date_range=sentinel.date_range,
                                                       other_kwarg=sentinel.other_kwarg,
                                                       read_preference=ReadPreference.PRIMARY)]


def test_read_reports_random_errors():
    self = create_autospec(VersionStore, _versions=Mock(), _arctic_lib=Mock(),
                           _allow_secondary=True)
    self._collection = create_autospec(Collection)
    self._do_read.__name__ = 'name'  # feh: mongo_retry decorator cares about this
    self._do_read.side_effect = Exception('bad')
    with pytest.raises(Exception) as e:
        with patch('arctic.store.version_store.log_exception') as le:
            VersionStore.read(self, sentinel.symbol, sentinel.as_of, sentinel.from_version)
    assert 'bad' in str(e.value)
    assert le.call_count == 1


def test_snapshot():
    vs = create_autospec(VersionStore, _snapshots=Mock(),
                                       _collection=Mock(),
                                       _versions=Mock())
    vs._snapshots.find_one.return_value = False
    vs._versions.update_one.__name__ = 'name'
    vs._snapshots.insert_one.__name__ = 'name'
    vs.list_symbols.return_value = ['foo', 'bar']
    VersionStore.snapshot(vs, "symbol")
    assert (vs._read_metadata.call_args_list == [call('foo', as_of=None, read_preference=ReadPreference.PRIMARY),
                                                call('bar', as_of=None, read_preference=ReadPreference.PRIMARY)] or 
                                                vs._read_metadata.call_args_list == [call('bar', as_of=None, read_preference=ReadPreference.PRIMARY),
                                                call('foo', as_of=None, read_preference=ReadPreference.PRIMARY)])


def test_list_symbols_default_pipeline():
    versions = Mock()
    vs = create_autospec(VersionStore, _versions=versions)
    versions.aggregate.return_value = []

    VersionStore.list_symbols(vs)

    pipeline = [
        {'$sort': bson.SON([('symbol', 1), ('version', -1)])},
        {'$group': {
            '_id': '$symbol',
            'deleted': {'$first': '$metadata.deleted'}
        }},
        {'$match': {'deleted': {'$ne': True}}}
    ]
    versions.aggregate.assert_called_once_with(pipeline, allowDiskUse=True)


def test_snapshot_duplicate_raises_exception():
    vs = create_autospec(VersionStore, _snapshots=Mock())
    with pytest.raises(DuplicateSnapshotException) as e:
        vs._snapshots.find_one.return_value = True
        VersionStore.snapshot(vs, 'symbol')
        assert "Snapshot 'symbol' already exists" in str(e.value)


TPL_VERSION = {'_id': ObjectId('5a2ffdf817f7041a4ff1aa82'),
               'base_version_id': ObjectId('5a2ffd5917f70412ca78d80a'),
               'append_count': 0,
               'dtype_metadata': {
                   'index': ['index'],
                   'columns': ['A', 'B', 'C', 'D']},
               'segment_count': 1,
               'symbol': 'SYM_E',
               'up_to': 3,
               'metadata': None,
               'shape': [-1],
               'version': 6,
               'type': 'pandasdf',
               'append_size': 0
               }

META_TO_WRITE = {'field_a': 1}
TEST_SYMBOL = 'FTL'
TEST_LIB = 'MYLIB'
MOCK_OBJID = ObjectId('5a2ffdf817f7041a4ff1aaaa')


def _create_mock_versionstore():
    vs = create_autospec(VersionStore, _arctic_lib=Mock(), _version_nums=Mock(), _versions=Mock())
    vs._insert_version = lambda version: VersionStore._insert_version(vs, version)
    vs._arctic_lib.get_name.return_value = TEST_LIB
    vs._read_metadata.return_value = TPL_VERSION
    vs._version_nums.find_one_and_update.return_value = {'version': TPL_VERSION['version'] + 1}
    vs._version_nums.find_one.return_value = {'version': TPL_VERSION['version'] + 1}
    vs._versions.find_one.return_value = TPL_VERSION
    vs._add_new_version_using_reference.side_effect = lambda *args: VersionStore._add_new_version_using_reference(vs, *args)
    vs._last_version_seqnum = lambda version: VersionStore._last_version_seqnum(vs, version)
    vs.write.return_value = VersionedItem(symbol=TEST_SYMBOL, library=vs._arctic_lib.get_name(),
                                          version=TPL_VERSION['version'] + 1, metadata=META_TO_WRITE, data=None,
                                          host=vs._arctic_lib.arctic.mongo_host)
    return vs


def test_write_metadata_no_previous_data():
    vs = _create_mock_versionstore()
    vs._read_metadata.side_effect = NoDataFoundException("no data found")

    assert VersionStore.write_metadata(vs, symbol=TEST_SYMBOL, metadata=META_TO_WRITE, my_custom_arg='hello') == vs.write.return_value
    assert vs._read_metadata.call_args_list == [call(TEST_SYMBOL)]
    assert vs.write.call_args_list == [call(TEST_SYMBOL, data=None, metadata=META_TO_WRITE,
                                            prune_previous_version=True, my_custom_arg='hello')]


def test_write_metadata_with_previous_data():
    vs = _create_mock_versionstore()

    expected_new_version = TPL_VERSION.copy()
    expected_new_version.update({'_id': MOCK_OBJID,
                                 'version': TPL_VERSION['version'] + 1,
                                 'metadata': META_TO_WRITE})

    expected_ret_val = VersionedItem(symbol=TEST_SYMBOL,
                                     library=vs._arctic_lib.get_name(),
                                     host=vs._arctic_lib.arctic.mongo_host,
                                     version=TPL_VERSION['version'] + 1,
                                     metadata=META_TO_WRITE,
                                     data=None)

    with patch('arctic.store.version_store.bson.ObjectId') as mock_objId,\
            patch('arctic.store.version_store.mongo_retry') as mock_retry:
        mock_objId.return_value = MOCK_OBJID
        mock_retry.side_effect = lambda f: f
        assert expected_ret_val == VersionStore.write_metadata(vs, symbol=TEST_SYMBOL, metadata=META_TO_WRITE)
        assert vs._versions.insert_one.call_args_list == [call(expected_new_version)]
        assert vs._versions.delete_one.called is False
        assert vs.write.called is False


def test_write_empty_metadata():
    vs = _create_mock_versionstore()

    expected_new_version = TPL_VERSION.copy()
    expected_new_version.update({'_id': MOCK_OBJID,
                                 'version': TPL_VERSION['version'] + 1,
                                 'metadata': None})

    expected_ret_val = VersionedItem(symbol=TEST_SYMBOL,
                                     library=vs._arctic_lib.get_name(),
                                     host=vs._arctic_lib.arctic.mongo_host,
                                     version=TPL_VERSION['version'] + 1,
                                     metadata=None,
                                     data=None)

    with patch('arctic.store.version_store.bson.ObjectId') as mock_objId, \
            patch('arctic.store.version_store.mongo_retry') as mock_retry:
        mock_objId.return_value = MOCK_OBJID
        mock_retry.side_effect = lambda f: f
        assert expected_ret_val == VersionStore.write_metadata(vs, symbol=TEST_SYMBOL, metadata=None)
        assert vs._versions.insert_one.call_args_list == [call(expected_new_version)]
        assert vs._versions.delete_one.called is False
        assert vs.write.called is False


def test_write_metadata_insert_version_dupkeyerror():
    vs = _create_mock_versionstore()
    vs._versions.insert_one.__name__ = 'insert_one'
    vs._versions.insert_one.side_effect = [DuplicateKeyError('dup key error'), None]
    VersionStore.write_metadata(vs, symbol=TEST_SYMBOL, metadata=META_TO_WRITE)
    assert vs._version_nums.find_one_and_update.call_count == 2
    assert vs._versions.insert_one.call_count == 2


def test_write_metadata_insert_version_opfailure():
    vs = _create_mock_versionstore()
    vs._versions.insert_one.__name__ = 'insert_one'
    vs._versions.insert_one.side_effect = [OperationFailure('op failure'), None]
    VersionStore.write_metadata(vs, symbol=TEST_SYMBOL, metadata=META_TO_WRITE)
    assert vs._version_nums.find_one_and_update.call_count == 1
    assert vs._versions.insert_one.call_count == 2


def test_restore_version():
    vs = _create_mock_versionstore()

    LASTEST_VERSION = dict(TPL_VERSION, version=TPL_VERSION['version']+1, metadata={'something': 'different'})
    last_item = VersionedItem(symbol=TEST_SYMBOL, library=vs._arctic_lib.get_name(),
                              host=vs._arctic_lib.arctic.mongo_host,
                              version=LASTEST_VERSION, metadata=LASTEST_VERSION['metadata'], data="hello world")
    new_version = dict(LASTEST_VERSION, version=LASTEST_VERSION['version'] + 1)
    new_item = VersionedItem(symbol=TEST_SYMBOL, library=vs._arctic_lib.get_name(),
                             host=vs._arctic_lib.arctic.mongo_host,
                             version=new_version, metadata=new_version['metadata'], data=last_item.data)

    vs.write.return_value = new_item
    vs.read.return_value = last_item
    vs._read_metadata.side_effect = [TPL_VERSION, LASTEST_VERSION]

    with patch('arctic.store.version_store.bson.ObjectId') as mock_objId, \
            patch('arctic.store.version_store.mongo_retry') as mock_retry:
        mock_objId.return_value = MOCK_OBJID
        mock_retry.side_effect = lambda f: f
        ret_item = VersionStore.restore_version(vs, symbol=TEST_SYMBOL, as_of=LASTEST_VERSION['version'], prune_previous_version=True)
        assert ret_item == new_item
        assert vs._read_metadata.call_args_list == [call(TEST_SYMBOL, as_of=LASTEST_VERSION['version'])]
        assert vs._version_nums.find_one.call_args_list == [call({'symbol': TEST_SYMBOL})]
        assert vs.read.call_args_list == [call(TEST_SYMBOL, as_of=LASTEST_VERSION['version'])]
        assert vs.write.call_args_list == [call(TEST_SYMBOL, data=last_item.data, metadata=last_item.metadata, prune_previous_version=True)]


def test_restore_version_data_missing_symbol():
    vs = _create_mock_versionstore()
    vs._read_metadata.side_effect = NoDataFoundException("no data")
    with patch('arctic.store.version_store.mongo_retry') as mock_retry:
        mock_retry.side_effect = lambda f: f
        with pytest.raises(NoDataFoundException):
            VersionStore.restore_version(vs, symbol=TEST_SYMBOL,
                                         as_of=TPL_VERSION['version'], prune_previous_version=True)
    assert vs._read_metadata.call_args_list == [call(TEST_SYMBOL, as_of=TPL_VERSION['version'])]
    assert vs._versions.insert_one.called is False


def test_restore_last_version():
    vs = _create_mock_versionstore()
    vs._version_nums.find_one.return_value = {'version': TPL_VERSION['version']}

    vs._read_metadata.side_effect = [TPL_VERSION, TPL_VERSION]

    with patch('arctic.store.version_store.bson.ObjectId') as mock_objId, \
            patch('arctic.store.version_store.mongo_retry') as mock_retry:
        mock_objId.return_value = MOCK_OBJID
        mock_retry.side_effect = lambda f: f

        ret_item = VersionStore.restore_version(vs, symbol=TEST_SYMBOL, as_of=TPL_VERSION['version'],
                                               prune_previous_version=True)

        assert ret_item.version == TPL_VERSION['version']
        assert ret_item.metadata == TPL_VERSION.get('metadata')
        assert vs._read_metadata.call_args_list == [call(TEST_SYMBOL, as_of=TPL_VERSION['version'])]
        assert vs._version_nums.find_one.call_args_list == [call({'symbol': TEST_SYMBOL})]
        assert not vs.read.called
        assert not vs.write.called


def test_write_error_clean_retry():
    write_handler = Mock(write=Mock(__name__=""))
    write_handler.write.side_effect = [OperationFailure("mongo failure"), None]
    vs = create_autospec(VersionStore, instance=True,
                         _collection=Mock(),
                         _version_nums=Mock(find_one_and_update=Mock(return_value={'version': 1})),
                         _versions=Mock(insert_one=Mock(__name__="insert_one"), find_one=Mock(__name__="find_one")),
                         _arctic_lib=create_autospec(ArcticLibraryBinding,
                                                     arctic=create_autospec(Arctic, mongo_host='some_host')))
    vs._insert_version = lambda version: VersionStore._insert_version(vs, version)
    vs._collection.database.connection.nodes = []
    vs._write_handler.return_value = write_handler
    VersionStore.write(vs, 'sym', sentinel.data, prune_previous_version=False)
    assert vs._version_nums.find_one_and_update.call_count == 2
    assert vs._versions.find_one.call_count == 2
    assert write_handler.write.call_count == 2
    assert vs._versions.insert_one.call_count == 1


def test_write_insert_version_duplicatekey():
    write_handler = Mock(write=Mock(__name__=""))
    vs = create_autospec(VersionStore, instance=True,
                         _collection=Mock(),
                         _version_nums=Mock(find_one_and_update=Mock(return_value={'version': 1})),
                         _versions=Mock(insert_one=Mock(__name__="insert_one"), find_one=Mock(__name__="find_one")),
                         _arctic_lib=create_autospec(ArcticLibraryBinding,
                                                     arctic=create_autospec(Arctic, mongo_host='some_host')))
    vs._insert_version = lambda version: VersionStore._insert_version(vs, version)
    vs._versions.insert_one.side_effect = [DuplicateKeyError("dup key error"), None]
    vs._collection.database.connection.nodes = []
    vs._write_handler.return_value = write_handler
    VersionStore.write(vs, 'sym', sentinel.data, prune_previous_version=False)
    assert vs._version_nums.find_one_and_update.call_count == 2
    assert vs._versions.find_one.call_count == 2
    assert write_handler.write.call_count == 2
    assert vs._versions.insert_one.call_count == 2


def test_write_insert_version_operror():
    write_handler = Mock(write=Mock(__name__=""))
    vs = create_autospec(VersionStore, instance=True,
                         _collection=Mock(),
                         _version_nums=Mock(find_one_and_update=Mock(return_value={'version': 1})),
                         _versions=Mock(insert_one=Mock(__name__="insert_one"), find_one=Mock(__name__="find_one")),
                         _arctic_lib=create_autospec(ArcticLibraryBinding,
                                                     arctic=create_autospec(Arctic, mongo_host='some_host')))
    vs._insert_version = lambda version: VersionStore._insert_version(vs, version)
    vs._versions.insert_one.side_effect = [OperationFailure("mongo op error"), None]
    vs._collection.database.connection.nodes = []
    vs._write_handler.return_value = write_handler
    VersionStore.write(vs, 'sym', sentinel.data, prune_previous_version=False)
    assert vs._version_nums.find_one_and_update.call_count == 1
    assert vs._versions.find_one.call_count == 1
    assert write_handler.write.call_count == 1
    assert vs._versions.insert_one.call_count == 2


def test_append_error_clean_retry():
    read_handler = Mock(append=Mock(__name__=""))
    read_handler.append.side_effect = [OperationFailure("mongo failure"), None]
    previous_version = TPL_VERSION.copy()
    previous_version['version'] = 1
    vs = create_autospec(VersionStore, instance=True,
                         _collection=Mock(),
                         _version_nums=Mock(find_one_and_update=Mock(return_value={'version': previous_version['version']+1})),
                         _versions=Mock(insert_one=Mock(__name__="insert_one"), find_one=Mock(__name__="find_one", return_value=previous_version)),
                         _arctic_lib=create_autospec(ArcticLibraryBinding,
                                                     arctic=create_autospec(Arctic, mongo_host='some_host')))
    vs._insert_version = lambda version: VersionStore._insert_version(vs, version)
    vs._collection.database.connection.nodes = []
    vs._read_handler.return_value = read_handler
    VersionStore.append(vs, 'sym', [1, 2, 3], prune_previous_version=False, upsert=False)
    assert vs._version_nums.find_one_and_update.call_count == 2
    assert vs._versions.find_one.call_count == 2
    assert read_handler.append.call_count == 2
    assert vs._versions.insert_one.call_count == 1


def test_append_insert_version_duplicatekey():
    read_handler = Mock(append=Mock(__name__=""))
    previous_version = TPL_VERSION.copy()
    previous_version['version'] = 1
    vs = create_autospec(VersionStore, instance=True,
                         _collection=Mock(),
                         _version_nums=Mock(find_one_and_update=Mock(return_value={'version': previous_version['version']+1})),
                         _versions=Mock(insert_one=Mock(__name__="insert_one"), find_one=Mock(__name__="find_one", return_value=previous_version)),
                         _arctic_lib=create_autospec(ArcticLibraryBinding,
                                                     arctic=create_autospec(Arctic, mongo_host='some_host')))
    vs._insert_version = lambda version: VersionStore._insert_version(vs, version)
    vs._versions.insert_one.side_effect = [DuplicateKeyError("dup key error"), None]
    vs._collection.database.connection.nodes = []
    vs._read_handler.return_value = read_handler
    VersionStore.append(vs, 'sym', [1, 2, 3], prune_previous_version=False, upsert=False)
    assert vs._version_nums.find_one_and_update.call_count == 2
    assert vs._versions.find_one.call_count == 2
    assert read_handler.append.call_count == 2
    assert vs._versions.insert_one.call_count == 2

def test_append_insert_version_operror():
    read_handler = Mock(append=Mock(__name__=""))
    previous_version = TPL_VERSION.copy()
    previous_version['version'] = 1
    vs = create_autospec(VersionStore, instance=True,
                         _collection=Mock(),
                         _version_nums=Mock(find_one_and_update=Mock(return_value={'version': previous_version['version']+1})),
                         _versions=Mock(insert_one=Mock(__name__="insert_one"), find_one=Mock(__name__="find_one", return_value=previous_version)),
                         _arctic_lib=create_autospec(ArcticLibraryBinding,
                                                     arctic=create_autospec(Arctic, mongo_host='some_host')))
    vs._insert_version = lambda version: VersionStore._insert_version(vs, version)
    vs._versions.insert_one.side_effect = [OperationFailure("mongo op error"), None]
    vs._collection.database.connection.nodes = []
    vs._read_handler.return_value = read_handler
    VersionStore.append(vs, 'sym', [1, 2, 3], prune_previous_version=False, upsert=False)
    assert vs._version_nums.find_one_and_update.call_count == 1
    assert vs._versions.find_one.call_count == 1
    assert read_handler.append.call_count == 1
    assert vs._versions.insert_one.call_count == 2
