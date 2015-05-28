from arctic.arctic import Arctic
from arctic.store.version_store import VersionStore


def test_arctic(arctic):
    assert isinstance(arctic, Arctic)


def test_library(library):
    assert isinstance(library, VersionStore)
