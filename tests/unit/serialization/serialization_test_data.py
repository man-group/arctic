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

        _TEST_DATA = {
            'onerow': (onerow_ts, df_serializer.serialize(onerow_ts)),
            'small': (small_ts, df_serializer.serialize(small_ts)),
            'medium': (medium_ts, df_serializer.serialize(medium_ts)),
            'large': (large_ts, df_serializer.serialize(large_ts)),
            'empty': (empty_ts, df_serializer.serialize(empty_ts)),
            'empty_index': (empty_index, df_serializer.serialize(empty_index)),
            'with_some_objects': (with_some_objects_ts, df_serializer.serialize(with_some_objects_ts)),
            'large_with_some_objects': (large_with_some_objects, df_serializer.serialize(large_with_some_objects)),
            'with_string': (with_string_ts, df_serializer.serialize(with_string_ts)),
            'with_unicode': (with_unicode_ts, df_serializer.serialize(with_unicode_ts)),
            'with_some_none': (with_some_none_ts, df_serializer.serialize(with_some_none_ts)),
            'multiindex': (multiindex_ts, df_serializer.serialize(multiindex_ts)),
            'empty_multiindex': (empty_multiindex_ts, df_serializer.serialize(empty_multiindex_ts)),
            'large_multi_index': (large_multi_index, df_serializer.serialize(large_multi_index)),
            'empty_multicolumn': (empty_multi_column_ts, df_serializer.serialize(empty_multi_column_ts)),
            'multi_column_no_multiindex': (multi_column_no_multiindex,
                                           df_serializer.serialize(multi_column_no_multiindex)),
            'large_multi_column': (large_multi_column, df_serializer.serialize(large_multi_column)),
            'multi_column_int_levels': (multi_column_int_levels, df_serializer.serialize(multi_column_int_levels)),
            'multi_column_and_multi_index': (multi_column_and_multi_index,
                                             df_serializer.serialize(multi_column_and_multi_index)),
            'n_dimensional_df': (n_dimensional_df, Exception),
            'mixed_dtypes_df': (mixed_dtypes_df, df_serializer.serialize(mixed_dtypes_df))
        }
    return _TEST_DATA
