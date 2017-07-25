from arctic.store.metadata_store import MetadataStore
from arctic.arctic import ArcticLibraryBinding
from pymongo.collection import Collection
from mock import Mock, sentinel, create_autospec, call


def test_ensure_index():
    ms = create_autospec(MetadataStore)
    MetadataStore._ensure_index(ms)
    assert ms.create_index.call_args_list == [call([('symbol', 1), ('start_time', -1)], unique=True, background=True)]


def test_find_one():
    arctic_lib = create_autospec(ArcticLibraryBinding, instance=True)
    collection = create_autospec(Collection, instance=True)
    collection.find_one.return_value = sentinel.document
    arctic_lib.get_top_level_collection.return_value = Mock(metadata=collection)

    ms = MetadataStore(arctic_lib)

    assert ms.find_one(sentinel.filter) == sentinel.document
    assert collection.find_one.call_count == 1
    assert collection.find_one.call_args_list == [call(sentinel.filter)]


def test_find_one_and_update():
    arctic_lib = create_autospec(ArcticLibraryBinding, instance=True)
    collection = create_autospec(Collection, instance=True)
    arctic_lib.get_top_level_collection.return_value = Mock(metadata=collection)

    ms = MetadataStore(arctic_lib)
    ms.find_one_and_update(sentinel.filter, sentinel.update)

    assert arctic_lib.check_quota.call_count == 1
    assert collection.find_one_and_update.call_count == 1
    assert collection.find_one_and_update.call_args_list == [call(sentinel.filter, sentinel.update)]


def test_find_one_and_delete():
    arctic_lib = create_autospec(ArcticLibraryBinding, instance=True)
    collection = create_autospec(Collection, instance=True)
    arctic_lib.get_top_level_collection.return_value = Mock(metadata=collection)

    ms = MetadataStore(arctic_lib)
    ms.find_one_and_delete(sentinel.filter)

    assert collection.find_one_and_delete.call_count == 1
    assert collection.find_one_and_delete.call_args_list == [call(sentinel.filter)]
