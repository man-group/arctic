from arctic.arctic import Arctic
from arctic.store.version_store import VersionStore
from arctic.store.metadata_store import MetadataStore


def test_arctic(arctic):
    assert isinstance(arctic, Arctic)


def test_library(library):
    assert isinstance(library, VersionStore)
    assert library._arctic_lib.get_library_type() == 'VersionStore'


def test_ms_lib(ms_lib):
    assert isinstance(ms_lib, MetadataStore)
    assert ms_lib._arctic_lib.get_library_type() == 'MetadataStore'
