from datetime import datetime as dt, timedelta

import bson
import numpy as np
from mock import patch

from arctic._util import mongo_count
from arctic.arctic import Arctic


def test_save_read_bson(library):
    blob = {'foo': dt(2015, 1, 1), 'bar': ['a', 'b', ['x', 'y', 'z']]}
    library.write('BLOB', blob)
    saved_blob = library.read('BLOB').data
    assert blob == saved_blob


'''
Run test at your own discretion. Takes > 60 secs
def test_save_read_MASSIVE(library):
    import pandas as pd
    df = pd.DataFrame(data={'data': [1] * 150000000})
    data = (df, df)
    library.write('BLOB', data)
    saved_blob = library.read('BLOB').data
    assert(saved_blob[0].equals(df))
    assert(saved_blob[1].equals(df))
'''


def test_save_read_big_encodable(library):
    blob = {'foo': 'a' * 1024 * 1024 * 20}
    library.write('BLOB', blob)
    saved_blob = library.read('BLOB').data
    assert blob == saved_blob


def test_save_read_bson_object(library):
    blob = {'foo': dt(2015, 1, 1), 'object': Arctic}
    library.write('BLOB', blob)
    saved_blob = library.read('BLOB').data
    assert blob == saved_blob


def test_get_info_bson_object(library):
    blob = {'foo': dt(2015, 1, 1), 'object': Arctic}
    library.write('BLOB', blob)
    assert library.get_info('BLOB')['handler'] == 'PickleStore'


def test_bson_large_object(library):
    blob = {'foo': dt(2015, 1, 1), 'object': Arctic,
            'large_thing': np.random.rand(int(2.1 * 1024 * 1024)).tostring()}
    assert len(blob['large_thing']) > 16 * 1024 * 1024
    library.write('BLOB', blob)
    saved_blob = library.read('BLOB').data
    assert blob == saved_blob


def test_bson_leak_objects_delete(library):
    blob = {'foo': dt(2015, 1, 1), 'object': Arctic}
    library.write('BLOB', blob)
    assert mongo_count(library._collection) == 1
    assert mongo_count(library._collection.versions) == 1
    library.delete('BLOB')
    assert mongo_count(library._collection) == 0
    assert mongo_count(library._collection.versions) == 0


def test_bson_leak_objects_prune_previous(library):
    blob = {'foo': dt(2015, 1, 1), 'object': Arctic}

    yesterday = dt.utcnow() - timedelta(days=1, seconds=1)
    _id = bson.ObjectId.from_datetime(yesterday)
    with patch("bson.ObjectId", return_value=_id):
        library.write('BLOB', blob)
    assert mongo_count(library._collection) == 1
    assert mongo_count(library._collection.versions) == 1

    _id = bson.ObjectId.from_datetime(dt.utcnow() - timedelta(minutes=130))
    with patch("bson.ObjectId", return_value=_id):
        library.write('BLOB', {}, prune_previous_version=False)
    assert mongo_count(library._collection) == 1
    assert mongo_count(library._collection.versions) == 2

    # This write should pruned the oldest version in the chunk collection
    library.write('BLOB', {})
    assert mongo_count(library._collection) == 0
    assert mongo_count(library._collection.versions) == 2


def test_prune_previous_doesnt_kill_other_objects(library):
    blob = {'foo': dt(2015, 1, 1), 'object': Arctic}

    yesterday = dt.utcnow() - timedelta(days=1, seconds=1)
    _id = bson.ObjectId.from_datetime(yesterday)
    with patch("bson.ObjectId", return_value=_id):
        library.write('BLOB', blob, prune_previous_version=False)
    assert mongo_count(library._collection) == 1
    assert mongo_count(library._collection.versions) == 1

    _id = bson.ObjectId.from_datetime(dt.utcnow() - timedelta(hours=10))
    with patch("bson.ObjectId", return_value=_id):
        library.write('BLOB', blob, prune_previous_version=False)
    assert mongo_count(library._collection) == 1
    assert mongo_count(library._collection.versions) == 2

    # This write should pruned the oldest version in the chunk collection
    library.write('BLOB', {})
    assert mongo_count(library._collection) == 1
    assert mongo_count(library._collection.versions) == 2

    library._delete_version('BLOB', 2)
    assert mongo_count(library._collection) == 0
    assert mongo_count(library._collection.versions) == 1


def test_write_metadata(library):
    blob = {'foo': dt(2015, 1, 1), 'object': Arctic}
    library.write(symbol='symX', data=blob, metadata={'key1': 'value1'})
    library.write_metadata(symbol='symX', metadata={'key2': 'value2'})
    v = library.read('symX')
    assert v.data == blob
    assert v.metadata == {'key2': 'value2'}
