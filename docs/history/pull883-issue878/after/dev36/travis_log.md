```shell
$ source ~/virtualenv/python3.6/bin/activate0.00s0.15s0.09s0.07s
worker_info
Worker information
0.16s0.01s0.00s0.01s
system_info
Build system information
0.01s0.01s0.70s0.23s0.05s0.00s0.04s0.00s0.01s0.01s0.01s0.01s0.01s0.00s0.00s0.02s0.00s0.01s0.34s0.00s0.00s0.00s0.01s0.00s0.09s0.01s0.81s0.00s0.00s6.04s0.00s2.76s0.00s2.60s
docker_mtu_and_registry_mirrors
resolvconf
services
3.02s$ sudo systemctl start mongod
git.checkout
0.77s$ git clone --depth=50 https://github.com/man-group/arctic.git man-group/arctic
git.submodule
0.03s$ git submodule update --init --recursive
$ python --version
Python 3.6.7
$ pip --version
pip 20.1.1 from /home/travis/virtualenv/python3.6.7/lib/python3.6/site-packages/pip (python 3.6)
before_install
1.05s$ pip install pycodestyle
install.1
0.13s$ mongo --version
install.2
2.24s$ pip install --upgrade pip
install.3
0.86s$ pip install python-dateutil --upgrade
install.4
1.09s$ pip install pytz --upgrade
install.5
0.75s$ pip install tzlocal --upgrade
install.6
1.55s$ pip install pymongo --upgrade
install.7
3.72s$ pip install numpy --upgrade
install.8
4.39s$ pip install pandas --upgrade
install.9
0.77s$ pip install decorator --upgrade
install.10
0.74s$ pip install enum34 --upgrade
install.11
1.21s$ pip install lz4 --upgrade
install.12
0.83s$ pip install mock --upgrade
install.13
0.74s$ pip install mockextras
install.14
1.77s$ pip install pytest --upgrade
install.15
1.54s$ pip install pytest-cov --upgrade
install.16
5.19s$ pip install pytest-server-fixtures --upgrade
install.17
0.90s$ pip install pytest-timeout --upgrade
install.18
1.08s$ pip install pytest-xdist --upgrade
install.19
0.89s$ pip install setuptools-git --upgrade
install.20
0.00s$ if [[ $TRAVIS_PYTHON_VERSION == 2.7 ]]; then pip install pandas==0.22.0; fi
0.36s$ pip freeze
apipkg==1.5
atomicwrites==1.2.1
attrs==20.3.0
certifi==2018.10.15
chardet==4.0.0
contextlib2==0.6.0.post1
coverage==5.4
decorator==4.4.2
enum34==1.1.10
execnet==1.8.0
future==0.18.2
idna==2.10
importlib-metadata==0.18
iniconfig==1.1.1
lz4==3.1.3
mock==4.0.3
mockextras==1.0.2
more-itertools==4.3.0
nose==1.3.7
numpy==1.19.5
packaging==19.0
pandas==1.1.5
path==15.0.1
path.py==12.5.0
pbr==5.0.0
pipenv==2018.11.26
pluggy==0.12.0
psutil==5.8.0
py==1.10.0
pycodestyle==2.6.0
pymongo==3.11.2
pyparsing==2.4.0
pytest==6.2.2
pytest-cov==2.11.1
pytest-fixture-config==1.7.0
pytest-forked==1.3.0
pytest-server-fixtures==1.7.0
pytest-shutil==1.7.0
pytest-timeout==1.4.2
pytest-xdist==2.2.0
python-dateutil==2.8.1
pytz==2020.5
requests==2.25.1
retry==0.9.2
setuptools-git==1.2
six==1.11.0
termcolor==1.1.0
toml==0.10.2
tzlocal==2.1
urllib3==1.26.3
virtualenv==16.0.0
virtualenv-clone==0.4.0
wcwidth==0.1.7
zipp==0.5.1
The command "pip freeze" exited with 0.
1327.80s$ python setup.py test --pytest-args=-v
running test
WARNING: Testing via this command is deprecated and will be removed in a future version. Users looking for a generic test entry point independent of test runner are encouraged to use tox.
running egg_info
creating arctic.egg-info
writing arctic.egg-info/PKG-INFO
writing dependency_links to arctic.egg-info/dependency_links.txt
writing entry points to arctic.egg-info/entry_points.txt
writing requirements to arctic.egg-info/requires.txt
writing top-level names to arctic.egg-info/top_level.txt
writing manifest file 'arctic.egg-info/SOURCES.txt'
writing manifest file 'arctic.egg-info/SOURCES.txt'
running build_ext
============================= test session starts ==============================
platform linux -- Python 3.6.7, pytest-6.2.2, py-1.10.0, pluggy-0.12.0 -- /home/travis/virtualenv/python3.6.7/bin/python
cachedir: .pytest_cache
rootdir: /home/travis/build/man-group/arctic
plugins: xdist-1.26.1, server-fixtures-1.7.0, shutil-1.7.0, timeout-1.4.2, cov-2.11.1, forked-1.3.0
collected 1339 items                                                           
tests/integration/test_arctic.py::test_connect_to_Arctic_string PASSED   [  0%]2021-01-28 02:12:52,731 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/test_arctic.py::test_connect_to_Arctic_connection PASSED [  0%]2021-01-28 02:12:53,409 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/test_arctic.py::test_reset_Arctic PASSED               [  0%]2021-01-28 02:12:54,295 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/test_arctic.py::test_re_authenticate_on_arctic_reset PASSED [  0%]2021-01-28 02:12:55,185 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/test_arctic.py::test_simple PASSED                     [  0%]2021-01-28 02:12:57,893 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/test_arctic.py::test_indexes PASSED                    [  0%]2021-01-28 02:12:58,768 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/test_arctic.py::test_delete_library PASSED             [  0%]2021-01-28 02:12:59,940 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/test_arctic.py::test_quota PASSED                      [  0%]2021-01-28 02:13:00,858 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/test_arctic.py::test_check_quota PASSED                [  0%]2021-01-28 02:13:01,742 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/test_arctic.py::test_default_mongo_retry_timout PASSED [  0%]
tests/integration/test_arctic.py::test_lib_rename PASSED                 [  0%]
tests/integration/test_arctic.py::test_lib_rename_namespace PASSED       [  0%]
tests/integration/test_arctic.py::test_lib_type PASSED                   [  0%]2021-01-28 02:13:04,428 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/test_arctic.py::test_library_exists PASSED             [  1%]2021-01-28 02:13:05,311 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/test_arctic.py::test_library_exists_no_auth PASSED     [  1%]
tests/integration/test_arctic.py::test_list_libraries_cached PASSED      [  1%]2021-01-28 02:13:07,275 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/test_arctic.py::test_initialize_library_adds_to_cache PASSED [  1%]2021-01-28 02:13:08,579 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/test_arctic.py::test_cache_does_not_return_stale_data PASSED [  1%]2021-01-28 02:13:09,884 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/test_arctic.py::test_renaming_returns_new_name_in_cache PASSED [  1%]2021-01-28 02:13:11,004 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/test_arctic.py::test_deleting_library_removes_it_from_cache PASSED [  1%]2021-01-28 02:13:12,245 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/test_arctic.py::test_disable_cache_by_settings PASSED  [  1%]2021-01-28 02:13:13,154 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/test_arctic_multithreading.py::test_multiprocessing_safety PASSED [  1%]2021-01-28 02:13:38,180 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/test_arctic_multithreading.py::test_multiprocessing_safety_parent_children_race PASSED [  1%]2021-01-28 02:13:58,287 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
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
tests/integration/test_concurrent_append.py::test_append_kill PASSED     [  2%]2021-01-28 02:17:06,263 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/test_decorators.py::test_get_host_VersionStore PASSED  [  2%]2021-01-28 02:17:07,133 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/test_howtos.py::test_howto[how_to_custom_arctic_library.py] PASSED [  2%]2021-01-28 02:17:07,873 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/test_howtos.py::test_howto[how_to_use_arctic.py] PASSED [  2%]2021-01-28 02:17:08,824 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_chunkstore.py::test_write_dataframe PASSED [  2%]2021-01-28 02:17:09,749 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_chunkstore.py::test_upsert_dataframe PASSED [  2%]2021-01-28 02:17:10,661 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_chunkstore.py::test_write_dataframe_noindex PASSED [  3%]2021-01-28 02:17:11,555 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_chunkstore.py::test_overwrite_dataframe PASSED [  3%]2021-01-28 02:17:12,463 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_chunkstore.py::test_overwrite_dataframe_noindex PASSED [  3%]2021-01-28 02:17:13,351 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_chunkstore.py::test_overwrite_dataframe_monthly PASSED [  3%]2021-01-28 02:17:14,288 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_chunkstore.py::test_write_read_with_daterange PASSED [  3%]2021-01-28 02:17:15,200 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_chunkstore.py::test_write_read_with_daterange_noindex PASSED [  3%]2021-01-28 02:17:16,083 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_chunkstore.py::test_store_single_index_df PASSED [  3%]2021-01-28 02:17:16,974 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_chunkstore.py::test_no_range PASSED    [  3%]2021-01-28 02:17:17,860 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_chunkstore.py::test_closed_open PASSED [  3%]2021-01-28 02:17:18,748 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_chunkstore.py::test_open_closed PASSED [  3%]2021-01-28 02:17:19,635 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_chunkstore.py::test_closed_open_no_index PASSED [  3%]2021-01-28 02:17:20,516 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_chunkstore.py::test_open_open_no_index PASSED [  3%]2021-01-28 02:17:21,408 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_chunkstore.py::test_monthly_df PASSED  [  3%]2021-01-28 02:17:22,300 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_chunkstore.py::test_yearly_df PASSED   [  4%]2021-01-28 02:17:23,183 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_chunkstore.py::test_append_daily PASSED [  4%]2021-01-28 02:17:24,216 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_chunkstore.py::test_append_monthly PASSED [  4%]2021-01-28 02:17:25,161 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_chunkstore.py::test_append_yearly PASSED [  4%]2021-01-28 02:17:26,066 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_chunkstore.py::test_append_existing_chunk PASSED [  4%]2021-01-28 02:17:26,950 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_chunkstore.py::test_store_objects_df PASSED [  4%]2021-01-28 02:17:27,827 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_chunkstore.py::test_empty_range PASSED [  4%]2021-01-28 02:17:28,710 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_chunkstore.py::test_update PASSED      [  4%]2021-01-28 02:17:29,633 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_chunkstore.py::test_update_no_overlap PASSED [  4%]2021-01-28 02:17:30,552 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_chunkstore.py::test_update_chunk_range PASSED [  4%]2021-01-28 02:17:31,462 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_chunkstore.py::test_update_chunk_range_overlap PASSED [  4%]2021-01-28 02:17:32,357 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_chunkstore.py::test_append_before PASSED [  4%]2021-01-28 02:17:33,277 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_chunkstore.py::test_append_and_update PASSED [  4%]2021-01-28 02:17:34,224 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_chunkstore.py::test_update_same_df PASSED [  5%]2021-01-28 02:17:35,132 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_chunkstore.py::test_df_with_multiindex PASSED [  5%]2021-01-28 02:17:36,021 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_chunkstore.py::test_with_strings PASSED [  5%]2021-01-28 02:17:36,908 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_chunkstore.py::test_with_strings_multiindex_append PASSED [  5%]2021-01-28 02:17:37,843 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_chunkstore.py::test_multiple_actions PASSED [  5%]2021-01-28 02:17:49,884 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_chunkstore.py::test_multiple_actions_monthly_data PASSED [  5%]2021-01-28 02:17:55,714 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_chunkstore.py::test_delete PASSED      [  5%]2021-01-28 02:17:56,674 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_chunkstore.py::test_delete_empty_df_on_range PASSED [  5%]2021-01-28 02:17:57,637 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_chunkstore.py::test_get_info PASSED    [  5%]2021-01-28 02:17:58,545 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_chunkstore.py::test_get_info_after_append PASSED [  5%]2021-01-28 02:18:00,130 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_chunkstore.py::test_get_info_after_update PASSED [  5%]2021-01-28 02:18:01,043 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_chunkstore.py::test_delete_range PASSED [  5%]2021-01-28 02:18:01,976 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_chunkstore.py::test_delete_range_noindex PASSED [  5%]2021-01-28 02:18:02,890 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_chunkstore.py::test_read_chunk_range PASSED [  5%]2021-01-28 02:18:03,835 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_chunkstore.py::test_read_data_doesnt_exist PASSED [  6%]
tests/integration/chunkstore/test_chunkstore.py::test_invalid_type PASSED [  6%]
tests/integration/chunkstore/test_chunkstore.py::test_append_no_data PASSED [  6%]
tests/integration/chunkstore/test_chunkstore.py::test_append_upsert PASSED [  6%]2021-01-28 02:18:07,297 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_chunkstore.py::test_append_no_new_data PASSED [  6%]2021-01-28 02:18:08,462 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_chunkstore.py::test_overwrite_series PASSED [  6%]2021-01-28 02:18:09,343 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_chunkstore.py::test_overwrite_series_monthly PASSED [  6%]2021-01-28 02:18:10,232 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_chunkstore.py::test_pandas_datetime_index_store_series PASSED [  6%]2021-01-28 02:18:11,114 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_chunkstore.py::test_yearly_series PASSED [  6%]2021-01-28 02:18:11,971 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_chunkstore.py::test_store_objects_series PASSED [  6%]2021-01-28 02:18:12,857 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_chunkstore.py::test_update_series PASSED [  6%]2021-01-28 02:18:13,771 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_chunkstore.py::test_update_same_series PASSED [  6%]2021-01-28 02:18:14,664 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_chunkstore.py::test_dtype_mismatch PASSED [  6%]2021-01-28 02:18:15,564 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_chunkstore.py::test_read_column_subset PASSED [  7%]2021-01-28 02:18:16,467 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_chunkstore.py::test_rename PASSED      [  7%]
tests/integration/chunkstore/test_chunkstore.py::test_pass_thru_chunker PASSED [  7%]2021-01-28 02:18:18,366 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_chunkstore.py::test_pass_thru_chunker_append PASSED [  7%]2021-01-28 02:18:19,231 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_chunkstore.py::test_pass_thru_chunker_update PASSED [  7%]2021-01-28 02:18:20,103 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_chunkstore.py::test_pass_thru_chunker_update_range PASSED [  7%]2021-01-28 02:18:20,975 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_chunkstore.py::test_size_chunking PASSED [  7%]2021-01-28 02:18:24,587 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_chunkstore.py::test_size_chunk_append PASSED [  7%]2021-01-28 02:18:31,991 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_chunkstore.py::test_delete_range_segment PASSED [  7%]2021-01-28 02:18:37,980 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_chunkstore.py::test_size_chunk_update PASSED [  7%]2021-01-28 02:18:45,157 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_chunkstore.py::test_size_chunk_multiple_update PASSED [  7%]2021-01-28 02:18:48,872 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_chunkstore.py::test_get_chunk_range PASSED [  7%]2021-01-28 02:18:49,737 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_chunkstore.py::test_iterators PASSED   [  7%]2021-01-28 02:18:50,747 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_chunkstore.py::test_unnamed_colums PASSED [  7%]
tests/integration/chunkstore/test_chunkstore.py::test_quarterly_data PASSED [  8%]2021-01-28 02:18:52,491 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_chunkstore.py::test_list_symbols PASSED [  8%]2021-01-28 02:18:57,780 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_chunkstore.py::test_stats PASSED       [  8%]2021-01-28 02:19:03,268 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_chunkstore.py::test_metadata PASSED    [  8%]2021-01-28 02:19:04,229 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_chunkstore.py::test_metadata_update PASSED [  8%]2021-01-28 02:19:05,132 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_chunkstore.py::test_metadata_nosymbol PASSED [  8%]2021-01-28 02:19:05,960 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_chunkstore.py::test_metadata_none PASSED [  8%]2021-01-28 02:19:06,819 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_chunkstore.py::test_metadata_invalid PASSED [  8%]2021-01-28 02:19:07,682 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_chunkstore.py::test_write_metadata PASSED [  8%]2021-01-28 02:19:08,531 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_chunkstore.py::test_write_metadata_nosymbol PASSED [  8%]2021-01-28 02:19:09,360 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_chunkstore.py::test_audit PASSED       [  8%]2021-01-28 02:19:10,472 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_chunkstore.py::test_chunkstore_misc PASSED [  8%]2021-01-28 02:19:11,307 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_chunkstore.py::test_unsorted_index PASSED [  8%]2021-01-28 02:19:12,226 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_chunkstore.py::test_unsorted_date_col PASSED [  9%]2021-01-28 02:19:13,143 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_chunkstore.py::test_chunk_range_with_dti PASSED [  9%]2021-01-28 02:19:14,011 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_chunkstore.py::test_chunkstore_multiread PASSED [  9%]2021-01-28 02:19:15,039 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_chunkstore.py::test_chunkstore_multiread_samedate PASSED [  9%]2021-01-28 02:19:16,030 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_chunkstore.py::test_write_dataframe_with_func PASSED [  9%]2021-01-28 02:19:16,934 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_fixes.py::test_write_dataframe PASSED  [  9%]2021-01-28 02:19:17,817 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_fixes.py::test_compression PASSED      [  9%]2021-01-28 02:19:19,920 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_fixes.py::test_date_interval PASSED    [  9%]2021-01-28 02:19:21,081 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_fixes.py::test_rewrite PASSED          [  9%]2021-01-28 02:19:21,968 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_fixes.py::test_iterator PASSED         [  9%]2021-01-28 02:19:23,270 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_fixes.py::test_missing_cols PASSED     [  9%]2021-01-28 02:19:24,228 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_fixes.py::test_column_copy PASSED      [  9%]2021-01-28 02:19:25,102 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_fixes.py::test_get_info_empty PASSED   [  9%]2021-01-28 02:19:25,944 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_utils.py::test_read_apply PASSED       [ 10%]2021-01-28 02:19:26,804 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/tools/test_tools.py::test_segment_repair_tool PASSED [ 10%]2021-01-28 02:19:30,230 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/fixtures/test_arctic.py::test_arctic PASSED            [ 10%]2021-01-28 02:19:30,911 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/fixtures/test_arctic.py::test_library PASSED           [ 10%]2021-01-28 02:19:31,790 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/fixtures/test_arctic.py::test_ms_lib PASSED            [ 10%]2021-01-28 02:19:32,543 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_arctic_fsck.py::test_cleanup_orphaned_chunks[True-data0-FwPointersCfg.DISABLED] PASSED [ 10%]2021-01-28 02:19:33,476 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_arctic_fsck.py::test_cleanup_orphaned_chunks[True-data1-FwPointersCfg.HYBRID] PASSED [ 10%]2021-01-28 02:19:34,408 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_arctic_fsck.py::test_cleanup_orphaned_chunks[True-data2-FwPointersCfg.ENABLED] PASSED [ 10%]2021-01-28 02:19:35,345 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_arctic_fsck.py::test_cleanup_orphaned_chunks[True-data3-FwPointersCfg.DISABLED] PASSED [ 10%]2021-01-28 02:19:36,282 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_arctic_fsck.py::test_cleanup_orphaned_chunks[True-data4-FwPointersCfg.HYBRID] PASSED [ 10%]2021-01-28 02:19:37,231 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_arctic_fsck.py::test_cleanup_orphaned_chunks[True-data5-FwPointersCfg.ENABLED] PASSED [ 10%]2021-01-28 02:19:38,173 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_arctic_fsck.py::test_cleanup_orphaned_chunks[False-data6-FwPointersCfg.DISABLED] PASSED [ 10%]2021-01-28 02:19:39,119 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_arctic_fsck.py::test_cleanup_orphaned_chunks[False-data7-FwPointersCfg.HYBRID] PASSED [ 10%]2021-01-28 02:19:40,062 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_arctic_fsck.py::test_cleanup_orphaned_chunks[False-data8-FwPointersCfg.ENABLED] PASSED [ 10%]2021-01-28 02:19:41,002 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_arctic_fsck.py::test_cleanup_orphaned_chunks[False-data9-FwPointersCfg.DISABLED] PASSED [ 11%]2021-01-28 02:19:41,930 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_arctic_fsck.py::test_cleanup_orphaned_chunks[False-data10-FwPointersCfg.HYBRID] PASSED [ 11%]2021-01-28 02:19:42,866 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_arctic_fsck.py::test_cleanup_orphaned_chunks[False-data11-FwPointersCfg.ENABLED] PASSED [ 11%]2021-01-28 02:19:43,802 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_arctic_fsck.py::test_cleanup_noop[True-data0-FwPointersCfg.DISABLED] PASSED [ 11%]2021-01-28 02:19:44,719 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_arctic_fsck.py::test_cleanup_noop[True-data1-FwPointersCfg.HYBRID] PASSED [ 11%]2021-01-28 02:19:45,645 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_arctic_fsck.py::test_cleanup_noop[True-data2-FwPointersCfg.ENABLED] PASSED [ 11%]2021-01-28 02:19:46,569 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_arctic_fsck.py::test_cleanup_noop[True-data3-FwPointersCfg.DISABLED] PASSED [ 11%]2021-01-28 02:19:47,523 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_arctic_fsck.py::test_cleanup_noop[True-data4-FwPointersCfg.HYBRID] PASSED [ 11%]2021-01-28 02:19:48,482 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_arctic_fsck.py::test_cleanup_noop[True-data5-FwPointersCfg.ENABLED] PASSED [ 11%]2021-01-28 02:19:49,435 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_arctic_fsck.py::test_cleanup_noop[False-data6-FwPointersCfg.DISABLED] PASSED [ 11%]2021-01-28 02:19:50,374 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_arctic_fsck.py::test_cleanup_noop[False-data7-FwPointersCfg.HYBRID] PASSED [ 11%]2021-01-28 02:19:51,310 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_arctic_fsck.py::test_cleanup_noop[False-data8-FwPointersCfg.ENABLED] PASSED [ 11%]2021-01-28 02:19:52,251 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_arctic_fsck.py::test_cleanup_noop[False-data9-FwPointersCfg.DISABLED] PASSED [ 11%]2021-01-28 02:19:53,230 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_arctic_fsck.py::test_cleanup_noop[False-data10-FwPointersCfg.HYBRID] PASSED [ 12%]2021-01-28 02:19:54,184 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_arctic_fsck.py::test_cleanup_noop[False-data11-FwPointersCfg.ENABLED] PASSED [ 12%]2021-01-28 02:19:55,141 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_arctic_fsck.py::test_cleanup_orphaned_chunks_ignores_recent[True-data0-FwPointersCfg.DISABLED] PASSED [ 12%]2021-01-28 02:19:56,070 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_arctic_fsck.py::test_cleanup_orphaned_chunks_ignores_recent[True-data1-FwPointersCfg.HYBRID] PASSED [ 12%]2021-01-28 02:19:57,010 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_arctic_fsck.py::test_cleanup_orphaned_chunks_ignores_recent[True-data2-FwPointersCfg.ENABLED] PASSED [ 12%]2021-01-28 02:19:57,953 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_arctic_fsck.py::test_cleanup_orphaned_chunks_ignores_recent[True-data3-FwPointersCfg.DISABLED] PASSED [ 12%]2021-01-28 02:19:58,907 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_arctic_fsck.py::test_cleanup_orphaned_chunks_ignores_recent[True-data4-FwPointersCfg.HYBRID] PASSED [ 12%]2021-01-28 02:19:59,834 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_arctic_fsck.py::test_cleanup_orphaned_chunks_ignores_recent[True-data5-FwPointersCfg.ENABLED] PASSED [ 12%]2021-01-28 02:20:00,764 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_arctic_fsck.py::test_cleanup_orphaned_chunks_ignores_recent[False-data6-FwPointersCfg.DISABLED] PASSED [ 12%]2021-01-28 02:20:01,695 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_arctic_fsck.py::test_cleanup_orphaned_chunks_ignores_recent[False-data7-FwPointersCfg.HYBRID] PASSED [ 12%]2021-01-28 02:20:02,635 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_arctic_fsck.py::test_cleanup_orphaned_chunks_ignores_recent[False-data8-FwPointersCfg.ENABLED] PASSED [ 12%]2021-01-28 02:20:03,581 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_arctic_fsck.py::test_cleanup_orphaned_chunks_ignores_recent[False-data9-FwPointersCfg.DISABLED] PASSED [ 12%]2021-01-28 02:20:04,509 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_arctic_fsck.py::test_cleanup_orphaned_chunks_ignores_recent[False-data10-FwPointersCfg.HYBRID] PASSED [ 12%]2021-01-28 02:20:05,448 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_arctic_fsck.py::test_cleanup_orphaned_chunks_ignores_recent[False-data11-FwPointersCfg.ENABLED] PASSED [ 12%]2021-01-28 02:20:06,384 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_arctic_fsck.py::test_cleanup_orphaned_chunk_doesnt_break_versions[data0-FwPointersCfg.DISABLED] PASSED [ 13%]2021-01-28 02:20:07,341 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_arctic_fsck.py::test_cleanup_orphaned_chunk_doesnt_break_versions[data1-FwPointersCfg.HYBRID] PASSED [ 13%]2021-01-28 02:20:08,302 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_arctic_fsck.py::test_cleanup_orphaned_chunk_doesnt_break_versions[data2-FwPointersCfg.ENABLED] PASSED [ 13%]2021-01-28 02:20:09,264 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_arctic_fsck.py::test_cleanup_orphaned_chunk_doesnt_break_versions[data3-FwPointersCfg.DISABLED] PASSED [ 13%]2021-01-28 02:20:10,268 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_arctic_fsck.py::test_cleanup_orphaned_chunk_doesnt_break_versions[data4-FwPointersCfg.HYBRID] PASSED [ 13%]2021-01-28 02:20:11,288 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_arctic_fsck.py::test_cleanup_orphaned_chunk_doesnt_break_versions[data5-FwPointersCfg.ENABLED] PASSED [ 13%]2021-01-28 02:20:12,295 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_arctic_fsck.py::test_cleanup_orphaned_snapshots[True-data0-FwPointersCfg.DISABLED] PASSED [ 13%]2021-01-28 02:20:13,246 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_arctic_fsck.py::test_cleanup_orphaned_snapshots[True-data1-FwPointersCfg.HYBRID] PASSED [ 13%]2021-01-28 02:20:14,201 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_arctic_fsck.py::test_cleanup_orphaned_snapshots[True-data2-FwPointersCfg.ENABLED] PASSED [ 13%]2021-01-28 02:20:15,154 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_arctic_fsck.py::test_cleanup_orphaned_snapshots[True-data3-FwPointersCfg.DISABLED] PASSED [ 13%]2021-01-28 02:20:16,126 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_arctic_fsck.py::test_cleanup_orphaned_snapshots[True-data4-FwPointersCfg.HYBRID] PASSED [ 13%]2021-01-28 02:20:17,116 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_arctic_fsck.py::test_cleanup_orphaned_snapshots[True-data5-FwPointersCfg.ENABLED] PASSED [ 13%]2021-01-28 02:20:18,080 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_arctic_fsck.py::test_cleanup_orphaned_snapshots[False-data6-FwPointersCfg.DISABLED] PASSED [ 13%]2021-01-28 02:20:19,013 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_arctic_fsck.py::test_cleanup_orphaned_snapshots[False-data7-FwPointersCfg.HYBRID] PASSED [ 14%]2021-01-28 02:20:19,955 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_arctic_fsck.py::test_cleanup_orphaned_snapshots[False-data8-FwPointersCfg.ENABLED] PASSED [ 14%]2021-01-28 02:20:20,897 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_arctic_fsck.py::test_cleanup_orphaned_snapshots[False-data9-FwPointersCfg.DISABLED] PASSED [ 14%]2021-01-28 02:20:21,856 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_arctic_fsck.py::test_cleanup_orphaned_snapshots[False-data10-FwPointersCfg.HYBRID] PASSED [ 14%]2021-01-28 02:20:22,829 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_arctic_fsck.py::test_cleanup_orphaned_snapshots[False-data11-FwPointersCfg.ENABLED] PASSED [ 14%]2021-01-28 02:20:23,795 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_arctic_fsck.py::test_cleanup_orphaned_snapshots_nop[True-data0-FwPointersCfg.DISABLED] PASSED [ 14%]2021-01-28 02:20:24,731 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_arctic_fsck.py::test_cleanup_orphaned_snapshots_nop[True-data1-FwPointersCfg.HYBRID] PASSED [ 14%]2021-01-28 02:20:25,669 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_arctic_fsck.py::test_cleanup_orphaned_snapshots_nop[True-data2-FwPointersCfg.ENABLED] PASSED [ 14%]2021-01-28 02:20:26,593 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_arctic_fsck.py::test_cleanup_orphaned_snapshots_nop[True-data3-FwPointersCfg.DISABLED] PASSED [ 14%]2021-01-28 02:20:27,541 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_arctic_fsck.py::test_cleanup_orphaned_snapshots_nop[True-data4-FwPointersCfg.HYBRID] PASSED [ 14%]2021-01-28 02:20:28,498 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_arctic_fsck.py::test_cleanup_orphaned_snapshots_nop[True-data5-FwPointersCfg.ENABLED] PASSED [ 14%]2021-01-28 02:20:29,456 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_arctic_fsck.py::test_cleanup_orphaned_snapshots_nop[False-data6-FwPointersCfg.DISABLED] PASSED [ 14%]2021-01-28 02:20:30,392 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_arctic_fsck.py::test_cleanup_orphaned_snapshots_nop[False-data7-FwPointersCfg.HYBRID] PASSED [ 14%]2021-01-28 02:20:31,333 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_arctic_fsck.py::test_cleanup_orphaned_snapshots_nop[False-data8-FwPointersCfg.ENABLED] PASSED [ 15%]2021-01-28 02:20:32,308 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_arctic_fsck.py::test_cleanup_orphaned_snapshots_nop[False-data9-FwPointersCfg.DISABLED] PASSED [ 15%]2021-01-28 02:20:33,297 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_arctic_fsck.py::test_cleanup_orphaned_snapshots_nop[False-data10-FwPointersCfg.HYBRID] PASSED [ 15%]2021-01-28 02:20:34,290 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_arctic_fsck.py::test_cleanup_orphaned_snapshots_nop[False-data11-FwPointersCfg.ENABLED] PASSED [ 15%]2021-01-28 02:20:35,302 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_arctic_fsck.py::test_dont_cleanup_recent_orphaned_snapshots[True-data0-FwPointersCfg.DISABLED] PASSED [ 15%]2021-01-28 02:20:36,280 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_arctic_fsck.py::test_dont_cleanup_recent_orphaned_snapshots[True-data1-FwPointersCfg.HYBRID] PASSED [ 15%]2021-01-28 02:20:37,229 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_arctic_fsck.py::test_dont_cleanup_recent_orphaned_snapshots[True-data2-FwPointersCfg.ENABLED] PASSED [ 15%]2021-01-28 02:20:38,161 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_arctic_fsck.py::test_dont_cleanup_recent_orphaned_snapshots[True-data3-FwPointersCfg.DISABLED] PASSED [ 15%]2021-01-28 02:20:39,114 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_arctic_fsck.py::test_dont_cleanup_recent_orphaned_snapshots[True-data4-FwPointersCfg.HYBRID] PASSED [ 15%]2021-01-28 02:20:40,073 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_arctic_fsck.py::test_dont_cleanup_recent_orphaned_snapshots[True-data5-FwPointersCfg.ENABLED] PASSED [ 15%]2021-01-28 02:20:41,038 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_arctic_fsck.py::test_dont_cleanup_recent_orphaned_snapshots[False-data6-FwPointersCfg.DISABLED] PASSED [ 15%]2021-01-28 02:20:41,966 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_arctic_fsck.py::test_dont_cleanup_recent_orphaned_snapshots[False-data7-FwPointersCfg.HYBRID] PASSED [ 15%]2021-01-28 02:20:42,899 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_arctic_fsck.py::test_dont_cleanup_recent_orphaned_snapshots[False-data8-FwPointersCfg.ENABLED] PASSED [ 15%]2021-01-28 02:20:43,831 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_arctic_fsck.py::test_dont_cleanup_recent_orphaned_snapshots[False-data9-FwPointersCfg.DISABLED] PASSED [ 15%]2021-01-28 02:20:44,786 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_arctic_fsck.py::test_dont_cleanup_recent_orphaned_snapshots[False-data10-FwPointersCfg.HYBRID] PASSED [ 16%]2021-01-28 02:20:45,746 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_arctic_fsck.py::test_dont_cleanup_recent_orphaned_snapshots[False-data11-FwPointersCfg.ENABLED] PASSED [ 16%]2021-01-28 02:20:46,705 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_copy_data.py::test_copy_data_no_force PASSED [ 16%]2021-01-28 02:20:47,924 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_copy_data.py::test_copy_data_force PASSED [ 16%]2021-01-28 02:20:49,165 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_copy_data.py::test_copy_data_splice PASSED [ 16%]2021-01-28 02:20:50,413 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_copy_data.py::test_copy_data_wild PASSED  [ 16%]2021-01-28 02:20:51,659 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_copy_data.py::test_copy_data_doesnt_exist PASSED [ 16%]2021-01-28 02:20:52,759 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_delete_library.py::test_delete_library PASSED [ 16%]2021-01-28 02:20:54,010 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_delete_library.py::test_delete_library1 PASSED [ 16%]2021-01-28 02:20:55,237 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_delete_library.py::test_delete_library2 PASSED [ 16%]2021-01-28 02:20:56,466 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_delete_library.py::test_delete_library3 PASSED [ 16%]2021-01-28 02:20:57,680 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_delete_library.py::test_delete_library_doesnt_exist PASSED [ 16%]2021-01-28 02:20:58,791 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_enable_sharding.py::test_enable_sharding PASSED [ 16%]2021-01-28 02:20:59,659 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_enable_sharding.py::test_enable_sharding_already_on_db PASSED [ 17%]2021-01-28 02:21:00,534 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_enable_sharding.py::test_enable_sharding_on_db_other_failure PASSED [ 17%]
tests/integration/scripts/test_initialize_library.py::test_init_library PASSED [ 17%]2021-01-28 02:21:02,298 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_initialize_library.py::test_init_library_no_arctic_prefix PASSED [ 17%]2021-01-28 02:21:03,197 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_initialize_library.py::test_init_library_quota PASSED [ 17%]2021-01-28 02:21:04,082 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_initialize_library.py::test_init_library_bad_library PASSED [ 17%]2021-01-28 02:21:04,724 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_list_libraries.py::test_list_library PASSED [ 17%]2021-01-28 02:21:05,613 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_list_libraries.py::test_list_library_args PASSED [ 17%]2021-01-28 02:21:06,482 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_list_libraries.py::test_list_library_args_not_found PASSED [ 17%]2021-01-28 02:21:07,359 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_prune_versions.py::test_prune_versions_symbol PASSED [ 17%]2021-01-28 02:21:08,229 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_prune_versions.py::test_prune_versions_full PASSED [ 17%]2021-01-28 02:21:09,183 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_prune_versions.py::test_keep_recent_snapshots PASSED [ 17%]2021-01-28 02:21:10,069 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_prune_versions.py::test_fix_broken_snapshot_references PASSED [ 17%]2021-01-28 02:21:10,979 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_prune_versions.py::test_keep_only_one_version PASSED [ 17%]2021-01-28 02:21:11,879 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_bitemporal_store.py::test_new_ts_read_write PASSED [ 18%]2021-01-28 02:21:12,782 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_bitemporal_store.py::test_read_ts_raw PASSED [ 18%]2021-01-28 02:21:13,713 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_bitemporal_store.py::test_write_ts_with_column_name_same_as_observed_dt_ok PASSED [ 18%]2021-01-28 02:21:14,633 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_bitemporal_store.py::test_last_update PASSED [ 18%]2021-01-28 02:21:15,563 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_bitemporal_store.py::test_existing_ts_update_and_read PASSED [ 18%]2021-01-28 02:21:16,496 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_bitemporal_store.py::test_existing_ts_update_existing_data_and_read PASSED [ 18%]2021-01-28 02:21:17,452 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_bitemporal_store.py::test_read_ts_with_historical_update PASSED [ 18%]2021-01-28 02:21:18,464 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_bitemporal_store.py::test_read_ts_with_historical_update_and_new_row PASSED [ 18%]2021-01-28 02:21:19,431 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_bitemporal_store.py::test_insert_new_rows_in_middle_remains_sorted PASSED [ 18%]2021-01-28 02:21:20,387 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_bitemporal_store.py::test_insert_versions_inbetween_works_ok PASSED [ 18%]2021-01-28 02:21:21,375 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_bitemporal_store.py::test_read_ts_raw_all_version_ok PASSED [ 18%]2021-01-28 02:21:22,399 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_bitemporal_store.py::test_bitemporal_store_saves_as_of_with_timezone PASSED [ 18%]2021-01-28 02:21:23,309 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_bitemporal_store.py::test_bitemporal_store_read_as_of_timezone PASSED [ 18%]2021-01-28 02:21:24,256 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_bitemporal_store.py::test_multi_index_ts_read_write PASSED [ 19%]2021-01-28 02:21:25,173 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_bitemporal_store.py::test_multi_index_ts_read_raw PASSED [ 19%]2021-01-28 02:21:26,099 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_bitemporal_store.py::test_multi_index_update PASSED [ 19%]2021-01-28 02:21:27,071 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_metadata_store.py::test_pickle PASSED       [ 19%]2021-01-28 02:21:27,834 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_metadata_store.py::test_has_symbol PASSED   [ 19%]2021-01-28 02:21:28,592 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_metadata_store.py::test_list_symbols PASSED [ 19%]2021-01-28 02:21:29,346 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_metadata_store.py::test_read_history PASSED [ 19%]2021-01-28 02:21:30,115 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_metadata_store.py::test_read PASSED         [ 19%]2021-01-28 02:21:30,875 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_metadata_store.py::test_write_history PASSED [ 19%]2021-01-28 02:21:31,647 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_metadata_store.py::test_append PASSED       [ 19%]2021-01-28 02:21:32,420 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_metadata_store.py::test_prepend PASSED      [ 19%]2021-01-28 02:21:33,193 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_metadata_store.py::test_pop PASSED          [ 19%]2021-01-28 02:21:33,960 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_metadata_store.py::test_purge PASSED        [ 19%]2021-01-28 02:21:34,724 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_ndarray_store.py::test_write_new_column_name_to_arctic_1_40_data PASSED [ 20%]2021-01-28 02:21:35,833 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_ndarray_store.py::test_save_read_simple_ndarray PASSED [ 20%]2021-01-28 02:21:36,725 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_ndarray_store.py::test_read_simple_ndarray_from_secondary XFAIL [ 20%]
tests/integration/store/test_ndarray_store.py::test_save_read_big_1darray[FwPointersCfg.DISABLED] PASSED [ 20%]2021-01-28 02:21:42,717 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_ndarray_store.py::test_save_read_big_1darray[FwPointersCfg.HYBRID] PASSED [ 20%]2021-01-28 02:21:47,759 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_ndarray_store.py::test_save_read_big_1darray[FwPointersCfg.ENABLED] PASSED [ 20%]2021-01-28 02:21:52,749 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_ndarray_store.py::test_save_and_resave_reuses_chunks[FwPointersCfg.DISABLED] PASSED [ 20%]2021-01-28 02:21:53,677 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_ndarray_store.py::test_save_and_resave_reuses_chunks[FwPointersCfg.HYBRID] PASSED [ 20%]2021-01-28 02:21:54,594 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_ndarray_store.py::test_save_and_resave_reuses_chunks[FwPointersCfg.ENABLED] PASSED [ 20%]2021-01-28 02:21:55,510 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_ndarray_store.py::test_save_read_big_2darray[FwPointersCfg.DISABLED] PASSED [ 20%]2021-01-28 02:22:00,561 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_ndarray_store.py::test_save_read_big_2darray[FwPointersCfg.HYBRID] PASSED [ 20%]2021-01-28 02:22:05,549 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_ndarray_store.py::test_save_read_big_2darray[FwPointersCfg.ENABLED] PASSED [ 20%]2021-01-28 02:22:10,541 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_ndarray_store.py::test_get_info_bson_object PASSED [ 20%]2021-01-28 02:22:11,449 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_ndarray_store.py::test_save_read_ndarray_with_array_field PASSED [ 20%]2021-01-28 02:22:12,348 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_ndarray_store.py::test_save_read_ndarray PASSED [ 21%]2021-01-28 02:22:13,247 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_ndarray_store.py::test_multiple_write[FwPointersCfg.DISABLED] PASSED [ 21%]2021-01-28 02:22:14,172 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_ndarray_store.py::test_multiple_write[FwPointersCfg.HYBRID] PASSED [ 21%]2021-01-28 02:22:15,108 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_ndarray_store.py::test_multiple_write[FwPointersCfg.ENABLED] PASSED [ 21%]2021-01-28 02:22:16,030 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_ndarray_store.py::test_cant_write_objects PASSED [ 21%]
tests/integration/store/test_ndarray_store.py::test_save_read_large_ndarray PASSED [ 21%]2021-01-28 02:22:17,331 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_ndarray_store.py::test_mutable_ndarray PASSED [ 21%]2021-01-28 02:22:18,216 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_ndarray_store.py::test_delete_version_shouldnt_break_read XPASS [ 21%]2021-01-28 02:22:19,124 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_ndarray_store_append.py::test_append_simple_ndarray[FwPointersCfg.DISABLED] PASSED [ 21%]2021-01-28 02:22:20,026 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_ndarray_store_append.py::test_append_simple_ndarray[FwPointersCfg.HYBRID] PASSED [ 21%]2021-01-28 02:22:20,930 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_ndarray_store_append.py::test_append_simple_ndarray[FwPointersCfg.ENABLED] PASSED [ 21%]2021-01-28 02:22:21,825 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_ndarray_store_append.py::test_append_simple_ndarray_promoting_types[FwPointersCfg.DISABLED] PASSED [ 21%]2021-01-28 02:22:22,726 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_ndarray_store_append.py::test_append_simple_ndarray_promoting_types[FwPointersCfg.HYBRID] PASSED [ 21%]2021-01-28 02:22:23,647 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_ndarray_store_append.py::test_append_simple_ndarray_promoting_types[FwPointersCfg.ENABLED] PASSED [ 22%]2021-01-28 02:22:24,550 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_ndarray_store_append.py::test_promote_types PASSED [ 22%]2021-01-28 02:22:25,443 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_ndarray_store_append.py::test_promote_types2 PASSED [ 22%]2021-01-28 02:22:26,334 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_ndarray_store_append.py::test_promote_types_smaller_sizes PASSED [ 22%]2021-01-28 02:22:27,227 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_ndarray_store_append.py::test_promote_types_larger_sizes PASSED [ 22%]2021-01-28 02:22:28,134 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_ndarray_store_append.py::test_promote_field_types_smaller_sizes PASSED [ 22%]2021-01-28 02:22:29,057 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_ndarray_store_append.py::test_promote_field_types_larger_sizes PASSED [ 22%]2021-01-28 02:22:29,955 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_ndarray_store_append.py::test_append_ndarray_with_field_shape[FwPointersCfg.DISABLED] PASSED [ 22%]2021-01-28 02:22:30,843 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_ndarray_store_append.py::test_append_ndarray_with_field_shape[FwPointersCfg.HYBRID] PASSED [ 22%]2021-01-28 02:22:31,736 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_ndarray_store_append.py::test_append_ndarray_with_field_shape[FwPointersCfg.ENABLED] PASSED [ 22%]2021-01-28 02:22:32,629 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_ndarray_store_append.py::test_append_read_large_ndarray[FwPointersCfg.DISABLED] PASSED [ 22%]2021-01-28 02:22:35,317 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_ndarray_store_append.py::test_append_read_large_ndarray[FwPointersCfg.HYBRID] PASSED [ 22%]2021-01-28 02:22:38,055 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_ndarray_store_append.py::test_append_read_large_ndarray[FwPointersCfg.ENABLED] PASSED [ 22%]2021-01-28 02:22:40,694 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_ndarray_store_append.py::test_save_append_read_ndarray[FwPointersCfg.DISABLED] PASSED [ 23%]2021-01-28 02:22:42,122 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_ndarray_store_append.py::test_save_append_read_ndarray[FwPointersCfg.HYBRID] PASSED [ 23%]2021-01-28 02:22:43,550 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_ndarray_store_append.py::test_save_append_read_ndarray[FwPointersCfg.ENABLED] PASSED [ 23%]2021-01-28 02:22:44,957 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_ndarray_store_append.py::test_save_append_read_1row_ndarray PASSED [ 23%]2021-01-28 02:22:46,365 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_ndarray_store_append.py::test_append_too_large_ndarray PASSED [ 23%]2021-01-28 02:22:48,113 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_ndarray_store_append.py::test_empty_field_append_keeps_all_columns PASSED [ 23%]2021-01-28 02:22:49,002 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_ndarray_store_append.py::test_empty_append_promotes_dtype[FwPointersCfg.DISABLED] PASSED [ 23%]2021-01-28 02:22:49,891 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_ndarray_store_append.py::test_empty_append_promotes_dtype[FwPointersCfg.HYBRID] PASSED [ 23%]2021-01-28 02:22:50,788 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_ndarray_store_append.py::test_empty_append_promotes_dtype[FwPointersCfg.ENABLED] PASSED [ 23%]2021-01-28 02:22:51,672 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_ndarray_store_append.py::test_empty_append_promotes_dtype2 PASSED [ 23%]2021-01-28 02:22:52,566 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_ndarray_store_append.py::test_empty_append_promotes_dtype3 PASSED [ 23%]2021-01-28 02:22:53,470 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_ndarray_store_append.py::test_convert_to_structured_array PASSED [ 23%]2021-01-28 02:22:54,352 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_ndarray_store_append.py::test_empty_append_concat_and_rewrite[FwPointersCfg.DISABLED] PASSED [ 23%]2021-01-28 02:22:55,311 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_ndarray_store_append.py::test_empty_append_concat_and_rewrite[FwPointersCfg.HYBRID] PASSED [ 23%]2021-01-28 02:22:56,264 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_ndarray_store_append.py::test_empty_append_concat_and_rewrite[FwPointersCfg.ENABLED] PASSED [ 24%]2021-01-28 02:22:57,209 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_ndarray_store_append.py::test_empty_append_concat_and_rewrite_2[FwPointersCfg.DISABLED] PASSED [ 24%]2021-01-28 02:22:58,373 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_ndarray_store_append.py::test_empty_append_concat_and_rewrite_2[FwPointersCfg.HYBRID] PASSED [ 24%]2021-01-28 02:22:59,547 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_ndarray_store_append.py::test_empty_append_concat_and_rewrite_2[FwPointersCfg.ENABLED] PASSED [ 24%]2021-01-28 02:23:00,763 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_ndarray_store_append.py::test_empty_append_concat_and_rewrite_3[FwPointersCfg.DISABLED] PASSED [ 24%]2021-01-28 02:23:01,778 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_ndarray_store_append.py::test_empty_append_concat_and_rewrite_3[FwPointersCfg.HYBRID] PASSED [ 24%]2021-01-28 02:23:02,779 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_ndarray_store_append.py::test_empty_append_concat_and_rewrite_3[FwPointersCfg.ENABLED] PASSED [ 24%]2021-01-28 02:23:03,782 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_ndarray_store_append.py::test_append_with_extra_columns PASSED [ 24%]2021-01-28 02:23:04,735 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_ndarray_store_append.py::test_save_append_delete_append[FwPointersCfg.DISABLED] PASSED [ 24%]2021-01-28 02:23:05,699 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_ndarray_store_append.py::test_save_append_delete_append[FwPointersCfg.HYBRID] PASSED [ 24%]2021-01-28 02:23:06,656 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_ndarray_store_append.py::test_save_append_delete_append[FwPointersCfg.ENABLED] PASSED [ 24%]2021-01-28 02:23:07,629 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_ndarray_store_append.py::test_append_after_failed_append[FwPointersCfg.DISABLED] PASSED [ 24%]2021-01-28 02:23:08,594 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_ndarray_store_append.py::test_append_after_failed_append[FwPointersCfg.HYBRID] PASSED [ 24%]2021-01-28 02:23:09,551 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_ndarray_store_append.py::test_append_after_failed_append[FwPointersCfg.ENABLED] PASSED [ 25%]2021-01-28 02:23:10,499 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_ndarray_store_append.py::test_append_reorder_columns PASSED [ 25%]2021-01-28 02:23:11,405 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_write_multi_column_to_arctic_1_40_data PASSED [ 25%]2021-01-28 02:23:12,319 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_save_read_pandas_series PASSED [ 25%]2021-01-28 02:23:13,223 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_save_read_pandas_series_maintains_name PASSED [ 25%]2021-01-28 02:23:14,132 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_save_read_pandas_series_with_multiindex PASSED [ 25%]2021-01-28 02:23:15,035 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_save_read_pandas_series_with_multiindex_and_name PASSED [ 25%]2021-01-28 02:23:15,925 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_save_read_pandas_series_with_unicode_index_name PASSED [ 25%]2021-01-28 02:23:16,819 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_save_read_pandas_dataframe_with_multiindex PASSED [ 25%]2021-01-28 02:23:17,717 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_save_read_pandas_dataframe_with_none_values PASSED [ 25%]2021-01-28 02:23:18,616 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_save_read_pandas_dataframe_with_unicode_index_name PASSED [ 25%]2021-01-28 02:23:19,510 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_cant_write_pandas_series_with_tuple_values PASSED [ 25%]2021-01-28 02:23:20,386 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_save_read_pandas_series_with_datetimeindex_with_timezone PASSED [ 25%]2021-01-28 02:23:21,288 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_save_read_pandas_series_with_datetimeindex PASSED [ 25%]2021-01-28 02:23:22,181 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_save_read_pandas_dataframe_with_datetimeindex_with_timezone PASSED [ 26%]2021-01-28 02:23:23,086 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_save_read_pandas_empty_series_with_datetime_multiindex_with_timezone PASSED [ 26%]2021-01-28 02:23:23,983 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_save_read_pandas_dataframe_with_datetimeindex PASSED [ 26%]2021-01-28 02:23:24,882 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_save_read_pandas_dataframe_with_strings PASSED [ 26%]2021-01-28 02:23:25,790 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_save_read_pandas_dataframe PASSED [ 26%]2021-01-28 02:23:26,692 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_save_read_empty_dataframe PASSED [ 26%]2021-01-28 02:23:27,586 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_save_read_pandas_dataframe2 PASSED [ 26%]2021-01-28 02:23:28,484 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_save_read_pandas_dataframe_strings PASSED [ 26%]2021-01-28 02:23:29,378 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_save_read_pandas_dataframe_empty_multiindex PASSED [ 26%]2021-01-28 02:23:30,298 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_save_read_pandas_dataframe_empty_multiindex_and_no_columns PASSED [ 26%]2021-01-28 02:23:31,205 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_save_read_pandas_dataframe_multiindex_and_no_columns PASSED [ 26%]2021-01-28 02:23:32,134 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_append_pandas_multi_columns_dataframe PASSED [ 26%]2021-01-28 02:23:33,066 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_append_pandas_multi_columns_dataframe_new_column PASSED [ 26%]2021-01-28 02:23:33,997 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_save_read_pandas_multi_columns_empty_dataframe PASSED [ 27%]2021-01-28 02:23:34,915 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_save_read_pandas_multi_columns_dataframe PASSED [ 27%]2021-01-28 02:23:35,819 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_save_read_pandas_multi_columns_no_names_dataframe PASSED [ 27%]2021-01-28 02:23:36,720 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_save_read_pandas_multi_columns_dataframe_with_int_levels PASSED [ 27%]2021-01-28 02:23:37,635 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_save_read_multi_index_and_multi_columns_dataframe PASSED [ 27%]2021-01-28 02:23:38,556 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_append_pandas_dataframe PASSED [ 27%]2021-01-28 02:23:39,464 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_empty_dataframe_multindex PASSED [ 27%]2021-01-28 02:23:40,358 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_dataframe_append_empty PASSED [ 27%]2021-01-28 02:23:41,259 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_empy_dataframe_append PASSED [ 27%]2021-01-28 02:23:42,173 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_dataframe_append_empty_multiindex PASSED [ 27%]2021-01-28 02:23:43,091 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_empty_dataframe_append_multiindex PASSED [ 27%]2021-01-28 02:23:44,022 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_empty_dataframe_should_ignore_dtype PASSED [ 27%]2021-01-28 02:23:44,940 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_empty_dataframe_should_ignore_dtype2 PASSED [ 27%]2021-01-28 02:23:45,856 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_dataframe_append_should_promote_string_column PASSED [ 28%]2021-01-28 02:23:46,769 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_dataframe_append_should_add_new_column PASSED [ 28%]2021-01-28 02:23:47,676 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_dataframe_append_should_add_new_columns_and_reorder PASSED [ 28%]2021-01-28 02:23:48,591 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_dataframe_save_read[df_size0] PASSED [ 28%]2021-01-28 02:23:49,488 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_dataframe_save_read[df_size1] PASSED [ 28%]2021-01-28 02:23:50,386 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_dataframe_save_read[df_size2] PASSED [ 28%]2021-01-28 02:23:51,276 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_dataframe_save_read[df_size3] PASSED [ 28%]2021-01-28 02:23:52,167 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_dataframe_save_read[df_size4] PASSED [ 28%]2021-01-28 02:23:53,074 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_dataframe_save_read[df_size5] PASSED [ 28%]2021-01-28 02:23:53,977 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_dataframe_save_read[df_size6] PASSED [ 28%]2021-01-28 02:23:54,874 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_dataframe_save_read[df_size7] PASSED [ 28%]2021-01-28 02:23:55,786 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_dataframe_save_read[df_size8] PASSED [ 28%]2021-01-28 02:23:56,681 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_dataframe_save_read[df_size9] PASSED [ 28%]2021-01-28 02:23:57,575 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_dataframe_save_read[df_size10] PASSED [ 28%]2021-01-28 02:23:58,465 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_dataframe_save_read[df_size11] PASSED [ 29%]2021-01-28 02:23:59,360 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_dataframe_save_read[df_size12] PASSED [ 29%]2021-01-28 02:24:00,262 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_dataframe_save_read[df_size13] PASSED [ 29%]2021-01-28 02:24:01,159 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_dataframe_save_read[df_size14] PASSED [ 29%]2021-01-28 02:24:02,072 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_dataframe_save_read[df_size15] PASSED [ 29%]2021-01-28 02:24:02,970 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_dataframe_save_read[df_size16] PASSED [ 29%]2021-01-28 02:24:03,872 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_dataframe_save_read[df_size17] PASSED [ 29%]2021-01-28 02:24:04,768 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_dataframe_save_read[df_size18] PASSED [ 29%]2021-01-28 02:24:05,672 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_dataframe_save_read[df_size19] PASSED [ 29%]2021-01-28 02:24:06,581 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_dataframe_save_append_read[df_size0] PASSED [ 29%]2021-01-28 02:24:07,473 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_dataframe_save_append_read[df_size1] PASSED [ 29%]2021-01-28 02:24:08,357 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_dataframe_save_append_read[df_size2] PASSED [ 29%]2021-01-28 02:24:09,254 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_dataframe_save_append_read[df_size3] PASSED [ 29%]2021-01-28 02:24:10,164 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_dataframe_save_append_read[df_size4] PASSED [ 30%]2021-01-28 02:24:11,069 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_dataframe_save_append_read[df_size5] PASSED [ 30%]2021-01-28 02:24:11,975 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_dataframe_save_append_read[df_size6] PASSED [ 30%]2021-01-28 02:24:12,886 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_dataframe_save_append_read[df_size7] PASSED [ 30%]2021-01-28 02:24:13,803 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_dataframe_save_append_read[df_size8] PASSED [ 30%]2021-01-28 02:24:14,710 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_dataframe_save_append_read[df_size9] PASSED [ 30%]2021-01-28 02:24:15,616 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_dataframe_save_append_read[df_size10] PASSED [ 30%]2021-01-28 02:24:16,525 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_dataframe_save_append_read[df_size11] PASSED [ 30%]2021-01-28 02:24:17,431 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_dataframe_save_append_read[df_size12] PASSED [ 30%]2021-01-28 02:24:18,332 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_dataframe_save_append_read[df_size13] PASSED [ 30%]2021-01-28 02:24:19,247 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_dataframe_save_append_read[df_size14] PASSED [ 30%]2021-01-28 02:24:20,180 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_dataframe_save_append_read[df_size15] PASSED [ 30%]2021-01-28 02:24:21,092 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_dataframe_save_append_read[df_size16] PASSED [ 30%]2021-01-28 02:24:21,998 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_dataframe_save_append_read[df_size17] PASSED [ 30%]2021-01-28 02:24:22,909 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_dataframe_save_append_read[df_size18] PASSED [ 31%]2021-01-28 02:24:23,821 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_dataframe_save_append_read[df_size19] PASSED [ 31%]2021-01-28 02:24:24,725 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_large_dataframe_append_rewrite_same_item PASSED [ 31%]2021-01-28 02:24:26,209 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_large_dataframe_rewrite_same_item PASSED [ 31%]2021-01-28 02:24:28,804 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_append_after_truncate_after_append PASSED [ 31%]2021-01-28 02:24:29,767 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_can_write_pandas_df_with_object_columns PASSED [ 31%]2021-01-28 02:24:30,682 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_panel_save_read[df_size0] SKIPPED [ 31%]
tests/integration/store/test_pandas_store.py::test_panel_save_read[df_size1] SKIPPED [ 31%]
tests/integration/store/test_pandas_store.py::test_panel_save_read[df_size2] SKIPPED [ 31%]
tests/integration/store/test_pandas_store.py::test_panel_save_read[df_size3] SKIPPED [ 31%]
tests/integration/store/test_pandas_store.py::test_panel_save_read[df_size4] SKIPPED [ 31%]
tests/integration/store/test_pandas_store.py::test_panel_save_read[df_size5] SKIPPED [ 31%]
tests/integration/store/test_pandas_store.py::test_panel_save_read[df_size6] SKIPPED [ 31%]
tests/integration/store/test_pandas_store.py::test_panel_save_read[df_size7] SKIPPED [ 32%]
tests/integration/store/test_pandas_store.py::test_panel_save_read[df_size8] SKIPPED [ 32%]
tests/integration/store/test_pandas_store.py::test_panel_save_read[df_size9] SKIPPED [ 32%]
tests/integration/store/test_pandas_store.py::test_panel_save_read_with_nans SKIPPED [ 32%]
tests/integration/store/test_pandas_store.py::test_save_read_ints PASSED [ 32%]2021-01-28 02:24:31,614 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_save_read_datetimes PASSED [ 32%]2021-01-28 02:24:32,526 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_labels PASSED         [ 32%]2021-01-28 02:24:33,431 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_duplicate_labels PASSED [ 32%]2021-01-28 02:24:34,350 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_no_labels PASSED      [ 32%]2021-01-28 02:24:35,274 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_no_index_labels XFAIL [ 32%]
tests/integration/store/test_pandas_store.py::test_not_unique PASSED     [ 32%]2021-01-28 02:24:37,163 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_daterange_end PASSED  [ 32%]2021-01-28 02:24:38,510 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_daterange_start PASSED [ 32%]2021-01-28 02:24:39,856 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_daterange_with_zero_index PASSED [ 33%]2021-01-28 02:24:40,791 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_daterange_large_DataFrame PASSED [ 33%]2021-01-28 02:24:42,349 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_daterange_large_DataFrame_middle PASSED [ 33%]2021-01-28 02:24:48,692 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_daterange[df0-assert_frame_equal] PASSED [ 33%]2021-01-28 02:24:49,760 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_daterange[df1-assert_series_equal] PASSED [ 33%]2021-01-28 02:24:50,780 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_daterange_append PASSED [ 33%]2021-01-28 02:24:52,715 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_daterange_single_chunk PASSED [ 33%]2021-01-28 02:24:53,644 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_daterange_when_end_beyond_chunk_index PASSED [ 33%]2021-01-28 02:24:54,566 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_daterange_when_end_beyond_chunk_index_no_start PASSED [ 33%]2021-01-28 02:24:55,487 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_daterange_fails_with_timezone_start PASSED [ 33%]2021-01-28 02:24:56,393 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_data_info_series PASSED [ 33%]2021-01-28 02:24:57,293 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_data_info_df PASSED   [ 33%]2021-01-28 02:24:58,183 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_data_info_cols PASSED [ 33%]2021-01-28 02:24:59,092 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_read_write_multiindex_store_keeps_timezone PASSED [ 33%]2021-01-28 02:25:00,033 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_mutable_df PASSED     [ 34%]2021-01-28 02:25:00,943 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_forced_encodings_with_df_mixed_types SKIPPED [ 34%]
tests/integration/store/test_pandas_store.py::test_forced_encodings_with_df SKIPPED [ 34%]
tests/integration/store/test_pandas_store.py::test_forced_encodings_with_df_py3 PASSED [ 34%]2021-01-28 02:25:01,889 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_forced_encodings_with_df_py3_multi_index PASSED [ 34%]2021-01-28 02:25:02,841 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pickle_store.py::test_save_read_bson PASSED [ 34%]2021-01-28 02:25:03,739 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pickle_store.py::test_save_read_big_encodable PASSED [ 34%]2021-01-28 02:25:04,773 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pickle_store.py::test_save_read_bson_object PASSED [ 34%]2021-01-28 02:25:05,665 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pickle_store.py::test_get_info_bson_object PASSED [ 34%]2021-01-28 02:25:06,555 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pickle_store.py::test_bson_large_object PASSED [ 34%]2021-01-28 02:25:07,800 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pickle_store.py::test_bson_leak_objects_delete PASSED [ 34%]2021-01-28 02:25:08,706 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pickle_store.py::test_bson_leak_objects_prune_previous PASSED [ 34%]2021-01-28 02:25:09,617 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pickle_store.py::test_prune_previous_doesnt_kill_other_objects PASSED [ 34%]2021-01-28 02:25:10,518 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pickle_store.py::test_write_metadata PASSED [ 35%]2021-01-28 02:25:11,415 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_store_item_new_version PASSED [ 35%]2021-01-28 02:25:12,308 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_store_item_read_preference 2021-01-28 02:25:13,375 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
XFAIL [ 35%]
tests/integration/store/test_version_store.py::test_read_item_read_preference_SECONDARY XFAIL [ 35%]
tests/integration/store/test_version_store.py::test_store_item_metadata[FwPointersCfg.DISABLED] PASSED [ 35%]2021-01-28 02:25:15,339 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_store_item_metadata[FwPointersCfg.HYBRID] PASSED [ 35%]2021-01-28 02:25:16,234 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_store_item_metadata[FwPointersCfg.ENABLED] PASSED [ 35%]2021-01-28 02:25:17,124 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_read_metadata[FwPointersCfg.DISABLED] PASSED [ 35%]2021-01-28 02:25:18,011 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_read_metadata[FwPointersCfg.HYBRID] PASSED [ 35%]2021-01-28 02:25:18,896 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_read_metadata[FwPointersCfg.ENABLED] PASSED [ 35%]2021-01-28 02:25:19,802 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_read_metadata_newer_version_with_lower_id[FwPointersCfg.DISABLED] PASSED [ 35%]2021-01-28 02:25:20,696 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_read_metadata_newer_version_with_lower_id[FwPointersCfg.HYBRID] PASSED [ 35%]2021-01-28 02:25:21,605 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_read_metadata_newer_version_with_lower_id[FwPointersCfg.ENABLED] PASSED [ 35%]2021-01-28 02:25:22,511 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_read_metadata_throws_on_deleted_symbol[FwPointersCfg.DISABLED] PASSED [ 35%]2021-01-28 02:25:23,417 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_read_metadata_throws_on_deleted_symbol[FwPointersCfg.HYBRID] PASSED [ 36%]2021-01-28 02:25:24,319 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_read_metadata_throws_on_deleted_symbol[FwPointersCfg.ENABLED] PASSED [ 36%]2021-01-28 02:25:25,221 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_store_item_and_update[FwPointersCfg.DISABLED] PASSED [ 36%]2021-01-28 02:25:29,195 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_store_item_and_update[FwPointersCfg.HYBRID] PASSED [ 36%]2021-01-28 02:25:33,178 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_store_item_and_update[FwPointersCfg.ENABLED] PASSED [ 36%]2021-01-28 02:25:37,160 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_append_update[FwPointersCfg.DISABLED] PASSED [ 36%]2021-01-28 02:25:38,223 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_append_update[FwPointersCfg.HYBRID] PASSED [ 36%]2021-01-28 02:25:39,270 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_append_update[FwPointersCfg.ENABLED] PASSED [ 36%]2021-01-28 02:25:40,313 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_append[FwPointersCfg.DISABLED] PASSED [ 36%]2021-01-28 02:25:41,244 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_append[FwPointersCfg.HYBRID] PASSED [ 36%]2021-01-28 02:25:42,181 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_append[FwPointersCfg.ENABLED] PASSED [ 36%]2021-01-28 02:25:43,088 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_append_should_overwrite_after_delete[FwPointersCfg.DISABLED] PASSED [ 36%]2021-01-28 02:25:44,040 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_append_should_overwrite_after_delete[FwPointersCfg.HYBRID] PASSED [ 36%]2021-01-28 02:25:44,969 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_append_should_overwrite_after_delete[FwPointersCfg.ENABLED] PASSED [ 37%]2021-01-28 02:25:45,897 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_append_empty_ts[FwPointersCfg.DISABLED] PASSED [ 37%]2021-01-28 02:25:46,788 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_append_empty_ts[FwPointersCfg.HYBRID] PASSED [ 37%]2021-01-28 02:25:47,685 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_append_empty_ts[FwPointersCfg.ENABLED] PASSED [ 37%]2021-01-28 02:25:48,581 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_append_corrupted_new_version[FwPointersCfg.DISABLED] PASSED [ 37%]2021-01-28 02:25:49,514 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_append_corrupted_new_version[FwPointersCfg.HYBRID] PASSED [ 37%]2021-01-28 02:25:50,445 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_append_corrupted_new_version[FwPointersCfg.ENABLED] PASSED [ 37%]2021-01-28 02:25:51,365 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_query_version_as_of_int PASSED [ 37%]2021-01-28 02:25:52,269 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_list_version[FwPointersCfg.DISABLED] PASSED [ 37%]2021-01-28 02:25:53,191 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_list_version[FwPointersCfg.HYBRID] PASSED [ 37%]2021-01-28 02:25:54,109 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_list_version[FwPointersCfg.ENABLED] PASSED [ 37%]2021-01-28 02:25:55,025 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_list_version_deleted PASSED [ 37%]2021-01-28 02:25:55,939 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_list_version_latest_only PASSED [ 37%]2021-01-28 02:25:56,863 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_list_version_snapshot PASSED [ 38%]2021-01-28 02:25:57,807 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_delete_versions[FwPointersCfg.DISABLED] PASSED [ 38%]2021-01-28 02:25:58,758 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_delete_versions[FwPointersCfg.HYBRID] PASSED [ 38%]2021-01-28 02:25:59,704 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_delete_versions[FwPointersCfg.ENABLED] PASSED [ 38%]2021-01-28 02:26:00,650 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_delete_bson_versions[FwPointersCfg.DISABLED] PASSED [ 38%]2021-01-28 02:26:01,565 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_delete_bson_versions[FwPointersCfg.HYBRID] PASSED [ 38%]2021-01-28 02:26:02,478 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_delete_bson_versions[FwPointersCfg.ENABLED] PASSED [ 38%]2021-01-28 02:26:03,396 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_read_none_does_not_exception[FwPointersCfg.DISABLED] PASSED [ 38%]2021-01-28 02:26:04,278 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_read_none_does_not_exception[FwPointersCfg.HYBRID] PASSED [ 38%]2021-01-28 02:26:05,167 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_read_none_does_not_exception[FwPointersCfg.ENABLED] PASSED [ 38%]2021-01-28 02:26:06,052 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_delete_item_has_symbol[FwPointersCfg.DISABLED] PASSED [ 38%]2021-01-28 02:26:06,977 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_delete_item_has_symbol[FwPointersCfg.HYBRID] PASSED [ 38%]2021-01-28 02:26:07,927 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_delete_item_has_symbol[FwPointersCfg.ENABLED] PASSED [ 38%]2021-01-28 02:26:08,854 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_delete_item_snapshot[FwPointersCfg.DISABLED] PASSED [ 38%]2021-01-28 02:26:09,803 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_delete_item_snapshot[FwPointersCfg.HYBRID] PASSED [ 39%]2021-01-28 02:26:10,761 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_delete_item_snapshot[FwPointersCfg.ENABLED] PASSED [ 39%]2021-01-28 02:26:11,722 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_has_symbol PASSED    [ 39%]2021-01-28 02:26:12,602 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_snapshot[FwPointersCfg.DISABLED] PASSED [ 39%]2021-01-28 02:26:13,563 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_snapshot[FwPointersCfg.HYBRID] PASSED [ 39%]2021-01-28 02:26:14,519 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_snapshot[FwPointersCfg.ENABLED] PASSED [ 39%]2021-01-28 02:26:15,478 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_snapshot_with_versions[FwPointersCfg.DISABLED] PASSED [ 39%]2021-01-28 02:26:16,410 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_snapshot_with_versions[FwPointersCfg.HYBRID] PASSED [ 39%]2021-01-28 02:26:17,348 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_snapshot_with_versions[FwPointersCfg.ENABLED] PASSED [ 39%]2021-01-28 02:26:18,294 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_snapshot_exclusion[FwPointersCfg.DISABLED] PASSED [ 39%]2021-01-28 02:26:19,178 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_snapshot_exclusion[FwPointersCfg.HYBRID] PASSED [ 39%]2021-01-28 02:26:20,082 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_snapshot_exclusion[FwPointersCfg.ENABLED] PASSED [ 39%]2021-01-28 02:26:20,969 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_snapshot_delete[FwPointersCfg.DISABLED] PASSED [ 39%]2021-01-28 02:26:21,898 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_snapshot_delete[FwPointersCfg.HYBRID] PASSED [ 40%]2021-01-28 02:26:22,825 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_snapshot_delete[FwPointersCfg.ENABLED] PASSED [ 40%]2021-01-28 02:26:23,754 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_multiple_snapshots[FwPointersCfg.DISABLED] PASSED [ 40%]2021-01-28 02:26:24,694 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_multiple_snapshots[FwPointersCfg.HYBRID] PASSED [ 40%]2021-01-28 02:26:25,635 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_multiple_snapshots[FwPointersCfg.ENABLED] PASSED [ 40%]2021-01-28 02:26:26,584 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_delete_identical_snapshots PASSED [ 40%]2021-01-28 02:26:27,501 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_list_snapshots PASSED [ 40%]2021-01-28 02:26:28,389 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_duplicate_snapshots PASSED [ 40%]2021-01-28 02:26:29,282 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_prunes_multiple_versions[FwPointersCfg.DISABLED] PASSED [ 40%]2021-01-28 02:26:30,194 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_prunes_multiple_versions[FwPointersCfg.HYBRID] PASSED [ 40%]2021-01-28 02:26:31,096 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_prunes_multiple_versions[FwPointersCfg.ENABLED] PASSED [ 40%]2021-01-28 02:26:32,016 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_prunes_doesnt_prune_snapshots[FwPointersCfg.DISABLED] PASSED [ 40%]2021-01-28 02:26:32,940 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_prunes_doesnt_prune_snapshots[FwPointersCfg.HYBRID] PASSED [ 40%]2021-01-28 02:26:33,848 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_prunes_doesnt_prune_snapshots[FwPointersCfg.ENABLED] PASSED [ 41%]2021-01-28 02:26:34,775 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_prunes_multiple_versions_ts[FwPointersCfg.DISABLED] PASSED [ 41%]2021-01-28 02:26:35,717 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_prunes_multiple_versions_ts[FwPointersCfg.HYBRID] PASSED [ 41%]2021-01-28 02:26:36,663 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_prunes_multiple_versions_ts[FwPointersCfg.ENABLED] PASSED [ 41%]2021-01-28 02:26:37,617 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_prunes_doesnt_prune_snapshots_ts[FwPointersCfg.DISABLED] PASSED [ 41%]2021-01-28 02:26:38,596 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_prunes_doesnt_prune_snapshots_ts[FwPointersCfg.HYBRID] PASSED [ 41%]2021-01-28 02:26:39,588 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_prunes_doesnt_prune_snapshots_ts[FwPointersCfg.ENABLED] PASSED [ 41%]2021-01-28 02:26:40,567 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_prunes_multiple_versions_fully_different_tss[FwPointersCfg.DISABLED] PASSED [ 41%]2021-01-28 02:26:41,531 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_prunes_multiple_versions_fully_different_tss[FwPointersCfg.HYBRID] PASSED [ 41%]2021-01-28 02:26:42,499 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_prunes_multiple_versions_fully_different_tss[FwPointersCfg.ENABLED] PASSED [ 41%]2021-01-28 02:26:43,448 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_prunes_doesnt_prune_snapshots_fully_different_tss[FwPointersCfg.DISABLED] PASSED [ 41%]2021-01-28 02:26:44,456 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_prunes_doesnt_prune_snapshots_fully_different_tss[FwPointersCfg.HYBRID] PASSED [ 41%]2021-01-28 02:26:45,481 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_prunes_doesnt_prune_snapshots_fully_different_tss[FwPointersCfg.ENABLED] PASSED [ 41%]2021-01-28 02:26:46,494 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_prunes_previous_version_append_interaction[FwPointersCfg.DISABLED] PASSED [ 41%]2021-01-28 02:26:47,547 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_prunes_previous_version_append_interaction[FwPointersCfg.HYBRID] PASSED [ 42%]2021-01-28 02:26:48,602 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_prunes_previous_version_append_interaction[FwPointersCfg.ENABLED] PASSED [ 42%]2021-01-28 02:26:49,636 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_list_symbols[FwPointersCfg.DISABLED] PASSED [ 42%]2021-01-28 02:26:50,538 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_list_symbols[FwPointersCfg.HYBRID] PASSED [ 42%]2021-01-28 02:26:51,438 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_list_symbols[FwPointersCfg.ENABLED] PASSED [ 42%]2021-01-28 02:26:52,331 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_list_symbols_regex[FwPointersCfg.DISABLED] PASSED [ 42%]2021-01-28 02:26:53,248 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_list_symbols_regex[FwPointersCfg.HYBRID] PASSED [ 42%]2021-01-28 02:26:54,158 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_list_symbols_regex[FwPointersCfg.ENABLED] PASSED [ 42%]2021-01-28 02:26:55,070 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_list_symbols_newer_version_with_lower_id[FwPointersCfg.DISABLED] PASSED [ 42%]2021-01-28 02:26:55,972 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_list_symbols_newer_version_with_lower_id[FwPointersCfg.HYBRID] PASSED [ 42%]2021-01-28 02:26:56,868 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_list_symbols_newer_version_with_lower_id[FwPointersCfg.ENABLED] PASSED [ 42%]2021-01-28 02:26:57,764 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_list_symbols_write_snapshot_write_delete[FwPointersCfg.DISABLED] PASSED [ 42%]2021-01-28 02:26:58,669 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_list_symbols_write_snapshot_write_delete[FwPointersCfg.HYBRID] PASSED [ 42%]2021-01-28 02:26:59,584 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_list_symbols_write_snapshot_write_delete[FwPointersCfg.ENABLED] PASSED [ 43%]2021-01-28 02:27:00,499 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_list_symbols_delete_write[FwPointersCfg.DISABLED] PASSED [ 43%]2021-01-28 02:27:01,402 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_list_symbols_delete_write[FwPointersCfg.HYBRID] PASSED [ 43%]2021-01-28 02:27:02,301 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_list_symbols_delete_write[FwPointersCfg.ENABLED] PASSED [ 43%]2021-01-28 02:27:03,197 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_date_range_large[FwPointersCfg.DISABLED] PASSED [ 43%]2021-01-28 02:27:04,257 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_date_range_large[FwPointersCfg.HYBRID] PASSED [ 43%]2021-01-28 02:27:05,324 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_date_range_large[FwPointersCfg.ENABLED] PASSED [ 43%]2021-01-28 02:27:06,372 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_append_after_empty[FwPointersCfg.DISABLED] PASSED [ 43%]2021-01-28 02:27:10,809 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_append_after_empty[FwPointersCfg.HYBRID] PASSED [ 43%]2021-01-28 02:27:15,256 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_append_after_empty[FwPointersCfg.ENABLED] PASSED [ 43%]2021-01-28 02:27:19,819 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_write_metadata[FwPointersCfg.DISABLED] PASSED [ 43%]2021-01-28 02:27:20,761 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_write_metadata[FwPointersCfg.HYBRID] PASSED [ 43%]2021-01-28 02:27:21,678 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_write_metadata[FwPointersCfg.ENABLED] PASSED [ 43%]2021-01-28 02:27:22,602 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_write_metadata_followed_by_append[FwPointersCfg.DISABLED] PASSED [ 43%]2021-01-28 02:27:25,525 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_write_metadata_followed_by_append[FwPointersCfg.HYBRID] PASSED [ 44%]2021-01-28 02:27:28,447 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_write_metadata_followed_by_append[FwPointersCfg.ENABLED] PASSED [ 44%]2021-01-28 02:27:31,389 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_write_metadata_new_symbol[FwPointersCfg.DISABLED] PASSED [ 44%]2021-01-28 02:27:32,281 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_write_metadata_new_symbol[FwPointersCfg.HYBRID] PASSED [ 44%]2021-01-28 02:27:33,170 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_write_metadata_new_symbol[FwPointersCfg.ENABLED] PASSED [ 44%]2021-01-28 02:27:34,072 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_write_metadata_after_append[FwPointersCfg.DISABLED] PASSED [ 44%]2021-01-28 02:27:35,006 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_write_metadata_after_append[FwPointersCfg.HYBRID] PASSED [ 44%]2021-01-28 02:27:35,927 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_write_metadata_after_append[FwPointersCfg.ENABLED] PASSED [ 44%]2021-01-28 02:27:36,855 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_write_metadata_purge_previous_versions[FwPointersCfg.DISABLED] PASSED [ 44%]2021-01-28 02:27:39,785 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_write_metadata_purge_previous_versions[FwPointersCfg.HYBRID] PASSED [ 44%]2021-01-28 02:27:42,745 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_write_metadata_purge_previous_versions[FwPointersCfg.ENABLED] PASSED [ 44%]2021-01-28 02:27:45,704 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_write_metadata_delete_symbol[FwPointersCfg.DISABLED] PASSED [ 44%]2021-01-28 02:27:46,642 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_write_metadata_delete_symbol[FwPointersCfg.HYBRID] PASSED [ 44%]2021-01-28 02:27:47,584 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_write_metadata_delete_symbol[FwPointersCfg.ENABLED] PASSED [ 45%]2021-01-28 02:27:48,512 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_write_metadata_snapshots[FwPointersCfg.DISABLED] PASSED [ 45%]2021-01-28 02:27:49,451 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_write_metadata_snapshots[FwPointersCfg.HYBRID] PASSED [ 45%]2021-01-28 02:27:50,387 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_write_metadata_snapshots[FwPointersCfg.ENABLED] PASSED [ 45%]2021-01-28 02:27:51,316 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_restore_version[FwPointersCfg.DISABLED] PASSED [ 45%]2021-01-28 02:27:52,247 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_restore_version[FwPointersCfg.HYBRID] PASSED [ 45%]2021-01-28 02:27:53,205 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_restore_version[FwPointersCfg.ENABLED] PASSED [ 45%]2021-01-28 02:27:54,132 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_restore_version_followed_by_append[FwPointersCfg.DISABLED] PASSED [ 45%]2021-01-28 02:27:57,077 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_restore_version_followed_by_append[FwPointersCfg.HYBRID] PASSED [ 45%]2021-01-28 02:28:00,029 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_restore_version_followed_by_append[FwPointersCfg.ENABLED] PASSED [ 45%]2021-01-28 02:28:02,973 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_restore_version_purging_previous_versions[FwPointersCfg.DISABLED] PASSED [ 45%]2021-01-28 02:28:05,910 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_restore_version_purging_previous_versions[FwPointersCfg.HYBRID] PASSED [ 45%]2021-01-28 02:28:08,852 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_restore_version_purging_previous_versions[FwPointersCfg.ENABLED] PASSED [ 45%]2021-01-28 02:28:11,797 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_restore_version_non_existent_version[FwPointersCfg.DISABLED] PASSED [ 46%]2021-01-28 02:28:12,760 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_restore_version_non_existent_version[FwPointersCfg.HYBRID] PASSED [ 46%]2021-01-28 02:28:13,725 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_restore_version_non_existent_version[FwPointersCfg.ENABLED] PASSED [ 46%]2021-01-28 02:28:14,677 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_restore_version_which_updated_only_metadata[FwPointersCfg.DISABLED] PASSED [ 46%]2021-01-28 02:28:15,661 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_restore_version_which_updated_only_metadata[FwPointersCfg.HYBRID] PASSED [ 46%]2021-01-28 02:28:16,665 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_restore_version_which_updated_only_metadata[FwPointersCfg.ENABLED] PASSED [ 46%]2021-01-28 02:28:17,651 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_restore_version_then_snapshot[FwPointersCfg.DISABLED] PASSED [ 46%]2021-01-28 02:28:18,662 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_restore_version_then_snapshot[FwPointersCfg.HYBRID] PASSED [ 46%]2021-01-28 02:28:19,654 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_restore_version_then_snapshot[FwPointersCfg.ENABLED] PASSED [ 46%]2021-01-28 02:28:20,633 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_restore_version_latest_snapshot_noop[FwPointersCfg.DISABLED] PASSED [ 46%]2021-01-28 02:28:21,549 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_restore_version_latest_snapshot_noop[FwPointersCfg.HYBRID] PASSED [ 46%]2021-01-28 02:28:22,453 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_restore_version_latest_snapshot_noop[FwPointersCfg.ENABLED] PASSED [ 46%]2021-01-28 02:28:23,384 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_restore_version_latest_version_noop[FwPointersCfg.DISABLED] PASSED [ 46%]2021-01-28 02:28:24,290 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_restore_version_latest_version_noop[FwPointersCfg.HYBRID] PASSED [ 46%]2021-01-28 02:28:25,204 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_restore_version_latest_version_noop[FwPointersCfg.ENABLED] PASSED [ 47%]2021-01-28 02:28:26,117 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_restore_version_snap_delete_symbol_restore[FwPointersCfg.DISABLED] PASSED [ 47%]2021-01-28 02:28:27,063 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_restore_version_snap_delete_symbol_restore[FwPointersCfg.HYBRID] PASSED [ 47%]2021-01-28 02:28:28,003 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_restore_version_snap_delete_symbol_restore[FwPointersCfg.ENABLED] PASSED [ 47%]2021-01-28 02:28:28,958 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_restore_from_version_with_deleted_symbol[FwPointersCfg.DISABLED] PASSED [ 47%]2021-01-28 02:28:29,864 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_restore_from_version_with_deleted_symbol[FwPointersCfg.HYBRID] PASSED [ 47%]2021-01-28 02:28:30,766 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_restore_from_version_with_deleted_symbol[FwPointersCfg.ENABLED] PASSED [ 47%]2021-01-28 02:28:31,682 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_prune_previous_versions_retries_on_cleanup_error[FwPointersCfg.DISABLED] PASSED [ 47%]2021-01-28 02:28:32,619 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_prune_previous_versions_retries_on_cleanup_error[FwPointersCfg.HYBRID] PASSED [ 47%]2021-01-28 02:28:33,564 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_prune_previous_versions_retries_on_cleanup_error[FwPointersCfg.ENABLED] PASSED [ 47%]2021-01-28 02:28:34,508 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_prune_previous_versions_retries_find_calls[FwPointersCfg.DISABLED] PASSED [ 47%]2021-01-28 02:28:35,417 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_prune_previous_versions_retries_find_calls[FwPointersCfg.HYBRID] PASSED [ 47%]2021-01-28 02:28:36,320 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_prune_previous_versions_retries_find_calls[FwPointersCfg.ENABLED] PASSED [ 47%]2021-01-28 02:28:37,220 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_append_does_not_duplicate_data_when_prune_fails[FwPointersCfg.DISABLED] PASSED [ 48%]
tests/integration/store/test_version_store.py::test_append_does_not_duplicate_data_when_prune_fails[FwPointersCfg.HYBRID] PASSED [ 48%]
tests/integration/store/test_version_store.py::test_append_does_not_duplicate_data_when_prune_fails[FwPointersCfg.ENABLED] PASSED [ 48%]
tests/integration/store/test_version_store.py::test_write_does_not_succeed_with_a_prune_error[FwPointersCfg.DISABLED] PASSED [ 48%]2021-01-28 02:28:40,957 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_write_does_not_succeed_with_a_prune_error[FwPointersCfg.HYBRID] PASSED [ 48%]2021-01-28 02:28:41,847 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_write_does_not_succeed_with_a_prune_error[FwPointersCfg.ENABLED] PASSED [ 48%]2021-01-28 02:28:42,743 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_prune_keeps_version[FwPointersCfg.DISABLED] PASSED [ 48%]2021-01-28 02:28:43,648 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_prune_keeps_version[FwPointersCfg.HYBRID] PASSED [ 48%]2021-01-28 02:28:44,546 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_prune_keeps_version[FwPointersCfg.ENABLED] PASSED [ 48%]2021-01-28 02:28:45,439 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_empty_string_column_name PASSED [ 48%]2021-01-28 02:28:46,329 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_snapshot_list_versions_after_delete[FwPointersCfg.DISABLED] PASSED [ 48%]2021-01-28 02:28:47,252 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_snapshot_list_versions_after_delete[FwPointersCfg.HYBRID] PASSED [ 48%]2021-01-28 02:28:48,169 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_snapshot_list_versions_after_delete[FwPointersCfg.ENABLED] PASSED [ 48%]2021-01-28 02:28:49,226 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_write_non_serializable_throws PASSED [ 48%]2021-01-28 02:28:50,124 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_write_non_serializable_pickling_default[FwPointersCfg.DISABLED] PASSED [ 49%]2021-01-28 02:28:51,028 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_write_non_serializable_pickling_default[FwPointersCfg.HYBRID] PASSED [ 49%]2021-01-28 02:28:51,928 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_write_non_serializable_pickling_default[FwPointersCfg.ENABLED] PASSED [ 49%]2021-01-28 02:28:52,842 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_write_strict_no_daterange[FwPointersCfg.DISABLED] PASSED [ 49%]2021-01-28 02:28:53,734 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_write_strict_no_daterange[FwPointersCfg.HYBRID] PASSED [ 49%]2021-01-28 02:28:54,618 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_write_strict_no_daterange[FwPointersCfg.ENABLED] PASSED [ 49%]2021-01-28 02:28:55,505 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_handler_check_default_false PASSED [ 49%]2021-01-28 02:28:56,367 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_handler_check_default_osenviron PASSED [ 49%]2021-01-28 02:28:57,231 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_handler_check_set_false PASSED [ 49%]2021-01-28 02:28:58,106 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_handler_check_set_true PASSED [ 49%]2021-01-28 02:28:59,002 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_write_df_with_objects_in_index PASSED [ 49%]2021-01-28 02:28:59,912 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_write_series_with_objects_in_index PASSED [ 49%]2021-01-28 02:29:00,822 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_write_series_with_some_objects[input_series0] PASSED [ 49%]2021-01-28 02:29:01,724 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_write_series_with_some_objects[input_series1] PASSED [ 50%]2021-01-28 02:29:02,614 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_can_write_tz_aware_data_df[FwPointersCfg.DISABLED] PASSED [ 50%]2021-01-28 02:29:03,519 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_can_write_tz_aware_data_df[FwPointersCfg.HYBRID] PASSED [ 50%]2021-01-28 02:29:04,426 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_can_write_tz_aware_data_df[FwPointersCfg.ENABLED] PASSED [ 50%]2021-01-28 02:29:05,333 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_can_write_tz_aware_data_series[FwPointersCfg.DISABLED] PASSED [ 50%]2021-01-28 02:29:06,229 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_can_write_tz_aware_data_series[FwPointersCfg.HYBRID] PASSED [ 50%]2021-01-28 02:29:07,123 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_can_write_tz_aware_data_series[FwPointersCfg.ENABLED] PASSED [ 50%]2021-01-28 02:29:08,021 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_fwpointers_mixed_scenarios[FwPointersCfg.DISABLED-FwPointersCfg.DISABLED-FwPointersCfg.DISABLED-FwPointersCfg.DISABLED] PASSED [ 50%]2021-01-28 02:29:08,988 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_fwpointers_mixed_scenarios[FwPointersCfg.ENABLED-FwPointersCfg.ENABLED-FwPointersCfg.ENABLED-FwPointersCfg.ENABLED] PASSED [ 50%]2021-01-28 02:29:09,954 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_fwpointers_mixed_scenarios[FwPointersCfg.HYBRID-FwPointersCfg.HYBRID-FwPointersCfg.HYBRID-FwPointersCfg.HYBRID] PASSED [ 50%]2021-01-28 02:29:10,935 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_fwpointers_mixed_scenarios[FwPointersCfg.HYBRID-FwPointersCfg.DISABLED-FwPointersCfg.HYBRID-FwPointersCfg.DISABLED] PASSED [ 50%]2021-01-28 02:29:11,895 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_fwpointers_mixed_scenarios[FwPointersCfg.HYBRID-FwPointersCfg.ENABLED-FwPointersCfg.HYBRID-FwPointersCfg.ENABLED] PASSED [ 50%]2021-01-28 02:29:12,862 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_fwpointers_mixed_scenarios[FwPointersCfg.ENABLED-FwPointersCfg.HYBRID-FwPointersCfg.ENABLED-FwPointersCfg.HYBRID] PASSED [ 50%]2021-01-28 02:29:13,840 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_fwpointers_mixed_scenarios[FwPointersCfg.DISABLED-FwPointersCfg.HYBRID-FwPointersCfg.DISABLED-FwPointersCfg.HYBRID] PASSED [ 51%]2021-01-28 02:29:14,806 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_fwpointers_mixed_scenarios[FwPointersCfg.DISABLED-FwPointersCfg.ENABLED-FwPointersCfg.DISABLED-FwPointersCfg.ENABLED] PASSED [ 51%]2021-01-28 02:29:15,776 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_fwpointers_mixed_scenarios[FwPointersCfg.ENABLED-FwPointersCfg.DISABLED-FwPointersCfg.ENABLED-FwPointersCfg.DISABLED] PASSED [ 51%]2021-01-28 02:29:16,755 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_fwpointers_mixed_scenarios[FwPointersCfg.ENABLED-FwPointersCfg.ENABLED-FwPointersCfg.DISABLED-FwPointersCfg.DISABLED] PASSED [ 51%]2021-01-28 02:29:17,757 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_fwpointers_mixed_scenarios[FwPointersCfg.ENABLED-FwPointersCfg.ENABLED-FwPointersCfg.HYBRID-FwPointersCfg.DISABLED] PASSED [ 51%]2021-01-28 02:29:18,760 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_fwpointers_mixed_scenarios[FwPointersCfg.ENABLED-FwPointersCfg.ENABLED-FwPointersCfg.HYBRID-FwPointersCfg.ENABLED] PASSED [ 51%]2021-01-28 02:29:19,769 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_fwpointers_writemetadata_enabled_disabled PASSED [ 51%]2021-01-28 02:29:20,761 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_fwpointer_enabled_write_delete_keep_version_append PASSED [ 51%]2021-01-28 02:29:21,702 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_version_arctic_version PASSED [ 51%]2021-01-28 02:29:22,590 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_prune_mixed_fwpointer_configs PASSED [ 51%]2021-01-28 02:29:30,193 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_prune_crossref_fwpointer_configs[FwPointersCfg.DISABLED-FwPointersCfg.HYBRID] PASSED [ 51%]2021-01-28 02:29:34,916 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_prune_crossref_fwpointer_configs[FwPointersCfg.DISABLED-FwPointersCfg.ENABLED] PASSED [ 51%]2021-01-28 02:29:39,448 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_prune_crossref_fwpointer_configs[FwPointersCfg.HYBRID-FwPointersCfg.DISABLED] PASSED [ 51%]2021-01-28 02:29:44,014 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_prune_crossref_fwpointer_configs[FwPointersCfg.HYBRID-FwPointersCfg.ENABLED] PASSED [ 51%]2021-01-28 02:29:48,705 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_prune_crossref_fwpointer_configs[FwPointersCfg.ENABLED-FwPointersCfg.HYBRID] PASSED [ 52%]2021-01-28 02:29:53,249 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_prune_crossref_fwpointer_configs[FwPointersCfg.ENABLED-FwPointersCfg.DISABLED] PASSED [ 52%]2021-01-28 02:29:57,782 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store_audit.py::test_ArcticTransaction_can_do_first_writes PASSED [ 52%]2021-01-28 02:29:58,719 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store_audit.py::test_ArcticTransaction_detects_concurrent_writes PASSED [ 52%]2021-01-28 02:29:59,686 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store_audit.py::test_audit_writes PASSED [ 52%]2021-01-28 02:30:00,632 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store_audit.py::test_metadata_changes_writes PASSED [ 52%]2021-01-28 02:30:01,580 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store_audit.py::test_audit_read PASSED [ 52%]2021-01-28 02:30:02,540 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store_audit.py::test_cleanup_orphaned_versions_integration PASSED [ 52%]2021-01-28 02:30:03,468 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store_audit.py::test_corrupted_read_writes_new PASSED [ 52%]
tests/integration/store/test_version_store_audit.py::test_write_after_delete PASSED [ 52%]2021-01-28 02:30:05,417 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store_audit.py::test_ArcticTransaction_write_skips_for_exact_match PASSED [ 52%]2021-01-28 02:30:06,366 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store_audit.py::test_ArcticTransaction_write_doesnt_skip_for_close_ts PASSED [ 52%]2021-01-28 02:30:07,320 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store_corruption.py::test_no_corruption_restore_append_overlapping PASSED [ 52%]2021-01-28 02:30:09,875 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store_corruption.py::test_no_corruption_restore_writemeta_append PASSED [ 53%]2021-01-28 02:30:12,240 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store_corruption.py::test_no_corruption_restore_append_non_overlapping_tstamps PASSED [ 53%]2021-01-28 02:30:16,365 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store_corruption.py::test_restore_append_overlapping_corrupts_old PASSED [ 53%]2021-01-28 02:30:18,032 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store_corruption.py::test_restore_append_overlapping_corrupts_last PASSED [ 53%]2021-01-28 02:30:19,692 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store_corruption.py::test_append_fail_after_delete_noupsert SKIPPED [ 53%]
tests/integration/store/test_version_store_corruption.py::test_append_without_corrupt_check PASSED [ 53%]2021-01-28 02:30:27,743 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store_corruption.py::test_append_with_corrupt_check PASSED [ 53%]2021-01-28 02:30:29,418 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store_corruption.py::test_fast_check_corruption PASSED [ 53%]2021-01-28 02:30:30,400 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store_corruption.py::test_fast_is_safe_to_append PASSED [ 53%]2021-01-28 02:30:44,254 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/tickstore/test_toplevel.py::test_should_return_libraries_for_the_given_daterange[start0-end0-expected0] PASSED [ 53%]2021-01-28 02:30:45,015 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/tickstore/test_toplevel.py::test_should_return_libraries_for_the_given_daterange[start1-end1-expected1] PASSED [ 53%]2021-01-28 02:30:45,776 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/tickstore/test_toplevel.py::test_should_return_libraries_for_the_given_daterange[start2-end2-expected2] PASSED [ 53%]2021-01-28 02:30:46,535 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/tickstore/test_toplevel.py::test_should_return_libraries_for_the_given_daterange[start3-end3-expected3] PASSED [ 53%]2021-01-28 02:30:47,292 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/tickstore/test_toplevel.py::test_should_return_libraries_for_the_given_daterange[start4-end4-expected4] PASSED [ 53%]2021-01-28 02:30:48,037 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/tickstore/test_toplevel.py::test_should_return_libraries_for_the_given_daterange[start5-end5-expected5] PASSED [ 54%]2021-01-28 02:30:48,786 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/tickstore/test_toplevel.py::test_should_return_libraries_for_the_given_daterange[start6-end6-expected6] PASSED [ 54%]2021-01-28 02:30:49,527 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/tickstore/test_toplevel.py::test_should_return_libraries_for_the_given_daterange[start7-end7-expected7] PASSED [ 54%]2021-01-28 02:30:50,269 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/tickstore/test_toplevel.py::test_should_return_libraries_for_the_given_daterange[start8-end8-expected8] PASSED [ 54%]2021-01-28 02:30:51,015 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/tickstore/test_toplevel.py::test_should_raise_exceptions_if_no_libraries_are_found_in_the_date_range_when_reading_data PASSED [ 54%]
tests/integration/tickstore/test_toplevel.py::test_should_return_data_when_date_range_falls_in_a_single_underlying_library FAILED [ 54%]
tests/integration/tickstore/test_toplevel.py::test_should_return_data_when_date_range_spans_libraries PASSED [ 54%]2021-01-28 02:30:53,713 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/tickstore/test_toplevel.py::test_should_return_data_when_date_range_spans_libraries_even_if_one_returns_nothing 2021-01-28 02:30:54,662 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
FAILED [ 54%]
tests/integration/tickstore/test_toplevel.py::test_should_add_underlying_library_where_none_exists PASSED [ 54%]2021-01-28 02:30:55,519 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/tickstore/test_toplevel.py::test_should_add_underlying_library_where_another_library_exists_in_a_non_overlapping_daterange PASSED [ 54%]2021-01-28 02:30:56,340 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/tickstore/test_toplevel.py::test_should_raise_exception_if_library_does_not_exist PASSED [ 54%]
tests/integration/tickstore/test_toplevel.py::test_should_raise_exception_if_date_range_for_library_overlaps_with_existing_libraries PASSED [ 54%]
tests/integration/tickstore/test_toplevel.py::test_should_successfully_do_a_roundtrip_write_and_read_spanning_multiple_underlying_libraries 2021-01-28 02:30:59,008 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
2021-01-28 02:30:59,159 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
XFAIL [ 54%]
tests/integration/tickstore/test_toplevel.py::test_should_list_symbols_from_the_underlying_library[start0-end0-0-10] PASSED [ 55%]2021-01-28 02:31:00,223 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/tickstore/test_toplevel.py::test_should_list_symbols_from_the_underlying_library[start1-end1-0-8] PASSED [ 55%]2021-01-28 02:31:01,245 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/tickstore/test_toplevel.py::test_should_list_symbols_from_the_underlying_library[start2-end2-7-10] PASSED [ 55%]2021-01-28 02:31:02,270 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/tickstore/test_toplevel.py::test_should_add_underlying_libraries_when_intialized PASSED [ 55%]2021-01-28 02:31:03,200 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/tickstore/test_toplevel.py::test_should_write_top_level_with_list_of_dicts FAILED [ 55%]
tests/integration/tickstore/test_toplevel.py::test_should_write_top_level_with_correct_timezone FAILED [ 55%]
tests/integration/tickstore/test_toplevel.py::test_min_max_date PASSED   [ 55%]2021-01-28 02:31:05,962 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/tickstore/test_toplevel.py::test_no_min_max_date PASSED [ 55%]2021-01-28 02:31:06,734 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/tickstore/test_toplevel.py::test_get_libraries_no_data_raises_exception PASSED [ 55%]2021-01-28 02:31:07,472 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/tickstore/test_toplevel.py::test_get_libraries_no_data_raises_exception_tzinfo_given PASSED [ 55%]2021-01-28 02:31:08,214 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/tickstore/test_toplevel.py::test_get_library_metadata PASSED [ 55%]2021-01-28 02:31:09,144 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/tickstore/test_ts_delete.py::test_delete[tickstore] PASSED [ 55%]2021-01-28 02:31:09,939 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/tickstore/test_ts_delete.py::test_delete_daterange[tickstore] PASSED [ 55%]2021-01-28 02:31:10,727 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/tickstore/test_ts_read.py::test_read[tickstore] PASSED [ 56%]2021-01-28 02:31:11,510 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/tickstore/test_ts_read.py::test_read_data_is_modifiable[tickstore] PASSED [ 56%]2021-01-28 02:31:12,290 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/tickstore/test_ts_read.py::test_read_allow_secondary[tickstore] PASSED [ 56%]2021-01-28 02:31:13,073 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/tickstore/test_ts_read.py::test_read_symbol_as_column[tickstore] PASSED [ 56%]2021-01-28 02:31:13,858 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/tickstore/test_ts_read.py::test_read_multiple_symbols[tickstore] PASSED [ 56%]2021-01-28 02:31:14,642 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/tickstore/test_ts_read.py::test_read_all_cols_all_dtypes[tickstore-1] PASSED [ 56%]2021-01-28 02:31:15,440 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/tickstore/test_ts_read.py::test_read_all_cols_all_dtypes[tickstore-100] PASSED [ 56%]2021-01-28 02:31:16,233 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/tickstore/test_ts_read.py::test_date_range[tickstore] PASSED [ 56%]2021-01-28 02:31:17,125 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/tickstore/test_ts_read.py::test_date_range_end_not_in_range[tickstore] PASSED [ 56%]2021-01-28 02:31:17,913 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/tickstore/test_ts_read.py::test_date_range_default_timezone[tickstore-UTC] PASSED [ 56%]2021-01-28 02:31:18,714 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/tickstore/test_ts_read.py::test_date_range_default_timezone[tickstore-Europe/London] PASSED [ 56%]2021-01-28 02:31:19,514 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/tickstore/test_ts_read.py::test_date_range_default_timezone[tickstore-America/New_York] PASSED [ 56%]2021-01-28 02:31:20,313 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/tickstore/test_ts_read.py::test_date_range_no_bounds[tickstore] PASSED [ 56%]2021-01-28 02:31:21,126 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/tickstore/test_ts_read.py::test_date_range_BST[tickstore] PASSED [ 56%]2021-01-28 02:31:21,930 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/tickstore/test_ts_read.py::test_read_no_data[tickstore] PASSED [ 57%]2021-01-28 02:31:22,711 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/tickstore/test_ts_read.py::test_write_no_tz[tickstore] PASSED [ 57%]2021-01-28 02:31:23,489 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/tickstore/test_ts_read.py::test_read_out_of_order[tickstore] PASSED [ 57%]2021-01-28 02:31:24,281 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/tickstore/test_ts_read.py::test_read_chunk_boundaries[tickstore] PASSED [ 57%]2021-01-28 02:31:25,080 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/tickstore/test_ts_read.py::test_read_spanning_chunks[tickstore] PASSED [ 57%]2021-01-28 02:31:25,870 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/tickstore/test_ts_read.py::test_read_inside_range[tickstore] PASSED [ 57%]2021-01-28 02:31:26,651 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/tickstore/test_ts_read.py::test_read_longs[tickstore] PASSED [ 57%]2021-01-28 02:31:27,438 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/tickstore/test_ts_read.py::test_read_with_image[tickstore] PASSED [ 57%]2021-01-28 02:31:28,245 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/tickstore/test_ts_read.py::test_read_with_metadata[tickstore] PASSED [ 57%]2021-01-28 02:31:29,031 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/tickstore/test_ts_read.py::test_read_strings[tickstore] PASSED [ 57%]2021-01-28 02:31:29,819 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/tickstore/test_ts_read.py::test_read_utf8_strings[tickstore] PASSED [ 57%]2021-01-28 02:31:30,603 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/tickstore/test_ts_read.py::test_read_unicode_strings[tickstore] PASSED [ 57%]2021-01-28 02:31:31,394 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/tickstore/test_ts_read.py::test_objects_fail[tickstore] PASSED [ 57%]
tests/integration/tickstore/test_ts_write.py::test_ts_write_simple[tickstore] PASSED [ 58%]2021-01-28 02:31:32,971 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/tickstore/test_ts_write.py::test_overlapping_load[tickstore] PASSED [ 58%]2021-01-28 02:31:33,758 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/tickstore/test_ts_write.py::test_ts_write_pandas[tickstore] PASSED [ 58%]2021-01-28 02:31:34,565 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/tickstore/test_ts_write.py::test_ts_write_named_col[tickstore] PASSED [ 58%]2021-01-28 02:31:35,360 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/tickstore/test_ts_write.py::test_millisecond_roundtrip[tickstore] PASSED [ 58%]2021-01-28 02:31:36,145 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
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
tests/unit/date/test_daterange.py::test_daterange_bounding[unbounded_left] PASSED [ 66%]
tests/unit/date/test_daterange.py::test_daterange_bounding[unbounded] PASSED [ 66%]
tests/unit/date/test_daterange.py::test_daterange_bounding[unbounded_right] PASSED [ 66%]
tests/unit/date/test_daterange.py::test_daterange_bounding[open_open] PASSED [ 66%]
tests/unit/date/test_daterange.py::test_daterange_bounding[open_closed] PASSED [ 66%]
tests/unit/date/test_daterange.py::test_daterange_bounding[closed_open] PASSED [ 66%]
tests/unit/date/test_daterange.py::test_daterange_bounding[closed_by_default] PASSED [ 67%]
tests/unit/date/test_daterange.py::test_daterange_bounding[closed_explicitly] PASSED [ 67%]
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
tests/unit/serialization/test_incremental.py::test_serialize_pandas_to_recarray[onerow] PASSED [ 77%]
tests/unit/serialization/test_incremental.py::test_serialize_pandas_to_recarray[small] PASSED [ 77%]
tests/unit/serialization/test_incremental.py::test_serialize_pandas_to_recarray[medium] PASSED [ 77%]
tests/unit/serialization/test_incremental.py::test_serialize_pandas_to_recarray[large] PASSED [ 77%]
tests/unit/serialization/test_incremental.py::test_serialize_pandas_to_recarray[empty] PASSED [ 77%]
tests/unit/serialization/test_incremental.py::test_serialize_pandas_to_recarray[empty_index] PASSED [ 77%]
tests/unit/serialization/test_incremental.py::test_serialize_pandas_to_recarray[with_some_objects] PASSED [ 77%]
tests/unit/serialization/test_incremental.py::test_serialize_pandas_to_recarray[large_with_some_objects] PASSED [ 77%]
tests/unit/serialization/test_incremental.py::test_serialize_pandas_to_recarray[with_string] PASSED [ 77%]
tests/unit/serialization/test_incremental.py::test_serialize_pandas_to_recarray[with_unicode] PASSED [ 78%]
tests/unit/serialization/test_incremental.py::test_serialize_pandas_to_recarray[with_some_none] PASSED [ 78%]
tests/unit/serialization/test_incremental.py::test_serialize_pandas_to_recarray[multiindex] PASSED [ 78%]
tests/unit/serialization/test_incremental.py::test_serialize_pandas_to_recarray[multiindex_with_object] PASSED [ 78%]
tests/unit/serialization/test_incremental.py::test_serialize_pandas_to_recarray[empty_multiindex] PASSED [ 78%]
tests/unit/serialization/test_incremental.py::test_serialize_pandas_to_recarray[large_multi_index] PASSED [ 78%]
tests/unit/serialization/test_incremental.py::test_serialize_pandas_to_recarray[empty_multicolumn] PASSED [ 78%]
tests/unit/serialization/test_incremental.py::test_serialize_pandas_to_recarray[multi_column_no_multiindex] PASSED [ 78%]
tests/unit/serialization/test_incremental.py::test_serialize_pandas_to_recarray[large_multi_column] PASSED [ 78%]
tests/unit/serialization/test_incremental.py::test_serialize_pandas_to_recarray[multi_column_int_levels] PASSED [ 78%]
tests/unit/serialization/test_incremental.py::test_serialize_pandas_to_recarray[multi_column_and_multi_index] PASSED [ 78%]
tests/unit/serialization/test_incremental.py::test_serialize_pandas_to_recarray[multi_column_with_some_objects] PASSED [ 78%]
tests/unit/serialization/test_incremental.py::test_serialize_pandas_to_recarray[n_dimensional_df] PASSED [ 78%]
tests/unit/serialization/test_incremental.py::test_serialize_pandas_to_recarray[mixed_dtypes_df] PASSED [ 79%]
tests/unit/serialization/test_incremental.py::test_serialize_pandas_to_recarray[index_tz_aware] PASSED [ 79%]
tests/unit/serialization/test_incremental.py::test_serialize_incremental_pandas_to_recarray[onerow] PASSED [ 79%]
tests/unit/serialization/test_incremental.py::test_serialize_incremental_pandas_to_recarray[small] PASSED [ 79%]
tests/unit/serialization/test_incremental.py::test_serialize_incremental_pandas_to_recarray[medium] PASSED [ 79%]
tests/unit/serialization/test_incremental.py::test_serialize_incremental_pandas_to_recarray[large] PASSED [ 79%]
tests/unit/serialization/test_incremental.py::test_serialize_incremental_pandas_to_recarray[empty] PASSED [ 79%]
tests/unit/serialization/test_incremental.py::test_serialize_incremental_pandas_to_recarray[empty_index] PASSED [ 79%]
tests/unit/serialization/test_incremental.py::test_serialize_incremental_pandas_to_recarray[with_some_objects] PASSED [ 79%]
tests/unit/serialization/test_incremental.py::test_serialize_incremental_pandas_to_recarray[large_with_some_objects] PASSED [ 79%]
tests/unit/serialization/test_incremental.py::test_serialize_incremental_pandas_to_recarray[with_string] PASSED [ 79%]
tests/unit/serialization/test_incremental.py::test_serialize_incremental_pandas_to_recarray[with_unicode] PASSED [ 79%]
tests/unit/serialization/test_incremental.py::test_serialize_incremental_pandas_to_recarray[with_some_none] PASSED [ 79%]
tests/unit/serialization/test_incremental.py::test_serialize_incremental_pandas_to_recarray[multiindex] PASSED [ 79%]
tests/unit/serialization/test_incremental.py::test_serialize_incremental_pandas_to_recarray[multiindex_with_object] PASSED [ 80%]
tests/unit/serialization/test_incremental.py::test_serialize_incremental_pandas_to_recarray[empty_multiindex] PASSED [ 80%]
tests/unit/serialization/test_incremental.py::test_serialize_incremental_pandas_to_recarray[large_multi_index] PASSED [ 80%]
tests/unit/serialization/test_incremental.py::test_serialize_incremental_pandas_to_recarray[empty_multicolumn] PASSED [ 80%]
tests/unit/serialization/test_incremental.py::test_serialize_incremental_pandas_to_recarray[multi_column_no_multiindex] PASSED [ 80%]
tests/unit/serialization/test_incremental.py::test_serialize_incremental_pandas_to_recarray[large_multi_column] PASSED [ 80%]
tests/unit/serialization/test_incremental.py::test_serialize_incremental_pandas_to_recarray[multi_column_int_levels] PASSED [ 80%]
tests/unit/serialization/test_incremental.py::test_serialize_incremental_pandas_to_recarray[multi_column_and_multi_index] PASSED [ 80%]
tests/unit/serialization/test_incremental.py::test_serialize_incremental_pandas_to_recarray[multi_column_with_some_objects] PASSED [ 80%]
tests/unit/serialization/test_incremental.py::test_serialize_incremental_pandas_to_recarray[n_dimensional_df] PASSED [ 80%]
tests/unit/serialization/test_incremental.py::test_serialize_incremental_pandas_to_recarray[mixed_dtypes_df] PASSED [ 80%]
tests/unit/serialization/test_incremental.py::test_serialize_incremental_pandas_to_recarray[index_tz_aware] PASSED [ 80%]
tests/unit/serialization/test_incremental.py::test_serialize_incremental_chunk_size_pandas_to_recarray[onerow] PASSED [ 80%]
tests/unit/serialization/test_incremental.py::test_serialize_incremental_chunk_size_pandas_to_recarray[small] PASSED [ 81%]
tests/unit/serialization/test_incremental.py::test_serialize_incremental_chunk_size_pandas_to_recarray[medium] PASSED [ 81%]
tests/unit/serialization/test_incremental.py::test_serialize_incremental_chunk_size_pandas_to_recarray[large] PASSED [ 81%]
tests/unit/serialization/test_incremental.py::test_serialize_incremental_chunk_size_pandas_to_recarray[empty] PASSED [ 81%]
tests/unit/serialization/test_incremental.py::test_serialize_incremental_chunk_size_pandas_to_recarray[empty_index] PASSED [ 81%]
tests/unit/serialization/test_incremental.py::test_serialize_incremental_chunk_size_pandas_to_recarray[with_some_objects] PASSED [ 81%]
tests/unit/serialization/test_incremental.py::test_serialize_incremental_chunk_size_pandas_to_recarray[large_with_some_objects] PASSED [ 81%]
tests/unit/serialization/test_incremental.py::test_serialize_incremental_chunk_size_pandas_to_recarray[with_string] PASSED [ 81%]
tests/unit/serialization/test_incremental.py::test_serialize_incremental_chunk_size_pandas_to_recarray[with_unicode] PASSED [ 81%]
tests/unit/serialization/test_incremental.py::test_serialize_incremental_chunk_size_pandas_to_recarray[with_some_none] PASSED [ 81%]
tests/unit/serialization/test_incremental.py::test_serialize_incremental_chunk_size_pandas_to_recarray[multiindex] PASSED [ 81%]
tests/unit/serialization/test_incremental.py::test_serialize_incremental_chunk_size_pandas_to_recarray[multiindex_with_object] PASSED [ 81%]
tests/unit/serialization/test_incremental.py::test_serialize_incremental_chunk_size_pandas_to_recarray[empty_multiindex] PASSED [ 81%]
tests/unit/serialization/test_incremental.py::test_serialize_incremental_chunk_size_pandas_to_recarray[large_multi_index] PASSED [ 82%]
tests/unit/serialization/test_incremental.py::test_serialize_incremental_chunk_size_pandas_to_recarray[empty_multicolumn] PASSED [ 82%]
tests/unit/serialization/test_incremental.py::test_serialize_incremental_chunk_size_pandas_to_recarray[multi_column_no_multiindex] PASSED [ 82%]
tests/unit/serialization/test_incremental.py::test_serialize_incremental_chunk_size_pandas_to_recarray[large_multi_column] PASSED [ 82%]
tests/unit/serialization/test_incremental.py::test_serialize_incremental_chunk_size_pandas_to_recarray[multi_column_int_levels] PASSED [ 82%]
tests/unit/serialization/test_incremental.py::test_serialize_incremental_chunk_size_pandas_to_recarray[multi_column_and_multi_index] PASSED [ 82%]
tests/unit/serialization/test_incremental.py::test_serialize_incremental_chunk_size_pandas_to_recarray[multi_column_with_some_objects] PASSED [ 82%]
tests/unit/serialization/test_incremental.py::test_serialize_incremental_chunk_size_pandas_to_recarray[n_dimensional_df] PASSED [ 82%]
tests/unit/serialization/test_incremental.py::test_serialize_incremental_chunk_size_pandas_to_recarray[mixed_dtypes_df] PASSED [ 82%]
tests/unit/serialization/test_incremental.py::test_serialize_incremental_chunk_size_pandas_to_recarray[index_tz_aware] PASSED [ 82%]
tests/unit/serialization/test_incremental.py::test_shape[onerow] PASSED  [ 82%]
tests/unit/serialization/test_incremental.py::test_shape[small] PASSED   [ 82%]
tests/unit/serialization/test_incremental.py::test_shape[medium] PASSED  [ 82%]
tests/unit/serialization/test_incremental.py::test_shape[large] PASSED   [ 82%]
tests/unit/serialization/test_incremental.py::test_shape[empty] PASSED   [ 83%]
tests/unit/serialization/test_incremental.py::test_shape[empty_index] PASSED [ 83%]
tests/unit/serialization/test_incremental.py::test_shape[with_some_objects] PASSED [ 83%]
tests/unit/serialization/test_incremental.py::test_shape[large_with_some_objects] PASSED [ 83%]
tests/unit/serialization/test_incremental.py::test_shape[with_string] PASSED [ 83%]
tests/unit/serialization/test_incremental.py::test_shape[with_unicode] PASSED [ 83%]
tests/unit/serialization/test_incremental.py::test_shape[with_some_none] PASSED [ 83%]
tests/unit/serialization/test_incremental.py::test_shape[multiindex] PASSED [ 83%]
tests/unit/serialization/test_incremental.py::test_shape[multiindex_with_object] PASSED [ 83%]
tests/unit/serialization/test_incremental.py::test_shape[empty_multiindex] PASSED [ 83%]
tests/unit/serialization/test_incremental.py::test_shape[large_multi_index] PASSED [ 83%]
tests/unit/serialization/test_incremental.py::test_shape[empty_multicolumn] PASSED [ 83%]
tests/unit/serialization/test_incremental.py::test_shape[multi_column_no_multiindex] PASSED [ 83%]
tests/unit/serialization/test_incremental.py::test_shape[large_multi_column] PASSED [ 84%]
tests/unit/serialization/test_incremental.py::test_shape[multi_column_int_levels] PASSED [ 84%]
tests/unit/serialization/test_incremental.py::test_shape[multi_column_and_multi_index] PASSED [ 84%]
tests/unit/serialization/test_incremental.py::test_shape[multi_column_with_some_objects] PASSED [ 84%]
tests/unit/serialization/test_incremental.py::test_shape[n_dimensional_df] PASSED [ 84%]
tests/unit/serialization/test_incremental.py::test_shape[mixed_dtypes_df] PASSED [ 84%]
tests/unit/serialization/test_incremental.py::test_shape[index_tz_aware] PASSED [ 84%]
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
tests/unit/serialization/test_pandas_is_serializable.py::test_dataframe_confirm_fast_check_compatibility[onerow] PASSED [ 87%]
tests/unit/serialization/test_pandas_is_serializable.py::test_dataframe_confirm_fast_check_compatibility[small] PASSED [ 87%]
tests/unit/serialization/test_pandas_is_serializable.py::test_dataframe_confirm_fast_check_compatibility[medium] PASSED [ 87%]
tests/unit/serialization/test_pandas_is_serializable.py::test_dataframe_confirm_fast_check_compatibility[large] PASSED [ 87%]
tests/unit/serialization/test_pandas_is_serializable.py::test_dataframe_confirm_fast_check_compatibility[empty] PASSED [ 87%]
tests/unit/serialization/test_pandas_is_serializable.py::test_dataframe_confirm_fast_check_compatibility[empty_index] PASSED [ 87%]
tests/unit/serialization/test_pandas_is_serializable.py::test_dataframe_confirm_fast_check_compatibility[with_some_objects] PASSED [ 87%]
tests/unit/serialization/test_pandas_is_serializable.py::test_dataframe_confirm_fast_check_compatibility[large_with_some_objects] PASSED [ 87%]
tests/unit/serialization/test_pandas_is_serializable.py::test_dataframe_confirm_fast_check_compatibility[with_string] PASSED [ 87%]
tests/unit/serialization/test_pandas_is_serializable.py::test_dataframe_confirm_fast_check_compatibility[with_unicode] PASSED [ 87%]
tests/unit/serialization/test_pandas_is_serializable.py::test_dataframe_confirm_fast_check_compatibility[with_some_none] PASSED [ 87%]
tests/unit/serialization/test_pandas_is_serializable.py::test_dataframe_confirm_fast_check_compatibility[multiindex] PASSED [ 87%]
tests/unit/serialization/test_pandas_is_serializable.py::test_dataframe_confirm_fast_check_compatibility[multiindex_with_object] PASSED [ 87%]
tests/unit/serialization/test_pandas_is_serializable.py::test_dataframe_confirm_fast_check_compatibility[empty_multiindex] PASSED [ 88%]
tests/unit/serialization/test_pandas_is_serializable.py::test_dataframe_confirm_fast_check_compatibility[large_multi_index] PASSED [ 88%]
tests/unit/serialization/test_pandas_is_serializable.py::test_dataframe_confirm_fast_check_compatibility[empty_multicolumn] PASSED [ 88%]
tests/unit/serialization/test_pandas_is_serializable.py::test_dataframe_confirm_fast_check_compatibility[multi_column_no_multiindex] PASSED [ 88%]
tests/unit/serialization/test_pandas_is_serializable.py::test_dataframe_confirm_fast_check_compatibility[large_multi_column] PASSED [ 88%]
tests/unit/serialization/test_pandas_is_serializable.py::test_dataframe_confirm_fast_check_compatibility[multi_column_int_levels] PASSED [ 88%]
tests/unit/serialization/test_pandas_is_serializable.py::test_dataframe_confirm_fast_check_compatibility[multi_column_and_multi_index] PASSED [ 88%]
tests/unit/serialization/test_pandas_is_serializable.py::test_dataframe_confirm_fast_check_compatibility[multi_column_with_some_objects] PASSED [ 88%]
tests/unit/serialization/test_pandas_is_serializable.py::test_dataframe_confirm_fast_check_compatibility[n_dimensional_df] PASSED [ 88%]
tests/unit/serialization/test_pandas_is_serializable.py::test_dataframe_confirm_fast_check_compatibility[mixed_dtypes_df] PASSED [ 88%]
tests/unit/serialization/test_pandas_is_serializable.py::test_dataframe_confirm_fast_check_compatibility[index_tz_aware] PASSED [ 88%]
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
tests/unit/store/test_pandas_ndarray_store.py::test_panel_converted_to_dataframe_and_stacked_to_write SKIPPED [ 91%]
tests/unit/store/test_pandas_ndarray_store.py::test_panel_append_not_supported SKIPPED [ 91%]
tests/unit/store/test_pandas_ndarray_store.py::test_panel_converted_from_dataframe_for_reading SKIPPED [ 91%]
tests/unit/store/test_pandas_ndarray_store.py::test_raises_upon_empty_panel_write SKIPPED [ 91%]
tests/unit/store/test_pandas_ndarray_store.py::test_read_multi_index_with_no_ts_info PASSED [ 91%]
tests/unit/store/test_pickle_store.py::test_write PASSED                 [ 92%]
tests/unit/store/test_pickle_store.py::test_write_object PASSED          [ 92%]
tests/unit/store/test_pickle_store.py::test_read PASSED                  [ 92%]
tests/unit/store/test_pickle_store.py::test_read_object_backwards_compat PASSED [ 92%]
tests/unit/store/test_pickle_store.py::test_read_object_2 PASSED         [ 92%]
tests/unit/store/test_pickle_store.py::test_read_with_base_version_id PASSED [ 92%]
tests/unit/store/test_pickle_store.py::test_read_backward_compatibility XFAIL [ 92%]
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
tests/unit/store/test_version_store_audit.py::test_ArcticTransaction_detects_concurrent_writes FAILED [ 96%]
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
=================================== FAILURES ===================================
_ test_should_return_data_when_date_range_falls_in_a_single_underlying_library _
toplevel_tickstore = <arctic.tickstore.toplevel.TopLevelTickStore object at 0x7ffae53764a8>
arctic = <Arctic at 0x7ffad32ff5c0, connected to MongoClient(host=['127.128.125.181:29026'], document_class=dict, tz_aware=False, connect=True)>
    def test_should_return_data_when_date_range_falls_in_a_single_underlying_library(toplevel_tickstore, arctic):
        arctic.initialize_library('FEED_2010.LEVEL1', tickstore.TICK_STORE_TYPE)
        tstore = arctic['FEED_2010.LEVEL1']
        arctic.initialize_library('test_current.toplevel_tickstore', tickstore.TICK_STORE_TYPE)
        tickstore_current = arctic['test_current.toplevel_tickstore']
        toplevel_tickstore._collection.insert_one({'start': dt(2010, 1, 1),
                                               'end': dt(2010, 12, 31, 23, 59, 59),
                                               'library_name': 'FEED_2010.LEVEL1'})
        dates = pd.date_range('20100101', periods=6, tz=mktz('Europe/London'))
        df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))
        tstore.write('blah', df)
        tickstore_current.write('blah', df)
        res = toplevel_tickstore.read('blah', DateRange(start=dt(2010, 1, 1), end=dt(2010, 1, 6)), list('ABCD'))        # FIXME: CM#014 - (read does not include January 1st)
    
>       assert_frame_equal(df, res.tz_convert(mktz('Europe/London')))
E       AssertionError: (<Day>, None)
tests/integration/tickstore/test_toplevel.py:65: AssertionError
---------------------------- Captured stdout setup -----------------------------
2021-01-28T02:30:51.780+0000 I CONTROL  [main] Automatically disabling TLS 1.0, to force-enable TLS 1.0 specify --sslDisabledProtocols 'none'
2021-01-28T02:30:51.783+0000 I CONTROL  [initandlisten] MongoDB starting : pid=31362 port=29026 dbpath=/tmp/tmp63bejz18 64-bit host=travis-job-37fb2906-cc17-4971-b5d1-b8c0f1c59a89
2021-01-28T02:30:51.783+0000 I CONTROL  [initandlisten] db version v4.0.19
2021-01-28T02:30:51.783+0000 I CONTROL  [initandlisten] git version: 7e28f4296a04d858a2e3dd84a1e79c9ba59a9568
2021-01-28T02:30:51.783+0000 I CONTROL  [initandlisten] OpenSSL version: OpenSSL 1.0.2g  1 Mar 2016
2021-01-28T02:30:51.783+0000 I CONTROL  [initandlisten] allocator: tcmalloc
2021-01-28T02:30:51.783+0000 I CONTROL  [initandlisten] modules: none
2021-01-28T02:30:51.783+0000 I CONTROL  [initandlisten] build environment:
2021-01-28T02:30:51.783+0000 I CONTROL  [initandlisten]     distmod: ubuntu1604
2021-01-28T02:30:51.783+0000 I CONTROL  [initandlisten]     distarch: x86_64
2021-01-28T02:30:51.783+0000 I CONTROL  [initandlisten]     target_arch: x86_64
2021-01-28T02:30:51.783+0000 I CONTROL  [initandlisten] options: { net: { bindIp: "127.128.125.181", port: 29026, unixDomainSocket: { enabled: false } }, storage: { dbPath: "/tmp/tmp63bejz18", journal: { enabled: false }, syncPeriodSecs: 0.0 }, systemLog: { quiet: true } }
2021-01-28T02:30:51.783+0000 I STORAGE  [initandlisten] 
2021-01-28T02:30:51.783+0000 I STORAGE  [initandlisten] ** WARNING: Using the XFS filesystem is strongly recommended with the WiredTiger storage engine
2021-01-28T02:30:51.783+0000 I STORAGE  [initandlisten] **          See http://dochub.mongodb.org/core/prodnotes-filesystem
2021-01-28T02:30:51.783+0000 I STORAGE  [initandlisten] wiredtiger_open config: create,cache_size=3476M,cache_overflow=(file_max=0M),session_max=20000,eviction=(threads_min=4,threads_max=4),config_base=false,statistics=(fast),log=(enabled=true,archive=true,path=journal,compressor=snappy),file_manager=(close_idle_time=100000),statistics_log=(wait=0),verbose=(recovery_progress),,log=(enabled=false),
2021-01-28T02:30:52.280+0000 I STORAGE  [initandlisten] WiredTiger message [1611801052:280368][31362:0x7fdfe6c10a80], txn-recover: Set global recovery timestamp: 0
2021-01-28T02:30:52.292+0000 I RECOVERY [initandlisten] WiredTiger recoveryTimestamp. Ts: Timestamp(0, 0)
2021-01-28T02:30:52.317+0000 I CONTROL  [initandlisten] 
2021-01-28T02:30:52.317+0000 I CONTROL  [initandlisten] ** WARNING: Access control is not enabled for the database.
2021-01-28T02:30:52.317+0000 I CONTROL  [initandlisten] **          Read and write access to data and configuration is unrestricted.
2021-01-28T02:30:52.317+0000 I CONTROL  [initandlisten] 
2021-01-28T02:30:52.318+0000 I STORAGE  [initandlisten] createCollection: admin.system.version with provided UUID: 99afe68f-bf63-48ee-b87d-9b8a4c8f656f
2021-01-28T02:30:52.334+0000 I SHARDING [initandlisten] Marking collection admin.system.version as collection version: <unsharded>
2021-01-28T02:30:52.334+0000 I COMMAND  [initandlisten] setting featureCompatibilityVersion to 4.0
2021-01-28T02:30:52.335+0000 I SHARDING [initandlisten] Marking collection local.system.replset as collection version: <unsharded>
2021-01-28T02:30:52.335+0000 I SHARDING [initandlisten] Marking collection admin.system.roles as collection version: <unsharded>
2021-01-28T02:30:52.335+0000 I STORAGE  [initandlisten] createCollection: local.startup_log with generated UUID: 2f280a97-f736-46b6-8024-3febfd3d95a3
2021-01-28T02:30:52.354+0000 I SHARDING [initandlisten] Marking collection local.startup_log as collection version: <unsharded>
2021-01-28T02:30:52.354+0000 I FTDC     [initandlisten] Initializing full-time diagnostic data capture with directory '/tmp/tmp63bejz18/diagnostic.data'
2021-01-28T02:30:52.355+0000 I SHARDING [LogicalSessionCacheRefresh] Marking collection config.system.sessions as collection version: <unsharded>
2021-01-28T02:30:52.355+0000 I STORAGE  [LogicalSessionCacheRefresh] createCollection: config.system.sessions with generated UUID: 7c574d5d-b551-44f6-8588-8cfa3b670bb8
2021-01-28T02:30:52.356+0000 I NETWORK  [initandlisten] waiting for connections on port 29026
2021-01-28T02:30:52.378+0000 I NETWORK  [conn1] received client metadata from 127.0.0.1:47762 conn1: { driver: { name: "PyMongo", version: "3.11.2" }, os: { type: "Linux", name: "Linux", architecture: "x86_64", version: "4.15.0-1077-gcp" }, platform: "CPython 3.6.7.final.0" }
2021-01-28T02:30:52.379+0000 I NETWORK  [conn2] received client metadata from 127.0.0.1:47764 conn2: { driver: { name: "PyMongo", version: "3.11.2" }, os: { type: "Linux", name: "Linux", architecture: "x86_64", version: "4.15.0-1077-gcp" }, platform: "CPython 3.6.7.final.0" }
2021-01-28T02:30:52.382+0000 I INDEX    [LogicalSessionCacheRefresh] build index on: config.system.sessions properties: { v: 2, key: { lastUse: 1 }, name: "lsidTTLIndex", ns: "config.system.sessions", expireAfterSeconds: 1800 }
2021-01-28T02:30:52.382+0000 I INDEX    [LogicalSessionCacheRefresh] 	 building index using bulk method; build may temporarily use up to 500 megabytes of RAM
2021-01-28T02:30:52.383+0000 I INDEX    [LogicalSessionCacheRefresh] build index done.  scanned 0 total records. 0 secs
2021-01-28T02:30:52.383+0000 I SHARDING [LogicalSessionCacheReap] Marking collection config.transactions as collection version: <unsharded>
2021-01-28T02:30:52.385+0000 I NETWORK  [conn3] received client metadata from 127.0.0.1:47766 conn3: { driver: { name: "PyMongo", version: "3.11.2" }, os: { type: "Linux", name: "Linux", architecture: "x86_64", version: "4.15.0-1077-gcp" }, platform: "CPython 3.6.7.final.0" }
2021-01-28T02:30:52.387+0000 I NETWORK  [conn4] received client metadata from 127.0.0.1:47768 conn4: { driver: { name: "PyMongo", version: "3.11.2" }, os: { type: "Linux", name: "Linux", architecture: "x86_64", version: "4.15.0-1077-gcp" }, platform: "CPython 3.6.7.final.0" }
2021-01-28T02:30:52.391+0000 I SHARDING [conn4] Marking collection meta_db.cache as collection version: <unsharded>
2021-01-28T02:30:52.391+0000 I STORAGE  [conn4] createCollection: meta_db.cache with generated UUID: e74ab9b3-7d71-4b0b-92c5-4d7de6229eb7
2021-01-28T02:30:52.419+0000 I INDEX    [conn4] build index on: meta_db.cache properties: { v: 2, key: { date: 1 }, name: "date_1", ns: "meta_db.cache", expireAfterSeconds: 3600 }
2021-01-28T02:30:52.419+0000 I INDEX    [conn4] 	 building index using bulk method; build may temporarily use up to 500 megabytes of RAM
2021-01-28T02:30:52.419+0000 W STORAGE  [conn4] failed to create WiredTiger bulk cursor: Device or resource busy
2021-01-28T02:30:52.419+0000 W STORAGE  [conn4] falling back to non-bulk cursor for index table:index-9--6100003300966920156
2021-01-28T02:30:52.419+0000 I INDEX    [conn4] build index done.  scanned 0 total records. 0 secs
2021-01-28T02:30:52.421+0000 I SHARDING [conn4] Marking collection arctic_test.toplevel_tickstore.ARCTIC as collection version: <unsharded>
2021-01-28T02:30:52.421+0000 I STORAGE  [conn4] createCollection: arctic_test.toplevel_tickstore.ARCTIC with generated UUID: 5820123b-35dc-4aec-a2c5-3b978aaa0f73
2021-01-28T02:30:52.440+0000 I SHARDING [conn4] Marking collection meta_db.settings as collection version: <unsharded>
2021-01-28T02:30:52.444+0000 I STORAGE  [conn4] createCollection: arctic_test.toplevel_tickstore with generated UUID: 41b77851-da44-42da-9a50-eb9ae9f1a7e0
2021-01-28T02:30:52.471+0000 I INDEX    [conn4] build index on: arctic_test.toplevel_tickstore properties: { v: 2, key: { start: 1 }, name: "start_1", ns: "arctic_test.toplevel_tickstore", background: true }
2021-01-28T02:30:52.471+0000 I INDEX    [conn4] build index done.  scanned 0 total records. 0 secs
---------------------------- Captured stderr setup -----------------------------
2021-01-28 02:30:51,754 DEBUG pytest_shutil.workspace 
2021-01-28 02:30:51,754 DEBUG pytest_shutil.workspace =======================================================
2021-01-28 02:30:51,754 DEBUG pytest_shutil.workspace pytest_shutil created workspace /tmp/tmp63bejz18
2021-01-28 02:30:51,754 DEBUG pytest_shutil.workspace This workspace will delete itself on teardown
2021-01-28 02:30:51,755 DEBUG pytest_shutil.workspace =======================================================
2021-01-28 02:30:51,755 DEBUG pytest_shutil.workspace 
2021-01-28 02:30:51,755 DEBUG pytest_server_fixtures.serverclass.thread Launching thread server.
2021-01-28 02:30:51,765 DEBUG pytest_server_fixtures.serverclass.thread Running server: mongod --bind_ip=127.128.125.181 --port=29026 --nounixsocket --syncdelay=0 --nojournal --quiet --dbpath=/tmp/tmp63bejz18
2021-01-28 02:30:51,765 DEBUG pytest_server_fixtures.serverclass.thread CWD: /home/travis/build/man-group/arctic
2021-01-28 02:30:51,766 DEBUG pytest_server_fixtures.base2 sleeping for 0.1 before retrying (1 of 28)
2021-01-28 02:30:51,766 INFO pytest_server_fixtures.mongo Connecting to Mongo at 127.128.125.181:29026
2021-01-28 02:30:51,769 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
2021-01-28 02:30:52,374 DEBUG pytest_server_fixtures.base2 sleeping for 0.1 before retrying (2 of 28)
2021-01-28 02:30:52,374 INFO pytest_server_fixtures.mongo Connecting to Mongo at 127.128.125.181:29026
2021-01-28 02:30:52,385 DEBUG pytest_server_fixtures.base2 waited 0:00:00.619210 for server to start successfully
2021-01-28 02:30:52,385 DEBUG pytest_server_fixtures.base2 Server now awake
2021-01-28 02:30:52,386 INFO arctic.fixtures.arctic arctic.fixtures: arctic init()
2021-01-28 02:30:52,441 DEBUG root Cache has expired data, fetching from slow path and reloading cache.
------------------------------ Captured log setup ------------------------------
DEBUG    pytest_shutil.workspace:workspace.py:52 
DEBUG    pytest_shutil.workspace:workspace.py:53 =======================================================
DEBUG    pytest_shutil.workspace:workspace.py:56 pytest_shutil created workspace /tmp/tmp63bejz18
DEBUG    pytest_shutil.workspace:workspace.py:64 This workspace will delete itself on teardown
DEBUG    pytest_shutil.workspace:workspace.py:65 =======================================================
DEBUG    pytest_shutil.workspace:workspace.py:66 
DEBUG    pytest_server_fixtures.serverclass.thread:thread.py:77 Launching thread server.
DEBUG    pytest_server_fixtures.serverclass.thread:thread.py:89 Running server: mongod --bind_ip=127.128.125.181 --port=29026 --nounixsocket --syncdelay=0 --nojournal --quiet --dbpath=/tmp/tmp63bejz18
DEBUG    pytest_server_fixtures.serverclass.thread:thread.py:90 CWD: /home/travis/build/man-group/arctic
DEBUG    pytest_server_fixtures.base2:base2.py:226 sleeping for 0.1 before retrying (1 of 28)
INFO     pytest_server_fixtures.mongo:mongo.py:128 Connecting to Mongo at 127.128.125.181:29026
DEBUG    pytest_server_fixtures.base2:base2.py:82 Server is already killed, skipping
DEBUG    pytest_server_fixtures.base2:base2.py:226 sleeping for 0.1 before retrying (2 of 28)
INFO     pytest_server_fixtures.mongo:mongo.py:128 Connecting to Mongo at 127.128.125.181:29026
DEBUG    pytest_server_fixtures.base2:base2.py:229 waited 0:00:00.619210 for server to start successfully
DEBUG    pytest_server_fixtures.base2:base2.py:69 Server now awake
INFO     arctic.fixtures.arctic:arctic.py:23 arctic.fixtures: arctic init()
DEBUG    root:arctic.py:234 Cache has expired data, fetching from slow path and reloading cache.
----------------------------- Captured stdout call -----------------------------
2021-01-28T02:30:52.478+0000 I SHARDING [conn4] Marking collection arctic_FEED_2010.LEVEL1.ARCTIC as collection version: <unsharded>
2021-01-28T02:30:52.478+0000 I STORAGE  [conn4] createCollection: arctic_FEED_2010.LEVEL1.ARCTIC with generated UUID: 14b124ba-66c3-47e2-bead-d5e696bab65a
2021-01-28T02:30:52.501+0000 I STORAGE  [conn4] createCollection: arctic_FEED_2010.LEVEL1 with generated UUID: 2d182c71-25b2-43cf-aa10-817ecfce6bf8
2021-01-28T02:30:52.530+0000 I INDEX    [conn4] build index on: arctic_FEED_2010.LEVEL1 properties: { v: 2, key: { sy: 1, s: 1 }, name: "sy_1_s_1", ns: "arctic_FEED_2010.LEVEL1", background: true }
2021-01-28T02:30:52.530+0000 I INDEX    [conn4] build index done.  scanned 0 total records. 0 secs
2021-01-28T02:30:52.541+0000 I INDEX    [conn4] build index on: arctic_FEED_2010.LEVEL1 properties: { v: 2, key: { s: 1 }, name: "s_1", ns: "arctic_FEED_2010.LEVEL1", background: true }
2021-01-28T02:30:52.542+0000 I INDEX    [conn4] build index done.  scanned 0 total records. 0 secs
2021-01-28T02:30:52.543+0000 I STORAGE  [conn4] createCollection: arctic_FEED_2010.LEVEL1.metadata with generated UUID: 6f104844-fa63-48ef-86ff-7c710b86d088
2021-01-28T02:30:52.564+0000 I SHARDING [conn4] Marking collection arctic_FEED_2010.LEVEL1.metadata as collection version: <unsharded>
2021-01-28T02:30:52.574+0000 I INDEX    [conn4] build index on: arctic_FEED_2010.LEVEL1.metadata properties: { v: 2, unique: true, key: { sy: 1 }, name: "sy_1", ns: "arctic_FEED_2010.LEVEL1.metadata", background: true }
2021-01-28T02:30:52.574+0000 I INDEX    [conn4] build index done.  scanned 0 total records. 0 secs
2021-01-28T02:30:52.579+0000 I SHARDING [conn4] Marking collection arctic_test_current.toplevel_tickstore.ARCTIC as collection version: <unsharded>
2021-01-28T02:30:52.579+0000 I STORAGE  [conn4] createCollection: arctic_test_current.toplevel_tickstore.ARCTIC with generated UUID: 79052f9e-c528-4a8f-81db-fcde40f92ac1
2021-01-28T02:30:52.599+0000 I STORAGE  [conn4] createCollection: arctic_test_current.toplevel_tickstore with generated UUID: 3a54c86d-a8ab-4248-a69e-a6a3d5d701b2
2021-01-28T02:30:52.628+0000 I INDEX    [conn4] build index on: arctic_test_current.toplevel_tickstore properties: { v: 2, key: { sy: 1, s: 1 }, name: "sy_1_s_1", ns: "arctic_test_current.toplevel_tickstore", background: true }
2021-01-28T02:30:52.628+0000 I INDEX    [conn4] build index done.  scanned 0 total records. 0 secs
2021-01-28T02:30:52.638+0000 I INDEX    [conn4] build index on: arctic_test_current.toplevel_tickstore properties: { v: 2, key: { s: 1 }, name: "s_1", ns: "arctic_test_current.toplevel_tickstore", background: true }
2021-01-28T02:30:52.639+0000 I INDEX    [conn4] build index done.  scanned 0 total records. 0 secs
2021-01-28T02:30:52.640+0000 I STORAGE  [conn4] createCollection: arctic_test_current.toplevel_tickstore.metadata with generated UUID: f50a0725-bc35-4eb2-b561-093aacf92544
2021-01-28T02:30:52.662+0000 I SHARDING [conn4] Marking collection arctic_test_current.toplevel_tickstore.metadata as collection version: <unsharded>
2021-01-28T02:30:52.672+0000 I INDEX    [conn4] build index on: arctic_test_current.toplevel_tickstore.metadata properties: { v: 2, unique: true, key: { sy: 1 }, name: "sy_1", ns: "arctic_test_current.toplevel_tickstore.metadata", background: true }
2021-01-28T02:30:52.672+0000 I INDEX    [conn4] build index done.  scanned 0 total records. 0 secs
2021-01-28T02:30:52.677+0000 I SHARDING [conn4] Marking collection arctic_test.toplevel_tickstore as collection version: <unsharded>
2021-01-28T02:30:52.680+0000 I SHARDING [conn4] Marking collection arctic_FEED_2010.LEVEL1 as collection version: <unsharded>
2021-01-28T02:30:52.685+0000 I SHARDING [conn4] Marking collection arctic_test_current.toplevel_tickstore as collection version: <unsharded>
----------------------------- Captured stderr call -----------------------------
2021-01-28 02:30:52,681 WARNING arctic.tickstore.tickstore NB treating all values as 'exists' - no longer sparse
2021-01-28 02:30:52,684 DEBUG arctic.tickstore.tickstore 1 buckets in 0.001145: approx 87336244 ticks/sec
2021-01-28 02:30:52,687 WARNING arctic.tickstore.tickstore NB treating all values as 'exists' - no longer sparse
2021-01-28 02:30:52,690 DEBUG arctic.tickstore.tickstore 1 buckets in 0.001071: approx 93370681 ticks/sec
2021-01-28 02:30:52,697 INFO arctic.tickstore.tickstore Got data in 0.004821 secs, creating DataFrame...
2021-01-28 02:30:52,698 INFO arctic.tickstore.tickstore 6 rows in 0.006157 secs: 974 ticks/sec
------------------------------ Captured log call -------------------------------
WARNING  arctic.tickstore.tickstore:tickstore.py:706 NB treating all values as 'exists' - no longer sparse
DEBUG    arctic.tickstore.tickstore:tickstore.py:612 1 buckets in 0.001145: approx 87336244 ticks/sec
WARNING  arctic.tickstore.tickstore:tickstore.py:706 NB treating all values as 'exists' - no longer sparse
DEBUG    arctic.tickstore.tickstore:tickstore.py:612 1 buckets in 0.001071: approx 93370681 ticks/sec
INFO     arctic.tickstore.tickstore:tickstore.py:355 Got data in 0.004821 secs, creating DataFrame...
INFO     arctic.tickstore.tickstore:tickstore.py:364 6 rows in 0.006157 secs: 974 ticks/sec
--------------------------- Captured stderr teardown ---------------------------
2021-01-28 02:30:52,728 DEBUG pytest_server_fixtures.serverclass.thread Killing process tree for 31362 (total_procs_to_kill=1)
2021-01-28 02:30:52,728 DEBUG pytest_server_fixtures.serverclass.thread Killing 1 processes with signal Signals.SIGKILL
2021-01-28 02:30:52,728 DEBUG pytest_server_fixtures.serverclass.thread Waiting for 1 processes to die
2021-01-28 02:30:52,732 DEBUG pytest_server_fixtures.serverclass.thread All processes are terminated
2021-01-28 02:30:52,733 DEBUG pytest_shutil.workspace 
2021-01-28 02:30:52,733 DEBUG pytest_shutil.workspace =======================================================
2021-01-28 02:30:52,733 DEBUG pytest_shutil.workspace pytest_shutil deleting workspace /tmp/tmp63bejz18
2021-01-28 02:30:52,733 DEBUG pytest_shutil.workspace =======================================================
2021-01-28 02:30:52,733 DEBUG pytest_shutil.workspace 
---------------------------- Captured log teardown -----------------------------
DEBUG    pytest_server_fixtures.serverclass.thread:thread.py:54 Killing process tree for 31362 (total_procs_to_kill=1)
DEBUG    pytest_server_fixtures.serverclass.thread:thread.py:35 Killing 1 processes with signal Signals.SIGKILL
DEBUG    pytest_server_fixtures.serverclass.thread:thread.py:39 Waiting for 1 processes to die
DEBUG    pytest_server_fixtures.serverclass.thread:thread.py:43 All processes are terminated
DEBUG    pytest_shutil.workspace:workspace.py:140 
DEBUG    pytest_shutil.workspace:workspace.py:141 =======================================================
DEBUG    pytest_shutil.workspace:workspace.py:142 pytest_shutil deleting workspace /tmp/tmp63bejz18
DEBUG    pytest_shutil.workspace:workspace.py:143 =======================================================
DEBUG    pytest_shutil.workspace:workspace.py:144
_ test_should_return_data_when_date_range_spans_libraries_even_if_one_returns_nothing _
toplevel_tickstore = <arctic.tickstore.toplevel.TopLevelTickStore object at 0x7ffad2c66630>
arctic = <Arctic at 0x7ffad32709e8, connected to MongoClient(host=['127.128.125.181:5899'], document_class=dict, tz_aware=False, connect=True)>
    def test_should_return_data_when_date_range_spans_libraries_even_if_one_returns_nothing(toplevel_tickstore, arctic):
        arctic.initialize_library('FEED_2010.LEVEL1', tickstore.TICK_STORE_TYPE)
        arctic.initialize_library('FEED_2011.LEVEL1', tickstore.TICK_STORE_TYPE)
        tickstore_2010 = arctic['FEED_2010.LEVEL1']
        tickstore_2011 = arctic['FEED_2011.LEVEL1']
        toplevel_tickstore.add(DateRange(start=dt(2010, 1, 1), end=dt(2010, 12, 31, 23, 59, 59, 999000)), 'FEED_2010.LEVEL1')
        toplevel_tickstore.add(DateRange(start=dt(2011, 1, 1), end=dt(2011, 12, 31, 23, 59, 59, 999000)), 'FEED_2011.LEVEL1')
        dates = pd.date_range('20100101', periods=6, tz=mktz('Europe/London'))
        df_10 = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))
        tickstore_2010.write('blah', df_10)
        dates = pd.date_range('20110201', periods=6, tz=mktz('Europe/London'))
        df_11 = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))
        tickstore_2011.write('blah', df_11)
        res = toplevel_tickstore.read('blah', DateRange(start=dt(2010, 1, 2), end=dt(2011, 1, 4)), list('ABCD'))
        expected_df = df_10[1:]
>       assert_frame_equal(expected_df, res.tz_convert(mktz('Europe/London')))
E       AssertionError: (<Day>, None)
tests/integration/tickstore/test_toplevel.py:101: AssertionError
---------------------------- Captured stdout setup -----------------------------
2021-01-28T02:30:53.741+0000 I CONTROL  [main] Automatically disabling TLS 1.0, to force-enable TLS 1.0 specify --sslDisabledProtocols 'none'
2021-01-28T02:30:53.743+0000 I CONTROL  [initandlisten] MongoDB starting : pid=31432 port=5899 dbpath=/tmp/tmpizx7gwmy 64-bit host=travis-job-37fb2906-cc17-4971-b5d1-b8c0f1c59a89
2021-01-28T02:30:53.743+0000 I CONTROL  [initandlisten] db version v4.0.19
2021-01-28T02:30:53.743+0000 I CONTROL  [initandlisten] git version: 7e28f4296a04d858a2e3dd84a1e79c9ba59a9568
2021-01-28T02:30:53.743+0000 I CONTROL  [initandlisten] OpenSSL version: OpenSSL 1.0.2g  1 Mar 2016
2021-01-28T02:30:53.743+0000 I CONTROL  [initandlisten] allocator: tcmalloc
2021-01-28T02:30:53.743+0000 I CONTROL  [initandlisten] modules: none
2021-01-28T02:30:53.743+0000 I CONTROL  [initandlisten] build environment:
2021-01-28T02:30:53.743+0000 I CONTROL  [initandlisten]     distmod: ubuntu1604
2021-01-28T02:30:53.743+0000 I CONTROL  [initandlisten]     distarch: x86_64
2021-01-28T02:30:53.743+0000 I CONTROL  [initandlisten]     target_arch: x86_64
2021-01-28T02:30:53.743+0000 I CONTROL  [initandlisten] options: { net: { bindIp: "127.128.125.181", port: 5899, unixDomainSocket: { enabled: false } }, storage: { dbPath: "/tmp/tmpizx7gwmy", journal: { enabled: false }, syncPeriodSecs: 0.0 }, systemLog: { quiet: true } }
2021-01-28T02:30:53.743+0000 I STORAGE  [initandlisten] 
2021-01-28T02:30:53.743+0000 I STORAGE  [initandlisten] ** WARNING: Using the XFS filesystem is strongly recommended with the WiredTiger storage engine
2021-01-28T02:30:53.743+0000 I STORAGE  [initandlisten] **          See http://dochub.mongodb.org/core/prodnotes-filesystem
2021-01-28T02:30:53.743+0000 I STORAGE  [initandlisten] wiredtiger_open config: create,cache_size=3476M,cache_overflow=(file_max=0M),session_max=20000,eviction=(threads_min=4,threads_max=4),config_base=false,statistics=(fast),log=(enabled=true,archive=true,path=journal,compressor=snappy),file_manager=(close_idle_time=100000),statistics_log=(wait=0),verbose=(recovery_progress),,log=(enabled=false),
2021-01-28T02:30:54.237+0000 I STORAGE  [initandlisten] WiredTiger message [1611801054:237938][31432:0x7fa5af83fa80], txn-recover: Set global recovery timestamp: 0
2021-01-28T02:30:54.249+0000 I RECOVERY [initandlisten] WiredTiger recoveryTimestamp. Ts: Timestamp(0, 0)
2021-01-28T02:30:54.274+0000 I CONTROL  [initandlisten] 
2021-01-28T02:30:54.274+0000 I CONTROL  [initandlisten] ** WARNING: Access control is not enabled for the database.
2021-01-28T02:30:54.274+0000 I CONTROL  [initandlisten] **          Read and write access to data and configuration is unrestricted.
2021-01-28T02:30:54.274+0000 I CONTROL  [initandlisten] 
2021-01-28T02:30:54.274+0000 I STORAGE  [initandlisten] createCollection: admin.system.version with provided UUID: 0093de8e-52f2-4e1f-a311-328c908f7630
2021-01-28T02:30:54.292+0000 I SHARDING [initandlisten] Marking collection admin.system.version as collection version: <unsharded>
2021-01-28T02:30:54.292+0000 I COMMAND  [initandlisten] setting featureCompatibilityVersion to 4.0
2021-01-28T02:30:54.292+0000 I SHARDING [initandlisten] Marking collection local.system.replset as collection version: <unsharded>
2021-01-28T02:30:54.292+0000 I SHARDING [initandlisten] Marking collection admin.system.roles as collection version: <unsharded>
2021-01-28T02:30:54.292+0000 I STORAGE  [initandlisten] createCollection: local.startup_log with generated UUID: f4b8098a-497f-4448-9093-5fe1db3db415
2021-01-28T02:30:54.310+0000 I SHARDING [initandlisten] Marking collection local.startup_log as collection version: <unsharded>
2021-01-28T02:30:54.310+0000 I FTDC     [initandlisten] Initializing full-time diagnostic data capture with directory '/tmp/tmpizx7gwmy/diagnostic.data'
2021-01-28T02:30:54.311+0000 I SHARDING [LogicalSessionCacheRefresh] Marking collection config.system.sessions as collection version: <unsharded>
2021-01-28T02:30:54.311+0000 I NETWORK  [initandlisten] waiting for connections on port 5899
2021-01-28T02:30:54.312+0000 I STORAGE  [LogicalSessionCacheRefresh] createCollection: config.system.sessions with generated UUID: b4f0f4dc-875b-4590-affe-ec1001072d50
2021-01-28T02:30:54.312+0000 I CONTROL  [LogicalSessionCacheReap] Sessions collection is not set up; waiting until next sessions reap interval: config.system.sessions does not exist
2021-01-28T02:30:54.338+0000 I NETWORK  [conn1] received client metadata from 127.0.0.1:47394 conn1: { driver: { name: "PyMongo", version: "3.11.2" }, os: { type: "Linux", name: "Linux", architecture: "x86_64", version: "4.15.0-1077-gcp" }, platform: "CPython 3.6.7.final.0" }
2021-01-28T02:30:54.339+0000 I NETWORK  [conn2] received client metadata from 127.0.0.1:47396 conn2: { driver: { name: "PyMongo", version: "3.11.2" }, os: { type: "Linux", name: "Linux", architecture: "x86_64", version: "4.15.0-1077-gcp" }, platform: "CPython 3.6.7.final.0" }
2021-01-28T02:30:54.342+0000 I INDEX    [LogicalSessionCacheRefresh] build index on: config.system.sessions properties: { v: 2, key: { lastUse: 1 }, name: "lsidTTLIndex", ns: "config.system.sessions", expireAfterSeconds: 1800 }
2021-01-28T02:30:54.342+0000 I INDEX    [LogicalSessionCacheRefresh] 	 building index using bulk method; build may temporarily use up to 500 megabytes of RAM
2021-01-28T02:30:54.342+0000 W STORAGE  [LogicalSessionCacheRefresh] failed to create WiredTiger bulk cursor: Device or resource busy
2021-01-28T02:30:54.342+0000 W STORAGE  [LogicalSessionCacheRefresh] falling back to non-bulk cursor for index table:index-6--6185045360240220669
2021-01-28T02:30:54.342+0000 I INDEX    [LogicalSessionCacheRefresh] build index done.  scanned 0 total records. 0 secs
2021-01-28T02:30:54.344+0000 I NETWORK  [conn3] received client metadata from 127.0.0.1:47398 conn3: { driver: { name: "PyMongo", version: "3.11.2" }, os: { type: "Linux", name: "Linux", architecture: "x86_64", version: "4.15.0-1077-gcp" }, platform: "CPython 3.6.7.final.0" }
2021-01-28T02:30:54.345+0000 I NETWORK  [conn4] received client metadata from 127.0.0.1:47400 conn4: { driver: { name: "PyMongo", version: "3.11.2" }, os: { type: "Linux", name: "Linux", architecture: "x86_64", version: "4.15.0-1077-gcp" }, platform: "CPython 3.6.7.final.0" }
2021-01-28T02:30:54.349+0000 I SHARDING [conn4] Marking collection meta_db.cache as collection version: <unsharded>
2021-01-28T02:30:54.349+0000 I STORAGE  [conn4] createCollection: meta_db.cache with generated UUID: 484829e2-9857-40e4-b515-dcdcddc17142
2021-01-28T02:30:54.375+0000 I INDEX    [conn4] build index on: meta_db.cache properties: { v: 2, key: { date: 1 }, name: "date_1", ns: "meta_db.cache", expireAfterSeconds: 3600 }
2021-01-28T02:30:54.375+0000 I INDEX    [conn4] 	 building index using bulk method; build may temporarily use up to 500 megabytes of RAM
2021-01-28T02:30:54.375+0000 W STORAGE  [conn4] failed to create WiredTiger bulk cursor: Device or resource busy
2021-01-28T02:30:54.375+0000 W STORAGE  [conn4] falling back to non-bulk cursor for index table:index-9--6185045360240220669
2021-01-28T02:30:54.375+0000 I INDEX    [conn4] build index done.  scanned 0 total records. 0 secs
2021-01-28T02:30:54.378+0000 I SHARDING [conn4] Marking collection arctic_test.toplevel_tickstore.ARCTIC as collection version: <unsharded>
2021-01-28T02:30:54.378+0000 I STORAGE  [conn4] createCollection: arctic_test.toplevel_tickstore.ARCTIC with generated UUID: 4dbe038a-f691-404c-9016-a4b10516ae7d
2021-01-28T02:30:54.397+0000 I SHARDING [conn4] Marking collection meta_db.settings as collection version: <unsharded>
2021-01-28T02:30:54.401+0000 I STORAGE  [conn4] createCollection: arctic_test.toplevel_tickstore with generated UUID: c4a84f29-82c6-4b72-af97-13628a617878
2021-01-28T02:30:54.434+0000 I INDEX    [conn4] build index on: arctic_test.toplevel_tickstore properties: { v: 2, key: { start: 1 }, name: "start_1", ns: "arctic_test.toplevel_tickstore", background: true }
2021-01-28T02:30:54.434+0000 I INDEX    [conn4] build index done.  scanned 0 total records. 0 secs
---------------------------- Captured stderr setup -----------------------------
2021-01-28 02:30:53,715 DEBUG pytest_shutil.workspace 
2021-01-28 02:30:53,715 DEBUG pytest_shutil.workspace =======================================================
2021-01-28 02:30:53,715 DEBUG pytest_shutil.workspace pytest_shutil created workspace /tmp/tmpizx7gwmy
2021-01-28 02:30:53,716 DEBUG pytest_shutil.workspace This workspace will delete itself on teardown
2021-01-28 02:30:53,716 DEBUG pytest_shutil.workspace =======================================================
2021-01-28 02:30:53,716 DEBUG pytest_shutil.workspace 
2021-01-28 02:30:53,716 DEBUG pytest_server_fixtures.serverclass.thread Launching thread server.
2021-01-28 02:30:53,726 DEBUG pytest_server_fixtures.serverclass.thread Running server: mongod --bind_ip=127.128.125.181 --port=5899 --nounixsocket --syncdelay=0 --nojournal --quiet --dbpath=/tmp/tmpizx7gwmy
2021-01-28 02:30:53,726 DEBUG pytest_server_fixtures.serverclass.thread CWD: /home/travis/build/man-group/arctic
2021-01-28 02:30:53,727 DEBUG pytest_server_fixtures.base2 sleeping for 0.1 before retrying (1 of 28)
2021-01-28 02:30:53,727 INFO pytest_server_fixtures.mongo Connecting to Mongo at 127.128.125.181:5899
2021-01-28 02:30:54,333 DEBUG pytest_server_fixtures.base2 sleeping for 0.1 before retrying (2 of 28)
2021-01-28 02:30:54,333 INFO pytest_server_fixtures.mongo Connecting to Mongo at 127.128.125.181:5899
2021-01-28 02:30:54,343 DEBUG pytest_server_fixtures.base2 waited 0:00:00.616503 for server to start successfully
2021-01-28 02:30:54,344 DEBUG pytest_server_fixtures.base2 Server now awake
2021-01-28 02:30:54,344 INFO arctic.fixtures.arctic arctic.fixtures: arctic init()
2021-01-28 02:30:54,398 DEBUG root Cache has expired data, fetching from slow path and reloading cache.
------------------------------ Captured log setup ------------------------------
DEBUG    pytest_shutil.workspace:workspace.py:52 
DEBUG    pytest_shutil.workspace:workspace.py:53 =======================================================
DEBUG    pytest_shutil.workspace:workspace.py:56 pytest_shutil created workspace /tmp/tmpizx7gwmy
DEBUG    pytest_shutil.workspace:workspace.py:64 This workspace will delete itself on teardown
DEBUG    pytest_shutil.workspace:workspace.py:65 =======================================================
DEBUG    pytest_shutil.workspace:workspace.py:66 
DEBUG    pytest_server_fixtures.serverclass.thread:thread.py:77 Launching thread server.
DEBUG    pytest_server_fixtures.serverclass.thread:thread.py:89 Running server: mongod --bind_ip=127.128.125.181 --port=5899 --nounixsocket --syncdelay=0 --nojournal --quiet --dbpath=/tmp/tmpizx7gwmy
DEBUG    pytest_server_fixtures.serverclass.thread:thread.py:90 CWD: /home/travis/build/man-group/arctic
DEBUG    pytest_server_fixtures.base2:base2.py:226 sleeping for 0.1 before retrying (1 of 28)
INFO     pytest_server_fixtures.mongo:mongo.py:128 Connecting to Mongo at 127.128.125.181:5899
DEBUG    pytest_server_fixtures.base2:base2.py:226 sleeping for 0.1 before retrying (2 of 28)
INFO     pytest_server_fixtures.mongo:mongo.py:128 Connecting to Mongo at 127.128.125.181:5899
DEBUG    pytest_server_fixtures.base2:base2.py:229 waited 0:00:00.616503 for server to start successfully
DEBUG    pytest_server_fixtures.base2:base2.py:69 Server now awake
INFO     arctic.fixtures.arctic:arctic.py:23 arctic.fixtures: arctic init()
DEBUG    root:arctic.py:234 Cache has expired data, fetching from slow path and reloading cache.
----------------------------- Captured stdout call -----------------------------
2021-01-28T02:30:54.440+0000 I SHARDING [conn4] Marking collection arctic_FEED_2010.LEVEL1.ARCTIC as collection version: <unsharded>
2021-01-28T02:30:54.440+0000 I STORAGE  [conn4] createCollection: arctic_FEED_2010.LEVEL1.ARCTIC with generated UUID: 2d71b910-6eac-4632-b9ce-244958d5adef
2021-01-28T02:30:54.461+0000 I STORAGE  [conn4] createCollection: arctic_FEED_2010.LEVEL1 with generated UUID: 17b96d09-016d-4ab5-87a0-55733fa4cd5e
2021-01-28T02:30:54.487+0000 I INDEX    [conn4] build index on: arctic_FEED_2010.LEVEL1 properties: { v: 2, key: { sy: 1, s: 1 }, name: "sy_1_s_1", ns: "arctic_FEED_2010.LEVEL1", background: true }
2021-01-28T02:30:54.487+0000 I INDEX    [conn4] build index done.  scanned 0 total records. 0 secs
2021-01-28T02:30:54.498+0000 I INDEX    [conn4] build index on: arctic_FEED_2010.LEVEL1 properties: { v: 2, key: { s: 1 }, name: "s_1", ns: "arctic_FEED_2010.LEVEL1", background: true }
2021-01-28T02:30:54.498+0000 I INDEX    [conn4] build index done.  scanned 0 total records. 0 secs
2021-01-28T02:30:54.500+0000 I STORAGE  [conn4] createCollection: arctic_FEED_2010.LEVEL1.metadata with generated UUID: 4e936954-f207-4089-a13d-8f09206fc196
2021-01-28T02:30:54.517+0000 I SHARDING [conn4] Marking collection arctic_FEED_2010.LEVEL1.metadata as collection version: <unsharded>
2021-01-28T02:30:54.527+0000 I INDEX    [conn4] build index on: arctic_FEED_2010.LEVEL1.metadata properties: { v: 2, unique: true, key: { sy: 1 }, name: "sy_1", ns: "arctic_FEED_2010.LEVEL1.metadata", background: true }
2021-01-28T02:30:54.527+0000 I INDEX    [conn4] build index done.  scanned 0 total records. 0 secs
2021-01-28T02:30:54.532+0000 I SHARDING [conn4] Marking collection arctic_FEED_2011.LEVEL1.ARCTIC as collection version: <unsharded>
2021-01-28T02:30:54.532+0000 I STORAGE  [conn4] createCollection: arctic_FEED_2011.LEVEL1.ARCTIC with generated UUID: 59210042-ee7e-43e4-985c-03819ef27b0b
2021-01-28T02:30:54.550+0000 I STORAGE  [conn4] createCollection: arctic_FEED_2011.LEVEL1 with generated UUID: 47b68305-5659-4c61-9754-4a2a90b2463b
2021-01-28T02:30:54.577+0000 I INDEX    [conn4] build index on: arctic_FEED_2011.LEVEL1 properties: { v: 2, key: { sy: 1, s: 1 }, name: "sy_1_s_1", ns: "arctic_FEED_2011.LEVEL1", background: true }
2021-01-28T02:30:54.578+0000 I INDEX    [conn4] build index done.  scanned 0 total records. 0 secs
2021-01-28T02:30:54.587+0000 I INDEX    [conn4] build index on: arctic_FEED_2011.LEVEL1 properties: { v: 2, key: { s: 1 }, name: "s_1", ns: "arctic_FEED_2011.LEVEL1", background: true }
2021-01-28T02:30:54.587+0000 I INDEX    [conn4] build index done.  scanned 0 total records. 0 secs
2021-01-28T02:30:54.588+0000 I STORAGE  [conn4] createCollection: arctic_FEED_2011.LEVEL1.metadata with generated UUID: 38ccca5f-ad85-4304-99c6-1e1f110d9db4
2021-01-28T02:30:54.609+0000 I SHARDING [conn4] Marking collection arctic_FEED_2011.LEVEL1.metadata as collection version: <unsharded>
2021-01-28T02:30:54.620+0000 I INDEX    [conn4] build index on: arctic_FEED_2011.LEVEL1.metadata properties: { v: 2, unique: true, key: { sy: 1 }, name: "sy_1", ns: "arctic_FEED_2011.LEVEL1.metadata", background: true }
2021-01-28T02:30:54.620+0000 I INDEX    [conn4] build index done.  scanned 0 total records. 0 secs
2021-01-28T02:30:54.626+0000 I SHARDING [conn4] Marking collection arctic_test.toplevel_tickstore as collection version: <unsharded>
2021-01-28T02:30:54.632+0000 I SHARDING [conn4] Marking collection arctic_FEED_2010.LEVEL1 as collection version: <unsharded>
2021-01-28T02:30:54.638+0000 I SHARDING [conn4] Marking collection arctic_FEED_2011.LEVEL1 as collection version: <unsharded>
----------------------------- Captured stderr call -----------------------------
2021-01-28 02:30:54,633 WARNING arctic.tickstore.tickstore NB treating all values as 'exists' - no longer sparse
2021-01-28 02:30:54,636 DEBUG arctic.tickstore.tickstore 1 buckets in 0.001328: approx 75301204 ticks/sec
2021-01-28 02:30:54,639 WARNING arctic.tickstore.tickstore NB treating all values as 'exists' - no longer sparse
2021-01-28 02:30:54,643 DEBUG arctic.tickstore.tickstore 1 buckets in 0.001051: approx 95147478 ticks/sec
2021-01-28 02:30:54,649 INFO arctic.tickstore.tickstore Got data in 0.004655 secs, creating DataFrame...
2021-01-28 02:30:54,650 INFO arctic.tickstore.tickstore 6 rows in 0.005995 secs: 1000 ticks/sec
------------------------------ Captured log call -------------------------------
WARNING  arctic.tickstore.tickstore:tickstore.py:706 NB treating all values as 'exists' - no longer sparse
DEBUG    arctic.tickstore.tickstore:tickstore.py:612 1 buckets in 0.001328: approx 75301204 ticks/sec
WARNING  arctic.tickstore.tickstore:tickstore.py:706 NB treating all values as 'exists' - no longer sparse
DEBUG    arctic.tickstore.tickstore:tickstore.py:612 1 buckets in 0.001051: approx 95147478 ticks/sec
INFO     arctic.tickstore.tickstore:tickstore.py:355 Got data in 0.004655 secs, creating DataFrame...
INFO     arctic.tickstore.tickstore:tickstore.py:364 6 rows in 0.005995 secs: 1000 ticks/sec
--------------------------- Captured stderr teardown ---------------------------
2021-01-28 02:30:54,685 DEBUG pytest_server_fixtures.serverclass.thread Killing process tree for 31432 (total_procs_to_kill=1)
2021-01-28 02:30:54,686 DEBUG pytest_server_fixtures.serverclass.thread Killing 1 processes with signal Signals.SIGKILL
2021-01-28 02:30:54,686 DEBUG pytest_server_fixtures.serverclass.thread Waiting for 1 processes to die
2021-01-28 02:30:54,690 DEBUG pytest_server_fixtures.serverclass.thread All processes are terminated
2021-01-28 02:30:54,691 DEBUG pytest_shutil.workspace 
2021-01-28 02:30:54,691 DEBUG pytest_shutil.workspace =======================================================
2021-01-28 02:30:54,691 DEBUG pytest_shutil.workspace pytest_shutil deleting workspace /tmp/tmpizx7gwmy
2021-01-28 02:30:54,691 DEBUG pytest_shutil.workspace =======================================================
2021-01-28 02:30:54,691 DEBUG pytest_shutil.workspace 
---------------------------- Captured log teardown -----------------------------
DEBUG    pytest_server_fixtures.serverclass.thread:thread.py:54 Killing process tree for 31432 (total_procs_to_kill=1)
DEBUG    pytest_server_fixtures.serverclass.thread:thread.py:35 Killing 1 processes with signal Signals.SIGKILL
DEBUG    pytest_server_fixtures.serverclass.thread:thread.py:39 Waiting for 1 processes to die
DEBUG    pytest_server_fixtures.serverclass.thread:thread.py:43 All processes are terminated
DEBUG    pytest_shutil.workspace:workspace.py:140 
DEBUG    pytest_shutil.workspace:workspace.py:141 =======================================================
DEBUG    pytest_shutil.workspace:workspace.py:142 pytest_shutil deleting workspace /tmp/tmpizx7gwmy
DEBUG    pytest_shutil.workspace:workspace.py:143 =======================================================
DEBUG    pytest_shutil.workspace:workspace.py:144
________________ test_should_write_top_level_with_list_of_dicts ________________
arctic = <Arctic at 0x7ffad2cb8390, connected to MongoClient(host=['127.128.125.181:26135'], document_class=dict, tz_aware=False, connect=True)>
    def test_should_write_top_level_with_list_of_dicts(arctic):
        arctic.initialize_library('FEED_2010.LEVEL1', tickstore.TICK_STORE_TYPE)
        arctic.initialize_library('FEED_2011.LEVEL1', tickstore.TICK_STORE_TYPE)
        arctic.initialize_library('FEED.LEVEL1', toplevel.TICK_STORE_TYPE)
        toplevel_tickstore = arctic['FEED.LEVEL1']
        dates = pd.date_range('20101201', periods=57, tz=mktz('Europe/London'))
        data = [{'index': dates[i], 'a': i} for i in range(len(dates))]
        expected = pd.DataFrame(np.arange(57, dtype=np.float64), index=dates, columns=list('a'))
        toplevel_tickstore.write('blah', data)
        res = toplevel_tickstore.read('blah', DateRange(start=dt(2010, 12, 1), end=dt(2011, 2, 1)), columns=list('a'))
>       assert_frame_equal(expected, res.tz_convert(mktz('Europe/London')))
E       AssertionError: (<Day>, None)
tests/integration/tickstore/test_toplevel.py:197: AssertionError
---------------------------- Captured stdout setup -----------------------------
2021-01-28T02:31:03.227+0000 I CONTROL  [main] Automatically disabling TLS 1.0, to force-enable TLS 1.0 specify --sslDisabledProtocols 'none'
2021-01-28T02:31:03.230+0000 I CONTROL  [initandlisten] MongoDB starting : pid=31782 port=26135 dbpath=/tmp/tmpdd8q2_hy 64-bit host=travis-job-37fb2906-cc17-4971-b5d1-b8c0f1c59a89
2021-01-28T02:31:03.230+0000 I CONTROL  [initandlisten] db version v4.0.19
2021-01-28T02:31:03.230+0000 I CONTROL  [initandlisten] git version: 7e28f4296a04d858a2e3dd84a1e79c9ba59a9568
2021-01-28T02:31:03.230+0000 I CONTROL  [initandlisten] OpenSSL version: OpenSSL 1.0.2g  1 Mar 2016
2021-01-28T02:31:03.230+0000 I CONTROL  [initandlisten] allocator: tcmalloc
2021-01-28T02:31:03.230+0000 I CONTROL  [initandlisten] modules: none
2021-01-28T02:31:03.230+0000 I CONTROL  [initandlisten] build environment:
2021-01-28T02:31:03.230+0000 I CONTROL  [initandlisten]     distmod: ubuntu1604
2021-01-28T02:31:03.230+0000 I CONTROL  [initandlisten]     distarch: x86_64
2021-01-28T02:31:03.230+0000 I CONTROL  [initandlisten]     target_arch: x86_64
2021-01-28T02:31:03.230+0000 I CONTROL  [initandlisten] options: { net: { bindIp: "127.128.125.181", port: 26135, unixDomainSocket: { enabled: false } }, storage: { dbPath: "/tmp/tmpdd8q2_hy", journal: { enabled: false }, syncPeriodSecs: 0.0 }, systemLog: { quiet: true } }
2021-01-28T02:31:03.230+0000 I STORAGE  [initandlisten] 
2021-01-28T02:31:03.230+0000 I STORAGE  [initandlisten] ** WARNING: Using the XFS filesystem is strongly recommended with the WiredTiger storage engine
2021-01-28T02:31:03.230+0000 I STORAGE  [initandlisten] **          See http://dochub.mongodb.org/core/prodnotes-filesystem
2021-01-28T02:31:03.230+0000 I STORAGE  [initandlisten] wiredtiger_open config: create,cache_size=3476M,cache_overflow=(file_max=0M),session_max=20000,eviction=(threads_min=4,threads_max=4),config_base=false,statistics=(fast),log=(enabled=true,archive=true,path=journal,compressor=snappy),file_manager=(close_idle_time=100000),statistics_log=(wait=0),verbose=(recovery_progress),,log=(enabled=false),
2021-01-28T02:31:03.725+0000 I STORAGE  [initandlisten] WiredTiger message [1611801063:725201][31782:0x7ffba6deda80], txn-recover: Set global recovery timestamp: 0
2021-01-28T02:31:03.736+0000 I RECOVERY [initandlisten] WiredTiger recoveryTimestamp. Ts: Timestamp(0, 0)
2021-01-28T02:31:03.758+0000 I CONTROL  [initandlisten] 
2021-01-28T02:31:03.758+0000 I CONTROL  [initandlisten] ** WARNING: Access control is not enabled for the database.
2021-01-28T02:31:03.758+0000 I CONTROL  [initandlisten] **          Read and write access to data and configuration is unrestricted.
2021-01-28T02:31:03.758+0000 I CONTROL  [initandlisten] 
2021-01-28T02:31:03.759+0000 I STORAGE  [initandlisten] createCollection: admin.system.version with provided UUID: 6c6efc63-06fa-4372-90b9-69ececb0b5aa
2021-01-28T02:31:03.776+0000 I SHARDING [initandlisten] Marking collection admin.system.version as collection version: <unsharded>
2021-01-28T02:31:03.776+0000 I COMMAND  [initandlisten] setting featureCompatibilityVersion to 4.0
2021-01-28T02:31:03.776+0000 I SHARDING [initandlisten] Marking collection local.system.replset as collection version: <unsharded>
2021-01-28T02:31:03.777+0000 I SHARDING [initandlisten] Marking collection admin.system.roles as collection version: <unsharded>
2021-01-28T02:31:03.777+0000 I STORAGE  [initandlisten] createCollection: local.startup_log with generated UUID: ce09c649-8594-411a-86c1-1dd04da5db65
2021-01-28T02:31:03.795+0000 I SHARDING [initandlisten] Marking collection local.startup_log as collection version: <unsharded>
2021-01-28T02:31:03.795+0000 I FTDC     [initandlisten] Initializing full-time diagnostic data capture with directory '/tmp/tmpdd8q2_hy/diagnostic.data'
2021-01-28T02:31:03.796+0000 I NETWORK  [initandlisten] waiting for connections on port 26135
2021-01-28T02:31:03.796+0000 I SHARDING [LogicalSessionCacheRefresh] Marking collection config.system.sessions as collection version: <unsharded>
2021-01-28T02:31:03.796+0000 I STORAGE  [LogicalSessionCacheRefresh] createCollection: config.system.sessions with generated UUID: 6de3ac7f-9d85-4dce-ad16-a17fa2492434
2021-01-28T02:31:03.796+0000 I CONTROL  [LogicalSessionCacheReap] Sessions collection is not set up; waiting until next sessions reap interval: config.system.sessions does not exist
2021-01-28T02:31:03.823+0000 I NETWORK  [conn1] received client metadata from 127.0.0.1:47140 conn1: { driver: { name: "PyMongo", version: "3.11.2" }, os: { type: "Linux", name: "Linux", architecture: "x86_64", version: "4.15.0-1077-gcp" }, platform: "CPython 3.6.7.final.0" }
2021-01-28T02:31:03.824+0000 I INDEX    [LogicalSessionCacheRefresh] build index on: config.system.sessions properties: { v: 2, key: { lastUse: 1 }, name: "lsidTTLIndex", ns: "config.system.sessions", expireAfterSeconds: 1800 }
2021-01-28T02:31:03.824+0000 I INDEX    [LogicalSessionCacheRefresh] 	 building index using bulk method; build may temporarily use up to 500 megabytes of RAM
2021-01-28T02:31:03.824+0000 I INDEX    [LogicalSessionCacheRefresh] build index done.  scanned 0 total records. 0 secs
2021-01-28T02:31:03.825+0000 I NETWORK  [conn2] received client metadata from 127.0.0.1:47142 conn2: { driver: { name: "PyMongo", version: "3.11.2" }, os: { type: "Linux", name: "Linux", architecture: "x86_64", version: "4.15.0-1077-gcp" }, platform: "CPython 3.6.7.final.0" }
2021-01-28T02:31:03.828+0000 I NETWORK  [conn3] received client metadata from 127.0.0.1:47144 conn3: { driver: { name: "PyMongo", version: "3.11.2" }, os: { type: "Linux", name: "Linux", architecture: "x86_64", version: "4.15.0-1077-gcp" }, platform: "CPython 3.6.7.final.0" }
2021-01-28T02:31:03.831+0000 I NETWORK  [conn4] received client metadata from 127.0.0.1:47146 conn4: { driver: { name: "PyMongo", version: "3.11.2" }, os: { type: "Linux", name: "Linux", architecture: "x86_64", version: "4.15.0-1077-gcp" }, platform: "CPython 3.6.7.final.0" }
2021-01-28T02:31:03.835+0000 I SHARDING [conn4] Marking collection meta_db.cache as collection version: <unsharded>
2021-01-28T02:31:03.835+0000 I STORAGE  [conn4] createCollection: meta_db.cache with generated UUID: 386330fd-76b0-48aa-b76f-6381f181cdf4
2021-01-28T02:31:03.863+0000 I INDEX    [conn4] build index on: meta_db.cache properties: { v: 2, key: { date: 1 }, name: "date_1", ns: "meta_db.cache", expireAfterSeconds: 3600 }
2021-01-28T02:31:03.864+0000 I INDEX    [conn4] 	 building index using bulk method; build may temporarily use up to 500 megabytes of RAM
2021-01-28T02:31:03.864+0000 W STORAGE  [conn4] failed to create WiredTiger bulk cursor: Device or resource busy
2021-01-28T02:31:03.864+0000 W STORAGE  [conn4] falling back to non-bulk cursor for index table:index-9--6347060631112427169
2021-01-28T02:31:03.864+0000 I INDEX    [conn4] build index done.  scanned 0 total records. 0 secs
---------------------------- Captured stderr setup -----------------------------
2021-01-28 02:31:03,202 DEBUG pytest_shutil.workspace 
2021-01-28 02:31:03,202 DEBUG pytest_shutil.workspace =======================================================
2021-01-28 02:31:03,202 DEBUG pytest_shutil.workspace pytest_shutil created workspace /tmp/tmpdd8q2_hy
2021-01-28 02:31:03,202 DEBUG pytest_shutil.workspace This workspace will delete itself on teardown
2021-01-28 02:31:03,202 DEBUG pytest_shutil.workspace =======================================================
2021-01-28 02:31:03,202 DEBUG pytest_shutil.workspace 
2021-01-28 02:31:03,203 DEBUG pytest_server_fixtures.serverclass.thread Launching thread server.
2021-01-28 02:31:03,212 DEBUG pytest_server_fixtures.serverclass.thread Running server: mongod --bind_ip=127.128.125.181 --port=26135 --nounixsocket --syncdelay=0 --nojournal --quiet --dbpath=/tmp/tmpdd8q2_hy
2021-01-28 02:31:03,213 DEBUG pytest_server_fixtures.serverclass.thread CWD: /home/travis/build/man-group/arctic
2021-01-28 02:31:03,213 DEBUG pytest_server_fixtures.base2 sleeping for 0.1 before retrying (1 of 28)
2021-01-28 02:31:03,214 INFO pytest_server_fixtures.mongo Connecting to Mongo at 127.128.125.181:26135
2021-01-28 02:31:03,820 DEBUG pytest_server_fixtures.base2 sleeping for 0.1 before retrying (2 of 28)
2021-01-28 02:31:03,820 INFO pytest_server_fixtures.mongo Connecting to Mongo at 127.128.125.181:26135
2021-01-28 02:31:03,829 DEBUG pytest_server_fixtures.base2 waited 0:00:00.615814 for server to start successfully
2021-01-28 02:31:03,830 DEBUG pytest_server_fixtures.base2 Server now awake
2021-01-28 02:31:03,830 INFO arctic.fixtures.arctic arctic.fixtures: arctic init()
------------------------------ Captured log setup ------------------------------
DEBUG    pytest_shutil.workspace:workspace.py:52 
DEBUG    pytest_shutil.workspace:workspace.py:53 =======================================================
DEBUG    pytest_shutil.workspace:workspace.py:56 pytest_shutil created workspace /tmp/tmpdd8q2_hy
DEBUG    pytest_shutil.workspace:workspace.py:64 This workspace will delete itself on teardown
DEBUG    pytest_shutil.workspace:workspace.py:65 =======================================================
DEBUG    pytest_shutil.workspace:workspace.py:66 
DEBUG    pytest_server_fixtures.serverclass.thread:thread.py:77 Launching thread server.
DEBUG    pytest_server_fixtures.serverclass.thread:thread.py:89 Running server: mongod --bind_ip=127.128.125.181 --port=26135 --nounixsocket --syncdelay=0 --nojournal --quiet --dbpath=/tmp/tmpdd8q2_hy
DEBUG    pytest_server_fixtures.serverclass.thread:thread.py:90 CWD: /home/travis/build/man-group/arctic
DEBUG    pytest_server_fixtures.base2:base2.py:226 sleeping for 0.1 before retrying (1 of 28)
INFO     pytest_server_fixtures.mongo:mongo.py:128 Connecting to Mongo at 127.128.125.181:26135
DEBUG    pytest_server_fixtures.base2:base2.py:226 sleeping for 0.1 before retrying (2 of 28)
INFO     pytest_server_fixtures.mongo:mongo.py:128 Connecting to Mongo at 127.128.125.181:26135
DEBUG    pytest_server_fixtures.base2:base2.py:229 waited 0:00:00.615814 for server to start successfully
DEBUG    pytest_server_fixtures.base2:base2.py:69 Server now awake
INFO     arctic.fixtures.arctic:arctic.py:23 arctic.fixtures: arctic init()
----------------------------- Captured stdout call -----------------------------
2021-01-28T02:31:03.867+0000 I SHARDING [conn4] Marking collection arctic_FEED_2010.LEVEL1.ARCTIC as collection version: <unsharded>
2021-01-28T02:31:03.867+0000 I STORAGE  [conn4] createCollection: arctic_FEED_2010.LEVEL1.ARCTIC with generated UUID: 47c2cc3d-c238-4487-80ba-6fbdc4c8dc2a
2021-01-28T02:31:03.885+0000 I STORAGE  [conn4] createCollection: arctic_FEED_2010.LEVEL1 with generated UUID: f253f048-79b9-47c0-992f-71b7db703043
2021-01-28T02:31:03.919+0000 I INDEX    [conn4] build index on: arctic_FEED_2010.LEVEL1 properties: { v: 2, key: { sy: 1, s: 1 }, name: "sy_1_s_1", ns: "arctic_FEED_2010.LEVEL1", background: true }
2021-01-28T02:31:03.919+0000 I INDEX    [conn4] build index done.  scanned 0 total records. 0 secs
2021-01-28T02:31:03.931+0000 I INDEX    [conn4] build index on: arctic_FEED_2010.LEVEL1 properties: { v: 2, key: { s: 1 }, name: "s_1", ns: "arctic_FEED_2010.LEVEL1", background: true }
2021-01-28T02:31:03.931+0000 I INDEX    [conn4] build index done.  scanned 0 total records. 0 secs
2021-01-28T02:31:03.932+0000 I STORAGE  [conn4] createCollection: arctic_FEED_2010.LEVEL1.metadata with generated UUID: 341878e0-8311-45b5-a82e-6b0a5666d3bc
2021-01-28T02:31:03.950+0000 I SHARDING [conn4] Marking collection arctic_FEED_2010.LEVEL1.metadata as collection version: <unsharded>
2021-01-28T02:31:03.960+0000 I INDEX    [conn4] build index on: arctic_FEED_2010.LEVEL1.metadata properties: { v: 2, unique: true, key: { sy: 1 }, name: "sy_1", ns: "arctic_FEED_2010.LEVEL1.metadata", background: true }
2021-01-28T02:31:03.960+0000 I INDEX    [conn4] build index done.  scanned 0 total records. 0 secs
2021-01-28T02:31:03.966+0000 I SHARDING [conn4] Marking collection arctic_FEED_2011.LEVEL1.ARCTIC as collection version: <unsharded>
2021-01-28T02:31:03.966+0000 I STORAGE  [conn4] createCollection: arctic_FEED_2011.LEVEL1.ARCTIC with generated UUID: c1c8492e-921b-44c8-9571-28f2e24a2936
2021-01-28T02:31:03.984+0000 I STORAGE  [conn4] createCollection: arctic_FEED_2011.LEVEL1 with generated UUID: fd2516a6-382a-43e2-8d7a-e30afff2a03d
2021-01-28T02:31:04.001+0000 I SHARDING [ftdc] Marking collection local.oplog.rs as collection version: <unsharded>
2021-01-28T02:31:04.018+0000 I INDEX    [conn4] build index on: arctic_FEED_2011.LEVEL1 properties: { v: 2, key: { sy: 1, s: 1 }, name: "sy_1_s_1", ns: "arctic_FEED_2011.LEVEL1", background: true }
2021-01-28T02:31:04.018+0000 I INDEX    [conn4] build index done.  scanned 0 total records. 0 secs
2021-01-28T02:31:04.028+0000 I INDEX    [conn4] build index on: arctic_FEED_2011.LEVEL1 properties: { v: 2, key: { s: 1 }, name: "s_1", ns: "arctic_FEED_2011.LEVEL1", background: true }
2021-01-28T02:31:04.028+0000 I INDEX    [conn4] build index done.  scanned 0 total records. 0 secs
2021-01-28T02:31:04.030+0000 I STORAGE  [conn4] createCollection: arctic_FEED_2011.LEVEL1.metadata with generated UUID: 5f8eaaa2-ae9a-4cba-9ca5-48e69cd0bf16
2021-01-28T02:31:04.048+0000 I SHARDING [conn4] Marking collection arctic_FEED_2011.LEVEL1.metadata as collection version: <unsharded>
2021-01-28T02:31:04.058+0000 I INDEX    [conn4] build index on: arctic_FEED_2011.LEVEL1.metadata properties: { v: 2, unique: true, key: { sy: 1 }, name: "sy_1", ns: "arctic_FEED_2011.LEVEL1.metadata", background: true }
2021-01-28T02:31:04.058+0000 I INDEX    [conn4] build index done.  scanned 0 total records. 0 secs
2021-01-28T02:31:04.063+0000 I SHARDING [conn4] Marking collection arctic_FEED.LEVEL1.ARCTIC as collection version: <unsharded>
2021-01-28T02:31:04.063+0000 I STORAGE  [conn4] createCollection: arctic_FEED.LEVEL1.ARCTIC with generated UUID: 5b9b1088-f0a1-48f6-9bbe-91b439ac7688
2021-01-28T02:31:04.079+0000 I SHARDING [conn4] Marking collection meta_db.settings as collection version: <unsharded>
2021-01-28T02:31:04.083+0000 I SHARDING [conn4] Marking collection arctic_FEED.LEVEL1 as collection version: <unsharded>
2021-01-28T02:31:04.084+0000 I STORAGE  [conn4] createCollection: arctic_FEED.LEVEL1 with generated UUID: 2c79d9bb-95ff-4dc9-9578-1ac6830ce548
2021-01-28T02:31:04.124+0000 I INDEX    [conn4] build index on: arctic_FEED.LEVEL1 properties: { v: 2, key: { start: 1 }, name: "start_1", ns: "arctic_FEED.LEVEL1", background: true }
2021-01-28T02:31:04.124+0000 I INDEX    [conn4] build index done.  scanned 2 total records. 0 secs
2021-01-28T02:31:04.133+0000 I SHARDING [conn4] Marking collection arctic_FEED_2010.LEVEL1 as collection version: <unsharded>
2021-01-28T02:31:04.142+0000 I SHARDING [conn4] Marking collection arctic_FEED_2011.LEVEL1 as collection version: <unsharded>
----------------------------- Captured stderr call -----------------------------
2021-01-28 02:31:04,140 DEBUG arctic.tickstore.tickstore 1 buckets in 0.00306: approx 32679738 ticks/sec
2021-01-28 02:31:04,146 DEBUG arctic.tickstore.tickstore 1 buckets in 0.001162: approx 86058519 ticks/sec
2021-01-28 02:31:04,153 INFO arctic.tickstore.tickstore Got data in 0.00493 secs, creating DataFrame...
2021-01-28 02:31:04,154 INFO arctic.tickstore.tickstore 31 rows in 0.006173 secs: 5021 ticks/sec
2021-01-28 02:31:04,159 INFO arctic.tickstore.tickstore Got data in 0.004338 secs, creating DataFrame...
2021-01-28 02:31:04,160 INFO arctic.tickstore.tickstore 26 rows in 0.005439 secs: 4780 ticks/sec
------------------------------ Captured log call -------------------------------
DEBUG    arctic.tickstore.tickstore:tickstore.py:612 1 buckets in 0.00306: approx 32679738 ticks/sec
DEBUG    arctic.tickstore.tickstore:tickstore.py:612 1 buckets in 0.001162: approx 86058519 ticks/sec
INFO     arctic.tickstore.tickstore:tickstore.py:355 Got data in 0.00493 secs, creating DataFrame...
INFO     arctic.tickstore.tickstore:tickstore.py:364 31 rows in 0.006173 secs: 5021 ticks/sec
INFO     arctic.tickstore.tickstore:tickstore.py:355 Got data in 0.004338 secs, creating DataFrame...
INFO     arctic.tickstore.tickstore:tickstore.py:364 26 rows in 0.005439 secs: 4780 ticks/sec
--------------------------- Captured stderr teardown ---------------------------
2021-01-28 02:31:04,192 DEBUG pytest_server_fixtures.serverclass.thread Killing process tree for 31782 (total_procs_to_kill=1)
2021-01-28 02:31:04,193 DEBUG pytest_server_fixtures.serverclass.thread Killing 1 processes with signal Signals.SIGKILL
2021-01-28 02:31:04,196 DEBUG pytest_server_fixtures.serverclass.thread Waiting for 1 processes to die
2021-01-28 02:31:04,197 DEBUG pytest_server_fixtures.serverclass.thread All processes are terminated
2021-01-28 02:31:04,197 DEBUG pytest_shutil.workspace 
2021-01-28 02:31:04,197 DEBUG pytest_shutil.workspace =======================================================
2021-01-28 02:31:04,197 DEBUG pytest_shutil.workspace pytest_shutil deleting workspace /tmp/tmpdd8q2_hy
2021-01-28 02:31:04,197 DEBUG pytest_shutil.workspace =======================================================
2021-01-28 02:31:04,197 DEBUG pytest_shutil.workspace 
---------------------------- Captured log teardown -----------------------------
DEBUG    pytest_server_fixtures.serverclass.thread:thread.py:54 Killing process tree for 31782 (total_procs_to_kill=1)
DEBUG    pytest_server_fixtures.serverclass.thread:thread.py:35 Killing 1 processes with signal Signals.SIGKILL
DEBUG    pytest_server_fixtures.serverclass.thread:thread.py:39 Waiting for 1 processes to die
DEBUG    pytest_server_fixtures.serverclass.thread:thread.py:43 All processes are terminated
DEBUG    pytest_shutil.workspace:workspace.py:140 
DEBUG    pytest_shutil.workspace:workspace.py:141 =======================================================
DEBUG    pytest_shutil.workspace:workspace.py:142 pytest_shutil deleting workspace /tmp/tmpdd8q2_hy
DEBUG    pytest_shutil.workspace:workspace.py:143 =======================================================
DEBUG    pytest_shutil.workspace:workspace.py:144
______________ test_should_write_top_level_with_correct_timezone _______________
arctic = <Arctic at 0x7ffad28b89e8, connected to MongoClient(host=['127.128.125.181:21725'], document_class=dict, tz_aware=False, connect=True)>
    def test_should_write_top_level_with_correct_timezone(arctic):
        # Write timezone aware data and read back in UTC
        utc = mktz('UTC')
        arctic.initialize_library('FEED_2010.LEVEL1', tickstore.TICK_STORE_TYPE)
        arctic.initialize_library('FEED_2011.LEVEL1', tickstore.TICK_STORE_TYPE)
        arctic.initialize_library('FEED.LEVEL1', toplevel.TICK_STORE_TYPE)
        toplevel_tickstore = arctic['FEED.LEVEL1']
        dates = pd.date_range('20101230220000', periods=10, tz=mktz('America/New_York'))  # 10pm New York time is 3am next day UTC
        data = [{'index': dates[i], 'a': i} for i in range(len(dates))]
        expected = pd.DataFrame(np.arange(len(dates), dtype=np.float64), index=dates.tz_convert(utc), columns=list('a'))
        toplevel_tickstore.write('blah', data)
        res = toplevel_tickstore.read('blah', DateRange(start=dt(2010, 1, 1), end=dt(2011, 12, 31)), columns=list('a')).tz_convert(utc)
>       assert_frame_equal(expected, res)
E       AssertionError: (<Day>, None)
tests/integration/tickstore/test_toplevel.py:215: AssertionError
---------------------------- Captured stdout setup -----------------------------
2021-01-28T02:31:04.226+0000 I CONTROL  [main] Automatically disabling TLS 1.0, to force-enable TLS 1.0 specify --sslDisabledProtocols 'none'
2021-01-28T02:31:04.228+0000 I CONTROL  [initandlisten] MongoDB starting : pid=31817 port=21725 dbpath=/tmp/tmp20m0drzy 64-bit host=travis-job-37fb2906-cc17-4971-b5d1-b8c0f1c59a89
2021-01-28T02:31:04.228+0000 I CONTROL  [initandlisten] db version v4.0.19
2021-01-28T02:31:04.229+0000 I CONTROL  [initandlisten] git version: 7e28f4296a04d858a2e3dd84a1e79c9ba59a9568
2021-01-28T02:31:04.229+0000 I CONTROL  [initandlisten] OpenSSL version: OpenSSL 1.0.2g  1 Mar 2016
2021-01-28T02:31:04.229+0000 I CONTROL  [initandlisten] allocator: tcmalloc
2021-01-28T02:31:04.229+0000 I CONTROL  [initandlisten] modules: none
2021-01-28T02:31:04.229+0000 I CONTROL  [initandlisten] build environment:
2021-01-28T02:31:04.229+0000 I CONTROL  [initandlisten]     distmod: ubuntu1604
2021-01-28T02:31:04.229+0000 I CONTROL  [initandlisten]     distarch: x86_64
2021-01-28T02:31:04.229+0000 I CONTROL  [initandlisten]     target_arch: x86_64
2021-01-28T02:31:04.229+0000 I CONTROL  [initandlisten] options: { net: { bindIp: "127.128.125.181", port: 21725, unixDomainSocket: { enabled: false } }, storage: { dbPath: "/tmp/tmp20m0drzy", journal: { enabled: false }, syncPeriodSecs: 0.0 }, systemLog: { quiet: true } }
2021-01-28T02:31:04.229+0000 I STORAGE  [initandlisten] 
2021-01-28T02:31:04.229+0000 I STORAGE  [initandlisten] ** WARNING: Using the XFS filesystem is strongly recommended with the WiredTiger storage engine
2021-01-28T02:31:04.229+0000 I STORAGE  [initandlisten] **          See http://dochub.mongodb.org/core/prodnotes-filesystem
2021-01-28T02:31:04.229+0000 I STORAGE  [initandlisten] wiredtiger_open config: create,cache_size=3476M,cache_overflow=(file_max=0M),session_max=20000,eviction=(threads_min=4,threads_max=4),config_base=false,statistics=(fast),log=(enabled=true,archive=true,path=journal,compressor=snappy),file_manager=(close_idle_time=100000),statistics_log=(wait=0),verbose=(recovery_progress),,log=(enabled=false),
2021-01-28T02:31:04.729+0000 I STORAGE  [initandlisten] WiredTiger message [1611801064:729931][31817:0x7fc29db65a80], txn-recover: Set global recovery timestamp: 0
2021-01-28T02:31:04.742+0000 I RECOVERY [initandlisten] WiredTiger recoveryTimestamp. Ts: Timestamp(0, 0)
2021-01-28T02:31:04.766+0000 I CONTROL  [initandlisten] 
2021-01-28T02:31:04.766+0000 I CONTROL  [initandlisten] ** WARNING: Access control is not enabled for the database.
2021-01-28T02:31:04.766+0000 I CONTROL  [initandlisten] **          Read and write access to data and configuration is unrestricted.
2021-01-28T02:31:04.766+0000 I CONTROL  [initandlisten] 
2021-01-28T02:31:04.766+0000 I STORAGE  [initandlisten] createCollection: admin.system.version with provided UUID: c74f1db3-8725-4746-bdf2-ec155ecad001
2021-01-28T02:31:04.784+0000 I SHARDING [initandlisten] Marking collection admin.system.version as collection version: <unsharded>
2021-01-28T02:31:04.784+0000 I COMMAND  [initandlisten] setting featureCompatibilityVersion to 4.0
2021-01-28T02:31:04.784+0000 I SHARDING [initandlisten] Marking collection local.system.replset as collection version: <unsharded>
2021-01-28T02:31:04.784+0000 I SHARDING [initandlisten] Marking collection admin.system.roles as collection version: <unsharded>
2021-01-28T02:31:04.784+0000 I STORAGE  [initandlisten] createCollection: local.startup_log with generated UUID: f911d7e7-17f1-48ed-9e40-31cc588328ab
2021-01-28T02:31:04.801+0000 I SHARDING [initandlisten] Marking collection local.startup_log as collection version: <unsharded>
2021-01-28T02:31:04.801+0000 I FTDC     [initandlisten] Initializing full-time diagnostic data capture with directory '/tmp/tmp20m0drzy/diagnostic.data'
2021-01-28T02:31:04.803+0000 I NETWORK  [initandlisten] waiting for connections on port 21725
2021-01-28T02:31:04.803+0000 I SHARDING [LogicalSessionCacheRefresh] Marking collection config.system.sessions as collection version: <unsharded>
2021-01-28T02:31:04.803+0000 I CONTROL  [LogicalSessionCacheReap] Sessions collection is not set up; waiting until next sessions reap interval: config.system.sessions does not exist
2021-01-28T02:31:04.803+0000 I STORAGE  [LogicalSessionCacheRefresh] createCollection: config.system.sessions with generated UUID: a4a39092-b3ae-4210-a10c-9627f2cffc73
2021-01-28T02:31:04.823+0000 I NETWORK  [conn1] received client metadata from 127.0.0.1:41776 conn1: { driver: { name: "PyMongo", version: "3.11.2" }, os: { type: "Linux", name: "Linux", architecture: "x86_64", version: "4.15.0-1077-gcp" }, platform: "CPython 3.6.7.final.0" }
2021-01-28T02:31:04.824+0000 I NETWORK  [conn2] received client metadata from 127.0.0.1:41778 conn2: { driver: { name: "PyMongo", version: "3.11.2" }, os: { type: "Linux", name: "Linux", architecture: "x86_64", version: "4.15.0-1077-gcp" }, platform: "CPython 3.6.7.final.0" }
2021-01-28T02:31:04.828+0000 I NETWORK  [conn3] received client metadata from 127.0.0.1:41780 conn3: { driver: { name: "PyMongo", version: "3.11.2" }, os: { type: "Linux", name: "Linux", architecture: "x86_64", version: "4.15.0-1077-gcp" }, platform: "CPython 3.6.7.final.0" }
2021-01-28T02:31:04.830+0000 I NETWORK  [conn4] received client metadata from 127.0.0.1:41782 conn4: { driver: { name: "PyMongo", version: "3.11.2" }, os: { type: "Linux", name: "Linux", architecture: "x86_64", version: "4.15.0-1077-gcp" }, platform: "CPython 3.6.7.final.0" }
2021-01-28T02:31:04.833+0000 I INDEX    [LogicalSessionCacheRefresh] build index on: config.system.sessions properties: { v: 2, key: { lastUse: 1 }, name: "lsidTTLIndex", ns: "config.system.sessions", expireAfterSeconds: 1800 }
2021-01-28T02:31:04.833+0000 I INDEX    [LogicalSessionCacheRefresh] 	 building index using bulk method; build may temporarily use up to 500 megabytes of RAM
2021-01-28T02:31:04.833+0000 W STORAGE  [LogicalSessionCacheRefresh] failed to create WiredTiger bulk cursor: Device or resource busy
2021-01-28T02:31:04.833+0000 W STORAGE  [LogicalSessionCacheRefresh] falling back to non-bulk cursor for index table:index-6--6038298779720906461
2021-01-28T02:31:04.833+0000 I INDEX    [LogicalSessionCacheRefresh] build index done.  scanned 0 total records. 0 secs
2021-01-28T02:31:04.836+0000 I SHARDING [conn4] Marking collection meta_db.cache as collection version: <unsharded>
2021-01-28T02:31:04.836+0000 I STORAGE  [conn4] createCollection: meta_db.cache with generated UUID: dbde6eda-fa08-49a8-a8da-4bf6a69686ab
2021-01-28T02:31:04.866+0000 I INDEX    [conn4] build index on: meta_db.cache properties: { v: 2, key: { date: 1 }, name: "date_1", ns: "meta_db.cache", expireAfterSeconds: 3600 }
2021-01-28T02:31:04.866+0000 I INDEX    [conn4] 	 building index using bulk method; build may temporarily use up to 500 megabytes of RAM
2021-01-28T02:31:04.866+0000 W STORAGE  [conn4] failed to create WiredTiger bulk cursor: Device or resource busy
2021-01-28T02:31:04.866+0000 W STORAGE  [conn4] falling back to non-bulk cursor for index table:index-9--6038298779720906461
2021-01-28T02:31:04.866+0000 I INDEX    [conn4] build index done.  scanned 0 total records. 0 secs
---------------------------- Captured stderr setup -----------------------------
2021-01-28 02:31:04,200 DEBUG pytest_shutil.workspace 
2021-01-28 02:31:04,201 DEBUG pytest_shutil.workspace =======================================================
2021-01-28 02:31:04,201 DEBUG pytest_shutil.workspace pytest_shutil created workspace /tmp/tmp20m0drzy
2021-01-28 02:31:04,201 DEBUG pytest_shutil.workspace This workspace will delete itself on teardown
2021-01-28 02:31:04,201 DEBUG pytest_shutil.workspace =======================================================
2021-01-28 02:31:04,201 DEBUG pytest_shutil.workspace 
2021-01-28 02:31:04,201 DEBUG pytest_server_fixtures.serverclass.thread Launching thread server.
2021-01-28 02:31:04,211 DEBUG pytest_server_fixtures.serverclass.thread Running server: mongod --bind_ip=127.128.125.181 --port=21725 --nounixsocket --syncdelay=0 --nojournal --quiet --dbpath=/tmp/tmp20m0drzy
2021-01-28 02:31:04,212 DEBUG pytest_server_fixtures.serverclass.thread CWD: /home/travis/build/man-group/arctic
2021-01-28 02:31:04,212 DEBUG pytest_server_fixtures.base2 sleeping for 0.1 before retrying (1 of 28)
2021-01-28 02:31:04,213 INFO pytest_server_fixtures.mongo Connecting to Mongo at 127.128.125.181:21725
2021-01-28 02:31:04,818 DEBUG pytest_server_fixtures.base2 sleeping for 0.1 before retrying (2 of 28)
2021-01-28 02:31:04,819 INFO pytest_server_fixtures.mongo Connecting to Mongo at 127.128.125.181:21725
2021-01-28 02:31:04,828 DEBUG pytest_server_fixtures.base2 waited 0:00:00.616109 for server to start successfully
2021-01-28 02:31:04,829 DEBUG pytest_server_fixtures.base2 Server now awake
2021-01-28 02:31:04,829 INFO arctic.fixtures.arctic arctic.fixtures: arctic init()
------------------------------ Captured log setup ------------------------------
DEBUG    pytest_shutil.workspace:workspace.py:52 
DEBUG    pytest_shutil.workspace:workspace.py:53 =======================================================
DEBUG    pytest_shutil.workspace:workspace.py:56 pytest_shutil created workspace /tmp/tmp20m0drzy
DEBUG    pytest_shutil.workspace:workspace.py:64 This workspace will delete itself on teardown
DEBUG    pytest_shutil.workspace:workspace.py:65 =======================================================
DEBUG    pytest_shutil.workspace:workspace.py:66 
DEBUG    pytest_server_fixtures.serverclass.thread:thread.py:77 Launching thread server.
DEBUG    pytest_server_fixtures.serverclass.thread:thread.py:89 Running server: mongod --bind_ip=127.128.125.181 --port=21725 --nounixsocket --syncdelay=0 --nojournal --quiet --dbpath=/tmp/tmp20m0drzy
DEBUG    pytest_server_fixtures.serverclass.thread:thread.py:90 CWD: /home/travis/build/man-group/arctic
DEBUG    pytest_server_fixtures.base2:base2.py:226 sleeping for 0.1 before retrying (1 of 28)
INFO     pytest_server_fixtures.mongo:mongo.py:128 Connecting to Mongo at 127.128.125.181:21725
DEBUG    pytest_server_fixtures.base2:base2.py:226 sleeping for 0.1 before retrying (2 of 28)
INFO     pytest_server_fixtures.mongo:mongo.py:128 Connecting to Mongo at 127.128.125.181:21725
DEBUG    pytest_server_fixtures.base2:base2.py:229 waited 0:00:00.616109 for server to start successfully
DEBUG    pytest_server_fixtures.base2:base2.py:69 Server now awake
INFO     arctic.fixtures.arctic:arctic.py:23 arctic.fixtures: arctic init()
----------------------------- Captured stdout call -----------------------------
2021-01-28T02:31:04.870+0000 I SHARDING [conn4] Marking collection arctic_FEED_2010.LEVEL1.ARCTIC as collection version: <unsharded>
2021-01-28T02:31:04.870+0000 I STORAGE  [conn4] createCollection: arctic_FEED_2010.LEVEL1.ARCTIC with generated UUID: 70b3fdc8-a5d1-4a7b-b7c2-6a8ab2765d59
2021-01-28T02:31:04.888+0000 I STORAGE  [conn4] createCollection: arctic_FEED_2010.LEVEL1 with generated UUID: 2b455a67-1fec-44b4-8129-5474ba13355b
2021-01-28T02:31:04.916+0000 I INDEX    [conn4] build index on: arctic_FEED_2010.LEVEL1 properties: { v: 2, key: { sy: 1, s: 1 }, name: "sy_1_s_1", ns: "arctic_FEED_2010.LEVEL1", background: true }
2021-01-28T02:31:04.916+0000 I INDEX    [conn4] build index done.  scanned 0 total records. 0 secs
2021-01-28T02:31:04.926+0000 I INDEX    [conn4] build index on: arctic_FEED_2010.LEVEL1 properties: { v: 2, key: { s: 1 }, name: "s_1", ns: "arctic_FEED_2010.LEVEL1", background: true }
2021-01-28T02:31:04.926+0000 I INDEX    [conn4] build index done.  scanned 0 total records. 0 secs
2021-01-28T02:31:04.927+0000 I STORAGE  [conn4] createCollection: arctic_FEED_2010.LEVEL1.metadata with generated UUID: ad2d45e3-f100-489e-a2cf-6b275ce8df64
2021-01-28T02:31:04.947+0000 I SHARDING [conn4] Marking collection arctic_FEED_2010.LEVEL1.metadata as collection version: <unsharded>
2021-01-28T02:31:04.958+0000 I INDEX    [conn4] build index on: arctic_FEED_2010.LEVEL1.metadata properties: { v: 2, unique: true, key: { sy: 1 }, name: "sy_1", ns: "arctic_FEED_2010.LEVEL1.metadata", background: true }
2021-01-28T02:31:04.958+0000 I INDEX    [conn4] build index done.  scanned 0 total records. 0 secs
2021-01-28T02:31:04.963+0000 I SHARDING [conn4] Marking collection arctic_FEED_2011.LEVEL1.ARCTIC as collection version: <unsharded>
2021-01-28T02:31:04.963+0000 I STORAGE  [conn4] createCollection: arctic_FEED_2011.LEVEL1.ARCTIC with generated UUID: a2935126-0826-4e10-965e-2e9cdfe00bc7
2021-01-28T02:31:04.983+0000 I STORAGE  [conn4] createCollection: arctic_FEED_2011.LEVEL1 with generated UUID: 1c8babc5-6b0f-4475-9d94-a7dbfe961048
2021-01-28T02:31:05.000+0000 I SHARDING [ftdc] Marking collection local.oplog.rs as collection version: <unsharded>
2021-01-28T02:31:05.016+0000 I INDEX    [conn4] build index on: arctic_FEED_2011.LEVEL1 properties: { v: 2, key: { sy: 1, s: 1 }, name: "sy_1_s_1", ns: "arctic_FEED_2011.LEVEL1", background: true }
2021-01-28T02:31:05.016+0000 I INDEX    [conn4] build index done.  scanned 0 total records. 0 secs
2021-01-28T02:31:05.025+0000 I INDEX    [conn4] build index on: arctic_FEED_2011.LEVEL1 properties: { v: 2, key: { s: 1 }, name: "s_1", ns: "arctic_FEED_2011.LEVEL1", background: true }
2021-01-28T02:31:05.025+0000 I INDEX    [conn4] build index done.  scanned 0 total records. 0 secs
2021-01-28T02:31:05.026+0000 I STORAGE  [conn4] createCollection: arctic_FEED_2011.LEVEL1.metadata with generated UUID: 3bdc8256-8ec9-4265-acf7-3ca1f72927bc
2021-01-28T02:31:05.047+0000 I SHARDING [conn4] Marking collection arctic_FEED_2011.LEVEL1.metadata as collection version: <unsharded>
2021-01-28T02:31:05.058+0000 I INDEX    [conn4] build index on: arctic_FEED_2011.LEVEL1.metadata properties: { v: 2, unique: true, key: { sy: 1 }, name: "sy_1", ns: "arctic_FEED_2011.LEVEL1.metadata", background: true }
2021-01-28T02:31:05.058+0000 I INDEX    [conn4] build index done.  scanned 0 total records. 0 secs
2021-01-28T02:31:05.062+0000 I SHARDING [conn4] Marking collection arctic_FEED.LEVEL1.ARCTIC as collection version: <unsharded>
2021-01-28T02:31:05.062+0000 I STORAGE  [conn4] createCollection: arctic_FEED.LEVEL1.ARCTIC with generated UUID: e7d326e9-46c5-4ded-87cf-d6e1f7ae9a56
2021-01-28T02:31:05.081+0000 I SHARDING [conn4] Marking collection meta_db.settings as collection version: <unsharded>
2021-01-28T02:31:05.084+0000 I SHARDING [conn4] Marking collection arctic_FEED.LEVEL1 as collection version: <unsharded>
2021-01-28T02:31:05.085+0000 I STORAGE  [conn4] createCollection: arctic_FEED.LEVEL1 with generated UUID: d9084561-dc86-4682-9ef4-b8ff76a3cb32
2021-01-28T02:31:05.120+0000 I INDEX    [conn4] build index on: arctic_FEED.LEVEL1 properties: { v: 2, key: { start: 1 }, name: "start_1", ns: "arctic_FEED.LEVEL1", background: true }
2021-01-28T02:31:05.120+0000 I INDEX    [conn4] build index done.  scanned 2 total records. 0 secs
2021-01-28T02:31:05.128+0000 I SHARDING [conn4] Marking collection arctic_FEED_2010.LEVEL1 as collection version: <unsharded>
2021-01-28T02:31:05.132+0000 I SHARDING [conn4] Marking collection arctic_FEED_2011.LEVEL1 as collection version: <unsharded>
----------------------------- Captured stderr call -----------------------------
2021-01-28 02:31:05,131 DEBUG arctic.tickstore.tickstore 1 buckets in 0.001147: approx 87183958 ticks/sec
2021-01-28 02:31:05,135 DEBUG arctic.tickstore.tickstore 1 buckets in 0.001136: approx 88028169 ticks/sec
2021-01-28 02:31:05,140 INFO arctic.tickstore.tickstore Got data in 0.003661 secs, creating DataFrame...
2021-01-28 02:31:05,141 INFO arctic.tickstore.tickstore 1 rows in 0.004825 secs: 207 ticks/sec
2021-01-28 02:31:05,146 INFO arctic.tickstore.tickstore Got data in 0.003347 secs, creating DataFrame...
2021-01-28 02:31:05,147 INFO arctic.tickstore.tickstore 9 rows in 0.004403 secs: 2044 ticks/sec
------------------------------ Captured log call -------------------------------
DEBUG    arctic.tickstore.tickstore:tickstore.py:612 1 buckets in 0.001147: approx 87183958 ticks/sec
DEBUG    arctic.tickstore.tickstore:tickstore.py:612 1 buckets in 0.001136: approx 88028169 ticks/sec
INFO     arctic.tickstore.tickstore:tickstore.py:355 Got data in 0.003661 secs, creating DataFrame...
INFO     arctic.tickstore.tickstore:tickstore.py:364 1 rows in 0.004825 secs: 207 ticks/sec
INFO     arctic.tickstore.tickstore:tickstore.py:355 Got data in 0.003347 secs, creating DataFrame...
INFO     arctic.tickstore.tickstore:tickstore.py:364 9 rows in 0.004403 secs: 2044 ticks/sec
--------------------------- Captured stderr teardown ---------------------------
2021-01-28 02:31:05,177 DEBUG pytest_server_fixtures.serverclass.thread Killing process tree for 31817 (total_procs_to_kill=1)
2021-01-28 02:31:05,177 DEBUG pytest_server_fixtures.serverclass.thread Killing 1 processes with signal Signals.SIGKILL
2021-01-28 02:31:05,178 DEBUG pytest_server_fixtures.serverclass.thread Waiting for 1 processes to die
2021-01-28 02:31:05,182 DEBUG pytest_server_fixtures.serverclass.thread All processes are terminated
2021-01-28 02:31:05,182 DEBUG pytest_shutil.workspace 
2021-01-28 02:31:05,182 DEBUG pytest_shutil.workspace =======================================================
2021-01-28 02:31:05,182 DEBUG pytest_shutil.workspace pytest_shutil deleting workspace /tmp/tmp20m0drzy
2021-01-28 02:31:05,182 DEBUG pytest_shutil.workspace =======================================================
2021-01-28 02:31:05,182 DEBUG pytest_shutil.workspace 
---------------------------- Captured log teardown -----------------------------
DEBUG    pytest_server_fixtures.serverclass.thread:thread.py:54 Killing process tree for 31817 (total_procs_to_kill=1)
DEBUG    pytest_server_fixtures.serverclass.thread:thread.py:35 Killing 1 processes with signal Signals.SIGKILL
DEBUG    pytest_server_fixtures.serverclass.thread:thread.py:39 Waiting for 1 processes to die
DEBUG    pytest_server_fixtures.serverclass.thread:thread.py:43 All processes are terminated
DEBUG    pytest_shutil.workspace:workspace.py:140 
DEBUG    pytest_shutil.workspace:workspace.py:141 =======================================================
DEBUG    pytest_shutil.workspace:workspace.py:142 pytest_shutil deleting workspace /tmp/tmp20m0drzy
DEBUG    pytest_shutil.workspace:workspace.py:143 =======================================================
DEBUG    pytest_shutil.workspace:workspace.py:144
_______________ test_ArcticTransaction_detects_concurrent_writes _______________
    def test_ArcticTransaction_detects_concurrent_writes():
        vs = Mock(spec=VersionStore)
        ts1 = pd.DataFrame(index=[1, 2], data={'a': [1.0, 2.0]})
        vs.read.return_value = VersionedItem(symbol=sentinel.symbol, library=sentinel.library, version=1, metadata=None,
                                             data=ts1, host=sentinel.host)
        vs.write.side_effect = [VersionedItem(symbol=sentinel.symbol, library=sentinel.library, version=2, metadata=None,
                                              data=None, host=sentinel.host),
                                VersionedItem(symbol=sentinel.symbol, library=sentinel.library, version=3, metadata=None,
                                              data=None, host=sentinel.host)]
        # note that we return some extra version 5, it is possible that we have a write coming in after our own write that gets picked up
        vs.list_versions.side_effect = [[{'version': 5}, {'version': 2}, {'version': 1}, ],
                                       [{'version': 5}, {'version': 3}, {'version': 2}, {'version': 1}, ]]
        from threading import Event, Thread
        e1 = Event()
        e2 = Event()
    
        def losing_writer():
            # will attempt to write version 2, should find that version 2 is there and it ends up writing version 3
            with pytest.raises(ArcticTransaction):
                with ArcticTransaction(vs, sentinel.symbol, sentinel.user, sentinel.log) as cwb:
                    cwb.write(sentinel.symbol, pd.DataFrame([1.0, 2.0], [3, 4]))
                    e1.wait()
    
        def winning_writer():
            # will attempt to write version 2 as well
            with ArcticTransaction(vs, sentinel.symbol, sentinel.user, sentinel.log) as cwb:
                cwb.write(sentinel.symbol, pd.DataFrame([1.0, 2.0], [5, 6]))
                e2.wait()
    
        t1 = Thread(target=losing_writer)
        t2 = Thread(target=winning_writer)
        t1.start()
        t2.start()
    
        # both read the same timeseries and are locked doing some 'work'
        e2.set()
        # t2  should now be able to finish
        t2.join()
        e1.set()
        t1.join()
    
        # we're expecting the losing_writer to undo its write once it realises that it wrote v3 instead of v2
>       vs._delete_version.assert_called_once_with(sentinel.symbol, 3)
tests/unit/store/test_version_store_audit.py:221: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
_mock_self = <Mock name='mock._delete_version' id='140714262361984'>
args = (sentinel.symbol, 3), kwargs = {}
self = <Mock name='mock._delete_version' id='140714262361984'>
msg = "Expected '_delete_version' to be called once. Called 0 times."
    def assert_called_once_with(_mock_self, *args, **kwargs):
        """assert that the mock was called exactly once and that that call was
        with the specified arguments."""
        self = _mock_self
        if not self.call_count == 1:
            msg = ("Expected '%s' to be called once. Called %s times.%s"
                   % (self._mock_name or 'mock',
                      self.call_count,
                      self._calls_repr()))
>           raise AssertionError(msg)
E           AssertionError: Expected '_delete_version' to be called once. Called 0 times.
../../../virtualenv/python3.6.7/lib/python3.6/site-packages/mock/mock.py:925: AssertionError
----------------------------- Captured stderr call -----------------------------
2021-01-28 02:34:44,808 INFO arctic.store.audit MT: None@None: [sentinel.user] sentinel.log: sentinel.symbol
Exception in thread Thread-764:
Traceback (most recent call last):
  File "/opt/python/3.6.7/lib/python3.6/threading.py", line 916, in _bootstrap_inner
    self.run()
  File "/opt/python/3.6.7/lib/python3.6/threading.py", line 864, in run
    self._target(*self._args, **self._kwargs)
  File "/home/travis/build/man-group/arctic/tests/unit/store/test_version_store_audit.py", line 197, in losing_writer
    with pytest.raises(ArcticTransaction):
  File "/home/travis/virtualenv/python3.6.7/lib/python3.6/site-packages/_pytest/python_api.py", line 719, in raises
    raise TypeError(msg.format(not_a))
TypeError: expected exception must be a BaseException type, not ArcticTransaction
------------------------------ Captured log call -------------------------------
INFO     arctic.store.audit:audit.py:87 MT: None@None: [sentinel.user] sentinel.log: sentinel.symbol
=============================== warnings summary ===============================
tests/integration/test_arctic.py: 4 warnings
tests/integration/test_concurrent_append.py: 1 warning
tests/integration/test_howtos.py: 3 warnings
tests/integration/scripts/test_arctic_fsck.py: 45 warnings
tests/integration/scripts/test_copy_data.py: 23 warnings
tests/integration/store/test_bitemporal_store.py: 43 warnings
tests/integration/store/test_ndarray_store.py: 37 warnings
tests/integration/store/test_ndarray_store_append.py: 69 warnings
tests/integration/store/test_pandas_store.py: 378 warnings
tests/integration/store/test_version_store.py: 653 warnings
tests/integration/store/test_version_store_audit.py: 29 warnings
tests/integration/store/test_version_store_corruption.py: 14 warnings
  /home/travis/build/man-group/arctic/arctic/store/_ndarray_store.py:600: DeprecationWarning: tostring() is deprecated. Use tobytes() instead.
    sha.update(item.tostring())
tests/integration/test_arctic.py: 3 warnings
tests/integration/test_howtos.py: 3 warnings
tests/integration/scripts/test_arctic_fsck.py: 42 warnings
tests/integration/scripts/test_copy_data.py: 21 warnings
tests/integration/store/test_bitemporal_store.py: 29 warnings
tests/integration/store/test_ndarray_store.py: 828 warnings
tests/integration/store/test_ndarray_store_append.py: 314 warnings
tests/integration/store/test_pandas_store.py: 285 warnings
tests/integration/store/test_version_store.py: 573 warnings
tests/integration/store/test_version_store_audit.py: 21 warnings
tests/integration/store/test_version_store_corruption.py: 18 warnings
  /home/travis/build/man-group/arctic/arctic/store/_ndarray_store.py:657: DeprecationWarning: tostring() is deprecated. Use tobytes() instead.
    chunks = [(item[i * rows_per_chunk: (i + 1) * rows_per_chunk]).tostring() for i in idxs]
tests/integration/test_arctic.py: 3 warnings
tests/integration/test_howtos.py: 3 warnings
tests/integration/scripts/test_arctic_fsck.py: 42 warnings
tests/integration/scripts/test_copy_data.py: 21 warnings
tests/integration/store/test_bitemporal_store.py: 29 warnings
tests/integration/store/test_pandas_store.py: 39 warnings
tests/integration/store/test_version_store.py: 1979 warnings
tests/integration/store/test_version_store_audit.py: 21 warnings
tests/integration/store/test_version_store_corruption.py: 138 warnings
  /home/travis/build/man-group/arctic/arctic/store/_pandas_ndarray_store.py:62: DeprecationWarning: tostring() is deprecated. Use tobytes() instead.
    return Binary(compress(index.tostring()))
tests/integration/test_arctic.py: 5 warnings
tests/integration/scripts/test_delete_library.py: 5 warnings
  /home/travis/build/man-group/arctic/arctic/_cache.py:120: DeprecationWarning: update is deprecated. Use replace_one, update_one or update_many instead.
    {"$pull": {"data": item}}
tests/integration/test_arctic.py::test_list_libraries_cached
  /home/travis/build/man-group/arctic/tests/integration/test_arctic.py:250: DeprecationWarning: remove is deprecated. Use delete_one or delete_many instead.
    arctic._conn.meta_db.cache.remove({})
tests/integration/chunkstore/test_chunkstore.py: 9982 warnings
tests/integration/chunkstore/test_fixes.py: 107 warnings
tests/integration/chunkstore/test_utils.py: 2 warnings
tests/integration/chunkstore/tools/test_tools.py: 52 warnings
tests/unit/serialization/test_numpy_arrays.py: 26 warnings
  /home/travis/build/man-group/arctic/arctic/serialization/numpy_arrays.py:119: DeprecationWarning: tostring() is deprecated. Use tobytes() instead.
    arrays.append(arr.tostring())
tests/integration/store/test_ndarray_store.py: 3 warnings
tests/integration/store/test_ndarray_store_append.py: 583 warnings
tests/integration/store/test_pandas_store.py: 21 warnings
tests/integration/store/test_version_store.py: 1546 warnings
tests/integration/store/test_version_store_corruption.py: 124 warnings
  /home/travis/build/man-group/arctic/arctic/store/_ndarray_store.py:449: DeprecationWarning: tostring() is deprecated. Use tobytes() instead.
    data = item.tostring()
tests/integration/store/test_pandas_store.py::test_save_read_pandas_empty_series_with_datetime_multiindex_with_timezone
  /home/travis/build/man-group/arctic/tests/integration/store/test_pandas_store.py:155: DeprecationWarning: The default dtype for empty Series will be 'object' instead of 'float64' in a future version. Specify a dtype explicitly to silence this warning.
    df = Series(data=[], index=empty_index)
tests/integration/store/test_pandas_store.py::test_duplicate_labels
tests/integration/store/test_pandas_store.py::test_duplicate_labels
tests/integration/store/test_pandas_store.py::test_duplicate_labels
tests/integration/store/test_pandas_store.py::test_duplicate_labels
  /home/travis/virtualenv/python3.6.7/lib/python3.6/site-packages/numpy/core/numeric.py:2378: DeprecationWarning: elementwise comparison failed; this will raise an error in the future.
    return bool(asarray(a1 == a2).all())
tests/integration/tickstore/test_toplevel.py: 44 warnings
tests/integration/tickstore/test_ts_read.py: 5 warnings
tests/integration/tickstore/test_ts_write.py: 2 warnings
tests/unit/tickstore/test_tickstore.py: 1 warning
  /home/travis/build/man-group/arctic/arctic/tickstore/tickstore.py:707: DeprecationWarning: tostring() is deprecated. Use tobytes() instead.
    rowmask = Binary(lz4_compressHC(np.packbits(np.ones(len(df), dtype='uint8')).tostring()))
tests/integration/tickstore/test_toplevel.py: 176 warnings
tests/integration/tickstore/test_ts_read.py: 6 warnings
tests/integration/tickstore/test_ts_write.py: 6 warnings
tests/unit/tickstore/test_tickstore.py: 3 warnings
  /home/travis/build/man-group/arctic/arctic/tickstore/tickstore.py:718: DeprecationWarning: tostring() is deprecated. Use tobytes() instead.
    DATA: Binary(lz4_compressHC(array.tostring())),
tests/integration/tickstore/test_toplevel.py: 44 warnings
tests/integration/tickstore/test_ts_read.py: 4 warnings
tests/integration/tickstore/test_ts_write.py: 2 warnings
tests/unit/tickstore/test_tickstore.py: 1 warning
  /home/travis/build/man-group/arctic/arctic/tickstore/tickstore.py:727: DeprecationWarning: tostring() is deprecated. Use tobytes() instead.
    recs[index_name].astype('datetime64[ms]').view('uint64')))).tostring()))
tests/integration/tickstore/test_toplevel.py: 4 warnings
tests/integration/tickstore/test_ts_delete.py: 12 warnings
tests/integration/tickstore/test_ts_read.py: 141 warnings
tests/integration/tickstore/test_ts_write.py: 18 warnings
tests/unit/tickstore/test_tickstore.py: 8 warnings
  /home/travis/build/man-group/arctic/arctic/tickstore/tickstore.py:758: DeprecationWarning: tostring() is deprecated. Use tobytes() instead.
    for k, v in iteritems(rowmask)])
tests/integration/tickstore/test_toplevel.py: 4 warnings
tests/integration/tickstore/test_ts_delete.py: 12 warnings
tests/integration/tickstore/test_ts_read.py: 141 warnings
tests/integration/tickstore/test_ts_write.py: 18 warnings
tests/unit/tickstore/test_tickstore.py: 8 warnings
  /home/travis/build/man-group/arctic/arctic/tickstore/tickstore.py:763: DeprecationWarning: tostring() is deprecated. Use tobytes() instead.
    rtn[COLUMNS][k] = {DATA: Binary(lz4_compressHC(v.tostring())),
tests/integration/tickstore/test_toplevel.py: 4 warnings
tests/integration/tickstore/test_ts_delete.py: 6 warnings
tests/integration/tickstore/test_ts_read.py: 40 warnings
tests/integration/tickstore/test_ts_write.py: 7 warnings
tests/unit/tickstore/test_tickstore.py: 2 warnings
  /home/travis/build/man-group/arctic/arctic/tickstore/tickstore.py:776: DeprecationWarning: tostring() is deprecated. Use tobytes() instead.
    rtn[INDEX] = Binary(lz4_compressHC(np.concatenate(([data['index'][0]], np.diff(data['index']))).tostring()))
tests/unit/chunkstore/test_passthrough_chunker.py::test_pass_thru
  /home/travis/build/man-group/arctic/arctic/chunkstore/passthrough_chunker.py:75: DeprecationWarning: The default dtype for empty Series will be 'object' instead of 'float64' in a future version. Specify a dtype explicitly to silence this warning.
    return Series()
tests/unit/chunkstore/test_passthrough_chunker.py::test_pass_thru
  /home/travis/build/man-group/arctic/tests/unit/chunkstore/test_passthrough_chunker.py:18: DeprecationWarning: The default dtype for empty Series will be 'object' instead of 'float64' in a future version. Specify a dtype explicitly to silence this warning.
    assert(p.exclude(Series([1, 2, 3]), None).equals(Series()))
tests/unit/serialization/test_incremental.py: 41846 warnings
  /home/travis/build/man-group/arctic/arctic/serialization/incremental.py:223: DeprecationWarning: tostring() is deprecated. Use tobytes() instead.
    chunk = chunk.tostring() if chunk is not None and get_bytes else chunk
tests/unit/serialization/test_numpy_arrays.py::test_string_cols_with_nans
tests/unit/serialization/test_numpy_arrays.py::test_objify_with_missing_columns
  /home/travis/build/man-group/arctic/arctic/serialization/numpy_arrays.py:118: DeprecationWarning: tostring() is deprecated. Use tobytes() instead.
    masks[str(c)] = Binary(compress(mask.tostring()))
tests/unit/store/test_pickle_store.py::test_unpickle_highest_protocol
  /home/travis/build/man-group/arctic/tests/unit/store/test_pickle_store.py:121: DeprecationWarning: The default dtype for empty Series will be 'object' instead of 'float64' in a future version. Specify a dtype explicitly to silence this warning.
    'blob': compressHC(cPickle.dumps(pd.Series(), protocol=cPickle.HIGHEST_PROTOCOL)),
tests/unit/store/test_pickle_store.py::test_unpickle_highest_protocol
  /home/travis/build/man-group/arctic/tests/unit/store/test_pickle_store.py:127: DeprecationWarning: The default dtype for empty Series will be 'object' instead of 'float64' in a future version. Specify a dtype explicitly to silence this warning.
    expected = pd.Series()
-- Docs: https://docs.pytest.org/en/stable/warnings.html
------ generated xml file: /home/travis/build/man-group/arctic/junit.xml -------
----------- coverage: platform linux, python 3.6.7-final-0 -----------
Coverage HTML written to dir htmlcov
Coverage XML written to file coverage.xml
=========================== short test summary info ============================
FAILED tests/integration/tickstore/test_toplevel.py::test_should_return_data_when_date_range_falls_in_a_single_underlying_library
FAILED tests/integration/tickstore/test_toplevel.py::test_should_return_data_when_date_range_spans_libraries_even_if_one_returns_nothing
FAILED tests/integration/tickstore/test_toplevel.py::test_should_write_top_level_with_list_of_dicts
FAILED tests/integration/tickstore/test_toplevel.py::test_should_write_top_level_with_correct_timezone
FAILED tests/unit/store/test_version_store_audit.py::test_ArcticTransaction_detects_concurrent_writes
= 5 failed, 1307 passed, 18 skipped, 8 xfailed, 1 xpassed, 60744 warnings in 1323.29s (0:22:03) =
The command "python setup.py test --pytest-args=-v" exited with 1.
1.26s$ pycodestyle arctic
The command "pycodestyle arctic" exited with 0.
Done. Your build exited with 1.
```