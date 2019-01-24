import pymongo
import pytest
from pymongo.errors import OperationFailure

import arctic
from arctic.store import _version_store_utils as vsu
from tests.integration.chunkstore.test_utils import create_test_data

symbol = 'TS1'


def n_append(library, library_name, total_appends, rows_per_append, bulk_data_ts, start_idx, do_snapshots=True, do_prune=True):
    open_last_row = 0
    for i in range(total_appends):
        first_row = start_idx + i * rows_per_append
        open_last_row = start_idx + (i + 1) * rows_per_append
        snap = 'snap_{}'.format(first_row)
        library.append(symbol, bulk_data_ts[first_row:open_last_row],
                       metadata={'snap': snap},
                       prune_previous_version=do_prune)
        if do_snapshots:
            library.snapshot(snap)

    return open_last_row


def _corrupt_with_append_only(library, library_name):
    def do_fail(version):
        raise Exception('test')

    large_ts = create_test_data(size=2000, cols=100,
                                index=True, multiindex=False,
                                random_data=True, random_ids=True)
    library.write(symbol, large_ts[0:1000])  # v1
    library.snapshot('snap_write_a')
    library.append(symbol, large_ts[1000:1010])  # v2
    library.snapshot('snap_write_b')

    # Here we simulate a scenario where an append succeeds to insert the data segments,
    # but fails to insert the version document (i.e. Mongo error occurred)
    orig_insert_version = library._insert_version
    library._insert_version = do_fail
    try:
        library.append(symbol, large_ts[1010:1020])  # v3
    except:
        pass
    library._insert_version = orig_insert_version

    library.write_metadata(symbol, {'hello': 'there'})  # , prune_previous_version=False)

    # Appending subsequently overlapping and non-SHA-matching data cause data corruption
    library.append(symbol, large_ts[1018:1030])  # , prune_previous_version=False)

    last_v = library._versions.find_one(sort=[('version', pymongo.DESCENDING)])
    vsu.analyze_symbol(library, symbol, 0, last_v['version'] + 1)

    # Verify no versions have been corrupted
    for v in library._versions.find(sort=[('version', pymongo.DESCENDING)]):
        library.read(symbol, as_of=v['version'])


def test_no_corruption_restore_append_overlapping(library, library_name):
    large_ts = create_test_data(size=3000, cols=100,
                                index=True, multiindex=False,
                                random_data=True, random_ids=True)
    rows_per_append = 100

    n_append(library, library_name, 18, rows_per_append, large_ts, 0)

    # Corrupts all versions between the version that row "restore_from_row" was written,
    restore_from_row = rows_per_append * 10
    library.restore_version(symbol, 'snap_{}'.format(restore_from_row))
    library.append(symbol, large_ts[restore_from_row:restore_from_row + 50])

    last_v = library._versions.find_one(sort=[('version', pymongo.DESCENDING)])
    vsu.analyze_symbol(library, symbol, 0, last_v['version'] + 1)

    # Verify no versions have been corrupted
    for v in library._versions.find(sort=[('version', pymongo.DESCENDING)]):
        library.read(symbol, as_of=v['version'])


def test_no_corruption_restore_writemeta_append(library, library_name):
    large_ts = create_test_data(size=2000, cols=100,
                                index=True, multiindex=False,
                                random_data=True, random_ids=True)
    rows_per_append = 100

    last_row = n_append(library, library_name, 9, rows_per_append, large_ts, 0)

    library.write_metadata(symbol, metadata={'abc': 'xyz'})

    n_append(library, library_name, 9, rows_per_append, large_ts, last_row)

    library.write_metadata(symbol, metadata={'abc2': 'xyz2'})

    # Corrupts all versions between the version that row "restore_from_row" was written,
    restore_from_row = rows_per_append * 10
    library.restore_version(symbol, 'snap_{}'.format(restore_from_row))

    library.write_metadata(symbol, metadata={'abc3': 'xyz3'})

    library.append(symbol, large_ts[restore_from_row:restore_from_row + 50])

    library.write_metadata(symbol, metadata={'abc4': 'xyz4'})

    last_v = library._versions.find_one(sort=[('version', pymongo.DESCENDING)])
    vsu.analyze_symbol(library, symbol, 0, last_v['version'] + 1)

    # Verify no versions have been corrupted
    for v in library._versions.find(sort=[('version', pymongo.DESCENDING)]):
        library.read(symbol, as_of=v['version'])


def test_no_corruption_restore_append_non_overlapping_tstamps(library, library_name):
    large_ts = create_test_data(size=2000, cols=100,
                                index=True, multiindex=False,
                                random_data=True, random_ids=True)

    # Append with 50 small uncompressed segments (no new base yet)
    last_row_b = n_append(library, library_name, 50, 25, large_ts, 0, False, True)

    library.snapshot('snap_A')

    # Append with 20 more small segments, causes once copy-rewrite with new base, and then some small appended segments
    n_append(library, library_name, 15, 25, large_ts, last_row_b, True, True)

    library.restore_version(symbol, as_of='snap_A')

    last_row = n_append(library, library_name, 1, 40, large_ts, last_row_b, False, True)
    library.snapshot('snap_B')

    # Corrupts all versions
    last_row = n_append(library, library_name, 1, 10, large_ts, last_row, False, True)
    last_row = n_append(library, library_name, 8, 20, large_ts, last_row, False, True)
    library.snapshot('snap_C')

    last_v = library._versions.find_one(sort=[('version', pymongo.DESCENDING)])
    vsu.analyze_symbol(library, symbol, 0, last_v['version'] + 1)

    # Verify no versions have been corrupted
    for v in library._versions.find(sort=[('version', pymongo.DESCENDING)]):
        library.read(symbol, as_of=v['version'])


def test_restore_append_overlapping_corrupts_old(library, library_name):
    large_ts = create_test_data(size=2000, cols=100,
                                index=True, multiindex=False,
                                random_data=True, random_ids=True)
    library.write(symbol, large_ts[0:1000])
    library.snapshot('snap_write_a')

    library.append(symbol, large_ts[1000:1010])

    library.restore_version(symbol, as_of='snap_write_a', prune_previous_version=True)
    library.append(symbol, large_ts[1000:1009])

    last_v = library._versions.find_one(sort=[('version', pymongo.DESCENDING)])
    vsu.analyze_symbol(library, symbol, 0, last_v['version'] + 1)

    # Verify no versions have been corrupted
    for v in library._versions.find(sort=[('version', pymongo.DESCENDING)]):
        library.read(symbol, as_of=v['version'])


def test_restore_append_overlapping_corrupts_last(library, library_name):
    large_ts = create_test_data(size=2000, cols=100,
                                index=True, multiindex=False,
                                random_data=True, random_ids=True)
    library.write(symbol, large_ts[0:1000])
    library.snapshot('snap_write_a')

    library.append(symbol, large_ts[1000:1010])

    library.restore_version(symbol, as_of='snap_write_a', prune_previous_version=True)
    library.append(symbol, large_ts[1000:1012])

    last_v = library._versions.find_one(sort=[('version', pymongo.DESCENDING)])
    vsu.analyze_symbol(library, symbol, 0, last_v['version'] + 1)

    # Verify no versions have been corrupted
    for v in library._versions.find(sort=[('version', pymongo.DESCENDING)]):
        library.read(symbol, as_of=v['version'])


# This is not necessary to fix, but the Exception thrown is quite confusing.
@pytest.mark.skip(reason="Not critical as upsert=False is rarely used. A more specific handling/exception is required here.")
def test_append_fail_after_delete_noupsert(library, library_name):
    large_ts = create_test_data(size=2000, cols=100,
                                index=True, multiindex=False,
                                random_data=True, random_ids=True)
    library.write(symbol, large_ts[0:1000])  #v1
    library.snapshot('snap_a')
    library.append(symbol, large_ts[1000:1010])  #v2
    library.snapshot('snap_b')
    library.append(symbol, large_ts[1010:1020])  #v3
    library.snapshot('snap_c')

    library.append(symbol, large_ts[1030:1040])  #v4

    library.delete(symbol) #v5

    library.append(symbol, large_ts[1040:1050], upsert=False)  # v6

    last_v = library._versions.find_one(sort=[('version', pymongo.DESCENDING)])
    vsu.analyze_symbol(library, symbol, 0, last_v['version'] + 1)

    # Verify no versions have been corrupted
    for v in library._versions.find(sort=[('version', pymongo.DESCENDING)]):
        library.read(symbol, as_of=v['version'])


def test_append_without_corrupt_check(library, library_name):
    orig_check = arctic.store._ndarray_store.CHECK_CORRUPTION_ON_APPEND
    arctic.store._ndarray_store.set_corruption_check_on_append(False)
    try:
        with pytest.raises(OperationFailure):
            _corrupt_with_append_only(library, library_name)
    finally:
        arctic.store._ndarray_store.set_corruption_check_on_append(orig_check)


def test_append_with_corrupt_check(library, library_name):
    orig_check = arctic.store._ndarray_store.CHECK_CORRUPTION_ON_APPEND
    arctic.store._ndarray_store.set_corruption_check_on_append(True)
    try:
        _corrupt_with_append_only(library, library_name)
    finally:
        arctic.store._ndarray_store.set_corruption_check_on_append(orig_check)


def test_fast_check_corruption(library, library_name):
    ts = create_test_data(size=100, cols=100,
                          index=True, multiindex=False,
                          random_data=True, random_ids=True)
    library.write(symbol, ts[0:10])  # v1

    assert not vsu.fast_is_corrupted(library, symbol, input_v=1)

    library.append(symbol, ts[10:20], prune_previous_version=False)  # v2
    assert not vsu.fast_is_corrupted(library, symbol, input_v=2)

    library.append(symbol, ts[20:30], prune_previous_version=False)  # v3
    assert not vsu.fast_is_corrupted(library, symbol, input_v=3)

    # Now the dangerous part
    last_segment = library._collection.find_one({}, sort=[('_id', pymongo.DESCENDING)])
    library._collection.delete_one({'_id': last_segment['_id']})

    assert vsu.fast_is_corrupted(library, symbol, input_v=3)


def test_fast_is_safe_to_append(library, library_name):
    from bson.binary import Binary
    import hashlib
    def modify_segment(segment, item):
        segment['segment'] -= 2
        sha = hashlib.sha1()
        sha.update(item.encode('ascii'))
        segment['sha'] = Binary(sha.digest())
        segment.pop('_id')

    ts = create_test_data(size=100, cols=100,
                          index=True, multiindex=False,
                          random_data=True, random_ids=True)
    library.write(symbol, ts[0:10])  # v1
    assert vsu.is_safe_to_append(library, symbol, input_v=1)

    library.append(symbol, ts[10:20], prune_previous_version=False)  # v2
    assert vsu.is_safe_to_append(library, symbol, input_v=2)

    library.append(symbol, ts[20:30], prune_previous_version=False)  # v3
    assert vsu.is_safe_to_append(library, symbol, input_v=3)

    # Corrupt the data be removing segment
    last_segment = library._collection.find_one({}, sort=[('_id', pymongo.DESCENDING)])
    library._collection.delete_one({'_id': last_segment['_id']})
    assert not vsu.is_safe_to_append(library, symbol, input_v=3)
    with pytest.raises(OperationFailure):
        library.read(symbol)

    # Fix the library by adding back the deleted segment
    library._collection.insert_one(last_segment)
    assert vsu.is_safe_to_append(library, symbol, input_v=3)

    # Corrupt the data be adding an unnecessary segment
    modify_segment(last_segment, 'abcd')
    library._collection.insert_one(last_segment)
    assert not vsu.is_safe_to_append(library, symbol, input_v=3)
    with pytest.raises(OperationFailure):
        library.read(symbol)
