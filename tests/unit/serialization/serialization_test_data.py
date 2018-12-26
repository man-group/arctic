import numpy as np
import pandas as pd

from arctic.serialization.numpy_records import DataFrameSerializer
from tests.integration.chunkstore.test_utils import create_test_data
from tests.util import get_large_ts

NON_HOMOGENEOUS_DTYPE_PATCH_SIZE_ROWS = 50
_TEST_DATA = None

df_serializer = DataFrameSerializer()


def _mixed_test_data():
    global _TEST_DATA
    if _TEST_DATA is None:
        onerow_ts = get_large_ts(1)
        small_ts = get_large_ts(10)
        medium_ts = get_large_ts(600)
        large_ts = get_large_ts(1800)
        empty_ts = pd.DataFrame()
        empty_index = create_test_data(size=0, cols=10, index=True, multiindex=False, random_data=True, random_ids=True)

        with_some_objects_ts = medium_ts.copy(deep=True)
        with_some_objects_ts.iloc[0:NON_HOMOGENEOUS_DTYPE_PATCH_SIZE_ROWS, 0] = None
        with_some_objects_ts.iloc[0:NON_HOMOGENEOUS_DTYPE_PATCH_SIZE_ROWS, 1] = 'A string'
        large_with_some_objects = create_test_data(size=10000, cols=64, index=True, multiindex=False, random_data=True,
                                                   random_ids=True, use_hours=True)
        large_with_some_objects.iloc[0:NON_HOMOGENEOUS_DTYPE_PATCH_SIZE_ROWS, 0] = None
        large_with_some_objects.iloc[0:NON_HOMOGENEOUS_DTYPE_PATCH_SIZE_ROWS, 1] = 'A string'

        with_string_ts = medium_ts.copy(deep=True)
        with_string_ts['str_col'] = 'abc'
        with_unicode_ts = medium_ts.copy(deep=True)
        with_unicode_ts['ustr_col'] = u'abc'

        with_some_none_ts = medium_ts.copy(deep=True)
        with_some_none_ts.iloc[10:10] = None
        with_some_none_ts.iloc[-10:-10] = np.nan
        with_some_none_ts = with_some_none_ts.replace({np.nan: None})

        # Multi-index data frames
        multiindex_ts = create_test_data(size=500, cols=10, index=True, multiindex=True, random_data=True,
                                         random_ids=True)
        empty_multiindex_ts = create_test_data(size=0, cols=10, index=True, multiindex=True, random_data=True,
                                               random_ids=True)
        large_multi_index = create_test_data(
            size=50000, cols=10, index=True, multiindex=True, random_data=True, random_ids=True, use_hours=True)

        # Multi-column data frames
        columns = pd.MultiIndex.from_product([["bar", "baz", "foo", "qux"], ["one", "two"]], names=["first", "second"])
        empty_multi_column_ts = pd.DataFrame([], columns=columns)

        columns = pd.MultiIndex.from_product([["bar", "baz", "foo", "qux"], ["one", "two"]], names=["first", "second"])
        multi_column_no_multiindex = pd.DataFrame(np.random.randn(2, 8), index=[0, 1], columns=columns)

        large_multi_column = pd.DataFrame(np.random.randn(100000, 8), index=range(100000), columns=columns)

        columns = pd.MultiIndex.from_product([[1, 2, 'a'], ['c', 5]])
        multi_column_int_levels = pd.DataFrame([[9, 2, 8, 1, 2, 3], [3, 4, 2, 9, 10, 11]],
                                               index=['x', 'y'], columns=columns)

        # Multi-index and multi-column data frames
        columns = pd.MultiIndex.from_product([["bar", "baz", "foo", "qux"], ["one", "two"]])
        index = pd.MultiIndex.from_product([["x", "y", "z"], ["a", "b"]])
        multi_column_and_multi_index = pd.DataFrame(np.random.randn(6, 8), index=index, columns=columns)

        # Nested n-dimensional
        def _new_np_nd_array(val):
            return np.rec.array([(val, ['A', 'BC'])],
                                dtype=[('index', '<M8[ns]'), ('values', 'S2', (2,))])
        n_dimensional_df = pd.DataFrame(
            {'a': [_new_np_nd_array(1356998400000000000), _new_np_nd_array(1356998400000000001)],
             'b': [_new_np_nd_array(1356998400000000002), _new_np_nd_array(1356998400000000003)]
             },
            index=(0, 1))

        # With mixed types (i.e. string / numbers) in multi-index
        input_dict = {'POSITION': {
            (pd.Timestamp('2013-10-07 15:45:43'), 'MYSTRT', 'SYMA', 'XX', 0): 0.0,
            (pd.Timestamp('2013-10-07 15:45:43'), 'MYSTRT', 'SYMA', 'FFL', '201312'): -558.0,
            (pd.Timestamp('2013-10-07 15:45:43'), 'MYSTRT', 'AG', 'FFL', '201312'): -74.0,
            (pd.Timestamp('2013-10-07 15:45:43'), 'MYSTRT', 'AG', 'XX', 0): 0.0}
        }
        multi_index_with_object = pd.DataFrame.from_dict(input_dict)

        # Exhaust all dtypes
        mixed_dtypes_df = pd.DataFrame({
            'string': list('abc'),
            'int64': list(range(1, 4)),
            'uint8': np.arange(3, 6).astype('u1'),
            'uint64': np.arange(3, 6).astype('u8'),
            'float64': np.arange(4.0, 7.0),
            'bool1': [True, False, True],
            'dates': pd.date_range('now', periods=3).values,
            'other_dates': pd.date_range('20130101', periods=3).values,
            # 'category': pd.Series(list("ABC")).astype('category'),
            'tz_aware_dates': pd.date_range('20130101', periods=3, tz='US/Eastern'),
            'complex': np.array([1. + 4.j, 2. + 5.j, 3. + 6.j])
        })
        mixed_dtypes_df['timedeltas'] = mixed_dtypes_df.dates.diff()

        # Multi-column with some objects
        multi_column_with_some_objects = multi_column_no_multiindex.copy()
        multi_column_with_some_objects.iloc[1:, 1:2] = 'Convert this columnt dtype to object'

        # Index with timezone-aware datetime
        index_tz_aware = pd.DataFrame(data={'colA': range(10),
                                            'colB': pd.date_range('20130101', periods=10, tz='US/Eastern')},
                                      index=pd.date_range('20130101', periods=10, tz='US/Eastern'))
        index_tz_aware.index.name = 'index'

        _TEST_DATA = {
            'onerow': (onerow_ts, df_serializer.serialize(onerow_ts),
                       df_serializer.can_convert_to_records_without_objects(small_ts, 'symA')),
            'small': (small_ts, df_serializer.serialize(small_ts),
                      df_serializer.can_convert_to_records_without_objects(small_ts, 'symA')),
            'medium': (medium_ts, df_serializer.serialize(medium_ts),
                       df_serializer.can_convert_to_records_without_objects(medium_ts, 'symA')),
            'large': (large_ts, df_serializer.serialize(large_ts),
                      df_serializer.can_convert_to_records_without_objects(large_ts, 'symA')),
            'empty': (empty_ts, df_serializer.serialize(empty_ts),
                      df_serializer.can_convert_to_records_without_objects(empty_ts, 'symA')),
            'empty_index': (empty_index, df_serializer.serialize(empty_index),
                            df_serializer.can_convert_to_records_without_objects(empty_index, 'symA')),
            'with_some_objects': (with_some_objects_ts, df_serializer.serialize(with_some_objects_ts),
                                  df_serializer.can_convert_to_records_without_objects(with_some_objects_ts, 'symA')),
            'large_with_some_objects': (
                large_with_some_objects, df_serializer.serialize(large_with_some_objects),
                df_serializer.can_convert_to_records_without_objects(large_with_some_objects, 'symA')),
            'with_string': (with_string_ts, df_serializer.serialize(with_string_ts),
                            df_serializer.can_convert_to_records_without_objects(with_string_ts, 'symA')),
            'with_unicode': (with_unicode_ts, df_serializer.serialize(with_unicode_ts),
                             df_serializer.can_convert_to_records_without_objects(with_unicode_ts, 'symA')),
            'with_some_none': (with_some_none_ts, df_serializer.serialize(with_some_none_ts),
                               df_serializer.can_convert_to_records_without_objects(with_some_none_ts, 'symA')),
            'multiindex': (multiindex_ts, df_serializer.serialize(multiindex_ts),
                           df_serializer.can_convert_to_records_without_objects(multiindex_ts, 'symA')),
            'multiindex_with_object': (
                multi_index_with_object, df_serializer.serialize(multi_index_with_object),
                df_serializer.can_convert_to_records_without_objects(multi_index_with_object, 'symA')),
            'empty_multiindex': (empty_multiindex_ts, df_serializer.serialize(empty_multiindex_ts),
                                 df_serializer.can_convert_to_records_without_objects(empty_multiindex_ts, 'symA')),
            'large_multi_index': (large_multi_index, df_serializer.serialize(large_multi_index),
                                  df_serializer.can_convert_to_records_without_objects(large_multi_index, 'symA')),
            'empty_multicolumn': (empty_multi_column_ts, df_serializer.serialize(empty_multi_column_ts),
                                  df_serializer.can_convert_to_records_without_objects(empty_multi_column_ts, 'symA')),
            'multi_column_no_multiindex': (
                multi_column_no_multiindex, df_serializer.serialize(multi_column_no_multiindex),
                df_serializer.can_convert_to_records_without_objects(multi_column_no_multiindex, 'symA')),
            'large_multi_column': (large_multi_column, df_serializer.serialize(large_multi_column),
                                   df_serializer.can_convert_to_records_without_objects(large_multi_column, 'symA')),
            'multi_column_int_levels': (
                multi_column_int_levels, df_serializer.serialize(multi_column_int_levels),
                df_serializer.can_convert_to_records_without_objects(multi_column_int_levels, 'symA')),
            'multi_column_and_multi_index': (
                multi_column_and_multi_index, df_serializer.serialize(multi_column_and_multi_index),
                df_serializer.can_convert_to_records_without_objects(multi_column_and_multi_index, 'symA')),
            'multi_column_with_some_objects': (
                multi_column_with_some_objects, df_serializer.serialize(multi_column_with_some_objects),
                df_serializer.can_convert_to_records_without_objects(multi_column_with_some_objects, 'symA')),
            'n_dimensional_df': (n_dimensional_df, Exception, None),
            'mixed_dtypes_df': (mixed_dtypes_df, df_serializer.serialize(mixed_dtypes_df),
                                df_serializer.can_convert_to_records_without_objects(mixed_dtypes_df, 'symA')),
            'index_tz_aware': (index_tz_aware, df_serializer.serialize(index_tz_aware),
                               df_serializer.can_convert_to_records_without_objects(index_tz_aware, 'symA'))
        }
    return _TEST_DATA


def is_test_data_serializable(input_df_descr):
    return _mixed_test_data()[input_df_descr][2]
