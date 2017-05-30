from arctic.store.bson_store import BSONStore
from arctic.arctic import ArcticLibraryBinding
from arctic import Arctic
from pymongo.collection import Collection
from mock import sentinel, create_autospec, patch, call


def test_initialize_library():
    arctic_lib = create_autospec(ArcticLibraryBinding)
    arctic_lib.arctic = create_autospec(Arctic)
    with patch('arctic.store.bson_store.enable_sharding', autospec=True) as enable_sharding:
        arctic_lib.get_top_level_collection.return_value.database.create_collection.__name__ = 'some_name'
        arctic_lib.get_top_level_collection.return_value.database.collection_names.__name__ = 'some_name'
        BSONStore.initialize_library(arctic_lib, hashed=sentinel.hashed)
        assert enable_sharding.call_args_list == [call(arctic_lib.arctic, arctic_lib.get_name(), hashed=sentinel.hashed)]


def test_find():
    arctic_lib = create_autospec(ArcticLibraryBinding, instance=True)
    collection = create_autospec(Collection, instance=True)
    collection.find.return_value = (doc for doc in [sentinel.document])
    arctic_lib.get_top_level_collection.return_value = collection

    bsons = BSONStore(arctic_lib)

    assert list(bsons.find(sentinel.filter)) == [sentinel.document]
    assert collection.find.call_count == 1


def test_insert_one():
    arctic_lib = create_autospec(ArcticLibraryBinding, instance=True)
    collection = create_autospec(Collection, instance=True)
    arctic_lib.get_top_level_collection.return_value = collection

    bsons = BSONStore(arctic_lib)
    bsons.insert_one(sentinel.entry)

    assert arctic_lib.check_quota.call_count == 1
    assert collection.insert_one.call_count == 1


def test_insert_many():
    arctic_lib = create_autospec(ArcticLibraryBinding, instance=True)
    collection = create_autospec(Collection, instance=True)
    arctic_lib.get_top_level_collection.return_value = collection

    bsons = BSONStore(arctic_lib)
    bsons.insert_many(sentinel.entries)

    assert arctic_lib.check_quota.call_count == 1
    assert collection.insert_many.call_count == 1


def test_delete_one():
    arctic_lib = create_autospec(ArcticLibraryBinding, instance=True)
    collection = create_autospec(Collection, instance=True)
    arctic_lib.get_top_level_collection.return_value = collection

    bsons = BSONStore(arctic_lib)
    bsons.delete_one(sentinel.query)

    assert collection.delete_one.call_count == 1


def test_delete_many():
    arctic_lib = create_autospec(ArcticLibraryBinding, instance=True)
    collection = create_autospec(Collection, instance=True)
    arctic_lib.get_top_level_collection.return_value = collection

    bsons = BSONStore(arctic_lib)
    bsons.delete_many(sentinel.query)

    assert collection.delete_many.call_count == 1


def test_create_index():
    arctic_lib = create_autospec(ArcticLibraryBinding, instance=True)
    collection = create_autospec(Collection, instance=True)
    arctic_lib.get_top_level_collection.return_value = collection

    bsons = BSONStore(arctic_lib)
    bsons.create_index([(sentinel.path1, sentinel.order1), (sentinel.path2, sentinel.path2)])

    assert collection.create_index.call_count == 1


def test_drop_index():
    arctic_lib = create_autospec(ArcticLibraryBinding, instance=True)
    collection = create_autospec(Collection, instance=True)
    arctic_lib.get_top_level_collection.return_value = collection

    bsons = BSONStore(arctic_lib)
    bsons.drop_index(sentinel.name)

    assert collection.drop_index.call_count == 1


def test_index_information():
    arctic_lib = create_autospec(ArcticLibraryBinding, instance=True)
    collection = create_autospec(Collection, instance=True)
    arctic_lib.get_top_level_collection.return_value = collection

    bsons = BSONStore(arctic_lib)
    bsons.index_information()

    assert collection.index_information.call_count == 1
