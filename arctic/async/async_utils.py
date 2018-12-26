import time
import uuid

from enum import Enum

from arctic.exceptions import RequestDurationException


class AsyncRequestType(Enum):
    MODIFIER = 'modifier'
    ACCESSOR = 'accessor'


class AsyncRequest(object):
    def __init__(self, kind, library, fun, callback, *args, **kwargs):
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
        self.callback = callback
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
        if None in (self.start_time, self.end_time):
            raise RequestDurationException("{} can't provide an execution_duration {}.".format(
                self, (self.start_time, self.end_time)))
        return self.end_time - self.start_time

    @property
    def schedule_delay(self):
        if None in (self.start_time, self.create_time):
            raise RequestDurationException("{} can't provide a schedule_delay {}.".format(
                self, (self.start_time, self.create_time)))
        return self.start_time - self.create_time

    @property
    def total_time(self):
        if None in (self.end_time, self.create_time):
            raise RequestDurationException("{} can't provide a total_time {}.".format(
                self, (self.end_time, self.create_time)))
        return self.end_time - self.create_time

    def __str__(self):
        return "Request id:{} library:{}, symbol:{} fun:{}, kind:{}".format(
            self.id, self.library, self.symbol, getattr(self.fun, '__name__', None), self.kind)
