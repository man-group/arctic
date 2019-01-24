import itertools
from datetime import datetime as dt, timedelta as dtd

import bson
import pytest
from mock import patch, sentinel

from arctic._util import mongo_count, FwPointersCfg
from arctic.scripts.arctic_fsck import main
from tests.integration.store.test_version_store import FwPointersCtx
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


@pytest.mark.parametrize(
    ['dry_run', 'data', 'fw_pointers_config'],
    [(x, y, z) for (x, y, z) in itertools.product(
        [True, False], [some_object, ts], [FwPointersCfg.DISABLED, FwPointersCfg.HYBRID, FwPointersCfg.ENABLED])])
def test_cleanup_orphaned_chunks(mongo_host, library, data, dry_run, fw_pointers_config):
    """
    Check that we do / don't cleanup chunks based on the dry-run
    """
    with FwPointersCtx(fw_pointers_config):
        yesterday = dt.utcnow() - dtd(days=1, seconds=1)
        _id = bson.ObjectId.from_datetime(yesterday)
        with patch("bson.ObjectId", return_value=_id):
            library.write('symbol', data, prune_previous_version=False)

        # Number of chunks
        chunk_count = mongo_count(library._collection)
        # Remove the version document ; should cleanup
        library._collection.versions.delete_one({'_id': _id})

        # No cleanup on dry-run
        if dry_run:
            run_as_main(main, '--library', 'user.library', '--host', mongo_host)
            assert mongo_count(library._collection) == chunk_count
        else:
            run_as_main(main, '--library', 'user.library', '--host', mongo_host, '-f')
            assert mongo_count(library._collection) == 0


@pytest.mark.parametrize(
    ['dry_run', 'data', 'fw_pointers_config'],
    [(x, y, z) for (x, y, z) in itertools.product(
        [True, False], [some_object, ts], [FwPointersCfg.DISABLED, FwPointersCfg.HYBRID, FwPointersCfg.ENABLED])])
def test_cleanup_noop(mongo_host, library, data, dry_run, fw_pointers_config):
    """
    Check that we do / don't cleanup chunks based on the dry-run
    """
    with FwPointersCtx(fw_pointers_config):
        yesterday = dt.utcnow() - dtd(days=1, seconds=1)
        _id = bson.ObjectId.from_datetime(yesterday)
        with patch("bson.ObjectId", return_value=_id):
            library.write('symbol', data, prune_previous_version=False)

        # Number of chunks
        chunk_count = mongo_count(library._collection)

        # No cleanup on dry-run
        if dry_run:
            run_as_main(main, '--library', 'user.library', '--host', mongo_host)
            assert mongo_count(library._collection) == chunk_count
            assert repr(library.read('symbol').data) == repr(data)
        else:
            run_as_main(main, '--library', 'user.library', '--host', mongo_host, '-f')
            assert mongo_count(library._collection) == chunk_count
            assert repr(library.read('symbol').data) == repr(data)


@pytest.mark.parametrize(
    ['dry_run', 'data', 'fw_pointers_config'],
    [(x, y, z) for (x, y, z) in itertools.product(
        [True, False], [some_object, ts], [FwPointersCfg.DISABLED, FwPointersCfg.HYBRID, FwPointersCfg.ENABLED])])
def test_cleanup_orphaned_chunks_ignores_recent(mongo_host, library, data, dry_run, fw_pointers_config):
    """
    We don't cleanup any chunks in the range of today.  That's just asking for trouble
    """
    with FwPointersCtx(fw_pointers_config):
        yesterday = dt.utcnow() - dtd(hours=12)
        _id = bson.ObjectId.from_datetime(yesterday)
        with patch("bson.ObjectId", return_value=_id):
            library.write('symbol', data, prune_previous_version=False)
        chunk_count = mongo_count(library._collection)
        library._collection.versions.delete_one({'_id': _id})

        if dry_run:
            run_as_main(main, '--library', 'user.library', '--host', mongo_host)
            assert mongo_count(library._collection) == chunk_count
        else:
            run_as_main(main, '--library', 'user.library', '--host', mongo_host, '-f')
            assert mongo_count(library._collection) == chunk_count


@pytest.mark.parametrize('data, fw_pointers_config',
                         [(x, y) for (x, y) in itertools.product(
                             [some_object, ts],
                             [FwPointersCfg.DISABLED, FwPointersCfg.HYBRID, FwPointersCfg.ENABLED])])
def test_cleanup_orphaned_chunk_doesnt_break_versions(mongo_host, library, data, fw_pointers_config):
    """
    Check that a chunk pointed to by more than one version, aren't inadvertently cleared
    """
    with FwPointersCtx(fw_pointers_config):
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
        assert mongo_count(library._collection.versions) == 0


@pytest.mark.parametrize(
    ['dry_run', 'data', 'fw_pointers_config'],
    [(x, y, z) for (x, y, z) in itertools.product(
        [True, False], [some_object, ts], [FwPointersCfg.DISABLED, FwPointersCfg.HYBRID, FwPointersCfg.ENABLED])])
def test_cleanup_orphaned_snapshots(mongo_host, library, data, dry_run, fw_pointers_config):
    """
    Check that we do / don't cleanup chunks based on the dry-run
    """
    with FwPointersCtx(fw_pointers_config):
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
            assert mongo_count(library._collection) > 0
            assert mongo_count(library._collection.versions)
            assert repr(library.read('symbol').data) == repr(data)
            # Nothing done_APPEND_COUNT
            assert len(library._collection.versions.find_one({})['parent'])
        else:
            run_as_main(main, '--library', 'user.library', '--host', mongo_host, '-f')
            assert mongo_count(library._collection) > 0
            assert mongo_count(library._collection.versions)
            # Data still available (write with prune_previous_version will do the cleanup)
            assert repr(library.read('symbol').data) == repr(data)
            # Snapshot cleaned up
            assert not len(library._collection.versions.find_one({})['parent'])


@pytest.mark.parametrize(
    ['dry_run', 'data', 'fw_pointers_config'],
    [(x, y, z) for (x, y, z) in itertools.product(
        [True, False], [some_object, ts], [FwPointersCfg.DISABLED, FwPointersCfg.HYBRID, FwPointersCfg.ENABLED])])
def test_cleanup_orphaned_snapshots_nop(mongo_host, library, data, dry_run, fw_pointers_config):
    """
    Check that we do / don't cleanup chunks based on the dry-run
    """
    with FwPointersCtx(fw_pointers_config):
        yesterday = dt.utcnow() - dtd(days=1, seconds=1)
        _id = bson.ObjectId.from_datetime(yesterday)
        library.write('symbol', data, prune_previous_version=False)
        with patch("bson.ObjectId", return_value=_id):
            library.snapshot('snap_name')

        # No cleanup on dry-run
        if dry_run:
            run_as_main(main, '--library', 'user.library', '--host', mongo_host)
            assert mongo_count(library._collection) > 0
            assert mongo_count(library._collection.versions)
            assert repr(library.read('symbol').data) == repr(data)
            # Nothing done
            assert len(library._collection.versions.find_one({})['parent'])
        else:
            run_as_main(main, '--library', 'user.library', '--host', mongo_host, '-f')
            assert mongo_count(library._collection) > 0
            assert mongo_count(library._collection.versions)
            # Data still available (write with prune_previous_version will do the cleanup)
            assert repr(library.read('symbol').data) == repr(data)
            # Nothing done
            assert len(library._collection.versions.find_one({})['parent'])


@pytest.mark.parametrize(
    ['dry_run', 'data', 'fw_pointers_config'],
    [(x, y, z) for (x, y, z) in itertools.product(
        [True, False], [some_object, ts], [FwPointersCfg.DISABLED, FwPointersCfg.HYBRID, FwPointersCfg.ENABLED])])
def test_dont_cleanup_recent_orphaned_snapshots(mongo_host, library, data, dry_run, fw_pointers_config):
    """
    Check that we do / don't cleanup chunks based on the dry-run
    """
    with FwPointersCtx(fw_pointers_config):
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
            assert mongo_count(library._collection) > 0
            assert mongo_count(library._collection.versions)
            assert repr(library.read('symbol').data) == repr(data)
            # Nothing done
            assert len(library._collection.versions.find_one({})['parent'])
        else:
            run_as_main(main, '--library', 'user.library', '--host', mongo_host, '-f')
            assert mongo_count(library._collection) > 0
            assert mongo_count(library._collection.versions)
            # Data still available (write with prune_previous_version will do the cleanup)
            assert repr(library.read('symbol').data) == repr(data)
            # Snapshot cleaned up
            assert len(library._collection.versions.find_one({})['parent'])
