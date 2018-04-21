import lmdb
import re
import hashlib

import cPickle as pickle
import bson
from bson import Binary
import lz4
from weakref import WeakValueDictionary

from datetime import datetime as dt
import threading
from threading import current_thread
from arctic.store.versioned_item import VersionedItem
from arctic.exceptions import NoDataFoundException
import logging

threadLocal = threading.local()
threadLocal.lmdb = WeakValueDictionary()

DATA = '__data__'

logger = logging.getLogger(__name__)

def _get_lmdb_env(data_path):
    try:
        env = threadLocal.lmdb[data_path]
        env.info()
    except:
        env = lmdb.open(data_path, sync=True, writemap=True, max_dbs=10, map_size=50 * 1024 * 1024 * 1024)  # 5OG
        threadLocal.lmdb[data_path] = env
    return env


class LmdbLibrary():


    def checksum(self, item):
        sha = hashlib.sha1()
        sha.update(item)
        return Binary(sha.digest())

    '''
    Lmdb Local VersionStore lookalike, like DictLibrary, but useful for local multiprocess graph execution.
    Only stores one version of each item at a time.
    '''
    def _pack(self, versioned_item):
        data = pickle.dumps(versioned_item.data, protocol=pickle.HIGHEST_PROTOCOL)
        compressed = False

        if len(data) > 2 * 1024 * 1024 * 1024:  # Max bson document size, should probably fix this properly
            data = lz4.compressHC(data)
            compressed = True

        return bson.BSON.encode({'version':versioned_item.version,
                          'compressed': compressed,
                          'metadata':versioned_item.metadata,
                          'symbol':versioned_item.symbol,
                          'sha':self.checksum(data)
                          }), data



    def _unpack(self, version, data):

        rtn = bson.BSON(version).decode()

        if data is not None:
            assert self.checksum(str(data)) == rtn['sha']

            if rtn.get('compressed'):
                data = lz4.decompress(data)
            data = pickle.loads(str(data))

        return VersionedItem(symbol=rtn['symbol'], library=self.data_path, version=rtn['version'],
                                 metadata=rtn['metadata'], data=data)


    def __init__(self, data_path):
        self.data_path = data_path
        logger.info('Data path {}'.format(data_path))
        self.env = _get_lmdb_env(data_path)
        self.mongoose = self

    def __getitem__(self, a):
        return self

    def write(self, item, data, metadata=None):
        logger.info('Writing %s' % item)
        if metadata is None:
            metadata = {}
        metadata['insert_time'] = dt.now()
        with self.env.begin(write=True,) as txn:
            p = txn.get(item)
            if p is not None:
                version = self._unpack(p, None).version + 1
            else:
                version = 1
            v, d = self._pack(VersionedItem(symbol=item,
                                                   library=self.data_path,
                                                   version=version,
                                                   metadata=metadata,
                                                   data=data))

            txn.put(item, v)
            txn.put(item + DATA, d)

            logger.info('Written %s' % item)
            return VersionedItem(symbol=item, library=self.data_path, version=version,
                                 metadata=metadata, data=None)

    def append(self, item, data, metadata):
        raise Exception('Not implemented')

    def read(self, item, version=None, as_of=None):
        return self._read(item, version , as_of)

    def _read(self, item, version=None, as_of=None, include_data=True):
        with self.env.begin(buffers=True) as txn:
            v = txn.get(item)
            if v is not None:
                d = None
                if include_data:
                    d = txn.get(item + DATA)
                rtn = self._unpack(v, d)
                if version is None or rtn.version == version:
                    return rtn
            raise NoDataFoundException()

    def read_metadata(self, item, **kwargs):
        return self._read(item, include_data=False, **kwargs)

    def has_symbol(self, item, as_of=None):
        try:
            self._read(item, version=as_of, include_data=False)
            return True
        except NoDataFoundException:
            return False

    def get_symbols(self, all_symbols=False, snapshot=None, regex=None, **kwargs):
        with self.env.begin() as txn:
            cursor = txn.cursor()
            _it = filter(lambda x: DATA not in x, cursor.iternext_nodup())
            if regex:
                regex = re.compile(regex)
                _it = filter(lambda symbol: regex.match(symbol), _it)
            return list(_it)

    def __contains__(self, item):
        return self.has_symbol(item)

    def snapshot(self, snap_name, metadata=None, skip_symbols=None, versions=None):
        raise NotImplementedError()


    def __getstate__(self):
        return {'data_path': self.data_path,
                }
    def __setstate__(self, state):
        return LmdbLibrary.__init__(self, **state)

    def __enter__(self):
        return self

    def __exit__(self, _1, _2, _3):
        self.close()

    def __del__(self):
        self.close()

    def close(self):
        self.env.close()

