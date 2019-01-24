from __future__ import print_function

import argparse
import logging

import pymongo

from .utils import do_db_auth, setup_logging
from ..arctic import Arctic, VERSION_STORE, LIBRARY_TYPES, \
    ArcticLibraryBinding
from ..hooks import get_mongodb_uri

logger = logging.getLogger(__name__)


def main():
    usage = """Initializes a named library in a user's database.  Note that it will enable sharding on the underlying
    collection if it can.  To do this you must have admin credentials in arctic:

    Example:
        arctic_init_library --host=hostname --library=arctic_jblackburn.my_library
    """
    setup_logging()

    parser = argparse.ArgumentParser(usage=usage)
    parser.add_argument("--host", default='localhost', help="Hostname, or clustername. Default: localhost")
    parser.add_argument("--library", help="The name of the library. e.g. 'arctic_jblackburn.lib'")
    parser.add_argument("--type", default=VERSION_STORE, choices=sorted(LIBRARY_TYPES.keys()),
                        help="The type of the library, as defined in "
                             "arctic.py. Default: %s" % VERSION_STORE)
    parser.add_argument("--quota", default=10, help="Quota for the library in GB. A quota of 0 is unlimited."
                                                    "Default: 10")
    parser.add_argument(
        "--hashed",
        action="store_true",
        default=False,
        help="Use hashed based sharding. Useful where SYMBOLs share a common prefix (e.g. Bloomberg BBGXXXX symbols) "
             "Default: False")

    opts = parser.parse_args()

    if not opts.library or '.' not in opts.library:
        parser.error('Must specify the full path of the library e.g. user.library!')
    db_name, _ = ArcticLibraryBinding._parse_db_lib(opts.library)

    print("Initializing: %s on mongo %s" % (opts.library, opts.host))
    c = pymongo.MongoClient(get_mongodb_uri(opts.host))

    if not do_db_auth(opts.host, c, db_name):
        logger.error('Authentication Failed. Exiting.')
        return

    store = Arctic(c)
    store.initialize_library("%s" % opts.library, opts.type, hashed=opts.hashed)
    logger.info("Library %s created" % opts.library)

    logger.info("Setting quota to %sG" % opts.quota)
    store.set_quota(opts.library, int(opts.quota) * 1024 * 1024 * 1024)


if __name__ == '__main__':
    main()
