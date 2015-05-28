from mock import create_autospec, sentinel
from pymongo.database import Database
from pymongo.errors import PyMongoError

from arctic import auth


def test_authenticate():
    db = create_autospec(Database)
    db.authenticate.return_value = sentinel.ret
    assert auth.authenticate(db, sentinel.user, sentinel.password) == sentinel.ret


def test_authenticate_fails():
    db = create_autospec(Database)
    db.authenticate.side_effect = PyMongoError("error")
    assert auth.authenticate(db, sentinel.user, sentinel.password) is False
