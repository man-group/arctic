from mock import sentinel, call, Mock
from arctic.hooks import register_log_exception_hook, register_resolve_mongodb_hook, get_mongodb_uri, log_exception


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
