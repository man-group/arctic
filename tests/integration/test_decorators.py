"""
Copyright (C) 2020 Man Group
For a list of authors, see README.md; for the license, see file LICENSE in project root directory.
"""
from arctic.decorators import _get_host


def test_get_host_VersionStore(library, mongo_host):
    assert _get_host(library) == {'mnodes': [mongo_host],
                                 'mhost': mongo_host,
                                 'l': u'arctic_test.TEST'}
