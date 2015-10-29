from mock import create_autospec, sentinel
from pymongo.database import Database
from pymongo.errors import PyMongoError, OperationFailure
import pytest

from arctic import auth


def test_authenticate():
    db = create_autospec(Database)
    db.authenticate.return_value = sentinel.ret
    assert auth.authenticate(db, sentinel.user, sentinel.password) == sentinel.ret


def test_authenticate_fails():
    db = create_autospec(Database)
    error = "command SON([('saslStart', 1), ('mechanism', 'SCRAM-SHA-1'), ('payload', Binary('n,,n=foo,r=OTI3MzA3MTEzMTIx', 0)), ('autoAuthorize', 1)]) on namespace admin.$cmd failed: Authentication failed."
    db.authenticate.side_effect = OperationFailure(error)
    assert auth.authenticate(db, sentinel.user, sentinel.password) is False


def test_authenticate_fails_exception():
    db = create_autospec(Database)
    db.authenticate.side_effect = PyMongoError("error")
    with pytest.raises(PyMongoError):
        assert auth.authenticate(db, sentinel.user, sentinel.password) is False
