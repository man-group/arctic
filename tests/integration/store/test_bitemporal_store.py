'''
Created on 25 Aug 2015

@author: ateng
'''
from datetime import datetime as dt

from mock import patch
from pandas.util.testing import assert_frame_equal

from tests.util import read_str_as_pandas


ts1 = read_str_as_pandas("""           sample_dt | near
                         2012-09-08 17:06:11.040 |  1.0
                         2012-10-08 17:06:11.040 |  2.0
                         2012-10-09 17:06:11.040 |  2.5
                         2012-11-08 17:06:11.040 |  3.0""")

ts1_append = read_str_as_pandas("""           sample_dt | near
                                2012-09-08 17:06:11.040 |  1.0
                                2012-10-08 17:06:11.040 |  2.0
                                2012-10-09 17:06:11.040 |  2.5
                                2012-11-08 17:06:11.040 |  3.0
                                2012-11-09 17:06:11.040 |  3.5""")


def test_new_ts_read_write(bitemporal_library):
    bitemporal_library.append('spam', ts1)
    assert_frame_equal(ts1, bitemporal_library.read('spam').data)


def test_read_ts_raw(bitemporal_library):
    bitemporal_library.append('spam', ts1, as_of=dt(2015, 5, 1))
    assert_frame_equal(bitemporal_library.read('spam', raw=True).data, read_str_as_pandas(
                                             """                    sample_dt | observed_dt | near
                                                      2012-09-08 17:06:11.040 |  2015-05-01 |  1.0
                                                      2012-10-08 17:06:11.040 |  2015-05-01 |  2.0
                                                      2012-10-09 17:06:11.040 |  2015-05-01 |  2.5
                                                      2012-11-08 17:06:11.040 |  2015-05-01 |  3.0""", num_index=2))


def test_existing_ts_append_and_read(bitemporal_library):
    bitemporal_library.append('spam', ts1)
    bitemporal_library.append('spam', ts1_append[-1:])
    assert_frame_equal(ts1_append, bitemporal_library.read('spam').data)


def test_existing_ts_update_existing_data_and_read(bitemporal_library):
    bitemporal_library.append('spam', ts1)
    bitemporal_library.append('spam', read_str_as_pandas("""         sample_dt | near
                                                         2012-10-09 17:06:11.040 |  4.2"""))
    expected_ts = read_str_as_pandas("""         sample_dt | near
                                     2012-09-08 17:06:11.040 |  1.0
                                     2012-10-08 17:06:11.040 |  2.0
                                     2012-10-09 17:06:11.040 |  4.2
                                     2012-11-08 17:06:11.040 |  3.0""")
    assert_frame_equal(expected_ts, bitemporal_library.read('spam').data)


def test_read_ts_with_historical_update(bitemporal_library):
    with patch('arctic.store.bitemporal_store.dt') as mock_dt:
        mock_dt.now.return_value = dt(2015, 5, 1)
        mock_dt.side_effect = lambda *args, **kwargs: dt(*args, **kwargs)
        bitemporal_library.append('spam', ts1)

    bitemporal_library.append('spam', read_str_as_pandas("""         sample_dt | near
                                                         2012-10-09 17:06:11.040 | 4.2"""),
                              as_of=dt(2015, 5, 2))

    bitemporal_library.append('spam', read_str_as_pandas("""         sample_dt | near
                                                         2012-10-09 17:06:11.040 | 6.6"""),
                              as_of=dt(2015, 5, 3))

    assert_frame_equal(bitemporal_library.read('spam', as_of=dt(2015, 5, 2, 10)).data, read_str_as_pandas(
                                                                                    """sample_dt   | near
                                                                           2012-09-08 17:06:11.040 |  1.0
                                                                           2012-10-08 17:06:11.040 |  2.0
                                                                           2012-10-09 17:06:11.040 |  4.2
                                                                           2012-11-08 17:06:11.040 |  3.0"""))

    assert_frame_equal(bitemporal_library.read('spam').data, read_str_as_pandas("""  sample_dt | near
                                                                       2012-09-08 17:06:11.040 |  1.0
                                                                       2012-10-08 17:06:11.040 |  2.0
                                                                       2012-10-09 17:06:11.040 |  6.6
                                                                       2012-11-08 17:06:11.040 |  3.0"""))

    assert_frame_equal(bitemporal_library.read('spam', as_of=dt(2015, 5, 1, 10)).data, ts1)


def test_read_ts_with_historical_update_and_new_row(bitemporal_library):
    with patch('arctic.store.bitemporal_store.dt') as mock_dt:
        mock_dt.now.return_value = dt(2015, 5, 1)
        mock_dt.side_effect = lambda *args, **kwargs: dt(*args, **kwargs)
        bitemporal_library.append('spam', ts1)

    bitemporal_library.append('spam', read_str_as_pandas("""           sample_dt | near
                                                         2012-10-09 17:06:11.040 | 4.2
                                                         2012-12-01 17:06:11.040 | 100"""),
                              as_of=dt(2015, 5, 2))

    assert_frame_equal(bitemporal_library.read('spam').data, read_str_as_pandas("""  sample_dt | near
                                                                       2012-09-08 17:06:11.040 |  1.0
                                                                       2012-10-08 17:06:11.040 |  2.0
                                                                       2012-10-09 17:06:11.040 |  4.2
                                                                       2012-11-08 17:06:11.040 |  3.0
                                                                       2012-12-01 17:06:11.040 |  100"""))

    assert_frame_equal(bitemporal_library.read('spam', as_of=dt(2015, 5, 1, 10)).data, ts1)


def test_insert_new_rows_in_middle_remains_sorted(bitemporal_library):
    bitemporal_library.append('spam', ts1)
    bitemporal_library.append('spam', read_str_as_pandas("""           sample_dt | near
                                                         2012-10-09 12:00:00.000 | 30.0
                                                         2012-12-01 17:06:11.040 | 100"""))

    assert_frame_equal(bitemporal_library.read('spam').data, read_str_as_pandas("""  sample_dt | near
                                                                       2012-09-08 17:06:11.040 |  1.0
                                                                       2012-10-08 17:06:11.040 |  2.0
                                                                       2012-10-09 12:00:00.000 | 30.0
                                                                       2012-10-09 17:06:11.040 |  2.5
                                                                       2012-11-08 17:06:11.040 |  3.0
                                                                       2012-12-01 17:06:11.040 |  100"""))


def test_insert_versions_inbetween_works_ok(bitemporal_library):
    bitemporal_library.append('spam', ts1, as_of=dt(2015, 5, 1))
    bitemporal_library.append('spam', read_str_as_pandas("""           sample_dt | near
                                                         2012-12-01 17:06:11.040 | 100"""),
                              as_of=dt(2015, 5, 10))

    bitemporal_library.append('spam', read_str_as_pandas("""           sample_dt | near
                                                         2012-12-01 17:06:11.040 | 25"""),
                              as_of=dt(2015, 5, 8))

    assert_frame_equal(bitemporal_library.read('spam').data, read_str_as_pandas("""  sample_dt | near
                                                                       2012-09-08 17:06:11.040 |  1.0
                                                                       2012-10-08 17:06:11.040 |  2.0
                                                                       2012-10-09 17:06:11.040 |  2.5
                                                                       2012-11-08 17:06:11.040 |  3.0
                                                                       2012-12-01 17:06:11.040 |  100"""))

    assert_frame_equal(bitemporal_library.read('spam', as_of=dt(2015, 5, 9)).data, read_str_as_pandas(
                                                                              """  sample_dt | near
                                                                     2012-09-08 17:06:11.040 |  1.0
                                                                     2012-10-08 17:06:11.040 |  2.0
                                                                     2012-10-09 17:06:11.040 |  2.5
                                                                     2012-11-08 17:06:11.040 |  3.0
                                                                     2012-12-01 17:06:11.040 |  25"""))


def test_read_ts_raw_all_version_ok(bitemporal_library):
    bitemporal_library.append('spam', ts1, as_of=dt(2015, 5, 1))
    bitemporal_library.append('spam', read_str_as_pandas("""           sample_dt | near
                                                         2012-12-01 17:06:11.040 | 25"""),
                              as_of=dt(2015, 5, 5))
    bitemporal_library.append('spam', read_str_as_pandas("""           sample_dt | near
                                                         2012-11-08 17:06:11.040 | 42"""),
                              as_of=dt(2015, 5, 3))
    bitemporal_library.append('spam', read_str_as_pandas("""           sample_dt | near
                                                         2012-10-08 17:06:11.040 | 42
                                                         2013-01-01 17:06:11.040 | 100"""),
                              as_of=dt(2015, 5, 10,))
    assert_frame_equal(bitemporal_library.read('spam', raw=True).data, read_str_as_pandas(
                                             """                    sample_dt | observed_dt | near
                                                      2012-09-08 17:06:11.040 |  2015-05-01 |  1.0
                                                      2012-10-08 17:06:11.040 |  2015-05-01 |  2.0
                                                      2012-10-08 17:06:11.040 |  2015-05-10 |  42
                                                      2012-10-09 17:06:11.040 |  2015-05-01 |  2.5
                                                      2012-11-08 17:06:11.040 |  2015-05-01 |  3.0
                                                      2012-11-08 17:06:11.040 |  2015-05-03 |  42
                                                      2012-12-01 17:06:11.040 |  2015-05-05 |  25
                                                      2013-01-01 17:06:11.040 |  2015-05-10 |  100""", num_index=2))

