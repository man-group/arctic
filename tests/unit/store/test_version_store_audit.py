from mock import create_autospec, Mock, sentinel, ANY, call
from pymongo.errors import OperationFailure
import pytest
import pandas as pd

from arctic.store.audit import ArcticTransaction
from arctic.store.version_store import VersionedItem, VersionStore
from arctic.exceptions import ConcurrentModificationException, NoDataFoundException


def test_ConcurrentWriteBlock_simple():
    vs = create_autospec(VersionStore, _collection=Mock())
    ts1 = pd.DataFrame(index=[1, 2], data={'a':[1.0, 2.0]})
    vs.read.return_value = VersionedItem(symbol=sentinel.symbol, library=sentinel.library, version=1, metadata=None, data=ts1)
    vs.write.return_value = VersionedItem(symbol=sentinel.symbol, library=sentinel.library, version=2,
                            metadata=None, data=None)
    vs.list_versions.return_value = [{'version': 2}, {'version': 1}]

    with ArcticTransaction(vs, sentinel.symbol, sentinel.user, sentinel.log) as cwb:
        cwb.write(sentinel.symbol, pd.DataFrame(index=[3, 4], data={'a': [1.0, 2.0]}), metadata=sentinel.meta)

    assert not vs._delete_version.called
    vs.write.assert_called_once_with(sentinel.symbol, ANY, prune_previous_version=True, metadata=sentinel.meta)
    vs.list_versions.assert_called_once_with(sentinel.symbol)


def test_ConcurrentWriteBlock_writes_if_metadata_changed():
    vs = create_autospec(VersionStore, _collection=Mock())
    ts1 = pd.DataFrame(index=[1, 2], data={'a':[1.0, 2.0]})
    vs.read.return_value = VersionedItem(symbol=sentinel.symbol, library=sentinel.library, version=1, metadata=None, data=ts1)
    vs.write.return_value = VersionedItem(symbol=sentinel.symbol, library=sentinel.library, version=2, metadata=None, data=None)
    vs.list_versions.return_value = [{'version': 2},
                                    {'version': 1}]

    with ArcticTransaction(vs, sentinel.symbol, sentinel.user, sentinel.log) as cwb:
        assert cwb._do_write is False
        cwb.write(sentinel.symbol, ts1, metadata={1: 2})
        assert cwb._do_write is True

    assert not vs._delete_version.called
    vs.write.assert_called_once_with(sentinel.symbol, ANY, prune_previous_version=True, metadata={1: 2})
    vs.list_versions.assert_called_once_with(sentinel.symbol)

    # Won't write on exit with same data and metadata
    vs.read.return_value = VersionedItem(symbol=sentinel.symbol, library=sentinel.library, version=2, metadata={1: 2}, data=ts1)
    with ArcticTransaction(vs, sentinel.symbol, sentinel.user, sentinel.log) as cwb:
        assert cwb._do_write is False
        cwb.write(sentinel.symbol, ts1, metadata={1: 2})
        assert cwb._do_write is False


def test_ConcurrentWriteBlock_writes_if_base_data_corrupted():

    vs = create_autospec(VersionStore, _collection=Mock())
    ts1 = pd.DataFrame(index=[1, 2], data={'a':[1.0, 2.0]})
    vs.read.side_effect = OperationFailure('some failure')
    vs.write.return_value = VersionedItem(symbol=sentinel.symbol, library=sentinel.library, version=2,
                            metadata=None, data=None)
    vs.read_metadata.return_value = VersionedItem(symbol=sentinel.symbol, library=sentinel.library, version=1,
                            metadata=None, data=None)
    vs.list_versions.return_value = [{'version': 2}, {'version': 1}]

    with ArcticTransaction(vs, sentinel.symbol, sentinel.user, sentinel.log) as cwb:
        cwb.write(sentinel.symbol, ts1, metadata={1: 2})

    vs.write.assert_called_once_with(sentinel.symbol, ANY, prune_previous_version=True, metadata={1: 2})
    assert vs.list_versions.call_args_list == [call(sentinel.symbol)]


def test_ConcurrentWriteBlock_writes_no_data_found():
    vs = create_autospec(VersionStore, _collection=Mock())
    ts1 = pd.DataFrame(index=[1, 2], data={'a':[1.0, 2.0]})
    vs.read.side_effect = NoDataFoundException('no data')
    vs.write.return_value = VersionedItem(symbol=sentinel.symbol, library=sentinel.library, version=1,
                            metadata=None, data=None)
    vs.list_versions.side_effect = [[],
                                   [{'version': 1}],
                                   ]

    with ArcticTransaction(vs, sentinel.symbol, sentinel.user, sentinel.log) as cwb:
        cwb.write(sentinel.symbol, ts1, metadata={1: 2})

    assert vs.write.call_args_list == [call(sentinel.symbol, ANY, prune_previous_version=True, metadata={1: 2})]
    assert vs.list_versions.call_args_list == [call(sentinel.symbol, latest_only=True),
                                              call(sentinel.symbol)]


def test_ConcurrentWriteBlock_writes_no_data_found_deleted():
    vs = create_autospec(VersionStore, _collection=Mock())
    ts1 = pd.DataFrame(index=[1, 2], data={'a':[1.0, 2.0]})
    vs.read.side_effect = NoDataFoundException('no data')
    vs.write.return_value = VersionedItem(symbol=sentinel.symbol, library=sentinel.library, version=3,
                            metadata=None, data=None)
    vs.list_versions.side_effect = [[{'version': 2}, {'version': 1}],
                                   [{'version': 3}, {'version': 2}],
                                   ]

    with ArcticTransaction(vs, sentinel.symbol, sentinel.user, sentinel.log) as cwb:
        cwb.write(sentinel.symbol, ts1, metadata={1: 2})

    assert vs.write.call_args_list == [call(sentinel.symbol, ANY, prune_previous_version=True, metadata={1: 2})]
    assert vs.list_versions.call_args_list == [call(sentinel.symbol, latest_only=True),
                                              call(sentinel.symbol)]


def test_ConcurrentWriteBlock_does_nothing_when_data_not_modified():
    vs = create_autospec(VersionStore, _collection=Mock())
    ts1 = pd.DataFrame(index=[1, 2], data={'a':[1.0, 2.0]})
    vs.read.return_value = VersionedItem(symbol=sentinel.symbol, library=sentinel.library, version=1, metadata=None, data=ts1)
    vs.write.return_value = VersionedItem(symbol=sentinel.symbol, library=sentinel.library, version=2, metadata=None, data=None)
    vs.list_versions.side_effect = [{'version': 2}, {'version': 1}]

    with ArcticTransaction(vs, sentinel.symbol, sentinel.user, sentinel.log) as cwb:
        cwb.write(sentinel.symbol, pd.DataFrame(index=[1, 2], data={'a':[1.0, 2.0]}))

    assert not vs._delete_version.called
    assert not vs.write.called


def test_ConcurrentWriteBlock_does_nothing_when_data_is_None():
    vs = create_autospec(VersionStore, _collection=Mock())
    ts1 = pd.DataFrame(index=[1, 2], data={'a':[1.0, 2.0]})
    vs.read.return_value = VersionedItem(symbol=sentinel.symbol, library=sentinel.library, version=1, metadata=None, data=ts1)
    vs.write.return_value = VersionedItem(symbol=sentinel.symbol, library=sentinel.library, version=2,
                            metadata=None, data=None)
    vs.list_versions.return_value = [{'version': 1}, {'version': 2}]

    with ArcticTransaction(vs, sentinel.symbol, sentinel.user, sentinel.log) as cwb:
        pass
    assert not vs._delete_version.called
    assert not vs.write.called


def test_ConcurrentWriteBlock_guards_against_inconsistent_ts():
    vs = create_autospec(VersionStore, _collection=Mock())
    ts1 = pd.DataFrame(index=[1, 2], data={'a':[1.0, 2.0]})
    vs.read.return_value = VersionedItem(symbol=sentinel.symbol, library=sentinel.library, version=1, metadata=None, data=ts1)
    vs.write.return_value = VersionedItem(symbol=sentinel.symbol, library=sentinel.library, version=2, metadata=None, data=None)
    vs.list_versions.side_effect = [{'version': 2}, {'version': 1}]

    ts1 = pd.DataFrame(index=[1, 2], data={'a': [2.0, 3.0]})
    with pytest.raises(ConcurrentModificationException):
        with ArcticTransaction(vs, sentinel.symbol, sentinel.user, sentinel.log, modify_timeseries=ts1) as cwb:
            pass


def test_ConcurrentWriteBlock_detects_concurrent_writes():
    vs = create_autospec(VersionStore, _collection=Mock())
    ts1 = pd.DataFrame(index=[1, 2], data={'a':[1.0, 2.0]})
    vs.read.return_value = VersionedItem(symbol=sentinel.symbol, library=sentinel.library, version=1, metadata=None, data=ts1)
    vs.write.side_effect = [VersionedItem(symbol=sentinel.symbol, library=sentinel.library, version=2, metadata=None, data=None),
                            VersionedItem(symbol=sentinel.symbol, library=sentinel.library, version=3, metadata=None, data=None)]
    #note that we return some extra version 5, it is possible that we have a write coming in after our own write that gets picked up 
    vs.list_versions.side_effect = [[{'version': 5}, {'version': 2}, {'version': 1}, ],
                                   [{'version': 5}, {'version': 3}, {'version': 2}, {'version': 1}, ]]
    from threading import Event, Thread
    e1 = Event()
    e2 = Event()

    def losing_writer():
        #will attempt to write version 2, should find that version 2 is there and it ends up writing version 3
        with pytest.raises(ArcticTransaction):
            with ArcticTransaction(vs, sentinel.symbol, sentinel.user, sentinel.log) as cwb:
                cwb.write(sentinel.symbol, pd.DataFrame([1.0, 2.0], [3, 4]))
                e1.wait()

    def winning_writer():
        #will attempt to write version 2 as well
        with ArcticTransaction(vs, sentinel.symbol, sentinel.user, sentinel.log) as cwb:
            cwb.write(sentinel.symbol, pd.DataFrame([1.0, 2.0], [5, 6]))
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
    vs._delete_version.assert_called_once_with(sentinel.symbol, 3)
