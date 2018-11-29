import logging
import time
from collections import defaultdict
from threading import RLock

from concurrent.futures import FIRST_COMPLETED

from .async_utils import AsyncRequestType, AsyncRequest
from ._workers_pool import LazySingletonWorkersPool
from ..decorators import mongo_retry
from ..exceptions import AsyncArcticException


def _arctic_task_exec(request):
    request.start_time = time.time()
    logging.debug("Executing asynchronous request for {}/{}".format(request.library, request.symbol))
    result = None
    try:
        request.is_running = True
        if request.mongo_retry:
            result = mongo_retry(request.fun)(*request.args, **request.kwargs)
        else:
            result = request.fun(*request.args, **request.kwargs)
    except Exception as e:
        request.exception = e
    finally:
        request.data = result
        request.end_time = time.time()
        request.is_running = False
    return result


class AsyncArctic(LazySingletonWorkersPool):
    _instance = None
    _SINGLETON_LOCK = RLock()
    _POOL_LOCK = RLock()

    def __init__(self, pool_size):
        # Only allow creation via get_instance
        if not type(self)._SINGLETON_LOCK._is_owned():
            raise AsyncArcticException("AsyncArctic is a singleton, can't create a new instance")

        # Enforce the singleton pattern
        with type(self)._SINGLETON_LOCK:
            super(AsyncArctic, self).__init__(pool_size)
            self.requests_per_library = defaultdict(lambda: defaultdict(lambda: defaultdict(list)))
            self.requests_by_id = dict()

    def __reduce__(self):
        return "ASYNC_ARCTIC"

    def _get_modifiers(self, library_name, symbol=None):
        return self.requests_per_library[library_name][symbol][AsyncRequestType.MODIFIER]

    def _get_accessors(self, library_name, symbol=None):
        return self.requests_per_library[library_name][symbol][AsyncRequestType.ACCESSOR]

    @staticmethod
    def _verify_request(store, is_modifier, **kwargs):
        library_name = None if store is None else store._arctic_lib.get_name()
        symbol = kwargs.get('symbol')
        kind = AsyncRequestType.MODIFIER if is_modifier else AsyncRequestType.ACCESSOR
        callback = kwargs.get('async_callback')
        mongo_retry = bool(kwargs.get('mongo_retry'))
        return library_name, symbol, kind, callback, mongo_retry

    def _add_request(self, request):
        self.requests_per_library[request.library][request.symbol][request.kind].append(request)
        self.requests_by_id[request.id] = request

    def _remove_request(self, request):
        self.requests_per_library[request.library][request.symbol][request.kind].remove(request)
        if request.id in self.requests_by_id:
            del self.requests_by_id[request.id]

    def submit_arctic_request(self, store, fun, is_modifier, *args, **kwargs):
        lib_name, symbol, kind, callback, mongo_retry = AsyncArctic._verify_request(store, is_modifier, **kwargs)

        for k in ('async_callback', 'mongo_retry'):
            kwargs.pop(k, None)

        with type(self)._POOL_LOCK:  # class level lock, since it is a Singleton
            if lib_name:
                if self._get_modifiers(lib_name, symbol):
                    raise AsyncArcticException("Can't submit async task as one or more {} tasks "
                                               "are already being processed".format(AsyncRequestType.MODIFIER))

                if is_modifier and self._get_accessors(lib_name, symbol):
                    raise AsyncArcticException("Can't submit async {} task as one or more {} tasks "
                                               "are being processed".format(AsyncRequestType.ACCESSOR,
                                                                            AsyncRequestType.MODIFIER))

            # Create the request object
            request = AsyncRequest(kind, lib_name, fun, *args, **kwargs)

            # Update the state of tracked tasks
            self._add_request(request)

            # Submit the task
            try:
                new_id, new_future = self.submit_task(False, _arctic_task_exec, request)
                request.id = new_id
                request.future = new_future
            except Exception:
                # clean up the state
                self._remove_request(request)
                raise

        # No need to hold the lock for the below statements
        # If request is already finished by now, the callback is invoked immediately
        request.future.add_done_callback(lambda the_future: self._request_finished(request, callback))

        return request

    def _request_finished(self, request, callback=None):
        with type(self)._POOL_LOCK:
            self._remove_request(request)
        request.is_completed = True
        if callback:
            callback(request)

    @staticmethod
    def wait_request(request, timeout=None):
        while request is not None and not request.is_completed:
            AsyncArctic.wait_tasks_or_abort((request.future, ), timeout=timeout)

    @staticmethod
    def wait_requests(requests, timeout=None):
        while requests and not all(r.is_completed for r in requests):
            AsyncArctic.wait_tasks_or_abort(tuple(r.future for r in requests if not r.is_completed), timeout=timeout)

    @staticmethod
    def wait_any_request(requests, timeout=None):
        while requests and not any(r.is_completed for r in requests):
            AsyncArctic.wait_tasks(tuple(r.future for r in requests if not r.is_completed),
                                   timeout=timeout, return_when=FIRST_COMPLETED, raise_exceptions=True)

    @staticmethod
    def filter_finished_requests(requests, do_raise=True):
        if not requests:
            return requests, requests
        alive_requests = [r for r in requests if not r.is_completed]
        done_requests = [r for r in requests if r.is_completed]
        if do_raise:
            AsyncArctic.raise_errored(done_requests)
        return alive_requests, done_requests

    @staticmethod
    def raise_errored(requests):
        errored = tuple(r for r in requests if r.is_completed and r.exception is not None)
        if errored:
            raise errored[0].exception

    def join(self, timeout=None):
        while len(self.requests_by_id):
            try:
                AsyncArctic.wait_requests(self.requests_by_id.values(), timeout=timeout)
            except Exception as e:
                logging.exception("Failed to join all requests")

    def total_requests(self):
        return len(self.requests_by_id)


ASYNC_ARCTIC = AsyncArctic.get_instance()
async_arctic_submit = ASYNC_ARCTIC.submit_arctic_request
async_wait_request = ASYNC_ARCTIC.wait_request
async_wait_requests = ASYNC_ARCTIC.wait_requests
async_join_all = ASYNC_ARCTIC.join
async_reset_pool = ASYNC_ARCTIC.reset
async_total_requests = ASYNC_ARCTIC.total_requests


# def async_modifier(func):
#     @wraps(func)
#     def wrapper(self, *args, **kwargs):
#         return async_arctic_submit(self, func, True, *args, **kwargs)
#
#     return wrapper
#
#
# def async_accessor(func):
#     @wraps(func)
#     def wrapper(self, *args, **kwargs):
#         return async_arctic_submit(self, func, False, *args, **kwargs)
#
#     return wrapper
