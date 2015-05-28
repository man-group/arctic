from mock import patch
from StringIO import StringIO

from arctic.auth import Credential
from arctic.scripts import arctic_create_user as mcu

from ...util import run_as_main


def test_create_user(mongo_host, mongodb):
    # Create the user agains the current mongo database
    with patch('arctic.scripts.arctic_create_user.get_auth',
               return_value=Credential('admin', 'adminuser', 'adminpwd')), \
         patch('pymongo.database.Database.authenticate',return_value=True):
        run_as_main(mcu.main, '--host', mongo_host, 'user', '--pass', 'pass')

    # Check:
    # User exists in system
    user = mongodb.admin.system.users.find_one({'user': 'user'})
    assert user
    assert user['readOnly'] == True
    # User db exists
    user = mongodb.arctic_user.system.users.find_one({'user': 'user'})
    assert user
    assert 'readOnly' not in user or user['readOnly'] == False


def test_create_admin_user(mongo_host, mongodb):
    # Create the user agains the current mongo database

    with patch('arctic.scripts.arctic_create_user.get_auth',
               return_value=Credential('admin', 'adminuser', 'adminpwd')), \
         patch('pymongo.database.Database.authenticate', return_value=True):
        run_as_main(mcu.main, '--host', mongo_host, 'user', '--pass', 'pass', '--admin-write')

    # Check:
    # User exists in system
    user = mongodb.admin.system.users.find_one({'user': 'user'})
    assert user
    assert 'readOnly' not in user or user['readOnly'] == False
    # User db exists
    user = mongodb.arctic_user.system.users.find_one({'user': 'user'})
    assert user
    assert 'readOnly' not in user or user['readOnly'] == False


def test_create_user_verbose(mongo_host, mongodb):
    user = 'user'
    pwd = 'password'
    stderr = StringIO()
    stdout = StringIO()
    with patch('arctic.scripts.arctic_create_user.get_auth',
               return_value=Credential('admin', 'adminuser', 'adminpwd')), \
         patch('pymongo.database.Database.authenticate', return_value=True), \
         patch('sys.stderr', stderr), \
         patch('sys.stdout', stdout):
        run_as_main(mcu.main, '--host', mongo_host, user, '--pass', pwd, '--verbose')
    out = stdout.getvalue()
    assert 'Adding user %s to DB %s' % (user, mongo_host) in out
    assert 'Adding database arctic_%s to DB %s' % (user, mongo_host) in out


def test_create_user_dryrun_nodb(mongo_host, mongodb):
    user = 'user'
    pwd = 'password'
    stderr = StringIO()
    stdout = StringIO()
    with patch('arctic.scripts.arctic_create_user.get_auth',
               return_value=Credential('admin', 'adminuser', 'adminpwd')), \
         patch('pymongo.database.Database.authenticate', return_value=True), \
         patch('sys.stderr', stderr), \
         patch('sys.stdout', stdout):
        run_as_main(mcu.main, '--host', mongo_host, user, '--pass', pwd, '--dryrun', '--nodb')
    out = stdout.getvalue()
    assert 'DRYRUN: add user %s readonly True nodb True' % (user) in out

def test_create_user_no_passwd(mongo_host, mongodb):
    user = 'user'
    pwd = None
    newpwd = 'newpasswd'
    stdout = StringIO()
    with patch('arctic.scripts.arctic_create_user.get_auth',
               return_value=Credential('admin', 'adminuser', 'adminpwd')), \
         patch('pymongo.database.Database.authenticate',return_value=True), \
         patch('base64.b64encode',return_value=newpwd), \
         patch('sys.stdout', stdout):
        run_as_main(mcu.main, '--host', mongo_host, user)
    out = stdout.getvalue()
    assert '%-16s %s' % (user,newpwd) in out


def test_create_user_no_creds(mongo_host, mongodb):
    stderr = StringIO()
    with patch('arctic.scripts.arctic_create_user.get_auth', return_value=None), \
         patch('sys.stderr', stderr):
        run_as_main(mcu.main, '--host', mongo_host)
    err = stderr.getvalue()
    assert 'You have no admin credentials' in err


def test_create_user_auth_fail(mongo_host):
    stderr = StringIO()
    with patch('arctic.scripts.arctic_create_user.get_auth', return_value=Credential('admin', 'user', 'pass')), \
         patch('pymongo.database.Database.authenticate', return_value=False), \
         patch('sys.stderr', stderr):
        run_as_main(mcu.main, '--host', mongo_host)
    err = stderr.getvalue()
    assert 'Failed to authenticate' in err
