try:
    import cStringIO as stringio
except ImportError:
    import io as stringio
from contextlib import contextmanager
from datetime import datetime as dt
import sys

import dateutil
from dateutil.rrule import rrule, DAILY
import pandas

import numpy as np


def dt_or_str_parser(string):
    try:
        return dateutil.parser.parse(string)
    except ValueError:
        return string.strip()


def read_str_as_pandas(ts_str, num_index=1):
    labels = [x.strip() for x in ts_str.split('\n')[0].split('|')]
    pd = pandas.read_csv(stringio.StringIO(ts_str), sep='|', index_col=list(range(num_index)), date_parser=dt_or_str_parser)
    # Trim the whitespace on the column names
    pd.columns = labels[num_index:]
    pd.index.names = labels[0:num_index]
    return pd


def get_large_ts(size=2500):
    timestamps = list(rrule(DAILY, count=size, dtstart=dt(1970, 1, 1), interval=1))
    pd = pandas.DataFrame(index=timestamps, data={'n' + str(i): np.random.random_sample(size) for i in range(size)})
    pd.index.name = 'index'
    return pd


@contextmanager
def _save_argv():
    args = sys.argv[:]
    yield
    sys.argv = args


def run_as_main(fn, *args):
    """ Run a given function as if it was the
    system entry point, eg for testing scripts.

    Eg::

        from scripts.Foo import main

        run_as_main(main, 'foo','bar')

    This is equivalent to ``Foo foo bar``, assuming
    ``scripts.Foo.main`` is registered as an entry point.
    """
    with _save_argv():
        print("run_as_main: %s" % str(args))
        sys.argv = ['progname'] + list(args)
        return fn()
