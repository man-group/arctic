from datetime import datetime as dt
from functools import partial
from mock import create_autospec, sentinel, call
import pytest
from pymongo.collection import Collection
import numpy as np
import pandas as pd
import lz4

from arctic.tickstore.tickstore import TickStore, IMAGE_DOC, IMAGE, START, \
    DTYPE, END, COUNT, SYMBOL, COLUMNS, ROWMASK, DATA, INDEX, IMAGE_TIME
from arctic.date import CLOSED_OPEN
from arctic.date._daterange import DateRange
from arctic.date._mktz import mktz
from arctic.exceptions import UnorderedDataException


def test_mongo_date_range_query():
    self = create_autospec(TickStore)
    self._collection = create_autospec(Collection)
    self._symbol_query.return_value = {"sy": { "$in" : [ "s1" , "s2"]}}
    self._collection.aggregate.return_value = iter([{"_id": "s1", "start": dt(2014, 1, 1, 0, 0, tzinfo=mktz())}])

    query = TickStore._mongo_date_range_query(self, 'sym', DateRange(dt(2014, 1, 2, 0, 0, tzinfo=mktz()),
                                                                     dt(2014, 1, 3, 0, 0, tzinfo=mktz())))
    
    assert self._collection.aggregate.call_args_list == [call([
     {"$match": {"s": {"$lte": dt(2014, 1, 2, 0, 0, tzinfo=mktz())}, "sy": { "$in" : [ "s1" , "s2"]}}},
     {"$project": {"_id": 0, "s": 1, "sy": 1}},
     {"$group": {"_id": "$sy", "start": {"$max": "$s"}}},
     {"$sort": {"start": 1}},
     {"$limit": 1}])]
    assert query == {'s': {'$gte': dt(2014, 1, 1, 0, 0, tzinfo=mktz()), '$lte': dt(2014, 1, 3, 0, 0, tzinfo=mktz())}}


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
    tz = 'UTC'
    initial_image = {'index': dt(2014, 1, 1, 0, 0, tzinfo=mktz(tz)), 'A': 123, 'B': 54.4, 'C': 'DESC'}
    data = [{'index': dt(2014, 1, 1, 0, 1, tzinfo=mktz(tz)), 'A': 124, 'D': 0},
            {'index': dt(2014, 1, 1, 0, 2, tzinfo=mktz(tz)), 'A': 125, 'B': 27.2}]
    bucket, final_image = TickStore._to_bucket(data, symbol, initial_image)
    assert bucket[COUNT] == 2
    assert bucket[END] == dt(2014, 1, 1, 0, 2, tzinfo=mktz(tz))
    assert set(bucket[COLUMNS]) == set(('A', 'B', 'D'))
    assert set(bucket[COLUMNS]['A']) == set((ROWMASK, DTYPE, DATA))
    assert get_coldata(bucket[COLUMNS]['A']) == ([124, 125], [1, 1, 0, 0, 0, 0, 0, 0])
    assert get_coldata(bucket[COLUMNS]['B']) == ([27.2], [0, 1, 0, 0, 0, 0, 0, 0])
    assert get_coldata(bucket[COLUMNS]['D']) == ([0], [1, 0, 0, 0, 0, 0, 0, 0])
    index = [dt.fromtimestamp(int(i/1000)).replace(tzinfo=mktz(tz)) for i in
             list(np.cumsum(np.fromstring(lz4.decompress(bucket[INDEX]), dtype='uint64')))]
    assert index == [i['index'] for i in data]
    assert bucket[COLUMNS]['A'][DTYPE] == 'int64'
    assert bucket[COLUMNS]['B'][DTYPE] == 'float64'
    assert bucket[SYMBOL] == symbol
    assert bucket[START] == initial_image['index']
    assert bucket[IMAGE_DOC][IMAGE] == initial_image
    assert bucket[IMAGE_DOC] == {IMAGE: initial_image,
                                 IMAGE_TIME: initial_image['index']}
    assert final_image == {'index': data[-1]['index'], 'A': 125, 'B': 27.2, 'C': 'DESC', 'D': 0}


def test_tickstore_to_bucket_always_forwards():
    symbol = 'SYM'
    tz = 'UTC'
    initial_image = {'index': dt(2014, 1, 1, 0, 0, tzinfo=mktz(tz)), 'A': 123, 'B': 54.4, 'C': 'DESC'}
    data = [{'index': dt(2014, 2, 1, 0, 1, tzinfo=mktz(tz)), 'A': 124, 'D': 0},
            {'index': dt(2014, 1, 1, 0, 1, tzinfo=mktz(tz)), 'A': 125, 'B': 27.2}]
    with pytest.raises(UnorderedDataException):
        TickStore._to_bucket(data, symbol, initial_image)


def test_tickstore_to_bucket_always_forwards_image():
    symbol = 'SYM'
    tz = 'UTC'
    initial_image = {'index': dt(2014, 2, 1, 0, 0, tzinfo=mktz(tz)), 'A': 123, 'B': 54.4, 'C': 'DESC'}
    data = [{'index': dt(2014, 1, 1, 0, 1, tzinfo=mktz(tz)), 'A': 124, 'D': 0}]
    with pytest.raises(UnorderedDataException) as e:
        TickStore._to_bucket(data, symbol, initial_image)


def get_coldata(coldata):
    """ return values and rowmask """
    dtype = np.dtype(coldata[DTYPE])
    values = np.fromstring(lz4.decompress(coldata[DATA]), dtype=dtype)
    rowmask = np.unpackbits(np.fromstring(lz4.decompress(coldata[ROWMASK]), dtype='uint8'))
    return list(values), list(rowmask)


def test_tickstore_pandas_to_bucket_image():
    symbol = 'SYM'
    tz = 'UTC'
    initial_image = {'index': dt(2014, 1, 1, 0, 0, tzinfo=mktz(tz)), 'A': 123, 'B': 54.4, 'C': 'DESC'}
    data = [{'A': 120, 'D': 1}, {'A': 122, 'B': 2.0}, {'A': 3, 'B': 3.0, 'D': 1}]
    tick_index = [dt(2014, 1, 2, 0, 0, tzinfo=mktz(tz)),
                  dt(2014, 1, 3, 0, 0, tzinfo=mktz(tz)),
                  dt(2014, 1, 4, 0, 0, tzinfo=mktz(tz))]
    data = pd.DataFrame(data, index=tick_index)
    bucket, final_image = TickStore._pandas_to_bucket(data, symbol, initial_image)
    assert final_image == {'index': dt(2014, 1, 4, 0, 0, tzinfo=mktz(tz)), 'A': 3, 'B': 3.0, 'C': 'DESC', 'D': 1}
    assert IMAGE_DOC in bucket
    assert bucket[COUNT] == 3
    assert bucket[START] == dt(2014, 1, 1, 0, 0, tzinfo=mktz(tz))
    assert bucket[END] == dt(2014, 1, 4, 0, 0, tzinfo=mktz(tz))
    assert set(bucket[COLUMNS]) == set(('A', 'B', 'D'))
    assert set(bucket[COLUMNS]['A']) == set((ROWMASK, DTYPE, DATA))
    assert get_coldata(bucket[COLUMNS]['A']) == ([120, 122, 3], [1, 1, 1, 0, 0, 0, 0, 0])
    values, rowmask = get_coldata(bucket[COLUMNS]['B'])
    assert np.isnan(values[0]) and values[1:] == [2.0, 3.0]
    assert rowmask == [1, 1, 1, 0, 0, 0, 0, 0]
    values, rowmask = get_coldata(bucket[COLUMNS]['D'])
    assert np.isnan(values[1])
    assert values[0] == 1 and values[2] == 1
    assert rowmask == [1, 1, 1, 0, 0, 0, 0, 0]
    index = [dt.fromtimestamp(int(i/1000)).replace(tzinfo=mktz(tz)) for i in
             list(np.cumsum(np.fromstring(lz4.decompress(bucket[INDEX]), dtype='uint64')))]
    assert index == tick_index
    assert bucket[COLUMNS]['A'][DTYPE] == 'int64'
    assert bucket[COLUMNS]['B'][DTYPE] == 'float64'
    assert bucket[SYMBOL] == symbol
    assert bucket[IMAGE_DOC] == {IMAGE: initial_image,
                                 IMAGE_TIME: initial_image['index']}
