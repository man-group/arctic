from contextlib import contextmanager


@contextmanager
def enable_profiling_for_library(library):
    library._arctic_lib._db.set_profiling_level(2)
    yield library._arctic_lib._db['system.profile']
    library._arctic_lib._db.set_profiling_level(0, slow_ms=100)