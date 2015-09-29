import bson
import datetime
from datetime import datetime as dt, timedelta as dtd
from mock import patch, MagicMock, sentinel, create_autospec, Mock, call, ANY
import pytest

import pymongo
from pymongo import ReadPreference, read_preferences

from arctic.date import mktz
from arctic.store import version_store
from arctic.store.version_store import VersionStore, VersionedItem
from arctic.arctic import ArcticLibraryBinding, Arctic
from arctic.exceptions import ConcurrentModificationException, DuplicateSnapshotException
from pymongo.errors import OperationFailure
from pymongo.collection import Collection


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
    vs = create_autospec(VersionStore, instance=True,
                         _versions=Mock())
    vs._find_snapshots.return_value = 'snap'
    date = dt(2013, 4, 1, 9, 0)
    vs._versions.find.return_value = [{'_id': bson.ObjectId.from_datetime(date),
                                       'symbol': 's', 'version': 10}]

    version = list(VersionStore.list_versions(vs, "symbol"))[0]
    local_date = date.replace(tzinfo=mktz("UTC"))
    assert version == {'symbol': version['symbol'], 'version': version['version'],
                       # We return naive datetimes in 'default' time, which is London for us
                       'date': local_date,
                       'snapshots': 'snap'}


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
    versions.find_one.assert_called_once_with({'symbol':'symbol', '_id':
                                              {'$lt': bson.ObjectId.from_datetime(dt(2013, 4, 1, 9, 0, tzinfo=mktz()) + dtd(seconds=1))}},
                                             sort=[('_id', pymongo.DESCENDING)])


def test_read_as_of_NotNaive():
    # When we do a read, with naive as_of, that as_of is treated in London Time.
    vs = create_autospec(VersionStore, instance=True,
                     _versions=Mock(), _allow_secondary=False)
    VersionStore._read_metadata(vs, 'symbol', dt(2013, 4, 1, 9, 0, tzinfo=mktz('Europe/Paris')))
    versions = vs._versions.with_options.return_value
    versions.find_one.assert_called_once_with({'symbol':'symbol', '_id':
                                              {'$lt': bson.ObjectId.from_datetime(dt(2013, 4, 1, 9, 0, tzinfo=mktz('Europe/Paris')) + dtd(seconds=1))}},
                                             sort=[('_id', pymongo.DESCENDING)])


def test_read_metadata_no_asof():
    # When we do a read, with naive as_of, that as_of is treated in London Time.
    vs = create_autospec(VersionStore, instance=True,
                     _versions=Mock(), _allow_secondary=False)
    VersionStore._read_metadata(vs, sentinel.symbol)
    versions = vs._versions.with_options.return_value
    assert versions.find_one.call_args_list == [call({'symbol': sentinel.symbol},
                                                         sort=[('version', pymongo.DESCENDING)])]


def test_write_ensure_index():
    write_handler = Mock(write=Mock(__name__=""))
    vs = create_autospec(VersionStore, instance=True,
                     _collection=Mock(),
                     _version_nums=Mock(find_one_and_update=Mock(return_value={'version':1})),
                     _versions=Mock(insert_one=lambda x:None),
                     _arctic_lib=Mock(),
                     _publish_changes=False)
    vs._collection.database.connection.nodes = []
    vs._write_handler.return_value = write_handler
    VersionStore.write(vs, 'sym', sentinel.data, prune_previous_version=False)
    vs._ensure_index.assert_called_once_with()


def test_write_check_quota():
    write_handler = Mock(write=Mock(__name__=""))
    vs = create_autospec(VersionStore, instance=True,
                     _collection=Mock(),
                     _version_nums=Mock(find_one_and_update=Mock(return_value={'version':1})),
                     _versions=Mock(insert_one=lambda x:None),
                     _arctic_lib=create_autospec(ArcticLibraryBinding),
                     _publish_changes=False)
    vs._collection.database.connection.nodes = []
    vs._write_handler.return_value = write_handler
    VersionStore.write(vs, 'sym', sentinel.data, prune_previous_version=False)
    assert vs._arctic_lib.check_quota.call_count == 1


def test_initialize_library():
    arctic_lib = create_autospec(ArcticLibraryBinding)
    arctic_lib.arctic = create_autospec(Arctic, _allow_secondary=False)
    with patch('arctic.store.version_store.enable_powerof2sizes', autospec=True) as enable_powerof2sizes, \
         patch('arctic.store.version_store.enable_sharding', autospec=True) as enable_sharding:
        arctic_lib.get_top_level_collection.return_value.database.create_collection.__name__ = 'some_name'
        arctic_lib.get_top_level_collection.return_value.database.collection_names.__name__ = 'some_name'
        VersionStore.initialize_library(arctic_lib, hashed=sentinel.hashed)
    assert enable_powerof2sizes.call_args_list == [call(arctic_lib.arctic, arctic_lib.get_name())]
    assert enable_sharding.call_args_list == [call(arctic_lib.arctic, arctic_lib.get_name(), hashed=sentinel.hashed)]


def test_ensure_index():
    th = Mock()
    vs = create_autospec(VersionStore, _collection=Mock())
    with patch('arctic.store.version_store._TYPE_HANDLERS', [th]):
        VersionStore._ensure_index(vs)
    assert vs._collection.snapshots.create_index.call_args_list == [call([('name', 1)], unique=True, background=True)]
    assert vs._collection.versions.create_index.call_args_list == [call([('symbol', 1), ('_id', -1)], background=True),
                                                               call([('symbol', 1), ('version', -1)], unique=True, background=True)]
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
        VersionStore._prune_previous_versions(self, sentinel.symbol, keep_mins=0)
    assert self._versions.with_options.call_args_list == [call(read_preference=ReadPreference.PRIMARY)]
    assert self._versions.with_options.return_value.find.call_args_list == [
                                                  call({'$or': [{'parent': {'$exists': False}},
                                                                {'parent': {'$size': 0}}],
                                                        'symbol': sentinel.symbol,
                                                        '_id': {'$lt': bson.ObjectId('524a10810000000000000000')}},
                                                       sort=[('version', -1)],
                                                       skip=1,
                                                       projection=['_id', 'type'])]


def test_read_handles_operation_failure():
    self = create_autospec(VersionStore, _versions=Mock(), _arctic_lib=Mock())
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
    assert 'bad' in str(e)
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
    assert vs._read_metadata.call_args_list == [call('foo', as_of=None, read_preference=ReadPreference.PRIMARY),
                                                call('bar', as_of=None, read_preference=ReadPreference.PRIMARY)]


def test_snapshot_duplicate_raises_exception():
    vs = create_autospec(VersionStore, _snapshots=Mock())
    with pytest.raises(DuplicateSnapshotException) as e:
        vs._snapshots.find_one.return_value = True
        VersionStore.snapshot(vs, 'symbol')
        assert "Snapshot 'symbol' already exists" in str(e.value)
