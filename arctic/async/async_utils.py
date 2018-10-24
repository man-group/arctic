import os
import time
import uuid
from enum import Enum


ARCTIC_DEFAULT_INTERNAL_POOL_NTHREADS = os.environ.get('ARCTIC_DEFAULT_INTERLAN_POOL_NTHREADS', 2)
ARCTIC_SERIALIZER_NTHREADS = os.environ.get('ARCTIC_SERIALIZER_NTHREADS', 2)
ARCTIC_MONGO_NTHREADS = os.environ.get('ARCTIC_MONGO_NTHREADS', 6)
ARCTIC_ASYNC_NTHREADS = os.environ.get('ARCTIC_ASYNC_NTHREADS', 4)

ARCTIC_MONGO_BATCH_SIZE = os.environ.get('ARCTIC_MONGO_BATCH_SIZE', 16)

ARCTIC_MEASURE_INTERNAL_ASYNC = bool(os.environ.get('ARCTIC_MEASURE_INTERNAL_ASYNC'))



class AsyncRequestType(Enum):
    MODIFIER = 'modifier'
    ACCESSOR = 'accessor'


class AsyncRequest(object):
    def __init__(self, kind, library, fun, *args, **kwargs):
        self.id = uuid.uuid4()

        # Request library call spec
        self.fun = fun
        self.args = args
        self.kwargs = kwargs

        # Request meta
        self.kind = kind
        self.library = library
        self.symbol = kwargs.get('symbol')

        # Request's state
        self.future = None
        self.data = None
        self.exception = None
        self.is_running = False
        self.is_completed = False

        # Timekeeping
        self.start_time = None
        self.end_time = None
        self.create_time = time.time()

        self.mongo_retry = bool(kwargs.get('mongo_retry'))

    @property
    def execution_duration(self):
        return self.end_time - self.start_time if self.end_time is not None else -1

    @property
    def schedule_delay(self):
        return self.start_time - self.create_time if self.start_time is not None else -1

    @property
    def total_time(self):
        return self.end_time - self.create_time if self.end_time is not None else -1
