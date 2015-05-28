import bson
from datetime import datetime as dt, timedelta as dtd
import itertools
from mock import patch, sentinel
import pytest

from arctic.scripts.arctic_fsck import main

from ...util import run_as_main, read_str_as_pandas


@pytest.fixture(scope='function')
def library_name():
    return 'user.library'


ts = read_str_as_pandas("""         times | near
                   2012-09-08 17:06:11.040 |  1.0
                   2012-10-08 17:06:11.040 |  2.0
                   2012-10-09 17:06:11.040 |  2.5
                   2012-11-08 17:06:11.040 |  3.0""")

some_object = {'thing': sentinel.val}


@pytest.mark.parametrize(['dry_run', 'data'], [(x, y) for (x, y) in itertools.product([True, False],
                                                                                      [some_object, ts])])
def test_cleanup_orphaned_chunks(mongo_host, library, data, dry_run):
    """
    Check that we do / don't cleanup chunks based on the dry-run
    """
    yesterday = dt.utcnow() - dtd(days=1, seconds=1)
    _id = bson.ObjectId.from_datetime(yesterday)
    with patch("bson.ObjectId", return_value=_id):
        library.write('symbol', data, prune_previous_version=False)

    # Number of chunks
    chunk_count = library._collection.count()
    # Remove the version document ; should cleanup
    library._collection.versions.delete_one({'_id': _id})

    # No cleanup on dry-run
    if dry_run:
        run_as_main(main, '--library', 'user.library', '--host', mongo_host)
        assert library._collection.count() == chunk_count
    else:
        run_as_main(main, '--library', 'user.library', '--host', mongo_host, '-f')
        assert library._collection.count() == 0


@pytest.mark.parametrize(['dry_run', 'data'], [(x, y) for (x, y) in itertools.product([True, False],
                                                                                      [some_object, ts])])
def test_cleanup_noop(mongo_host, library, data, dry_run):
    """
    Check that we do / don't cleanup chunks based on the dry-run
    """
    yesterday = dt.utcnow() - dtd(days=1, seconds=1)
    _id = bson.ObjectId.from_datetime(yesterday)
    with patch("bson.ObjectId", return_value=_id):
        library.write('symbol', data, prune_previous_version=False)

    # Number of chunks
    chunk_count = library._collection.count()

    # No cleanup on dry-run
    if dry_run:
        run_as_main(main, '--library', 'user.library', '--host', mongo_host)
        assert library._collection.count() == chunk_count
        assert repr(library.read('symbol').data) == repr(data)
    else:
        run_as_main(main, '--library', 'user.library', '--host', mongo_host, '-f')
        assert library._collection.count() == chunk_count
        assert repr(library.read('symbol').data) == repr(data)


@pytest.mark.parametrize(['dry_run', 'data'], [(x, y) for (x, y) in itertools.product([True, False],
                                                                                      [some_object, ts])])
def test_cleanup_orphaned_chunks_ignores_recent(mongo_host, library, data, dry_run):
    """
    We don't cleanup any chunks in the range of today.  That's just asking for trouble
    """
    yesterday = dt.utcnow() - dtd(hours=12)
    _id = bson.ObjectId.from_datetime(yesterday)
    with patch("bson.ObjectId", return_value=_id):
        library.write('symbol', data, prune_previous_version=False)
    chunk_count = library._collection.count()
    library._collection.versions.delete_one({'_id': _id})

    if dry_run:
        run_as_main(main, '--library', 'user.library', '--host', mongo_host)
        assert library._collection.count() == chunk_count
    else:
        run_as_main(main, '--library', 'user.library', '--host', mongo_host, '-f')
        assert library._collection.count() == chunk_count


@pytest.mark.parametrize('data', [some_object, ts])
def test_cleanup_orphaned_chunk_doesnt_break_versions(mongo_host, library, data):
    """
    Check that a chunk pointed to by more than one version, aren't inadvertently cleared
    """
    yesterday = dt.utcnow() - dtd(days=1, seconds=1)
    _id = bson.ObjectId.from_datetime(yesterday)
    with patch("bson.ObjectId", return_value=_id):
        library.write('symbol', data, prune_previous_version=False)

    # Re-Write the data again
    # Write a whole new version rather than going down the append path...
    #     - we want two self-standing versions, the removal of one shouldn't break the other... 
    with patch('arctic.store._ndarray_store._APPEND_COUNT', 0):
        library.write('symbol', data, prune_previous_version=False)
    library._delete_version('symbol', 1)
    library._collection.versions.delete_one({'_id': _id})
    assert repr(library.read('symbol').data) == repr(data)

    run_as_main(main, '--library', 'user.library', '--host', mongo_host, '-f')
    assert repr(library.read('symbol').data) == repr(data)
    library.delete('symbol')
    assert library._collection.versions.count() == 0


@pytest.mark.parametrize(['dry_run', 'data'], [(x, y) for (x, y) in itertools.product([True, False],
                                                                                      [some_object, ts])])
def test_cleanup_orphaned_snapshots(mongo_host, library, data, dry_run):
    """
    Check that we do / don't cleanup chunks based on the dry-run
    """
    yesterday = dt.utcnow() - dtd(days=1, seconds=1)
    _id = bson.ObjectId.from_datetime(yesterday)
    library.write('symbol', data, prune_previous_version=False)
    with patch("bson.ObjectId", return_value=_id):
        library.snapshot('snap_name')

    # Remove the version document ; should cleanup
    assert library._collection.snapshots.delete_one({})

    # No cleanup on dry-run
    if dry_run:
        run_as_main(main, '--library', 'user.library', '--host', mongo_host)
        assert library._collection.count() > 0
        assert library._collection.versions.count()
        assert repr(library.read('symbol').data) == repr(data)
        # Nothing done_APPEND_COUNT
        assert len(library._collection.versions.find_one({})['parent'])
    else:
        run_as_main(main, '--library', 'user.library', '--host', mongo_host, '-f')
        assert library._collection.count() > 0
        assert library._collection.versions.count()
        # Data still available (write with prune_previous_version will do the cleanup)
        assert repr(library.read('symbol').data) == repr(data)
        # Snapshot cleaned up
        assert not len(library._collection.versions.find_one({})['parent'])


@pytest.mark.parametrize(['dry_run', 'data'], [(x, y) for (x, y) in itertools.product([True, False],
                                                                                      [some_object, ts])])
def test_cleanup_orphaned_snapshots_nop(mongo_host, library, data, dry_run):
    """
    Check that we do / don't cleanup chunks based on the dry-run
    """
    yesterday = dt.utcnow() - dtd(days=1, seconds=1)
    _id = bson.ObjectId.from_datetime(yesterday)
    library.write('symbol', data, prune_previous_version=False)
    with patch("bson.ObjectId", return_value=_id):
        library.snapshot('snap_name')

    # No cleanup on dry-run
    if dry_run:
        run_as_main(main, '--library', 'user.library', '--host', mongo_host)
        assert library._collection.count() > 0
        assert library._collection.versions.count()
        assert repr(library.read('symbol').data) == repr(data)
        # Nothing done
        assert len(library._collection.versions.find_one({})['parent'])
    else:
        run_as_main(main, '--library', 'user.library', '--host', mongo_host, '-f')
        assert library._collection.count() > 0
        assert library._collection.versions.count()
        # Data still available (write with prune_previous_version will do the cleanup)
        assert repr(library.read('symbol').data) == repr(data)
        # Nothing done
        assert len(library._collection.versions.find_one({})['parent'])


@pytest.mark.parametrize(['dry_run', 'data'], [(x, y) for (x, y) in itertools.product([True, False],
                                                                                      [some_object, ts])])
def test_dont_cleanup_recent_orphaned_snapshots(mongo_host, library, data, dry_run):
    """
    Check that we do / don't cleanup chunks based on the dry-run
    """
    today = dt.utcnow() - dtd(hours=12, seconds=1)
    _id = bson.ObjectId.from_datetime(today)
    library.write('symbol', data, prune_previous_version=False)
    with patch("bson.ObjectId", return_value=_id):
        library.snapshot('snap_name')

    # Remove the version document ; should cleanup
    assert library._collection.snapshots.delete_many({})

    # No cleanup on dry-run
    if dry_run:
        run_as_main(main, '--library', 'user.library', '--host', mongo_host)
        assert library._collection.count() > 0
        assert library._collection.versions.count()
        assert repr(library.read('symbol').data) == repr(data)
        # Nothing done
        assert len(library._collection.versions.find_one({})['parent'])
    else:
        run_as_main(main, '--library', 'user.library', '--host', mongo_host, '-f')
        assert library._collection.count() > 0
        assert library._collection.versions.count()
        # Data still available (write with prune_previous_version will do the cleanup)
        assert repr(library.read('symbol').data) == repr(data)
        # Snapshot cleaned up
        assert len(library._collection.versions.find_one({})['parent'])
