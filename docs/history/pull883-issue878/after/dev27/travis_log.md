```shell
$ source ~/virtualenv/python2.7/bin/activate0.00s0.14s0.09s0.07s
worker_info
Worker information
0.15s0.01s0.00s0.01s
system_info
Build system information
0.01s0.01s0.74s0.23s0.05s0.00s0.04s0.00s0.01s0.01s0.01s0.01s0.01s0.00s0.00s0.02s0.00s0.01s0.34s0.00s0.00s0.00s0.01s0.00s0.10s0.01s0.81s0.00s0.00s6.03s0.00s2.68s0.00s2.60s
docker_mtu_and_registry_mirrors
resolvconf
services
3.03s$ sudo systemctl start mongod
git.checkout
0.76s$ git clone --depth=50 https://github.com/man-group/arctic.git man-group/arctic
git.submodule
0.03s$ git submodule update --init --recursive
$ python --version
Python 2.7.15
$ pip --version
pip 20.1.1 from /home/travis/virtualenv/python2.7.15/lib/python2.7/site-packages/pip (python 2.7)
before_install
0.90s$ pip install pycodestyle
install.1
0.14s$ mongo --version
install.2
1.83s$ pip install --upgrade pip
install.3
0.70s$ pip install python-dateutil --upgrade
install.4
0.94s$ pip install pytz --upgrade
install.5
0.60s$ pip install tzlocal --upgrade
install.6
1.48s$ pip install pymongo --upgrade
install.7
1.05s$ pip install numpy --upgrade
install.8
3.71s$ pip install pandas --upgrade
install.9
0.63s$ pip install decorator --upgrade
install.10
0.65s$ pip install enum34 --upgrade
install.11
2.13s$ pip install lz4 --upgrade
install.12
0.55s$ pip install mock --upgrade
install.13
0.68s$ pip install mockextras
install.14
0.75s$ pip install pytest --upgrade
install.15
1.39s$ pip install pytest-cov --upgrade
install.16
3.30s$ pip install pytest-server-fixtures --upgrade
install.17
0.75s$ pip install pytest-timeout --upgrade
install.18
0.91s$ pip install pytest-xdist --upgrade
install.19
0.73s$ pip install setuptools-git --upgrade
install.20
4.18s$ if [[ $TRAVIS_PYTHON_VERSION == 2.7 ]]; then pip install pandas==0.22.0; fi
0.25s$ pip freeze
DEPRECATION: Python 2.7 reached the end of its life on January 1st, 2020. Please upgrade your Python as Python 2.7 is no longer maintained. pip 21.0 will drop support for Python 2.7 in January 2021. More details about Python 2 support in pip can be found at https://pip.pypa.io/en/latest/development/release-process/#python-2-support pip 21.0 will remove support for this functionality.
apipkg==1.5
atomicwrites==1.2.1
attrs==18.2.0
backports.os==0.1.1
certifi==2018.10.15
chardet==4.0.0
configparser==3.7.4
contextlib2==0.5.5
coverage==5.3.1
decorator==4.4.2
enum34==1.1.10
execnet==1.7.1
funcsigs==1.0.2
future==0.18.2
idna==2.10
importlib-metadata==0.18
lz4==2.2.1
mock==3.0.5
mockextras==1.0.2
more-itertools==4.3.0
nose==1.3.7
numpy==1.16.6
packaging==19.0
pandas==0.22.0
path.py==11.5.2
pathlib2==2.3.2
pbr==5.1.1
pipenv==2018.11.26
pluggy==0.12.0
psutil==5.8.0
py==1.7.0
pycodestyle==2.6.0
pymongo==3.11.2
pyparsing==2.4.0
pytest==4.6.11
pytest-cov==2.11.0
pytest-fixture-config==1.7.0
pytest-forked==1.3.0
pytest-server-fixtures==1.7.0
pytest-shutil==1.7.0
pytest-timeout==1.4.2
pytest-xdist==1.34.0
python-dateutil==2.8.1
pytz==2020.5
requests==2.25.1
retry==0.9.2
scandir==1.9.0
setuptools-git==1.2
six==1.11.0
termcolor==1.1.0
typing==3.6.6
tzlocal==2.1
urllib3==1.26.2
virtualenv==16.1.0
virtualenv-clone==0.4.0
wcwidth==0.1.7
zipp==0.5.1
The command "pip freeze" exited with 0.
1341.10s$ python setup.py test --pytest-args=-v
running test
WARNING: Testing via this command is deprecated and will be removed in a future version. Users looking for a generic test entry point independent of test runner are encouraged to use tox.
DEPRECATION: Python 2.7 reached the end of its life on January 1st, 2020. Please upgrade your Python as Python 2.7 is no longer maintained. pip 21.0 will drop support for Python 2.7 in January 2021. More details about Python 2 support in pip can be found at https://pip.pypa.io/en/latest/development/release-process/#python-2-support pip 21.0 will remove support for this functionality.
DEPRECATION: Python 2.7 reached the end of its life on January 1st, 2020. Please upgrade your Python as Python 2.7 is no longer maintained. pip 21.0 will drop support for Python 2.7 in January 2021. More details about Python 2 support in pip can be found at https://pip.pypa.io/en/latest/development/release-process/#python-2-support pip 21.0 will remove support for this functionality.
DEPRECATION: Python 2.7 reached the end of its life on January 1st, 2020. Please upgrade your Python as Python 2.7 is no longer maintained. pip 21.0 will drop support for Python 2.7 in January 2021. More details about Python 2 support in pip can be found at https://pip.pypa.io/en/latest/development/release-process/#python-2-support pip 21.0 will remove support for this functionality.
running egg_info
creating arctic.egg-info
writing requirements to arctic.egg-info/requires.txt
writing arctic.egg-info/PKG-INFO
writing top-level names to arctic.egg-info/top_level.txt
writing dependency_links to arctic.egg-info/dependency_links.txt
writing entry points to arctic.egg-info/entry_points.txt
writing manifest file 'arctic.egg-info/SOURCES.txt'
writing manifest file 'arctic.egg-info/SOURCES.txt'
running build_ext
============================= test session starts ==============================
platform linux2 -- Python 2.7.15, pytest-4.6.11, py-1.7.0, pluggy-0.12.0 -- /home/travis/virtualenv/python2.7.15/bin/python
cachedir: .pytest_cache
rootdir: /home/travis/build/man-group/arctic
plugins: xdist-1.26.1, server-fixtures-1.7.0, shutil-1.7.0, timeout-1.4.2, forked-1.3.0, cov-2.11.0
collected 1339 items                                                           
tests/integration/test_arctic.py::test_connect_to_Arctic_string PASSED   [  0%]2021-01-20 04:11:23,065 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/test_arctic.py::test_connect_to_Arctic_connection PASSED [  0%]2021-01-20 04:11:23,747 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/test_arctic.py::test_reset_Arctic PASSED               [  0%]2021-01-20 04:11:24,654 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/test_arctic.py::test_re_authenticate_on_arctic_reset PASSED [  0%]2021-01-20 04:11:25,572 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/test_arctic.py::test_simple PASSED                     [  0%]2021-01-20 04:11:27,633 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/test_arctic.py::test_indexes PASSED                    [  0%]2021-01-20 04:11:28,532 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/test_arctic.py::test_delete_library PASSED             [  0%]2021-01-20 04:11:29,759 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/test_arctic.py::test_quota PASSED                      [  0%]2021-01-20 04:11:30,706 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/test_arctic.py::test_check_quota PASSED                [  0%]2021-01-20 04:11:31,629 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/test_arctic.py::test_default_mongo_retry_timout PASSED [  0%]
tests/integration/test_arctic.py::test_lib_rename PASSED                 [  0%]
tests/integration/test_arctic.py::test_lib_rename_namespace PASSED       [  0%]
tests/integration/test_arctic.py::test_lib_type PASSED                   [  0%]2021-01-20 04:11:34,421 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/test_arctic.py::test_library_exists PASSED             [  1%]2021-01-20 04:11:35,327 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/test_arctic.py::test_library_exists_no_auth PASSED     [  1%]2021-01-20 04:11:36,236 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/test_arctic.py::test_list_libraries_cached PASSED      [  1%]2021-01-20 04:11:37,356 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/test_arctic.py::test_initialize_library_adds_to_cache PASSED [  1%]2021-01-20 04:11:38,687 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/test_arctic.py::test_cache_does_not_return_stale_data PASSED [  1%]2021-01-20 04:11:40,584 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/test_arctic.py::test_renaming_returns_new_name_in_cache PASSED [  1%]2021-01-20 04:11:41,689 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/test_arctic.py::test_deleting_library_removes_it_from_cache PASSED [  1%]2021-01-20 04:11:42,947 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/test_arctic.py::test_disable_cache_by_settings PASSED  [  1%]2021-01-20 04:11:43,860 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/test_arctic_multithreading.py::test_multiprocessing_safety PASSED [  1%]2021-01-20 04:12:06,879 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/test_arctic_multithreading.py::test_multiprocessing_safety_parent_children_race PASSED [  1%]2021-01-20 04:12:25,480 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/test_async_arctic.py::test_async_arctic PASSED         [  1%]
tests/integration/test_compress_integration.py::test_roundtrip[arctic/lz4] PASSED [  1%]
tests/integration/test_compress_integration.py::test_roundtrip[arcticHC/lz4] PASSED [  1%]
tests/integration/test_compress_integration.py::test_roundtrip[lz4/arctic] PASSED [  2%]
tests/integration/test_compress_integration.py::test_roundtrip[lz4HC/arctic] PASSED [  2%]
tests/integration/test_compress_integration.py::test_performance_sequential[300-50000.0] PASSED [  2%]
tests/integration/test_compress_integration.py::test_performance_sequential[5-2000000.0] PASSED [  2%]
tests/integration/test_compress_integration.py::test_performance_sequential[10-2000000.0] PASSED [  2%]
tests/integration/test_compress_integration.py::test_performance_sequential[100-2000000.0] PASSED [  2%]
tests/integration/test_compress_integration.py::test_performance_sequential[250-2000000.0] PASSED [  2%]
tests/integration/test_compress_integration.py::test_exceptions PASSED   [  2%]
tests/integration/test_concurrent_append.py::test_append_kill PASSED     [  2%]2021-01-20 04:15:30,398 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/test_decorators.py::test_get_host_VersionStore PASSED  [  2%]2021-01-20 04:15:31,302 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/test_howtos.py::test_howto[how_to_custom_arctic_library.py] PASSED [  2%]2021-01-20 04:15:32,063 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/test_howtos.py::test_howto[how_to_use_arctic.py] PASSED [  2%]2021-01-20 04:15:33,050 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_chunkstore.py::test_write_dataframe PASSED [  2%]2021-01-20 04:15:33,956 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_chunkstore.py::test_upsert_dataframe PASSED [  2%]2021-01-20 04:15:35,465 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_chunkstore.py::test_write_dataframe_noindex PASSED [  3%]2021-01-20 04:15:36,370 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_chunkstore.py::test_overwrite_dataframe PASSED [  3%]2021-01-20 04:15:37,287 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_chunkstore.py::test_overwrite_dataframe_noindex PASSED [  3%]2021-01-20 04:15:38,178 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_chunkstore.py::test_overwrite_dataframe_monthly PASSED [  3%]2021-01-20 04:15:39,118 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_chunkstore.py::test_write_read_with_daterange PASSED [  3%]2021-01-20 04:15:40,025 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_chunkstore.py::test_write_read_with_daterange_noindex PASSED [  3%]2021-01-20 04:15:40,914 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_chunkstore.py::test_store_single_index_df PASSED [  3%]2021-01-20 04:15:41,810 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_chunkstore.py::test_no_range PASSED    [  3%]2021-01-20 04:15:42,707 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_chunkstore.py::test_closed_open PASSED [  3%]2021-01-20 04:15:43,600 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_chunkstore.py::test_open_closed PASSED [  3%]2021-01-20 04:15:44,492 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_chunkstore.py::test_closed_open_no_index PASSED [  3%]2021-01-20 04:15:45,377 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_chunkstore.py::test_open_open_no_index PASSED [  3%]2021-01-20 04:15:46,259 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_chunkstore.py::test_monthly_df PASSED  [  3%]2021-01-20 04:15:47,165 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_chunkstore.py::test_yearly_df PASSED   [  4%]2021-01-20 04:15:48,041 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_chunkstore.py::test_append_daily PASSED [  4%]2021-01-20 04:15:49,025 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_chunkstore.py::test_append_monthly PASSED [  4%]2021-01-20 04:15:49,954 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_chunkstore.py::test_append_yearly PASSED [  4%]2021-01-20 04:15:50,864 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_chunkstore.py::test_append_existing_chunk PASSED [  4%]2021-01-20 04:15:51,757 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_chunkstore.py::test_store_objects_df PASSED [  4%]2021-01-20 04:15:52,647 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_chunkstore.py::test_empty_range PASSED [  4%]2021-01-20 04:15:53,550 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_chunkstore.py::test_update PASSED      [  4%]2021-01-20 04:15:54,482 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_chunkstore.py::test_update_no_overlap PASSED [  4%]2021-01-20 04:15:55,395 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_chunkstore.py::test_update_chunk_range PASSED [  4%]2021-01-20 04:15:56,315 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_chunkstore.py::test_update_chunk_range_overlap PASSED [  4%]2021-01-20 04:15:57,208 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_chunkstore.py::test_append_before PASSED [  4%]2021-01-20 04:15:58,173 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_chunkstore.py::test_append_and_update PASSED [  4%]2021-01-20 04:15:59,179 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_chunkstore.py::test_update_same_df PASSED [  5%]2021-01-20 04:16:00,149 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_chunkstore.py::test_df_with_multiindex PASSED [  5%]2021-01-20 04:16:01,694 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_chunkstore.py::test_with_strings PASSED [  5%]2021-01-20 04:16:03,230 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_chunkstore.py::test_with_strings_multiindex_append PASSED [  5%]2021-01-20 04:16:04,233 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_chunkstore.py::test_multiple_actions PASSED [  5%]2021-01-20 04:16:12,122 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_chunkstore.py::test_multiple_actions_monthly_data PASSED [  5%]2021-01-20 04:16:15,755 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_chunkstore.py::test_delete PASSED      [  5%]2021-01-20 04:16:16,672 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_chunkstore.py::test_delete_empty_df_on_range PASSED [  5%]2021-01-20 04:16:17,594 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_chunkstore.py::test_get_info PASSED    [  5%]2021-01-20 04:16:18,481 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_chunkstore.py::test_get_info_after_append PASSED [  5%]2021-01-20 04:16:19,435 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_chunkstore.py::test_get_info_after_update PASSED [  5%]2021-01-20 04:16:20,365 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_chunkstore.py::test_delete_range PASSED [  5%]2021-01-20 04:16:21,295 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_chunkstore.py::test_delete_range_noindex PASSED [  5%]2021-01-20 04:16:22,202 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_chunkstore.py::test_read_chunk_range PASSED [  5%]2021-01-20 04:16:23,129 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_chunkstore.py::test_read_data_doesnt_exist PASSED [  6%]
tests/integration/chunkstore/test_chunkstore.py::test_invalid_type PASSED [  6%]
tests/integration/chunkstore/test_chunkstore.py::test_append_no_data PASSED [  6%]
tests/integration/chunkstore/test_chunkstore.py::test_append_upsert PASSED [  6%]2021-01-20 04:16:26,637 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_chunkstore.py::test_append_no_new_data PASSED [  6%]2021-01-20 04:16:27,724 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_chunkstore.py::test_overwrite_series PASSED [  6%]2021-01-20 04:16:28,625 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_chunkstore.py::test_overwrite_series_monthly PASSED [  6%]2021-01-20 04:16:29,515 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_chunkstore.py::test_pandas_datetime_index_store_series PASSED [  6%]2021-01-20 04:16:30,392 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_chunkstore.py::test_yearly_series PASSED [  6%]2021-01-20 04:16:31,259 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_chunkstore.py::test_store_objects_series PASSED [  6%]2021-01-20 04:16:32,177 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_chunkstore.py::test_update_series PASSED [  6%]2021-01-20 04:16:33,096 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_chunkstore.py::test_update_same_series PASSED [  6%]2021-01-20 04:16:33,984 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_chunkstore.py::test_dtype_mismatch PASSED [  6%]2021-01-20 04:16:34,885 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_chunkstore.py::test_read_column_subset PASSED [  7%]2021-01-20 04:16:35,805 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_chunkstore.py::test_rename PASSED      [  7%]
tests/integration/chunkstore/test_chunkstore.py::test_pass_thru_chunker PASSED [  7%]2021-01-20 04:16:37,766 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_chunkstore.py::test_pass_thru_chunker_append PASSED [  7%]2021-01-20 04:16:38,653 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_chunkstore.py::test_pass_thru_chunker_update PASSED [  7%]2021-01-20 04:16:39,545 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_chunkstore.py::test_pass_thru_chunker_update_range PASSED [  7%]2021-01-20 04:16:40,447 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_chunkstore.py::test_size_chunking PASSED [  7%]2021-01-20 04:16:43,664 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_chunkstore.py::test_size_chunk_append PASSED [  7%]2021-01-20 04:16:50,325 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_chunkstore.py::test_delete_range_segment PASSED [  7%]2021-01-20 04:16:55,533 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_chunkstore.py::test_size_chunk_update PASSED [  7%]2021-01-20 04:17:01,952 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_chunkstore.py::test_size_chunk_multiple_update PASSED [  7%]2021-01-20 04:17:05,220 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_chunkstore.py::test_get_chunk_range PASSED [  7%]2021-01-20 04:17:06,122 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_chunkstore.py::test_iterators PASSED   [  7%]2021-01-20 04:17:07,130 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_chunkstore.py::test_unnamed_colums PASSED [  7%]
tests/integration/chunkstore/test_chunkstore.py::test_quarterly_data PASSED [  8%]2021-01-20 04:17:08,945 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_chunkstore.py::test_list_symbols PASSED [  8%]2021-01-20 04:17:13,081 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_chunkstore.py::test_stats PASSED       [  8%]2021-01-20 04:17:17,224 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_chunkstore.py::test_metadata PASSED    [  8%]2021-01-20 04:17:18,113 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_chunkstore.py::test_metadata_update PASSED [  8%]2021-01-20 04:17:18,998 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_chunkstore.py::test_metadata_nosymbol PASSED [  8%]2021-01-20 04:17:19,855 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_chunkstore.py::test_metadata_none PASSED [  8%]2021-01-20 04:17:20,748 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_chunkstore.py::test_metadata_invalid PASSED [  8%]2021-01-20 04:17:21,636 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_chunkstore.py::test_write_metadata PASSED [  8%]2021-01-20 04:17:22,511 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_chunkstore.py::test_write_metadata_nosymbol PASSED [  8%]2021-01-20 04:17:23,359 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_chunkstore.py::test_audit PASSED       [  8%]2021-01-20 04:17:24,433 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_chunkstore.py::test_chunkstore_misc PASSED [  8%]2021-01-20 04:17:25,316 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_chunkstore.py::test_unsorted_index PASSED [  8%]2021-01-20 04:17:26,239 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_chunkstore.py::test_unsorted_date_col PASSED [  9%]2021-01-20 04:17:27,145 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_chunkstore.py::test_chunk_range_with_dti PASSED [  9%]2021-01-20 04:17:28,019 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_chunkstore.py::test_chunkstore_multiread PASSED [  9%]2021-01-20 04:17:28,999 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_chunkstore.py::test_chunkstore_multiread_samedate PASSED [  9%]2021-01-20 04:17:29,966 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_chunkstore.py::test_write_dataframe_with_func PASSED [  9%]2021-01-20 04:17:31,274 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_fixes.py::test_write_dataframe PASSED  [  9%]2021-01-20 04:17:32,178 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_fixes.py::test_compression PASSED      [  9%]2021-01-20 04:17:34,289 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_fixes.py::test_date_interval PASSED    [  9%]2021-01-20 04:17:35,367 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_fixes.py::test_rewrite PASSED          [  9%]2021-01-20 04:17:36,258 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_fixes.py::test_iterator PASSED         [  9%]2021-01-20 04:17:37,541 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_fixes.py::test_missing_cols PASSED     [  9%]2021-01-20 04:17:38,493 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_fixes.py::test_column_copy PASSED      [  9%]2021-01-20 04:17:39,381 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_fixes.py::test_get_info_empty PASSED   [  9%]2021-01-20 04:17:40,252 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_utils.py::test_read_apply PASSED       [ 10%]2021-01-20 04:17:41,140 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/tools/test_tools.py::test_segment_repair_tool PASSED [ 10%]2021-01-20 04:17:44,630 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/fixtures/test_arctic.py::test_arctic PASSED            [ 10%]2021-01-20 04:17:45,318 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/fixtures/test_arctic.py::test_library PASSED           [ 10%]2021-01-20 04:17:46,222 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/fixtures/test_arctic.py::test_ms_lib PASSED            [ 10%]2021-01-20 04:17:46,990 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_arctic_fsck.py::test_cleanup_orphaned_chunks[True-data0-FwPointersCfg.DISABLED] PASSED [ 10%]2021-01-20 04:17:47,949 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_arctic_fsck.py::test_cleanup_orphaned_chunks[True-data1-FwPointersCfg.HYBRID] PASSED [ 10%]2021-01-20 04:17:48,914 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_arctic_fsck.py::test_cleanup_orphaned_chunks[True-data2-FwPointersCfg.ENABLED] PASSED [ 10%]2021-01-20 04:17:49,872 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_arctic_fsck.py::test_cleanup_orphaned_chunks[True-data3-FwPointersCfg.DISABLED] PASSED [ 10%]2021-01-20 04:17:50,820 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_arctic_fsck.py::test_cleanup_orphaned_chunks[True-data4-FwPointersCfg.HYBRID] PASSED [ 10%]2021-01-20 04:17:51,783 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_arctic_fsck.py::test_cleanup_orphaned_chunks[True-data5-FwPointersCfg.ENABLED] PASSED [ 10%]2021-01-20 04:17:52,753 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_arctic_fsck.py::test_cleanup_orphaned_chunks[False-data6-FwPointersCfg.DISABLED] PASSED [ 10%]2021-01-20 04:17:53,705 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_arctic_fsck.py::test_cleanup_orphaned_chunks[False-data7-FwPointersCfg.HYBRID] PASSED [ 10%]2021-01-20 04:17:54,653 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_arctic_fsck.py::test_cleanup_orphaned_chunks[False-data8-FwPointersCfg.ENABLED] PASSED [ 10%]2021-01-20 04:17:55,600 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_arctic_fsck.py::test_cleanup_orphaned_chunks[False-data9-FwPointersCfg.DISABLED] PASSED [ 11%]2021-01-20 04:17:56,562 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_arctic_fsck.py::test_cleanup_orphaned_chunks[False-data10-FwPointersCfg.HYBRID] PASSED [ 11%]2021-01-20 04:17:57,520 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_arctic_fsck.py::test_cleanup_orphaned_chunks[False-data11-FwPointersCfg.ENABLED] PASSED [ 11%]2021-01-20 04:17:58,472 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_arctic_fsck.py::test_cleanup_noop[True-data0-FwPointersCfg.DISABLED] PASSED [ 11%]2021-01-20 04:17:59,414 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_arctic_fsck.py::test_cleanup_noop[True-data1-FwPointersCfg.HYBRID] PASSED [ 11%]2021-01-20 04:18:00,350 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_arctic_fsck.py::test_cleanup_noop[True-data2-FwPointersCfg.ENABLED] PASSED [ 11%]2021-01-20 04:18:01,298 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_arctic_fsck.py::test_cleanup_noop[True-data3-FwPointersCfg.DISABLED] PASSED [ 11%]2021-01-20 04:18:02,252 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_arctic_fsck.py::test_cleanup_noop[True-data4-FwPointersCfg.HYBRID] PASSED [ 11%]2021-01-20 04:18:03,215 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_arctic_fsck.py::test_cleanup_noop[True-data5-FwPointersCfg.ENABLED] PASSED [ 11%]2021-01-20 04:18:04,204 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_arctic_fsck.py::test_cleanup_noop[False-data6-FwPointersCfg.DISABLED] PASSED [ 11%]2021-01-20 04:18:05,160 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_arctic_fsck.py::test_cleanup_noop[False-data7-FwPointersCfg.HYBRID] PASSED [ 11%]2021-01-20 04:18:06,133 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_arctic_fsck.py::test_cleanup_noop[False-data8-FwPointersCfg.ENABLED] PASSED [ 11%]2021-01-20 04:18:07,081 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_arctic_fsck.py::test_cleanup_noop[False-data9-FwPointersCfg.DISABLED] PASSED [ 11%]2021-01-20 04:18:08,039 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_arctic_fsck.py::test_cleanup_noop[False-data10-FwPointersCfg.HYBRID] PASSED [ 12%]2021-01-20 04:18:08,996 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_arctic_fsck.py::test_cleanup_noop[False-data11-FwPointersCfg.ENABLED] PASSED [ 12%]2021-01-20 04:18:09,952 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_arctic_fsck.py::test_cleanup_orphaned_chunks_ignores_recent[True-data0-FwPointersCfg.DISABLED] PASSED [ 12%]2021-01-20 04:18:10,901 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_arctic_fsck.py::test_cleanup_orphaned_chunks_ignores_recent[True-data1-FwPointersCfg.HYBRID] PASSED [ 12%]2021-01-20 04:18:11,842 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_arctic_fsck.py::test_cleanup_orphaned_chunks_ignores_recent[True-data2-FwPointersCfg.ENABLED] PASSED [ 12%]2021-01-20 04:18:12,783 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_arctic_fsck.py::test_cleanup_orphaned_chunks_ignores_recent[True-data3-FwPointersCfg.DISABLED] PASSED [ 12%]2021-01-20 04:18:13,739 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_arctic_fsck.py::test_cleanup_orphaned_chunks_ignores_recent[True-data4-FwPointersCfg.HYBRID] PASSED [ 12%]2021-01-20 04:18:14,695 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_arctic_fsck.py::test_cleanup_orphaned_chunks_ignores_recent[True-data5-FwPointersCfg.ENABLED] PASSED [ 12%]2021-01-20 04:18:15,668 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_arctic_fsck.py::test_cleanup_orphaned_chunks_ignores_recent[False-data6-FwPointersCfg.DISABLED] PASSED [ 12%]2021-01-20 04:18:16,608 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_arctic_fsck.py::test_cleanup_orphaned_chunks_ignores_recent[False-data7-FwPointersCfg.HYBRID] PASSED [ 12%]2021-01-20 04:18:17,558 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_arctic_fsck.py::test_cleanup_orphaned_chunks_ignores_recent[False-data8-FwPointersCfg.ENABLED] PASSED [ 12%]2021-01-20 04:18:18,518 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_arctic_fsck.py::test_cleanup_orphaned_chunks_ignores_recent[False-data9-FwPointersCfg.DISABLED] PASSED [ 12%]2021-01-20 04:18:19,472 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_arctic_fsck.py::test_cleanup_orphaned_chunks_ignores_recent[False-data10-FwPointersCfg.HYBRID] PASSED [ 12%]2021-01-20 04:18:20,415 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_arctic_fsck.py::test_cleanup_orphaned_chunks_ignores_recent[False-data11-FwPointersCfg.ENABLED] PASSED [ 12%]2021-01-20 04:18:21,364 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_arctic_fsck.py::test_cleanup_orphaned_chunk_doesnt_break_versions[data0-FwPointersCfg.DISABLED] PASSED [ 13%]2021-01-20 04:18:22,316 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_arctic_fsck.py::test_cleanup_orphaned_chunk_doesnt_break_versions[data1-FwPointersCfg.HYBRID] PASSED [ 13%]2021-01-20 04:18:23,283 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_arctic_fsck.py::test_cleanup_orphaned_chunk_doesnt_break_versions[data2-FwPointersCfg.ENABLED] PASSED [ 13%]2021-01-20 04:18:24,248 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_arctic_fsck.py::test_cleanup_orphaned_chunk_doesnt_break_versions[data3-FwPointersCfg.DISABLED] PASSED [ 13%]2021-01-20 04:18:25,842 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_arctic_fsck.py::test_cleanup_orphaned_chunk_doesnt_break_versions[data4-FwPointersCfg.HYBRID] PASSED [ 13%]2021-01-20 04:18:26,843 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_arctic_fsck.py::test_cleanup_orphaned_chunk_doesnt_break_versions[data5-FwPointersCfg.ENABLED] PASSED [ 13%]2021-01-20 04:18:27,844 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_arctic_fsck.py::test_cleanup_orphaned_snapshots[True-data0-FwPointersCfg.DISABLED] PASSED [ 13%]2021-01-20 04:18:28,795 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_arctic_fsck.py::test_cleanup_orphaned_snapshots[True-data1-FwPointersCfg.HYBRID] PASSED [ 13%]2021-01-20 04:18:29,746 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_arctic_fsck.py::test_cleanup_orphaned_snapshots[True-data2-FwPointersCfg.ENABLED] PASSED [ 13%]2021-01-20 04:18:30,691 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_arctic_fsck.py::test_cleanup_orphaned_snapshots[True-data3-FwPointersCfg.DISABLED] PASSED [ 13%]2021-01-20 04:18:31,663 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_arctic_fsck.py::test_cleanup_orphaned_snapshots[True-data4-FwPointersCfg.HYBRID] PASSED [ 13%]2021-01-20 04:18:32,632 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_arctic_fsck.py::test_cleanup_orphaned_snapshots[True-data5-FwPointersCfg.ENABLED] PASSED [ 13%]2021-01-20 04:18:33,621 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_arctic_fsck.py::test_cleanup_orphaned_snapshots[False-data6-FwPointersCfg.DISABLED] PASSED [ 13%]2021-01-20 04:18:34,588 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_arctic_fsck.py::test_cleanup_orphaned_snapshots[False-data7-FwPointersCfg.HYBRID] PASSED [ 14%]2021-01-20 04:18:35,551 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_arctic_fsck.py::test_cleanup_orphaned_snapshots[False-data8-FwPointersCfg.ENABLED] PASSED [ 14%]2021-01-20 04:18:36,530 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_arctic_fsck.py::test_cleanup_orphaned_snapshots[False-data9-FwPointersCfg.DISABLED] PASSED [ 14%]2021-01-20 04:18:37,513 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_arctic_fsck.py::test_cleanup_orphaned_snapshots[False-data10-FwPointersCfg.HYBRID] PASSED [ 14%]2021-01-20 04:18:38,507 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_arctic_fsck.py::test_cleanup_orphaned_snapshots[False-data11-FwPointersCfg.ENABLED] PASSED [ 14%]2021-01-20 04:18:39,490 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_arctic_fsck.py::test_cleanup_orphaned_snapshots_nop[True-data0-FwPointersCfg.DISABLED] PASSED [ 14%]2021-01-20 04:18:40,454 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_arctic_fsck.py::test_cleanup_orphaned_snapshots_nop[True-data1-FwPointersCfg.HYBRID] PASSED [ 14%]2021-01-20 04:18:41,415 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_arctic_fsck.py::test_cleanup_orphaned_snapshots_nop[True-data2-FwPointersCfg.ENABLED] PASSED [ 14%]2021-01-20 04:18:42,391 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_arctic_fsck.py::test_cleanup_orphaned_snapshots_nop[True-data3-FwPointersCfg.DISABLED] PASSED [ 14%]2021-01-20 04:18:43,357 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_arctic_fsck.py::test_cleanup_orphaned_snapshots_nop[True-data4-FwPointersCfg.HYBRID] PASSED [ 14%]2021-01-20 04:18:44,334 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_arctic_fsck.py::test_cleanup_orphaned_snapshots_nop[True-data5-FwPointersCfg.ENABLED] PASSED [ 14%]2021-01-20 04:18:45,307 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_arctic_fsck.py::test_cleanup_orphaned_snapshots_nop[False-data6-FwPointersCfg.DISABLED] PASSED [ 14%]2021-01-20 04:18:46,264 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_arctic_fsck.py::test_cleanup_orphaned_snapshots_nop[False-data7-FwPointersCfg.HYBRID] PASSED [ 14%]2021-01-20 04:18:47,232 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_arctic_fsck.py::test_cleanup_orphaned_snapshots_nop[False-data8-FwPointersCfg.ENABLED] PASSED [ 15%]2021-01-20 04:18:48,189 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_arctic_fsck.py::test_cleanup_orphaned_snapshots_nop[False-data9-FwPointersCfg.DISABLED] PASSED [ 15%]2021-01-20 04:18:49,151 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_arctic_fsck.py::test_cleanup_orphaned_snapshots_nop[False-data10-FwPointersCfg.HYBRID] PASSED [ 15%]2021-01-20 04:18:50,129 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_arctic_fsck.py::test_cleanup_orphaned_snapshots_nop[False-data11-FwPointersCfg.ENABLED] PASSED [ 15%]2021-01-20 04:18:51,106 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_arctic_fsck.py::test_dont_cleanup_recent_orphaned_snapshots[True-data0-FwPointersCfg.DISABLED] PASSED [ 15%]2021-01-20 04:18:52,066 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_arctic_fsck.py::test_dont_cleanup_recent_orphaned_snapshots[True-data1-FwPointersCfg.HYBRID] PASSED [ 15%]2021-01-20 04:18:53,030 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_arctic_fsck.py::test_dont_cleanup_recent_orphaned_snapshots[True-data2-FwPointersCfg.ENABLED] PASSED [ 15%]2021-01-20 04:18:53,992 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_arctic_fsck.py::test_dont_cleanup_recent_orphaned_snapshots[True-data3-FwPointersCfg.DISABLED] PASSED [ 15%]2021-01-20 04:18:54,952 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_arctic_fsck.py::test_dont_cleanup_recent_orphaned_snapshots[True-data4-FwPointersCfg.HYBRID] PASSED [ 15%]2021-01-20 04:18:55,925 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_arctic_fsck.py::test_dont_cleanup_recent_orphaned_snapshots[True-data5-FwPointersCfg.ENABLED] PASSED [ 15%]2021-01-20 04:18:56,909 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_arctic_fsck.py::test_dont_cleanup_recent_orphaned_snapshots[False-data6-FwPointersCfg.DISABLED] PASSED [ 15%]2021-01-20 04:18:57,872 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_arctic_fsck.py::test_dont_cleanup_recent_orphaned_snapshots[False-data7-FwPointersCfg.HYBRID] PASSED [ 15%]2021-01-20 04:18:58,853 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_arctic_fsck.py::test_dont_cleanup_recent_orphaned_snapshots[False-data8-FwPointersCfg.ENABLED] PASSED [ 15%]2021-01-20 04:18:59,814 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_arctic_fsck.py::test_dont_cleanup_recent_orphaned_snapshots[False-data9-FwPointersCfg.DISABLED] PASSED [ 15%]2021-01-20 04:19:00,773 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_arctic_fsck.py::test_dont_cleanup_recent_orphaned_snapshots[False-data10-FwPointersCfg.HYBRID] PASSED [ 16%]2021-01-20 04:19:01,743 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_arctic_fsck.py::test_dont_cleanup_recent_orphaned_snapshots[False-data11-FwPointersCfg.ENABLED] PASSED [ 16%]2021-01-20 04:19:02,751 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_copy_data.py::test_copy_data_no_force PASSED [ 16%]2021-01-20 04:19:04,609 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_copy_data.py::test_copy_data_force PASSED [ 16%]2021-01-20 04:19:05,889 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_copy_data.py::test_copy_data_splice PASSED [ 16%]2021-01-20 04:19:07,140 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_copy_data.py::test_copy_data_wild PASSED  [ 16%]2021-01-20 04:19:08,396 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_copy_data.py::test_copy_data_doesnt_exist PASSED [ 16%]2021-01-20 04:19:09,551 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_delete_library.py::test_delete_library PASSED [ 16%]2021-01-20 04:19:10,807 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_delete_library.py::test_delete_library1 PASSED [ 16%]2021-01-20 04:19:12,090 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_delete_library.py::test_delete_library2 PASSED [ 16%]2021-01-20 04:19:13,379 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_delete_library.py::test_delete_library3 PASSED [ 16%]2021-01-20 04:19:14,665 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_delete_library.py::test_delete_library_doesnt_exist PASSED [ 16%]2021-01-20 04:19:15,823 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_enable_sharding.py::test_enable_sharding PASSED [ 16%]2021-01-20 04:19:16,722 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_enable_sharding.py::test_enable_sharding_already_on_db PASSED [ 17%]2021-01-20 04:19:17,623 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_enable_sharding.py::test_enable_sharding_on_db_other_failure PASSED [ 17%]2021-01-20 04:19:18,515 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_initialize_library.py::test_init_library PASSED [ 17%]2021-01-20 04:19:19,445 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_initialize_library.py::test_init_library_no_arctic_prefix PASSED [ 17%]2021-01-20 04:19:20,371 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_initialize_library.py::test_init_library_quota PASSED [ 17%]2021-01-20 04:19:21,282 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_initialize_library.py::test_init_library_bad_library PASSED [ 17%]2021-01-20 04:19:21,935 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_list_libraries.py::test_list_library PASSED [ 17%]2021-01-20 04:19:22,865 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_list_libraries.py::test_list_library_args PASSED [ 17%]2021-01-20 04:19:23,777 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_list_libraries.py::test_list_library_args_not_found PASSED [ 17%]2021-01-20 04:19:24,689 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_prune_versions.py::test_prune_versions_symbol PASSED [ 17%]2021-01-20 04:19:25,616 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_prune_versions.py::test_prune_versions_full PASSED [ 17%]2021-01-20 04:19:26,601 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_prune_versions.py::test_keep_recent_snapshots PASSED [ 17%]2021-01-20 04:19:27,526 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_prune_versions.py::test_fix_broken_snapshot_references PASSED [ 17%]2021-01-20 04:19:28,453 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_prune_versions.py::test_keep_only_one_version PASSED [ 17%]2021-01-20 04:19:29,395 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_bitemporal_store.py::test_new_ts_read_write PASSED [ 18%]2021-01-20 04:19:30,327 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_bitemporal_store.py::test_read_ts_raw PASSED [ 18%]2021-01-20 04:19:31,271 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_bitemporal_store.py::test_write_ts_with_column_name_same_as_observed_dt_ok PASSED [ 18%]2021-01-20 04:19:32,212 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_bitemporal_store.py::test_last_update PASSED [ 18%]2021-01-20 04:19:33,160 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_bitemporal_store.py::test_existing_ts_update_and_read PASSED [ 18%]2021-01-20 04:19:34,120 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_bitemporal_store.py::test_existing_ts_update_existing_data_and_read PASSED [ 18%]2021-01-20 04:19:35,089 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_bitemporal_store.py::test_read_ts_with_historical_update PASSED [ 18%]2021-01-20 04:19:36,115 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_bitemporal_store.py::test_read_ts_with_historical_update_and_new_row PASSED [ 18%]2021-01-20 04:19:37,104 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_bitemporal_store.py::test_insert_new_rows_in_middle_remains_sorted PASSED [ 18%]2021-01-20 04:19:38,064 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_bitemporal_store.py::test_insert_versions_inbetween_works_ok PASSED [ 18%]2021-01-20 04:19:39,077 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_bitemporal_store.py::test_read_ts_raw_all_version_ok PASSED [ 18%]2021-01-20 04:19:40,113 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_bitemporal_store.py::test_bitemporal_store_saves_as_of_with_timezone PASSED [ 18%]2021-01-20 04:19:41,052 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_bitemporal_store.py::test_bitemporal_store_read_as_of_timezone PASSED [ 18%]2021-01-20 04:19:42,023 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_bitemporal_store.py::test_multi_index_ts_read_write PASSED [ 19%]2021-01-20 04:19:42,969 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_bitemporal_store.py::test_multi_index_ts_read_raw PASSED [ 19%]2021-01-20 04:19:43,913 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_bitemporal_store.py::test_multi_index_update PASSED [ 19%]2021-01-20 04:19:44,879 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_metadata_store.py::test_pickle PASSED       [ 19%]2021-01-20 04:19:45,656 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_metadata_store.py::test_has_symbol PASSED   [ 19%]2021-01-20 04:19:46,428 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_metadata_store.py::test_list_symbols PASSED [ 19%]2021-01-20 04:19:47,198 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_metadata_store.py::test_read_history PASSED [ 19%]2021-01-20 04:19:47,979 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_metadata_store.py::test_read PASSED         [ 19%]2021-01-20 04:19:48,762 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_metadata_store.py::test_write_history PASSED [ 19%]2021-01-20 04:19:49,555 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_metadata_store.py::test_append PASSED       [ 19%]2021-01-20 04:19:50,342 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_metadata_store.py::test_prepend PASSED      [ 19%]2021-01-20 04:19:51,145 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_metadata_store.py::test_pop PASSED          [ 19%]2021-01-20 04:19:51,924 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_metadata_store.py::test_purge PASSED        [ 19%]2021-01-20 04:19:52,703 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_ndarray_store.py::test_write_new_column_name_to_arctic_1_40_data PASSED [ 20%]2021-01-20 04:19:53,815 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_ndarray_store.py::test_save_read_simple_ndarray PASSED [ 20%]2021-01-20 04:19:54,751 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_ndarray_store.py::test_read_simple_ndarray_from_secondary XFAIL [ 20%]
tests/integration/store/test_ndarray_store.py::test_save_read_big_1darray[FwPointersCfg.DISABLED] PASSED [ 20%]2021-01-20 04:20:00,786 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_ndarray_store.py::test_save_read_big_1darray[FwPointersCfg.HYBRID] PASSED [ 20%]2021-01-20 04:20:06,582 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_ndarray_store.py::test_save_read_big_1darray[FwPointersCfg.ENABLED] PASSED [ 20%]2021-01-20 04:20:11,735 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_ndarray_store.py::test_save_and_resave_reuses_chunks[FwPointersCfg.DISABLED] PASSED [ 20%]2021-01-20 04:20:12,670 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_ndarray_store.py::test_save_and_resave_reuses_chunks[FwPointersCfg.HYBRID] PASSED [ 20%]2021-01-20 04:20:13,634 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_ndarray_store.py::test_save_and_resave_reuses_chunks[FwPointersCfg.ENABLED] PASSED [ 20%]2021-01-20 04:20:14,575 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_ndarray_store.py::test_save_read_big_2darray[FwPointersCfg.DISABLED] PASSED [ 20%]2021-01-20 04:20:19,597 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_ndarray_store.py::test_save_read_big_2darray[FwPointersCfg.HYBRID] PASSED [ 20%]2021-01-20 04:20:24,701 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_ndarray_store.py::test_save_read_big_2darray[FwPointersCfg.ENABLED] PASSED [ 20%]2021-01-20 04:20:29,731 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_ndarray_store.py::test_get_info_bson_object PASSED [ 20%]2021-01-20 04:20:30,646 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_ndarray_store.py::test_save_read_ndarray_with_array_field PASSED [ 20%]2021-01-20 04:20:31,558 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_ndarray_store.py::test_save_read_ndarray PASSED [ 21%]2021-01-20 04:20:32,470 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_ndarray_store.py::test_multiple_write[FwPointersCfg.DISABLED] PASSED [ 21%]2021-01-20 04:20:33,399 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_ndarray_store.py::test_multiple_write[FwPointersCfg.HYBRID] PASSED [ 21%]2021-01-20 04:20:34,352 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_ndarray_store.py::test_multiple_write[FwPointersCfg.ENABLED] PASSED [ 21%]2021-01-20 04:20:35,307 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_ndarray_store.py::test_cant_write_objects PASSED [ 21%]
tests/integration/store/test_ndarray_store.py::test_save_read_large_ndarray PASSED [ 21%]2021-01-20 04:20:36,628 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_ndarray_store.py::test_mutable_ndarray PASSED [ 21%]2021-01-20 04:20:37,571 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_ndarray_store.py::test_delete_version_shouldnt_break_read XPASS [ 21%]2021-01-20 04:20:38,506 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_ndarray_store_append.py::test_append_simple_ndarray[FwPointersCfg.DISABLED] PASSED [ 21%]2021-01-20 04:20:39,435 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_ndarray_store_append.py::test_append_simple_ndarray[FwPointersCfg.HYBRID] PASSED [ 21%]2021-01-20 04:20:40,366 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_ndarray_store_append.py::test_append_simple_ndarray[FwPointersCfg.ENABLED] PASSED [ 21%]2021-01-20 04:20:41,310 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_ndarray_store_append.py::test_append_simple_ndarray_promoting_types[FwPointersCfg.DISABLED] PASSED [ 21%]2021-01-20 04:20:42,256 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_ndarray_store_append.py::test_append_simple_ndarray_promoting_types[FwPointersCfg.HYBRID] PASSED [ 21%]2021-01-20 04:20:43,218 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_ndarray_store_append.py::test_append_simple_ndarray_promoting_types[FwPointersCfg.ENABLED] PASSED [ 22%]2021-01-20 04:20:44,192 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_ndarray_store_append.py::test_promote_types PASSED [ 22%]2021-01-20 04:20:45,115 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_ndarray_store_append.py::test_promote_types2 PASSED [ 22%]2021-01-20 04:20:46,050 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_ndarray_store_append.py::test_promote_types_smaller_sizes PASSED [ 22%]2021-01-20 04:20:46,976 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_ndarray_store_append.py::test_promote_types_larger_sizes PASSED [ 22%]2021-01-20 04:20:47,898 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_ndarray_store_append.py::test_promote_field_types_smaller_sizes PASSED [ 22%]2021-01-20 04:20:48,823 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_ndarray_store_append.py::test_promote_field_types_larger_sizes PASSED [ 22%]2021-01-20 04:20:50,374 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_ndarray_store_append.py::test_append_ndarray_with_field_shape[FwPointersCfg.DISABLED] PASSED [ 22%]2021-01-20 04:20:51,324 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_ndarray_store_append.py::test_append_ndarray_with_field_shape[FwPointersCfg.HYBRID] PASSED [ 22%]2021-01-20 04:20:52,249 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_ndarray_store_append.py::test_append_ndarray_with_field_shape[FwPointersCfg.ENABLED] PASSED [ 22%]2021-01-20 04:20:53,175 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_ndarray_store_append.py::test_append_read_large_ndarray[FwPointersCfg.DISABLED] PASSED [ 22%]2021-01-20 04:20:55,770 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_ndarray_store_append.py::test_append_read_large_ndarray[FwPointersCfg.HYBRID] PASSED [ 22%]2021-01-20 04:20:58,439 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_ndarray_store_append.py::test_append_read_large_ndarray[FwPointersCfg.ENABLED] PASSED [ 22%]2021-01-20 04:21:01,006 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_ndarray_store_append.py::test_save_append_read_ndarray[FwPointersCfg.DISABLED] PASSED [ 23%]2021-01-20 04:21:02,491 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_ndarray_store_append.py::test_save_append_read_ndarray[FwPointersCfg.HYBRID] PASSED [ 23%]2021-01-20 04:21:03,975 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_ndarray_store_append.py::test_save_append_read_ndarray[FwPointersCfg.ENABLED] PASSED [ 23%]2021-01-20 04:21:05,461 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_ndarray_store_append.py::test_save_append_read_1row_ndarray PASSED [ 23%]2021-01-20 04:21:06,940 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_ndarray_store_append.py::test_append_too_large_ndarray PASSED [ 23%]2021-01-20 04:21:08,669 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_ndarray_store_append.py::test_empty_field_append_keeps_all_columns PASSED [ 23%]2021-01-20 04:21:10,241 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_ndarray_store_append.py::test_empty_append_promotes_dtype[FwPointersCfg.DISABLED] PASSED [ 23%]2021-01-20 04:21:11,204 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_ndarray_store_append.py::test_empty_append_promotes_dtype[FwPointersCfg.HYBRID] PASSED [ 23%]2021-01-20 04:21:12,176 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_ndarray_store_append.py::test_empty_append_promotes_dtype[FwPointersCfg.ENABLED] PASSED [ 23%]2021-01-20 04:21:13,182 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_ndarray_store_append.py::test_empty_append_promotes_dtype2 PASSED [ 23%]2021-01-20 04:21:14,188 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_ndarray_store_append.py::test_empty_append_promotes_dtype3 PASSED [ 23%]2021-01-20 04:21:15,150 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_ndarray_store_append.py::test_convert_to_structured_array PASSED [ 23%]2021-01-20 04:21:16,095 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_ndarray_store_append.py::test_empty_append_concat_and_rewrite[FwPointersCfg.DISABLED] PASSED [ 23%]2021-01-20 04:21:17,116 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_ndarray_store_append.py::test_empty_append_concat_and_rewrite[FwPointersCfg.HYBRID] PASSED [ 23%]2021-01-20 04:21:18,133 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_ndarray_store_append.py::test_empty_append_concat_and_rewrite[FwPointersCfg.ENABLED] PASSED [ 24%]2021-01-20 04:21:19,099 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_ndarray_store_append.py::test_empty_append_concat_and_rewrite_2[FwPointersCfg.DISABLED] PASSED [ 24%]2021-01-20 04:21:20,279 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_ndarray_store_append.py::test_empty_append_concat_and_rewrite_2[FwPointersCfg.HYBRID] PASSED [ 24%]2021-01-20 04:21:22,086 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_ndarray_store_append.py::test_empty_append_concat_and_rewrite_2[FwPointersCfg.ENABLED] PASSED [ 24%]2021-01-20 04:21:23,273 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_ndarray_store_append.py::test_empty_append_concat_and_rewrite_3[FwPointersCfg.DISABLED] PASSED [ 24%]2021-01-20 04:21:24,259 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_ndarray_store_append.py::test_empty_append_concat_and_rewrite_3[FwPointersCfg.HYBRID] PASSED [ 24%]2021-01-20 04:21:25,221 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_ndarray_store_append.py::test_empty_append_concat_and_rewrite_3[FwPointersCfg.ENABLED] PASSED [ 24%]2021-01-20 04:21:26,187 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_ndarray_store_append.py::test_append_with_extra_columns PASSED [ 24%]2021-01-20 04:21:27,109 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_ndarray_store_append.py::test_save_append_delete_append[FwPointersCfg.DISABLED] PASSED [ 24%]2021-01-20 04:21:28,048 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_ndarray_store_append.py::test_save_append_delete_append[FwPointersCfg.HYBRID] PASSED [ 24%]2021-01-20 04:21:28,982 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_ndarray_store_append.py::test_save_append_delete_append[FwPointersCfg.ENABLED] PASSED [ 24%]2021-01-20 04:21:29,895 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_ndarray_store_append.py::test_append_after_failed_append[FwPointersCfg.DISABLED] PASSED [ 24%]2021-01-20 04:21:30,802 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_ndarray_store_append.py::test_append_after_failed_append[FwPointersCfg.HYBRID] PASSED [ 24%]2021-01-20 04:21:31,727 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_ndarray_store_append.py::test_append_after_failed_append[FwPointersCfg.ENABLED] PASSED [ 25%]2021-01-20 04:21:32,669 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_ndarray_store_append.py::test_append_reorder_columns PASSED [ 25%]2021-01-20 04:21:33,600 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_write_multi_column_to_arctic_1_40_data PASSED [ 25%]2021-01-20 04:21:34,562 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_save_read_pandas_series PASSED [ 25%]2021-01-20 04:21:35,484 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_save_read_pandas_series_maintains_name PASSED [ 25%]2021-01-20 04:21:36,388 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_save_read_pandas_series_with_multiindex PASSED [ 25%]2021-01-20 04:21:37,332 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_save_read_pandas_series_with_multiindex_and_name PASSED [ 25%]2021-01-20 04:21:38,261 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_save_read_pandas_series_with_unicode_index_name PASSED [ 25%]2021-01-20 04:21:39,183 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_save_read_pandas_dataframe_with_multiindex PASSED [ 25%]2021-01-20 04:21:40,100 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_save_read_pandas_dataframe_with_none_values PASSED [ 25%]2021-01-20 04:21:41,016 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_save_read_pandas_dataframe_with_unicode_index_name PASSED [ 25%]2021-01-20 04:21:41,944 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_cant_write_pandas_series_with_tuple_values PASSED [ 25%]2021-01-20 04:21:42,862 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_save_read_pandas_series_with_datetimeindex_with_timezone PASSED [ 25%]2021-01-20 04:21:43,781 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_save_read_pandas_series_with_datetimeindex PASSED [ 25%]2021-01-20 04:21:44,691 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_save_read_pandas_dataframe_with_datetimeindex_with_timezone PASSED [ 26%]2021-01-20 04:21:45,623 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_save_read_pandas_empty_series_with_datetime_multiindex_with_timezone PASSED [ 26%]2021-01-20 04:21:46,532 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_save_read_pandas_dataframe_with_datetimeindex PASSED [ 26%]2021-01-20 04:21:47,447 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_save_read_pandas_dataframe_with_strings PASSED [ 26%]2021-01-20 04:21:48,363 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_save_read_pandas_dataframe PASSED [ 26%]2021-01-20 04:21:49,281 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_save_read_empty_dataframe PASSED [ 26%]2021-01-20 04:21:50,194 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_save_read_pandas_dataframe2 PASSED [ 26%]2021-01-20 04:21:51,118 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_save_read_pandas_dataframe_strings PASSED [ 26%]2021-01-20 04:21:52,032 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_save_read_pandas_dataframe_empty_multiindex PASSED [ 26%]2021-01-20 04:21:52,972 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_save_read_pandas_dataframe_empty_multiindex_and_no_columns PASSED [ 26%]2021-01-20 04:21:53,894 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_save_read_pandas_dataframe_multiindex_and_no_columns PASSED [ 26%]2021-01-20 04:21:54,826 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_append_pandas_multi_columns_dataframe PASSED [ 26%]2021-01-20 04:21:55,743 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_append_pandas_multi_columns_dataframe_new_column PASSED [ 26%]2021-01-20 04:21:56,696 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_save_read_pandas_multi_columns_empty_dataframe PASSED [ 27%]2021-01-20 04:21:57,632 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_save_read_pandas_multi_columns_dataframe PASSED [ 27%]2021-01-20 04:21:58,545 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_save_read_pandas_multi_columns_no_names_dataframe PASSED [ 27%]2021-01-20 04:21:59,459 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_save_read_pandas_multi_columns_dataframe_with_int_levels PASSED [ 27%]2021-01-20 04:22:00,383 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_save_read_multi_index_and_multi_columns_dataframe PASSED [ 27%]2021-01-20 04:22:01,309 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_append_pandas_dataframe PASSED [ 27%]2021-01-20 04:22:02,255 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_empty_dataframe_multindex PASSED [ 27%]2021-01-20 04:22:03,201 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_dataframe_append_empty PASSED [ 27%]2021-01-20 04:22:04,129 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_empy_dataframe_append PASSED [ 27%]2021-01-20 04:22:05,066 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_dataframe_append_empty_multiindex PASSED [ 27%]2021-01-20 04:22:06,002 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_empty_dataframe_append_multiindex PASSED [ 27%]2021-01-20 04:22:06,950 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_empty_dataframe_should_ignore_dtype PASSED [ 27%]2021-01-20 04:22:07,885 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_empty_dataframe_should_ignore_dtype2 PASSED [ 27%]2021-01-20 04:22:08,828 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_dataframe_append_should_promote_string_column PASSED [ 28%]2021-01-20 04:22:09,757 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_dataframe_append_should_add_new_column PASSED [ 28%]2021-01-20 04:22:10,669 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_dataframe_append_should_add_new_columns_and_reorder PASSED [ 28%]2021-01-20 04:22:11,603 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_dataframe_save_read[df_size0] PASSED [ 28%]2021-01-20 04:22:12,548 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_dataframe_save_read[df_size1] PASSED [ 28%]2021-01-20 04:22:13,477 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_dataframe_save_read[df_size2] PASSED [ 28%]2021-01-20 04:22:14,405 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_dataframe_save_read[df_size3] PASSED [ 28%]2021-01-20 04:22:15,338 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_dataframe_save_read[df_size4] PASSED [ 28%]2021-01-20 04:22:16,263 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_dataframe_save_read[df_size5] PASSED [ 28%]2021-01-20 04:22:17,188 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_dataframe_save_read[df_size6] PASSED [ 28%]2021-01-20 04:22:18,115 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_dataframe_save_read[df_size7] PASSED [ 28%]2021-01-20 04:22:19,053 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_dataframe_save_read[df_size8] PASSED [ 28%]2021-01-20 04:22:19,981 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_dataframe_save_read[df_size9] PASSED [ 28%]2021-01-20 04:22:20,907 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_dataframe_save_read[df_size10] PASSED [ 28%]2021-01-20 04:22:21,831 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_dataframe_save_read[df_size11] PASSED [ 29%]2021-01-20 04:22:22,743 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_dataframe_save_read[df_size12] PASSED [ 29%]2021-01-20 04:22:24,295 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_dataframe_save_read[df_size13] PASSED [ 29%]2021-01-20 04:22:25,250 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_dataframe_save_read[df_size14] PASSED [ 29%]2021-01-20 04:22:26,190 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_dataframe_save_read[df_size15] PASSED [ 29%]2021-01-20 04:22:27,129 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_dataframe_save_read[df_size16] PASSED [ 29%]2021-01-20 04:22:28,057 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_dataframe_save_read[df_size17] PASSED [ 29%]2021-01-20 04:22:29,600 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_dataframe_save_read[df_size18] PASSED [ 29%]2021-01-20 04:22:30,531 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_dataframe_save_read[df_size19] PASSED [ 29%]2021-01-20 04:22:31,452 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_dataframe_save_append_read[df_size0] PASSED [ 29%]2021-01-20 04:22:32,382 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_dataframe_save_append_read[df_size1] PASSED [ 29%]2021-01-20 04:22:33,301 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_dataframe_save_append_read[df_size2] PASSED [ 29%]2021-01-20 04:22:34,216 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_dataframe_save_append_read[df_size3] PASSED [ 29%]2021-01-20 04:22:35,185 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_dataframe_save_append_read[df_size4] PASSED [ 30%]2021-01-20 04:22:36,133 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_dataframe_save_append_read[df_size5] PASSED [ 30%]2021-01-20 04:22:37,091 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_dataframe_save_append_read[df_size6] PASSED [ 30%]2021-01-20 04:22:38,048 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_dataframe_save_append_read[df_size7] PASSED [ 30%]2021-01-20 04:22:38,981 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_dataframe_save_append_read[df_size8] PASSED [ 30%]2021-01-20 04:22:39,910 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_dataframe_save_append_read[df_size9] PASSED [ 30%]2021-01-20 04:22:40,842 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_dataframe_save_append_read[df_size10] PASSED [ 30%]2021-01-20 04:22:41,778 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_dataframe_save_append_read[df_size11] PASSED [ 30%]2021-01-20 04:22:42,728 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_dataframe_save_append_read[df_size12] PASSED [ 30%]2021-01-20 04:22:43,656 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_dataframe_save_append_read[df_size13] PASSED [ 30%]2021-01-20 04:22:44,615 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_dataframe_save_append_read[df_size14] PASSED [ 30%]2021-01-20 04:22:45,544 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_dataframe_save_append_read[df_size15] PASSED [ 30%]2021-01-20 04:22:46,478 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_dataframe_save_append_read[df_size16] PASSED [ 30%]2021-01-20 04:22:47,423 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_dataframe_save_append_read[df_size17] PASSED [ 30%]2021-01-20 04:22:48,354 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_dataframe_save_append_read[df_size18] PASSED [ 31%]2021-01-20 04:22:49,283 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_dataframe_save_append_read[df_size19] PASSED [ 31%]2021-01-20 04:22:50,220 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_large_dataframe_append_rewrite_same_item PASSED [ 31%]2021-01-20 04:22:51,636 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_large_dataframe_rewrite_same_item PASSED [ 31%]2021-01-20 04:22:54,121 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_append_after_truncate_after_append PASSED [ 31%]2021-01-20 04:22:55,119 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_can_write_pandas_df_with_object_columns PASSED [ 31%]2021-01-20 04:22:56,062 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_panel_save_read[df_size0] XPASS [ 31%]2021-01-20 04:22:57,018 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_panel_save_read[df_size1] XPASS [ 31%]2021-01-20 04:22:57,969 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_panel_save_read[df_size2] XPASS [ 31%]2021-01-20 04:22:58,914 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_panel_save_read[df_size3] XPASS [ 31%]2021-01-20 04:22:59,856 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_panel_save_read[df_size4] XPASS [ 31%]2021-01-20 04:23:00,795 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_panel_save_read[df_size5] XPASS [ 31%]2021-01-20 04:23:01,733 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_panel_save_read[df_size6] XPASS [ 31%]2021-01-20 04:23:02,670 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_panel_save_read[df_size7] XPASS [ 32%]2021-01-20 04:23:03,599 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_panel_save_read[df_size8] XPASS [ 32%]2021-01-20 04:23:04,529 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_panel_save_read[df_size9] XPASS [ 32%]2021-01-20 04:23:05,462 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_panel_save_read_with_nans XPASS [ 32%]2021-01-20 04:23:06,376 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_save_read_ints PASSED [ 32%]2021-01-20 04:23:07,298 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_save_read_datetimes PASSED [ 32%]2021-01-20 04:23:08,211 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_labels PASSED         [ 32%]2021-01-20 04:23:09,128 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_duplicate_labels PASSED [ 32%]2021-01-20 04:23:10,050 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_no_labels PASSED      [ 32%]2021-01-20 04:23:10,980 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_no_index_labels 2021-01-20 04:23:11,993 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
XFAIL [ 32%]
tests/integration/store/test_pandas_store.py::test_not_unique PASSED     [ 32%]2021-01-20 04:23:13,183 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_daterange_end PASSED  [ 32%]2021-01-20 04:23:14,543 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_daterange_start PASSED [ 32%]2021-01-20 04:23:15,865 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_daterange_with_zero_index PASSED [ 33%]2021-01-20 04:23:16,796 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_daterange_large_DataFrame PASSED [ 33%]2021-01-20 04:23:18,215 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_daterange_large_DataFrame_middle PASSED [ 33%]2021-01-20 04:23:22,913 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_daterange[df0-assert_frame_equal] PASSED [ 33%]2021-01-20 04:23:23,961 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_daterange[df1-assert_series_equal] PASSED [ 33%]2021-01-20 04:23:24,982 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_daterange_append PASSED [ 33%]2021-01-20 04:23:26,793 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_daterange_single_chunk PASSED [ 33%]2021-01-20 04:23:27,731 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_daterange_when_end_beyond_chunk_index PASSED [ 33%]2021-01-20 04:23:28,667 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_daterange_when_end_beyond_chunk_index_no_start PASSED [ 33%]2021-01-20 04:23:29,596 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_daterange_fails_with_timezone_start PASSED [ 33%]2021-01-20 04:23:30,536 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_data_info_series PASSED [ 33%]2021-01-20 04:23:31,481 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_data_info_df PASSED   [ 33%]2021-01-20 04:23:32,405 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_data_info_cols PASSED [ 33%]2021-01-20 04:23:33,316 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_read_write_multiindex_store_keeps_timezone PASSED [ 33%]2021-01-20 04:23:34,244 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_mutable_df PASSED     [ 34%]2021-01-20 04:23:35,167 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_forced_encodings_with_df_mixed_types PASSED [ 34%]2021-01-20 04:23:36,112 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_forced_encodings_with_df PASSED [ 34%]2021-01-20 04:23:37,052 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_forced_encodings_with_df_py3 SKIPPED [ 34%]
tests/integration/store/test_pandas_store.py::test_forced_encodings_with_df_py3_multi_index SKIPPED [ 34%]
tests/integration/store/test_pickle_store.py::test_save_read_bson PASSED [ 34%]2021-01-20 04:23:37,960 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pickle_store.py::test_save_read_big_encodable PASSED [ 34%]2021-01-20 04:23:39,121 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pickle_store.py::test_save_read_bson_object PASSED [ 34%]2021-01-20 04:23:40,028 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pickle_store.py::test_get_info_bson_object PASSED [ 34%]2021-01-20 04:23:40,939 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pickle_store.py::test_bson_large_object PASSED [ 34%]2021-01-20 04:23:42,220 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pickle_store.py::test_bson_leak_objects_delete PASSED [ 34%]2021-01-20 04:23:43,146 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pickle_store.py::test_bson_leak_objects_prune_previous PASSED [ 34%]2021-01-20 04:23:44,091 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pickle_store.py::test_prune_previous_doesnt_kill_other_objects PASSED [ 34%]2021-01-20 04:23:45,013 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pickle_store.py::test_write_metadata PASSED [ 35%]2021-01-20 04:23:45,921 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_store_item_new_version PASSED [ 35%]2021-01-20 04:23:46,840 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_store_item_read_preference XFAIL [ 35%]
tests/integration/store/test_version_store.py::test_read_item_read_preference_SECONDARY 2021-01-20 04:23:48,917 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
2021-01-20 04:23:48,919 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
XFAIL [ 35%]
tests/integration/store/test_version_store.py::test_store_item_metadata[FwPointersCfg.DISABLED] PASSED [ 35%]2021-01-20 04:23:49,938 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_store_item_metadata[FwPointersCfg.HYBRID] PASSED [ 35%]2021-01-20 04:23:50,846 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_store_item_metadata[FwPointersCfg.ENABLED] PASSED [ 35%]2021-01-20 04:23:51,760 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_read_metadata[FwPointersCfg.DISABLED] PASSED [ 35%]2021-01-20 04:23:52,667 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_read_metadata[FwPointersCfg.HYBRID] PASSED [ 35%]2021-01-20 04:23:53,595 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_read_metadata[FwPointersCfg.ENABLED] PASSED [ 35%]2021-01-20 04:23:54,526 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_read_metadata_newer_version_with_lower_id[FwPointersCfg.DISABLED] PASSED [ 35%]2021-01-20 04:23:55,439 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_read_metadata_newer_version_with_lower_id[FwPointersCfg.HYBRID] PASSED [ 35%]2021-01-20 04:23:56,363 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_read_metadata_newer_version_with_lower_id[FwPointersCfg.ENABLED] PASSED [ 35%]2021-01-20 04:23:57,278 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_read_metadata_throws_on_deleted_symbol[FwPointersCfg.DISABLED] PASSED [ 35%]2021-01-20 04:23:58,220 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_read_metadata_throws_on_deleted_symbol[FwPointersCfg.HYBRID] PASSED [ 36%]2021-01-20 04:23:59,160 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_read_metadata_throws_on_deleted_symbol[FwPointersCfg.ENABLED] PASSED [ 36%]2021-01-20 04:24:00,106 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_store_item_and_update[FwPointersCfg.DISABLED] PASSED [ 36%]2021-01-20 04:24:04,092 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_store_item_and_update[FwPointersCfg.HYBRID] PASSED [ 36%]2021-01-20 04:24:08,087 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_store_item_and_update[FwPointersCfg.ENABLED] PASSED [ 36%]2021-01-20 04:24:12,067 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_append_update[FwPointersCfg.DISABLED] PASSED [ 36%]2021-01-20 04:24:13,101 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_append_update[FwPointersCfg.HYBRID] PASSED [ 36%]2021-01-20 04:24:14,116 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_append_update[FwPointersCfg.ENABLED] PASSED [ 36%]2021-01-20 04:24:15,141 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_append[FwPointersCfg.DISABLED] PASSED [ 36%]2021-01-20 04:24:16,074 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_append[FwPointersCfg.HYBRID] PASSED [ 36%]2021-01-20 04:24:17,025 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_append[FwPointersCfg.ENABLED] PASSED [ 36%]2021-01-20 04:24:17,978 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_append_should_overwrite_after_delete[FwPointersCfg.DISABLED] PASSED [ 36%]2021-01-20 04:24:18,939 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_append_should_overwrite_after_delete[FwPointersCfg.HYBRID] PASSED [ 36%]2021-01-20 04:24:19,892 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_append_should_overwrite_after_delete[FwPointersCfg.ENABLED] PASSED [ 37%]2021-01-20 04:24:20,832 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_append_empty_ts[FwPointersCfg.DISABLED] PASSED [ 37%]2021-01-20 04:24:21,747 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_append_empty_ts[FwPointersCfg.HYBRID] PASSED [ 37%]2021-01-20 04:24:22,679 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_append_empty_ts[FwPointersCfg.ENABLED] PASSED [ 37%]2021-01-20 04:24:23,595 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_append_corrupted_new_version[FwPointersCfg.DISABLED] PASSED [ 37%]2021-01-20 04:24:24,531 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_append_corrupted_new_version[FwPointersCfg.HYBRID] PASSED [ 37%]2021-01-20 04:24:25,477 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_append_corrupted_new_version[FwPointersCfg.ENABLED] PASSED [ 37%]2021-01-20 04:24:26,423 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_query_version_as_of_int PASSED [ 37%]2021-01-20 04:24:27,362 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_list_version[FwPointersCfg.DISABLED] PASSED [ 37%]2021-01-20 04:24:28,313 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_list_version[FwPointersCfg.HYBRID] PASSED [ 37%]2021-01-20 04:24:29,261 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_list_version[FwPointersCfg.ENABLED] PASSED [ 37%]2021-01-20 04:24:30,216 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_list_version_deleted PASSED [ 37%]2021-01-20 04:24:31,138 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_list_version_latest_only PASSED [ 37%]2021-01-20 04:24:32,082 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_list_version_snapshot PASSED [ 38%]2021-01-20 04:24:33,063 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_delete_versions[FwPointersCfg.DISABLED] PASSED [ 38%]2021-01-20 04:24:34,048 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_delete_versions[FwPointersCfg.HYBRID] PASSED [ 38%]2021-01-20 04:24:35,626 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_delete_versions[FwPointersCfg.ENABLED] PASSED [ 38%]2021-01-20 04:24:36,601 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_delete_bson_versions[FwPointersCfg.DISABLED] PASSED [ 38%]2021-01-20 04:24:37,564 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_delete_bson_versions[FwPointersCfg.HYBRID] PASSED [ 38%]2021-01-20 04:24:38,512 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_delete_bson_versions[FwPointersCfg.ENABLED] PASSED [ 38%]2021-01-20 04:24:39,458 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_read_none_does_not_exception[FwPointersCfg.DISABLED] PASSED [ 38%]2021-01-20 04:24:40,386 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_read_none_does_not_exception[FwPointersCfg.HYBRID] PASSED [ 38%]2021-01-20 04:24:41,302 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_read_none_does_not_exception[FwPointersCfg.ENABLED] PASSED [ 38%]2021-01-20 04:24:42,219 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_delete_item_has_symbol[FwPointersCfg.DISABLED] PASSED [ 38%]2021-01-20 04:24:43,183 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_delete_item_has_symbol[FwPointersCfg.HYBRID] PASSED [ 38%]2021-01-20 04:24:44,155 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_delete_item_has_symbol[FwPointersCfg.ENABLED] PASSED [ 38%]2021-01-20 04:24:45,132 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_delete_item_snapshot[FwPointersCfg.DISABLED] PASSED [ 38%]2021-01-20 04:24:46,117 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_delete_item_snapshot[FwPointersCfg.HYBRID] PASSED [ 39%]2021-01-20 04:24:47,107 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_delete_item_snapshot[FwPointersCfg.ENABLED] PASSED [ 39%]2021-01-20 04:24:48,094 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_has_symbol PASSED    [ 39%]2021-01-20 04:24:49,018 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_snapshot[FwPointersCfg.DISABLED] PASSED [ 39%]2021-01-20 04:24:50,006 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_snapshot[FwPointersCfg.HYBRID] PASSED [ 39%]2021-01-20 04:24:50,982 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_snapshot[FwPointersCfg.ENABLED] PASSED [ 39%]2021-01-20 04:24:51,953 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_snapshot_with_versions[FwPointersCfg.DISABLED] PASSED [ 39%]2021-01-20 04:24:52,937 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_snapshot_with_versions[FwPointersCfg.HYBRID] PASSED [ 39%]2021-01-20 04:24:53,899 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_snapshot_with_versions[FwPointersCfg.ENABLED] PASSED [ 39%]2021-01-20 04:24:54,869 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_snapshot_exclusion[FwPointersCfg.DISABLED] PASSED [ 39%]2021-01-20 04:24:55,796 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_snapshot_exclusion[FwPointersCfg.HYBRID] PASSED [ 39%]2021-01-20 04:24:56,723 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_snapshot_exclusion[FwPointersCfg.ENABLED] PASSED [ 39%]2021-01-20 04:24:57,629 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_snapshot_delete[FwPointersCfg.DISABLED] PASSED [ 39%]2021-01-20 04:24:58,580 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_snapshot_delete[FwPointersCfg.HYBRID] PASSED [ 40%]2021-01-20 04:24:59,550 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_snapshot_delete[FwPointersCfg.ENABLED] PASSED [ 40%]2021-01-20 04:25:00,528 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_multiple_snapshots[FwPointersCfg.DISABLED] PASSED [ 40%]2021-01-20 04:25:01,496 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_multiple_snapshots[FwPointersCfg.HYBRID] PASSED [ 40%]2021-01-20 04:25:02,473 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_multiple_snapshots[FwPointersCfg.ENABLED] PASSED [ 40%]2021-01-20 04:25:03,426 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_delete_identical_snapshots PASSED [ 40%]2021-01-20 04:25:04,365 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_list_snapshots PASSED [ 40%]2021-01-20 04:25:05,297 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_duplicate_snapshots PASSED [ 40%]2021-01-20 04:25:06,209 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_prunes_multiple_versions[FwPointersCfg.DISABLED] PASSED [ 40%]2021-01-20 04:25:07,185 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_prunes_multiple_versions[FwPointersCfg.HYBRID] PASSED [ 40%]2021-01-20 04:25:08,172 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_prunes_multiple_versions[FwPointersCfg.ENABLED] PASSED [ 40%]2021-01-20 04:25:09,168 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_prunes_doesnt_prune_snapshots[FwPointersCfg.DISABLED] PASSED [ 40%]2021-01-20 04:25:10,171 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_prunes_doesnt_prune_snapshots[FwPointersCfg.HYBRID] PASSED [ 40%]2021-01-20 04:25:11,171 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_prunes_doesnt_prune_snapshots[FwPointersCfg.ENABLED] PASSED [ 41%]2021-01-20 04:25:12,128 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_prunes_multiple_versions_ts[FwPointersCfg.DISABLED] PASSED [ 41%]2021-01-20 04:25:13,096 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_prunes_multiple_versions_ts[FwPointersCfg.HYBRID] PASSED [ 41%]2021-01-20 04:25:14,068 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_prunes_multiple_versions_ts[FwPointersCfg.ENABLED] PASSED [ 41%]2021-01-20 04:25:15,047 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_prunes_doesnt_prune_snapshots_ts[FwPointersCfg.DISABLED] PASSED [ 41%]2021-01-20 04:25:16,077 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_prunes_doesnt_prune_snapshots_ts[FwPointersCfg.HYBRID] PASSED [ 41%]2021-01-20 04:25:17,079 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_prunes_doesnt_prune_snapshots_ts[FwPointersCfg.ENABLED] PASSED [ 41%]2021-01-20 04:25:18,094 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_prunes_multiple_versions_fully_different_tss[FwPointersCfg.DISABLED] PASSED [ 41%]2021-01-20 04:25:19,083 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_prunes_multiple_versions_fully_different_tss[FwPointersCfg.HYBRID] PASSED [ 41%]2021-01-20 04:25:20,063 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_prunes_multiple_versions_fully_different_tss[FwPointersCfg.ENABLED] PASSED [ 41%]2021-01-20 04:25:21,039 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_prunes_doesnt_prune_snapshots_fully_different_tss[FwPointersCfg.DISABLED] PASSED [ 41%]2021-01-20 04:25:22,065 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_prunes_doesnt_prune_snapshots_fully_different_tss[FwPointersCfg.HYBRID] PASSED [ 41%]2021-01-20 04:25:23,100 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_prunes_doesnt_prune_snapshots_fully_different_tss[FwPointersCfg.ENABLED] PASSED [ 41%]2021-01-20 04:25:24,152 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_prunes_previous_version_append_interaction[FwPointersCfg.DISABLED] PASSED [ 41%]2021-01-20 04:25:25,205 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_prunes_previous_version_append_interaction[FwPointersCfg.HYBRID] PASSED [ 42%]2021-01-20 04:25:26,242 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_prunes_previous_version_append_interaction[FwPointersCfg.ENABLED] PASSED [ 42%]2021-01-20 04:25:27,257 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_list_symbols[FwPointersCfg.DISABLED] PASSED [ 42%]2021-01-20 04:25:28,174 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_list_symbols[FwPointersCfg.HYBRID] PASSED [ 42%]2021-01-20 04:25:29,103 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_list_symbols[FwPointersCfg.ENABLED] PASSED [ 42%]2021-01-20 04:25:30,039 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_list_symbols_regex[FwPointersCfg.DISABLED] PASSED [ 42%]2021-01-20 04:25:30,974 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_list_symbols_regex[FwPointersCfg.HYBRID] PASSED [ 42%]2021-01-20 04:25:31,907 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_list_symbols_regex[FwPointersCfg.ENABLED] PASSED [ 42%]2021-01-20 04:25:32,836 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_list_symbols_newer_version_with_lower_id[FwPointersCfg.DISABLED] PASSED [ 42%]2021-01-20 04:25:33,764 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_list_symbols_newer_version_with_lower_id[FwPointersCfg.HYBRID] PASSED [ 42%]2021-01-20 04:25:34,690 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_list_symbols_newer_version_with_lower_id[FwPointersCfg.ENABLED] PASSED [ 42%]2021-01-20 04:25:35,619 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_list_symbols_write_snapshot_write_delete[FwPointersCfg.DISABLED] PASSED [ 42%]2021-01-20 04:25:36,556 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_list_symbols_write_snapshot_write_delete[FwPointersCfg.HYBRID] PASSED [ 42%]2021-01-20 04:25:38,094 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_list_symbols_write_snapshot_write_delete[FwPointersCfg.ENABLED] PASSED [ 43%]2021-01-20 04:25:39,033 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_list_symbols_delete_write[FwPointersCfg.DISABLED] PASSED [ 43%]2021-01-20 04:25:39,968 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_list_symbols_delete_write[FwPointersCfg.HYBRID] PASSED [ 43%]2021-01-20 04:25:40,884 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_list_symbols_delete_write[FwPointersCfg.ENABLED] PASSED [ 43%]2021-01-20 04:25:41,827 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_date_range_large[FwPointersCfg.DISABLED] PASSED [ 43%]2021-01-20 04:25:42,888 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_date_range_large[FwPointersCfg.HYBRID] PASSED [ 43%]2021-01-20 04:25:43,936 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_date_range_large[FwPointersCfg.ENABLED] PASSED [ 43%]2021-01-20 04:25:44,990 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_append_after_empty[FwPointersCfg.DISABLED] PASSED [ 43%]2021-01-20 04:25:49,197 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_append_after_empty[FwPointersCfg.HYBRID] PASSED [ 43%]2021-01-20 04:25:53,416 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_append_after_empty[FwPointersCfg.ENABLED] PASSED [ 43%]2021-01-20 04:25:57,663 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_write_metadata[FwPointersCfg.DISABLED] PASSED [ 43%]2021-01-20 04:25:58,634 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_write_metadata[FwPointersCfg.HYBRID] PASSED [ 43%]2021-01-20 04:25:59,586 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_write_metadata[FwPointersCfg.ENABLED] PASSED [ 43%]2021-01-20 04:26:00,533 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_write_metadata_followed_by_append[FwPointersCfg.DISABLED] PASSED [ 43%]2021-01-20 04:26:03,479 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_write_metadata_followed_by_append[FwPointersCfg.HYBRID] PASSED [ 44%]2021-01-20 04:26:06,426 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_write_metadata_followed_by_append[FwPointersCfg.ENABLED] PASSED [ 44%]2021-01-20 04:26:09,368 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_write_metadata_new_symbol[FwPointersCfg.DISABLED] PASSED [ 44%]2021-01-20 04:26:10,303 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_write_metadata_new_symbol[FwPointersCfg.HYBRID] PASSED [ 44%]2021-01-20 04:26:11,215 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_write_metadata_new_symbol[FwPointersCfg.ENABLED] PASSED [ 44%]2021-01-20 04:26:12,145 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_write_metadata_after_append[FwPointersCfg.DISABLED] PASSED [ 44%]2021-01-20 04:26:13,093 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_write_metadata_after_append[FwPointersCfg.HYBRID] PASSED [ 44%]2021-01-20 04:26:14,075 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_write_metadata_after_append[FwPointersCfg.ENABLED] PASSED [ 44%]2021-01-20 04:26:15,042 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_write_metadata_purge_previous_versions[FwPointersCfg.DISABLED] PASSED [ 44%]2021-01-20 04:26:18,023 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_write_metadata_purge_previous_versions[FwPointersCfg.HYBRID] PASSED [ 44%]2021-01-20 04:26:21,029 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_write_metadata_purge_previous_versions[FwPointersCfg.ENABLED] PASSED [ 44%]2021-01-20 04:26:24,047 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_write_metadata_delete_symbol[FwPointersCfg.DISABLED] PASSED [ 44%]2021-01-20 04:26:25,658 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_write_metadata_delete_symbol[FwPointersCfg.HYBRID] PASSED [ 44%]2021-01-20 04:26:27,295 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_write_metadata_delete_symbol[FwPointersCfg.ENABLED] PASSED [ 45%]2021-01-20 04:26:28,904 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_write_metadata_snapshots[FwPointersCfg.DISABLED] PASSED [ 45%]2021-01-20 04:26:29,874 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_write_metadata_snapshots[FwPointersCfg.HYBRID] PASSED [ 45%]2021-01-20 04:26:31,438 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_write_metadata_snapshots[FwPointersCfg.ENABLED] PASSED [ 45%]2021-01-20 04:26:32,421 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_restore_version[FwPointersCfg.DISABLED] PASSED [ 45%]2021-01-20 04:26:33,391 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_restore_version[FwPointersCfg.HYBRID] PASSED [ 45%]2021-01-20 04:26:34,362 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_restore_version[FwPointersCfg.ENABLED] PASSED [ 45%]2021-01-20 04:26:35,311 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_restore_version_followed_by_append[FwPointersCfg.DISABLED] PASSED [ 45%]2021-01-20 04:26:38,291 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_restore_version_followed_by_append[FwPointersCfg.HYBRID] PASSED [ 45%]2021-01-20 04:26:41,257 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_restore_version_followed_by_append[FwPointersCfg.ENABLED] PASSED [ 45%]2021-01-20 04:26:44,217 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_restore_version_purging_previous_versions[FwPointersCfg.DISABLED] PASSED [ 45%]2021-01-20 04:26:47,193 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_restore_version_purging_previous_versions[FwPointersCfg.HYBRID] PASSED [ 45%]2021-01-20 04:26:50,157 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_restore_version_purging_previous_versions[FwPointersCfg.ENABLED] PASSED [ 45%]2021-01-20 04:26:53,110 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_restore_version_non_existent_version[FwPointersCfg.DISABLED] PASSED [ 46%]2021-01-20 04:26:54,642 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_restore_version_non_existent_version[FwPointersCfg.HYBRID] PASSED [ 46%]2021-01-20 04:26:55,568 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_restore_version_non_existent_version[FwPointersCfg.ENABLED] PASSED [ 46%]2021-01-20 04:26:56,481 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_restore_version_which_updated_only_metadata[FwPointersCfg.DISABLED] PASSED [ 46%]2021-01-20 04:26:57,456 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_restore_version_which_updated_only_metadata[FwPointersCfg.HYBRID] PASSED [ 46%]2021-01-20 04:26:58,431 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_restore_version_which_updated_only_metadata[FwPointersCfg.ENABLED] PASSED [ 46%]2021-01-20 04:26:59,383 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_restore_version_then_snapshot[FwPointersCfg.DISABLED] PASSED [ 46%]2021-01-20 04:27:00,345 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_restore_version_then_snapshot[FwPointersCfg.HYBRID] PASSED [ 46%]2021-01-20 04:27:01,291 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_restore_version_then_snapshot[FwPointersCfg.ENABLED] PASSED [ 46%]2021-01-20 04:27:02,243 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_restore_version_latest_snapshot_noop[FwPointersCfg.DISABLED] PASSED [ 46%]2021-01-20 04:27:03,221 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_restore_version_latest_snapshot_noop[FwPointersCfg.HYBRID] PASSED [ 46%]2021-01-20 04:27:04,163 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_restore_version_latest_snapshot_noop[FwPointersCfg.ENABLED] PASSED [ 46%]2021-01-20 04:27:05,117 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_restore_version_latest_version_noop[FwPointersCfg.DISABLED] PASSED [ 46%]2021-01-20 04:27:06,046 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_restore_version_latest_version_noop[FwPointersCfg.HYBRID] PASSED [ 46%]2021-01-20 04:27:06,965 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_restore_version_latest_version_noop[FwPointersCfg.ENABLED] PASSED [ 47%]2021-01-20 04:27:07,883 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_restore_version_snap_delete_symbol_restore[FwPointersCfg.DISABLED] PASSED [ 47%]2021-01-20 04:27:08,846 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_restore_version_snap_delete_symbol_restore[FwPointersCfg.HYBRID] PASSED [ 47%]2021-01-20 04:27:09,803 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_restore_version_snap_delete_symbol_restore[FwPointersCfg.ENABLED] PASSED [ 47%]2021-01-20 04:27:10,772 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_restore_from_version_with_deleted_symbol[FwPointersCfg.DISABLED] PASSED [ 47%]2021-01-20 04:27:11,700 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_restore_from_version_with_deleted_symbol[FwPointersCfg.HYBRID] PASSED [ 47%]2021-01-20 04:27:12,622 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_restore_from_version_with_deleted_symbol[FwPointersCfg.ENABLED] PASSED [ 47%]2021-01-20 04:27:13,575 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_prune_previous_versions_retries_on_cleanup_error[FwPointersCfg.DISABLED] PASSED [ 47%]2021-01-20 04:27:14,547 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_prune_previous_versions_retries_on_cleanup_error[FwPointersCfg.HYBRID] PASSED [ 47%]2021-01-20 04:27:15,520 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_prune_previous_versions_retries_on_cleanup_error[FwPointersCfg.ENABLED] PASSED [ 47%]2021-01-20 04:27:16,510 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_prune_previous_versions_retries_find_calls[FwPointersCfg.DISABLED] PASSED [ 47%]2021-01-20 04:27:17,671 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_prune_previous_versions_retries_find_calls[FwPointersCfg.HYBRID] PASSED [ 47%]2021-01-20 04:27:18,787 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_prune_previous_versions_retries_find_calls[FwPointersCfg.ENABLED] PASSED [ 47%]2021-01-20 04:27:19,928 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_append_does_not_duplicate_data_when_prune_fails[FwPointersCfg.DISABLED] PASSED [ 48%]2021-01-20 04:27:20,928 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_append_does_not_duplicate_data_when_prune_fails[FwPointersCfg.HYBRID] PASSED [ 48%]2021-01-20 04:27:21,912 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_append_does_not_duplicate_data_when_prune_fails[FwPointersCfg.ENABLED] PASSED [ 48%]2021-01-20 04:27:22,885 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_write_does_not_succeed_with_a_prune_error[FwPointersCfg.DISABLED] PASSED [ 48%]2021-01-20 04:27:23,794 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_write_does_not_succeed_with_a_prune_error[FwPointersCfg.HYBRID] PASSED [ 48%]2021-01-20 04:27:24,736 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_write_does_not_succeed_with_a_prune_error[FwPointersCfg.ENABLED] PASSED [ 48%]2021-01-20 04:27:25,668 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_prune_keeps_version[FwPointersCfg.DISABLED] PASSED [ 48%]2021-01-20 04:27:26,607 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_prune_keeps_version[FwPointersCfg.HYBRID] PASSED [ 48%]2021-01-20 04:27:27,543 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_prune_keeps_version[FwPointersCfg.ENABLED] PASSED [ 48%]2021-01-20 04:27:28,480 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_empty_string_column_name PASSED [ 48%]2021-01-20 04:27:29,392 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_snapshot_list_versions_after_delete[FwPointersCfg.DISABLED] PASSED [ 48%]2021-01-20 04:27:30,334 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_snapshot_list_versions_after_delete[FwPointersCfg.HYBRID] PASSED [ 48%]2021-01-20 04:27:31,287 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_snapshot_list_versions_after_delete[FwPointersCfg.ENABLED] PASSED [ 48%]2021-01-20 04:27:32,219 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_write_non_serializable_throws PASSED [ 48%]2021-01-20 04:27:33,143 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_write_non_serializable_pickling_default[FwPointersCfg.DISABLED] PASSED [ 49%]2021-01-20 04:27:34,075 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_write_non_serializable_pickling_default[FwPointersCfg.HYBRID] PASSED [ 49%]2021-01-20 04:27:35,013 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_write_non_serializable_pickling_default[FwPointersCfg.ENABLED] PASSED [ 49%]2021-01-20 04:27:35,946 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_write_strict_no_daterange[FwPointersCfg.DISABLED] PASSED [ 49%]2021-01-20 04:27:36,857 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_write_strict_no_daterange[FwPointersCfg.HYBRID] PASSED [ 49%]2021-01-20 04:27:37,791 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_write_strict_no_daterange[FwPointersCfg.ENABLED] PASSED [ 49%]2021-01-20 04:27:38,712 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_handler_check_default_false PASSED [ 49%]2021-01-20 04:27:39,605 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_handler_check_default_osenviron PASSED [ 49%]2021-01-20 04:27:40,498 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_handler_check_set_false PASSED [ 49%]2021-01-20 04:27:41,403 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_handler_check_set_true PASSED [ 49%]2021-01-20 04:27:42,329 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_write_df_with_objects_in_index PASSED [ 49%]2021-01-20 04:27:43,269 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_write_series_with_objects_in_index PASSED [ 49%]2021-01-20 04:27:44,216 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_write_series_with_some_objects[input_series0] PASSED [ 49%]2021-01-20 04:27:45,155 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_write_series_with_some_objects[input_series1] PASSED [ 50%]2021-01-20 04:27:46,110 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_can_write_tz_aware_data_df[FwPointersCfg.DISABLED] PASSED [ 50%]2021-01-20 04:27:47,063 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_can_write_tz_aware_data_df[FwPointersCfg.HYBRID] PASSED [ 50%]2021-01-20 04:27:47,979 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_can_write_tz_aware_data_df[FwPointersCfg.ENABLED] PASSED [ 50%]2021-01-20 04:27:48,898 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_can_write_tz_aware_data_series[FwPointersCfg.DISABLED] PASSED [ 50%]2021-01-20 04:27:49,821 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_can_write_tz_aware_data_series[FwPointersCfg.HYBRID] PASSED [ 50%]2021-01-20 04:27:51,333 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_can_write_tz_aware_data_series[FwPointersCfg.ENABLED] PASSED [ 50%]2021-01-20 04:27:52,248 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_fwpointers_mixed_scenarios[FwPointersCfg.DISABLED-FwPointersCfg.DISABLED-FwPointersCfg.DISABLED-FwPointersCfg.DISABLED] PASSED [ 50%]2021-01-20 04:27:53,233 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_fwpointers_mixed_scenarios[FwPointersCfg.ENABLED-FwPointersCfg.ENABLED-FwPointersCfg.ENABLED-FwPointersCfg.ENABLED] PASSED [ 50%]2021-01-20 04:27:54,231 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_fwpointers_mixed_scenarios[FwPointersCfg.HYBRID-FwPointersCfg.HYBRID-FwPointersCfg.HYBRID-FwPointersCfg.HYBRID] PASSED [ 50%]2021-01-20 04:27:55,211 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_fwpointers_mixed_scenarios[FwPointersCfg.HYBRID-FwPointersCfg.DISABLED-FwPointersCfg.HYBRID-FwPointersCfg.DISABLED] PASSED [ 50%]2021-01-20 04:27:56,193 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_fwpointers_mixed_scenarios[FwPointersCfg.HYBRID-FwPointersCfg.ENABLED-FwPointersCfg.HYBRID-FwPointersCfg.ENABLED] PASSED [ 50%]2021-01-20 04:27:57,203 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_fwpointers_mixed_scenarios[FwPointersCfg.ENABLED-FwPointersCfg.HYBRID-FwPointersCfg.ENABLED-FwPointersCfg.HYBRID] PASSED [ 50%]2021-01-20 04:27:58,183 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_fwpointers_mixed_scenarios[FwPointersCfg.DISABLED-FwPointersCfg.HYBRID-FwPointersCfg.DISABLED-FwPointersCfg.HYBRID] PASSED [ 51%]2021-01-20 04:27:59,160 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_fwpointers_mixed_scenarios[FwPointersCfg.DISABLED-FwPointersCfg.ENABLED-FwPointersCfg.DISABLED-FwPointersCfg.ENABLED] PASSED [ 51%]2021-01-20 04:28:00,149 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_fwpointers_mixed_scenarios[FwPointersCfg.ENABLED-FwPointersCfg.DISABLED-FwPointersCfg.ENABLED-FwPointersCfg.DISABLED] PASSED [ 51%]2021-01-20 04:28:01,131 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_fwpointers_mixed_scenarios[FwPointersCfg.ENABLED-FwPointersCfg.ENABLED-FwPointersCfg.DISABLED-FwPointersCfg.DISABLED] PASSED [ 51%]2021-01-20 04:28:02,157 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_fwpointers_mixed_scenarios[FwPointersCfg.ENABLED-FwPointersCfg.ENABLED-FwPointersCfg.HYBRID-FwPointersCfg.DISABLED] PASSED [ 51%]2021-01-20 04:28:03,186 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_fwpointers_mixed_scenarios[FwPointersCfg.ENABLED-FwPointersCfg.ENABLED-FwPointersCfg.HYBRID-FwPointersCfg.ENABLED] PASSED [ 51%]2021-01-20 04:28:04,211 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_fwpointers_writemetadata_enabled_disabled PASSED [ 51%]2021-01-20 04:28:05,216 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_fwpointer_enabled_write_delete_keep_version_append PASSED [ 51%]2021-01-20 04:28:06,191 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_version_arctic_version PASSED [ 51%]2021-01-20 04:28:07,722 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_prune_mixed_fwpointer_configs PASSED [ 51%]2021-01-20 04:28:14,029 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_prune_crossref_fwpointer_configs[FwPointersCfg.DISABLED-FwPointersCfg.HYBRID] PASSED [ 51%]2021-01-20 04:28:18,078 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_prune_crossref_fwpointer_configs[FwPointersCfg.DISABLED-FwPointersCfg.ENABLED] PASSED [ 51%]2021-01-20 04:28:22,006 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_prune_crossref_fwpointer_configs[FwPointersCfg.HYBRID-FwPointersCfg.DISABLED] PASSED [ 51%]2021-01-20 04:28:25,979 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_prune_crossref_fwpointer_configs[FwPointersCfg.HYBRID-FwPointersCfg.ENABLED] PASSED [ 51%]2021-01-20 04:28:29,797 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_prune_crossref_fwpointer_configs[FwPointersCfg.ENABLED-FwPointersCfg.HYBRID] PASSED [ 52%]2021-01-20 04:28:33,709 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_prune_crossref_fwpointer_configs[FwPointersCfg.ENABLED-FwPointersCfg.DISABLED] PASSED [ 52%]2021-01-20 04:28:38,164 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store_audit.py::test_ArcticTransaction_can_do_first_writes PASSED [ 52%]2021-01-20 04:28:39,119 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store_audit.py::test_ArcticTransaction_detects_concurrent_writes PASSED [ 52%]2021-01-20 04:28:40,121 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store_audit.py::test_audit_writes PASSED [ 52%]2021-01-20 04:28:41,099 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store_audit.py::test_metadata_changes_writes PASSED [ 52%]2021-01-20 04:28:42,085 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store_audit.py::test_audit_read PASSED [ 52%]2021-01-20 04:28:43,088 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store_audit.py::test_cleanup_orphaned_versions_integration PASSED [ 52%]2021-01-20 04:28:44,035 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store_audit.py::test_corrupted_read_writes_new PASSED [ 52%]2021-01-20 04:28:45,058 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store_audit.py::test_write_after_delete PASSED [ 52%]2021-01-20 04:28:46,040 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store_audit.py::test_ArcticTransaction_write_skips_for_exact_match PASSED [ 52%]2021-01-20 04:28:47,014 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store_audit.py::test_ArcticTransaction_write_doesnt_skip_for_close_ts PASSED [ 52%]2021-01-20 04:28:47,969 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store_corruption.py::test_no_corruption_restore_append_overlapping PASSED [ 52%]2021-01-20 04:28:50,176 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store_corruption.py::test_no_corruption_restore_writemeta_append PASSED [ 53%]2021-01-20 04:28:52,248 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store_corruption.py::test_no_corruption_restore_append_non_overlapping_tstamps PASSED [ 53%]2021-01-20 04:28:55,854 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store_corruption.py::test_restore_append_overlapping_corrupts_old PASSED [ 53%]2021-01-20 04:28:57,358 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store_corruption.py::test_restore_append_overlapping_corrupts_last PASSED [ 53%]2021-01-20 04:28:58,861 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store_corruption.py::test_append_fail_after_delete_noupsert SKIPPED [ 53%]
tests/integration/store/test_version_store_corruption.py::test_append_without_corrupt_check PASSED [ 53%]
tests/integration/store/test_version_store_corruption.py::test_append_with_corrupt_check PASSED [ 53%]2021-01-20 04:29:08,305 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store_corruption.py::test_fast_check_corruption PASSED [ 53%]2021-01-20 04:29:09,293 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store_corruption.py::test_fast_is_safe_to_append PASSED [ 53%]
tests/integration/tickstore/test_toplevel.py::test_should_return_libraries_for_the_given_daterange[start0-end0-expected0] PASSED [ 53%]2021-01-20 04:29:23,920 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/tickstore/test_toplevel.py::test_should_return_libraries_for_the_given_daterange[start1-end1-expected1] PASSED [ 53%]2021-01-20 04:29:24,683 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/tickstore/test_toplevel.py::test_should_return_libraries_for_the_given_daterange[start2-end2-expected2] PASSED [ 53%]2021-01-20 04:29:25,445 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/tickstore/test_toplevel.py::test_should_return_libraries_for_the_given_daterange[start3-end3-expected3] PASSED [ 53%]2021-01-20 04:29:26,202 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/tickstore/test_toplevel.py::test_should_return_libraries_for_the_given_daterange[start4-end4-expected4] PASSED [ 53%]2021-01-20 04:29:26,979 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/tickstore/test_toplevel.py::test_should_return_libraries_for_the_given_daterange[start5-end5-expected5] PASSED [ 54%]2021-01-20 04:29:27,754 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/tickstore/test_toplevel.py::test_should_return_libraries_for_the_given_daterange[start6-end6-expected6] PASSED [ 54%]2021-01-20 04:29:28,516 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/tickstore/test_toplevel.py::test_should_return_libraries_for_the_given_daterange[start7-end7-expected7] PASSED [ 54%]2021-01-20 04:29:29,271 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/tickstore/test_toplevel.py::test_should_return_libraries_for_the_given_daterange[start8-end8-expected8] PASSED [ 54%]2021-01-20 04:29:30,021 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/tickstore/test_toplevel.py::test_should_raise_exceptions_if_no_libraries_are_found_in_the_date_range_when_reading_data PASSED [ 54%]
tests/integration/tickstore/test_toplevel.py::test_should_return_data_when_date_range_falls_in_a_single_underlying_library PASSED [ 54%]2021-01-20 04:29:31,775 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/tickstore/test_toplevel.py::test_should_return_data_when_date_range_spans_libraries PASSED [ 54%]2021-01-20 04:29:32,782 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/tickstore/test_toplevel.py::test_should_return_data_when_date_range_spans_libraries_even_if_one_returns_nothing PASSED [ 54%]2021-01-20 04:29:33,776 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/tickstore/test_toplevel.py::test_should_add_underlying_library_where_none_exists PASSED [ 54%]2021-01-20 04:29:34,634 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/tickstore/test_toplevel.py::test_should_add_underlying_library_where_another_library_exists_in_a_non_overlapping_daterange PASSED [ 54%]2021-01-20 04:29:35,493 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/tickstore/test_toplevel.py::test_should_raise_exception_if_library_does_not_exist PASSED [ 54%]
tests/integration/tickstore/test_toplevel.py::test_should_raise_exception_if_date_range_for_library_overlaps_with_existing_libraries PASSED [ 54%]
tests/integration/tickstore/test_toplevel.py::test_should_successfully_do_a_roundtrip_write_and_read_spanning_multiple_underlying_libraries XPASS [ 54%]2021-01-20 04:29:38,246 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/tickstore/test_toplevel.py::test_should_list_symbols_from_the_underlying_library[start0-end0-0-10] PASSED [ 55%]2021-01-20 04:29:39,309 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/tickstore/test_toplevel.py::test_should_list_symbols_from_the_underlying_library[start1-end1-0-8] PASSED [ 55%]2021-01-20 04:29:40,359 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/tickstore/test_toplevel.py::test_should_list_symbols_from_the_underlying_library[start2-end2-7-10] PASSED [ 55%]2021-01-20 04:29:41,383 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/tickstore/test_toplevel.py::test_should_add_underlying_libraries_when_intialized PASSED [ 55%]2021-01-20 04:29:42,353 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/tickstore/test_toplevel.py::test_should_write_top_level_with_list_of_dicts PASSED [ 55%]2021-01-20 04:29:43,343 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/tickstore/test_toplevel.py::test_should_write_top_level_with_correct_timezone PASSED [ 55%]2021-01-20 04:29:44,353 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/tickstore/test_toplevel.py::test_min_max_date PASSED   [ 55%]2021-01-20 04:29:45,158 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/tickstore/test_toplevel.py::test_no_min_max_date PASSED [ 55%]2021-01-20 04:29:45,966 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/tickstore/test_toplevel.py::test_get_libraries_no_data_raises_exception PASSED [ 55%]2021-01-20 04:29:46,727 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/tickstore/test_toplevel.py::test_get_libraries_no_data_raises_exception_tzinfo_given PASSED [ 55%]2021-01-20 04:29:47,481 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/tickstore/test_toplevel.py::test_get_library_metadata PASSED [ 55%]2021-01-20 04:29:48,439 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/tickstore/test_ts_delete.py::test_delete[tickstore] PASSED [ 55%]2021-01-20 04:29:49,245 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/tickstore/test_ts_delete.py::test_delete_daterange[tickstore] PASSED [ 55%]2021-01-20 04:29:50,056 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/tickstore/test_ts_read.py::test_read[tickstore] PASSED [ 56%]2021-01-20 04:29:50,864 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/tickstore/test_ts_read.py::test_read_data_is_modifiable[tickstore] PASSED [ 56%]2021-01-20 04:29:51,671 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/tickstore/test_ts_read.py::test_read_allow_secondary[tickstore] PASSED [ 56%]2021-01-20 04:29:52,491 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/tickstore/test_ts_read.py::test_read_symbol_as_column[tickstore] PASSED [ 56%]2021-01-20 04:29:53,292 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/tickstore/test_ts_read.py::test_read_multiple_symbols[tickstore] PASSED [ 56%]2021-01-20 04:29:54,107 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/tickstore/test_ts_read.py::test_read_all_cols_all_dtypes[tickstore-1] PASSED [ 56%]2021-01-20 04:29:54,918 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/tickstore/test_ts_read.py::test_read_all_cols_all_dtypes[tickstore-100] PASSED [ 56%]2021-01-20 04:29:55,725 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/tickstore/test_ts_read.py::test_date_range[tickstore] PASSED [ 56%]2021-01-20 04:29:56,598 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/tickstore/test_ts_read.py::test_date_range_end_not_in_range[tickstore] PASSED [ 56%]2021-01-20 04:29:57,399 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/tickstore/test_ts_read.py::test_date_range_default_timezone[tickstore-UTC] PASSED [ 56%]2021-01-20 04:29:58,216 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/tickstore/test_ts_read.py::test_date_range_default_timezone[tickstore-Europe/London] PASSED [ 56%]2021-01-20 04:29:59,045 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/tickstore/test_ts_read.py::test_date_range_default_timezone[tickstore-America/New_York] PASSED [ 56%]2021-01-20 04:29:59,877 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/tickstore/test_ts_read.py::test_date_range_no_bounds[tickstore] PASSED [ 56%]2021-01-20 04:30:00,707 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/tickstore/test_ts_read.py::test_date_range_BST[tickstore] PASSED [ 56%]2021-01-20 04:30:01,521 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/tickstore/test_ts_read.py::test_read_no_data[tickstore] PASSED [ 57%]2021-01-20 04:30:02,319 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/tickstore/test_ts_read.py::test_write_no_tz[tickstore] PASSED [ 57%]2021-01-20 04:30:03,122 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/tickstore/test_ts_read.py::test_read_out_of_order[tickstore] PASSED [ 57%]2021-01-20 04:30:03,956 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/tickstore/test_ts_read.py::test_read_chunk_boundaries[tickstore] PASSED [ 57%]2021-01-20 04:30:04,785 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/tickstore/test_ts_read.py::test_read_spanning_chunks[tickstore] PASSED [ 57%]2021-01-20 04:30:05,600 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/tickstore/test_ts_read.py::test_read_inside_range[tickstore] PASSED [ 57%]2021-01-20 04:30:06,409 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/tickstore/test_ts_read.py::test_read_longs[tickstore] PASSED [ 57%]2021-01-20 04:30:07,226 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/tickstore/test_ts_read.py::test_read_with_image[tickstore] PASSED [ 57%]2021-01-20 04:30:08,052 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/tickstore/test_ts_read.py::test_read_with_metadata[tickstore] PASSED [ 57%]2021-01-20 04:30:08,843 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/tickstore/test_ts_read.py::test_read_strings[tickstore] PASSED [ 57%]2021-01-20 04:30:09,633 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/tickstore/test_ts_read.py::test_read_utf8_strings[tickstore] PASSED [ 57%]2021-01-20 04:30:10,423 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/tickstore/test_ts_read.py::test_read_unicode_strings[tickstore] PASSED [ 57%]2021-01-20 04:30:11,210 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/tickstore/test_ts_read.py::test_objects_fail[tickstore] PASSED [ 57%]
tests/integration/tickstore/test_ts_write.py::test_ts_write_simple[tickstore] PASSED [ 58%]2021-01-20 04:30:13,468 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/tickstore/test_ts_write.py::test_overlapping_load[tickstore] PASSED [ 58%]2021-01-20 04:30:14,306 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/tickstore/test_ts_write.py::test_ts_write_pandas[tickstore] PASSED [ 58%]2021-01-20 04:30:15,154 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/tickstore/test_ts_write.py::test_ts_write_named_col[tickstore] PASSED [ 58%]2021-01-20 04:30:16,601 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/tickstore/test_ts_write.py::test_millisecond_roundtrip[tickstore] PASSED [ 58%]2021-01-20 04:30:17,415 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/unit/test_arctic.py::test_arctic_lazy_init PASSED                  [ 58%]
tests/unit/test_arctic.py::test_arctic_lazy_init_ssl_true PASSED         [ 58%]
tests/unit/test_arctic.py::test_connection_passed_warning_raised PASSED  [ 58%]
tests/unit/test_arctic.py::test_arctic_auth PASSED                       [ 58%]
tests/unit/test_arctic.py::test_arctic_auth_custom_app_name PASSED       [ 58%]
tests/unit/test_arctic.py::test_arctic_connect_hostname PASSED           [ 58%]
tests/unit/test_arctic.py::test_arctic_connect_with_environment_name PASSED [ 58%]
tests/unit/test_arctic.py::test_database_library_specifier[library-library-arctic] PASSED [ 58%]
tests/unit/test_arctic.py::test_database_library_specifier[user.library-library-arctic_user] PASSED [ 58%]
tests/unit/test_arctic.py::test_arctic_repr PASSED                       [ 59%]
tests/unit/test_arctic.py::test_lib_repr PASSED                          [ 59%]
tests/unit/test_arctic.py::test_register_library_type PASSED             [ 59%]
tests/unit/test_arctic.py::test_set_quota PASSED                         [ 59%]
tests/unit/test_arctic.py::test_get_quota PASSED                         [ 59%]
tests/unit/test_arctic.py::test_check_quota_Zero PASSED                  [ 59%]
tests/unit/test_arctic.py::test_check_quota_None PASSED                  [ 59%]
tests/unit/test_arctic.py::test_check_quota_Zero2 PASSED                 [ 59%]
tests/unit/test_arctic.py::test_check_quota_countdown PASSED             [ 59%]
tests/unit/test_arctic.py::test_check_quota PASSED                       [ 59%]
tests/unit/test_arctic.py::test_check_quota_90_percent PASSED            [ 59%]
tests/unit/test_arctic.py::test_check_quota_info PASSED                  [ 59%]
tests/unit/test_arctic.py::test_check_quota_exceeded PASSED              [ 59%]
tests/unit/test_arctic.py::test_initialize_library PASSED                [ 60%]
tests/unit/test_arctic.py::test_initialize_library_too_many_ns PASSED    [ 60%]
tests/unit/test_arctic.py::test_initialize_library_with_list_coll_names PASSED [ 60%]
tests/unit/test_arctic.py::test_library_exists PASSED                    [ 60%]
tests/unit/test_arctic.py::test_library_doesnt_exist PASSED              [ 60%]
tests/unit/test_arctic.py::test_get_library PASSED                       [ 60%]
tests/unit/test_arctic.py::test_get_library_not_initialized PASSED       [ 60%]
tests/unit/test_arctic.py::test_get_library_auth_issue PASSED            [ 60%]
tests/unit/test_arctic.py::test_get_library_not_registered PASSED        [ 60%]
tests/unit/test_arctic.py::test_mongo_host_get_set PASSED                [ 60%]
tests/unit/test_arctic.py::test_arctic_set_get_state PASSED              [ 60%]
tests/unit/test_arctic.py::test__conn_auth_issue PASSED                  [ 60%]
tests/unit/test_arctic.py::test_reset PASSED                             [ 60%]
tests/unit/test_arctic.py::test_ArcticLibraryBinding_db PASSED           [ 61%]
tests/unit/test_auth.py::test_authenticate PASSED                        [ 61%]
tests/unit/test_auth.py::test_authenticate_fails PASSED                  [ 61%]
tests/unit/test_auth.py::test_authenticate_fails_exception PASSED        [ 61%]
tests/unit/test_compress.py::test_roundtrip[arctic] PASSED               [ 61%]
tests/unit/test_compress.py::test_roundtrip[arcticHC] PASSED             [ 61%]
tests/unit/test_compress.py::test_roundtrip_multi[1] PASSED              [ 61%]
tests/unit/test_compress.py::test_roundtrip_multi[100.0] PASSED          [ 61%]
tests/unit/test_compress.py::test_roundtrip_multi[1000.0] PASSED         [ 61%]
tests/unit/test_compress.py::test_roundtrip_multi[1000000.0] PASSED      [ 61%]
tests/unit/test_compress.py::test_roundtrip_arr[1-10] PASSED             [ 61%]
tests/unit/test_compress.py::test_roundtrip_arr[100-10] PASSED           [ 61%]
tests/unit/test_compress.py::test_roundtrip_arr[1000-10] PASSED          [ 61%]
tests/unit/test_compress.py::test_roundtrip_arrHC[1-10] PASSED           [ 61%]
tests/unit/test_compress.py::test_roundtrip_arrHC[100-10] PASSED         [ 62%]
tests/unit/test_compress.py::test_roundtrip_arrHC[1000-10] PASSED        [ 62%]
tests/unit/test_compress.py::test_arr_zero PASSED                        [ 62%]
tests/unit/test_compression.py::test_compress PASSED                     [ 62%]
tests/unit/test_compression.py::test_compress_LZ4 PASSED                 [ 62%]
tests/unit/test_compression.py::test_compress_array PASSED               [ 62%]
tests/unit/test_compression.py::test_compress_array_usesLZ4 PASSED       [ 62%]
tests/unit/test_compression.py::test_compress_array_LZ4_sequential PASSED [ 62%]
tests/unit/test_compression.py::test_decompress PASSED                   [ 62%]
tests/unit/test_compression.py::test_decompress_array PASSED             [ 62%]
tests/unit/test_compression.py::test_compression_equal_regardless_parallel_mode PASSED [ 62%]
tests/unit/test_compression.py::test_enable_parallel_lz4 PASSED          [ 62%]
tests/unit/test_compression.py::test_compress_empty_string PASSED        [ 62%]
tests/unit/test_decorators_unit.py::test_mongo_retry PASSED              [ 63%]
tests/unit/test_decorators_unit.py::test_mongo_retry_hook_changes PASSED [ 63%]
tests/unit/test_decorators_unit.py::test_mongo_retry_fails PASSED        [ 63%]
tests/unit/test_decorators_unit.py::test_retry_nested PASSED             [ 63%]
tests/unit/test_decorators_unit.py::test_all_other_exceptions_logged PASSED [ 63%]
tests/unit/test_decorators_unit.py::test_other_exceptions_not_logged_outside_of_arctic PASSED [ 63%]
tests/unit/test_decorators_unit.py::test_auth_failure_no_retry XFAIL     [ 63%]
tests/unit/test_decorators_unit.py::test_duplicate_key_failure_no_retry PASSED [ 63%]
tests/unit/test_decorators_unit.py::test_ServerSelectionTimeoutError_no_retry PASSED [ 63%]
tests/unit/test_decorators_unit.py::test_get_host PASSED                 [ 63%]
tests/unit/test_decorators_unit.py::test_get_host_list PASSED            [ 63%]
tests/unit/test_decorators_unit.py::test_get_host_not_a_vs PASSED        [ 63%]
tests/unit/test_fixtures.py::test_overlay_library_name PASSED            [ 63%]
tests/unit/test_fixtures.py::test_overlay_library PASSED                 [ 64%]
tests/unit/test_fixtures.py::test_tickstore_lib PASSED                   [ 64%]
tests/unit/test_hooks.py::test_log_exception_hook PASSED                 [ 64%]
tests/unit/test_hooks.py::test_get_mongodb_uri_hook PASSED               [ 64%]
tests/unit/test_hooks.py::test_get_auth_hook PASSED                      [ 64%]
tests/unit/test_hosts.py::test_get_arctic_lib_with_known_host PASSED     [ 64%]
tests/unit/test_hosts.py::test_get_arctic_lib_with_unknown_host PASSED   [ 64%]
tests/unit/test_hosts.py::test_get_arctic_connection_strings PASSED      [ 64%]
tests/unit/test_hosts.py::test_get_arctic_malformed_connection_strings[donkey] PASSED [ 64%]
tests/unit/test_hosts.py::test_get_arctic_malformed_connection_strings[donkey:ride@blackpool] PASSED [ 64%]
tests/unit/test_hosts.py::test_get_arctic_malformed_connection_strings[donkey:ride] PASSED [ 64%]
tests/unit/test_multi_index.py::test__can_create_df_with_multiple_index PASSED [ 64%]
tests/unit/test_multi_index.py::test__get_ts__asof_latest PASSED         [ 64%]
tests/unit/test_multi_index.py::test__get_ts__asof_datetime PASSED       [ 64%]
tests/unit/test_multi_index.py::test__get_ts__unsorted_index PASSED      [ 65%]
tests/unit/test_multi_index.py::test_fancy_group_by_multi_index PASSED   [ 65%]
tests/unit/test_multi_index.py::test__minmax_last PASSED                 [ 65%]
tests/unit/test_multi_index.py::test__minmax_first PASSED                [ 65%]
tests/unit/test_multi_index.py::test__within_numeric_first PASSED        [ 65%]
tests/unit/test_multi_index.py::test__within_numeric_last PASSED         [ 65%]
tests/unit/test_multi_index.py::test__first_within_datetime PASSED       [ 65%]
tests/unit/test_multi_index.py::test__last_within_datetime PASSED        [ 65%]
tests/unit/test_multi_index.py::test__can_insert_row PASSED              [ 65%]
tests/unit/test_multi_index.py::test__can_append_row PASSED              [ 65%]
tests/unit/test_multi_index.py::test_fancy_group_by_raises PASSED        [ 65%]
tests/unit/test_util.py::test_are_equals_not_df PASSED                   [ 65%]
tests/unit/test_util.py::test_enable_sharding_hashed PASSED              [ 65%]
tests/unit/chunkstore/test_date_chunker.py::test_date_filter PASSED      [ 66%]
tests/unit/chunkstore/test_date_chunker.py::test_date_filter_no_index PASSED [ 66%]
tests/unit/chunkstore/test_date_chunker.py::test_date_filter_with_pd_date_range PASSED [ 66%]
tests/unit/chunkstore/test_date_chunker.py::test_to_chunks_exceptions PASSED [ 66%]
tests/unit/chunkstore/test_date_chunker.py::test_exclude PASSED          [ 66%]
tests/unit/chunkstore/test_date_chunker.py::test_exclude_no_index PASSED [ 66%]
tests/unit/chunkstore/test_date_chunker.py::test_with_tuples PASSED      [ 66%]
tests/unit/chunkstore/test_passthrough_chunker.py::test_pass_thru PASSED [ 66%]
tests/unit/date/test_daterange.py::test_daterange_bounding[unbounded] PASSED [ 66%]
tests/unit/date/test_daterange.py::test_daterange_bounding[unbounded_left] PASSED [ 66%]
tests/unit/date/test_daterange.py::test_daterange_bounding[unbounded_right] PASSED [ 66%]
tests/unit/date/test_daterange.py::test_daterange_bounding[open_open] PASSED [ 66%]
tests/unit/date/test_daterange.py::test_daterange_bounding[open_closed] PASSED [ 66%]
tests/unit/date/test_daterange.py::test_daterange_bounding[closed_open] PASSED [ 66%]
tests/unit/date/test_daterange.py::test_daterange_bounding[closed_explicitly] PASSED [ 67%]
tests/unit/date/test_daterange.py::test_daterange_bounding[closed_by_default] PASSED [ 67%]
tests/unit/date/test_daterange.py::test_daterange_arg_parsing[date_range0] PASSED [ 67%]
tests/unit/date/test_daterange.py::test_daterange_arg_parsing[date_range1] PASSED [ 67%]
tests/unit/date/test_daterange.py::test_daterange_arg_parsing[date_range2] PASSED [ 67%]
tests/unit/date/test_daterange.py::test_daterange_arg_parsing[date_range3] PASSED [ 67%]
tests/unit/date/test_daterange.py::test_daterange_eq PASSED              [ 67%]
tests/unit/date/test_daterange.py::test_daterange_hash PASSED            [ 67%]
tests/unit/date/test_daterange.py::test_daterange_invalid_start PASSED   [ 67%]
tests/unit/date/test_daterange.py::test_daterange_invalid_end PASSED     [ 67%]
tests/unit/date/test_daterange.py::test_daterange_index PASSED           [ 67%]
tests/unit/date/test_daterange.py::test_daterange_index_error PASSED     [ 67%]
tests/unit/date/test_daterange.py::test_as_dates PASSED                  [ 67%]
tests/unit/date/test_daterange.py::test_string_to_daterange[20110101-expected_ts0-expected_dt0] PASSED [ 68%]
tests/unit/date/test_daterange.py::test_string_to_daterange[20110101-20110102-expected_ts1-expected_dt1] PASSED [ 68%]
tests/unit/date/test_daterange.py::test_string_to_daterange[201101011030-expected_ts2-expected_dt2] PASSED [ 68%]
tests/unit/date/test_daterange.py::test_string_to_daterange[-201101011030-expected_ts3-expected_dt3] PASSED [ 68%]
tests/unit/date/test_daterange.py::test_string_to_daterange[201101011030--expected_ts4-expected_dt4] PASSED [ 68%]
tests/unit/date/test_daterange.py::test_string_to_daterange[(20110101-20110102)-expected_ts5-expected_dt5] PASSED [ 68%]
tests/unit/date/test_daterange.py::test_string_to_daterange[(20110101-20110102]-expected_ts6-expected_dt6] PASSED [ 68%]
tests/unit/date/test_daterange.py::test_string_to_daterange[[20110101-20110102)-expected_ts7-expected_dt7] PASSED [ 68%]
tests/unit/date/test_daterange.py::test_string_to_daterange[[20110101-20110102]-expected_ts8-expected_dt8] PASSED [ 68%]
tests/unit/date/test_daterange.py::test_string_to_daterange_raises PASSED [ 68%]
tests/unit/date/test_daterange.py::test_mongo_query[date_range0-expected0] PASSED [ 68%]
tests/unit/date/test_daterange.py::test_mongo_query[date_range1-expected1] PASSED [ 68%]
tests/unit/date/test_daterange.py::test_mongo_query[date_range2-expected2] PASSED [ 68%]
tests/unit/date/test_daterange.py::test_mongo_query[date_range3-expected3] PASSED [ 69%]
tests/unit/date/test_daterange.py::test_mongo_query[date_range4-expected4] PASSED [ 69%]
tests/unit/date/test_daterange.py::test_mongo_query[date_range5-expected5] PASSED [ 69%]
tests/unit/date/test_daterange.py::test_mongo_query[date_range6-expected6] PASSED [ 69%]
tests/unit/date/test_daterange.py::test_mongo_query[date_range7-expected7] PASSED [ 69%]
tests/unit/date/test_daterange.py::test_get_date_bounds[date_range0-expected0] PASSED [ 69%]
tests/unit/date/test_daterange.py::test_get_date_bounds[date_range1-expected1] PASSED [ 69%]
tests/unit/date/test_daterange.py::test_get_date_bounds[date_range2-expected2] PASSED [ 69%]
tests/unit/date/test_daterange.py::test_get_date_bounds[date_range3-expected3] PASSED [ 69%]
tests/unit/date/test_daterange.py::test_get_date_bounds[date_range4-expected4] PASSED [ 69%]
tests/unit/date/test_daterange.py::test_get_date_bounds[date_range5-expected5] PASSED [ 69%]
tests/unit/date/test_daterange.py::test_get_date_bounds[date_range6-expected6] PASSED [ 69%]
tests/unit/date/test_daterange.py::test_get_date_bounds[date_range7-expected7] PASSED [ 69%]
tests/unit/date/test_daterange.py::test_intersection_with_self[dr0] PASSED [ 69%]
tests/unit/date/test_daterange.py::test_intersection_with_self[dr1] PASSED [ 70%]
tests/unit/date/test_daterange.py::test_intersection_with_self[dr2] PASSED [ 70%]
tests/unit/date/test_daterange.py::test_intersection_with_self[dr3] PASSED [ 70%]
tests/unit/date/test_daterange.py::test_intersection_with_self[dr4] PASSED [ 70%]
tests/unit/date/test_daterange.py::test_intersection_with_self[dr5] PASSED [ 70%]
tests/unit/date/test_daterange.py::test_intersection_with_self[dr6] PASSED [ 70%]
tests/unit/date/test_daterange.py::test_intersection_returns_inner_boundaries PASSED [ 70%]
tests/unit/date/test_daterange.py::test_intersection_preserves_boundaries PASSED [ 70%]
tests/unit/date/test_daterange.py::test_intersection_contains PASSED     [ 70%]
tests/unit/date/test_datetime_to_ms_roundtrip.py::test_UTC_roundtrip PASSED [ 70%]
tests/unit/date/test_datetime_to_ms_roundtrip.py::test_weird_get_tz_local PASSED [ 70%]
tests/unit/date/test_datetime_to_ms_roundtrip.py::test_pytz_London XFAIL [ 70%]
tests/unit/date/test_datetime_to_ms_roundtrip.py::test_mktz_London PASSED [ 70%]
tests/unit/date/test_datetime_to_ms_roundtrip.py::test_datetime_roundtrip_local_no_tz PASSED [ 71%]
tests/unit/date/test_datetime_to_ms_roundtrip.py::test_datetime_roundtrip_local_tz PASSED [ 71%]
tests/unit/date/test_datetime_to_ms_roundtrip.py::test_datetime_roundtrip_est_tz PASSED [ 71%]
tests/unit/date/test_datetime_to_ms_roundtrip.py::test_millisecond_conversion[807000-1074069004807] PASSED [ 71%]
tests/unit/date/test_datetime_to_ms_roundtrip.py::test_millisecond_conversion[807243-1074069004807] PASSED [ 71%]
tests/unit/date/test_datetime_to_ms_roundtrip.py::test_millisecond_conversion[807675-1074069004807] PASSED [ 71%]
tests/unit/date/test_mktz.py::test_mktz PASSED                           [ 71%]
tests/unit/date/test_mktz.py::test_mktz_noarg PASSED                     [ 71%]
tests/unit/date/test_mktz.py::test_mktz_zone PASSED                      [ 71%]
tests/unit/date/test_mktz.py::test_mktz_fails_if_invalid_timezone PASSED [ 71%]
tests/unit/date/test_util.py::test_datetime_to_ms_and_back[local_tz0-pdt0] PASSED [ 71%]
tests/unit/date/test_util.py::test_datetime_to_ms_and_back[local_tz0-pdt1] PASSED [ 71%]
tests/unit/date/test_util.py::test_datetime_to_ms_and_back[local_tz0-pdt2] PASSED [ 71%]
tests/unit/date/test_util.py::test_datetime_to_ms_and_back[local_tz0-pdt3] PASSED [ 71%]
tests/unit/date/test_util.py::test_datetime_to_ms_and_back[local_tz0-pdt4] PASSED [ 72%]
tests/unit/date/test_util.py::test_datetime_to_ms_and_back[local_tz0-pdt5] PASSED [ 72%]
tests/unit/date/test_util.py::test_datetime_to_ms_and_back[local_tz1-pdt0] PASSED [ 72%]
tests/unit/date/test_util.py::test_datetime_to_ms_and_back[local_tz1-pdt1] PASSED [ 72%]
tests/unit/date/test_util.py::test_datetime_to_ms_and_back[local_tz1-pdt2] PASSED [ 72%]
tests/unit/date/test_util.py::test_datetime_to_ms_and_back[local_tz1-pdt3] PASSED [ 72%]
tests/unit/date/test_util.py::test_datetime_to_ms_and_back[local_tz1-pdt4] PASSED [ 72%]
tests/unit/date/test_util.py::test_datetime_to_ms_and_back[local_tz1-pdt5] PASSED [ 72%]
tests/unit/date/test_util.py::test_datetime_to_ms_and_back[local_tz2-pdt0] PASSED [ 72%]
tests/unit/date/test_util.py::test_datetime_to_ms_and_back[local_tz2-pdt1] PASSED [ 72%]
tests/unit/date/test_util.py::test_datetime_to_ms_and_back[local_tz2-pdt2] PASSED [ 72%]
tests/unit/date/test_util.py::test_datetime_to_ms_and_back[local_tz2-pdt3] PASSED [ 72%]
tests/unit/date/test_util.py::test_datetime_to_ms_and_back[local_tz2-pdt4] PASSED [ 72%]
tests/unit/date/test_util.py::test_datetime_to_ms_and_back[local_tz2-pdt5] PASSED [ 73%]
tests/unit/date/test_util.py::test_datetime_to_ms_and_back[local_tz3-pdt0] PASSED [ 73%]
tests/unit/date/test_util.py::test_datetime_to_ms_and_back[local_tz3-pdt1] PASSED [ 73%]
tests/unit/date/test_util.py::test_datetime_to_ms_and_back[local_tz3-pdt2] PASSED [ 73%]
tests/unit/date/test_util.py::test_datetime_to_ms_and_back[local_tz3-pdt3] PASSED [ 73%]
tests/unit/date/test_util.py::test_datetime_to_ms_and_back[local_tz3-pdt4] PASSED [ 73%]
tests/unit/date/test_util.py::test_datetime_to_ms_and_back[local_tz3-pdt5] PASSED [ 73%]
tests/unit/date/test_util.py::test_datetime_to_ms_and_back[local_tz4-pdt0] PASSED [ 73%]
tests/unit/date/test_util.py::test_datetime_to_ms_and_back[local_tz4-pdt1] PASSED [ 73%]
tests/unit/date/test_util.py::test_datetime_to_ms_and_back[local_tz4-pdt2] PASSED [ 73%]
tests/unit/date/test_util.py::test_datetime_to_ms_and_back[local_tz4-pdt3] PASSED [ 73%]
tests/unit/date/test_util.py::test_datetime_to_ms_and_back[local_tz4-pdt4] PASSED [ 73%]
tests/unit/date/test_util.py::test_datetime_to_ms_and_back[local_tz4-pdt5] PASSED [ 73%]
tests/unit/date/test_util.py::test_datetime_to_ms_and_back[local_tz5-pdt0] PASSED [ 74%]
tests/unit/date/test_util.py::test_datetime_to_ms_and_back[local_tz5-pdt1] PASSED [ 74%]
tests/unit/date/test_util.py::test_datetime_to_ms_and_back[local_tz5-pdt2] PASSED [ 74%]
tests/unit/date/test_util.py::test_datetime_to_ms_and_back[local_tz5-pdt3] PASSED [ 74%]
tests/unit/date/test_util.py::test_datetime_to_ms_and_back[local_tz5-pdt4] PASSED [ 74%]
tests/unit/date/test_util.py::test_datetime_to_ms_and_back[local_tz5-pdt5] PASSED [ 74%]
tests/unit/date/test_util.py::test_datetime_to_ms_and_back[local_tz6-pdt0] PASSED [ 74%]
tests/unit/date/test_util.py::test_datetime_to_ms_and_back[local_tz6-pdt1] PASSED [ 74%]
tests/unit/date/test_util.py::test_datetime_to_ms_and_back[local_tz6-pdt2] PASSED [ 74%]
tests/unit/date/test_util.py::test_datetime_to_ms_and_back[local_tz6-pdt3] PASSED [ 74%]
tests/unit/date/test_util.py::test_datetime_to_ms_and_back[local_tz6-pdt4] PASSED [ 74%]
tests/unit/date/test_util.py::test_datetime_to_ms_and_back[local_tz6-pdt5] PASSED [ 74%]
tests/unit/date/test_util.py::test_datetime_to_ms_and_back_microseconds PASSED [ 74%]
tests/unit/date/test_util.py::test_daterange_closedclosed_None PASSED    [ 74%]
tests/unit/date/test_util.py::test_daterange_closedclosed PASSED         [ 75%]
tests/unit/date/test_util.py::test_daterange_closedclosed_no_tz PASSED   [ 75%]
tests/unit/date/test_util.py::test_to_dt_0 PASSED                        [ 75%]
tests/unit/date/test_util.py::test_to_dt_0_default PASSED                [ 75%]
tests/unit/date/test_util.py::test_to_dt_dt_no_tz PASSED                 [ 75%]
tests/unit/date/test_util.py::test_to_dt_dt_no_tz_default PASSED         [ 75%]
tests/unit/date/test_util.py::test_to_dt_dt_tz PASSED                    [ 75%]
tests/unit/date/test_util.py::test_to_dt_dt_tz_default PASSED            [ 75%]
tests/unit/date/test_util.py::test_daterange_raises PASSED               [ 75%]
tests/unit/date/test_util.py::test_daterange_eq PASSED                   [ 75%]
tests/unit/date/test_util.py::test_daterange_lt PASSED                   [ 75%]
tests/unit/date/test_util.py::test_utc_dt_to_local_dt PASSED             [ 75%]
tests/unit/scripts/test_arctic_create_user.py::test_main_minimal PASSED  [ 75%]
tests/unit/scripts/test_arctic_create_user.py::test_main_with_db PASSED  [ 76%]
tests/unit/scripts/test_arctic_create_user.py::test_main_with_db_write PASSED [ 76%]
tests/unit/scripts/test_arctic_create_user.py::test_no_auth PASSED       [ 76%]
tests/unit/scripts/test_arctic_fsck.py::test_main PASSED                 [ 76%]
tests/unit/scripts/test_arctic_fsck.py::test_main_dry_run PASSED         [ 76%]
tests/unit/scripts/test_initialize_library.py::test_init_library PASSED  [ 76%]
tests/unit/scripts/test_initialize_library.py::test_init_library_no_admin PASSED [ 76%]
tests/unit/scripts/test_initialize_library.py::test_init_library_hashed PASSED [ 76%]
tests/unit/scripts/test_initialize_library.py::test_init_library_no_admin_no_user_creds PASSED [ 76%]
tests/unit/scripts/test_initialize_library.py::test_bad_library_name PASSED [ 76%]
tests/unit/scripts/test_utils.py::test_do_db_auth PASSED                 [ 76%]
tests/unit/scripts/test_utils.py::test_do_db_auth_no_admin PASSED        [ 76%]
tests/unit/scripts/test_utils.py::test_do_db_auth_no_user_creds PASSED   [ 76%]
tests/unit/scripts/test_utils.py::test_do_db_auth_no_admin_user_creds_fails PASSED [ 76%]
tests/unit/scripts/test_utils.py::test_do_db_auth_admin_user_creds_fails PASSED [ 77%]
tests/unit/scripts/test_utils.py::test_do_db_auth_role PASSED            [ 77%]
tests/unit/serialization/test_incremental.py::test_incremental_bad_init PASSED [ 77%]
tests/unit/serialization/test_incremental.py::test_none_df PASSED        [ 77%]
tests/unit/serialization/test_incremental.py::test_serialize_pandas_to_recarray[multi_column_no_multiindex] PASSED [ 77%]
tests/unit/serialization/test_incremental.py::test_serialize_pandas_to_recarray[multiindex] PASSED [ 77%]
tests/unit/serialization/test_incremental.py::test_serialize_pandas_to_recarray[empty_multicolumn] PASSED [ 77%]
tests/unit/serialization/test_incremental.py::test_serialize_pandas_to_recarray[multiindex_with_object] PASSED [ 77%]
tests/unit/serialization/test_incremental.py::test_serialize_pandas_to_recarray[with_some_none] PASSED [ 77%]
tests/unit/serialization/test_incremental.py::test_serialize_pandas_to_recarray[with_string] PASSED [ 77%]
tests/unit/serialization/test_incremental.py::test_serialize_pandas_to_recarray[multi_column_with_some_objects] PASSED [ 77%]
tests/unit/serialization/test_incremental.py::test_serialize_pandas_to_recarray[large_with_some_objects] PASSED [ 77%]
tests/unit/serialization/test_incremental.py::test_serialize_pandas_to_recarray[large_multi_index] PASSED [ 77%]
tests/unit/serialization/test_incremental.py::test_serialize_pandas_to_recarray[empty_multiindex] PASSED [ 78%]
tests/unit/serialization/test_incremental.py::test_serialize_pandas_to_recarray[empty] PASSED [ 78%]
tests/unit/serialization/test_incremental.py::test_serialize_pandas_to_recarray[medium] PASSED [ 78%]
tests/unit/serialization/test_incremental.py::test_serialize_pandas_to_recarray[index_tz_aware] PASSED [ 78%]
tests/unit/serialization/test_incremental.py::test_serialize_pandas_to_recarray[n_dimensional_df] PASSED [ 78%]
tests/unit/serialization/test_incremental.py::test_serialize_pandas_to_recarray[multi_column_int_levels] PASSED [ 78%]
tests/unit/serialization/test_incremental.py::test_serialize_pandas_to_recarray[multi_column_and_multi_index] PASSED [ 78%]
tests/unit/serialization/test_incremental.py::test_serialize_pandas_to_recarray[empty_index] PASSED [ 78%]
tests/unit/serialization/test_incremental.py::test_serialize_pandas_to_recarray[large_multi_column] PASSED [ 78%]
tests/unit/serialization/test_incremental.py::test_serialize_pandas_to_recarray[large] PASSED [ 78%]
tests/unit/serialization/test_incremental.py::test_serialize_pandas_to_recarray[with_some_objects] PASSED [ 78%]
tests/unit/serialization/test_incremental.py::test_serialize_pandas_to_recarray[onerow] PASSED [ 78%]
tests/unit/serialization/test_incremental.py::test_serialize_pandas_to_recarray[small] PASSED [ 78%]
tests/unit/serialization/test_incremental.py::test_serialize_pandas_to_recarray[with_unicode] PASSED [ 79%]
tests/unit/serialization/test_incremental.py::test_serialize_pandas_to_recarray[mixed_dtypes_df] PASSED [ 79%]
tests/unit/serialization/test_incremental.py::test_serialize_incremental_pandas_to_recarray[multi_column_no_multiindex] PASSED [ 79%]
tests/unit/serialization/test_incremental.py::test_serialize_incremental_pandas_to_recarray[multiindex] PASSED [ 79%]
tests/unit/serialization/test_incremental.py::test_serialize_incremental_pandas_to_recarray[empty_multicolumn] PASSED [ 79%]
tests/unit/serialization/test_incremental.py::test_serialize_incremental_pandas_to_recarray[multiindex_with_object] PASSED [ 79%]
tests/unit/serialization/test_incremental.py::test_serialize_incremental_pandas_to_recarray[with_some_none] PASSED [ 79%]
tests/unit/serialization/test_incremental.py::test_serialize_incremental_pandas_to_recarray[with_string] PASSED [ 79%]
tests/unit/serialization/test_incremental.py::test_serialize_incremental_pandas_to_recarray[multi_column_with_some_objects] PASSED [ 79%]
tests/unit/serialization/test_incremental.py::test_serialize_incremental_pandas_to_recarray[large_with_some_objects] PASSED [ 79%]
tests/unit/serialization/test_incremental.py::test_serialize_incremental_pandas_to_recarray[large_multi_index] PASSED [ 79%]
tests/unit/serialization/test_incremental.py::test_serialize_incremental_pandas_to_recarray[empty_multiindex] PASSED [ 79%]
tests/unit/serialization/test_incremental.py::test_serialize_incremental_pandas_to_recarray[empty] PASSED [ 79%]
tests/unit/serialization/test_incremental.py::test_serialize_incremental_pandas_to_recarray[medium] PASSED [ 79%]
tests/unit/serialization/test_incremental.py::test_serialize_incremental_pandas_to_recarray[index_tz_aware] PASSED [ 80%]
tests/unit/serialization/test_incremental.py::test_serialize_incremental_pandas_to_recarray[n_dimensional_df] PASSED [ 80%]
tests/unit/serialization/test_incremental.py::test_serialize_incremental_pandas_to_recarray[multi_column_int_levels] PASSED [ 80%]
tests/unit/serialization/test_incremental.py::test_serialize_incremental_pandas_to_recarray[multi_column_and_multi_index] PASSED [ 80%]
tests/unit/serialization/test_incremental.py::test_serialize_incremental_pandas_to_recarray[empty_index] PASSED [ 80%]
tests/unit/serialization/test_incremental.py::test_serialize_incremental_pandas_to_recarray[large_multi_column] PASSED [ 80%]
tests/unit/serialization/test_incremental.py::test_serialize_incremental_pandas_to_recarray[large] PASSED [ 80%]
tests/unit/serialization/test_incremental.py::test_serialize_incremental_pandas_to_recarray[with_some_objects] PASSED [ 80%]
tests/unit/serialization/test_incremental.py::test_serialize_incremental_pandas_to_recarray[onerow] PASSED [ 80%]
tests/unit/serialization/test_incremental.py::test_serialize_incremental_pandas_to_recarray[small] PASSED [ 80%]
tests/unit/serialization/test_incremental.py::test_serialize_incremental_pandas_to_recarray[with_unicode] PASSED [ 80%]
tests/unit/serialization/test_incremental.py::test_serialize_incremental_pandas_to_recarray[mixed_dtypes_df] PASSED [ 80%]
tests/unit/serialization/test_incremental.py::test_serialize_incremental_chunk_size_pandas_to_recarray[multi_column_no_multiindex] PASSED [ 80%]
tests/unit/serialization/test_incremental.py::test_serialize_incremental_chunk_size_pandas_to_recarray[multiindex] PASSED [ 81%]
tests/unit/serialization/test_incremental.py::test_serialize_incremental_chunk_size_pandas_to_recarray[empty_multicolumn] PASSED [ 81%]
tests/unit/serialization/test_incremental.py::test_serialize_incremental_chunk_size_pandas_to_recarray[multiindex_with_object] PASSED [ 81%]
tests/unit/serialization/test_incremental.py::test_serialize_incremental_chunk_size_pandas_to_recarray[with_some_none] PASSED [ 81%]
tests/unit/serialization/test_incremental.py::test_serialize_incremental_chunk_size_pandas_to_recarray[with_string] PASSED [ 81%]
tests/unit/serialization/test_incremental.py::test_serialize_incremental_chunk_size_pandas_to_recarray[multi_column_with_some_objects] PASSED [ 81%]
tests/unit/serialization/test_incremental.py::test_serialize_incremental_chunk_size_pandas_to_recarray[large_with_some_objects] PASSED [ 81%]
tests/unit/serialization/test_incremental.py::test_serialize_incremental_chunk_size_pandas_to_recarray[large_multi_index] PASSED [ 81%]
tests/unit/serialization/test_incremental.py::test_serialize_incremental_chunk_size_pandas_to_recarray[empty_multiindex] PASSED [ 81%]
tests/unit/serialization/test_incremental.py::test_serialize_incremental_chunk_size_pandas_to_recarray[empty] PASSED [ 81%]
tests/unit/serialization/test_incremental.py::test_serialize_incremental_chunk_size_pandas_to_recarray[medium] PASSED [ 81%]
tests/unit/serialization/test_incremental.py::test_serialize_incremental_chunk_size_pandas_to_recarray[index_tz_aware] PASSED [ 81%]
tests/unit/serialization/test_incremental.py::test_serialize_incremental_chunk_size_pandas_to_recarray[n_dimensional_df] PASSED [ 81%]
tests/unit/serialization/test_incremental.py::test_serialize_incremental_chunk_size_pandas_to_recarray[multi_column_int_levels] PASSED [ 82%]
tests/unit/serialization/test_incremental.py::test_serialize_incremental_chunk_size_pandas_to_recarray[multi_column_and_multi_index] PASSED [ 82%]
tests/unit/serialization/test_incremental.py::test_serialize_incremental_chunk_size_pandas_to_recarray[empty_index] PASSED [ 82%]
tests/unit/serialization/test_incremental.py::test_serialize_incremental_chunk_size_pandas_to_recarray[large_multi_column] PASSED [ 82%]
tests/unit/serialization/test_incremental.py::test_serialize_incremental_chunk_size_pandas_to_recarray[large] PASSED [ 82%]
tests/unit/serialization/test_incremental.py::test_serialize_incremental_chunk_size_pandas_to_recarray[with_some_objects] PASSED [ 82%]
tests/unit/serialization/test_incremental.py::test_serialize_incremental_chunk_size_pandas_to_recarray[onerow] PASSED [ 82%]
tests/unit/serialization/test_incremental.py::test_serialize_incremental_chunk_size_pandas_to_recarray[small] PASSED [ 82%]
tests/unit/serialization/test_incremental.py::test_serialize_incremental_chunk_size_pandas_to_recarray[with_unicode] PASSED [ 82%]
tests/unit/serialization/test_incremental.py::test_serialize_incremental_chunk_size_pandas_to_recarray[mixed_dtypes_df] PASSED [ 82%]
tests/unit/serialization/test_incremental.py::test_shape[multi_column_no_multiindex] PASSED [ 82%]
tests/unit/serialization/test_incremental.py::test_shape[multiindex] PASSED [ 82%]
tests/unit/serialization/test_incremental.py::test_shape[empty_multicolumn] PASSED [ 82%]
tests/unit/serialization/test_incremental.py::test_shape[multiindex_with_object] PASSED [ 82%]
tests/unit/serialization/test_incremental.py::test_shape[with_some_none] PASSED [ 83%]
tests/unit/serialization/test_incremental.py::test_shape[with_string] PASSED [ 83%]
tests/unit/serialization/test_incremental.py::test_shape[multi_column_with_some_objects] PASSED [ 83%]
tests/unit/serialization/test_incremental.py::test_shape[large_with_some_objects] PASSED [ 83%]
tests/unit/serialization/test_incremental.py::test_shape[large_multi_index] PASSED [ 83%]
tests/unit/serialization/test_incremental.py::test_shape[empty_multiindex] PASSED [ 83%]
tests/unit/serialization/test_incremental.py::test_shape[empty] PASSED   [ 83%]
tests/unit/serialization/test_incremental.py::test_shape[medium] PASSED  [ 83%]
tests/unit/serialization/test_incremental.py::test_shape[index_tz_aware] PASSED [ 83%]
tests/unit/serialization/test_incremental.py::test_shape[n_dimensional_df] PASSED [ 83%]
tests/unit/serialization/test_incremental.py::test_shape[multi_column_int_levels] PASSED [ 83%]
tests/unit/serialization/test_incremental.py::test_shape[multi_column_and_multi_index] PASSED [ 83%]
tests/unit/serialization/test_incremental.py::test_shape[empty_index] PASSED [ 83%]
tests/unit/serialization/test_incremental.py::test_shape[large_multi_column] PASSED [ 84%]
tests/unit/serialization/test_incremental.py::test_shape[large] PASSED   [ 84%]
tests/unit/serialization/test_incremental.py::test_shape[with_some_objects] PASSED [ 84%]
tests/unit/serialization/test_incremental.py::test_shape[onerow] PASSED  [ 84%]
tests/unit/serialization/test_incremental.py::test_shape[small] PASSED   [ 84%]
tests/unit/serialization/test_incremental.py::test_shape[with_unicode] PASSED [ 84%]
tests/unit/serialization/test_incremental.py::test_shape[mixed_dtypes_df] PASSED [ 84%]
tests/unit/serialization/test_incremental.py::test_generator_bytes_range[-10--10] PASSED [ 84%]
tests/unit/serialization/test_incremental.py::test_generator_bytes_range[-10-490] PASSED [ 84%]
tests/unit/serialization/test_incremental.py::test_generator_bytes_range[-10-990] PASSED [ 84%]
tests/unit/serialization/test_incremental.py::test_generator_bytes_range[-10-1490] PASSED [ 84%]
tests/unit/serialization/test_incremental.py::test_generator_bytes_range[490-490] PASSED [ 84%]
tests/unit/serialization/test_incremental.py::test_generator_bytes_range[490-990] PASSED [ 84%]
tests/unit/serialization/test_incremental.py::test_generator_bytes_range[490-1490] PASSED [ 84%]
tests/unit/serialization/test_incremental.py::test_generator_bytes_range[990-990] PASSED [ 85%]
tests/unit/serialization/test_incremental.py::test_generator_bytes_range[990-1490] PASSED [ 85%]
tests/unit/serialization/test_incremental.py::test_generator_bytes_range[1490-1490] PASSED [ 85%]
tests/unit/serialization/test_numpy_arrays.py::test_frame_converter PASSED [ 85%]
tests/unit/serialization/test_numpy_arrays.py::test_with_strings PASSED  [ 85%]
tests/unit/serialization/test_numpy_arrays.py::test_with_objects_raises PASSED [ 85%]
tests/unit/serialization/test_numpy_arrays.py::test_without_index PASSED [ 85%]
tests/unit/serialization/test_numpy_arrays.py::test_with_index PASSED    [ 85%]
tests/unit/serialization/test_numpy_arrays.py::test_with_nans PASSED     [ 85%]
tests/unit/serialization/test_numpy_arrays.py::test_empty_dataframe PASSED [ 85%]
tests/unit/serialization/test_numpy_arrays.py::test_empty_columns PASSED [ 85%]
tests/unit/serialization/test_numpy_arrays.py::test_string_cols_with_nans PASSED [ 85%]
tests/unit/serialization/test_numpy_arrays.py::test_objify_with_missing_columns PASSED [ 85%]
tests/unit/serialization/test_numpy_arrays.py::test_multi_column_fail PASSED [ 86%]
tests/unit/serialization/test_numpy_arrays.py::test_dataframe_writable_after_objify PASSED [ 86%]
tests/unit/serialization/test_numpy_records.py::test_to_primitive_timestamps PASSED [ 86%]
tests/unit/serialization/test_numpy_records.py::test_to_primitive_fixed_length_strings PASSED [ 86%]
tests/unit/serialization/test_numpy_records.py::test_can_convert_to_records_without_objects_returns_false_on_exception_in_to_records[True] PASSED [ 86%]
tests/unit/serialization/test_numpy_records.py::test_can_convert_to_records_without_objects_returns_false_on_exception_in_to_records[False] PASSED [ 86%]
tests/unit/serialization/test_numpy_records.py::test_can_convert_to_records_without_objects_returns_false_when_records_have_object_dtype[True] PASSED [ 86%]
tests/unit/serialization/test_numpy_records.py::test_can_convert_to_records_without_objects_returns_false_when_records_have_object_dtype[False] PASSED [ 86%]
tests/unit/serialization/test_numpy_records.py::test_can_convert_to_records_without_objects_returns_false_when_records_have_arrays_in_them[True] PASSED [ 86%]
tests/unit/serialization/test_numpy_records.py::test_can_convert_to_records_without_objects_returns_false_when_records_have_arrays_in_them[False] PASSED [ 86%]
tests/unit/serialization/test_numpy_records.py::test_can_convert_to_records_without_objects_returns_true_otherwise[True] PASSED [ 86%]
tests/unit/serialization/test_numpy_records.py::test_can_convert_to_records_without_objects_returns_true_otherwise[False] PASSED [ 86%]
tests/unit/serialization/test_numpy_records.py::test_can_convert_to_records_mixed_object_column_string_nan[False] PASSED [ 86%]
tests/unit/serialization/test_numpy_records.py::test_can_convert_to_records_mixed_object_column_string_nan[True] PASSED [ 87%]
tests/unit/serialization/test_pandas_is_serializable.py::test_dataframe_confirm_fast_check_compatibility[multi_column_no_multiindex] PASSED [ 87%]
tests/unit/serialization/test_pandas_is_serializable.py::test_dataframe_confirm_fast_check_compatibility[multiindex] PASSED [ 87%]
tests/unit/serialization/test_pandas_is_serializable.py::test_dataframe_confirm_fast_check_compatibility[empty_multicolumn] PASSED [ 87%]
tests/unit/serialization/test_pandas_is_serializable.py::test_dataframe_confirm_fast_check_compatibility[multiindex_with_object] PASSED [ 87%]
tests/unit/serialization/test_pandas_is_serializable.py::test_dataframe_confirm_fast_check_compatibility[with_some_none] PASSED [ 87%]
tests/unit/serialization/test_pandas_is_serializable.py::test_dataframe_confirm_fast_check_compatibility[with_string] PASSED [ 87%]
tests/unit/serialization/test_pandas_is_serializable.py::test_dataframe_confirm_fast_check_compatibility[multi_column_with_some_objects] PASSED [ 87%]
tests/unit/serialization/test_pandas_is_serializable.py::test_dataframe_confirm_fast_check_compatibility[large_with_some_objects] PASSED [ 87%]
tests/unit/serialization/test_pandas_is_serializable.py::test_dataframe_confirm_fast_check_compatibility[large_multi_index] PASSED [ 87%]
tests/unit/serialization/test_pandas_is_serializable.py::test_dataframe_confirm_fast_check_compatibility[empty_multiindex] PASSED [ 87%]
tests/unit/serialization/test_pandas_is_serializable.py::test_dataframe_confirm_fast_check_compatibility[empty] PASSED [ 87%]
tests/unit/serialization/test_pandas_is_serializable.py::test_dataframe_confirm_fast_check_compatibility[medium] PASSED [ 87%]
tests/unit/serialization/test_pandas_is_serializable.py::test_dataframe_confirm_fast_check_compatibility[index_tz_aware] PASSED [ 87%]
tests/unit/serialization/test_pandas_is_serializable.py::test_dataframe_confirm_fast_check_compatibility[n_dimensional_df] PASSED [ 88%]
tests/unit/serialization/test_pandas_is_serializable.py::test_dataframe_confirm_fast_check_compatibility[multi_column_int_levels] PASSED [ 88%]
tests/unit/serialization/test_pandas_is_serializable.py::test_dataframe_confirm_fast_check_compatibility[multi_column_and_multi_index] PASSED [ 88%]
tests/unit/serialization/test_pandas_is_serializable.py::test_dataframe_confirm_fast_check_compatibility[empty_index] PASSED [ 88%]
tests/unit/serialization/test_pandas_is_serializable.py::test_dataframe_confirm_fast_check_compatibility[large_multi_column] PASSED [ 88%]
tests/unit/serialization/test_pandas_is_serializable.py::test_dataframe_confirm_fast_check_compatibility[large] PASSED [ 88%]
tests/unit/serialization/test_pandas_is_serializable.py::test_dataframe_confirm_fast_check_compatibility[with_some_objects] PASSED [ 88%]
tests/unit/serialization/test_pandas_is_serializable.py::test_dataframe_confirm_fast_check_compatibility[onerow] PASSED [ 88%]
tests/unit/serialization/test_pandas_is_serializable.py::test_dataframe_confirm_fast_check_compatibility[small] PASSED [ 88%]
tests/unit/serialization/test_pandas_is_serializable.py::test_dataframe_confirm_fast_check_compatibility[with_unicode] PASSED [ 88%]
tests/unit/serialization/test_pandas_is_serializable.py::test_dataframe_confirm_fast_check_compatibility[mixed_dtypes_df] PASSED [ 88%]
tests/unit/store/test_bitemporal_store.py::test_add_observe_dt_index PASSED [ 88%]
tests/unit/store/test_bson_store.py::test_enable_sharding PASSED         [ 88%]
tests/unit/store/test_bson_store.py::test_find PASSED                    [ 89%]
tests/unit/store/test_bson_store.py::test_find_one PASSED                [ 89%]
tests/unit/store/test_bson_store.py::test_insert_one PASSED              [ 89%]
tests/unit/store/test_bson_store.py::test_insert_many PASSED             [ 89%]
tests/unit/store/test_bson_store.py::test_replace_one PASSED             [ 89%]
tests/unit/store/test_bson_store.py::test_update_one PASSED              [ 89%]
tests/unit/store/test_bson_store.py::test_update_many PASSED             [ 89%]
tests/unit/store/test_bson_store.py::test_find_one_and_replace PASSED    [ 89%]
tests/unit/store/test_bson_store.py::test_find_one_and_update PASSED     [ 89%]
tests/unit/store/test_bson_store.py::test_find_one_and_delete PASSED     [ 89%]
tests/unit/store/test_bson_store.py::test_bulk_write PASSED              [ 89%]
tests/unit/store/test_bson_store.py::test_delete_one PASSED              [ 89%]
tests/unit/store/test_bson_store.py::test_count PASSED                   [ 89%]
tests/unit/store/test_bson_store.py::test_distinct PASSED                [ 89%]
tests/unit/store/test_bson_store.py::test_delete_many PASSED             [ 90%]
tests/unit/store/test_bson_store.py::test_create_index PASSED            [ 90%]
tests/unit/store/test_bson_store.py::test_drop_index PASSED              [ 90%]
tests/unit/store/test_bson_store.py::test_index_information PASSED       [ 90%]
tests/unit/store/test_metadata_store.py::test_ensure_index PASSED        [ 90%]
tests/unit/store/test_metadata_store.py::test_list_symbols_simple PASSED [ 90%]
tests/unit/store/test_metadata_store.py::test_list_symbols_regex PASSED  [ 90%]
tests/unit/store/test_metadata_store.py::test_list_symbols_as_of PASSED  [ 90%]
tests/unit/store/test_metadata_store.py::test_list_symbols_as_of_regex PASSED [ 90%]
tests/unit/store/test_metadata_store.py::test_list_symbols_metadata_query PASSED [ 90%]
tests/unit/store/test_metadata_store.py::test_list_symbols_all_options PASSED [ 90%]
tests/unit/store/test_ndarray_store.py::test_dtype_parsing PASSED        [ 90%]
tests/unit/store/test_ndarray_store.py::test_promote_dtype_handles_string_increase PASSED [ 90%]
tests/unit/store/test_ndarray_store.py::test_promote_dtype_handles_string_decrease PASSED [ 91%]
tests/unit/store/test_ndarray_store.py::test_promote_dtype_handles_new_column PASSED [ 91%]
tests/unit/store/test_ndarray_store.py::test_promote_dtype_handles_rearrangement_of_columns_favouring_dtype1 PASSED [ 91%]
tests/unit/store/test_ndarray_store.py::test_promote_dtype_throws_if_column_is_removed PASSED [ 91%]
tests/unit/store/test_ndarray_store.py::test_concat_and_rewrite_checks_chunk_count PASSED [ 91%]
tests/unit/store/test_ndarray_store.py::test_concat_and_rewrite_checks_written PASSED [ 91%]
tests/unit/store/test_ndarray_store.py::test_concat_and_rewrite_checks_different_id PASSED [ 91%]
tests/unit/store/test_ndarray_store.py::test_concat_and_rewrite_checks_fewer_updated PASSED [ 91%]
tests/unit/store/test_pandas_ndarray_store.py::test_panel_converted_to_dataframe_and_stacked_to_write PASSED [ 91%]
tests/unit/store/test_pandas_ndarray_store.py::test_panel_append_not_supported PASSED [ 91%]
tests/unit/store/test_pandas_ndarray_store.py::test_panel_converted_from_dataframe_for_reading PASSED [ 91%]
tests/unit/store/test_pandas_ndarray_store.py::test_raises_upon_empty_panel_write PASSED [ 91%]
tests/unit/store/test_pandas_ndarray_store.py::test_read_multi_index_with_no_ts_info PASSED [ 91%]
tests/unit/store/test_pickle_store.py::test_write PASSED                 [ 92%]
tests/unit/store/test_pickle_store.py::test_write_object PASSED          [ 92%]
tests/unit/store/test_pickle_store.py::test_read PASSED                  [ 92%]
tests/unit/store/test_pickle_store.py::test_read_object_backwards_compat PASSED [ 92%]
tests/unit/store/test_pickle_store.py::test_read_object_2 PASSED         [ 92%]
tests/unit/store/test_pickle_store.py::test_read_with_base_version_id PASSED [ 92%]
tests/unit/store/test_pickle_store.py::test_read_backward_compatibility PASSED [ 92%]
tests/unit/store/test_pickle_store.py::test_unpickle_highest_protocol PASSED [ 92%]
tests/unit/store/test_pickle_store.py::test_pickle_chunk_V1_read PASSED  [ 92%]
tests/unit/store/test_pickle_store.py::test_pickle_store_future_version PASSED [ 92%]
tests/unit/store/test_version_item.py::test_versioned_item_str PASSED    [ 92%]
tests/unit/store/test_version_item.py::test_versioned_item_default_host PASSED [ 92%]
tests/unit/store/test_version_item.py::test_versioned_item_str_handles_none PASSED [ 92%]
tests/unit/store/test_version_item.py::test_versioned_item_metadata_dict PASSED [ 92%]
tests/unit/store/test_version_store.py::test_delete_version_version_not_found PASSED [ 93%]
tests/unit/store/test_version_store.py::test_list_versions_localTime PASSED [ 93%]
tests/unit/store/test_version_store.py::test_list_versions_no_snapshot PASSED [ 93%]
tests/unit/store/test_version_store.py::test__read_preference__allow_secondary_true PASSED [ 93%]
tests/unit/store/test_version_store.py::test__read_preference__allow_secondary_false PASSED [ 93%]
tests/unit/store/test_version_store.py::test__read_preference__default_true PASSED [ 93%]
tests/unit/store/test_version_store.py::test__read_preference__default_false PASSED [ 93%]
tests/unit/store/test_version_store.py::test_get_version_allow_secondary_True PASSED [ 93%]
tests/unit/store/test_version_store.py::test_get_version_allow_secondary_user_override_False PASSED [ 93%]
tests/unit/store/test_version_store.py::test_read_as_of_LondonTime PASSED [ 93%]
tests/unit/store/test_version_store.py::test_read_as_of_NotNaive PASSED  [ 93%]
tests/unit/store/test_version_store.py::test_read_metadata_no_asof PASSED [ 93%]
tests/unit/store/test_version_store.py::test_write_check_quota PASSED    [ 93%]
tests/unit/store/test_version_store.py::test_initialize_library PASSED   [ 94%]
tests/unit/store/test_version_store.py::test_ensure_index PASSED         [ 94%]
tests/unit/store/test_version_store.py::test_prune_previous_versions_0_timeout PASSED [ 94%]
tests/unit/store/test_version_store.py::test_read_handles_operation_failure PASSED [ 94%]
tests/unit/store/test_version_store.py::test_read_reports_random_errors PASSED [ 94%]
tests/unit/store/test_version_store.py::test_snapshot PASSED             [ 94%]
tests/unit/store/test_version_store.py::test_list_symbols_default_pipeline PASSED [ 94%]
tests/unit/store/test_version_store.py::test_snapshot_duplicate_raises_exception PASSED [ 94%]
tests/unit/store/test_version_store.py::test_write_metadata_no_previous_data PASSED [ 94%]
tests/unit/store/test_version_store.py::test_write_metadata_with_previous_data PASSED [ 94%]
tests/unit/store/test_version_store.py::test_write_empty_metadata PASSED [ 94%]
tests/unit/store/test_version_store.py::test_write_metadata_insert_version_dupkeyerror PASSED [ 94%]
tests/unit/store/test_version_store.py::test_write_metadata_insert_version_opfailure PASSED [ 94%]
tests/unit/store/test_version_store.py::test_restore_version PASSED      [ 94%]
tests/unit/store/test_version_store.py::test_restore_version_data_missing_symbol PASSED [ 95%]
tests/unit/store/test_version_store.py::test_restore_last_version PASSED [ 95%]
tests/unit/store/test_version_store.py::test_write_error_clean_retry PASSED [ 95%]
tests/unit/store/test_version_store.py::test_write_insert_version_duplicatekey PASSED [ 95%]
tests/unit/store/test_version_store.py::test_write_insert_version_operror PASSED [ 95%]
tests/unit/store/test_version_store.py::test_append_error_clean_retry PASSED [ 95%]
tests/unit/store/test_version_store.py::test_append_insert_version_duplicatekey PASSED [ 95%]
tests/unit/store/test_version_store.py::test_append_insert_version_operror PASSED [ 95%]
tests/unit/store/test_version_store_audit.py::test_data_change PASSED    [ 95%]
tests/unit/store/test_version_store_audit.py::test_ArcticTransaction_simple PASSED [ 95%]
tests/unit/store/test_version_store_audit.py::test_ArticTransaction_no_audit PASSED [ 95%]
tests/unit/store/test_version_store_audit.py::test_ArcticTransaction_writes_if_metadata_changed PASSED [ 95%]
tests/unit/store/test_version_store_audit.py::test_ArcticTransaction_writes_if_base_data_corrupted PASSED [ 95%]
tests/unit/store/test_version_store_audit.py::test_ArcticTransaction_writes_no_data_found PASSED [ 96%]
tests/unit/store/test_version_store_audit.py::test_ArcticTransaction_writes_no_data_found_deleted PASSED [ 96%]
tests/unit/store/test_version_store_audit.py::test_ArcticTransaction_does_nothing_when_data_not_modified PASSED [ 96%]
tests/unit/store/test_version_store_audit.py::test_ArcticTransaction_does_nothing_when_data_is_None PASSED [ 96%]
tests/unit/store/test_version_store_audit.py::test_ArcticTransaction_guards_against_inconsistent_ts PASSED [ 96%]
tests/unit/store/test_version_store_audit.py::test_ArcticTransaction_detects_concurrent_writes PASSED [ 96%]
tests/unit/store/test_version_store_utils.py::test_split_arrs_empty PASSED [ 96%]
tests/unit/store/test_version_store_utils.py::test_split_arrs PASSED     [ 96%]
tests/unit/store/test_version_store_utils.py::test_checksum PASSED       [ 96%]
tests/unit/store/test_version_store_utils.py::test_checksum_handles_p3strs_and_binary PASSED [ 96%]
tests/unit/store/test_version_store_utils.py::test_version_base_or_id PASSED [ 96%]
tests/unit/tickstore/test_tickstore.py::test_mongo_date_range_query PASSED [ 96%]
tests/unit/tickstore/test_tickstore.py::test_mongo_date_range_query_asserts PASSED [ 96%]
tests/unit/tickstore/test_tickstore.py::test_strify_tickstore PASSED     [ 97%]
tests/unit/tickstore/test_tickstore.py::test_tickstore_to_bucket_no_image PASSED [ 97%]
tests/unit/tickstore/test_tickstore.py::test_tickstore_to_bucket_with_image PASSED [ 97%]
tests/unit/tickstore/test_tickstore.py::test_tickstore_to_bucket_always_forwards PASSED [ 97%]
tests/unit/tickstore/test_tickstore.py::test_tickstore_to_bucket_always_forwards_image PASSED [ 97%]
tests/unit/tickstore/test_tickstore.py::test_tickstore_pandas_to_bucket_image PASSED [ 97%]
tests/unit/tickstore/test_tickstore.py::test__read_preference__allow_secondary_true PASSED [ 97%]
tests/unit/tickstore/test_tickstore.py::test__read_preference__allow_secondary_false PASSED [ 97%]
tests/unit/tickstore/test_tickstore.py::test__read_preference__default_true PASSED [ 97%]
tests/unit/tickstore/test_tickstore.py::test__read_preference__default_false PASSED [ 97%]
tests/unit/tickstore/test_toplevel.py::test_raise_exception_if_daterange_is_not_provided PASSED [ 97%]
tests/unit/tickstore/test_toplevel.py::test_raise_exception_if_date_range_does_not_contain_start_date PASSED [ 97%]
tests/unit/tickstore/test_toplevel.py::test_raise_exception_if_date_range_does_not_contain_end_date PASSED [ 97%]
tests/unit/tickstore/test_toplevel.py::test_raise_exception_if_date_range_does_not_contain_start_and_end_date PASSED [ 97%]
tests/unit/tickstore/test_toplevel.py::test_raise_exception_and_log_an_error_if_an_invalid_library_name_is_added PASSED [ 98%]
tests/unit/tickstore/test_toplevel.py::test_raise_exception_if_date_range_overlaps PASSED [ 98%]
tests/unit/tickstore/test_toplevel.py::test_add_library_to_colllection_if_date_range_is_on_UTC_or_naive_day_boundaries[start0-end0-expected_start0-expected_end0] PASSED [ 98%]
tests/unit/tickstore/test_toplevel.py::test_add_library_to_colllection_if_date_range_is_on_UTC_or_naive_day_boundaries[start1-end1-expected_start1-expected_end1] PASSED [ 98%]
tests/unit/tickstore/test_toplevel.py::test_add_library_to_colllection_if_date_range_is_on_UTC_or_naive_day_boundaries[start2-end2-expected_start2-expected_end2] PASSED [ 98%]
tests/unit/tickstore/test_toplevel.py::test_raise_error_add_library_is_called_with_a_date_range_not_on_day_boundaries[start0-end0] PASSED [ 98%]
tests/unit/tickstore/test_toplevel.py::test_raise_error_add_library_is_called_with_a_date_range_not_on_day_boundaries[start1-end1] PASSED [ 98%]
tests/unit/tickstore/test_toplevel.py::test_raise_error_add_library_is_called_with_a_date_range_not_on_day_boundaries[start2-end2] PASSED [ 98%]
tests/unit/tickstore/test_toplevel.py::test_raise_error_add_library_is_called_with_a_date_range_not_on_day_boundaries[start3-end3] PASSED [ 98%]
tests/unit/tickstore/test_toplevel.py::test_raise_error_add_library_is_called_with_a_date_range_not_on_day_boundaries[start4-end4] PASSED [ 98%]
tests/unit/tickstore/test_toplevel.py::test_raise_error_add_library_is_called_with_a_date_range_not_on_day_boundaries[start5-end5] PASSED [ 98%]
tests/unit/tickstore/test_toplevel.py::test_raise_error_add_library_is_called_with_a_date_range_not_on_day_boundaries[start6-end6] PASSED [ 98%]
tests/unit/tickstore/test_toplevel.py::test_raise_error_add_library_is_called_with_a_date_range_not_on_day_boundaries[start7-end7] PASSED [ 98%]
tests/unit/tickstore/test_toplevel.py::test_raise_error_add_library_is_called_with_a_date_range_not_on_day_boundaries[start8-end8] PASSED [ 99%]
tests/unit/tickstore/test_toplevel.py::test_slice_pandas_dataframe[start0-end0-0-3] PASSED [ 99%]
tests/unit/tickstore/test_toplevel.py::test_slice_pandas_dataframe[start1-end1-0-3] PASSED [ 99%]
tests/unit/tickstore/test_toplevel.py::test_slice_pandas_dataframe[start2-end2-1-3] PASSED [ 99%]
tests/unit/tickstore/test_toplevel.py::test_slice_pandas_dataframe[start3-end3-1-2] PASSED [ 99%]
tests/unit/tickstore/test_toplevel.py::test_slice_pandas_dataframe[start4-end4-0-3] PASSED [ 99%]
tests/unit/tickstore/test_toplevel.py::test_slice_list_of_dicts[start0-end0-0-3] PASSED [ 99%]
tests/unit/tickstore/test_toplevel.py::test_slice_list_of_dicts[start1-end1-0-3] PASSED [ 99%]
tests/unit/tickstore/test_toplevel.py::test_slice_list_of_dicts[start2-end2-1-3] PASSED [ 99%]
tests/unit/tickstore/test_toplevel.py::test_slice_list_of_dicts[start3-end3-1-2] PASSED [ 99%]
tests/unit/tickstore/test_toplevel.py::test_slice_list_of_dicts[start4-end4-0-3] PASSED [ 99%]
tests/unit/tickstore/test_toplevel.py::test_write_pandas_data_to_right_libraries PASSED [ 99%]
tests/unit/tickstore/test_toplevel.py::test_read PASSED                  [ 99%]
tests/unit/tickstore/test_toplevel.py::test_slice_raises PASSED          [100%]
=============================== warnings summary ===============================
tests/integration/test_arctic.py::test_delete_library
tests/integration/test_arctic.py::test_lib_rename
tests/integration/test_arctic.py::test_lib_rename_namespace
tests/integration/test_arctic.py::test_renaming_returns_new_name_in_cache
tests/integration/test_arctic.py::test_deleting_library_removes_it_from_cache
tests/integration/scripts/test_delete_library.py::test_delete_library
tests/integration/scripts/test_delete_library.py::test_delete_library1
tests/integration/scripts/test_delete_library.py::test_delete_library2
tests/integration/scripts/test_delete_library.py::test_delete_library3
tests/integration/scripts/test_delete_library.py::test_delete_library_doesnt_exist
  /home/travis/build/man-group/arctic/arctic/_cache.py:120: DeprecationWarning: update is deprecated. Use replace_one, update_one or update_many instead.
    {"$pull": {"data": item}}
tests/integration/test_arctic.py::test_list_libraries_cached
  /home/travis/build/man-group/arctic/tests/integration/test_arctic.py:250: DeprecationWarning: remove is deprecated. Use delete_one or delete_many instead.
    arctic._conn.meta_db.cache.remove({})
tests/integration/chunkstore/test_chunkstore.py::test_write_dataframe_with_func
  /home/travis/virtualenv/python2.7.15/lib/python2.7/site-packages/pandas/core/indexing.py:621: SettingWithCopyWarning: 
  A value is trying to be set on a copy of a slice from a DataFrame.
  Try using .loc[row_indexer,col_indexer] = value instead
  
  See the caveats in the documentation: http://pandas.pydata.org/pandas-docs/stable/indexing.html#indexing-view-versus-copy
    self.obj[item_labels[indexer[info_axis]]] = value
tests/integration/store/test_pandas_store.py::test_panel_save_read[df_size0]
tests/integration/store/test_pandas_store.py::test_panel_save_read[df_size1]
tests/integration/store/test_pandas_store.py::test_panel_save_read[df_size2]
tests/integration/store/test_pandas_store.py::test_panel_save_read[df_size3]
tests/integration/store/test_pandas_store.py::test_panel_save_read[df_size4]
tests/integration/store/test_pandas_store.py::test_panel_save_read[df_size5]
tests/integration/store/test_pandas_store.py::test_panel_save_read[df_size6]
tests/integration/store/test_pandas_store.py::test_panel_save_read[df_size7]
tests/integration/store/test_pandas_store.py::test_panel_save_read[df_size8]
tests/integration/store/test_pandas_store.py::test_panel_save_read[df_size9]
  /home/travis/build/man-group/arctic/tests/integration/store/test_pandas_store.py:660: DeprecationWarning: 
  Panel is deprecated and will be removed in a future version.
  The recommended way to represent these types of 3-dimensional data are with a MultiIndex on a DataFrame, via the Panel.to_frame() method
  Alternatively, you can use the xarray package http://xarray.pydata.org/en/stable/.
  Pandas provides a `.to_xarray()` method to help automate this conversion.
  
    pn = panel(*df_size)
tests/integration/store/test_pandas_store.py::test_panel_save_read[df_size0]
tests/integration/store/test_pandas_store.py::test_panel_save_read[df_size1]
tests/integration/store/test_pandas_store.py::test_panel_save_read[df_size2]
tests/integration/store/test_pandas_store.py::test_panel_save_read[df_size3]
tests/integration/store/test_pandas_store.py::test_panel_save_read[df_size4]
tests/integration/store/test_pandas_store.py::test_panel_save_read[df_size5]
tests/integration/store/test_pandas_store.py::test_panel_save_read[df_size6]
tests/integration/store/test_pandas_store.py::test_panel_save_read[df_size7]
tests/integration/store/test_pandas_store.py::test_panel_save_read[df_size8]
tests/integration/store/test_pandas_store.py::test_panel_save_read[df_size9]
  /home/travis/build/man-group/arctic/arctic/store/_pandas_ndarray_store.py:249: DeprecationWarning: 
  Panel is deprecated and will be removed in a future version.
  The recommended way to represent these types of 3-dimensional data are with a MultiIndex on a DataFrame, via the Panel.to_frame() method
  Alternatively, you can use the xarray package http://xarray.pydata.org/en/stable/.
  Pandas provides a `.to_xarray()` method to help automate this conversion.
  
    return item.iloc[:, 0].unstack().to_panel()
tests/integration/store/test_pandas_store.py::test_panel_save_read_with_nans
  /home/travis/virtualenv/python2.7.15/lib/python2.7/site-packages/_pytest/python.py:174: DeprecationWarning: 
  Panel is deprecated and will be removed in a future version.
  The recommended way to represent these types of 3-dimensional data are with a MultiIndex on a DataFrame, via the Panel.to_frame() method
  Alternatively, you can use the xarray package http://xarray.pydata.org/en/stable/.
  Pandas provides a `.to_xarray()` method to help automate this conversion.
  
    testfunction(**testargs)
tests/integration/store/test_pandas_store.py::test_panel_save_read_with_nans
  /home/travis/build/man-group/arctic/arctic/store/_pandas_ndarray_store.py:250: DeprecationWarning: 
  Panel is deprecated and will be removed in a future version.
  The recommended way to represent these types of 3-dimensional data are with a MultiIndex on a DataFrame, via the Panel.to_frame() method
  Alternatively, you can use the xarray package http://xarray.pydata.org/en/stable/.
  Pandas provides a `.to_xarray()` method to help automate this conversion.
  
    return item.to_panel()
tests/integration/store/test_pandas_store.py::test_duplicate_labels
tests/integration/store/test_pandas_store.py::test_duplicate_labels
tests/integration/store/test_pandas_store.py::test_duplicate_labels
tests/integration/store/test_pandas_store.py::test_duplicate_labels
tests/integration/store/test_pandas_store.py::test_duplicate_labels
tests/integration/store/test_pandas_store.py::test_duplicate_labels
  /home/travis/virtualenv/python2.7.15/lib/python2.7/site-packages/numpy/core/numeric.py:2591: DeprecationWarning: elementwise comparison failed; this will raise an error in the future.
    return bool(asarray(a1 == a2).all())
tests/integration/tickstore/test_toplevel.py::test_should_return_data_when_date_range_falls_in_a_single_underlying_library
  /home/travis/build/man-group/arctic/arctic/tickstore/tickstore.py:419: FutureWarning: Conversion of the second argument of issubdtype from `int` to `np.signedinteger` is deprecated. In future, it will be treated as `np.int64 == np.dtype(int).type`.
    if np.issubdtype(dtype, int):
-- Docs: https://docs.pytest.org/en/latest/warnings.html
------ generated xml file: /home/travis/build/man-group/arctic/junit.xml -------
---------- coverage: platform linux2, python 2.7.15-final-0 ----------
Coverage HTML written to dir htmlcov
Coverage XML written to file coverage.xml
 1317 passed, 3 skipped, 6 xfailed, 13 xpassed, 41 warnings in 1336.84 seconds =
The command "python setup.py test --pytest-args=-v" exited with 0.
0.99s$ pycodestyle arctic
The command "pycodestyle arctic" exited with 0.
Done. Your build exited with 0.
```