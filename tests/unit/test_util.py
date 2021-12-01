from mock import MagicMock, ANY, patch

from arctic._util import are_equals, enable_sharding, mongo_count
from arctic.arctic import Arctic
import arctic._util


def test_are_equals_not_df():
    assert(are_equals(1.0, 2.0) is False)
    assert(are_equals([1, 2, 3], [1, 2, 3]))
    assert(are_equals("Hello", "World") is False)


def test_enable_sharding_hashed():
    m = MagicMock(Arctic, autospec=True)
    enable_sharding(m, "test", hashed=True)
    m._conn.admin.command.assert_called_with('shardCollection', ANY, key={'symbol': 'hashed'})


def test_mongo_count_old_pymongo(monkeypatch):
    monkeypatch.setattr(arctic._util, '_use_new_count_api', None)
    with patch('pymongo.version', '3.6.0'):
        coll = MagicMock()
        mongo_count(coll, filter="_id:1")
        mongo_count(coll, filter={})
        mongo_count(coll)
        assert coll.estimated_document_count.call_count == 0
        assert coll.count_documents.call_count == 0
        assert coll.count.call_count == 3


def test_mongo_count_new_pymongo(monkeypatch):
    monkeypatch.setattr(arctic._util, '_use_new_count_api', None)
    with patch('pymongo.version', '3.11.0'):
        coll2 = MagicMock()
        mongo_count(coll2, filter="_id:1")
        mongo_count(coll2, filter={})
        mongo_count(coll2)
        assert coll2.estimated_document_count.call_count == 2
        assert coll2.count_documents.call_count == 1
        assert coll2.count.call_count == 0
