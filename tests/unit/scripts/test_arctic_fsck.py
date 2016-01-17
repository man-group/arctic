from mock import patch, sentinel, call

from arctic.scripts.arctic_fsck import main

from ...util import run_as_main
import sys
import pytest


def test_main():
    with patch('arctic.scripts.arctic_fsck.Arctic') as Arctic, \
         patch('arctic.scripts.arctic_fsck.get_mongodb_uri') as get_mongodb_uri, \
         patch('arctic.scripts.arctic_fsck.do_db_auth') as do_db_auth:
        run_as_main(main, '--host', '%s:%s' % (sentinel.host, sentinel.port),
                          '-v', '--library', 'sentinel.library', 'lib2', '-f')
    get_mongodb_uri.assert_called_once_with('sentinel.host:sentinel.port')
    Arctic.assert_called_once_with(get_mongodb_uri.return_value)
    assert do_db_auth.call_args_list == [call('%s:%s' % (sentinel.host, sentinel.port),
                                                  Arctic.return_value._conn,
                                                  'arctic_sentinel'),
                                         call('%s:%s' % (sentinel.host, sentinel.port),
                                                  Arctic.return_value._conn,
                                                  'arctic')]
    assert Arctic.return_value.__getitem__.return_value._fsck.call_args_list == [call(False),
                                                                                   call(False), ]


def test_main_dry_run():
    with patch('arctic.scripts.arctic_fsck.Arctic') as Arctic, \
         patch('arctic.scripts.arctic_fsck.get_mongodb_uri') as get_mongodb_uri, \
         patch('arctic.scripts.arctic_fsck.do_db_auth') as do_db_auth:
        run_as_main(main, '--host', '%s:%s' % (sentinel.host, sentinel.port),
                    '-v', '--library', 'sentinel.library', 'sentinel.lib2')
    get_mongodb_uri.assert_called_once_with('sentinel.host:sentinel.port')
    Arctic.assert_called_once_with(get_mongodb_uri.return_value)
    assert do_db_auth.call_count == 0
    assert Arctic.return_value.__getitem__.return_value._fsck.call_args_list == [call(True),
                                                                                   call(True), ]
