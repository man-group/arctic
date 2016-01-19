from mock import sentinel, call, Mock
from arctic.hooks import register_get_auth_hook, register_log_exception_hook, \
    register_resolve_mongodb_hook, get_mongodb_uri, log_exception
from arctic.auth import get_auth


def test_log_exception_hook():
    logger = Mock()
    register_log_exception_hook(logger)
    log_exception(sentinel.fn, sentinel.e, sentinel.r)
    assert logger.call_args_list == [call(sentinel.fn, sentinel.e, sentinel.r)]


def test_get_mongodb_uri_hook():
    resolver = Mock()
    resolver.return_value = sentinel.result
    register_resolve_mongodb_hook(resolver)
    assert get_mongodb_uri(sentinel.host) == sentinel.result
    assert resolver.call_args_list == [call(sentinel.host)]


def test_get_auth_hook():
    auth_resolver = Mock()
    register_get_auth_hook(auth_resolver)
    get_auth(sentinel.host, sentinel.app_name, sentinel.database_name)
    assert auth_resolver.call_args_list == [call(sentinel.host, sentinel.app_name, sentinel.database_name)]
