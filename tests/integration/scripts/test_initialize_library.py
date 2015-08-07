from mock import patch
import pytest

from arctic.auth import Credential
from arctic.arctic import Arctic
from arctic.scripts import arctic_init_library as mil

from ...util import run_as_main


def test_init_library(mongo_host):
    # Create the user agains the current mongo database
    with patch('arctic.scripts.arctic_init_library.do_db_auth', return_value=True), \
         patch('pymongo.database.Database.authenticate', return_value=True):
        run_as_main(mil.main, '--host', mongo_host, '--library', 'arctic_user.library')

    # Should be able to write something to the library now
    store = Arctic(mongo_host)
    assert store['user.library']._arctic_lib.get_library_metadata('QUOTA') == 10240 * 1024 * 1024
    store['user.library'].write('key', {'a': 'b'})
    assert store['user.library'].read('key').data == {'a': 'b'}


def test_init_library_no_arctic_prefix(mongo_host):
    # Create the user agains the current mongo database
    with patch('arctic.scripts.arctic_init_library.do_db_auth', return_value=True), \
         patch('pymongo.database.Database.authenticate', return_value=True):
        run_as_main(mil.main, '--host', mongo_host, '--library', 'user.library')

    # Should be able to write something to the library now
    store = Arctic(mongo_host)
    assert store['user.library']._arctic_lib.get_library_metadata('QUOTA') == 10240 * 1024 * 1024
    store['user.library'].write('key', {'a': 'b'})
    assert store['user.library'].read('key').data == {'a': 'b'}


def test_init_library_quota(mongo_host):
    # Create the user agains the current mongo database
    with patch('arctic.scripts.arctic_init_library.do_db_auth', return_value=True), \
         patch('pymongo.database.Database.authenticate', return_value=True):
        run_as_main(mil.main, '--host', mongo_host, '--library', 'arctic_user.library', '--quota', '100')

    # Should be able to write something to the library now
    store = Arctic(mongo_host)
    assert store['user.library']._arctic_lib.get_library_metadata('QUOTA') == 100 * 1024 * 1024 * 1024


def test_init_library_bad_library(mongo_host):
    with pytest.raises(Exception):
        with patch('arctic.arctic.get_auth', return_value=Credential('admin', 'adminuser', 'adminpwd', 'admin')), \
             patch('pymongo.database.Database.authenticate', return_value=True), \
             patch('argparse.ArgumentParser.error', side_effect=Exception):
            # Create the user agains the current mongo database
            run_as_main(mil.main, '--host', mongo_host, '--library', 'user')
