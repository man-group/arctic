import time

import arctic.serialization.numpy_records as anr
from tests.unit.serialization.serialization_test_data import _mixed_test_data as input_test_data

df_serializer = anr.DataFrameSerializer()


def _bench(rounds, input_df, fast):
    fast = bool(fast)
    anr.set_fast_check_df_serializable(fast)
    start = time.time()
    for i in range(rounds):
        df_serializer.can_convert_to_records_without_objects(input_df, 'symA')
    print("Time per iteration (fast={}): {}".format(fast, (time.time() - start)/rounds))


# Results suggest significant speed improvements for
#   (1) large df with objects
#       Time per iteration (fast=False): 0.0281402397156
#       Time per iteration (fast=True):  0.00866063833237
#   (2) large multi-column df
#       Time per iteration (fast=False): 0.00556221961975
#       Time per iteration (fast=True):  0.00276621818542
#   (3) large multi-index df
#       Time per iteration (fast=False): 0.00640722036362
#       Time per iteration (fast=True):  0.00154552936554
def assess_speed(df_kind):
    rounds = 100
    input_df = input_test_data()[df_kind][0]
    orig_config = anr.FAST_CHECK_DF_SERIALIZABLE
    try:
        _bench(rounds, input_df, fast=False)

        _bench(rounds, input_df, fast=True)
    finally:
        anr.FAST_CHECK_DF_SERIALIZABLE = orig_config


def main():
    for df_kind in ('large_with_some_objects', 'large_multi_index', 'large_multi_column'):
        assess_speed(df_kind)


if __name__ == '__main__':
    main()
