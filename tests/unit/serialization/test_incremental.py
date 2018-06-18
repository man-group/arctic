import pytest
import pandas as pd

from arctic._util import are_equals
from arctic.exceptions import ArcticSerializationException
from arctic.serialization.incremental import IncrementalDataFrameToRecArraySerializer
from arctic.serialization.numpy_records import DataFrameSerializer

from tests.util import get_large_ts

small_ts = get_large_ts(10)
medium_ts = get_large_ts(500)
large_ts = get_large_ts(2000)
empty_ts = pd.DataFrame()

df_serializer = DataFrameSerializer()

TEST_DATA = {
    'small': (small_ts, df_serializer.serialize(small_ts)),
    'medium': (medium_ts, df_serializer.serialize(medium_ts)),
    'large': (large_ts, df_serializer.serialize(large_ts)),
    'empty': (empty_ts, df_serializer.serialize(empty_ts))
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


@pytest.mark.parametrize("input_df",
                         [
                             'empty',
                             'small',
                             'medium',
                             'large'
                         ])
def test_serialize_pandas_to_recarray(input_df):
    incr_ser = IncrementalDataFrameToRecArraySerializer(df_serializer, TEST_DATA[input_df][0])
    incr_ser_data, incr_ser_dtype = incr_ser.serialize()
    assert TEST_DATA[input_df][1][0].tostring() == incr_ser_data.tostring()
    assert TEST_DATA[input_df][1][1] == incr_ser_dtype


@pytest.mark.parametrize("input_df",
                         [
                             'empty',
                             'small',
                             'medium',
                             'large'
                         ])
def test_serialize_incremental_pandas_to_recarray(input_df):
    incr_ser = IncrementalDataFrameToRecArraySerializer(df_serializer, TEST_DATA[input_df][0])
    chunk_bytes = [chunk_b for chunk_b, _ in incr_ser.generator_bytes]
    dtype = incr_ser.dtype
    assert TEST_DATA[input_df][1][0].tostring() == ''.join(chunk_bytes)
    assert TEST_DATA[input_df][1][1] == dtype


@pytest.mark.parametrize("input_df",
                         [
                             'empty',
                             'small',
                             'medium',
                             'large'
                         ])
def test_serialize_incremental_chunk_size_pandas_to_recarray(input_df):
    incr_ser = IncrementalDataFrameToRecArraySerializer(df_serializer, TEST_DATA[input_df][0], chunk_size=1024*64*8)
    chunk_bytes = [chunk_b for chunk_b, _ in incr_ser.generator_bytes]
    dtype = incr_ser.dtype
    assert TEST_DATA[input_df][1][0].tostring() == ''.join(chunk_bytes)
    assert TEST_DATA[input_df][1][1] == dtype
