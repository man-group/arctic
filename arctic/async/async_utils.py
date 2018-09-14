import uuid
from enum import Enum
from functools import wraps


def async_rlock(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print('Calling with read lock', func.__name__)
        return func(*args, **kwargs)
    return wrapper


def async_wlock(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print('Calling with write lock', func.__name__)
        return func(*args, **kwargs)
    return wrapper


class AsyncRequestType(Enum):
    MODIFIER = 'modifier'
    ACCESSOR = 'accessor'


class AsyncRequest(object):
    def __init__(self, kind, library, symbol, fun, *args, **kwargs):
        self.id = uuid.uuid4()
        self.fun = fun
        self.args = args
        self.kwargs = kwargs
        self.kind = kind
        self.library = library
        self.symbol = symbol

        # Request's state
        self.future = None
        self.data = None

        # Timekeeping
        self.start_time = None
        self.end_time = None
        self.create_time = time.time()
