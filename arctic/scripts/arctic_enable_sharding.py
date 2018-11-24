from __future__ import print_function

import optparse

import pymongo

from .utils import setup_logging
from .._util import enable_sharding
from ..arctic import Arctic
from ..auth import authenticate
from ..auth import get_auth
from ..hooks import get_mongodb_uri


def main():
    usage = """usage: %prog [options] arg1=value, arg2=value

    Enables sharding on the specified arctic library.
    """
    setup_logging()

    parser = optparse.OptionParser(usage=usage)
    parser.add_option("--host", default='localhost', help="Hostname, or clustername. Default: localhost")
    parser.add_option("--library", help="The name of the library. e.g. 'arctic_jblackburn.lib'")

    (opts, _) = parser.parse_args()

    if not opts.library or '.' not in opts.library:
        parser.error('must specify the full path of the library e.g. arctic_jblackburn.lib!')

    print("Enabling-sharding: %s on mongo %s" % (opts.library, opts.host))

    c = pymongo.MongoClient(get_mongodb_uri(opts.host))
    credentials = get_auth(opts.host, 'admin', 'admin')
    if credentials:
        authenticate(c.admin, credentials.user, credentials.password)
    store = Arctic(c)
    enable_sharding(store, opts.library)


if __name__ == '__main__':
    main()
