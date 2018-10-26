import numpy as np
import pytest
from mock import patch, Mock, sentinel
from numpy.testing import assert_array_equal
from pandas import Timestamp

import arctic.serialization.numpy_records as anr


def test_to_primitive_timestamps():
    arr = anr._to_primitive(np.array([Timestamp('2010-11-12 00:00:00')]))
    assert_array_equal(arr, np.array([Timestamp('2010-11-12 00:00:00').value], dtype='datetime64[ns]'))


@pytest.mark.parametrize("fast_serializable_check", (True, False))
def test_can_convert_to_records_without_objects_returns_false_on_exception_in_to_records(fast_serializable_check):
    orig_config = anr._FAST_CHECK_DF_SERIALIZABLE
    try:
        anr.set_fast_check_df_serializable(fast_serializable_check)
        store = anr.PandasSerializer()
        mymock = Mock(side_effect=TypeError('uhoh'))
        if fast_serializable_check:
            store.fast_check_serializable = mymock
        else:
            store._to_records = mymock
        with patch('arctic.serialization.numpy_records.log') as mock_log:
            assert store.can_convert_to_records_without_objects(sentinel.df, 'my_symbol') is False

        mock_log.warning.assert_called_once_with('Pandas dataframe my_symbol caused exception "TypeError(\'uhoh\',)" '
                                                 'when attempting to convert to records. Saving as Blob.')
        if fast_serializable_check:
            store.fast_check_serializable.assert_called_once_with(sentinel.df)
        else:
            store._to_records.assert_called_once_with(sentinel.df)
    finally:
        anr._FAST_CHECK_DF_SERIALIZABLE = orig_config


@pytest.mark.parametrize("fast_serializable_check", (True, False))
def test_can_convert_to_records_without_objects_returns_false_when_records_have_object_dtype(fast_serializable_check):
    orig_config = anr._FAST_CHECK_DF_SERIALIZABLE
    try:
        anr.set_fast_check_df_serializable(fast_serializable_check)
        store = anr.PandasSerializer()
        mymock = Mock(return_value=(np.array(['a', 'b', None, 'd']), None))
        if fast_serializable_check:
            store.fast_check_serializable = mymock
        else:
            store._to_records = mymock
        with patch('arctic.serialization.numpy_records.log') as mock_log:
            assert store.can_convert_to_records_without_objects(sentinel.df, 'my_symbol') is False
        mock_log.warning.assert_called_once_with('Pandas dataframe my_symbol contains Objects, saving as Blob')
        if fast_serializable_check:
            store.fast_check_serializable.assert_called_once_with(sentinel.df)
        else:
            store._to_records.assert_called_once_with(sentinel.df)
    finally:
        anr._FAST_CHECK_DF_SERIALIZABLE = orig_config


@pytest.mark.parametrize("fast_serializable_check", (True, False))
def test_can_convert_to_records_without_objects_returns_false_when_records_have_arrays_in_them(fast_serializable_check):
    orig_config = anr._FAST_CHECK_DF_SERIALIZABLE
    try:
        anr.set_fast_check_df_serializable(fast_serializable_check)
        store = anr.PandasSerializer()
        mymock = Mock(return_value=(np.rec.array([(1356998400000000000, ['A', 'BC'])], dtype=[('index', '<M8[ns]'), ('values', 'S2', (2,))]), None))
        if fast_serializable_check:
            store.fast_check_serializable = mymock
        else:
            store._to_records = mymock
        with patch('arctic.serialization.numpy_records.log') as mock_log:
            assert store.can_convert_to_records_without_objects(sentinel.df, 'my_symbol') is False
        mock_log.warning.assert_called_once_with('Pandas dataframe my_symbol contains >1 dimensional arrays, saving as Blob')
        if fast_serializable_check:
            store.fast_check_serializable.assert_called_once_with(sentinel.df)
        else:
            store._to_records.assert_called_once_with(sentinel.df)
    finally:
        anr._FAST_CHECK_DF_SERIALIZABLE = orig_config


@pytest.mark.parametrize("fast_serializable_check", (True, False))
def test_can_convert_to_records_without_objects_returns_true_otherwise(fast_serializable_check):
    orig_config = anr._FAST_CHECK_DF_SERIALIZABLE
    try:
        anr.set_fast_check_df_serializable(fast_serializable_check)
        store = anr.PandasSerializer()
        mymock = Mock(return_value=(np.rec.array([(1356998400000000000, 'a')], dtype=[('index', '<M8[ns]'), ('values', 'S2')]), None))
        if fast_serializable_check:
            store.fast_check_serializable = mymock
        else:
            store._to_records = mymock
        with patch('arctic.serialization.numpy_records.log') as mock_log:
            assert store.can_convert_to_records_without_objects(sentinel.df, 'my_symbol') is True
        assert mock_log.warning.call_count == 0
        if fast_serializable_check:
            store.fast_check_serializable.assert_called_once_with(sentinel.df)
        else:
            store._to_records.assert_called_once_with(sentinel.df)
    finally:
        anr._FAST_CHECK_DF_SERIALIZABLE = orig_config
