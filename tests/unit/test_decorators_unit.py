from mock import patch, create_autospec, sentinel, Mock, PropertyMock, MagicMock, call
import pytest
from pymongo.errors import AutoReconnect, OperationFailure, DuplicateKeyError, ServerSelectionTimeoutError
from pymongo.read_preferences import ReadPreference

from arctic import decorators
from arctic.decorators import mongo_retry, _get_host
from pymongo.collection import Collection
from arctic.hooks import register_log_exception_hook


def test_mongo_retry():
    retries = [2]
    self = MagicMock()
    self._arctic_lib.arctic.mongo_host = sentinel.host
    self._collection.database.client.nodes = set([('a', 12)])
    self._arctic_lib.get_name.return_value = sentinel.lib_name
    op_fail_ex = OperationFailure('error')
    auto_reconn_ex = AutoReconnect('error')
    with patch('arctic.decorators._log_exception') as le, \
            patch('arctic.decorators.sleep') as mock_sleep:
        @mongo_retry
        def foo(self):
            if retries[0] == 2:
                retries[0] -= 1
                raise op_fail_ex
            elif retries[0] == 1:
                retries[0] -= 1
                raise auto_reconn_ex
            return "success"
        foo(self)
    assert le.call_args_list[0] == call('foo', op_fail_ex, 1, mnodes=['a:12'], l=sentinel.lib_name, mhost='sentinel.host')
    assert le.call_args_list[1] == call('foo', auto_reconn_ex, 2, mnodes=['a:12'], l=sentinel.lib_name, mhost='sentinel.host')
    assert self._arctic_lib.reset_auth.call_args_list == [call()]
    assert mock_sleep.call_count == 2


def test_mongo_retry_hook_changes():
    retries = [2]
    self = MagicMock()
    hook1 = Mock()
    register_log_exception_hook(hook1)
    hook2 = Mock()

    @mongo_retry
    def foo(self):
        if retries[0] == 2:
            retries[0] -= 1
            raise OperationFailure('error')
        elif retries[0] == 1:
            register_log_exception_hook(hook2)
            retries[0] -= 1
            raise AutoReconnect('error')
        return "success"
    foo(self)

    assert hook1.call_count == 1
    assert hook2.call_count == 1


def test_mongo_retry_fails():
    error = OperationFailure('error')
    retries = [16]
    with patch('arctic.decorators._log_exception', autospec=True) as le:
        @mongo_retry
        def foo():
            if retries[0]:
                retries[0] -= 1
                raise error
            return "success"
        with pytest.raises(OperationFailure):
            foo()
    assert le.call_count == 15
    assert le.call_args[0][0] == 'foo'
    assert le.call_args[0][1] == error


def test_retry_nested():
    error = OperationFailure('error')
    with patch('arctic.decorators._log_exception', autospec=True) as le:
        @mongo_retry
        def foo():
            @mongo_retry
            def bar():
                raise error
            try:
                bar()
            except:
                raise error
        with pytest.raises(OperationFailure):
            foo()
    assert le.call_count == 15
    assert le.call_args[0][0] == 'bar'
    assert le.call_args[0][1] == error


def test_all_other_exceptions_logged():
    with patch('arctic.decorators._log_exception', autospec=True) as le:
        def foo():
            raise Exception("Unexpected Error")
        foo.__module__ = 'arctic.foo'
        foo = mongo_retry(foo)
        with pytest.raises(Exception) as e:
            foo()
    assert "Unexpected Error" in str(e)
    assert le.call_count == 1
    assert le.call_args[0][0] == "foo"


def test_other_exceptions_not_logged_outside_of_arctic():
    with patch('arctic.decorators._log_exception', autospec=True) as le:
        @mongo_retry
        def foo():
            raise Exception("Unexpected Error")
        with pytest.raises(Exception) as e:
            foo()
    assert "Unexpected Error" in str(e)
    assert le.call_count == 0


@pytest.mark.xfail(reason="CS-8393 Mongo server reports auth failure when servers flip")
def test_auth_failure_no_retry():
    error = OperationFailure('unauthorized for db:arctic_jblackburn')
    with patch('arctic.decorators._log_exception', autospec=True) as le:
        @mongo_retry
        def foo():
            raise error
        with pytest.raises(OperationFailure) as e:
            foo()
    assert 'OperationFailure: unauthorized for db:arctic_jblackburn' in str(e)
    assert le.call_count == 1


def test_duplicate_key_failure_no_retry():
    error = DuplicateKeyError('duplicate key')
    with patch('arctic.decorators._log_exception', autospec=True) as le:
        @mongo_retry
        def foo():
            raise error
        with pytest.raises(OperationFailure) as e:
            foo()
    assert 'duplicate key' in str(e)
    assert le.call_count == 1


def test_ServerSelectionTimeoutError_no_retry():
    error = ServerSelectionTimeoutError('some error')
    with patch('arctic.decorators._log_exception', autospec=True) as le:
        @mongo_retry
        def foo():
            raise error
        with pytest.raises(ServerSelectionTimeoutError) as e:
            foo()
    assert 'some error' in str(e)
    assert le.call_count == 1


def test_get_host():
    store = Mock()
    store._arctic_lib.arctic.mongo_host = sentinel.host
    store._collection.database.client.nodes = set([('a', 12)])
    store._arctic_lib.get_name.return_value = sentinel.lib_name
    assert _get_host(store) == {'mhost': 'sentinel.host',
                                'mnodes': ['a:12'],
                                'l': sentinel.lib_name,
                               }


def test_get_host_list():
    store = Mock()
    store._arctic_lib.arctic.mongo_host = sentinel.host
    store._collection.database.client.nodes = set([('a', 12)])
    store._arctic_lib.get_name.return_value = sentinel.lib_name
    assert _get_host([store]) == {'mhost': 'sentinel.host',
                                 'mnodes': ['a:12'],
                                 'l': sentinel.lib_name,
                                 }


def test_get_host_not_a_vs():
    store = MagicMock()
    store._arctic_lib.get_name.side_effect = AttributeError("Hello")
    assert _get_host(store) == {}
    store._arctic_lib.get_name.side_effect = ValueError("Hello")
    assert _get_host(store) == {}
