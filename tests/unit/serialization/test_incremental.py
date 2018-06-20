import pytest
import numpy as np
import pandas as pd

from arctic._util import are_equals
from arctic.exceptions import ArcticSerializationException
from arctic.serialization.incremental import IncrementalDataFrameToRecArraySerializer
from arctic.serialization.numpy_records import DataFrameSerializer
from tests.integration.chunkstore.test_utils import create_test_data

from tests.util import get_large_ts

NON_HOMOGENEOUS_DTYPE_PATCH_SIZE_ROWS = 50

onerow_ts = get_large_ts(1)
small_ts = get_large_ts(10)
medium_ts = get_large_ts(600)
large_ts = get_large_ts(1800)
empty_ts = pd.DataFrame()
empty_index = create_test_data(size=0, cols=10, index=True, multiindex=False, random_data=True, random_ids=True)

with_some_objects_ts = medium_ts.copy(deep=True)
with_some_objects_ts.iloc[0:NON_HOMOGENEOUS_DTYPE_PATCH_SIZE_ROWS, 0] = None
with_some_objects_ts.iloc[0:NON_HOMOGENEOUS_DTYPE_PATCH_SIZE_ROWS, 1] = 'A string'

with_string_ts = medium_ts.copy(deep=True)
with_string_ts['str_col'] = 'abc'
with_unicode_ts = medium_ts.copy(deep=True)
with_unicode_ts['ustr_col'] = u'abc'

with_some_none_ts = medium_ts.copy(deep=True)
with_some_none_ts.iloc[10:10] = None
with_some_none_ts.iloc[-10:-10] = np.nan
with_some_none_ts = with_some_none_ts.replace({np.nan: None})

multiindex_ts = create_test_data(size=500, cols=10, index=True, multiindex=True, random_data=True, random_ids=True)
empty_multiindex_ts = create_test_data(size=0, cols=10, index=True, multiindex=True, random_data=True, random_ids=True)

df_serializer = DataFrameSerializer()

TEST_DATA = {
    'onerow': (onerow_ts, df_serializer.serialize(onerow_ts)),
    'small': (small_ts, df_serializer.serialize(small_ts)),
    'medium': (medium_ts, df_serializer.serialize(medium_ts)),
    'large': (large_ts, df_serializer.serialize(large_ts)),
    'empty': (empty_ts, df_serializer.serialize(empty_ts)),
    'empty_index': (empty_index, df_serializer.serialize(empty_index)),
    'with_some_objects': (with_some_objects_ts, df_serializer.serialize(with_some_objects_ts)),
    'with_string': (with_string_ts, df_serializer.serialize(with_string_ts)),
    'with_unicode': (with_unicode_ts, df_serializer.serialize(with_unicode_ts)),
    'with_some_none': (with_some_none_ts, df_serializer.serialize(with_some_none_ts)),
    'multiindex': (multiindex_ts, df_serializer.serialize(multiindex_ts)),
    'empty_multiindex': (empty_multiindex_ts, df_serializer.serialize(empty_multiindex_ts))
}


def test_incremental_bad_init():
    with pytest.raises(ArcticSerializationException):
        IncrementalDataFrameToRecArraySerializer(df_serializer, 'hello world')
    with pytest.raises(ArcticSerializationException):
        IncrementalDataFrameToRecArraySerializer(df_serializer, 1234)
    with pytest.raises(ArcticSerializationException):
        IncrementalDataFrameToRecArraySerializer(df_serializer, small_ts, chunk_size=0)
    with pytest.raises(ArcticSerializationException):
        IncrementalDataFrameToRecArraySerializer(df_serializer, small_ts, chunk_size=-1)
    with pytest.raises(ArcticSerializationException):
        IncrementalDataFrameToRecArraySerializer(df_serializer, small_ts, string_max_len=-1)


def test_none_df():
    with pytest.raises(ArcticSerializationException):
        incr_ser = IncrementalDataFrameToRecArraySerializer(df_serializer, None)
        incr_ser.serialize()


@pytest.mark.parametrize("input_df", TEST_DATA.keys())
def test_serialize_pandas_to_recarray(input_df):
    incr_ser = IncrementalDataFrameToRecArraySerializer(df_serializer, TEST_DATA[input_df][0])
    incr_ser_data, incr_ser_dtype = incr_ser.serialize()
    matching = TEST_DATA[input_df][1][0].tostring() == incr_ser_data.tostring()
    assert matching
    assert TEST_DATA[input_df][1][1] == incr_ser_dtype


@pytest.mark.parametrize("input_df", TEST_DATA.keys())
def test_serialize_incremental_pandas_to_recarray(input_df):
    incr_ser = IncrementalDataFrameToRecArraySerializer(df_serializer, TEST_DATA[input_df][0])
    chunk_bytes = [chunk_b for chunk_b, _ in incr_ser.generator_bytes]
    matching = TEST_DATA[input_df][1][0].tostring() == ''.join(chunk_bytes)
    assert matching
    assert TEST_DATA[input_df][1][1] == incr_ser.dtype


@pytest.mark.parametrize("input_df", TEST_DATA.keys())
def test_serialize_incremental_chunk_size_pandas_to_recarray(input_df):
    for div in (1, 4, 8):
        chunk_size = div * 8 * 1024 ** 2
        if input_df is not None and len(TEST_DATA[input_df][1]) > 0:
            row_size = int(TEST_DATA[input_df][1][0].dtype.itemsize)
            chunk_size = NON_HOMOGENEOUS_DTYPE_PATCH_SIZE_ROWS * row_size / div
        incr_ser = IncrementalDataFrameToRecArraySerializer(df_serializer, TEST_DATA[input_df][0], chunk_size=chunk_size)
        chunk_bytes = [chunk[0] for chunk in incr_ser.generator_bytes]
        matching = TEST_DATA[input_df][1][0].tostring() == ''.join(chunk_bytes)
        assert matching
        assert TEST_DATA[input_df][1][1] == incr_ser.dtype
