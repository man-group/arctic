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


@pytest.mark.parametrize("input_data",
                         [
                             None,
                             empty_ts,
                             small_ts,
                             medium_ts,
                             large_ts,
                         ])
def test_serialize_pandas_to_recarray(input_data):
    exc, ser_data, dtype = None, None, None
    try:
        ser_data, dtype = df_serializer.serialize(input_data)
    except Exception as e:
        exc = e

    if exc:
        with pytest.raises(ArcticSerializationException):
            incr_ser = IncrementalDataFrameToRecArraySerializer(df_serializer, input_data)
            incr_ser.serialize()
    else:
        incr_ser = IncrementalDataFrameToRecArraySerializer(df_serializer, input_data)
        incr_ser_data, incr_ser_dtype = incr_ser.serialize()
        assert ser_data.tostring() == incr_ser_data.tostring()
        assert dtype == incr_ser_dtype


def test_bulk_serialize_pandas_to_recarray():
    pass


def test_empty_serialize_pandas_to_recarray():
    pass


def test_incremental_serialize_pandas_to_recarray():
    pass
