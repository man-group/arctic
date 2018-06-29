import bson
import six
import struct
from datetime import datetime as dt, timedelta as dtd
import pandas as pd
from pandas.util.testing import assert_frame_equal
from pymongo.errors import OperationFailure
from pymongo.server_type import SERVER_TYPE
from datetime import datetime
from mock import Mock, patch
import inspect
import time
import pytest
import numpy as np

import arctic
from arctic.exceptions import NoDataFoundException, DuplicateSnapshotException, ArcticException
from arctic.date import DateRange
from arctic.store import _version_store_utils

from ...util import read_str_as_pandas
from arctic.date._mktz import mktz
import pymongo


ts1 = read_str_as_pandas("""         times | near
                   2012-09-08 17:06:11.040 |  1.0
                   2012-10-08 17:06:11.040 |  2.0
                   2012-10-09 17:06:11.040 |  2.5
                   2012-11-08 17:06:11.040 |  3.0""")

ts2 = read_str_as_pandas("""         times | near
                   2012-09-08 17:06:11.040 |  1.0
                   2012-10-08 17:06:11.040 |  4.0
                   2012-10-09 17:06:11.040 |  4.5
                   2012-10-10 17:06:11.040 |  5.0
                   2012-11-08 17:06:11.040 |  3.0""")

ts1_append = read_str_as_pandas("""  times | near
                   2012-09-08 17:06:11.040 |  1.0
                   2012-10-08 17:06:11.040 |  2.0
                   2012-10-09 17:06:11.040 |  2.5
                   2012-11-08 17:06:11.040 |  3.0
                   2012-11-09 17:06:11.040 |  3.0""")


symbol = 'TS1'


from pymongo.cursor import _QUERY_OPTIONS
from pymongo.message import query as __query
def _query(allow_secondary, library_name):
    def _internal_query(options, *args, **kwargs):
        coll_name = args[0]
        data_coll_name = 'arctic_{}'.format(library_name)
        versions_coll_name = data_coll_name + '.versions'
        if allow_secondary and coll_name in (data_coll_name, versions_coll_name):
            # Reads to the Version and Chunks collections are allowed to slaves
            assert bool(options & _QUERY_OPTIONS['slave_okay']) == allow_secondary, "{}: options:{}".format(coll_name, options)
        elif '.$cmd' not in coll_name:
            # All other collections we force PRIMARY read.
            assert bool(options & _QUERY_OPTIONS['slave_okay']) == False, "{}: options:{}".format(coll_name, options)
        return __query(options, *args, **kwargs)
    return _internal_query


# MongoDB always sets slaveOk when talking to a single server.
# Pretend we're a mongos for the tests that care...
#
# A _Query's slaveOk bit is already set for queries with non-primary
# read preference. If this is a direct connection to a mongod, override
# and *always* set the slaveOk bit. See bullet point 2 in
# server-selection.rst#topology-type-single.
# set_slave_ok = (
#     topology.description.topology_type == TOPOLOGY_TYPE.Single
#    and server.description.server_type != SERVER_TYPE.Mongos)


def test_store_item_new_version(library, library_name):
    with patch('pymongo.message.query', side_effect=_query(False, library_name)), \
         patch('pymongo.server_description.ServerDescription.server_type', SERVER_TYPE.Mongos):
        library.write(symbol, ts1)
        coll = library._collection
        count = coll.count()
        assert coll.versions.count() == 1

        # No change to the TS
        library.write(symbol, ts1, prune_previous_version=False)
        assert coll.count() == count
        assert coll.versions.count() == 2


def test_store_item_read_preference(library_secondary, library_name):
    with patch('arctic.arctic.ArcticLibraryBinding.check_quota'), \
         patch('pymongo.message.query', side_effect=_query(False, library_name)) as query, \
         patch('pymongo.server_description.ServerDescription.server_type', SERVER_TYPE.Mongos):
        # write an item
        library_secondary.write(symbol, ts1)
        library_secondary.write(symbol, ts1_append, prune_previous_version=False)
        # delete an individual version
        library_secondary._delete_version(symbol, 1)
    # delete the item entirely
    library_secondary.delete(symbol)
    assert query.call_count > 0


def test_read_item_read_preference_SECONDARY(library_secondary, library_name):
    # write an item
    library_secondary.write(symbol, ts1)
    with patch('pymongo.message.query', side_effect=_query(True, library_name)) as query, \
         patch('pymongo.server_description.ServerDescription.server_type', SERVER_TYPE.Mongos):
        library_secondary.read(symbol)
    assert query.call_count > 0


def test_query_falls_back_to_primary(library_secondary, library_name):
    allow_secondary = [True]
    def _query(options, *args, **kwargs):
        # If we're allowing secondary read and an error occurs when reading a chunk.
        # We should attempt a call to primary only subsequently.
        # In newer MongoDBs we query <database>.$cmd rather than <database>.<collection>
        if args[0].startswith('arctic_{}.'.format(library_name.split('.')[0])) and \
                    bool(options & _QUERY_OPTIONS['slave_okay']) == True:
            allow_secondary[0] = False
            raise OperationFailure("some_error")
        return __query(options, *args, **kwargs)

    library_secondary.write(symbol, ts1)
    with patch('pymongo.message.query', side_effect=_query), \
         patch('pymongo.server_description.ServerDescription.server_type', SERVER_TYPE.Mongos):
        assert library_secondary.read(symbol) is not None
    # We raised at least once on a secondary read
    assert allow_secondary[0] == False


def test_store_item_metadata(library):
    library.write(symbol, ts1, metadata={'key': 'value'})

    after = library.read(symbol)

    assert after.metadata['key'] == 'value'
    assert after.version
    assert_frame_equal(after.data, ts1)


def test_read_metadata(library):
    library.write(symbol, ts1, metadata={'key': 'value'})

    after = library.read_metadata(symbol)

    assert after.metadata['key'] == 'value'
    assert after.version
    assert after.data is None


def test_read_metadata_newer_version_with_lower_id(library):
    now_timestamp = int(time.time())
    now = struct.pack(">i", now_timestamp)
    old_id = bson.ObjectId(now + b"\x00\x00\x00\x00\x00\x00\x00\x00")
    new_id = bson.ObjectId(now + b"\x00\x00\x00\x00\x00\x00\x00\x01")
    object_id_class = Mock()
    object_id_class.from_datetime = bson.ObjectId.from_datetime

    object_id_class.return_value = new_id
    with patch("bson.ObjectId", object_id_class):
        library.write(symbol, ts1)

    library.snapshot('s1')

    object_id_class.return_value = old_id
    with patch("bson.ObjectId", object_id_class):
        library.write(symbol, ts2)

    now_dt = datetime.fromtimestamp(now_timestamp)
    assert library.read_metadata(symbol, as_of=now_dt).version == 2


def test_read_metadata_throws_on_deleted_symbol(library):
    library.write(symbol, ts1, metadata={'key': 'value'})
    library.delete(symbol)

    with pytest.raises(NoDataFoundException):
        library.read_metadata(symbol)


def test_store_item_and_update(library):
    coll = library._collection

    # Store the first timeseries
    none = datetime.now()
    time.sleep(1)
    library.write(symbol, ts1)
    original = datetime.now()

    # Assertions:
    assert coll.versions.count() == 1
    assert_frame_equal(library.read(symbol).data, ts1)

    # Update the TimeSeries
    time.sleep(1)
    library.write(symbol, ts2, prune_previous_version=False)
    recent = datetime.now()

    assert coll.versions.count() == 2
    assert_frame_equal(library.read(symbol).data, ts2)

    # Get the different versions of the DB
    with pytest.raises(NoDataFoundException):
        library.read(symbol, as_of=none)
    assert_frame_equal(library.read(symbol, as_of=original).data, ts1)
    assert_frame_equal(library.read(symbol, as_of=recent).data, ts2)

    # Now push back in the original version
    time.sleep(1)
    library.write(symbol, ts1, prune_previous_version=False)

    assert coll.versions.count() == 3
    assert_frame_equal(library.read(symbol).data, ts1)

    # Get the different versions of the DB
    with pytest.raises(NoDataFoundException):
        library.read(symbol, as_of=none)
    assert_frame_equal(library.read(symbol, as_of=original).data, ts1)
    assert_frame_equal(library.read(symbol, as_of=recent).data, ts2)
    assert_frame_equal(library.read(symbol, as_of=datetime.now()).data, ts1)


def test_append_update(library):
    library.write(symbol, ts1)
    library.snapshot('snap')

    coll = library._collection

    # Assertions:
    assert coll.versions.count() == 1
    assert_frame_equal(library.read(symbol).data, ts1)

    # Append an item
    dts = list(ts1.index)
    dts.append(dts[-1] + dtd(days=1))
    values = list(ts1.near.values)
    values.append(47.)
    ts2 = pd.DataFrame(index=dts, data=values, columns=ts1.columns)
    ts2.index.name = ts1.index.name

    # Saving ts2 shouldn't create any new chunks.  Instead it should
    # reuse the last chunk.
    library.write(symbol, ts2, prune_previous_version=False)
    assert coll.versions.count() == 2
    assert_frame_equal(library.read(symbol, as_of='snap').data, ts1)
    assert_frame_equal(library.read(symbol).data, ts2)

    # We should be able to save a smaller timeseries too
    # This isn't likely to happen, so we don't care too much about space saving
    # just make sure we get it right.
    library.write(symbol, ts1, prune_previous_version=False)
    assert_frame_equal(library.read(symbol, as_of=1).data, ts1)
    assert_frame_equal(library.read(symbol, as_of=2).data, ts2)
    assert_frame_equal(library.read(symbol, as_of=3).data, ts1)

    # Append an item, and add a whole new chunk
    dts = list(ts2.index)
    dts.append(dts[-1] + dtd(days=1))
    dts.append(dts[-1] + dtd(days=40))
    values = list(ts2.near.values)
    values.append(47.)
    values.append(53.)
    ts3 = pd.DataFrame(index=dts, data=values, columns=ts1.columns)
    ts3.index.name = ts1.index.name

    library.write(symbol, ts3, prune_previous_version=False)
    assert_frame_equal(library.read(symbol, as_of=1).data, ts1)
    assert_frame_equal(library.read(symbol, as_of=2).data, ts2)
    assert_frame_equal(library.read(symbol, as_of=3).data, ts1)
    assert_frame_equal(library.read(symbol, as_of=4).data, ts3)

    library.write(symbol, ts3, prune_previous_version=False)
    assert_frame_equal(library.read(symbol, as_of=1).data, ts1)
    assert_frame_equal(library.read(symbol, as_of=2).data, ts2)
    assert_frame_equal(library.read(symbol, as_of=3).data, ts1)
    assert_frame_equal(library.read(symbol, as_of=4).data, ts3)
    assert_frame_equal(library.read(symbol, as_of=5).data, ts3)


def test_append(library):
    library.append(symbol, ts1, upsert=True)
    library.append(symbol, ts1_append, upsert=True)
    assert len(library.read(symbol).data) == len(ts1) + len(ts1_append)


def test_append_should_overwrite_after_delete(library):
    library.append(symbol, ts1, upsert=True)
    library.append(symbol, ts1_append, upsert=True)
    assert len(library.read(symbol).data) == len(ts1) + len(ts1_append)
    library.delete(symbol)
    library.append(symbol, ts1_append, upsert=True)
    assert len(library.read(symbol).data) == len(ts1_append)


def test_append_empty_ts(library):
    data = library.append(symbol, ts1, upsert=True)
    assert(data.version == 1)
    data = library.append(symbol, pd.DataFrame(), upsert=True)
    assert(data.version == 1)
    assert len(library.read(symbol).data) == len(ts1)


def test_append_corrupted_new_version(library):
    to_append = read_str_as_pandas("""  times | near
                      2012-11-09 17:06:11.040 |  30.0""")
    to_append_2 = read_str_as_pandas("""  times | near
                      2012-11-10 17:06:11.040 |  40.0""")
    library.write(symbol, ts1)
    # Append version
    library.append(symbol, to_append)
    # The append went wrong, and the new version document (written last), not available
    library._versions.find_one_and_delete({'symbol': symbol}, sort=[('version', pymongo.DESCENDING)])

    # Should still be able to append new data
    library.append(symbol, to_append_2, upsert=True)
    assert library.read(symbol).data['near'][-1] == 40.
    assert len(library.read(symbol).data) == len(ts1) + 1


def test_query_version_as_of_int(library):
    # Store the first timeseries
    library.write(symbol, ts1)
    library.write(symbol, ts2, prune_previous_version=False)

    assert_frame_equal(library.read(symbol, as_of=1).data, ts1)
    assert_frame_equal(library.read(symbol).data, ts2)


def test_list_version(library):
    assert len(list(library.list_versions(symbol))) == 0
    dates = [None, None, None]
    now = dt.utcnow().replace(tzinfo=mktz('UTC'))
    for x in six.moves.xrange(len(dates)):
        dates[x] = now - dtd(minutes=130 - x)
        with patch("bson.ObjectId", return_value=bson.ObjectId.from_datetime(dates[x])):
            library.write(symbol, ts1, prune_previous_version=False)
    assert len(list(library.list_versions(symbol))) == 3

    library.write(symbol, ts1, prune_previous_version=True)
    assert len(list(library.list_versions(symbol))) >= 2

    versions = list(library.list_versions(symbol))
    for i, x in enumerate([4, 3]):
        assert versions[i]['symbol'] == symbol
        assert versions[i]['date'] >= dates[i]
        assert versions[i]['version'] == x


def test_list_version_deleted(library):
    assert len(library.list_versions(symbol)) == 0
    library.write(symbol, ts1, prune_previous_version=False)
    assert len(library.list_versions(symbol)) == 1
    # Snapshot the library so we keep the sentinel version
    library.snapshot('xxx', versions={symbol: 1})
    library.delete(symbol)
    versions = library.list_versions(symbol)
    assert len(versions) == 2
    assert versions[0]['symbol'] == symbol
    assert versions[0]['version'] == 2
    assert versions[0]['snapshots'] == []
    assert versions[0]['deleted'] == True

    assert versions[1]['symbol'] == symbol
    assert versions[1]['version'] == 1
    assert versions[1]['deleted'] == False
    assert versions[1]['snapshots'] == ['xxx']


def test_list_version_latest_only(library):
    assert len(list(library.list_versions(symbol))) == 0
    dates = [None, None, None]
    now = dt.utcnow().replace(tzinfo=mktz('UTC'))
    for x in six.moves.xrange(len(dates)):
        dates[x] = now - dtd(minutes=20 - x)
        with patch("bson.ObjectId", return_value=bson.ObjectId.from_datetime(dates[x])):
            library.write(symbol, ts1, prune_previous_version=False)
    assert len(list(library.list_versions(symbol))) == 3

    library.write(symbol, ts1, prune_previous_version=True)
    assert len(list(library.list_versions(symbol, latest_only=True))) == 1

    versions = list(library.list_versions(symbol))
    for i, x in enumerate([4, ]):
        assert versions[i]['symbol'] == symbol
        assert versions[i]['date'] >= dates[i]
        assert versions[i]['version'] == x


def test_list_version_snapshot(library):
    library.write('A', ts1)
    library.snapshot('one')
    library.write('B', ts2)
    library.snapshot('two')
    library.write('A', ts2)
    library.snapshot('three')
    library.write('C', ts2)

    assert set(x['symbol'] for x in library.list_versions()) \
        == set(['A', 'B', 'C'])

    assert set(x['symbol'] for x in library.list_versions(snapshot='one')) \
        == set(['A'])

    assert set(x['symbol'] for x in library.list_versions(snapshot='two')) \
        == set(['A', 'B'])

    assert set(x['symbol'] for x in library.list_versions(snapshot='three')) \
        == set(['A', 'B'])

    assert [x['snapshots'] for x in library.list_versions(symbol='A')] \
        == [['three', ], ['one', 'two']]

    assert [x['snapshots'] for x in library.list_versions(symbol='B')] \
        == [['two', 'three']]

    assert all('parent' not in x for x in library.list_versions(symbol='C'))


def test_delete_versions(library):
    library.write(symbol, ts1)
    library.write(symbol, ts2, prune_previous_version=False)
    library.write(symbol, ts1, prune_previous_version=False)
    library.write(symbol, ts2, prune_previous_version=False)

    coll = library._collection

    # Delete version 1 (ts1)
    library._delete_version(symbol, 1)
    assert_frame_equal(library.read(symbol, as_of=2).data, ts2)
    assert_frame_equal(library.read(symbol, as_of=3).data, ts1)

    library._delete_version(symbol, 2)
    assert_frame_equal(library.read(symbol, as_of=3).data, ts1)
    assert_frame_equal(library.read(symbol, as_of=4).data, ts2)

    library._delete_version(symbol, 3)
    assert_frame_equal(library.read(symbol).data, ts2)

    library._delete_version(symbol, 4)
    assert coll.count() == 0


def test_delete_bson_versions(library):
    coll = library._collection

    a = [{'a':'b'}]
    c = [{'c':'d'}]
    library.write(symbol, a)
    library.write(symbol, c, prune_previous_version=False)
    library.write(symbol, a, prune_previous_version=False)
    library.write(symbol, c, prune_previous_version=False)
    assert coll.versions.count() == 4

    library._delete_version(symbol, 1)
    assert library.read(symbol, as_of=2).data == c
    assert library.read(symbol, as_of=3).data == a
    assert coll.versions.count() == 3

    library._delete_version(symbol, 2)
    assert library.read(symbol, as_of=3).data == a
    assert library.read(symbol, as_of=4).data == c
    assert coll.versions.count() == 2

    library._delete_version(symbol, 3)
    assert coll.versions.count() == 1
    assert library.read(symbol).data == c

    library._delete_version(symbol, 4)
    assert coll.versions.count() == 0


def test_read_none_does_not_exception(library):
    library.write(symbol, None)
    assert library.read(symbol).data is None


def test_delete_item_has_symbol(library):
    library.write(symbol, ts1)
    library.write(symbol, ts2, prune_previous_version=False)
    library.write(symbol, ts1, prune_previous_version=False)
    library.write(symbol, ts2, prune_previous_version=False)

    library.delete(symbol)
    for version in (1, 2, 3, 4, None):
        with pytest.raises(NoDataFoundException):
            library.read(symbol, version)

    # Has symbol returns false - this should really be has_data
    assert not library.has_symbol(symbol)
    assert symbol not in library.list_symbols()
    assert [x['version'] for x in library.list_versions(symbol)] == []


def test_delete_item_snapshot(library):
    library.write(symbol, ts1)
    library.write(symbol, ts2, prune_previous_version=False)
    library.write(symbol, ts1, prune_previous_version=False)
    library.snapshot('snap')
    library.write(symbol, ts2, prune_previous_version=False)

    library.delete(symbol)

    for version in (1, 2, 4, None):
        with pytest.raises(NoDataFoundException):
            library.read(symbol, version)

    # Can get the version out of the snapshots
    assert_frame_equal(library.read(symbol, 'snap').data, ts1)
    assert_frame_equal(library.read(symbol, 3).data, ts1)

    assert not library.has_symbol(symbol)
    assert not library.has_symbol(symbol, as_of=2)
    assert library.has_symbol(symbol, as_of=3)
    assert symbol in library.list_symbols(all_symbols=True)
    assert symbol in library.list_symbols(snapshot='snap')
    assert symbol not in library.list_symbols()
    assert sorted([x['version'] for x in library.list_versions(symbol)]) == [3, 5]

    # Should be able to create another snapshot
    library.snapshot('snap2')
    with pytest.raises(NoDataFoundException):
        library.read(symbol, 'snap2')
    assert_frame_equal(library.read(symbol, 'snap').data, ts1)
    assert symbol in library.list_symbols(snapshot='snap')
    assert symbol not in library.list_symbols(snapshot='snap2')


def test_has_symbol(library):
    assert not library.has_symbol(symbol)
    library.write(symbol, ts1)
    assert library.has_symbol(symbol)


def test_snapshot(library):
    library.write(symbol, ts1)
    library.snapshot('current')
    library.write(symbol, ts2)
    assert_frame_equal(library.read(symbol, as_of='current').data, ts1)
    assert_frame_equal(library.read(symbol).data, ts2)
    versions = library.list_versions(symbol)
    assert versions[0]['snapshots'] == []
    assert versions[1]['snapshots'] == ['current']

    library.snapshot('new')
    assert_frame_equal(library.read(symbol, as_of='current').data, ts1)
    assert_frame_equal(library.read(symbol, as_of='new').data, ts2)
    assert_frame_equal(library.read(symbol).data, ts2)
    versions = library.list_versions(symbol)
    assert versions[0]['snapshots'] == ['new']
    assert versions[1]['snapshots'] == ['current']

    # Replace the current version, and the snapshot shouldn't be deleted
    library.write(symbol, ts1, prune_previous_version=True)
    assert_frame_equal(library.read(symbol, as_of='current').data, ts1)
    assert_frame_equal(library.read(symbol, as_of='new').data, ts2)
    assert_frame_equal(library.read(symbol).data, ts1)
    versions = library.list_versions(symbol)
    assert versions[0]['snapshots'] == []
    assert versions[1]['snapshots'] == ['new']
    assert versions[2]['snapshots'] == ['current']


def test_snapshot_with_versions(library):
    """ Test snapshot of write versions consistency """
    library.write(symbol, ts1)
    library.write(symbol, ts2)

    # ensure snapshot of previous version is taken
    library.snapshot('previous', versions={symbol: 1})
    versions = library.list_versions(symbol)
    assert versions[0]['snapshots'] == []
    assert versions[1]['snapshots'] == ['previous']
    assert_frame_equal(library.read(symbol, as_of='previous').data, ts1)

    # ensure new snapshots are ordered after previous ones
    library.snapshot('new')
    versions = library.list_versions(symbol)
    assert versions[0]['snapshots'] == ['new']
    assert versions[0]['version'] == 2
    assert_frame_equal(library.read(symbol, as_of='new').data, ts2)

    assert versions[1]['snapshots'] == ['previous']
    assert versions[1]['version'] == 1
    assert_frame_equal(library.read(symbol, as_of='previous').data, ts1)

    # ensure snapshot of previous version doesn't overwrite current version
    library.write(symbol, ts1, prune_previous_version=True)
    library.snapshot('another', versions={symbol: 1})
    versions = library.list_versions(symbol)

    assert versions[0]['snapshots'] == []
    assert versions[0]['version'] == 3
    assert_frame_equal(library.read(symbol).data, ts1)

    assert versions[1]['snapshots'] == ['new']
    assert versions[1]['version'] == 2

    assert versions[2]['snapshots'] == ['previous', 'another']
    assert versions[2]['version'] == 1
    assert_frame_equal(library.read(symbol, as_of='another').data, ts1)


def test_snapshot_exclusion(library):
    library.write(symbol, ts1)
    library.snapshot('current', skip_symbols=[symbol])
    versions = list(library.list_versions(symbol))
    assert len(versions) == 1
    assert versions[0]['snapshots'] == []


def test_snapshot_delete(library):
    library.write(symbol, ts1)
    library.snapshot('current')
    library.write(symbol, ts2)

    # We have two versions of the symbol
    assert len(list(library.list_versions(symbol))) == 2
    library.delete_snapshot('current')
    # Data no longer referenced by snapshot
    with pytest.raises(NoDataFoundException):
        library.read(symbol, as_of='current')
    # But still accessible through the version
    assert_frame_equal(library.read(symbol, as_of=1).data, ts1)
    assert_frame_equal(library.read(symbol, as_of=2).data, ts2)

    # Snapshot again
    library.snapshot('current')
    library.write(symbol, ts1)
    assert_frame_equal(library.read(symbol, as_of='current').data, ts2)


def test_multiple_snapshots(library):
    library.write(symbol, ts1)
    library.snapshot('current')
    library.write(symbol, ts2)
    library.snapshot('current2')

    assert 'current' in library.list_snapshots()
    assert 'current2' in library.list_snapshots()

    assert_frame_equal(library.read(symbol).data, ts2)
    assert_frame_equal(library.read(symbol, as_of=1).data, ts1)
    assert_frame_equal(library.read(symbol, as_of=2).data, ts2)
    assert_frame_equal(library.read(symbol, as_of='current').data, ts1)
    assert_frame_equal(library.read(symbol, as_of='current2').data, ts2)

    library.delete_snapshot('current')
    assert_frame_equal(library.read(symbol, as_of='current2').data, ts2)
    library.delete_snapshot('current2')
    assert len(list(library.list_versions(symbol))) == 2


def test_delete_identical_snapshots(library):
    library.write(symbol, ts1)
    library.snapshot('current1')
    library.snapshot('current2')
    library.snapshot('current3')

    library.delete_snapshot('current3')
    assert_frame_equal(library.read(symbol, as_of='current2').data, ts1)
    library.delete_snapshot('current1')
    assert_frame_equal(library.read(symbol, as_of='current2').data, ts1)
    assert_frame_equal(library.read(symbol).data, ts1)


def test_list_snapshots(library):
    library.write(symbol, ts1)
    library.snapshot('current')
    library.snapshot('current2')

    assert 'current' in library.list_snapshots()
    assert 'current2' in library.list_snapshots()


def test_duplicate_snapshots(library):
    library.write(symbol, ts1)
    library.snapshot('current')
    with pytest.raises(DuplicateSnapshotException):
        library.snapshot('current')


def test_prunes_multiple_versions(library):
    coll = library._collection

    a = [{'a':'b'}]
    c = [{'c':'d'}]
    # Create an ObjectId
    now = dt.utcnow()
    with patch("bson.ObjectId", return_value=bson.ObjectId.from_datetime(now - dtd(minutes=125))):
        library.write(symbol, a, prune_previous_version=False)
    with patch("bson.ObjectId", return_value=bson.ObjectId.from_datetime(now - dtd(minutes=122))):
        library.write(symbol, c, prune_previous_version=False)
    with patch("bson.ObjectId", return_value=bson.ObjectId.from_datetime(now - dtd(minutes=121))):
        library.write(symbol, a, prune_previous_version=False)
    with patch("bson.ObjectId", return_value=bson.ObjectId.from_datetime(now - dtd(minutes=119))):
        library.write(symbol, c, prune_previous_version=False)
    assert coll.versions.count() == 4

    # Prunes all versions older than the most recent version that's older than 10 mins
    library.write(symbol, a, prune_previous_version=True)
    assert coll.versions.count() == 3
    assert library.read(symbol, as_of=3).data == a
    assert library.read(symbol, as_of=4).data == c
    assert library.read(symbol, as_of=5).data == a


def test_prunes_doesnt_prune_snapshots(library):
    coll = library._collection

    a = [{'a':'b'}]
    c = [{'c':'d'}]
    now = dt.utcnow()
    with patch("bson.ObjectId", return_value=bson.ObjectId.from_datetime(now - dtd(minutes=125))):
        library.write(symbol, a, prune_previous_version=False)
    with patch("bson.ObjectId", return_value=bson.ObjectId.from_datetime(now - dtd(minutes=122))):
        library.write(symbol, c, prune_previous_version=False)
    library.snapshot('snap')
    with patch("bson.ObjectId", return_value=bson.ObjectId.from_datetime(now - dtd(minutes=121))):
        library.write(symbol, a, prune_previous_version=False)
    with patch("bson.ObjectId", return_value=bson.ObjectId.from_datetime(now - dtd(minutes=119))):
        library.write(symbol, c, prune_previous_version=False)
    assert coll.versions.count() == 4

    # Prunes all versions older than the most recent version that's older than 10 mins
    library.write(symbol, a, prune_previous_version=True)
    assert coll.versions.count() == 4
    assert library.read(symbol, as_of='snap').data == c
    assert library.read(symbol, as_of=3).data == a
    assert library.read(symbol, as_of=4).data == c
    assert library.read(symbol, as_of=5).data == a

    # Remove the snapshot, the version should now be pruned
    library.delete_snapshot('snap')
    assert coll.versions.count() == 4
    library.write(symbol, c, prune_previous_version=True)
    assert coll.versions.count() == 4
    assert library.read(symbol, as_of=4).data == c
    assert library.read(symbol, as_of=5).data == a
    assert library.read(symbol, as_of=6).data == c


def test_prunes_multiple_versions_ts(library):
    coll = library._collection

    a = ts1
    c = ts2
    # Create an ObjectId
    now = dt.utcnow()
    with patch("bson.ObjectId", return_value=bson.ObjectId.from_datetime(now - dtd(minutes=125))):
        library.write(symbol, a, prune_previous_version=False)
    with patch("bson.ObjectId", return_value=bson.ObjectId.from_datetime(now - dtd(minutes=122))):
        library.write(symbol, c, prune_previous_version=False)
    with patch("bson.ObjectId", return_value=bson.ObjectId.from_datetime(now - dtd(minutes=121))):
        library.write(symbol, a, prune_previous_version=False)
    with patch("bson.ObjectId", return_value=bson.ObjectId.from_datetime(now - dtd(minutes=119))):
        library.write(symbol, c, prune_previous_version=False)
    assert coll.versions.count() == 4

    # Prunes all versions older than the most recent version that's older than 10 mins
    library.write(symbol, a, prune_previous_version=True)
    assert coll.versions.count() == 3
    assert_frame_equal(library.read(symbol, as_of=3).data, a)
    assert_frame_equal(library.read(symbol, as_of=4).data, c)
    assert_frame_equal(library.read(symbol, as_of=5).data, a)


def test_prunes_doesnt_prune_snapshots_ts(library):
    coll = library._collection

    a = ts1
    c = ts2
    now = dt.utcnow()
    with patch("bson.ObjectId", return_value=bson.ObjectId.from_datetime(now - dtd(minutes=125))):
        library.write(symbol, a, prune_previous_version=False)
    with patch("bson.ObjectId", return_value=bson.ObjectId.from_datetime(now - dtd(minutes=122))):
        library.write(symbol, c, prune_previous_version=False)
    library.snapshot('snap')
    with patch("bson.ObjectId", return_value=bson.ObjectId.from_datetime(now - dtd(minutes=121))):
        library.write(symbol, a, prune_previous_version=False)
    with patch("bson.ObjectId", return_value=bson.ObjectId.from_datetime(now - dtd(minutes=119))):
        library.write(symbol, c, prune_previous_version=False)
    assert coll.versions.count() == 4

    # Prunes all versions older than the most recent version that's older than 10 mins
    library.write(symbol, a, prune_previous_version=True)
    assert coll.versions.count() == 4
    assert_frame_equal(library.read(symbol, as_of='snap').data, c)
    assert_frame_equal(library.read(symbol, as_of=3).data, a)
    assert_frame_equal(library.read(symbol, as_of=4).data, c)
    assert_frame_equal(library.read(symbol, as_of=5).data, a)

    # Remove the snapshot, the version should now be pruned
    library.delete_snapshot('snap')
    assert coll.versions.count() == 4
    library.write(symbol, c, prune_previous_version=True)
    assert coll.versions.count() == 4
    assert_frame_equal(library.read(symbol, as_of=4).data, c)
    assert_frame_equal(library.read(symbol, as_of=5).data, a)
    assert_frame_equal(library.read(symbol, as_of=6).data, c)


def test_prunes_multiple_versions_fully_different_tss(library):
    coll = library._collection

    a = ts1
    b = ts2
    c = b.copy()
    c.index = [i + dtd(days=365) for i in c.index]
    c.index.name = b.index.name
    # Create an ObjectId
    now = dt.utcnow()
    with patch("bson.ObjectId", return_value=bson.ObjectId.from_datetime(now - dtd(minutes=125))):
        library.write(symbol, a, prune_previous_version=False)
    with patch("bson.ObjectId", return_value=bson.ObjectId.from_datetime(now - dtd(minutes=124))):
        library.write(symbol, b, prune_previous_version=False)
    with patch("bson.ObjectId", return_value=bson.ObjectId.from_datetime(now - dtd(minutes=122))):
        library.write(symbol, c, prune_previous_version=False)
    # a b and c versions above will be pruned a and b share months
    with patch("bson.ObjectId", return_value=bson.ObjectId.from_datetime(now - dtd(minutes=121))):
        library.write(symbol, c, prune_previous_version=False)
    with patch("bson.ObjectId", return_value=bson.ObjectId.from_datetime(now - dtd(minutes=119))):
        library.write(symbol, c, prune_previous_version=False)
    assert coll.versions.count() == 5

    # Prunes all versions older than the most recent version that's older than 10 mins
    library.write(symbol, c, prune_previous_version=True)
    assert_frame_equal(library.read(symbol, as_of=4).data, c)
    assert_frame_equal(library.read(symbol, as_of=5).data, c)
    assert_frame_equal(library.read(symbol, as_of=6).data, c)


def test_prunes_doesnt_prune_snapshots_fully_different_tss(library):
    coll = library._collection

    a = ts1
    b = ts2
    c = b.copy()
    c.index = [i + dtd(days=365) for i in c.index]
    c.index.name = b.index.name
    now = dt.utcnow()
    with patch("bson.ObjectId", return_value=bson.ObjectId.from_datetime(now - dtd(minutes=125))):
        library.write(symbol, a, prune_previous_version=False)
    with patch("bson.ObjectId", return_value=bson.ObjectId.from_datetime(now - dtd(minutes=123))):
        library.write(symbol, b, prune_previous_version=False)
    with patch("bson.ObjectId", return_value=bson.ObjectId.from_datetime(now - dtd(minutes=122))):
        library.write(symbol, c, prune_previous_version=False)
    library.snapshot('snap')
    with patch("bson.ObjectId", return_value=bson.ObjectId.from_datetime(now - dtd(minutes=121))):
        library.write(symbol, c, prune_previous_version=False)
    with patch("bson.ObjectId", return_value=bson.ObjectId.from_datetime(now - dtd(minutes=118))):
        library.write(symbol, c, prune_previous_version=False)
    with patch("bson.ObjectId", return_value=bson.ObjectId.from_datetime(now - dtd(minutes=119))):
        library.write(symbol, c, prune_previous_version=False)
    assert coll.versions.count() == 6

    # Prunes all versions older than the most recent version that's older than 10 mins
    library.write(symbol, c, prune_previous_version=True)
    assert coll.versions.count() == 5
    assert_frame_equal(library.read(symbol, as_of='snap').data, c)
    assert_frame_equal(library.read(symbol, as_of=4).data, c)
    assert_frame_equal(library.read(symbol, as_of=5).data, c)
    assert_frame_equal(library.read(symbol, as_of=6).data, c)
    assert_frame_equal(library.read(symbol, as_of=7).data, c)

    library.delete_snapshot('snap')
    assert coll.versions.count() == 5
    library.write(symbol, c, prune_previous_version=True)
    assert_frame_equal(library.read(symbol, as_of=4).data, c)
    assert_frame_equal(library.read(symbol, as_of=5).data, c)
    assert_frame_equal(library.read(symbol, as_of=6).data, c)
    assert_frame_equal(library.read(symbol, as_of=7).data, c)


def test_prunes_previous_version_append_interaction(library):
    ts = ts1
    ts2 = ts1.append(pd.DataFrame(index=[ts.index[-1] + dtd(days=1),
                                         ts.index[-1] + dtd(days=2), ],
                                  data=[3.7, 3.8],
                                  columns=['near']))
    ts2.index.name = ts1.index.name
    ts3 = ts.append(pd.DataFrame(index=[ts2.index[-1] + dtd(days=1),
                                        ts2.index[-1] + dtd(days=2)],
                                 data=[4.8, 4.9],
                                 columns=['near']))
    ts3.index.name = ts1.index.name
    ts4 = ts
    ts5 = ts2
    ts6 = ts3
    now = dt.utcnow()
    with patch("bson.ObjectId", return_value=bson.ObjectId.from_datetime(now - dtd(minutes=130)),
                                from_datetime=bson.ObjectId.from_datetime):
        library.write(symbol, ts, prune_previous_version=False)
    assert_frame_equal(ts, library.read(symbol).data)

    with patch("bson.ObjectId", return_value=bson.ObjectId.from_datetime(now - dtd(minutes=129)),
                                from_datetime=bson.ObjectId.from_datetime):
        library.write(symbol, ts2, prune_previous_version=False)
    assert_frame_equal(ts, library.read(symbol, as_of=1).data)
    assert_frame_equal(ts2, library.read(symbol).data)

    with patch("bson.ObjectId", return_value=bson.ObjectId.from_datetime(now - dtd(minutes=128)),
                                from_datetime=bson.ObjectId.from_datetime):
        library.write(symbol, ts3, prune_previous_version=False)
    assert_frame_equal(ts, library.read(symbol, as_of=1).data)
    assert_frame_equal(ts2, library.read(symbol, as_of=2).data)
    assert_frame_equal(ts3, library.read(symbol).data)

    with patch("bson.ObjectId", return_value=bson.ObjectId.from_datetime(now - dtd(minutes=127)),
                                from_datetime=bson.ObjectId.from_datetime):
        library.write(symbol, ts4, prune_previous_version=False)
    assert_frame_equal(ts, library.read(symbol, as_of=1).data)
    assert_frame_equal(ts2, library.read(symbol, as_of=2).data)
    assert_frame_equal(ts3, library.read(symbol, as_of=3).data)
    assert_frame_equal(ts4, library.read(symbol).data)

    with patch("bson.ObjectId", return_value=bson.ObjectId.from_datetime(now - dtd(minutes=126)),
                                from_datetime=bson.ObjectId.from_datetime):
        library.write(symbol, ts5, prune_previous_version=False)
    assert_frame_equal(ts, library.read(symbol, as_of=1).data)
    assert_frame_equal(ts2, library.read(symbol, as_of=2).data)
    assert_frame_equal(ts3, library.read(symbol, as_of=3).data)
    assert_frame_equal(ts4, library.read(symbol, as_of=4).data)
    assert_frame_equal(ts5, library.read(symbol).data)

    with patch("bson.ObjectId", return_value=bson.ObjectId.from_datetime(now),
                                from_datetime=bson.ObjectId.from_datetime):
        library.write(symbol, ts6, prune_previous_version=True)

    with pytest.raises(NoDataFoundException):
        library.read(symbol, as_of=1)
    with pytest.raises(NoDataFoundException):
        library.read(symbol, as_of=2)
    with pytest.raises(NoDataFoundException):
        library.read(symbol, as_of=3)
    assert_frame_equal(ts5, library.read(symbol, as_of=5).data)
    assert_frame_equal(ts6, library.read(symbol).data)


def test_list_symbols(library):
    library.snapshot('snap1')
    library.write('asdf', {'foo':'bar'}, metadata={'a':1, 'b':10})
    library.snapshot('snap2')
    assert 'asdf' in library.list_symbols()
    assert 'asdf' not in library.list_symbols(snapshot='snap1')
    assert 'asdf' in library.list_symbols(snapshot='snap2')
    assert 'asdf' in library.list_symbols(all_symbols=True)
    assert 'asdf' in library.list_symbols(a=1)
    assert library.list_symbols(a={'$gt': 5}) == []
    assert library.list_symbols(b={'$gt': 5}) == ['asdf']


def test_list_symbols_regex(library):
    library.snapshot('snap1')
    library.write('asdf', {'foo':'bar'}, metadata={'a':1, 'b':10})
    library.write('furble', {'foo':'bar'}, metadata={'a':1, 'b':10})
    library.snapshot('snap2')
    assert 'asdf' in library.list_symbols(regex='asd')
    assert 'furble' not in library.list_symbols(regex='asd')
    assert 'asdf' not in library.list_symbols(snapshot='snap1', regex='asd')
    assert 'asdf' in library.list_symbols(snapshot='snap2', regex='asd')
    assert 'furble' not in library.list_symbols(snapshot='snap2', regex='asd')
    assert 'asdf' in library.list_symbols(all_symbols=True, regex='asd')
    assert 'furble' not in library.list_symbols(all_symbols=True, regex='asd')
    assert 'asdf' in library.list_symbols(a=1, regex='asd')
    assert 'furble' not in library.list_symbols(a=1, regex='asd')
    assert library.list_symbols(a={'$gt': 5}, regex='asd') == []
    assert library.list_symbols(b={'$gt': 5}, regex='asd') == ['asdf']


def test_list_symbols_newer_version_with_lower_id(library):
    now = struct.pack(">i", int(time.time()))
    old_id = bson.ObjectId(now + b"\x00\x00\x00\x00\x00\x00\x00\x00")
    new_id = bson.ObjectId(now + b"\x00\x00\x00\x00\x00\x00\x00\x01")
    object_id_class = Mock()
    object_id_class.from_datetime = bson.ObjectId.from_datetime

    object_id_class.return_value = new_id
    with patch("bson.ObjectId", object_id_class):
        library.write(symbol, ts1)

    library.snapshot('s1')

    object_id_class.return_value = old_id
    with patch("bson.ObjectId", object_id_class):
        library.delete(symbol)

    assert symbol not in library.list_symbols()


def test_list_symbols_write_snapshot_write_delete(library):
    library.write('asdf', {'foo': 'bar'})
    symbol = 'sym_a'
    library.write(symbol, {'foo2': 'bar2'}, prune_previous_version=False)
    library.snapshot('s1')
    library.write(symbol, {'foo3': 'bar2'}, prune_previous_version=False)
    library.delete(symbol)
    # at this point we have one version retained from 's1' and
    # one more version added with delete (version with foo3 is pruned)
    # The list_symbols should return only 'asdf'
    assert library.list_symbols() == ['asdf']


def test_list_symbols_delete_write(library):
    symbol = 'sym_a'
    library.write(symbol, {'foo': 'bar2'}, prune_previous_version=False)
    library.delete(symbol)
    library.write(symbol, {'foo2': 'bar2'}, prune_previous_version=False)
    assert library.list_symbols() == [symbol]


def test_date_range_large(library):
    index = [dt(2017,1,1)]*20000 + [dt(2017,1,2)]*20000
    data = np.random.random((40000, 10))
    df = pd.DataFrame(index=index, data=data)
    df.index.name = 'index'
    df.columns = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
    library.write('test', df)
    r = library.read('test', date_range=DateRange(dt(2017,1,1), dt(2017,1,2)))
    assert_frame_equal(df, r.data)


def test_append_after_empty(library):
    len_df = 500
    index = [dt(2017, 1, 2)] * len_df
    data = np.random.random((len_df, 10))
    df = pd.DataFrame(index=index, data=data)
    df.index.name = 'index'
    df.columns = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
    library.write(symbol, df.iloc[:0])

    for i in range(len_df):
        library.append(symbol, df.iloc[i:i + 1])
    r = library.read(symbol)
    assert_frame_equal(df, r.data)


def _rnd_df(nrows, ncols):
    ret_df = pd.DataFrame(np.random.randn(nrows, ncols),
                          index=pd.date_range('20170101',
                          periods=nrows, freq='S'),
                          columns=[chr(i) for i in range(ord('a'), ord('a')+ncols)])
    ret_df.index.name = 'index'
    return ret_df


def test_write_metadata(library):
    symbol = 'FTL'
    mydf_a, mydf_b = _rnd_df(10, 5), _rnd_df(10, 5)
    with patch('arctic.arctic.logger.info') as info:
        library.write(symbol, data=mydf_a, metadata={'field_a': 1})  # creates version 1
        library.write(symbol, data=mydf_b, metadata={'field_a': 2})  # creates version 2
        library.write_metadata(symbol, metadata={'field_b': 1})  # creates version 3 (only metadata)
        v = library.read(symbol)
        assert_frame_equal(v.data, mydf_b)
        assert v.metadata == {'field_b': 1}
        assert library._read_metadata(symbol).get('version') == 3
        assert_frame_equal(library.read(symbol, as_of=1).data, mydf_a)


def test_write_metadata_followed_by_append(library):
    symbol = 'FTL'
    mydf_a, mydf_b = _rnd_df(10, 5), _rnd_df(10, 5)
    with patch('arctic.arctic.logger.info') as info:
        library.write(symbol, data=mydf_a, metadata={'field_a': 1})  # creates version 1
        library.write_metadata(symbol, metadata={'field_b': 1})  # creates version 2 (only metadata)
        library.append(symbol, data=mydf_b,metadata={'field_c': 1})  # creates version 3

        # Trigger GC now
        library._prune_previous_versions(symbol, 0)
        time.sleep(2)

        v = library.read(symbol)
        assert_frame_equal(v.data, mydf_a.append(mydf_b))
        assert v.metadata == {'field_c': 1}
        assert library._read_metadata(symbol).get('version') == 3
        assert_frame_equal(library.read(symbol, as_of=1).data, mydf_a)


def test_write_metadata_new_symbol(library):
    symbol = 'FTL'
    with patch('arctic.arctic.logger.info') as info:
        library.write_metadata(symbol, metadata={'field_b': 1})  # creates version 1 (only metadata)
        v = library.read(symbol)
        assert v.data == None
        assert v.metadata == {'field_b': 1}
        assert library._read_metadata(symbol).get('version') == 1


def test_write_metadata_after_append(library):
    symbol = 'FTL'
    mydf_a, mydf_b = _rnd_df(10, 5), _rnd_df(10, 5)
    with patch('arctic.arctic.logger.info') as info:
        library.write(symbol, data=mydf_a, metadata={'field_a': 1})  # creates version 1
        library.append(symbol, data=mydf_b, metadata={'field_a': 2})  # creates version 2
        library.write_metadata(symbol, metadata={'field_b': 1})  # creates version 3
        v = library.read(symbol)
        assert_frame_equal(v.data, mydf_a.append(mydf_b))
        assert v.metadata == {'field_b': 1}
        assert library._read_metadata(symbol).get('version') == 3


def test_write_metadata_purge_previous_versions(library):
    symbol = 'FTL'
    mydf_a, mydf_b, mydf_c = _rnd_df(10, 5), _rnd_df(10, 5), _rnd_df(10, 5)
    with patch('arctic.arctic.logger.info') as info:
        library.write(symbol, data=mydf_a, metadata={'field_a': 1})  # creates version 1
        library.write(symbol, data=mydf_b, metadata={'field_a': 2})  # creates version 2
        assert library._read_metadata(symbol).get('version') == 2
        library.write_metadata(symbol, metadata={'field_b': 1})  # creates version 3 (only metadata)

        # Trigger GC now
        library._prune_previous_versions(symbol, 0)
        time.sleep(2)

        # Assert the data
        v = library.read(symbol)
        assert_frame_equal(v.data, mydf_b)
        assert v.metadata == {'field_b': 1}

        # Check if after snapshot and deleting the symbol, the data/metadata survive
        library.snapshot('SNAP_1')
        library.delete(symbol)
        v = library.read(symbol, as_of='SNAP_1')
        assert_frame_equal(v.data, mydf_b)
        assert library._read_metadata(symbol, as_of='SNAP_1').get('version') == 3
        assert v.metadata == {'field_b': 1}


def test_write_metadata_delete_symbol(library):
    symbol = 'FTL'
    mydf_a = _rnd_df(10, 5)
    mydf_b = _rnd_df(10, 5)
    with patch('arctic.arctic.logger.info') as info:
        library.write(symbol, data=mydf_a, metadata={'field_a': 1})  # creates version 1
        library.write_metadata(symbol, metadata={'field_b': 1})  # creates version 2 (only metadata)

        library.delete(symbol)

        with pytest.raises(NoDataFoundException):
            library.read(symbol)

        library.write(symbol, data=mydf_b, metadata={'field_a': 1})  # creates version 1
        assert_frame_equal(library.read(symbol).data, mydf_b)


def test_write_metadata_snapshots(library):
    symbol = 'FTL'
    mydf_a, mydf_b = _rnd_df(10, 5), _rnd_df(10, 5)
    with patch('arctic.arctic.logger.info') as info:
        library.write(symbol, data=mydf_a, metadata={'field_a': 1})  # creates version 1
        library.snapshot('SNAP_1')
        library.write_metadata(symbol, metadata={'field_b': 1})  # creates version 2 (only metadata)
        library.snapshot('SNAP_2')
        library.write(symbol, data=mydf_b, metadata={'field_c': 1})  # creates version 3
        library.snapshot('SNAP_3')

        library._prune_previous_versions(symbol, keep_mins=0)

        v = library.read(symbol)
        assert_frame_equal(v.data, mydf_b)
        assert v.metadata == {'field_c': 1}

        v = library.read(symbol, as_of='SNAP_1')
        assert_frame_equal(v.data, mydf_a)
        assert v.metadata == {'field_a': 1}

        v = library.read(symbol, as_of='SNAP_2')
        assert_frame_equal(v.data, mydf_a)
        assert v.metadata == {'field_b': 1}


def test_restore_version(library):
    symbol = 'FTL'
    mydf_a = _rnd_df(10, 5)
    mydf_b = _rnd_df(10, 5)
    with patch('arctic.arctic.logger.info') as info:
        library.write(symbol, data=mydf_a, metadata={'field_a': 1})  # creates version 1
        library.write(symbol, data=mydf_b, metadata={'field_a': 2})  # creates version 2

        v = library.read(symbol)
        assert_frame_equal(v.data, mydf_b)
        assert v.metadata == {'field_a': 2}
        assert library._read_metadata(symbol).get('version') == 2

        library.restore_version(symbol, as_of=1)  # creates version 3

        #library._delete_version(symbol, 1)  # delete the original version to test further the robustness/dependency

        v = library.read(symbol)
        assert_frame_equal(v.data, mydf_a)
        assert v.metadata == {'field_a': 1}
        assert library._read_metadata(symbol).get('version') == 3


def test_restore_version_followed_by_append(library):
    symbol = 'FTL'
    mydf_a = _rnd_df(10, 5)
    mydf_b = _rnd_df(10, 5)
    mydf_c = _rnd_df(10, 5)
    with patch('arctic.arctic.logger.info') as info:
        library.write(symbol, data=mydf_a, metadata={'field_a': 1})  # creates version 1
        library.write(symbol, data=mydf_b, metadata={'field_b': 2})  # creates version 2
        library.restore_version(symbol, as_of=1)  # creates version 3
        library.append(symbol, data=mydf_c, metadata={'field_c': 3})  # creates version 4

        # Trigger GC now
        library._prune_previous_versions(symbol, 0)
        time.sleep(2)

        v = library.read(symbol)
        assert_frame_equal(v.data, mydf_a.append(mydf_c))
        assert v.metadata == {'field_c': 3}
        assert library._read_metadata(symbol).get('version') == 4


def test_restore_version_purging_previous_versions(library):
    symbol = 'FTL'
    mydf_a = _rnd_df(10, 5)
    mydf_b = _rnd_df(10, 5)
    with patch('arctic.arctic.logger.info') as info:
        library.write(symbol, data=mydf_a, metadata={'field_a': 1})  # creates version 1
        library.write(symbol, data=mydf_b, metadata={'field_a': 2})  # creates version 2

        library.restore_version(symbol, as_of=1)  # creates version 3

        # Trigger GC now
        library._prune_previous_versions(symbol, 0)
        time.sleep(2)

        # library._delete_version(symbol, 1)  # delete the original version to test further the robustness/dependency

        v = library.read(symbol)
        assert_frame_equal(v.data, mydf_a)
        assert v.metadata == {'field_a': 1}
        assert library._read_metadata(symbol).get('version') == 3


def test_restore_version_non_existent_version(library):
    symbol = 'FTL'
    mydf_a = _rnd_df(10, 5)
    with patch('arctic.arctic.logger.info') as info:
        library.write(symbol, data=mydf_a, metadata={'field_a': 1})  # creates version 1

        with pytest.raises(NoDataFoundException):
            library.restore_version(symbol, as_of=3)

        v = library.read(symbol)
        assert_frame_equal(v.data, mydf_a)
        assert v.metadata == {'field_a': 1}
        assert library._read_metadata(symbol).get('version') == 1


def test_restore_version_which_updated_only_metadata(library):
    symbol = 'FTL'
    mydf_a = _rnd_df(10, 5)
    mydf_b = _rnd_df(10, 5)
    with patch('arctic.arctic.logger.info') as info:
        library.write(symbol, data=mydf_a, metadata={'field_a': 1})  # creates version 1
        library.write_metadata(symbol, metadata={'field_b': 1})  # creates version 2
        library.write(symbol, data=mydf_b)  # creates version 3

        library.restore_version(symbol, as_of=2)  # creates version 4

        v = library.read(symbol)
        assert_frame_equal(v.data, mydf_a)
        assert v.metadata == {'field_b': 1}
        assert library._read_metadata(symbol).get('version') == 4


def test_restore_version_snapshot(library):
    symbol = 'FTL'
    mydf_a = _rnd_df(10, 5)
    mydf_b = _rnd_df(10, 5)
    with patch('arctic.arctic.logger.info') as info:
        library.write(symbol, data=mydf_a, metadata={'field_a': 1})  # creates version 1
        library.write_metadata(symbol, metadata={'field_b': 1})  # creates version 2
        library.restore_version(symbol, as_of=2)  # creates version 3
        library.snapshot('SNAP_1')
        library.write(symbol, data=mydf_b)  # creates version 3

        v = library.read(symbol, as_of='SNAP_1')
        assert_frame_equal(v.data, mydf_a)
        assert v.metadata == {'field_b': 1}
        assert library._read_metadata(symbol, as_of='SNAP_1').get('version') == 3


def test_prune_previous_versions_retries_on_cleanup_error(library):
    original_cleanup = _version_store_utils.cleanup
    def _cleanup(*args, **kwargs):
        if _cleanup.first_try:
            _cleanup.first_try = False
            raise OperationFailure(0)
        else:
            return original_cleanup(*args, **kwargs)
    _cleanup.first_try = True

    library.write(symbol, ts1)
    library.write(symbol, ts2)

    with patch("arctic.store.version_store.cleanup", side_effect=_cleanup) as cleanup:
        cleanup.__name__ = "cleanup"  # required by functools.wraps
        library._prune_previous_versions(symbol, keep_mins=0)

    assert len(list(library._arctic_lib.get_top_level_collection().find({'symbol': symbol}))) == 1


def test_prune_previous_versions_retries_find_calls(library):
    original_next = pymongo.cursor.Cursor.next

    callers = set()
    def _next(*args, **kwargs):
        vs_caller_name = next(c for c in inspect.stack() if c[1].endswith('arctic/store/version_store.py'))[3]
        if vs_caller_name not in callers:
            callers.add(vs_caller_name)
            raise OperationFailure(0)
        else:
            return original_next(*args, **kwargs)

    library.write(symbol, ts1, prune_previous_version=False)
    library.write(symbol, ts2, prune_previous_version=False)

    with patch.object(pymongo.cursor.Cursor, "next", autospec=True, side_effect=_next):
        library._prune_previous_versions(symbol, keep_mins=0)

    assert library._versions.count({'symbol': symbol}) == 1


def test_append_does_not_duplicate_data_when_prune_fails(library):
    side_effect = [OperationFailure(0), arctic.store.version_store.VersionStore._prune_previous_versions]
    new_data = read_str_as_pandas("""times | near
    2013-01-01 17:06:11.040 |  7.0
    2013-01-02 17:06:11.040 |  8.2
    2013-01-03 17:06:11.040 |  3.5
    2013-01-04 17:06:11.040 |  0.7""")
    library.write(symbol, ts1)

    with patch.object(arctic.store.version_store.VersionStore, "_prune_previous_versions", autospec=True, side_effect=side_effect):
        library.append(symbol, new_data)

    data = library.read(symbol).data
    assert len(set(data.index)) == len(data.index)


def test_append_does_not_duplicate_data_when_publish_fails(library):
    side_effect = [OperationFailure(0), arctic.store.version_store.VersionStore._publish_change]
    new_data = read_str_as_pandas("""times | near
    2013-01-01 17:06:11.040 |  7.0
    2013-01-02 17:06:11.040 |  8.2
    2013-01-03 17:06:11.040 |  3.5
    2013-01-04 17:06:11.040 |  0.7""")
    library.write(symbol, ts1)

    with patch.object(arctic.store.version_store.VersionStore, "_publish_change", autospec=True, side_effect=side_effect):
        library.append(symbol, new_data)

    data = library.read(symbol).data
    assert len(set(data.index)) == len(data.index)


def test_write_does_not_succeed_with_a_prune_error(library):
    # More than max retries OperationFailure would be more realistic, but ValueError is used for simplicity
    side_effect = [ValueError, arctic.store.version_store.VersionStore._prune_previous_versions]
    library.write(symbol, ts1)

    with patch.object(arctic.store.version_store.VersionStore, "_prune_previous_versions", autospec=True, side_effect=side_effect):
        with pytest.raises(ValueError):
            library.write(symbol, ts1)

    assert len(library.list_versions(symbol)) == 1


def test_write_does_not_succeed_with_a_publish_error(library):
    # More than max retries OperationFailure would be more realistic, but ValueError is used for simplicity
    side_effect = [ValueError, arctic.store.version_store.VersionStore._publish_change]

    with patch.object(arctic.store.version_store.VersionStore, "_publish_change", autospec=True, side_effect=side_effect):
        with pytest.raises(ValueError):
            library.append(symbol, ts1)

    assert not library.list_versions(symbol)


def test_prune_keeps_version(library):
    library.write(symbol, ts1)
    library.write(symbol, ts1)
    old_version = [v["_id"] for v in library._versions.find({"symbol": symbol}, sort=[("_id", 1)])][0]

    library._prune_previous_versions(symbol, keep_mins=0, keep_version=old_version)

    assert len(library.list_versions(symbol)) == 2


def test_empty_string_column_name(library):
    df = pd.DataFrame(data=[0, 1, 2], index=[0, 1, 2])
    df.columns = ['']

    with pytest.raises(ArcticException):
        library.write('df', df)
