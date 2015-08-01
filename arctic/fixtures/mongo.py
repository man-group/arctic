# Copyright (C) 2013 by Clearcode <http://clearcode.cc>
# and associates (see AUTHORS).

# This file is part of pytest-dbfixtures.

# pytest-dbfixtures is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# pytest-dbfixtures is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.

# You should have received a copy of the GNU Lesser General Public License
# along with pytest-dbfixtures.  If not, see <http://www.gnu.org/licenses/>.

import os
import pytest

from path import path
from tempfile import mkdtemp

from pytest_dbfixtures.executors import TCPExecutor
from pytest_dbfixtures.port import get_port
from pytest_dbfixtures.utils import get_config, try_import, get_process_fixture


def mongo_proc(executable=None, params=None, host=None, port=None,
               logs_prefix=''):
    """
    Mongo process factory.

    :param str executable: path to mongod
    :param str params: params
    :param str host: hostname
    :param str port: exact port (e.g. '8000')
        or randomly selected port:
            '?' - any random available port
            '2000-3000' - random available port from a given range
            '4002,4003' - random of 4002 or 4003 ports
    :param str logs_prefix: prefix for log filename
    :rtype: func
    :returns: function which makes a mongo process
    """

    @pytest.fixture(scope='function')
    def mongo_proc_fixture(request):
        """
        #. Get config.
        #. Run a ``mongod`` process.
        #. Stop ``mongod`` process after tests.

        .. note::
            `mongod <http://docs.mongodb.org/v2.2/reference/mongod/>`_

        :param FixtureRequest request: fixture request object
        :rtype: pytest_dbfixtures.executors.TCPExecutor
        :returns: tcp executor
        """
        config = get_config(request)

        # make a temporary directory for tests and delete it
        # if tests have been finished
        tmp = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'tmp')
        if not os.path.exists(tmp):
            os.mkdir(tmp)
        tmpdir = path(mkdtemp(prefix='mongo_pytest_fixture', dir=tmp))
        request.addfinalizer(lambda: tmpdir.exists() and tmpdir.rmtree())

        mongo_exec = executable or config.mongo.mongo_exec
        mongo_params = params or config.mongo.params

        mongo_host = host or config.mongo.host
        mongo_port = get_port(port or config.mongo.port)

        logsdir = path(request.config.getvalue('logsdir'))
        mongo_logpath = logsdir / '{prefix}mongo.{port}.log'.format(
            prefix=logs_prefix,
            port=mongo_port
        )

        mongo_executor = TCPExecutor(
            '{mongo_exec} --bind_ip {host} --port {port} --dbpath {dbpath} --logpath {logpath} {params}'.format(  # noqa
                mongo_exec=mongo_exec,
                params=mongo_params,
                host=mongo_host,
                port=mongo_port,
                dbpath=tmpdir,
                logpath=mongo_logpath,
            ),
            host=mongo_host,
            port=mongo_port,
        )
        mongo_executor.start()

        request.addfinalizer(mongo_executor.stop)

        return mongo_executor

    return mongo_proc_fixture


def mongodb(process_fixture_name):
    """
    Mongo database factory.

    :param str process_fixture_name: name of the process fixture
    :rtype: func
    :returns: function which makes a connection to mongo
    """

    @pytest.fixture
    def mongodb_factory(request):
        """
        #. Get pymongo module and config.
        #. Get connection to mongo.
        #. Drop collections before and after tests.

        :param FixtureRequest request: fixture request object
        :rtype: pymongo.connection.Connection
        :returns: connection to mongo database
        """
        proc_fixture = get_process_fixture(request, process_fixture_name)

        pymongo, _ = try_import('pymongo', request)

        mongo_host = proc_fixture.host
        mongo_port = proc_fixture.port

        try:
            client = pymongo.MongoClient
        except AttributeError:
            client = pymongo.Connection

        mongo_conn = client(mongo_host, mongo_port)

        return mongo_conn

    return mongodb_factory


__all__ = [mongodb, mongo_proc]
