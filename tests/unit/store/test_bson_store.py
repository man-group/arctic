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
        BSONStore.initialize_library(arctic_lib, hashed=True)
        BSONStore.initialize_library(arctic_lib, hashed=False)
        # Check we always set the sharding to be hashed, regarless of user input
        assert enable_sharding.call_args_list == [call(arctic_lib.arctic, arctic_lib.get_name(), hashed=True, key='_id'),
                                                  call(arctic_lib.arctic, arctic_lib.get_name(), hashed=True, key='_id')]


def test_find():
    arctic_lib = create_autospec(ArcticLibraryBinding, instance=True)
    collection = create_autospec(Collection, instance=True)
    collection.find.return_value = (doc for doc in [sentinel.document])
    arctic_lib.get_top_level_collection.return_value = collection

    bsons = BSONStore(arctic_lib)

    assert list(bsons.find(sentinel.filter)) == [sentinel.document]
    assert collection.find.call_count == 1
    assert collection.find.call_args_list == [call(sentinel.filter)]


def test_insert_one():
    arctic_lib = create_autospec(ArcticLibraryBinding, instance=True)
    collection = create_autospec(Collection, instance=True)
    arctic_lib.get_top_level_collection.return_value = collection

    bsons = BSONStore(arctic_lib)
    bsons.insert_one(sentinel.document)

    assert arctic_lib.check_quota.call_count == 1
    assert collection.insert_one.call_count == 1
    assert collection.insert_one.call_args_list == [call(sentinel.document)]


def test_insert_many():
    arctic_lib = create_autospec(ArcticLibraryBinding, instance=True)
    collection = create_autospec(Collection, instance=True)
    arctic_lib.get_top_level_collection.return_value = collection

    bsons = BSONStore(arctic_lib)
    bsons.insert_many(sentinel.documents)

    assert arctic_lib.check_quota.call_count == 1
    assert collection.insert_many.call_count == 1
    assert collection.insert_many.call_args_list == [call(sentinel.documents)]


def test_replace_one():
    arctic_lib = create_autospec(ArcticLibraryBinding, instance=True)
    collection = create_autospec(Collection, instance=True)
    arctic_lib.get_top_level_collection.return_value = collection

    bsons = BSONStore(arctic_lib)
    bsons.replace_one(sentinel.filter, sentinel.replacement)

    assert arctic_lib.check_quota.call_count == 1
    assert collection.replace_one.call_count == 1
    assert collection.replace_one.call_args_list == [call(sentinel.filter, sentinel.replacement)]


def test_update_one():
    arctic_lib = create_autospec(ArcticLibraryBinding, instance=True)
    collection = create_autospec(Collection, instance=True)
    arctic_lib.get_top_level_collection.return_value = collection

    bsons = BSONStore(arctic_lib)
    bsons.update_one(sentinel.filter, sentinel.replacement)

    assert arctic_lib.check_quota.call_count == 1
    assert collection.update_one.call_count == 1
    assert collection.update_one.call_args_list == [call(sentinel.filter, sentinel.replacement)]


def test_update_many():
    arctic_lib = create_autospec(ArcticLibraryBinding, instance=True)
    collection = create_autospec(Collection, instance=True)
    arctic_lib.get_top_level_collection.return_value = collection

    bsons = BSONStore(arctic_lib)
    bsons.update_many(sentinel.filter, sentinel.replacements)

    assert arctic_lib.check_quota.call_count == 1
    assert collection.update_many.call_count == 1
    assert collection.update_many.call_args_list == [call(sentinel.filter, sentinel.replacements)]


def test_find_one_and_replace():
    arctic_lib = create_autospec(ArcticLibraryBinding, instance=True)
    collection = create_autospec(Collection, instance=True)
    arctic_lib.get_top_level_collection.return_value = collection

    bsons = BSONStore(arctic_lib)
    bsons.find_one_and_replace(sentinel.filter, sentinel.replacement)

    assert arctic_lib.check_quota.call_count == 1
    assert collection.find_one_and_replace.call_count == 1
    assert collection.find_one_and_replace.call_args_list == [call(sentinel.filter, sentinel.replacement)]


def test_bulk_write():
    arctic_lib = create_autospec(ArcticLibraryBinding, instance=True)
    collection = create_autospec(Collection, instance=True)
    arctic_lib.get_top_level_collection.return_value = collection

    bsons = BSONStore(arctic_lib)
    bsons.bulk_write(sentinel.requests)

    assert arctic_lib.check_quota.call_count == 1
    assert collection.bulk_write.call_count == 1
    assert collection.bulk_write.call_args_list == [call(sentinel.requests)]


def test_delete_one():
    arctic_lib = create_autospec(ArcticLibraryBinding, instance=True)
    collection = create_autospec(Collection, instance=True)
    arctic_lib.get_top_level_collection.return_value = collection

    bsons = BSONStore(arctic_lib)
    bsons.delete_one(sentinel.filter)

    assert collection.delete_one.call_count == 1
    assert collection.delete_one.call_args_list == [call(sentinel.filter)]


def test_count():
    arctic_lib = create_autospec(ArcticLibraryBinding, instance=True)
    collection = create_autospec(Collection, instance=True)
    arctic_lib.get_top_level_collection.return_value = collection

    bsons = BSONStore(arctic_lib)
    bsons.count(sentinel.filter)

    assert collection.count.call_count == 1
    assert collection.count.call_args_list == [call(sentinel.filter)]


def test_distinct():
    arctic_lib = create_autospec(ArcticLibraryBinding, instance=True)
    collection = create_autospec(Collection, instance=True)
    arctic_lib.get_top_level_collection.return_value = collection

    bsons = BSONStore(arctic_lib)
    bsons.distinct(sentinel.key)

    assert collection.distinct.call_count == 1
    assert collection.distinct.call_args_list == [call(sentinel.key)]


def test_delete_many():
    arctic_lib = create_autospec(ArcticLibraryBinding, instance=True)
    collection = create_autospec(Collection, instance=True)
    arctic_lib.get_top_level_collection.return_value = collection

    bsons = BSONStore(arctic_lib)
    bsons.delete_many(sentinel.filter)

    assert collection.delete_many.call_count == 1
    assert collection.delete_many.call_args_list == [call(sentinel.filter)]


def test_create_index():
    arctic_lib = create_autospec(ArcticLibraryBinding, instance=True)
    collection = create_autospec(Collection, instance=True)
    arctic_lib.get_top_level_collection.return_value = collection

    bsons = BSONStore(arctic_lib)
    bsons.create_index([(sentinel.path1, sentinel.order1), (sentinel.path2, sentinel.path2)])

    assert collection.create_index.call_count == 1
    assert collection.create_index.call_args_list == [call([(sentinel.path1, sentinel.order1), (sentinel.path2, sentinel.path2)])]


def test_drop_index():
    arctic_lib = create_autospec(ArcticLibraryBinding, instance=True)
    collection = create_autospec(Collection, instance=True)
    arctic_lib.get_top_level_collection.return_value = collection

    bsons = BSONStore(arctic_lib)
    bsons.drop_index(sentinel.name)

    assert collection.drop_index.call_count == 1
    assert collection.drop_index.call_args_list == [call(sentinel.name)]


def test_index_information():
    arctic_lib = create_autospec(ArcticLibraryBinding, instance=True)
    collection = create_autospec(Collection, instance=True)
    arctic_lib.get_top_level_collection.return_value = collection

    bsons = BSONStore(arctic_lib)
    bsons.index_information()

    assert collection.index_information.call_count == 1
