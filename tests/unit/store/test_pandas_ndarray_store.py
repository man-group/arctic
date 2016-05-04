from mock import Mock, sentinel, patch
from pandas.util.testing import assert_frame_equal
from pytest import raises

from arctic.store._pandas_ndarray_store import PandasStore, \
    PandasDataFrameStore, PandasPanelStore
import numpy as np
import pandas as pd
from tests.util import read_str_as_pandas


def test_panel_converted_to_dataframe_and_stacked_to_write():
    store = PandasPanelStore()
    panel = Mock(shape=(1, 2, 3), axes=[Mock(names=['n%d' % i]) for i in range(3)])
    panel.to_frame.return_value.dtypes = [sentinel.dtype]
    with patch.object(PandasDataFrameStore, 'write') as mock_write:
        with patch('arctic.store._pandas_ndarray_store.DataFrame') as DF:
            store.write(sentinel.mlib, sentinel.version, sentinel.symbol, panel, sentinel.prev)
    panel.to_frame.assert_called_with(filter_observations=False)
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
    record = store.SERIALIZER.serialize(df)[0]

    # now take away timezone info from metadata
    record = np.array(record.tolist(), dtype=np.dtype([('index 1', '<M8[ns]'), ('index 2', '<M8[ns]'), ('SPAM', '<f8')],
                                                      metadata={'index': ['index 1', 'index 2'], 'columns': ['SPAM']}))
    assert store.SERIALIZER._index_from_records(record).equals(df.index)
