from datetime import datetime as dt
from functools import partial
from mock import create_autospec, sentinel, call
import pytest
from pymongo.collection import Collection

from arctic.tickstore.tickstore import TickStore
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
