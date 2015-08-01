import optparse
import pymongo
import logging

from ..hooks import get_mongodb_uri
from ..arctic import Arctic, ArcticLibraryBinding
from .utils import do_db_auth, setup_logging

logger = logging.getLogger(__name__)


def prune_versions(lib, symbol, keep_mins):
    lib._prune_previous_versions(symbol, keep_mins=keep_mins)


def main():
    usage = """usage: %prog [options]

    Prunes (i.e. deletes) versions of data that are not the most recent, and are older than 10 minutes,
    and are not in use by snapshots. Must be used on a Arctic VersionStore library instance.

    Example:
        arctic_prune_versions --host=hostname --library=arctic_jblackburn.my_library
    """
    setup_logging()

    parser = optparse.OptionParser(usage=usage)
    parser.add_option("--host", default='localhost', help="Hostname, or clustername. Default: localhost")
    parser.add_option("--library", help="The name of the library. e.g. 'arctic_jblackburn.library'")
    parser.add_option("--symbols", help="The symbols to prune - comma separated (default all)")
    parser.add_option("--keep-mins", default=10, help="Ensure there's a version at least keep-mins old. Default:10")

    (opts, _) = parser.parse_args()

    if not opts.library:
        parser.error('Must specify the Arctic library e.g. arctic_jblackburn.library!')
    db_name, _ = ArcticLibraryBinding._parse_db_lib(opts.library)

    print "Pruning (old) versions in : %s on mongo %s" % (opts.library, opts.host)
    print "Keeping all versions <= %s mins old" % (opts.keep_mins)
    c = pymongo.MongoClient(get_mongodb_uri(opts.host))

    if not do_db_auth(opts.host, c, db_name):
        logger.error('Authentication Failed. Exiting.')
        return
    lib = Arctic(c)[opts.library]

    if opts.symbols:
        symbols = opts.symbols.split(',')
    else:
        symbols = lib.list_symbols(all_symbols=True)
        logger.info("Found %s symbols" % len(symbols))

    for s in symbols:
        logger.info("Pruning %s" % s)
        prune_versions(lib, s, opts.keep_mins)
    logger.info("Done")


if __name__ == '__main__':
    main()
