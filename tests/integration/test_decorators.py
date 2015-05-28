from arctic.decorators import _get_host


def test_get_host_VersionStore(library, mongo_host):
    assert _get_host(library) == {'mnodes': [mongo_host],
                                 'mhost': mongo_host,
                                 'l': u'arctic_test.TEST'}
