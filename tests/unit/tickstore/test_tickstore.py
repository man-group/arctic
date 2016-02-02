from datetime import datetime as dt
from functools import partial
from mock import create_autospec, sentinel, call
import pytest
from pymongo.collection import Collection
import numpy as np
import pandas as pd

from arctic.tickstore.tickstore import TickStore, IMAGE_DOC, IMAGE, START, DTYPE, END, COUNT, SYMBOL, COLUMNS
from arctic.date import CLOSED_OPEN
from arctic.date._daterange import DateRange
from arctic.date._mktz import mktz


def test_mongo_date_range_query():
    self = create_autospec(TickStore)
    self._collection = create_autospec(Collection)
    self._collection.find_one.return_value = {'s': sentinel.start}
    self._symbol_query = partial(TickStore._symbol_query, self)
    query = TickStore._mongo_date_range_query(self, 'sym', DateRange(dt(2014, 1, 1, 0, 0, tzinfo=mktz()),
                                                                     dt(2014, 1, 2, 0, 0, tzinfo=mktz())))
    assert self._collection.find_one.call_args_list == [call({'sy': 'sym', 's': {'$lte': dt(2014, 1, 1, 0, 0, tzinfo=mktz())}},
                                                             sort=[('s', -1)], projection={'s': 1, '_id': 0}),
                                                        call({'sy': 'sym', 's': {'$gt': dt(2014, 1, 2, 0, 0, tzinfo=mktz())}},
                                                             sort=[('s', 1)], projection={'s': 1, '_id': 0})]
    assert query == {'s': {'$gte': sentinel.start, '$lt': sentinel.start}}


def test_mongo_date_range_query_asserts():
    self = create_autospec(TickStore)
    self._collection = create_autospec(Collection)
    self._collection.find_one.return_value = {'s': sentinel.start}
    with pytest.raises(AssertionError):
        TickStore._mongo_date_range_query(self, 'sym', DateRange(None, None, CLOSED_OPEN))

    with pytest.raises(AssertionError):
        TickStore._mongo_date_range_query(self, 'sym', DateRange(dt(2014, 1, 1), None))

    with pytest.raises(AssertionError):
        TickStore._mongo_date_range_query(self, 'sym', DateRange(None, dt(2014, 1, 1)))


def test_strify_tickstore():
    # Fix GH issue 49 - str(tick library) fails in IPython
    self = create_autospec(TickStore)
    self._arctic_lib = sentinel.library
    assert 'sentinel.library' in TickStore.__str__(self)


def test_tickstore_to_bucket_no_image():
    symbol = 'SYM'
    data = [{'index': dt(2014, 1, 1, 0, 1, tzinfo=mktz()), 'A': 124, 'D': 0},
            {'index': dt(2014, 1, 1, 0, 2, tzinfo=mktz()), 'A': 125, 'B': 27.2}]
    bucket, final_image = TickStore._to_bucket(data, symbol, None)
    assert bucket[COUNT] == 2
    assert bucket[END] == dt(2014, 1, 1, 0, 2, tzinfo=mktz())
    assert bucket[SYMBOL] == symbol
    assert bucket[START] == dt(2014, 1, 1, 0, 1, tzinfo=mktz())
    assert 'A' in bucket[COLUMNS]
    assert IMAGE_DOC not in bucket
    assert not final_image


def test_tickstore_to_bucket_with_image():
    symbol = 'SYM'
    initial_image = {'index': dt(2014, 1, 1, 0, 0, tzinfo=mktz()), 'A': 123, 'B': 54.4, 'C': 'DESC'}
    data = [{'index': dt(2014, 1, 1, 0, 1, tzinfo=mktz()), 'A': 124, 'D': 0},
            {'index': dt(2014, 1, 1, 0, 2, tzinfo=mktz()), 'A': 125, 'B': 27.2}]
    bucket, final_image = TickStore._to_bucket(data, symbol, initial_image)
    assert bucket[COUNT] == 2
    assert bucket[END] == dt(2014, 1, 1, 0, 2, tzinfo=mktz())
    assert bucket[SYMBOL] == symbol
    assert bucket[START] == dt(2014, 1, 1, 0, 0, tzinfo=mktz())
    assert final_image == {'index': dt(2014, 1, 1, 0, 2, tzinfo=mktz()), 'A': 125, 'B': 27.2, 'C': 'DESC', 'D': 0}


def test_tickstore_pandas_to_bucket_image():
    symbol = 'SYM'
    initial_image = {'index': dt(2014, 1, 1, 0, 0, tzinfo=mktz()), 'A': 123, 'B': 54.4, 'C': 'DESC'}
    data = [{'A': 120, 'D': 1}, {'A': 122, 'B': 2.0}, {'A': 3, 'B': 3.0, 'D': 1}]
    data = pd.DataFrame(data, index=[dt(2014, 1, 2, 0, 0, tzinfo=mktz()), dt(2014, 1, 3, 0, 0, tzinfo=mktz()),
                                     dt(2014, 1, 4, 0, 0, tzinfo=mktz())])
    bucket, final_image = TickStore._pandas_to_bucket(data, symbol, initial_image)
    assert final_image == {'index': dt(2014, 1, 4, 0, 0, tzinfo=mktz()), 'A': 3, 'B': 3.0, 'C': 'DESC', 'D': 1}
    assert IMAGE_DOC in bucket
    assert bucket[COUNT] == 3
    assert bucket[START] == dt(2014, 1, 1, 0, 0, tzinfo=mktz())
    assert bucket[END] == dt(2014, 1, 4, 0, 0, tzinfo=mktz())
    assert bucket[SYMBOL] == symbol
    assert bucket[IMAGE_DOC] == {IMAGE: initial_image,
                                 START: 0,
                                 DTYPE: dt(2014, 1, 1, 0, 0, tzinfo=mktz())}
