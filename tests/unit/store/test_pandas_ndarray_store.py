from mock import Mock, sentinel, patch
import numpy as np
import pandas as pd
from pytest import raises

from arctic.store._pandas_ndarray_store import PandasStore, \
    PandasDataFrameStore, PandasPanelStore


def test_can_convert_to_records_without_objects_returns_false_on_exception_in_to_records():
    store = PandasStore()
    store.to_records = Mock(side_effect=TypeError('uhoh'))

    with patch('arctic.store._pandas_ndarray_store.log') as mock_log:
        assert store.can_convert_to_records_without_objects(sentinel.df, 'my_symbol') is False

    mock_log.info.assert_called_once_with('Pandas dataframe my_symbol caused exception "TypeError(\'uhoh\',)"'
                                          ' when attempting to convert to records. Saving as Blob.')
    store.to_records.assert_called_once_with(sentinel.df)


def test_can_convert_to_records_without_objects_returns_false_when_records_have_object_dtype():
    store = PandasStore()
    store.to_records = Mock(return_value=np.array(['a', 'b', None, 'd']))

    with patch('arctic.store._pandas_ndarray_store.log') as mock_log:
        assert store.can_convert_to_records_without_objects(sentinel.df, 'my_symbol') is False

    mock_log.info.assert_called_once_with('Pandas dataframe my_symbol contains Objects, saving as Blob')
    store.to_records.assert_called_once_with(sentinel.df)


def test_can_convert_to_records_without_objects_returns_false_when_records_have_arrays_in_them():
    store = PandasStore()
    store.to_records = Mock(return_value=np.rec.array([(1356998400000000000L, ['A', 'BC'])],
                                                      dtype=[('index', '<M8[ns]'), ('values', 'S2', (2,))]))

    with patch('arctic.store._pandas_ndarray_store.log') as mock_log:
        assert store.can_convert_to_records_without_objects(sentinel.df, 'my_symbol') is False

    mock_log.info.assert_called_once_with('Pandas dataframe my_symbol contains >1 dimensional arrays, saving as Blob')
    store.to_records.assert_called_once_with(sentinel.df)


def test_can_convert_to_records_without_objects_returns_true_otherwise():
    store = PandasStore()
    store.to_records = Mock(return_value=np.rec.array([(1356998400000000000L, 'a')],
                                                      dtype=[('index', '<M8[ns]'), ('values', 'S2')]))

    with patch('arctic.store._pandas_ndarray_store.log') as mock_log:
        assert store.can_convert_to_records_without_objects(sentinel.df, 'my_symbol') is True

    assert mock_log.info.call_count == 0
    store.to_records.assert_called_once_with(sentinel.df)


def test_to_records_raises_when_object_dtypes_present():
    store = PandasDataFrameStore()
    df = pd.DataFrame(data=dict(A=['a', 'b', None, 'c'], B=[1., 2., 3., 4.]), index=range(4))
    with raises(TypeError) as e:
        store.to_records(df)

    assert "Cannot change data-type for object array." in str(e)


def test_panel_converted_to_dataframe_and_stacked_to_write():
    store = PandasPanelStore()
    panel = Mock(shape=(1, 2, 3), axes=[Mock(names=['n%d' % i]) for i in range(3)])
    panel.to_frame.return_value.dtypes = [sentinel.dtype]
    with patch.object(PandasDataFrameStore, 'write') as mock_write:
        with patch('arctic.store._pandas_ndarray_store.DataFrame') as DF:
            store.write(sentinel.mlib, sentinel.version, sentinel.symbol, panel, sentinel.prev)
    panel.to_frame.assert_called_with()
    DF.assert_called_with(panel.to_frame.return_value.stack.return_value)
    mock_write.assert_called_with(sentinel.mlib, sentinel.version, sentinel.symbol,
                                  DF.return_value, sentinel.prev)


def test_panel_append_not_supported():
    store = PandasPanelStore()
    panel = Mock(shape=(1, 2, 3), axes=[Mock(names=['n%d' % i]) for i in range(3)], dtypes=['a'])
    with raises(ValueError):
        store.append(sentinel.mlib, sentinel.version, sentinel.symbol, panel, sentinel.prev)


def test_panel_converted_from_dataframe_for_reading():
    store = PandasPanelStore()
    with patch.object(PandasDataFrameStore, 'read') as mock_read:
        res = store.read(sentinel.mlib, sentinel.version, sentinel.symbol)
    mock_read.assert_called_with(sentinel.mlib, sentinel.version, sentinel.symbol)
    assert res == mock_read.return_value.to_panel.return_value


def test_raises_upon_empty_panel_write():
    store = PandasPanelStore()
    panel = Mock(shape=(1, 0, 3))
    with raises(ValueError):
        store.write(sentinel.mlib, sentinel.version, sentinel.symbol, panel, sentinel.prev)
