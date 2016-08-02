import numpy as np

from numpy.testing import assert_array_equal
from mock import patch, Mock, sentinel
from arctic.serialization.numpy_records import PandasSerializer, _to_primitive
from pandas import Timestamp


def test_to_primitive_timestamps():
    arr = _to_primitive(np.array([Timestamp('2010-11-12 00:00:00')]))
    assert_array_equal(arr, np.array([Timestamp('2010-11-12 00:00:00').value], dtype='datetime64[ns]'))

def test_can_convert_to_records_without_objects_returns_false_on_exception_in_to_records():
    store = PandasSerializer()
    store._to_records = Mock(side_effect=TypeError('uhoh'))

    with patch('arctic.serialization.numpy_records.log') as mock_log:
        assert store.can_convert_to_records_without_objects(sentinel.df, 'my_symbol') is False

    mock_log.info.assert_called_once_with('Pandas dataframe my_symbol caused exception "TypeError(\'uhoh\',)"'
                                          ' when attempting to convert to records. Saving as Blob.')
    store._to_records.assert_called_once_with(sentinel.df)


def test_can_convert_to_records_without_objects_returns_false_when_records_have_object_dtype():
    store = PandasSerializer()
    store._to_records = Mock(return_value=(np.array(['a', 'b', None, 'd']), None))

    with patch('arctic.serialization.numpy_records.log') as mock_log:
        assert store.can_convert_to_records_without_objects(sentinel.df, 'my_symbol') is False

    mock_log.info.assert_called_once_with('Pandas dataframe my_symbol contains Objects, saving as Blob')
    store._to_records.assert_called_once_with(sentinel.df)


def test_can_convert_to_records_without_objects_returns_false_when_records_have_arrays_in_them():
    store = PandasSerializer()
    store._to_records = Mock(return_value=(np.rec.array([(1356998400000000000, ['A', 'BC'])],
                                                       dtype=[('index', '<M8[ns]'), ('values', 'S2', (2,))]), None))

    with patch('arctic.serialization.numpy_records.log') as mock_log:
        assert store.can_convert_to_records_without_objects(sentinel.df, 'my_symbol') is False

    mock_log.info.assert_called_once_with('Pandas dataframe my_symbol contains >1 dimensional arrays, saving as Blob')
    store._to_records.assert_called_once_with(sentinel.df)


def test_can_convert_to_records_without_objects_returns_true_otherwise():
    store = PandasSerializer()
    store._to_records = Mock(return_value=(np.rec.array([(1356998400000000000, 'a')],
                                                       dtype=[('index', '<M8[ns]'), ('values', 'S2')]), None))

    with patch('arctic.serialization.numpy_records.log') as mock_log:
        assert store.can_convert_to_records_without_objects(sentinel.df, 'my_symbol') is True

    assert mock_log.info.call_count == 0
    store._to_records.assert_called_once_with(sentinel.df)
