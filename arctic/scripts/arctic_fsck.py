import logging
import argparse

from ..hooks import get_mongodb_uri
from ..arctic import Arctic, ArcticLibraryBinding
from .utils import do_db_auth, setup_logging

logger = logging.getLogger(__name__)


def main():
    usage = """
    Check a Arctic Library for inconsistencies.
    """
    setup_logging()

    parser = argparse.ArgumentParser(usage=usage)
    parser.add_argument("--host", default='localhost', help="Hostname, or clustername. Default: localhost")
    parser.add_argument("--library", nargs='+', required=True, help="The name of the library. e.g. 'arctic_jblackburn.lib'")
    parser.add_argument("-v", action='store_true', help="Verbose mode")
    parser.add_argument("-f", action='store_true', help="Force ; Cleanup any problems found. (Default is dry-run.)")
    parser.add_argument("-n", action='store_true', help="No FSCK ; just print stats.)")

    opts = parser.parse_args()

    if opts.v:
        logger.setLevel(logging.DEBUG)

    if not opts.f:
        logger.info("DRY-RUN: No changes will be made.")

    logger.info("FSCK'ing: %s on mongo %s" % (opts.library, opts.host))
    store = Arctic(get_mongodb_uri(opts.host))

    for lib in opts.library:
        # Auth to the DB for making changes
        if opts.f:
            database_name, _ = ArcticLibraryBinding._parse_db_lib(lib)
            do_db_auth(opts.host, store._conn, database_name)

        orig_stats = store[lib].stats()

        logger.info('----------------------------')
        if not opts.n:
            store[lib]._fsck(not opts.f)
        logger.info('----------------------------')

        final_stats = store[lib].stats()
        logger.info('Stats:')
        logger.info('Sharded:        %s' % final_stats['chunks'].get('sharded', False))
        logger.info('Symbols:  %10d' % len(store[lib].list_symbols()))
        logger.info('Versions: %10d   Change(+/-) %6d  (av: %.2fMB)' %
                    (final_stats['versions']['count'],
                     final_stats['versions']['count'] - orig_stats['versions']['count'],
                     final_stats['versions'].get('avgObjSize', 0) / 1024. / 1024.))
        logger.info("Versions: %10.2fMB Change(+/-) %.2fMB" %
                    (final_stats['versions']['size'] / 1024. / 1024.,
                    (final_stats['versions']['size'] - orig_stats['versions']['size']) / 1024. / 1024.))
        logger.info('Chunk Count: %7d   Change(+/-) %6d  (av: %.2fMB)' %
                    (final_stats['chunks']['count'],
                     final_stats['chunks']['count'] - orig_stats['chunks']['count'],
                     final_stats['chunks'].get('avgObjSize', 0) / 1024. / 1024.))
        logger.info("Chunks: %12.2fMB Change(+/-) %6.2fMB" %
                    (final_stats['chunks']['size'] / 1024. / 1024.,
                    (final_stats['chunks']['size'] - orig_stats['chunks']['size']) / 1024. / 1024.))
        logger.info('----------------------------')

    if not opts.f:
        logger.info("Done: DRY-RUN: No changes made. (Use -f to fix any problems)")
    else:
        logger.info("Done.")

if __name__ == '__main__':
    main()
