'''
Created on 25 Aug 2015

@author: ateng
'''
from pandas.util.testing import assert_frame_equal
import pytest

from tests.util import read_str_as_pandas


ts1 = read_str_as_pandas("""         observed_dt | near
                         2012-09-08 17:06:11.040 |  1.0
                         2012-10-08 17:06:11.040 |  2.0
                         2012-10-09 17:06:11.040 |  2.5
                         2012-11-08 17:06:11.040 |  3.0""")

ts1_append = read_str_as_pandas("""         observed_dt | near
                                2012-09-08 17:06:11.040 |  1.0
                                2012-10-08 17:06:11.040 |  2.0
                                2012-10-09 17:06:11.040 |  2.5
                                2012-11-08 17:06:11.040 |  3.0
                                2012-11-09 17:06:11.040 |  3.5""")


def test_new_ts_read_write(bitemporal_library):
    bitemporal_library.append('spam', ts1)
    assert_frame_equal(ts1, bitemporal_library.read('spam').data)


def test_existing_ts_append_and_read(bitemporal_library):
    bitemporal_library.append('spam', ts1)
    bitemporal_library.append('spam', ts1_append[-1:])
    assert_frame_equal(ts1_append, bitemporal_library.read('spam').data)


def test_existing_ts_update_existing_data_and_read(bitemporal_library):
    bitemporal_library.append('spam', ts1)
    bitemporal_library.append('spam', read_str_as_pandas("""         observed_dt | near
                                                         2012-10-09 17:06:11.040 |  4.2"""))
    expected_ts = read_str_as_pandas("""         observed_dt | near
                                     2012-09-08 17:06:11.040 |  1.0
                                     2012-10-08 17:06:11.040 |  2.0
                                     2012-10-09 17:06:11.040 |  4.2
                                     2012-11-08 17:06:11.040 |  3.0""")
    assert_frame_equal(expected_ts, bitemporal_library.read('spam').data)
