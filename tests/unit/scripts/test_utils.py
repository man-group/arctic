from mock import patch, Mock, call, sentinel, MagicMock
import pytest

from arctic.scripts import arctic_init_library as mil
from arctic.scripts.utils import do_db_auth
from ...util import run_as_main


def test_do_db_auth():
    # Create the user agains the current mongo database
    admin_creds = Mock()
    user_creds = Mock()
    connection = MagicMock()
    with patch('arctic.scripts.utils.logger', autospec=True) as logger, \
         patch('arctic.scripts.utils.get_auth', autospec=True, side_effect=[admin_creds, user_creds]) as get_auth:
        assert do_db_auth('hostname', connection, 'arctic_user')

    assert get_auth.call_args_list == [call('hostname', 'admin', 'admin'),
                                       call('hostname', 'arctic', 'arctic_user')]
    connection.admin.authenticate.assert_called_once_with(admin_creds.user,
                                                          admin_creds.password)
    # Must also ensure that we auth against the user's db too ; the user
    # may well have read-only access to the admin database, but not to their user_db!
    connection.__getitem__.assert_called_once_with('arctic_user')
    connection.__getitem__.return_value.authenticate.assert_called_once_with(user_creds.user, user_creds.password)
    assert logger.error.call_count == 0


def test_do_db_auth_no_admin():
    user_creds = Mock()
    connection = MagicMock()
    # Create the user agains the current mongo database
    with patch('arctic.scripts.utils.logger', autospec=True) as logger, \
         patch('arctic.scripts.utils.get_auth', side_effect=[None, user_creds],
              autospec=True) as get_auth:

        connection.admin.authenticate.return_value = False
        assert do_db_auth('hostname', connection, 'arctic_user')

    assert logger.call_count == 0
    assert get_auth.call_args_list == [call('hostname', 'admin', 'admin'),
                                       call('hostname', 'arctic', 'arctic_user')]
    connection['arctic_user'].authenticate.assert_called_once_with(user_creds.user, user_creds.password)


def test_do_db_auth_no_user_creds():
    user_creds = Mock()
    connection = MagicMock()
    with patch('arctic.scripts.utils.logger', autospec=True) as logger, \
         patch('arctic.scripts.utils.get_auth', side_effect=[None, user_creds],
              autospec=True) as get_auth:
        connection['arctic_user'].authenticate.return_value = False
        assert not do_db_auth('hostname', connection, 'arctic_user')

    assert get_auth.call_args_list == [call('hostname', 'admin', 'admin'),
                                       call('hostname', 'arctic', 'arctic_user')]
    logger.error.assert_called_once_with("Failed to authenticate to db 'arctic_user' on 'hostname',"
                                         " using user credentials")


def test_do_db_auth_no_admin_user_creds_fails():
    connection = MagicMock()
    with patch('arctic.scripts.utils.logger', autospec=True) as logger, \
         patch('arctic.scripts.utils.get_auth', side_effect=[None, None],
              autospec=True) as get_auth:
        connection.admin.authenticate.return_value = False
        assert not do_db_auth('hostname', connection, 'arctic_user')

    assert get_auth.call_args_list == [call('hostname', 'admin', 'admin'),
                                       call('hostname', 'arctic', 'arctic_user')]
    logger.error.assert_called_once_with("You need credentials for db 'arctic_user' on 'hostname',"
                                         " or admin credentials")


def test_do_db_auth_admin_user_creds_fails():
    connection = MagicMock()
    with patch('arctic.scripts.utils.logger', autospec=True) as logger, \
         patch('arctic.scripts.utils.get_auth', side_effect=[Mock(), None],
              autospec=True) as get_auth:
        connection.admin.authenticate.return_value = False
        assert not do_db_auth('hostname', connection, 'arctic_user')

    assert get_auth.call_args_list == [call('hostname', 'admin', 'admin'),
                                       call('hostname', 'arctic', 'arctic_user')]
    logger.error.assert_called_once_with("Failed to authenticate to '%s' as Admin. Giving up." % ('hostname'))


def test_do_db_auth_role():
    # Create the user agains the current mongo database
    admin_creds = Mock()
    user_creds = Mock()
    connection = MagicMock()
    with patch('arctic.scripts.utils.logger', autospec=True) as logger, \
        patch('arctic.scripts.utils.get_auth', autospec=True, side_effect=[admin_creds, user_creds]) as get_auth:
        assert do_db_auth('hostname', connection, 'arctic_user')

    assert get_auth.call_args_list == [call('hostname', 'admin', 'admin'),
                                       call('hostname', 'arctic', 'arctic_user')]
    connection.admin.authenticate.assert_called_once_with(admin_creds.user,
                                                          admin_creds.password)
    # Must also ensure that we auth against the user's db too ; the user
    # may well have read-only access to the admin database, but not to their user_db!
    connection.__getitem__.assert_called_once_with('arctic_user')
    connection.__getitem__.return_value.authenticate.assert_called_once_with(user_creds.user, user_creds.password)
    assert logger.error.call_count == 0
