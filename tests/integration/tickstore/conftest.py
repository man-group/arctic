import pytest

from arctic.tickstore import toplevel
from arctic.tickstore import tickstore


def pytest_generate_tests(metafunc):
    if 'tickstore_lib' in metafunc.fixturenames:
        metafunc.parametrize("tickstore_lib", ['tickstore'], indirect=True)


@pytest.fixture(scope='function')
def tickstore_lib(arctic, request):
    if request.param == "tickstore":
        store = tickstore
    arctic.initialize_library('test.tickstore', store.TICK_STORE_TYPE)
    return arctic['test.tickstore']


@pytest.fixture(scope='function')
def toplevel_tickstore(arctic):
    arctic.initialize_library('test.toplevel_tickstore', toplevel.TICK_STORE_TYPE)
    return arctic['test.toplevel_tickstore']
