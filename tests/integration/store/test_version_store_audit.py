from bson import ObjectId
from datetime import datetime as dt
from mock import patch
from pandas.util.testing import assert_frame_equal
from pymongo.errors import OperationFailure
import pytest

from arctic.store.audit import ArcticTransaction
from arctic.exceptions import ConcurrentModificationException, NoDataFoundException

from ...util import read_str_as_pandas


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

ts3 = read_str_as_pandas("""         times | near
                   2012-09-08 17:06:11.040 |  1.0
                   2012-10-08 17:06:11.040 |  4.0
                   2012-10-09 17:06:11.040 |  4.5
                   2012-10-10 17:06:11.040 |  5.0
                   2012-11-08 17:06:11.040 |  3.0
                   2012-11-09 17:06:11.040 |  44.0""")

ts1_append = read_str_as_pandas("""         times | near
                   2012-09-08 17:06:11.040 |  1.0
                   2012-10-08 17:06:11.040 |  2.0
                   2012-10-09 17:06:11.040 |  2.5
                   2012-11-08 17:06:11.040 |  3.0
                   2012-11-09 17:06:11.040 |  3.0""")

symbol = 'TS1'
symbol2 = 'TS2'
symbol3 = 'TS3'


def test_ArcticTransaction_can_do_first_writes(library):
    with ArcticTransaction(library, 'SYMBOL_NOT_HERE', 'user', 'log') as cwb:
        cwb.write('SYMBOL_NOT_HERE', ts1)
    wrote_vi = library.read('SYMBOL_NOT_HERE')
    assert_frame_equal(wrote_vi.data, ts1)


def test_ArcticTransaction_detects_concurrent_writes(library):
    library.write('FOO', ts1)

    from threading import Event, Thread
    e1 = Event()
    e2 = Event()

    def losing_writer():
        #will attempt to write version 2, should find that version 2 is there and it ends up writing version 3
        with pytest.raises(ConcurrentModificationException):
            with ArcticTransaction(library, 'FOO', 'user', 'log') as cwb:
                cwb.write('FOO', ts1_append, metadata={'foo': 'bar'})
                e1.wait()

    def winning_writer():
        #will attempt to write version 2 as well
        with ArcticTransaction(library, 'FOO', 'user', 'log') as cwb:
            cwb.write('FOO', ts2, metadata={'foo': 'bar'})
            e2.wait()

    t1 = Thread(target=losing_writer)
    t2 = Thread(target=winning_writer)
    t1.start()
    t2.start()

    # both read the same timeseries and are locked doing some 'work'
    e2.set()
    # t2  should now be able to finish
    t2.join()
    e1.set()
    t1.join()

    # we're expecting the losing_writer to undo its write once it realises that it wrote v3 instead of v2
    wrote_vi = library.read('FOO')
    assert_frame_equal(wrote_vi.data, ts2)
    assert {'foo': 'bar'} == wrote_vi.metadata


def test_audit_writes(library):
    with ArcticTransaction(library, symbol, 'u1', 'l1') as mt:
        mt.write(symbol, ts1)

    with ArcticTransaction(library, symbol, 'u2', 'l2') as mt:
        mt.write(symbol, ts2)

    audit_log = library.read_audit_log(symbol)
    assert audit_log == [{u'new_v': 2, u'symbol': u'TS1', u'message': u'l2', u'user': u'u2', u'orig_v': 1},
                         {u'new_v': 1, u'symbol': u'TS1', u'message': u'l1', u'user': u'u1', u'orig_v': 0}]
    assert_frame_equal(ts1, library.read(symbol, audit_log[0]['orig_v']).data)
    assert_frame_equal(ts2, library.read(symbol, audit_log[0]['new_v']).data)


def test_metadata_changes_writes(library):
    with ArcticTransaction(library, symbol, 'u1', 'l1') as mt:
        mt.write(symbol, ts1, metadata={'original': 'data'})

    with ArcticTransaction(library, symbol, 'u2', 'l2') as mt:
        mt.write(symbol, ts1, metadata={'some': 'data', 'original': 'data'})

    audit_log = library.read_audit_log(symbol)
    assert audit_log == [{u'new_v': 2, u'symbol': u'TS1', u'message': u'l2', u'user': u'u2', u'orig_v': 1},
                         {u'new_v': 1, u'symbol': u'TS1', u'message': u'l1', u'user': u'u1', u'orig_v': 0}]
    assert_frame_equal(ts1, library.read(symbol, audit_log[0]['orig_v']).data)
    assert_frame_equal(ts1, library.read(symbol, audit_log[0]['new_v']).data)

    assert library.read(symbol, audit_log[0]['orig_v']).metadata == {'original': 'data'}
    assert library.read(symbol, audit_log[0]['new_v']).metadata == {'some': 'data', 'original': 'data'}



def test_audit_read(library):
    with ArcticTransaction(library, symbol3, 'u3', 'foo') as mt:
        mt.write(symbol3, ts1)

    with ArcticTransaction(library, symbol, 'u1', 'l1') as mt:
        mt.write(symbol, ts1)

    with ArcticTransaction(library, symbol, 'u2', 'l2') as mt:
        mt.write(symbol, ts2)

    with ArcticTransaction(library, symbol2, 'u2', 'l2') as mt:
        mt.write(symbol2, ts2)
        
    audit_log = library.read_audit_log()

    assert audit_log == [{u'new_v': 1, u'symbol': u'TS2', u'message': u'l2', u'user': u'u2', u'orig_v': 0},
                         {u'new_v': 2, u'symbol': u'TS1', u'message': u'l2', u'user': u'u2', u'orig_v': 1},
                         {u'new_v': 1, u'symbol': u'TS1', u'message': u'l1', u'user': u'u1', u'orig_v': 0},
                         {u'new_v': 1, u'symbol': u'TS3', u'message': u'foo', u'user': u'u3', u'orig_v': 0},
                         ]

    l2_audit_log = library.read_audit_log(message='l2')

    assert l2_audit_log == [{u'new_v': 1, u'symbol': u'TS2', u'message': u'l2', u'user': u'u2', u'orig_v': 0},
                         {u'new_v': 2, u'symbol': u'TS1', u'message': u'l2', u'user': u'u2', u'orig_v': 1},
                         ]

    symbol_audit_log = library.read_audit_log(symbol=symbol)

    assert symbol_audit_log == [{u'new_v': 2, u'symbol': u'TS1', u'message': u'l2', u'user': u'u2', u'orig_v': 1},
                         {u'new_v': 1, u'symbol': u'TS1', u'message': u'l1', u'user': u'u1', u'orig_v': 0}]


    symbols_audit_log = library.read_audit_log(symbol=[symbol, symbol2])

    assert symbols_audit_log == [{u'new_v': 1, u'symbol': u'TS2', u'message': u'l2', u'user': u'u2', u'orig_v': 0},
                                {u'new_v': 2, u'symbol': u'TS1', u'message': u'l2', u'user': u'u2', u'orig_v': 1},
                         {u'new_v': 1, u'symbol': u'TS1', u'message': u'l1', u'user': u'u1', u'orig_v': 0}]


    symbol_message_audit_log = library.read_audit_log(symbol=symbol, message='l2')

    assert symbol_message_audit_log == [{u'new_v': 2, u'symbol': u'TS1', u'message': u'l2', u'user': u'u2', u'orig_v': 1}, ]



def test_cleanup_orphaned_versions_integration(library):
    _id = ObjectId.from_datetime(dt(2013, 1, 1))
    with patch('bson.ObjectId', return_value=_id):
        with ArcticTransaction(library, symbol, 'u1', 'l1') as mt:
            mt.write(symbol, ts1)
    assert library._versions.find({'parent': {'$size': 1}}).count() == 1
    library._cleanup_orphaned_versions(False)
    assert library._versions.find({'parent': {'$size': 1}}).count() == 1


def test_corrupted_read_writes_new(library):
    with ArcticTransaction(library, symbol, 'u1', 'l1') as mt:
        mt.write(symbol, ts1)

    res = library.read(symbol)
    assert res.version == 1

    with ArcticTransaction(library, symbol, 'u1', 'l2') as mt:
        mt.write(symbol, ts2)

    res = library.read(symbol)
    assert res.version == 2

    with patch.object(library, 'read') as l:
        l.side_effect = OperationFailure('some failure')
        with ArcticTransaction(library, symbol, 'u1', 'l2') as mt:
            mt.write(symbol, ts3, metadata={'a': 1, 'b': 2})

    res = library.read(symbol)
    # Corrupted data still increments on write to next version correctly with new data
    assert res.version == 3
    assert_frame_equal(ts3, library.read(symbol, 3).data)
    assert res.metadata == {'a': 1, 'b': 2}

    with patch.object(library, 'read') as l:
        l.side_effect = OperationFailure('some failure')
        with ArcticTransaction(library, symbol, 'u1', 'l2') as mt:
            mt.write(symbol, ts3, metadata={'a': 1, 'b': 2})

    res = library.read(symbol)
    # Corrupted data still increments to next version correctly with ts & metadata unchanged
    assert res.version == 4
    assert_frame_equal(ts3, library.read(symbol, 4).data)
    assert res.metadata == {'a': 1, 'b': 2}


def test_write_after_delete(library):
    with ArcticTransaction(library, symbol, 'u1', 'l') as mt:
        mt.write(symbol, ts1)
    library.delete(symbol)

    with ArcticTransaction(library, symbol, 'u1', 'l') as mt:
        mt.write(symbol, ts1_append)
    assert_frame_equal(library.read(symbol).data, ts1_append)


def test_ArcticTransaction_write_skips_for_exact_match(library):
    ts = read_str_as_pandas("""times |    PX_LAST
             2014-10-31 21:30:00.000 | 204324.674
             2014-11-13 21:30:00.000 |  193964.45
             2014-11-14 21:30:00.000 | 193650.403""")

    with ArcticTransaction(library, symbol, 'u1', 'l1') as mt:
        mt.write(symbol, ts)

    version = library.read(symbol).version

    # try and store same TimeSeries again
    with ArcticTransaction(library, symbol, 'u1', 'l2') as mt:
        mt.write(symbol, ts)

    assert library.read(symbol).version == version


def test_ArcticTransaction_write_doesnt_skip_for_close_ts(library):
    orig_ts = read_str_as_pandas("""times |    PX_LAST
                  2014-10-31 21:30:00.000 | 204324.674
                  2014-11-13 21:30:00.000 |  193964.45
                  2014-11-14 21:30:00.000 | 193650.403""")

    with ArcticTransaction(library, symbol, 'u1', 'l1') as mt:
        mt.write(symbol, orig_ts)

    assert_frame_equal(library.read(symbol).data, orig_ts)

    # try and store slighty different TimeSeries
    new_ts = read_str_as_pandas("""times |    PX_LAST
                 2014-10-31 21:30:00.000 | 204324.672
                 2014-11-13 21:30:00.000 | 193964.453
                 2014-11-14 21:30:00.000 | 193650.406""")

    with ArcticTransaction(library, symbol, 'u1', 'l2') as mt:
        mt.write(symbol, new_ts)

    assert_frame_equal(library.read(symbol).data, new_ts)
