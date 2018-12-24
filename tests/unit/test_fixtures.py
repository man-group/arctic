from mock import Mock

import arctic.fixtures.arctic as fix
from arctic.arctic import Arctic


def test_overlay_library_name(overlay_library_name):
    assert(overlay_library_name == 'test.OVERLAY')


def test_overlay_library():
    a = Mock(Arctic, autospec=True)
    fix._overlay_library(a, 'test')
    a.initialize_library.assert_called_with("test_RAW", "VersionStore", segment='year')


def test_tickstore_lib():
    a = Mock(Arctic, autospec=True)
    fix._tickstore_lib(a, "test")
    a.initialize_library.assert_called_with('test', 'TickStoreV3')
    a.get_library.assert_called_with('test')
