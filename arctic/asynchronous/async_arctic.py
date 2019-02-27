import logging
import time
from collections import defaultdict
from threading import RLock

from concurrent.futures import FIRST_COMPLETED

from ._workers_pool import LazySingletonTasksCoordinator
from .async_utils import AsyncRequestType, AsyncRequest
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


class AsyncArctic(LazySingletonTasksCoordinator):
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
            self.local_shutdown = False
            self.deferred_requests = list()

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

    def _is_clashing(self, request):
        return bool(self._get_modifiers(request.library, request.symbol) or
                    request.kind is AsyncRequestType.MODIFIER and self._get_accessors(request.library, request.symbol))

    def _add_request(self, request):
        self.requests_per_library[request.library][request.symbol][request.kind].append(request)
        self.requests_by_id[request.id] = request

    def _remove_request(self, request):
        self.requests_per_library[request.library][request.symbol][request.kind].remove(request)
        if request.id in self.requests_by_id:
            del self.requests_by_id[request.id]

    def _schedule_request(self, request):
        try:
            new_id, new_future = self.submit_task(False, _arctic_task_exec, request)
            request.id = new_id
            # Update the state of tracked tasks
            self._add_request(request)
            request.future = new_future
            request.future.add_done_callback(lambda the_future: self._request_finished(request))
        except Exception:
            # clean up the state
            self._remove_request(request)
            raise

    def submit_arctic_request(self, store, fun, is_modifier, *args, **kwargs):
        lib_name, symbol, kind, callback, mongo_retry = AsyncArctic._verify_request(store, is_modifier, **kwargs)

        for k in ('async_callback', 'mongo_retry'):
            kwargs.pop(k, None)

        with type(self)._POOL_LOCK:  # class level lock, since it is a Singleton
            if self.local_shutdown:
                raise AsyncArcticException("AsyncArctic has been shutdown and can no longer accept new requests.")

            # Create the request object
            request = AsyncRequest(kind, lib_name, fun, callback, *args, **kwargs)

            if lib_name and self._is_clashing(request):
                self.deferred_requests.append(request)
                return request

            self._schedule_request(request)

        return request

    def _reschedule_deferred(self):
        picked = None
        try:
            for deferred in self.deferred_requests:
                if not self._is_clashing(deferred):
                    picked = deferred
                    self._schedule_request(deferred)
                    break
        except:
            logging.exception("Failed to re-schedule a deferred task: {}".format(picked))
            return
        self.deferred_requests.remove(picked)

    def _request_finished(self, request):
        with type(self)._POOL_LOCK:
            self._remove_request(request)
            if self.deferred_requests:
                self._reschedule_deferred()
            elif self.local_shutdown:
                # Deferred shutdown of the underlying pool until the deferred jobs have finished
                super(AsyncArctic, self).shutdown()
        request.is_completed = True
        if callable(request.callback):
            request.callback(request)

    def reset(self, pool_size=None, timeout=None):
        self.shutdown(timeout=timeout)
        self.await_termination(timeout=timeout)
        super(AsyncArctic, self).reset(pool_size, timeout)
        with type(self)._SINGLETON_LOCK:
            self.requests_per_library = defaultdict(lambda: defaultdict(lambda: defaultdict(list)))
            self.requests_by_id = dict()
            self.local_shutdown = False
            self.deferred_requests = list()

    def shutdown(self, timeout=None):
        if self.local_shutdown:
            return
        with type(self)._POOL_LOCK:
            self.local_shutdown = True
            if self.total_pending_requests() == 0:
                # safe to use this non-atomic check here, as self.deferred_requests
                # is updated only after the deferred request is scheduled
                super(AsyncArctic, self).shutdown(timeout=timeout)

    def await_termination(self, timeout=None):
        while self.total_pending_requests() > 0:
            AsyncArctic.wait_requests(self.requests_by_id.values() + self.deferred_requests,
                                      do_raise=False, timeout=timeout)
        # super(AsyncArctic, self).await_termination(timeout)

    def total_pending_requests(self):
        with type(self)._POOL_LOCK:  # the lock here is "really" necessary
            return len(self.requests_by_id) + len(self.deferred_requests)

    @staticmethod
    def _wait_until_scheduled(requests, timeout=None, check_interval=0.1):
        start = time.time()
        while True:
            if any(r for r in requests if r.future is None):
                time.sleep(check_interval)
            else:
                return True
            if timeout is not None and time.time() - start >= timeout:
                break
        return False

    @staticmethod
    def wait_request(request, do_raise=False, timeout=None):
        if request is None:
            return
        if not AsyncArctic._wait_until_scheduled((request,), timeout):
            raise AsyncArcticException("Timed-out while waiting for request to be scheduled")
        while request.is_completed:
            AsyncArctic.wait_tasks((request.future,), timeout=timeout, raise_exceptions=do_raise)

    @staticmethod
    def wait_requests(requests, do_raise=False, timeout=None):
        if not AsyncArctic._wait_until_scheduled(requests, timeout):
            raise AsyncArcticException("Timed-out while waiting for request to be scheduled")
        while requests and not all(r.is_completed for r in requests):
            AsyncArctic.wait_tasks(tuple(r.future for r in requests if not r.is_completed and r.future is not None),
                                   timeout=timeout, raise_exceptions=do_raise)

    @staticmethod
    def wait_any_request(requests, do_raise=False, timeout=None):
        if not AsyncArctic._wait_until_scheduled(requests, timeout):
            raise AsyncArcticException("Timed-out while waiting for request to be scheduled")
        while requests and not any(r.is_completed for r in requests):
            AsyncArctic.wait_tasks(tuple(r.future for r in requests if not r.is_completed and r.future is not None),
                                   timeout=timeout, return_when=FIRST_COMPLETED, raise_exceptions=do_raise)

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
    def raise_first_errored(requests):
        errored = tuple(r for r in requests if r.is_completed and r.exception is not None)
        if errored:
            raise errored[0].exception

    @staticmethod
    def filter_errored(requests):
        return tuple(r for r in requests if r.is_completed and r.exception is not None)


ASYNC_ARCTIC = AsyncArctic.get_instance()
async_arctic_submit = ASYNC_ARCTIC.submit_arctic_request
async_wait_request = ASYNC_ARCTIC.wait_request
async_wait_requests = ASYNC_ARCTIC.wait_requests
async_shutdown = ASYNC_ARCTIC.shutdown
async_await_termination = ASYNC_ARCTIC.await_termination
async_reset_pool = ASYNC_ARCTIC.reset
async_total_requests = ASYNC_ARCTIC.total_pending_requests


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
