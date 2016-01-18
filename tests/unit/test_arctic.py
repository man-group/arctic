try:
    import cPickle as pickle
except ImportError:
    import pickle
from mock import patch, MagicMock, sentinel, create_autospec, Mock, call
import pytest
from pymongo.errors import OperationFailure, ServerSelectionTimeoutError, AutoReconnect
from pymongo.mongo_client import MongoClient

from arctic.auth import Credential
from arctic.arctic import Arctic, ArcticLibraryBinding, \
    register_library_type, LIBRARY_TYPES
from arctic.exceptions import LibraryNotFoundException, \
    ArcticException, QuotaExceededException
import six


def test_arctic_lazy_init():
    with patch('pymongo.MongoClient', return_value=MagicMock(), autospec=True) as mc, \
        patch('arctic.arctic.mongo_retry', side_effect=lambda x:x, autospec=True), \
        patch('arctic.arctic.get_auth', autospec=True) as ga:
            store = Arctic('cluster')
            assert not mc.called
            # do something to trigger lazy arctic init
            store.list_libraries()
            assert mc.called


def test_arctic_auth():
    with patch('pymongo.MongoClient', return_value=MagicMock(), autospec=True), \
        patch('arctic.arctic.mongo_retry', autospec=True), \
        patch('arctic.arctic.get_auth', autospec=True) as ga:
            ga.return_value = Credential('db', 'admin_user', 'admin_pass')
            store = Arctic('cluster')
            # do something to trigger lazy arctic init
            store.list_libraries()
            ga.assert_called_once_with('cluster', 'arctic', 'admin')
            store._adminDB.authenticate.assert_called_once_with('admin_user', 'admin_pass')
            ga.reset_mock()

            # Get a 'missing' library
            with pytest.raises(LibraryNotFoundException):
                with patch('arctic.arctic.ArcticLibraryBinding.get_library_type', return_value=None, autospec=True):
                    ga.return_value = Credential('db', 'user', 'pass')
                    store._conn['arctic_jblackburn'].name = 'arctic_jblackburn'
                    store['jblackburn.library']

            # Creating the library will have attempted to auth against it
            ga.assert_called_once_with('cluster', 'arctic', 'arctic_jblackburn')
            store._conn['arctic_jblackburn'].authenticate.assert_called_once_with('user', 'pass')


def test_arctic_auth_custom_app_name():
    with patch('pymongo.MongoClient', return_value=MagicMock(), autospec=True), \
        patch('arctic.arctic.mongo_retry', autospec=True), \
        patch('arctic.arctic.get_auth', autospec=True) as ga:
            ga.return_value = Credential('db', 'admin_user', 'admin_pass')
            store = Arctic('cluster', app_name=sentinel.app_name)
            # do something to trigger lazy arctic init
            store.list_libraries()
            assert ga.call_args_list == [call('cluster', sentinel.app_name, 'admin')]
            ga.reset_mock()

            # Get a 'missing' library
            with pytest.raises(LibraryNotFoundException):
                with patch('arctic.arctic.ArcticLibraryBinding.get_library_type', return_value=None, autospec=True):
                    ga.return_value = Credential('db', 'user', 'pass')
                    store._conn['arctic_jblackburn'].name = 'arctic_jblackburn'
                    store['jblackburn.library']

            # Creating the library will have attempted to auth against it
            assert ga.call_args_list == [call('cluster', sentinel.app_name, 'arctic_jblackburn')]


def test_arctic_connect_hostname():
    with patch('pymongo.MongoClient', return_value=MagicMock(), autospec=True) as mc, \
         patch('arctic.arctic.mongo_retry', autospec=True) as ar, \
         patch('arctic.arctic.get_mongodb_uri', autospec=True) as gmu:
                store = Arctic('hostname', socketTimeoutMS=sentinel.socket_timeout,
                                         connectTimeoutMS=sentinel.connect_timeout,
                                         serverSelectionTimeoutMS=sentinel.select_timeout)
                # do something to trigger lazy arctic init
                store.list_libraries()
                mc.assert_called_once_with(host=gmu('hostname'), maxPoolSize=4,
                                           socketTimeoutMS=sentinel.socket_timeout,
                                           connectTimeoutMS=sentinel.connect_timeout,
                                           serverSelectionTimeoutMS=sentinel.select_timeout)
                
                
def test_arctic_connect_with_environment_name():
    with patch('pymongo.MongoClient', return_value=MagicMock(), autospec=True) as mc, \
         patch('arctic.arctic.mongo_retry', autospec=True) as ar, \
         patch('arctic.arctic.get_auth', autospec=True), \
         patch('arctic.arctic.get_mongodb_uri') as gmfe:
            store = Arctic('live', socketTimeoutMS=sentinel.socket_timeout,
                                 connectTimeoutMS=sentinel.connect_timeout,
                                 serverSelectionTimeoutMS=sentinel.select_timeout)
            # do something to trigger lazy arctic init
            store.list_libraries()
    assert gmfe.call_args_list == [call('live')]
    assert mc.call_args_list == [call(host=gmfe.return_value, maxPoolSize=4,
                                      socketTimeoutMS=sentinel.socket_timeout,
                                      connectTimeoutMS=sentinel.connect_timeout,
                                      serverSelectionTimeoutMS=sentinel.select_timeout)]


@pytest.mark.parametrize(
    ["library", "expected_library", "expected_database"], [
        ('library', 'library', 'arctic'),
        ('user.library', 'library', 'arctic_user'),
    ])
def test_database_library_specifier(library, expected_library, expected_database):
    mongo = MagicMock()
    with patch('arctic.arctic.ArcticLibraryBinding._auth'):
        ml = ArcticLibraryBinding(mongo, library)

    assert ml.library == expected_library
    mongo._conn.__getitem__.assert_called_with(expected_database)


def test_arctic_repr():
    with patch('pymongo.MongoClient', return_value=MagicMock(), autospec=True):
        with patch('arctic.arctic.mongo_retry', autospec=True):
            with patch('arctic.arctic.get_auth', autospec=True) as ga:
                ga.return_value = Credential('db', 'admin_user', 'admin_pass')
                store = Arctic('cluster')
                assert str(store) == repr(store)


def test_lib_repr():
    mongo = MagicMock()
    with patch('arctic.arctic.ArcticLibraryBinding._auth'):
        ml = ArcticLibraryBinding(mongo, 'asdf')
        assert str(ml) == repr(ml)


def test_register_library_type():
    class DummyType(object):
        pass
    register_library_type("new_dummy_type", DummyType)
    assert LIBRARY_TYPES['new_dummy_type'] == DummyType

    with pytest.raises(ArcticException) as e:
        register_library_type("new_dummy_type", DummyType)
    assert "ArcticException: Library new_dummy_type already registered" in str(e)


def test_set_quota():
    m = Mock(spec=ArcticLibraryBinding)
    ArcticLibraryBinding.set_quota(m, 10000)
    m.set_library_metadata.assert_called_once_with('QUOTA', 10000)
    assert m.quota_countdown == 0
    assert m.quota == 10000


def test_get_quota():
    m = Mock(spec=ArcticLibraryBinding)
    m.get_library_metadata.return_value = 42
    assert ArcticLibraryBinding.get_quota(m) == 42
    m.get_library_metadata.assert_called_once_with('QUOTA')


def test_check_quota_Zero():
    self = create_autospec(ArcticLibraryBinding)
    self.quota = 0
    ArcticLibraryBinding.check_quota(self)


def test_check_quota_None():
    m = Mock(spec=ArcticLibraryBinding)
    m.quota = None
    m.get_library_metadata.return_value = None
    ArcticLibraryBinding.check_quota(m)
    m.get_library_metadata.assert_called_once_with('QUOTA')
    assert m.quota == 0


def test_check_quota_Zero2():
    m = Mock(spec=ArcticLibraryBinding)
    m.quota = None
    m.get_library_metadata.return_value = 0
    ArcticLibraryBinding.check_quota(m)
    m.get_library_metadata.assert_called_once_with('QUOTA')
    assert m.quota == 0


def test_check_quota_countdown():
    self = create_autospec(ArcticLibraryBinding)
    self.quota = 10
    self.quota_countdown = 10
    ArcticLibraryBinding.check_quota(self)
    assert self.quota_countdown == 9


def test_check_quota():
    self = create_autospec(ArcticLibraryBinding)
    self.arctic = create_autospec(Arctic)
    self.quota = 1024 * 1024 * 1024
    self.quota_countdown = 0
    self.arctic.__getitem__.return_value = Mock(stats=Mock(return_value={'totals':
                                                                             {'size': 900 * 1024 * 1024,
                                                                              'count': 100,
                                                                              }
                                                                             }))
    with patch('arctic.arctic.logger.warning') as warn:
        ArcticLibraryBinding.check_quota(self)
    self.arctic.__getitem__.assert_called_once_with(self.get_name.return_value)
    warn.assert_called_once_with('Mongo Quota: 0.879 / 1 GB used')
    assert self.quota_countdown == 6


def test_check_quota_info():
    self = create_autospec(ArcticLibraryBinding)
    self.arctic = create_autospec(Arctic)
    self.quota = 1024 * 1024 * 1024
    self.quota_countdown = 0
    self.arctic.__getitem__.return_value = Mock(stats=Mock(return_value={'totals':
                                                                             {'size': 1 * 1024 * 1024,
                                                                              'count': 100,
                                                                              }
                                                                             }))
    with patch('arctic.arctic.logger.info') as info:
        ArcticLibraryBinding.check_quota(self)
    self.arctic.__getitem__.assert_called_once_with(self.get_name.return_value)
    info.assert_called_once_with('Mongo Quota: 0.001 / 1 GB used')
    assert self.quota_countdown == 51153


def test_check_quota_exceeded():
    self = create_autospec(ArcticLibraryBinding)
    self.arctic = create_autospec(Arctic)
    self.quota = 1024 * 1024 * 1024
    self.quota_countdown = 0
    self.arctic.__getitem__.return_value = Mock(stats=Mock(return_value={'totals':
                                                                             {'size': 1024 * 1024 * 1024,
                                                                              'count': 100,
                                                                              }
                                                                             }))
    with pytest.raises(QuotaExceededException) as e:
        ArcticLibraryBinding.check_quota(self)
    assert "Quota Exceeded: 1.000 / 1 GB used" in str(e)


def test_initialize_library():
    self = create_autospec(Arctic)
    self._conn = create_autospec(MongoClient)
    lib = create_autospec(ArcticLibraryBinding)
    lib.database_name = sentinel.db_name
    lib.get_quota.return_value = None
    lib_type = Mock()
    with patch.dict('arctic.arctic.LIBRARY_TYPES', {sentinel.lib_type: lib_type}), \
         patch('arctic.arctic.ArcticLibraryBinding', return_value=lib, autospec=True) as ML:
        Arctic.initialize_library(self, sentinel.lib_name, sentinel.lib_type, thing=sentinel.thing)
    assert ML.call_args_list == [call(self, sentinel.lib_name)]
    assert ML.return_value.set_library_type.call_args_list == [call(sentinel.lib_type)]
    assert ML.return_value.set_quota.call_args_list == [call(10 * 1024 * 1024 * 1024)]
    assert lib_type.initialize_library.call_args_list == [call(ML.return_value, thing=sentinel.thing)]


def test_initialize_library_too_many_ns():
    self = create_autospec(Arctic)
    self._conn = create_autospec(MongoClient)
    lib = create_autospec(ArcticLibraryBinding)
    lib.database_name = sentinel.db_name
    self._conn.__getitem__.return_value.collection_names.return_value = [x for x in six.moves.xrange(3001)]
    lib_type = Mock()
    with pytest.raises(ArcticException) as e:
        with patch.dict('arctic.arctic.LIBRARY_TYPES', {sentinel.lib_type: lib_type}), \
             patch('arctic.arctic.ArcticLibraryBinding', return_value=lib, autospec=True) as ML:
            Arctic.initialize_library(self, sentinel.lib_name, sentinel.lib_type, thing=sentinel.thing)
    assert self._conn.__getitem__.call_args_list == [call(sentinel.db_name),
                                                     call(sentinel.db_name)]
    assert lib_type.initialize_library.call_count == 0
    assert 'Too many namespaces 3001, not creating: sentinel.lib_name' in str(e)


def test_get_library():
    self = create_autospec(Arctic)
    self._library_cache = {}
    library_type = Mock()
    register_library_type(sentinel.lib_type, library_type)
    with patch('arctic.arctic.ArcticLibraryBinding', autospec=True) as ML:
        ML.return_value.get_library_type.return_value = sentinel.lib_type
        library = Arctic.get_library(self, sentinel.lib_name)
    del LIBRARY_TYPES[sentinel.lib_type]
    assert ML.call_args_list == [call(self, sentinel.lib_name)]
    assert library_type.call_args_list == [call(ML.return_value)]
    assert library == library_type.return_value


def test_get_library_not_initialized():
    self = create_autospec(Arctic,
                           mongo_host=sentinel.host)
    self._library_cache = {}
    with pytest.raises(LibraryNotFoundException) as e, \
         patch('arctic.arctic.ArcticLibraryBinding', autospec=True) as ML:
        ML.return_value.get_library_type.return_value = None
        Arctic.get_library(self, sentinel.lib_name)
    assert "Library %s was not correctly initialized in %s." % (sentinel.lib_name, self) in str(e)


def test_get_library_auth_issue():
    self = create_autospec(Arctic,
                           mongo_host=sentinel.host)
    self._library_cache = {}
    with pytest.raises(LibraryNotFoundException) as e, \
         patch('arctic.arctic.ArcticLibraryBinding', autospec=True) as ML:
        ML.return_value.get_library_type.side_effect = OperationFailure('database error: not authorized for query on arctic_marketdata.index.ARCTIC')
        Arctic.get_library(self, sentinel.lib_name)
    assert "Library %s was not correctly initialized in %s." % (sentinel.lib_name, self) in str(e)


def test_get_library_not_registered():
    self = create_autospec(Arctic)
    self._library_cache = {}
    with pytest.raises(LibraryNotFoundException) as e, \
         patch('arctic.arctic.ArcticLibraryBinding', autospec=True) as ML:
        ML.return_value.get_library_type.return_value = sentinel.lib_type
        Arctic.get_library(self, sentinel.lib_name)
    assert ("Couldn't load LibraryType '%s' for '%s' (has the class been registered?)" %
            (sentinel.lib_type, sentinel.lib_name)
            )in str(e)


def test_mongo_host_get_set():
    sentinel.mongo_host = Mock(nodes={("host", "port")})
    arctic = Arctic(sentinel.mongo_host)
    assert arctic.mongo_host == "host:port"


def test_arctic_set_get_state():
    sentinel.mongo_host = Mock(nodes={("host", "port")})
    store = Arctic(sentinel.mongo_host, allow_secondary="allow_secondary", app_name="app_name", 
                   socketTimeoutMS=1234, connectTimeoutMS=2345, serverSelectionTimeoutMS=3456)
    buff = pickle.dumps(store)
    mnew = pickle.loads(buff)
    assert mnew.mongo_host == "host:port"
    assert mnew._allow_secondary == "allow_secondary"
    assert mnew._application_name == "app_name"
    assert mnew._socket_timeout == 1234
    assert mnew._connect_timeout == 2345
    assert mnew._server_selection_timeout == 3456


def test__conn_auth_issue():
    auth_timeout = [0]
    
    a = Arctic("host:12345")
    sentinel.creds = Mock()

    def flaky_auth(*args, **kwargs):
        if not auth_timeout[0]:
            auth_timeout[0] = 1
            raise AutoReconnect()

    with patch('arctic.arctic.authenticate', flaky_auth), \
    patch('arctic.arctic.get_auth', return_value=sentinel.creds), \
    patch('arctic.decorators._handle_error') as he:
        a._conn
        assert he.call_count == 1
        assert auth_timeout[0]
