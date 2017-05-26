import pandas as pd
from six.moves import cPickle
import pytest
import sys
from os import path
from bson.binary import Binary
from bson.objectid import ObjectId
from distutils.version import LooseVersion
from mock import create_autospec, sentinel, Mock, call

from arctic._compression import compress, decompress, compressHC
from arctic.store._pickle_store import PickleStore
from arctic.store._version_store_utils import checksum
from arctic.exceptions import UnsupportedPickleStoreVersion


PANDAS_VERSION = LooseVersion(pd.__version__)


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

    assert version['blob'] == '__chunked__V2'
    coll = arctic_lib.get_top_level_collection.return_value
    assert coll.update_one.call_args_list == [call({'sha': checksum('sentinel.symbol', {'segment':0, 'data': Binary(compress(cPickle.dumps(sentinel.item, cPickle.HIGHEST_PROTOCOL)))}),
                                                    'symbol': 'sentinel.symbol'},
                                                   {'$set': {'segment': 0, 'data': Binary(compress(cPickle.dumps(sentinel.item, cPickle.HIGHEST_PROTOCOL)), 0)},
                                                    '$addToSet': {'parent': version['_id']}}, upsert=True)]


def test_read():
    self = create_autospec(PickleStore)
    version = {'data': 'item'}
    assert PickleStore.read(self, sentinel.arctic_lib, version, sentinel.symbol) == 'item'


def test_read_object_backwards_compat():
    self = create_autospec(PickleStore)
    version = {'blob': Binary(compressHC(cPickle.dumps(object)))}
    assert PickleStore.read(self, sentinel.arctic_lib, version, sentinel.symbol) == object


def test_read_object_2():
    self = create_autospec(PickleStore)
    version = {'_id': sentinel._id,
               'blob': '__chunked__'}
    coll = Mock()
    arctic_lib = Mock()
    coll.find.return_value = [{'data': Binary(compressHC(cPickle.dumps(object))),
                               'symbol': 'sentinel.symbol'}
                              ]
    arctic_lib.get_top_level_collection.return_value = coll

    assert PickleStore.read(self, arctic_lib, version, sentinel.symbol) == object
    assert coll.find.call_args_list == [call({'symbol': sentinel.symbol, 'parent': sentinel._id}, sort=[('segment', 1)])]

@pytest.mark.xfail(sys.version_info >= (3,),
                   reason="lz4 data written with python2 not compatible with python3")
def test_read_backward_compatibility():
    """Test backwards compatibility with a pickled file that's created with Python 2.7.3,
    Numpy 1.7.1_ahl2 and Pandas 0.14.1
    """
    fname = path.join(path.dirname(__file__), "data", "test-data.pkl")

    # For newer versions; verify that unpickling fails when using cPickle
    if PANDAS_VERSION >= LooseVersion("0.16.1"):
        if sys.version_info[0] >= 3:
            with pytest.raises(UnicodeDecodeError), open(fname) as fh:
                cPickle.load(fh)
        else:    
            with pytest.raises(TypeError), open(fname) as fh:
                cPickle.load(fh)

    # Verify that PickleStore() uses a backwards compatible unpickler.
    store = PickleStore()

    with open(fname) as fh:
        # PickleStore compresses data with lz4
        version = {'blob': compressHC(fh.read())}
    df = store.read(sentinel.arctic_lib, version, sentinel.symbol)

    expected = pd.DataFrame(range(4), pd.date_range(start="20150101", periods=4))
    assert (df == expected).all().all()


def test_unpickle_highest_protocol():
    """Pandas version 0.14.1 fails to unpickle a pandas.Series() in compat mode if the
    container has been pickled with HIGHEST_PROTOCOL.
    """
    version = {
        'blob': compressHC(cPickle.dumps(pd.Series(), protocol=cPickle.HIGHEST_PROTOCOL)),
    }

    store = PickleStore()
    ps = store.read(sentinel.arctic_lib, version, sentinel.symbol)

    expected = pd.Series()
    assert (ps == expected).all()


def test_pickle_chunk_V1_read():
    data = {'foo': b'abcdefghijklmnopqrstuvwxyz'}
    version = {'_id': sentinel._id,
               'blob': '__chunked__'}
    coll = Mock()
    arctic_lib = Mock()
    datap = compressHC(cPickle.dumps(data, protocol=cPickle.HIGHEST_PROTOCOL))
    data_1 = datap[0:5]
    data_2 = datap[5:]
    coll.find.return_value = [{'data': Binary(data_1),
                               'symbol': 'sentinel.symbol',
                               'segment': 0},
                              {'data': Binary(data_2),
                               'symbol': 'sentinel.symbol',
                               'segment': 1},
                              ]
    arctic_lib.get_top_level_collection.return_value = coll

    ps = PickleStore()
    assert(data == ps.read(arctic_lib, version, sentinel.symbol))


def test_pickle_store_future_version():
    data = {'foo': b'abcdefghijklmnopqrstuvwxyz'}
    version = {'_id': sentinel._id,
               'blob': '__chunked__VERSION_ONE_MILLION'}
    coll = Mock()
    arctic_lib = Mock()
    datap = compressHC(cPickle.dumps(data, protocol=cPickle.HIGHEST_PROTOCOL))
    data_1 = datap[0:5]
    data_2 = datap[5:]
    coll.find.return_value = [{'data': Binary(data_1),
                               'symbol': 'sentinel.symbol',
                               'segment': 0},
                              {'data': Binary(data_2),
                               'symbol': 'sentinel.symbol',
                               'segment': 1},
                              ]
    arctic_lib.get_top_level_collection.return_value = coll

    ps = PickleStore()
    with pytest.raises(UnsupportedPickleStoreVersion) as e:
        ps.read(arctic_lib, version, sentinel.symbol)
    assert('unsupported version of pickle store' in str(e))


