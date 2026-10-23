import pytest
from mock import patch, MagicMock, sentinel
from pymongo.errors import PyMongoError, OperationFailure

from arctic import auth


@pytest.fixture(autouse=True)
def legacy_pymongo_auth():
    with patch('arctic.auth.PYMONGO_4_PLUS', False):
        yield


def test_authenticate():
    db = MagicMock()
    db.authenticate.return_value = sentinel.ret
    assert auth.authenticate(db, sentinel.user, sentinel.password) == sentinel.ret


def test_authenticate_fails():
    db = MagicMock()
    error = "command SON([('saslStart', 1), ('mechanism', 'SCRAM-SHA-1'), ('payload', Binary('n,,n=foo,r=OTI3MzA3MTEzMTIx', 0)), ('autoAuthorize', 1)]) on namespace admin.$cmd failed: Authentication failed."
    db.authenticate.side_effect = OperationFailure(error)
    assert auth.authenticate(db, sentinel.user, sentinel.password) is False


def test_authenticate_fails_exception():
    db = MagicMock()
    db.authenticate.side_effect = PyMongoError("error")
    with pytest.raises(PyMongoError):
        assert auth.authenticate(db, sentinel.user, sentinel.password) is False


def test_authenticate_pymongo4():
    db = MagicMock()
    db.client.address = ('somehost', 27018)
    with patch('arctic.auth.PYMONGO_4_PLUS', True), patch('arctic.auth.MongoClient') as mc:
        assert auth.authenticate(db, 'user', 'pass') is True
    mc.assert_called_once_with(host='somehost', port=27018, username='user', password='pass', authSource=db.name)
    mc.return_value.close.assert_called_once_with()


def test_authenticate_pymongo4_fails():
    db = MagicMock()
    db.client.address = ('somehost', 27018)
    with patch('arctic.auth.PYMONGO_4_PLUS', True), patch('arctic.auth.MongoClient') as mc:
        mc.return_value.__getitem__.return_value.command.side_effect = OperationFailure('bad auth')
        assert auth.authenticate(db, 'user', 'pass') is False
    mc.return_value.close.assert_called_once_with()
