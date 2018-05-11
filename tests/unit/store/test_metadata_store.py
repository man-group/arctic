import datetime as dt

from arctic.store.metadata_store import MetadataStore
from mock import create_autospec, call


def test_ensure_index():
    ms = create_autospec(MetadataStore)
    MetadataStore._ensure_index(ms)
    assert ms.create_index.call_args_list == [call([('symbol', 1),
                                                    ('start_time', -1)],
                                                   unique=True,
                                                   background=True)]


def test_list_symbols_simple():
    ms = create_autospec(MetadataStore)
    ms.distinct.return_value = []

    MetadataStore.list_symbols(ms)
    ms.distinct.assert_called_once_with('symbol')


def test_list_symbols_regex():
    ms = create_autospec(MetadataStore)
    ms.aggregate.return_value = []

    expected_pipeline = [
        {'$sort': {'symbol': 1, 'start_time': -1}},
        {'$match': {'symbol': {'$regex': 'test.*'}}},
        {'$group': {'_id': '$symbol', 'metadata': {'$first': '$metadata'}}},
        {'$project': {'_id': 0, 'symbol':  '$_id'}}
    ]

    MetadataStore.list_symbols(ms, regex='test.*')
    ms.aggregate.assert_called_once_with(expected_pipeline)


def test_list_symbols_as_of():
    ms = create_autospec(MetadataStore)
    ms.aggregate.return_value = []

    expected_pipeline = [
        {'$sort': {'symbol': 1, 'start_time': -1}},
        {'$match': {'symbol': {'$regex': '^'},
                    'start_time': {'$lte': dt.datetime(2018, 5, 11)}}},
        {'$group': {'_id': '$symbol', 'metadata': {'$first': '$metadata'}}},
        {'$project': {'_id': 0, 'symbol':  '$_id'}}
    ]

    MetadataStore.list_symbols(ms, as_of=dt.datetime(2018, 5, 11))
    ms.aggregate.assert_called_once_with(expected_pipeline)


def test_list_symbols_as_of_regex():
    ms = create_autospec(MetadataStore)
    ms.aggregate.return_value = []

    expected_pipeline = [
        {'$sort': {'symbol': 1, 'start_time': -1}},
        {'$match': {'symbol': {'$regex': 'test.*'},
                    'start_time': {'$lte': dt.datetime(2018, 5, 11)}}},
        {'$group': {'_id': '$symbol', 'metadata': {'$first': '$metadata'}}},
        {'$project': {'_id': 0, 'symbol':  '$_id'}}
    ]

    MetadataStore.list_symbols(ms,
                               regex='test.*',
                               as_of=dt.datetime(2018, 5, 11))
    ms.aggregate.assert_called_once_with(expected_pipeline)


def test_list_symbols_metadata_query():
    ms = create_autospec(MetadataStore)
    ms.aggregate.return_value = []

    expected_pipeline = [
        {'$sort': {'symbol': 1, 'start_time': -1}},
        {'$group': {'_id': '$symbol', 'metadata': {'$first': '$metadata'}}},
        {'$match': {'metadata.foo': 'bar'}},
        {'$project': {'_id': 0, 'symbol':  '$_id'}}
    ]

    MetadataStore.list_symbols(ms, foo='bar')
    ms.aggregate.assert_called_once_with(expected_pipeline)


def test_list_symbols_all_options():
    ms = create_autospec(MetadataStore)
    ms.aggregate.return_value = []

    expected_pipeline = [
        {'$sort': {'symbol': 1, 'start_time': -1}},
        {'$match': {'symbol': {'$regex': 'test.*'},
                    'start_time': {'$lte': dt.datetime(2018, 5, 11)}}},
        {'$group': {'_id': '$symbol', 'metadata': {'$first': '$metadata'}}},
        {'$match': {'metadata.foo': 'bar'}},
        {'$project': {'_id': 0, 'symbol':  '$_id'}}
    ]

    MetadataStore.list_symbols(ms,
                               regex='test.*',
                               as_of=dt.datetime(2018, 5, 11),
                               foo='bar')
    ms.aggregate.assert_called_once_with(expected_pipeline)