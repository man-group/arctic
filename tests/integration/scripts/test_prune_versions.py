import time

from mock import patch, ANY, call

from arctic.auth import Credential
from arctic.scripts import arctic_prune_versions as mpv
from ...util import run_as_main


def test_prune_versions_symbol(mongo_host, library, library_name):
    with patch('arctic.scripts.arctic_prune_versions.prune_versions', autospec=True) as prune_versions, \
            patch('arctic.scripts.utils.get_auth', return_value=Credential('admin', 'adminuser', 'adminpwd')), \
            patch('pymongo.database.Database.authenticate', return_value=True):

        run_as_main(mpv.main, '--host', mongo_host, '--library', library_name, '--symbols', 'sym1,sym2')
        prune_versions.assert_has_calls([call(ANY, ['sym1', 'sym2'], 10)])


def test_prune_versions_full(mongo_host, library, library_name):
    with patch('arctic.scripts.arctic_prune_versions.do_db_auth', return_value=True):
        # Write some stuff with snapshots
        library.snapshot('snap')
        library.write('symbol', "val1")
        library.write('symbol', "val2")
        library.snapshot('snap1')
        library.write('symbol', "val3")

        # Prune older than 10 mins - nothing deleted
        run_as_main(mpv.main, '--host', mongo_host, '--library', library_name, '--keep-mins', 10)
        assert [x['version'] for x in library.list_versions('symbol')] == [3, 2, 1]
        # Prune older than 0 minutes, v1 deleted
        run_as_main(mpv.main, '--host', mongo_host, '--library', library_name, '--keep-mins', 0)
        assert [x['version'] for x in library.list_versions('symbol')] == [3, 2]

        # Delete the snapshots
        library.delete_snapshot('snap')
        library.delete_snapshot('snap1')
        run_as_main(mpv.main, '--host', mongo_host, '--library', library_name, '--keep-mins', 0)
        assert [x['version'] for x in library.list_versions('symbol')] == [3]


def test_keep_recent_snapshots(library):
    library.write("cherry", "blob")
    half_a_day_ago = time.time() - (3600 * 12.)
    with patch('time.time', return_value=half_a_day_ago):
        library.snapshot("snappy")
    library._snapshots.delete_one({"name": "snappy"})

    mpv.prune_versions(library, ["cherry"], 10)

    assert len(library._versions.find_one({"symbol": "cherry"}).get("parent", [])) == 1


def test_fix_broken_snapshot_references(library):
    library.write("cherry", "blob")
    one_day_ago = time.time() - (3600 * 24.) - 10  # make sure we are a few seconds before 24 hours
    with patch('time.time', return_value=one_day_ago):
        library.snapshot("snappy")
    library._snapshots.delete_one({"name": "snappy"})

    mpv.prune_versions(library, ["cherry"], 10)

    assert library._versions.find_one({"symbol": "cherry"}).get("parent", []) == []


def test_keep_only_one_version(library):
    library.write("cherry", "blob")
    library.write("cherry", "blob")
    one_day_ago = time.time() - (3600 * 24.) - 10  # make sure we are a few seconds before 24 hours
    with patch('time.time', return_value=one_day_ago):
        library.snapshot("snappy")
    library._snapshots.delete_one({"name": "snappy"})

    mpv.prune_versions(library, ["cherry"], 0)

    assert len(list(library._versions.find({"symbol": "cherry"}))) == 1
