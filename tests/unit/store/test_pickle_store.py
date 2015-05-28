from bson.binary import Binary
from bson.objectid import ObjectId
import cPickle
import lz4
from mock import create_autospec, sentinel, Mock, call

from arctic.store._pickle_store import PickleStore
from arctic.store._version_store_utils import checksum


def test_write():
    self = create_autospec(PickleStore)
    version = {}
    PickleStore.write(self, sentinel.arctic_lib, version, sentinel.symbol, 'item', sentinel.previous_version)
    assert version['data'] == 'item'


def test_write_object():
    arctic_lib = Mock()
    self = create_autospec(PickleStore)
    version = {'_id': ObjectId()}
    PickleStore.write(self, arctic_lib, version, 'sentinel.symbol', sentinel.item, sentinel.previous_version)
    assert 'data' not in version

    assert version['blob'] == '__chunked__'
    coll = arctic_lib.get_top_level_collection.return_value
    assert coll.update_one.call_args_list == [call({'sha': checksum('sentinel.symbol',
                                                                    {'data': Binary(lz4.compressHC(cPickle.dumps(sentinel.item, cPickle.HIGHEST_PROTOCOL)))}), 'symbol': 'sentinel.symbol'},
                                               {'$set': {'segment': 0,
                                                         'data': Binary(lz4.compressHC(cPickle.dumps(sentinel.item, cPickle.HIGHEST_PROTOCOL)), 0)},
                                                         '$addToSet': {'parent': version['_id']}}, upsert=True)]


def test_read():
    self = create_autospec(PickleStore)
    version = {'data': 'item'}
    assert PickleStore.read(self, sentinel.arctic_lib, version, sentinel.symbol) == 'item'


def test_read_object_backwards_compat():
    self = create_autospec(PickleStore)
    version = {'blob': Binary(lz4.compressHC(cPickle.dumps(object)))}
    assert PickleStore.read(self, sentinel.arctic_lib, version, sentinel.symbol) == object


def test_read_object_2():
    self = create_autospec(PickleStore)
    version = {'_id': sentinel._id,
               'blob': '__chunked__'}
    coll = Mock()
    arctic_lib = Mock()
    coll.find.return_value = [{'data': Binary(lz4.compressHC(cPickle.dumps(object))),
                               'symbol': 'sentinel.symbol'}
                              ]
    arctic_lib.get_top_level_collection.return_value = coll

    assert PickleStore.read(self, arctic_lib, version, sentinel.symbol) == object
    assert coll.find.call_args_list == [call({'symbol': sentinel.symbol, 'parent': sentinel._id}, sort=[('segment', 1)])]
