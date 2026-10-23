import logging
from collections import namedtuple

import pymongo
from pymongo import MongoClient
from pymongo.errors import OperationFailure

PYMONGO_4_PLUS = pymongo.version_tuple[0] >= 4

logger = logging.getLogger(__name__)


def authenticate(db, user, password):
    """
    Return True / False on authentication success.

    PyMongo 2.6 changed the auth API to raise on Auth failure.
    PyMongo 4 removed Database.authenticate: credentials are bound to a MongoClient,
    so here they are verified with a temporary client against the db's auth source. Use
    `PYMONGO_4_PLUS` / MongoClient(username=..., password=...) to authenticate a connection.
    """
    try:
        logger.debug("Authenticating {} with {}".format(db, user))
        if not PYMONGO_4_PLUS:
            return db.authenticate(user, password)
        host, port = db.client.address or ('localhost', 27017)
        client = MongoClient(host=host, port=port, username=user, password=password, authSource=db.name)
        try:
            client[db.name].command('ping')
            return True
        finally:
            client.close()
    except OperationFailure as e:
        logger.debug("Auth Error %s" % e)
    return False


Credential = namedtuple("MongoCredentials", ['database', 'user', 'password'])


def get_auth(host, app_name, database_name):
    """
    Authentication hook to allow plugging in custom authentication credential providers
    """
    from .hooks import _get_auth_hook
    return _get_auth_hook(host, app_name, database_name)
