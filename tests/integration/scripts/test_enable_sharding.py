from mock import patch, Mock, call
import getpass
import pytest
from pymongo.errors import OperationFailure
from pymongo.read_preferences import Primary

from arctic.hooks import get_mongodb_uri
from arctic.scripts import arctic_enable_sharding as mes

from ...util import run_as_main


def test_enable_sharding(mongo_host, arctic, mongo_server, user_library, user_library_name):
    c = mongo_server.api
    with patch.object(c, 'admin') as admin:
        with patch('pymongo.MongoClient', return_value=c) as mc:
            run_as_main(mes.main, '--host', mongo_host, '--library', user_library_name)
    assert mc.call_args_list == [call(get_mongodb_uri(mongo_host))]
    assert admin.command.call_args_list == [call('buildinfo', read_preference=Primary()),
                                            call('enablesharding', 'arctic_' + getpass.getuser()),
                                            call('shardCollection', 'arctic_' + user_library_name, key={'symbol': 'hashed'})]


def test_enable_sharding_already_on_db(mongo_host, arctic, mongo_server, user_library, user_library_name):
    c = mongo_server.api
    with patch.object(c, 'admin') as admin:
        admin.command = Mock(return_value=[OperationFailure("failed: already enabled"),
                                           None])
        with patch('pymongo.MongoClient', return_value=c) as mc:
            run_as_main(mes.main, '--host', mongo_host, '--library', user_library_name)
    assert mc.call_args_list == [call(get_mongodb_uri(mongo_host))]
    assert admin.command.call_args_list == [call('buildinfo', read_preference=Primary()),
                                            call('enablesharding', 'arctic_' + getpass.getuser()),
                                            call('shardCollection', 'arctic_' + user_library_name, key={'symbol': 'hashed'})]


def test_enable_sharding_on_db_other_failure(mongo_host, arctic, mongo_server, user_library, user_library_name):
    # Create the user agains the current mongo database
    c = mongo_server.api
    with pytest.raises(OperationFailure):
        with patch.object(c, 'admin') as admin:
            with patch('pymongo.MongoClient', return_value=c):
                admin.command = Mock(side_effect=OperationFailure('OOPS'))
                run_as_main(mes.main, '--host', mongo_host, '--library', user_library_name)
