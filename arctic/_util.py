from pandas import DataFrame
from pandas.util.testing import assert_frame_equal
from pymongo.errors import OperationFailure
import logging

logger = logging.getLogger(__name__)


def indent(s, num_spaces):
    s = s.split('\n')
    s = [(num_spaces * ' ') + line for line in s]
    s = '\n'.join(s)
    return s


def are_equals(o1, o2, **kwargs):
    try:
        if isinstance(o1, DataFrame):
            assert_frame_equal(o1, o2, kwargs)
            return True
        return o1 == o2
    except Exception:
        return False


def enable_sharding(arctic, library_name, hashed=False):
    c = arctic._conn
    lib = arctic[library_name]._arctic_lib
    dbname = lib._db.name
    library_name = lib.get_top_level_collection().name
    try:
        c.admin.command('enablesharding', dbname)
    except OperationFailure as e:
        if not 'failed: already enabled' in str(e):
            raise
    if not hashed:
        logger.info("Range sharding 'symbol' on: " + dbname + '.' + library_name)
        c.admin.command('shardCollection', dbname + '.' + library_name, key={'symbol': 1})
    else:
        logger.info("Hash sharding 'symbol' on: " + dbname + '.' + library_name)
        c.admin.command('shardCollection', dbname + '.' + library_name, key={'symbol': 'hashed'})


def enable_powerof2sizes(arctic, library_name):
    lib = arctic[library_name]._arctic_lib
    collection = lib.get_top_level_collection()
    lib._db.command({"collMod": collection.name, 'usePowerOf2Sizes': "true"})
    logger.info("usePowerOf2Sizes enabled for %s", collection.name)

    for coll in collection.database.collection_names():
        if coll.startswith("%s." % collection.name):
            lib._db.command({"collMod": coll, 'usePowerOf2Sizes': "true"})
            logger.info("usePowerOf2Sizes enabled for %s", coll)
