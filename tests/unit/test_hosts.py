from mock import patch, sentinel, call, PropertyMock, Mock
import os
import pytest

try:
    from ConfigParser import NoSectionError
except ImportError:
    from configparser import NoSectionError
from arctic.hosts import get_arctic_lib


def test_get_arctic_lib_with_known_host():
    with patch('arctic.arctic.Arctic') as Arctic:
        get_arctic_lib("foo@bar")
        assert Arctic.call_args_list == [call('bar')]


def test_get_arctic_lib_with_unknown_host():
    with patch('arctic.arctic.Arctic') as Arctic:
        with patch('pymongo.MongoClient') as MongoClient:
            get_arctic_lib("foo@bar:123")
            assert Arctic.call_args_list == [call("bar:123")]


def test_get_arctic_connection_strings():
    with patch('arctic.arctic.Arctic') as Arctic:
        with patch('pymongo.MongoClient') as MongoClient:
            get_arctic_lib("foo@bar")
            get_arctic_lib("foo.sheep@bar")
            get_arctic_lib("foo.sheep@bar:123")
            get_arctic_lib("foo.sheep@127.0.0.1:123")


@pytest.mark.parametrize(
    ["string"], [('donkey',), ('donkey:ride@blackpool',),
                 ('donkey:ride',)])
def test_get_arctic_malformed_connection_strings(string):
    with pytest.raises(ValueError):
        get_arctic_lib(string)
