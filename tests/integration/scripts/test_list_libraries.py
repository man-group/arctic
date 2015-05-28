from mock import patch, call
import pytest

from arctic.scripts import arctic_list_libraries

from ...util import run_as_main


def test_list_library(mongo_host, library, library_name):
    with patch('arctic.scripts.arctic_list_libraries.print') as p:
        run_as_main(arctic_list_libraries.main, "--host", mongo_host)
    for x in p.call_args_list:
        if x == call(library_name):
            return
    assert False, "Failed to find a library"


def test_list_library_args(mongo_host, library, library_name):
    with patch('arctic.scripts.arctic_list_libraries.print') as p:
        run_as_main(arctic_list_libraries.main, "--host", mongo_host, library_name[:2])
    for x in p.call_args_list:
        assert x[0][0].startswith(library_name[:2])


def test_list_library_args_not_found(mongo_host, library, library_name):
    with patch('arctic.scripts.arctic_list_libraries.print') as p:
        run_as_main(arctic_list_libraries.main, "--host", mongo_host, 'some_library_which_doesnt_exist')
    assert p.call_count == 0
