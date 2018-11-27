import pytest

import arctic.serialization.numpy_records as anr
from tests.unit.serialization.serialization_test_data import _mixed_test_data as input_test_data

df_serializer = anr.DataFrameSerializer()


@pytest.mark.parametrize("input_df", input_test_data().keys())
def test_dataframe_confirm_fast_check_compatibility(input_df):
    orig_config = anr.FAST_CHECK_DF_SERIALIZABLE
    try:
        input_df = input_test_data()[input_df][0]
        anr.set_fast_check_df_serializable(True)
        with_fast_check = df_serializer.can_convert_to_records_without_objects(input_df, 'symA')
        anr.set_fast_check_df_serializable(False)
        without_fast_check = df_serializer.can_convert_to_records_without_objects(input_df, 'symA')
        assert with_fast_check == without_fast_check
    finally:
        anr.FAST_CHECK_DF_SERIALIZABLE = orig_config
