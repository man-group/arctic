from arctic.store.metadata_store import MetadataStore
from mock import create_autospec, call


def test_ensure_index():
    ms = create_autospec(MetadataStore)
    MetadataStore._ensure_index(ms)
    assert ms.create_index.call_args_list == [call([('symbol', 1), ('start_time', -1)], unique=True, background=True)]
