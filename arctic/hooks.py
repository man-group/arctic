

_resolve_mongodb_hook = lambda env: env
_log_exception_hook = lambda *args, **kwargs: None
_get_auth_hook = lambda *args, **kwargs: None


def get_mongodb_uri(host):
    """
    Return the MongoDB URI for the passed in host-alias / environment.

    Allows an indirection point for mapping aliases to particular
    MongoDB instances.
    """
    return _resolve_mongodb_hook(host)


def register_resolve_mongodb_hook(hook):
    global _resolve_mongodb_hook
    _resolve_mongodb_hook = hook


def log_exception(fn_name, exception, retry_count, **kwargs):
    """
    External exception logging hook.
    """
    _log_exception_hook(fn_name, exception, retry_count, **kwargs)


def register_log_exception_hook(hook):
    global _log_exception_hook
    _log_exception_hook = hook


def register_get_auth_hook(hook):
    global _get_auth_hook
    _get_auth_hook = hook
