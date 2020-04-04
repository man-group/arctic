import numpy as np
import pandas as pd
import pytest
from mock import patch, Mock, sentinel
from numpy.testing import assert_array_equal
from pandas import Timestamp

import arctic.serialization.numpy_records as anr


class FastCheckSerializable(object):
    def __init__(self, enabled):
        self.enabled = bool(enabled)
        self.orig_setting = None

    def __enter__(self):
        self.orig_setting = anr.FAST_CHECK_DF_SERIALIZABLE
        anr.set_fast_check_df_serializable(self.enabled)

    def __exit__(self, *args):
        anr.set_fast_check_df_serializable(self.orig_setting)


def test_to_primitive_timestamps():
    arr = anr._to_primitive(np.array([Timestamp('2010-11-12 00:00:00')]))
    assert_array_equal(arr, np.array([Timestamp('2010-11-12 00:00:00').value], dtype='datetime64[ns]'))


def test_to_primitive_fixed_length_strings():
    mydf = pd.DataFrame({'a': ['abc', u'xyz', '']})
    primitives_arr = anr._to_primitive(np.array(mydf.a.values), string_max_len=32)
    assert_array_equal(primitives_arr, np.array([u'abc', u'xyz', u''], dtype='U32'))
    assert primitives_arr.dtype == np.dtype('U32')


@pytest.mark.parametrize("fast_serializable_check", (True, False))
def test_can_convert_to_records_without_objects_returns_false_on_exception_in_to_records(fast_serializable_check):
    with FastCheckSerializable(fast_serializable_check):
        store = anr.PandasSerializer()
        mymock = Mock(side_effect=TypeError('uhoh'))
        if fast_serializable_check:
            store.fast_check_serializable = mymock
        else:
            store._to_records = mymock
        with patch('arctic.serialization.numpy_records.log') as mock_log:
            assert store.can_convert_to_records_without_objects(sentinel.df, 'my_symbol') is False

        assert 'Pandas dataframe my_symbol caused exception' in str(mock_log.warning.call_args)
        if fast_serializable_check:
            store.fast_check_serializable.assert_called_once_with(sentinel.df)
        else:
            store._to_records.assert_called_once_with(sentinel.df)


@pytest.mark.parametrize("fast_serializable_check", (True, False))
def test_can_convert_to_records_without_objects_returns_false_when_records_have_object_dtype(fast_serializable_check):
    with FastCheckSerializable(fast_serializable_check):
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


@pytest.mark.parametrize("fast_serializable_check", (True, False))
def test_can_convert_to_records_without_objects_returns_false_when_records_have_arrays_in_them(fast_serializable_check):
    with FastCheckSerializable(fast_serializable_check):
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


@pytest.mark.parametrize("fast_serializable_check", (True, False))
def test_can_convert_to_records_without_objects_returns_true_otherwise(fast_serializable_check):
    with FastCheckSerializable(fast_serializable_check):
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


@pytest.mark.parametrize("fast_serializable_check", (False, True))
def test_can_convert_to_records_mixed_object_column_string_nan(fast_serializable_check):
    with FastCheckSerializable(fast_serializable_check):
        serializer = anr.DataFrameSerializer()

        df = pd.DataFrame({'a': [1, 3, 4], 'b': [1.2, 8.0, 0.2]})
        assert serializer.can_convert_to_records_without_objects(df, 'my_symbol')

        df = pd.DataFrame({'a': [1, 3, 4], 'b': [1, 8.0, 2]})
        assert serializer.can_convert_to_records_without_objects(df, 'my_symbol')

        df = pd.DataFrame({'a': [1, 3, 4], 'b': [1.2, 8.0, np.NaN]})
        assert serializer.can_convert_to_records_without_objects(df, 'my_symbol')

        df = pd.DataFrame({'a': ['abc', 'cde', 'def'], 'b': [1.2, 8.0, np.NaN]})
        assert serializer.can_convert_to_records_without_objects(df, 'my_symbol')

        df = pd.DataFrame({'a': [u'abc', u'cde', 'def'], 'b': [1.2, 8.0, np.NaN]})
        assert serializer.can_convert_to_records_without_objects(df, 'my_symbol')

        df = pd.DataFrame({'a': [u'abc', u'cde', 'def'], 'b': [1.2, '8.0', np.NaN]})
        assert not serializer.can_convert_to_records_without_objects(df, 'my_symbol')

        # Do not serialize and force-stringify None
        df = pd.DataFrame({'a': ['abc', None, 'def'], 'b': [1.2, 8.0, np.NaN]})
        assert not serializer.can_convert_to_records_without_objects(df, 'my_symbol')

        # Do not serialize and force-stringify np.NaN among strings, rather pickle
        df = pd.DataFrame({'a': ['abc', np.NaN, 'def'], 'b': [1.2, 8.0, np.NaN]})
        assert not serializer.can_convert_to_records_without_objects(df, 'my_symbol')
