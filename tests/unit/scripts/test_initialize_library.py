from mock import patch
import pytest

from arctic.scripts import arctic_init_library as mil

from ...util import run_as_main


def test_init_library():
    # Create the user agains the current mongo database
    with patch('pymongo.MongoClient') as MongoClient, \
         patch('arctic.scripts.arctic_init_library.logger', autospec=True) as logger, \
         patch('arctic.scripts.arctic_init_library.Arctic', autospec=True) as Arctic, \
         patch('arctic.scripts.arctic_init_library.get_mongodb_uri', autospec=True) as get_mongodb_uri, \
         patch('arctic.scripts.arctic_init_library.do_db_auth', autospec=True) as do_db_auth:
        run_as_main(mil.main, '--host', 'hostname', '--library', 'arctic_user.library', '--type', 'VersionStore')

    get_mongodb_uri.assert_called_once_with('hostname')
    MongoClient.assert_called_once_with(get_mongodb_uri.return_value)
    do_db_auth.assert_called_once_with('hostname', MongoClient.return_value, 'arctic_user')
    Arctic.assert_called_once_with(MongoClient.return_value)
    Arctic.return_value.initialize_library.assert_called_once_with('arctic_user.library', 'VersionStore', hashed=False)
    assert logger.warn.call_count == 0


def test_init_library_no_admin():
    # Create the user agains the current mongo database
    with patch('pymongo.MongoClient') as MongoClient, \
         patch('arctic.scripts.arctic_init_library.logger', autospec=True), \
         patch('arctic.scripts.arctic_init_library.Arctic', autospec=True) as Arctic, \
         patch('arctic.scripts.arctic_init_library.get_mongodb_uri', autospec=True) as get_mongodb_uri, \
         patch('arctic.scripts.arctic_init_library.do_db_auth', autospec=True) as do_db_auth:
        run_as_main(mil.main, '--host', 'hostname', '--library', 'arctic_user.library', '--type', 'VersionStore')

    get_mongodb_uri.assert_called_once_with('hostname')
    MongoClient.assert_called_once_with(get_mongodb_uri.return_value)
    Arctic.assert_called_once_with(MongoClient.return_value)
    Arctic.return_value.initialize_library.assert_called_once_with('arctic_user.library', 'VersionStore', hashed=False)


def test_init_library_hashed():
    # Create the user agains the current mongo database
    with patch('pymongo.MongoClient') as MongoClient, \
         patch('arctic.scripts.arctic_init_library.logger', autospec=True) as logger, \
         patch('arctic.scripts.arctic_init_library.Arctic', autospec=True) as Arctic, \
         patch('arctic.scripts.arctic_init_library.get_mongodb_uri', autospec=True) as get_mongodb_uri, \
         patch('arctic.scripts.arctic_init_library.do_db_auth', autospec=True) as do_db_auth:
        run_as_main(mil.main, '--host', 'hostname', '--library', 'arctic_user.library', '--type', 'VersionStore', '--hashed')

    get_mongodb_uri.assert_called_once_with('hostname')
    MongoClient.assert_called_once_with(get_mongodb_uri.return_value)
    do_db_auth.assert_called_once_with('hostname', MongoClient.return_value, 'arctic_user')
    Arctic.assert_called_once_with(MongoClient.return_value)
    Arctic.return_value.initialize_library.assert_called_once_with('arctic_user.library', 'VersionStore', hashed=True)
    assert logger.warn.call_count == 0


def test_init_library_no_admin_no_user_creds():
    with patch('pymongo.MongoClient') as MongoClient, \
         patch('arctic.scripts.arctic_init_library.logger', autospec=True) as logger, \
         patch('arctic.scripts.arctic_init_library.Arctic', autospec=True) as Arctic, \
         patch('arctic.scripts.arctic_init_library.get_mongodb_uri', autospec=True) as get_mongodb_uri, \
         patch('arctic.scripts.arctic_init_library.do_db_auth', autospec=True, return_value=False) as do_db_auth:

        MongoClient.return_value['arctic_user'].authenticate.return_value = False
        run_as_main(mil.main, '--host', 'hostname', '--library', 'arctic_user.library', '--type', 'VersionStore')

    get_mongodb_uri.assert_called_once_with('hostname')
    MongoClient.assert_called_once_with(get_mongodb_uri.return_value)
    assert Arctic.call_count == 0


def test_bad_library_name():
    with pytest.raises(Exception):
        with patch('argparse.ArgumentParser.error', side_effect=Exception) as error:
            run_as_main(mil.main, '--library', 'arctic_jblackburn')
    error.assert_called_once_with('Must specify the full path of the library e.g. user.library!')

    with pytest.raises(Exception):
        with patch('argparse.ArgumentParser.error', side_effect=Exception) as error:
            run_as_main(mil.main)
    error.assert_called_once_with('Must specify the full path of the library e.g. user.library!')
