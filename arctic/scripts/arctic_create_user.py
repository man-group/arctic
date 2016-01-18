import argparse
import base64
from pymongo import MongoClient
import uuid
import logging

from ..hooks import get_mongodb_uri
from .utils import do_db_auth
from arctic.arctic import Arctic

logger = logging.getLogger(__name__)


def main():
    usage = """arctic_create_user --host research [--db mongoose_user] [--write] user

    Creates the user's personal Arctic mongo database
    Or add a user to an existing Mongo Database.
    """

    parser = argparse.ArgumentParser(usage=usage)
    parser.add_argument("--host", default='localhost', help="Hostname, or clustername. Default: localhost")
    parser.add_argument("--db", default=None, help="Database to add user on. Default: mongoose_<user>")
    parser.add_argument("--password", default=None, help="Password. Default: random")
    parser.add_argument("--write", action='store_true', default=False, help="Used for granting write access to someone else's DB")
    parser.add_argument("users", nargs='+', help="Users to add.")

    args = parser.parse_args()

    c = MongoClient(get_mongodb_uri(args.host))

    if not do_db_auth(args.host, c, args.db if args.db else 'admin'):
        logger.error("Failed to authenticate to '%s'. Check your admin password!" % (args.host))
        return

    for user in args.users:
        write_access = args.write
        p = args.password
        if p is None:
            p = base64.b64encode(uuid.uuid4().bytes).replace(b'/', b'')[:12]
        db = args.db
        if not db:
            # Users always have write access to their database
            write_access = True
            db = Arctic.DB_PREFIX + '_' + user

        # Add the user to the database
        c[db].add_user(user, p, read_only=not write_access)

        logger.info("Granted: {user} [{permission}] to {db}".format(user=user,
                                                                    permission='WRITE' if write_access else 'READ',
                                                                    db=db))
        logger.info("User creds: {db}/{user}/{password}".format(user=user,
                                                                host=args.host,
                                                                db=db,
                                                                password=p,
                                                                ))


if __name__ == '__main__':
    main()
