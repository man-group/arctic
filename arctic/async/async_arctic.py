import logging
import time
from collections import defaultdict
from functools import wraps
from threading import RLock, Event

from concurrent.futures import ThreadPoolExecutor, wait, FIRST_EXCEPTION, ALL_COMPLETED

from arctic.decorators import mongo_retry
from .async_utils import AsyncRequestType, AsyncRequest, ARCTIC_ASYNC_NTHREADS
from arctic.exceptions import AsyncArcticException


def _task_exec(request):
    request.start_time = time.time()
    logging.debug("Executing asynchronous request for library: {}".format(request.library, request.symbol))
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


# def _mongo_exec(request):
#     request.start_time = time.time()
#     if request.with_retry:
#         result = mongo_retry(request.fun)(*request.args, **request.kwargs)
#     else:
#         result = request.fun(*request.args, **request.kwargs)
#     if isinstance(result, pymongo.cursor.Cursor):
#         request.data = list(result)
#         result = request.data
#     request.end_time = time.time()
#     return result


class AsyncArctic(object):
    _instance = None
    _SINGLETON_LOCK = RLock()
    _POOL_INIT_LOCK = RLock()
    _TASK_SUBMIT_LOCK = RLock()

    @staticmethod
    def is_initialized():
        with AsyncArctic._POOL_INIT_LOCK:
            is_init = AsyncArctic._instance is not None and AsyncArctic._instance._pool is not None
        return is_init

    @staticmethod
    def get_instance():
        # Lazy init
        with AsyncArctic._SINGLETON_LOCK:
            if AsyncArctic._instance is None:
                AsyncArctic._instance = AsyncArctic()
        return AsyncArctic._instance

    @property
    def _workers_pool(self):
        if self._pool is not None:
            return self._pool

        # lazy init the workers pool
        initialized = False
        with AsyncArctic._POOL_INIT_LOCK:
            if self._pool is None:
                self._pool = ThreadPoolExecutor(max_workers=self._pool_size,
                                                thread_name_prefix='AsyncArcticWorker')
                initialized = True

        # Call hooks outside the lock, to minimize time-under-lock
        if initialized:
            for hook in self._pool_update_hooks:
                hook(self._pool_size)

        return self._pool

    def __init__(self):
        # Only allow creation via get_instance
        if not AsyncArctic._SINGLETON_LOCK._is_owned():
            raise AsyncArcticException("AsyncArctic is a singleton, can't create a new instance")

        # Enforce the singleton pattern
        with AsyncArctic._SINGLETON_LOCK:
            if AsyncArctic._instance is not None:
                raise AsyncArcticException("AsyncArctic is a singleton, can't create a new instance")
            self._lock = RLock()
            self.request_done_events = []
            self._pool = None
            self._pool_size = ARCTIC_ASYNC_NTHREADS
            self.requests_per_library = defaultdict(lambda: defaultdict(lambda: defaultdict(list)))
            self.requests_by_id = dict()
            self._pool_update_hooks = []

    def __reduce__(self):
        return "ASYNC_ARCTIC"

    def reset(self, block=True, pool_size=ARCTIC_ASYNC_NTHREADS):
        with AsyncArctic._POOL_INIT_LOCK:
            self._workers_pool.shutdown(wait=block)
            pool_size = max(pool_size, 1)
            self._pool = None
            self._pool_size = pool_size
            # pool will be lazily initialized with pool_size on next request submission

    def _get_modifiers(self, library_name, symbol=None):
        return self.requests_per_library[library_name][symbol][AsyncRequestType.MODIFIER]

    def _get_accessors(self, library_name, symbol=None):
        return self.requests_per_library[library_name][symbol][AsyncRequestType.ACCESSOR]

    @staticmethod
    def _verify_request(store, is_modifier, **kwargs):
        if store is None:
            raise AsyncArcticException("Can't submit async arctic task passing an empty store")

        library_name = store._arctic_lib.get_name()
        symbol = kwargs.get('symbol')
        kind = AsyncRequestType.MODIFIER if is_modifier else AsyncRequestType.ACCESSOR

        callback = kwargs.get('async_callback')
        block = bool(kwargs.get('async_block'))
        mongo_retry = bool(kwargs.get('mongo_retry'))

        if block and callback:
            raise AsyncArcticException("Can't use both async_callback and async_block")

        return library_name, symbol, kind, callback, block, mongo_retry

    def _add_request(self, request):
        self.requests_per_library[request.library][request.symbol][request.kind].append(request)
        self.requests_by_id[request.id] = request

    def _remove_request(self, request):
        self.requests_per_library[request.library][request.symbol][request.kind].remove(request)
        if request.id in self.requests_by_id:
            del self.requests_by_id[request.id]
    
    def submit_request(self, store, fun, is_modifier, *args, **kwargs):
        library_name, symbol, kind, callback, block, mongo_retry = AsyncArctic._verify_request(store, is_modifier, **kwargs)

        if 'async_callback' in kwargs:
            kwargs.pop('async_callback')

        if 'async_block' in kwargs:
            kwargs.pop('async_block')

        if 'mongo_retry' in kwargs:
            kwargs.pop('mongo_retry')

        with AsyncArctic._TASK_SUBMIT_LOCK:
            if self._get_modifiers(library_name, symbol):
                raise AsyncArcticException("Can't submit async task as there are "
                                           "being processed one or more {} tasks".format(AsyncRequestType.MODIFIER))

            if is_modifier and self._get_accessors(library_name, symbol):
                raise AsyncArcticException("Can't submit async {} task as there are being processed one or "
                                           "more {} tasks".format(AsyncRequestType.ACCESSOR, AsyncRequestType.MODIFIER))

            # Create the request object
            request = AsyncRequest(kind, library_name, fun, *args, **kwargs)

            # Update the state of tracked tasks
            self._add_request(request)

            # Submit the task
            try:
                request.future = self._workers_pool.submit(_task_exec, request)
            except:
                # clean up the state
                self._remove_request(request)
                raise

        # No need to hold the lock for the below statements
        if block:
            AsyncArctic.wait_request(request)
        request.future.add_done_callback(lambda the_future: self._request_finished(request, callback))

        return request

    def _request_finished(self, request, callback=None):
        with AsyncArctic._TASK_SUBMIT_LOCK:
            self._remove_request(request)
        # request.future = None
        request.is_completed = True
        if callback:
            callback(request)

    @staticmethod
    def wait_request(request, timeout=None):
        while request is not None and not request.is_completed:
            wait((request.future,),
                 timeout=timeout,
                 return_when=FIRST_EXCEPTION)

    @staticmethod
    def wait_requests(requests, timeout=None):
        if not requests:
            return
        while not all(r.is_completed for r in requests):
            wait((r.future for r in requests),
                 timeout=timeout,
                 return_when=ALL_COMPLETED)

    @staticmethod
    def wait_any_request(requests, timeout=None):
        if not requests:
            return
        while not any(r.is_completed for r in requests):
            wait((r.future for r in requests),
                 timeout=timeout,
                 return_when=FIRST_EXCEPTION)

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
        with AsyncArctic._TASK_SUBMIT_LOCK:
            try:
                AsyncArctic.wait_requests(self.requests_by_id.values(), timeout=timeout)
            except Exception as e:
                logging.exception("Failed to join all requests")

    def total_requests(self):
        return len(self.requests_by_id)

    def total_mongo_requests(self):
        return len([1 for r in self.requests_by_id if isinstance(r, MongoAsyncRequest)])


class InternalAsyncArctic(AsyncArctic):
    pass


ASYNC_ARCTIC = AsyncArctic.get_instance()
async_arctic_submit = ASYNC_ARCTIC.submit_request
async_wait_request = ASYNC_ARCTIC.wait_request
async_wait_requests = ASYNC_ARCTIC.wait_requests
async_join_all = ASYNC_ARCTIC.join
async_reset_pool = ASYNC_ARCTIC.reset
async_total_requests = ASYNC_ARCTIC.total_requests
async_total_mongo_requests = ASYNC_ARCTIC.total_mongo_requests


INTERNAL_ASYNC = InternalAsyncArctic.get_instance()
INTERNAL_ASYNC.reset(block=True, pool_size=ARCTIC_ASYNC_NTHREADS)


def async_modifier(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        return async_arctic_submit(self, func, True, *args, **kwargs)
    return wrapper


def async_accessor(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        return async_arctic_submit(self, func, False, *args, **kwargs)
    return wrapper
