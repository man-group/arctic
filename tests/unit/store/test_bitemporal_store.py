from datetime import datetime as dt

from mock import create_autospec, sentinel
from pandas.util.testing import assert_frame_equal
import pytest

from arctic.store.bitemporal_store import BitemporalStore
from tests.util import read_str_as_pandas


ts1 = read_str_as_pandas("""           sample_dt | near
                         2012-09-08 17:06:11.040 |  1.0
                         2012-10-08 17:06:11.040 |  2.0
                         2012-10-09 17:06:11.040 |  2.5
                         2012-11-08 17:06:11.040 |  3.0""")


def test_add_observe_dt_index():
    self = create_autospec(BitemporalStore, observe_column='col_a')
    assert_frame_equal(BitemporalStore._add_observe_dt_index(self, ts1, as_of=dt(2001, 1, 1)),
                       read_str_as_pandas("""sample_dt |      col_a | near
                               2012-09-08 17:06:11.040 | 2001-01-01 |  1.0
                               2012-10-08 17:06:11.040 | 2001-01-01 |  2.0
                               2012-10-09 17:06:11.040 | 2001-01-01 |  2.5
                               2012-11-08 17:06:11.040 | 2001-01-01 |  3.0""", num_index=2))


def test_update_with_observe_column_fails():
    self = create_autospec(BitemporalStore, observe_column='col_a')
    with pytest.raises(ValueError) as e:
        BitemporalStore.update(self, sentinel.symbol, read_str_as_pandas(
                           """col_b |      col_a | near
            2012-09-08 17:06:11.040 | 2001-01-01 |  1.0""", num_index=2))
    assert str(e.value) == "Column col_a is not allowed as it is being used by bitemporal store interally."
