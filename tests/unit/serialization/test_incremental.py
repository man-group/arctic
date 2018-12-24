import itertools

import pytest

from arctic.exceptions import ArcticSerializationException
from arctic.serialization.incremental import IncrementalPandasToRecArraySerializer
from arctic.serialization.numpy_records import DataFrameSerializer
from tests.unit.serialization.serialization_test_data import _mixed_test_data, is_test_data_serializable

_CHUNK_SIZE = 2 * 1024 * 1024 - 2048
NON_HOMOGENEOUS_DTYPE_PATCH_SIZE_ROWS = 50
_TEST_DATA = None

df_serializer = DataFrameSerializer()


def test_incremental_bad_init():
    with pytest.raises(ArcticSerializationException):
        IncrementalPandasToRecArraySerializer(df_serializer, 'hello world', chunk_size=_CHUNK_SIZE)
    with pytest.raises(ArcticSerializationException):
        IncrementalPandasToRecArraySerializer(df_serializer, 1234, chunk_size=_CHUNK_SIZE)
    with pytest.raises(ArcticSerializationException):
        IncrementalPandasToRecArraySerializer(df_serializer, _mixed_test_data()['small'][0], chunk_size=0)
    with pytest.raises(ArcticSerializationException):
        IncrementalPandasToRecArraySerializer(df_serializer, _mixed_test_data()['small'][0], chunk_size=-1)
    with pytest.raises(ArcticSerializationException):
        IncrementalPandasToRecArraySerializer(df_serializer, _mixed_test_data()['small'][0], chunk_size=_CHUNK_SIZE, string_max_len=-1)


def test_none_df():
    with pytest.raises(ArcticSerializationException):
        incr_ser = IncrementalPandasToRecArraySerializer(df_serializer, None, chunk_size=_CHUNK_SIZE)
        incr_ser.serialize()
    with pytest.raises(ArcticSerializationException):
        incr_ser = IncrementalPandasToRecArraySerializer(df_serializer, None, chunk_size=_CHUNK_SIZE)
        incr_ser.generator_bytes()


@pytest.mark.parametrize("input_df_descr", _mixed_test_data().keys())
def test_serialize_pandas_to_recarray(input_df_descr):
    if not is_test_data_serializable(input_df_descr):
        return

    df = _mixed_test_data()[input_df_descr][0]
    expectation = _mixed_test_data()[input_df_descr][1]

    incr_ser = IncrementalPandasToRecArraySerializer(df_serializer, df, chunk_size=_CHUNK_SIZE)
    if not isinstance(expectation, tuple) and issubclass(expectation, Exception):
        with pytest.raises(expectation):
            [chunk for chunk, _, _, _ in incr_ser.generator_bytes()]
    else:
        incr_ser_data, incr_ser_dtype = incr_ser.serialize()
        matching = expectation[0].tostring() == incr_ser_data.tostring()
        assert matching
        assert expectation[1] == incr_ser_dtype


@pytest.mark.parametrize("input_df_descr", _mixed_test_data().keys())
def test_serialize_incremental_pandas_to_recarray(input_df_descr):
    if not is_test_data_serializable(input_df_descr):
        return

    df = _mixed_test_data()[input_df_descr][0]
    expectation = _mixed_test_data()[input_df_descr][1]

    incr_ser = IncrementalPandasToRecArraySerializer(df_serializer, df, chunk_size=_CHUNK_SIZE)

    if not isinstance(expectation, tuple) and issubclass(expectation, Exception):
        with pytest.raises(expectation):
            [chunk for chunk, _, _, _ in incr_ser.generator_bytes()]
    else:
        chunk_bytes = [chunk_b for chunk_b, _, _, _ in incr_ser.generator_bytes()]
        matching = expectation[0].tostring() == b''.join(chunk_bytes)
        assert matching
        assert expectation[1] == incr_ser.dtype


@pytest.mark.parametrize("input_df_descr", _mixed_test_data().keys())
def test_serialize_incremental_chunk_size_pandas_to_recarray(input_df_descr):
    if not is_test_data_serializable(input_df_descr):
        return

    df = _mixed_test_data()[input_df_descr][0]
    expectation = _mixed_test_data()[input_df_descr][1]

    if not isinstance(expectation, tuple) and issubclass(expectation, Exception):
        for div in (1, 4, 8):
            chunk_size = div * 8 * 1024 ** 2
            with pytest.raises(expectation):
                incr_ser = IncrementalPandasToRecArraySerializer(df_serializer, df, chunk_size=chunk_size)
                [chunk for chunk, _, _, _ in incr_ser.generator_bytes()]
        return

    for div in (1, 4, 8):
        chunk_size = div * 8 * 1024 ** 2
        if input_df_descr is not None and len(expectation) > 0:
            row_size = int(expectation[0].dtype.itemsize)
            chunk_size = NON_HOMOGENEOUS_DTYPE_PATCH_SIZE_ROWS * row_size / div
        incr_ser = IncrementalPandasToRecArraySerializer(df_serializer, df, chunk_size=chunk_size)
        chunk_bytes = [chunk for chunk, _, _, _ in incr_ser.generator_bytes()]
        matching = expectation[0].tostring() == b''.join(chunk_bytes)
        assert matching
        assert expectation[1] == incr_ser.dtype


@pytest.mark.parametrize("input_df_descr", _mixed_test_data().keys())
def test_shape(input_df_descr):
    if not is_test_data_serializable(input_df_descr):
        return

    df = _mixed_test_data()[input_df_descr][0]
    expectation = _mixed_test_data()[input_df_descr][1]

    incr_ser = IncrementalPandasToRecArraySerializer(df_serializer, df, chunk_size=_CHUNK_SIZE)

    if not isinstance(expectation, tuple) and issubclass(expectation, Exception):
        with pytest.raises(expectation):
            [chunk for chunk, _, _, _ in incr_ser.shape]
    else:
        assert incr_ser.shape == expectation[0].shape


@pytest.mark.parametrize("from_idx, to_idx",
                         [(x, y) for (x, y) in itertools.product(range(-10, len(_mixed_test_data()['large'][0])+100, 500),
                                                                 range(-10, len(_mixed_test_data()['large'][0])+100, 500))
                          if x <= y]
                         )
def test_generator_bytes_range(from_idx, to_idx):
    # Tests also negative indexing
    df = _mixed_test_data()['large'][0]
    expectation = _mixed_test_data()['large'][1]

    incr_ser = IncrementalPandasToRecArraySerializer(df_serializer, df, chunk_size=_CHUNK_SIZE)

    chunk_bytes = [chunk_b for chunk_b, _, _, _ in incr_ser.generator_bytes(from_idx=from_idx, to_idx=to_idx)]
    matching = expectation[0][from_idx:to_idx].tostring() == b''.join(chunk_bytes)
    assert matching
    assert expectation[1] == incr_ser.dtype
