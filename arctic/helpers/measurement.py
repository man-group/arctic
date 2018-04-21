import time
from contextlib import  contextmanager

MEASUREMENTS = dict()
MEASUREMENT_ENABLED=False


def enable_measurements():
    global MEASUREMENT_ENABLED
    MEASUREMENT_ENABLED = True


def disable_measurements():
    global MEASUREMENT_ENABLED
    MEASUREMENT_ENABLED = False


def add_measurement(key, value):
    if key not in MEASUREMENTS:
        MEASUREMENTS[key] = [value]
    else:
        MEASUREMENTS[key].append(value)


def reset_measurements():
    for k, v in MEASUREMENTS.iteritems():
        del v[:]


@contextmanager
def measure_block(key, omit_on_exception=True):
    if MEASUREMENT_ENABLED:
        skip = False
        start = time.time()
        try:
            yield
        except Exception:
            skip = omit_on_exception
            raise 
        finally:
            if not skip:
                add_measurement(key, time.time() - start)
    else:
        yield
