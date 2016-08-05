from arctic._util import are_equals, enable_sharding
from mock import MagicMock, ANY
from arctic.arctic import Arctic


def test_are_equals_not_df():
    assert(are_equals(1.0, 2.0) is False)
    assert(are_equals([1, 2, 3], [1,2,3]))
    assert(are_equals("Hello", "World") is False)


def test_enable_sharding_hashed():
    m = MagicMock(Arctic, autospec=True)
    enable_sharding(m, "test", hashed=True)
    m._conn.admin.command.assert_called_with('shardCollection', ANY, key={'symbol': 'hashed'})
