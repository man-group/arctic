import logging
import sys
from functools import wraps
from time import sleep
from pymongo.errors import AutoReconnect, OperationFailure, DuplicateKeyError, ServerSelectionTimeoutError

from .hooks import log_exception as _log_exception

logger = logging.getLogger(__name__)

_MAX_RETRIES = 15


def _get_store(args):
    store = args[0] if args and isinstance(args, (list, tuple)) else args
    return store


def _get_host(store):
    ret = {}
    if store:
        try:
            if isinstance(store, (list, tuple)):
                store = store[0]
            ret['l'] = store._arctic_lib.get_name()
            ret['mnodes'] = ["{}:{}".format(h, p) for h, p in store._collection.database.client.nodes]
            ret['mhost'] = "{}".format(store._arctic_lib.arctic.mongo_host)
        except Exception:
            # Sometimes get_name(), for example, fails if we're not connected to MongoDB.
            pass
    return ret

_in_retry = False
_retry_count = 0


def _retry_authenticate(store):
    if store:
        try:
            store._arctic_lib.reset_auth()
        except Exception:
            # do this transparently, don't add noise to the logs
            pass


def mongo_retry(f):
    """
    Catch-all decorator that handles AutoReconnect and OperationFailure
    errors from PyMongo
    """
    log_all_exceptions = 'arctic' in f.__module__ if f.__module__ else False

    @wraps(f)
    def f_retry(*args, **kwargs):
        global _retry_count, _in_retry
        top_level = not _in_retry
        _in_retry = True
        store = _get_store(args)
        try:
            while True:
                try:
                    return f(*args, **kwargs)
                except (DuplicateKeyError, ServerSelectionTimeoutError) as e:
                    # Re-raise errors that won't go away.
                    _handle_error(f, e, _retry_count, store)
                    raise
                except (OperationFailure, AutoReconnect) as e:
                    _retry_count += 1
                    _handle_error(f, e, _retry_count, store)
                except Exception as e:
                    if log_all_exceptions:
                        _log_exception(f.__name__, e, _retry_count, **_get_host(store))
                    raise
        finally:
            if top_level:
                _in_retry = False
                _retry_count = 0
    return f_retry


def _handle_error(f, e, retry_count, store):
    if retry_count > _MAX_RETRIES:
        logger.error('Too many retries %s [%s], raising' % (f.__name__, e))
        e.traceback = sys.exc_info()[2]
        raise
    log_fn = logger.warning if retry_count > 2 else logger.debug
    log_fn('%s %s [%s], retrying %i' % (type(e), f.__name__, e, retry_count))
    # Log operation failure errors
    _log_exception(f.__name__, e, retry_count, **_get_host(store))
    sleep(0.01 * min((3 ** retry_count), 50))
    if isinstance(e, OperationFailure):  # retry auth after random back-off time
        # we could have a more specific test here:
        #   if isinstance(e, OperationFailure) and e.code == 13:
        # See https://github.com/mongodb/mongo/blob/master/src/mongo/base/error_codes.err#L74
        # Nonetheless, it is no harm to re-authenticate in the background whenever OperationFailure is raised
        _retry_authenticate(store)
