from collections import namedtuple
import logging
from pymongo.errors import OperationFailure

logger = logging.getLogger(__name__)


def authenticate(db, user, password):
    """
    Return True / False on authentication success.

    PyMongo 2.6 changed the auth API to raise on Auth failure.
    """
    try:
        logger.debug("Authenticating {} with {}".format(db, user))
        return db.authenticate(user, password)
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
