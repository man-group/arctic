from mock import Mock, sentinel, patch
from pandas.util.testing import assert_frame_equal
from pytest import raises

from arctic.store._pandas_ndarray_store import PandasStore, \
    PandasDataFrameStore, PandasPanelStore
import numpy as np
import pandas as pd
from tests.util import read_str_as_pandas


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
    store.to_records = Mock(return_value=(np.array(['a', 'b', None, 'd']), None))

    with patch('arctic.store._pandas_ndarray_store.log') as mock_log:
        assert store.can_convert_to_records_without_objects(sentinel.df, 'my_symbol') is False

    mock_log.info.assert_called_once_with('Pandas dataframe my_symbol contains Objects, saving as Blob')
    store.to_records.assert_called_once_with(sentinel.df)


def test_can_convert_to_records_without_objects_returns_false_when_records_have_arrays_in_them():
    store = PandasStore()
    store.to_records = Mock(return_value=(np.rec.array([(1356998400000000000L, ['A', 'BC'])],
                                                       dtype=[('index', '<M8[ns]'), ('values', 'S2', (2,))]), None))

    with patch('arctic.store._pandas_ndarray_store.log') as mock_log:
        assert store.can_convert_to_records_without_objects(sentinel.df, 'my_symbol') is False

    mock_log.info.assert_called_once_with('Pandas dataframe my_symbol contains >1 dimensional arrays, saving as Blob')
    store.to_records.assert_called_once_with(sentinel.df)


def test_can_convert_to_records_without_objects_returns_true_otherwise():
    store = PandasStore()
    store.to_records = Mock(return_value=(np.rec.array([(1356998400000000000L, 'a')],
                                                       dtype=[('index', '<M8[ns]'), ('values', 'S2')]), None))

    with patch('arctic.store._pandas_ndarray_store.log') as mock_log:
        assert store.can_convert_to_records_without_objects(sentinel.df, 'my_symbol') is True

    assert mock_log.info.call_count == 0
    store.to_records.assert_called_once_with(sentinel.df)


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


def test_read_multi_index_with_no_ts_info():
    # github #81: old multi-index ts would not have tz info in metadata. Ensure read is not broken
    df = read_str_as_pandas("""index 1 |    index 2 | SPAM
                            2012-09-08 | 2015-01-01 |  1.0
                            2012-09-09 | 2015-01-02 |  1.1
                            2012-10-08 | 2015-01-03 |  2.0""", num_index=2)
    store = PandasDataFrameStore()
    record = store.to_records(df)[0]

    # now take away timezone info from metadata
    record = np.array(record.tolist(), dtype=np.dtype([('index 1', '<M8[ns]'), ('index 2', '<M8[ns]'), ('SPAM', '<f8')],
                                                      metadata={'index': ['index 1', 'index 2'], 'columns': ['SPAM']}))
    assert store._index_from_records(record).equals(df.index)
