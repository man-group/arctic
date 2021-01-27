```shell
$ source ~/virtualenv/python3.6/bin/activate0.00s0.11s0.08s0.06s
worker_info
Worker information
0.14s0.01s0.00s0.01s
system_info
Build system information
0.01s0.01s0.62s0.19s0.05s0.00s0.04s0.00s0.01s0.01s0.01s0.01s0.01s0.00s0.00s0.02s0.00s0.01s0.27s0.00s0.00s0.00s0.01s0.00s0.08s0.01s0.75s0.00s0.00s6.03s0.00s2.58s0.00s2.59s
docker_mtu_and_registry_mirrors
resolvconf
services
3.02s$ sudo systemctl start mongod
git.checkout
0.68s$ git clone --depth=50 https://github.com/man-group/arctic.git man-group/arctic
git.submodule
0.03s$ git submodule update --init --recursive
$ python --version
Python 3.6.7
$ pip --version
pip 20.1.1 from /home/travis/virtualenv/python3.6.7/lib/python3.6/site-packages/pip (python 3.6)
before_install
0.87s$ pip install pycodestyle
install.1
0.10s$ mongo --version
install.2
2.06s$ pip install --upgrade pip
install.3
0.77s$ pip install python-dateutil --upgrade
install.4
1.01s$ pip install pytz --upgrade
install.5
0.66s$ pip install tzlocal --upgrade
install.6
1.45s$ pip install pymongo --upgrade
install.7
4.10s$ pip install numpy --upgrade
install.8
4.19s$ pip install pandas --upgrade
install.9
0.71s$ pip install decorator --upgrade
install.10
0.70s$ pip install enum34 --upgrade
install.11
1.15s$ pip install lz4 --upgrade
install.12
1.03s$ pip install mock --upgrade
install.13
0.70s$ pip install mockextras
install.14
2.93s$ pip install pytest --upgrade
install.15
1.45s$ pip install pytest-cov --upgrade
install.16
4.60s$ pip install pytest-server-fixtures --upgrade
install.17
0.82s$ pip install pytest-timeout --upgrade
install.18
0.98s$ pip install pytest-xdist --upgrade
install.19
0.79s$ pip install setuptools-git --upgrade
install.20
0.00s$ if [[ $TRAVIS_PYTHON_VERSION == 2.7 ]]; then pip install pandas==0.22.0; fi
0.33s$ pip freeze
apipkg==1.5
atomicwrites==1.2.1
attrs==20.3.0
certifi==2018.10.15
chardet==4.0.0
contextlib2==0.6.0.post1
coverage==5.3.1
decorator==4.4.2
enum34==1.1.10
execnet==1.7.1
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
pytest==6.2.1
pytest-cov==2.11.0
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
urllib3==1.26.2
virtualenv==16.0.0
virtualenv-clone==0.4.0
wcwidth==0.1.7
zipp==0.5.1
The command "pip freeze" exited with 0.
1276.56s$ python setup.py test --pytest-args=-v
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
platform linux -- Python 3.6.7, pytest-6.2.1, py-1.10.0, pluggy-0.12.0 -- /home/travis/virtualenv/python3.6.7/bin/python
cachedir: .pytest_cache
rootdir: /home/travis/build/man-group/arctic
plugins: xdist-1.26.1, server-fixtures-1.7.0, shutil-1.7.0, timeout-1.4.2, forked-1.3.0, cov-2.11.0
collected 1339 items                                                           
tests/integration/test_arctic.py::test_connect_to_Arctic_string PASSED   [  0%]2021-01-20 04:11:23,540 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/test_arctic.py::test_connect_to_Arctic_connection PASSED [  0%]2021-01-20 04:11:24,207 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/test_arctic.py::test_reset_Arctic PASSED               [  0%]2021-01-20 04:11:25,039 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/test_arctic.py::test_re_authenticate_on_arctic_reset PASSED [  0%]2021-01-20 04:11:25,879 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/test_arctic.py::test_simple PASSED                     [  0%]2021-01-20 04:11:27,927 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/test_arctic.py::test_indexes PASSED                    [  0%]2021-01-20 04:11:28,742 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/test_arctic.py::test_delete_library PASSED             [  0%]2021-01-20 04:11:29,834 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/test_arctic.py::test_quota PASSED                      [  0%]2021-01-20 04:11:30,685 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/test_arctic.py::test_check_quota PASSED                [  0%]2021-01-20 04:11:31,512 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/test_arctic.py::test_default_mongo_retry_timout PASSED [  0%]
tests/integration/test_arctic.py::test_lib_rename PASSED                 [  0%]
tests/integration/test_arctic.py::test_lib_rename_namespace PASSED       [  0%]
tests/integration/test_arctic.py::test_lib_type PASSED                   [  0%]2021-01-20 04:11:34,037 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/test_arctic.py::test_library_exists PASSED             [  1%]2021-01-20 04:11:34,850 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/test_arctic.py::test_library_exists_no_auth PASSED     [  1%]
tests/integration/test_arctic.py::test_list_libraries_cached PASSED      [  1%]2021-01-20 04:11:36,659 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/test_arctic.py::test_initialize_library_adds_to_cache PASSED [  1%]2021-01-20 04:11:37,807 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/test_arctic.py::test_cache_does_not_return_stale_data PASSED [  1%]2021-01-20 04:11:39,011 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/test_arctic.py::test_renaming_returns_new_name_in_cache PASSED [  1%]2021-01-20 04:11:40,026 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/test_arctic.py::test_deleting_library_removes_it_from_cache PASSED [  1%]2021-01-20 04:11:41,135 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/test_arctic.py::test_disable_cache_by_settings PASSED  [  1%]2021-01-20 04:11:41,977 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/test_arctic_multithreading.py::test_multiprocessing_safety PASSED [  1%]2021-01-20 04:12:05,044 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/test_arctic_multithreading.py::test_multiprocessing_safety_parent_children_race PASSED [  1%]2021-01-20 04:12:25,785 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
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
tests/integration/test_concurrent_append.py::test_append_kill PASSED     [  2%]2021-01-20 04:15:30,714 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/test_decorators.py::test_get_host_VersionStore PASSED  [  2%]2021-01-20 04:15:31,531 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/test_howtos.py::test_howto[how_to_custom_arctic_library.py] PASSED [  2%]2021-01-20 04:15:32,251 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/test_howtos.py::test_howto[how_to_use_arctic.py] PASSED [  2%]2021-01-20 04:15:33,151 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_chunkstore.py::test_write_dataframe PASSED [  2%]2021-01-20 04:15:34,017 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_chunkstore.py::test_upsert_dataframe PASSED [  2%]2021-01-20 04:15:34,879 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_chunkstore.py::test_write_dataframe_noindex PASSED [  3%]2021-01-20 04:15:35,720 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_chunkstore.py::test_overwrite_dataframe PASSED [  3%]2021-01-20 04:15:36,579 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_chunkstore.py::test_overwrite_dataframe_noindex PASSED [  3%]2021-01-20 04:15:37,422 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_chunkstore.py::test_overwrite_dataframe_monthly PASSED [  3%]2021-01-20 04:15:38,320 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_chunkstore.py::test_write_read_with_daterange PASSED [  3%]2021-01-20 04:15:39,194 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_chunkstore.py::test_write_read_with_daterange_noindex PASSED [  3%]2021-01-20 04:15:40,027 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_chunkstore.py::test_store_single_index_df PASSED [  3%]2021-01-20 04:15:40,860 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_chunkstore.py::test_no_range PASSED    [  3%]2021-01-20 04:15:41,700 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_chunkstore.py::test_closed_open PASSED [  3%]2021-01-20 04:15:42,548 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_chunkstore.py::test_open_closed PASSED [  3%]2021-01-20 04:15:43,392 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_chunkstore.py::test_closed_open_no_index PASSED [  3%]2021-01-20 04:15:44,232 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_chunkstore.py::test_open_open_no_index PASSED [  3%]2021-01-20 04:15:45,071 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_chunkstore.py::test_monthly_df PASSED  [  3%]2021-01-20 04:15:45,922 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_chunkstore.py::test_yearly_df PASSED   [  4%]2021-01-20 04:15:46,747 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_chunkstore.py::test_append_daily PASSED [  4%]2021-01-20 04:15:47,783 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_chunkstore.py::test_append_monthly PASSED [  4%]2021-01-20 04:15:48,683 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_chunkstore.py::test_append_yearly PASSED [  4%]2021-01-20 04:15:49,541 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_chunkstore.py::test_append_existing_chunk PASSED [  4%]2021-01-20 04:15:50,374 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_chunkstore.py::test_store_objects_df PASSED [  4%]2021-01-20 04:15:51,219 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_chunkstore.py::test_empty_range PASSED [  4%]2021-01-20 04:15:52,047 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_chunkstore.py::test_update PASSED      [  4%]2021-01-20 04:15:52,918 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_chunkstore.py::test_update_no_overlap PASSED [  4%]2021-01-20 04:15:53,778 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_chunkstore.py::test_update_chunk_range PASSED [  4%]2021-01-20 04:15:54,639 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_chunkstore.py::test_update_chunk_range_overlap PASSED [  4%]2021-01-20 04:15:55,483 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_chunkstore.py::test_append_before PASSED [  4%]2021-01-20 04:15:56,347 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_chunkstore.py::test_append_and_update PASSED [  4%]2021-01-20 04:15:57,231 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_chunkstore.py::test_update_same_df PASSED [  5%]2021-01-20 04:15:58,083 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_chunkstore.py::test_df_with_multiindex PASSED [  5%]2021-01-20 04:15:58,925 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_chunkstore.py::test_with_strings PASSED [  5%]2021-01-20 04:15:59,756 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_chunkstore.py::test_with_strings_multiindex_append PASSED [  5%]2021-01-20 04:16:00,635 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_chunkstore.py::test_multiple_actions PASSED [  5%]2021-01-20 04:16:11,355 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_chunkstore.py::test_multiple_actions_monthly_data PASSED [  5%]2021-01-20 04:16:16,556 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_chunkstore.py::test_delete PASSED      [  5%]2021-01-20 04:16:17,414 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_chunkstore.py::test_delete_empty_df_on_range PASSED [  5%]2021-01-20 04:16:18,280 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_chunkstore.py::test_get_info PASSED    [  5%]2021-01-20 04:16:19,112 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_chunkstore.py::test_get_info_after_append PASSED [  5%]2021-01-20 04:16:20,019 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_chunkstore.py::test_get_info_after_update PASSED [  5%]2021-01-20 04:16:20,877 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_chunkstore.py::test_delete_range PASSED [  5%]2021-01-20 04:16:21,758 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_chunkstore.py::test_delete_range_noindex PASSED [  5%]2021-01-20 04:16:22,625 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_chunkstore.py::test_read_chunk_range PASSED [  5%]2021-01-20 04:16:23,519 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_chunkstore.py::test_read_data_doesnt_exist PASSED [  6%]
tests/integration/chunkstore/test_chunkstore.py::test_invalid_type PASSED [  6%]
tests/integration/chunkstore/test_chunkstore.py::test_append_no_data PASSED [  6%]
tests/integration/chunkstore/test_chunkstore.py::test_append_upsert PASSED [  6%]2021-01-20 04:16:26,785 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_chunkstore.py::test_append_no_new_data PASSED [  6%]2021-01-20 04:16:27,860 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_chunkstore.py::test_overwrite_series PASSED [  6%]2021-01-20 04:16:28,694 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_chunkstore.py::test_overwrite_series_monthly PASSED [  6%]2021-01-20 04:16:29,530 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_chunkstore.py::test_pandas_datetime_index_store_series PASSED [  6%]2021-01-20 04:16:30,363 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_chunkstore.py::test_yearly_series PASSED [  6%]2021-01-20 04:16:31,182 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_chunkstore.py::test_store_objects_series PASSED [  6%]2021-01-20 04:16:32,024 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_chunkstore.py::test_update_series PASSED [  6%]2021-01-20 04:16:32,975 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_chunkstore.py::test_update_same_series PASSED [  6%]2021-01-20 04:16:33,820 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_chunkstore.py::test_dtype_mismatch PASSED [  6%]2021-01-20 04:16:34,677 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_chunkstore.py::test_read_column_subset PASSED [  7%]2021-01-20 04:16:35,550 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_chunkstore.py::test_rename PASSED      [  7%]
tests/integration/chunkstore/test_chunkstore.py::test_pass_thru_chunker PASSED [  7%]2021-01-20 04:16:37,353 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_chunkstore.py::test_pass_thru_chunker_append PASSED [  7%]2021-01-20 04:16:38,183 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_chunkstore.py::test_pass_thru_chunker_update PASSED [  7%]2021-01-20 04:16:39,006 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_chunkstore.py::test_pass_thru_chunker_update_range PASSED [  7%]2021-01-20 04:16:39,835 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_chunkstore.py::test_size_chunking PASSED [  7%]2021-01-20 04:16:43,323 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_chunkstore.py::test_size_chunk_append PASSED [  7%]2021-01-20 04:16:50,684 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_chunkstore.py::test_delete_range_segment PASSED [  7%]2021-01-20 04:16:56,578 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_chunkstore.py::test_size_chunk_update PASSED [  7%]2021-01-20 04:17:03,830 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_chunkstore.py::test_size_chunk_multiple_update PASSED [  7%]2021-01-20 04:17:07,437 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_chunkstore.py::test_get_chunk_range PASSED [  7%]2021-01-20 04:17:08,268 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_chunkstore.py::test_iterators PASSED   [  7%]2021-01-20 04:17:09,217 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_chunkstore.py::test_unnamed_colums PASSED [  7%]
tests/integration/chunkstore/test_chunkstore.py::test_quarterly_data PASSED [  8%]2021-01-20 04:17:10,881 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_chunkstore.py::test_list_symbols PASSED [  8%]2021-01-20 04:17:15,881 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_chunkstore.py::test_stats PASSED       [  8%]2021-01-20 04:17:21,079 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_chunkstore.py::test_metadata PASSED    [  8%]2021-01-20 04:17:21,985 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_chunkstore.py::test_metadata_update PASSED [  8%]2021-01-20 04:17:22,813 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_chunkstore.py::test_metadata_nosymbol PASSED [  8%]2021-01-20 04:17:23,607 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_chunkstore.py::test_metadata_none PASSED [  8%]2021-01-20 04:17:24,420 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_chunkstore.py::test_metadata_invalid PASSED [  8%]2021-01-20 04:17:25,246 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_chunkstore.py::test_write_metadata PASSED [  8%]2021-01-20 04:17:26,063 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_chunkstore.py::test_write_metadata_nosymbol PASSED [  8%]2021-01-20 04:17:26,854 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_chunkstore.py::test_audit PASSED       [  8%]2021-01-20 04:17:27,880 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_chunkstore.py::test_chunkstore_misc PASSED [  8%]2021-01-20 04:17:28,686 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_chunkstore.py::test_unsorted_index PASSED [  8%]2021-01-20 04:17:29,545 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_chunkstore.py::test_unsorted_date_col PASSED [  9%]2021-01-20 04:17:30,410 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_chunkstore.py::test_chunk_range_with_dti PASSED [  9%]2021-01-20 04:17:31,226 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_chunkstore.py::test_chunkstore_multiread PASSED [  9%]2021-01-20 04:17:32,192 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_chunkstore.py::test_chunkstore_multiread_samedate PASSED [  9%]2021-01-20 04:17:33,136 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_chunkstore.py::test_write_dataframe_with_func PASSED [  9%]2021-01-20 04:17:34,001 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_fixes.py::test_write_dataframe PASSED  [  9%]2021-01-20 04:17:34,836 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_fixes.py::test_compression PASSED      [  9%]2021-01-20 04:17:36,803 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_fixes.py::test_date_interval PASSED    [  9%]2021-01-20 04:17:37,888 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_fixes.py::test_rewrite PASSED          [  9%]2021-01-20 04:17:38,723 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_fixes.py::test_iterator PASSED         [  9%]2021-01-20 04:17:39,936 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_fixes.py::test_missing_cols PASSED     [  9%]2021-01-20 04:17:40,847 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_fixes.py::test_column_copy PASSED      [  9%]2021-01-20 04:17:41,677 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_fixes.py::test_get_info_empty PASSED   [  9%]2021-01-20 04:17:42,481 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/test_utils.py::test_read_apply PASSED       [ 10%]2021-01-20 04:17:43,314 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/chunkstore/tools/test_tools.py::test_segment_repair_tool PASSED [ 10%]2021-01-20 04:17:46,439 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/fixtures/test_arctic.py::test_arctic PASSED            [ 10%]2021-01-20 04:17:47,103 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/fixtures/test_arctic.py::test_library PASSED           [ 10%]2021-01-20 04:17:47,926 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/fixtures/test_arctic.py::test_ms_lib PASSED            [ 10%]2021-01-20 04:17:48,654 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_arctic_fsck.py::test_cleanup_orphaned_chunks[True-data0-FwPointersCfg.DISABLED] PASSED [ 10%]2021-01-20 04:17:49,533 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_arctic_fsck.py::test_cleanup_orphaned_chunks[True-data1-FwPointersCfg.HYBRID] PASSED [ 10%]2021-01-20 04:17:50,416 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_arctic_fsck.py::test_cleanup_orphaned_chunks[True-data2-FwPointersCfg.ENABLED] PASSED [ 10%]2021-01-20 04:17:51,305 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_arctic_fsck.py::test_cleanup_orphaned_chunks[True-data3-FwPointersCfg.DISABLED] PASSED [ 10%]2021-01-20 04:17:52,191 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_arctic_fsck.py::test_cleanup_orphaned_chunks[True-data4-FwPointersCfg.HYBRID] PASSED [ 10%]2021-01-20 04:17:53,076 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_arctic_fsck.py::test_cleanup_orphaned_chunks[True-data5-FwPointersCfg.ENABLED] PASSED [ 10%]2021-01-20 04:17:53,953 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_arctic_fsck.py::test_cleanup_orphaned_chunks[False-data6-FwPointersCfg.DISABLED] PASSED [ 10%]2021-01-20 04:17:54,823 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_arctic_fsck.py::test_cleanup_orphaned_chunks[False-data7-FwPointersCfg.HYBRID] PASSED [ 10%]2021-01-20 04:17:55,709 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_arctic_fsck.py::test_cleanup_orphaned_chunks[False-data8-FwPointersCfg.ENABLED] PASSED [ 10%]2021-01-20 04:17:56,588 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_arctic_fsck.py::test_cleanup_orphaned_chunks[False-data9-FwPointersCfg.DISABLED] PASSED [ 11%]2021-01-20 04:17:57,473 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_arctic_fsck.py::test_cleanup_orphaned_chunks[False-data10-FwPointersCfg.HYBRID] PASSED [ 11%]2021-01-20 04:17:58,370 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_arctic_fsck.py::test_cleanup_orphaned_chunks[False-data11-FwPointersCfg.ENABLED] PASSED [ 11%]2021-01-20 04:17:59,252 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_arctic_fsck.py::test_cleanup_noop[True-data0-FwPointersCfg.DISABLED] PASSED [ 11%]2021-01-20 04:18:00,135 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_arctic_fsck.py::test_cleanup_noop[True-data1-FwPointersCfg.HYBRID] PASSED [ 11%]2021-01-20 04:18:01,015 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_arctic_fsck.py::test_cleanup_noop[True-data2-FwPointersCfg.ENABLED] PASSED [ 11%]2021-01-20 04:18:01,894 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_arctic_fsck.py::test_cleanup_noop[True-data3-FwPointersCfg.DISABLED] PASSED [ 11%]2021-01-20 04:18:02,783 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_arctic_fsck.py::test_cleanup_noop[True-data4-FwPointersCfg.HYBRID] PASSED [ 11%]2021-01-20 04:18:03,682 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_arctic_fsck.py::test_cleanup_noop[True-data5-FwPointersCfg.ENABLED] PASSED [ 11%]2021-01-20 04:18:04,578 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_arctic_fsck.py::test_cleanup_noop[False-data6-FwPointersCfg.DISABLED] PASSED [ 11%]2021-01-20 04:18:05,452 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_arctic_fsck.py::test_cleanup_noop[False-data7-FwPointersCfg.HYBRID] PASSED [ 11%]2021-01-20 04:18:06,333 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_arctic_fsck.py::test_cleanup_noop[False-data8-FwPointersCfg.ENABLED] PASSED [ 11%]2021-01-20 04:18:07,296 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_arctic_fsck.py::test_cleanup_noop[False-data9-FwPointersCfg.DISABLED] PASSED [ 11%]2021-01-20 04:18:08,203 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_arctic_fsck.py::test_cleanup_noop[False-data10-FwPointersCfg.HYBRID] PASSED [ 12%]2021-01-20 04:18:09,098 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_arctic_fsck.py::test_cleanup_noop[False-data11-FwPointersCfg.ENABLED] PASSED [ 12%]2021-01-20 04:18:09,982 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_arctic_fsck.py::test_cleanup_orphaned_chunks_ignores_recent[True-data0-FwPointersCfg.DISABLED] PASSED [ 12%]2021-01-20 04:18:10,859 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_arctic_fsck.py::test_cleanup_orphaned_chunks_ignores_recent[True-data1-FwPointersCfg.HYBRID] PASSED [ 12%]2021-01-20 04:18:11,735 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_arctic_fsck.py::test_cleanup_orphaned_chunks_ignores_recent[True-data2-FwPointersCfg.ENABLED] PASSED [ 12%]2021-01-20 04:18:12,612 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_arctic_fsck.py::test_cleanup_orphaned_chunks_ignores_recent[True-data3-FwPointersCfg.DISABLED] PASSED [ 12%]2021-01-20 04:18:13,485 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_arctic_fsck.py::test_cleanup_orphaned_chunks_ignores_recent[True-data4-FwPointersCfg.HYBRID] PASSED [ 12%]2021-01-20 04:18:14,362 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_arctic_fsck.py::test_cleanup_orphaned_chunks_ignores_recent[True-data5-FwPointersCfg.ENABLED] PASSED [ 12%]2021-01-20 04:18:15,246 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_arctic_fsck.py::test_cleanup_orphaned_chunks_ignores_recent[False-data6-FwPointersCfg.DISABLED] PASSED [ 12%]2021-01-20 04:18:16,128 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_arctic_fsck.py::test_cleanup_orphaned_chunks_ignores_recent[False-data7-FwPointersCfg.HYBRID] PASSED [ 12%]2021-01-20 04:18:17,001 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_arctic_fsck.py::test_cleanup_orphaned_chunks_ignores_recent[False-data8-FwPointersCfg.ENABLED] PASSED [ 12%]2021-01-20 04:18:17,875 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_arctic_fsck.py::test_cleanup_orphaned_chunks_ignores_recent[False-data9-FwPointersCfg.DISABLED] PASSED [ 12%]2021-01-20 04:18:18,757 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_arctic_fsck.py::test_cleanup_orphaned_chunks_ignores_recent[False-data10-FwPointersCfg.HYBRID] PASSED [ 12%]2021-01-20 04:18:19,639 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_arctic_fsck.py::test_cleanup_orphaned_chunks_ignores_recent[False-data11-FwPointersCfg.ENABLED] PASSED [ 12%]2021-01-20 04:18:20,522 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_arctic_fsck.py::test_cleanup_orphaned_chunk_doesnt_break_versions[data0-FwPointersCfg.DISABLED] PASSED [ 13%]2021-01-20 04:18:21,419 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_arctic_fsck.py::test_cleanup_orphaned_chunk_doesnt_break_versions[data1-FwPointersCfg.HYBRID] PASSED [ 13%]2021-01-20 04:18:22,319 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_arctic_fsck.py::test_cleanup_orphaned_chunk_doesnt_break_versions[data2-FwPointersCfg.ENABLED] PASSED [ 13%]2021-01-20 04:18:23,224 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_arctic_fsck.py::test_cleanup_orphaned_chunk_doesnt_break_versions[data3-FwPointersCfg.DISABLED] PASSED [ 13%]2021-01-20 04:18:24,155 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_arctic_fsck.py::test_cleanup_orphaned_chunk_doesnt_break_versions[data4-FwPointersCfg.HYBRID] PASSED [ 13%]2021-01-20 04:18:25,095 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_arctic_fsck.py::test_cleanup_orphaned_chunk_doesnt_break_versions[data5-FwPointersCfg.ENABLED] PASSED [ 13%]2021-01-20 04:18:26,034 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_arctic_fsck.py::test_cleanup_orphaned_snapshots[True-data0-FwPointersCfg.DISABLED] PASSED [ 13%]2021-01-20 04:18:26,912 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_arctic_fsck.py::test_cleanup_orphaned_snapshots[True-data1-FwPointersCfg.HYBRID] PASSED [ 13%]2021-01-20 04:18:27,793 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_arctic_fsck.py::test_cleanup_orphaned_snapshots[True-data2-FwPointersCfg.ENABLED] PASSED [ 13%]2021-01-20 04:18:28,668 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_arctic_fsck.py::test_cleanup_orphaned_snapshots[True-data3-FwPointersCfg.DISABLED] PASSED [ 13%]2021-01-20 04:18:29,562 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_arctic_fsck.py::test_cleanup_orphaned_snapshots[True-data4-FwPointersCfg.HYBRID] PASSED [ 13%]2021-01-20 04:18:30,461 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_arctic_fsck.py::test_cleanup_orphaned_snapshots[True-data5-FwPointersCfg.ENABLED] PASSED [ 13%]2021-01-20 04:18:31,359 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_arctic_fsck.py::test_cleanup_orphaned_snapshots[False-data6-FwPointersCfg.DISABLED] PASSED [ 13%]2021-01-20 04:18:32,238 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_arctic_fsck.py::test_cleanup_orphaned_snapshots[False-data7-FwPointersCfg.HYBRID] PASSED [ 14%]2021-01-20 04:18:33,119 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_arctic_fsck.py::test_cleanup_orphaned_snapshots[False-data8-FwPointersCfg.ENABLED] PASSED [ 14%]2021-01-20 04:18:34,005 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_arctic_fsck.py::test_cleanup_orphaned_snapshots[False-data9-FwPointersCfg.DISABLED] PASSED [ 14%]2021-01-20 04:18:34,903 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_arctic_fsck.py::test_cleanup_orphaned_snapshots[False-data10-FwPointersCfg.HYBRID] PASSED [ 14%]2021-01-20 04:18:35,811 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_arctic_fsck.py::test_cleanup_orphaned_snapshots[False-data11-FwPointersCfg.ENABLED] PASSED [ 14%]2021-01-20 04:18:36,718 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_arctic_fsck.py::test_cleanup_orphaned_snapshots_nop[True-data0-FwPointersCfg.DISABLED] PASSED [ 14%]2021-01-20 04:18:37,600 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_arctic_fsck.py::test_cleanup_orphaned_snapshots_nop[True-data1-FwPointersCfg.HYBRID] PASSED [ 14%]2021-01-20 04:18:38,482 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_arctic_fsck.py::test_cleanup_orphaned_snapshots_nop[True-data2-FwPointersCfg.ENABLED] PASSED [ 14%]2021-01-20 04:18:39,358 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_arctic_fsck.py::test_cleanup_orphaned_snapshots_nop[True-data3-FwPointersCfg.DISABLED] PASSED [ 14%]2021-01-20 04:18:40,255 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_arctic_fsck.py::test_cleanup_orphaned_snapshots_nop[True-data4-FwPointersCfg.HYBRID] PASSED [ 14%]2021-01-20 04:18:41,153 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_arctic_fsck.py::test_cleanup_orphaned_snapshots_nop[True-data5-FwPointersCfg.ENABLED] PASSED [ 14%]2021-01-20 04:18:42,047 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_arctic_fsck.py::test_cleanup_orphaned_snapshots_nop[False-data6-FwPointersCfg.DISABLED] PASSED [ 14%]2021-01-20 04:18:42,925 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_arctic_fsck.py::test_cleanup_orphaned_snapshots_nop[False-data7-FwPointersCfg.HYBRID] PASSED [ 14%]2021-01-20 04:18:43,801 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_arctic_fsck.py::test_cleanup_orphaned_snapshots_nop[False-data8-FwPointersCfg.ENABLED] PASSED [ 15%]2021-01-20 04:18:44,680 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_arctic_fsck.py::test_cleanup_orphaned_snapshots_nop[False-data9-FwPointersCfg.DISABLED] PASSED [ 15%]2021-01-20 04:18:45,576 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_arctic_fsck.py::test_cleanup_orphaned_snapshots_nop[False-data10-FwPointersCfg.HYBRID] PASSED [ 15%]2021-01-20 04:18:46,472 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_arctic_fsck.py::test_cleanup_orphaned_snapshots_nop[False-data11-FwPointersCfg.ENABLED] PASSED [ 15%]2021-01-20 04:18:47,379 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_arctic_fsck.py::test_dont_cleanup_recent_orphaned_snapshots[True-data0-FwPointersCfg.DISABLED] PASSED [ 15%]2021-01-20 04:18:48,262 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_arctic_fsck.py::test_dont_cleanup_recent_orphaned_snapshots[True-data1-FwPointersCfg.HYBRID] PASSED [ 15%]2021-01-20 04:18:49,153 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_arctic_fsck.py::test_dont_cleanup_recent_orphaned_snapshots[True-data2-FwPointersCfg.ENABLED] PASSED [ 15%]2021-01-20 04:18:50,034 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_arctic_fsck.py::test_dont_cleanup_recent_orphaned_snapshots[True-data3-FwPointersCfg.DISABLED] PASSED [ 15%]2021-01-20 04:18:50,938 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_arctic_fsck.py::test_dont_cleanup_recent_orphaned_snapshots[True-data4-FwPointersCfg.HYBRID] PASSED [ 15%]2021-01-20 04:18:51,833 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_arctic_fsck.py::test_dont_cleanup_recent_orphaned_snapshots[True-data5-FwPointersCfg.ENABLED] PASSED [ 15%]2021-01-20 04:18:52,728 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_arctic_fsck.py::test_dont_cleanup_recent_orphaned_snapshots[False-data6-FwPointersCfg.DISABLED] PASSED [ 15%]2021-01-20 04:18:53,608 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_arctic_fsck.py::test_dont_cleanup_recent_orphaned_snapshots[False-data7-FwPointersCfg.HYBRID] PASSED [ 15%]2021-01-20 04:18:54,488 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_arctic_fsck.py::test_dont_cleanup_recent_orphaned_snapshots[False-data8-FwPointersCfg.ENABLED] PASSED [ 15%]2021-01-20 04:18:55,367 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_arctic_fsck.py::test_dont_cleanup_recent_orphaned_snapshots[False-data9-FwPointersCfg.DISABLED] PASSED [ 15%]2021-01-20 04:18:56,263 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_arctic_fsck.py::test_dont_cleanup_recent_orphaned_snapshots[False-data10-FwPointersCfg.HYBRID] PASSED [ 16%]2021-01-20 04:18:57,161 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_arctic_fsck.py::test_dont_cleanup_recent_orphaned_snapshots[False-data11-FwPointersCfg.ENABLED] PASSED [ 16%]2021-01-20 04:18:58,056 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_copy_data.py::test_copy_data_no_force PASSED [ 16%]2021-01-20 04:18:59,172 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_copy_data.py::test_copy_data_force PASSED [ 16%]2021-01-20 04:19:00,305 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_copy_data.py::test_copy_data_splice PASSED [ 16%]2021-01-20 04:19:01,446 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_copy_data.py::test_copy_data_wild PASSED  [ 16%]2021-01-20 04:19:02,565 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_copy_data.py::test_copy_data_doesnt_exist PASSED [ 16%]2021-01-20 04:19:03,577 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_delete_library.py::test_delete_library PASSED [ 16%]2021-01-20 04:19:04,704 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_delete_library.py::test_delete_library1 PASSED [ 16%]2021-01-20 04:19:05,815 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_delete_library.py::test_delete_library2 PASSED [ 16%]2021-01-20 04:19:06,927 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_delete_library.py::test_delete_library3 PASSED [ 16%]2021-01-20 04:19:08,032 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_delete_library.py::test_delete_library_doesnt_exist PASSED [ 16%]2021-01-20 04:19:09,049 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_enable_sharding.py::test_enable_sharding PASSED [ 16%]2021-01-20 04:19:09,868 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_enable_sharding.py::test_enable_sharding_already_on_db PASSED [ 17%]2021-01-20 04:19:10,687 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_enable_sharding.py::test_enable_sharding_on_db_other_failure PASSED [ 17%]
tests/integration/scripts/test_initialize_library.py::test_init_library PASSED [ 17%]2021-01-20 04:19:12,347 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_initialize_library.py::test_init_library_no_arctic_prefix PASSED [ 17%]2021-01-20 04:19:13,192 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_initialize_library.py::test_init_library_quota PASSED [ 17%]2021-01-20 04:19:14,024 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_initialize_library.py::test_init_library_bad_library PASSED [ 17%]2021-01-20 04:19:14,660 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_list_libraries.py::test_list_library PASSED [ 17%]2021-01-20 04:19:15,484 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_list_libraries.py::test_list_library_args PASSED [ 17%]2021-01-20 04:19:16,313 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_list_libraries.py::test_list_library_args_not_found PASSED [ 17%]2021-01-20 04:19:17,136 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_prune_versions.py::test_prune_versions_symbol PASSED [ 17%]2021-01-20 04:19:17,963 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_prune_versions.py::test_prune_versions_full PASSED [ 17%]2021-01-20 04:19:18,854 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_prune_versions.py::test_keep_recent_snapshots PASSED [ 17%]2021-01-20 04:19:19,691 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_prune_versions.py::test_fix_broken_snapshot_references PASSED [ 17%]2021-01-20 04:19:20,534 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/scripts/test_prune_versions.py::test_keep_only_one_version PASSED [ 17%]2021-01-20 04:19:21,383 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_bitemporal_store.py::test_new_ts_read_write PASSED [ 18%]2021-01-20 04:19:22,239 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_bitemporal_store.py::test_read_ts_raw PASSED [ 18%]2021-01-20 04:19:23,112 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_bitemporal_store.py::test_write_ts_with_column_name_same_as_observed_dt_ok PASSED [ 18%]2021-01-20 04:19:23,981 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_bitemporal_store.py::test_last_update PASSED [ 18%]2021-01-20 04:19:24,852 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_bitemporal_store.py::test_existing_ts_update_and_read PASSED [ 18%]2021-01-20 04:19:25,729 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_bitemporal_store.py::test_existing_ts_update_existing_data_and_read PASSED [ 18%]2021-01-20 04:19:26,617 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_bitemporal_store.py::test_read_ts_with_historical_update PASSED [ 18%]2021-01-20 04:19:27,557 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_bitemporal_store.py::test_read_ts_with_historical_update_and_new_row PASSED [ 18%]2021-01-20 04:19:28,463 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_bitemporal_store.py::test_insert_new_rows_in_middle_remains_sorted PASSED [ 18%]2021-01-20 04:19:29,350 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_bitemporal_store.py::test_insert_versions_inbetween_works_ok PASSED [ 18%]2021-01-20 04:19:30,296 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_bitemporal_store.py::test_read_ts_raw_all_version_ok PASSED [ 18%]2021-01-20 04:19:31,250 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_bitemporal_store.py::test_bitemporal_store_saves_as_of_with_timezone PASSED [ 18%]2021-01-20 04:19:32,119 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_bitemporal_store.py::test_bitemporal_store_read_as_of_timezone PASSED [ 18%]2021-01-20 04:19:33,028 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_bitemporal_store.py::test_multi_index_ts_read_write PASSED [ 19%]2021-01-20 04:19:33,896 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_bitemporal_store.py::test_multi_index_ts_read_raw PASSED [ 19%]2021-01-20 04:19:34,777 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_bitemporal_store.py::test_multi_index_update PASSED [ 19%]2021-01-20 04:19:35,693 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_metadata_store.py::test_pickle PASSED       [ 19%]2021-01-20 04:19:36,430 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_metadata_store.py::test_has_symbol PASSED   [ 19%]2021-01-20 04:19:37,158 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_metadata_store.py::test_list_symbols PASSED [ 19%]2021-01-20 04:19:37,888 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_metadata_store.py::test_read_history PASSED [ 19%]2021-01-20 04:19:38,623 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_metadata_store.py::test_read PASSED         [ 19%]2021-01-20 04:19:39,353 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_metadata_store.py::test_write_history PASSED [ 19%]2021-01-20 04:19:40,093 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_metadata_store.py::test_append PASSED       [ 19%]2021-01-20 04:19:40,836 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_metadata_store.py::test_prepend PASSED      [ 19%]2021-01-20 04:19:41,582 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_metadata_store.py::test_pop PASSED          [ 19%]2021-01-20 04:19:42,320 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_metadata_store.py::test_purge PASSED        [ 19%]2021-01-20 04:19:43,048 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_ndarray_store.py::test_write_new_column_name_to_arctic_1_40_data PASSED [ 20%]2021-01-20 04:19:44,075 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_ndarray_store.py::test_save_read_simple_ndarray PASSED [ 20%]2021-01-20 04:19:44,913 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_ndarray_store.py::test_read_simple_ndarray_from_secondary XFAIL [ 20%]
tests/integration/store/test_ndarray_store.py::test_save_read_big_1darray[FwPointersCfg.DISABLED] PASSED [ 20%]2021-01-20 04:19:50,498 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_ndarray_store.py::test_save_read_big_1darray[FwPointersCfg.HYBRID] PASSED [ 20%]2021-01-20 04:19:55,146 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_ndarray_store.py::test_save_read_big_1darray[FwPointersCfg.ENABLED] PASSED [ 20%]2021-01-20 04:19:59,790 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_ndarray_store.py::test_save_and_resave_reuses_chunks[FwPointersCfg.DISABLED] PASSED [ 20%]2021-01-20 04:20:00,654 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_ndarray_store.py::test_save_and_resave_reuses_chunks[FwPointersCfg.HYBRID] PASSED [ 20%]2021-01-20 04:20:01,507 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_ndarray_store.py::test_save_and_resave_reuses_chunks[FwPointersCfg.ENABLED] PASSED [ 20%]2021-01-20 04:20:02,359 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_ndarray_store.py::test_save_read_big_2darray[FwPointersCfg.DISABLED] PASSED [ 20%]2021-01-20 04:20:06,888 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_ndarray_store.py::test_save_read_big_2darray[FwPointersCfg.HYBRID] PASSED [ 20%]2021-01-20 04:20:11,560 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_ndarray_store.py::test_save_read_big_2darray[FwPointersCfg.ENABLED] PASSED [ 20%]2021-01-20 04:20:16,062 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_ndarray_store.py::test_get_info_bson_object PASSED [ 20%]2021-01-20 04:20:16,900 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_ndarray_store.py::test_save_read_ndarray_with_array_field PASSED [ 20%]2021-01-20 04:20:17,736 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_ndarray_store.py::test_save_read_ndarray PASSED [ 21%]2021-01-20 04:20:18,572 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_ndarray_store.py::test_multiple_write[FwPointersCfg.DISABLED] PASSED [ 21%]2021-01-20 04:20:19,425 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_ndarray_store.py::test_multiple_write[FwPointersCfg.HYBRID] PASSED [ 21%]2021-01-20 04:20:20,285 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_ndarray_store.py::test_multiple_write[FwPointersCfg.ENABLED] PASSED [ 21%]2021-01-20 04:20:21,140 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_ndarray_store.py::test_cant_write_objects PASSED [ 21%]
tests/integration/store/test_ndarray_store.py::test_save_read_large_ndarray PASSED [ 21%]2021-01-20 04:20:22,369 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_ndarray_store.py::test_mutable_ndarray PASSED [ 21%]2021-01-20 04:20:23,205 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_ndarray_store.py::test_delete_version_shouldnt_break_read XPASS [ 21%]2021-01-20 04:20:24,048 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_ndarray_store_append.py::test_append_simple_ndarray[FwPointersCfg.DISABLED] PASSED [ 21%]2021-01-20 04:20:24,902 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_ndarray_store_append.py::test_append_simple_ndarray[FwPointersCfg.HYBRID] PASSED [ 21%]2021-01-20 04:20:25,752 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_ndarray_store_append.py::test_append_simple_ndarray[FwPointersCfg.ENABLED] PASSED [ 21%]2021-01-20 04:20:26,604 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_ndarray_store_append.py::test_append_simple_ndarray_promoting_types[FwPointersCfg.DISABLED] PASSED [ 21%]2021-01-20 04:20:27,453 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_ndarray_store_append.py::test_append_simple_ndarray_promoting_types[FwPointersCfg.HYBRID] PASSED [ 21%]2021-01-20 04:20:28,294 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_ndarray_store_append.py::test_append_simple_ndarray_promoting_types[FwPointersCfg.ENABLED] PASSED [ 22%]2021-01-20 04:20:29,143 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_ndarray_store_append.py::test_promote_types PASSED [ 22%]2021-01-20 04:20:29,985 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_ndarray_store_append.py::test_promote_types2 PASSED [ 22%]2021-01-20 04:20:30,819 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_ndarray_store_append.py::test_promote_types_smaller_sizes PASSED [ 22%]2021-01-20 04:20:31,656 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_ndarray_store_append.py::test_promote_types_larger_sizes PASSED [ 22%]2021-01-20 04:20:32,498 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_ndarray_store_append.py::test_promote_field_types_smaller_sizes PASSED [ 22%]2021-01-20 04:20:33,340 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_ndarray_store_append.py::test_promote_field_types_larger_sizes PASSED [ 22%]2021-01-20 04:20:34,187 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_ndarray_store_append.py::test_append_ndarray_with_field_shape[FwPointersCfg.DISABLED] PASSED [ 22%]2021-01-20 04:20:35,029 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_ndarray_store_append.py::test_append_ndarray_with_field_shape[FwPointersCfg.HYBRID] PASSED [ 22%]2021-01-20 04:20:35,867 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_ndarray_store_append.py::test_append_ndarray_with_field_shape[FwPointersCfg.ENABLED] PASSED [ 22%]2021-01-20 04:20:36,704 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_ndarray_store_append.py::test_append_read_large_ndarray[FwPointersCfg.DISABLED] PASSED [ 22%]2021-01-20 04:20:39,240 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_ndarray_store_append.py::test_append_read_large_ndarray[FwPointersCfg.HYBRID] PASSED [ 22%]2021-01-20 04:20:41,811 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_ndarray_store_append.py::test_append_read_large_ndarray[FwPointersCfg.ENABLED] PASSED [ 22%]2021-01-20 04:20:44,297 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_ndarray_store_append.py::test_save_append_read_ndarray[FwPointersCfg.DISABLED] PASSED [ 23%]2021-01-20 04:20:45,627 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_ndarray_store_append.py::test_save_append_read_ndarray[FwPointersCfg.HYBRID] PASSED [ 23%]2021-01-20 04:20:46,956 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_ndarray_store_append.py::test_save_append_read_ndarray[FwPointersCfg.ENABLED] PASSED [ 23%]2021-01-20 04:20:48,291 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_ndarray_store_append.py::test_save_append_read_1row_ndarray PASSED [ 23%]2021-01-20 04:20:49,616 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_ndarray_store_append.py::test_append_too_large_ndarray PASSED [ 23%]2021-01-20 04:20:51,228 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_ndarray_store_append.py::test_empty_field_append_keeps_all_columns PASSED [ 23%]2021-01-20 04:20:52,066 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_ndarray_store_append.py::test_empty_append_promotes_dtype[FwPointersCfg.DISABLED] PASSED [ 23%]2021-01-20 04:20:52,906 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_ndarray_store_append.py::test_empty_append_promotes_dtype[FwPointersCfg.HYBRID] PASSED [ 23%]2021-01-20 04:20:53,749 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_ndarray_store_append.py::test_empty_append_promotes_dtype[FwPointersCfg.ENABLED] PASSED [ 23%]2021-01-20 04:20:54,588 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_ndarray_store_append.py::test_empty_append_promotes_dtype2 PASSED [ 23%]2021-01-20 04:20:55,433 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_ndarray_store_append.py::test_empty_append_promotes_dtype3 PASSED [ 23%]2021-01-20 04:20:56,275 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_ndarray_store_append.py::test_convert_to_structured_array PASSED [ 23%]2021-01-20 04:20:57,112 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_ndarray_store_append.py::test_empty_append_concat_and_rewrite[FwPointersCfg.DISABLED] PASSED [ 23%]2021-01-20 04:20:58,002 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_ndarray_store_append.py::test_empty_append_concat_and_rewrite[FwPointersCfg.HYBRID] PASSED [ 23%]2021-01-20 04:20:58,895 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_ndarray_store_append.py::test_empty_append_concat_and_rewrite[FwPointersCfg.ENABLED] PASSED [ 24%]2021-01-20 04:20:59,783 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_ndarray_store_append.py::test_empty_append_concat_and_rewrite_2[FwPointersCfg.DISABLED] PASSED [ 24%]2021-01-20 04:21:00,854 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_ndarray_store_append.py::test_empty_append_concat_and_rewrite_2[FwPointersCfg.HYBRID] PASSED [ 24%]2021-01-20 04:21:01,944 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_ndarray_store_append.py::test_empty_append_concat_and_rewrite_2[FwPointersCfg.ENABLED] PASSED [ 24%]2021-01-20 04:21:03,031 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_ndarray_store_append.py::test_empty_append_concat_and_rewrite_3[FwPointersCfg.DISABLED] PASSED [ 24%]2021-01-20 04:21:03,919 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_ndarray_store_append.py::test_empty_append_concat_and_rewrite_3[FwPointersCfg.HYBRID] PASSED [ 24%]2021-01-20 04:21:04,820 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_ndarray_store_append.py::test_empty_append_concat_and_rewrite_3[FwPointersCfg.ENABLED] PASSED [ 24%]2021-01-20 04:21:05,712 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_ndarray_store_append.py::test_append_with_extra_columns PASSED [ 24%]2021-01-20 04:21:06,565 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_ndarray_store_append.py::test_save_append_delete_append[FwPointersCfg.DISABLED] PASSED [ 24%]2021-01-20 04:21:07,419 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_ndarray_store_append.py::test_save_append_delete_append[FwPointersCfg.HYBRID] PASSED [ 24%]2021-01-20 04:21:08,268 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_ndarray_store_append.py::test_save_append_delete_append[FwPointersCfg.ENABLED] PASSED [ 24%]2021-01-20 04:21:09,121 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_ndarray_store_append.py::test_append_after_failed_append[FwPointersCfg.DISABLED] PASSED [ 24%]2021-01-20 04:21:09,978 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_ndarray_store_append.py::test_append_after_failed_append[FwPointersCfg.HYBRID] PASSED [ 24%]2021-01-20 04:21:10,836 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_ndarray_store_append.py::test_append_after_failed_append[FwPointersCfg.ENABLED] PASSED [ 25%]2021-01-20 04:21:11,692 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_ndarray_store_append.py::test_append_reorder_columns PASSED [ 25%]2021-01-20 04:21:12,550 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_write_multi_column_to_arctic_1_40_data PASSED [ 25%]2021-01-20 04:21:13,408 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_save_read_pandas_series PASSED [ 25%]2021-01-20 04:21:14,254 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_save_read_pandas_series_maintains_name PASSED [ 25%]2021-01-20 04:21:15,102 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_save_read_pandas_series_with_multiindex PASSED [ 25%]2021-01-20 04:21:15,951 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_save_read_pandas_series_with_multiindex_and_name PASSED [ 25%]2021-01-20 04:21:16,817 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_save_read_pandas_series_with_unicode_index_name PASSED [ 25%]2021-01-20 04:21:17,690 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_save_read_pandas_dataframe_with_multiindex PASSED [ 25%]2021-01-20 04:21:18,558 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_save_read_pandas_dataframe_with_none_values PASSED [ 25%]2021-01-20 04:21:19,419 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_save_read_pandas_dataframe_with_unicode_index_name PASSED [ 25%]2021-01-20 04:21:20,276 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_cant_write_pandas_series_with_tuple_values PASSED [ 25%]2021-01-20 04:21:21,121 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_save_read_pandas_series_with_datetimeindex_with_timezone PASSED [ 25%]2021-01-20 04:21:21,991 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_save_read_pandas_series_with_datetimeindex PASSED [ 25%]2021-01-20 04:21:22,864 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_save_read_pandas_dataframe_with_datetimeindex_with_timezone PASSED [ 26%]2021-01-20 04:21:23,743 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_save_read_pandas_empty_series_with_datetime_multiindex_with_timezone PASSED [ 26%]2021-01-20 04:21:24,608 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_save_read_pandas_dataframe_with_datetimeindex PASSED [ 26%]2021-01-20 04:21:25,481 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_save_read_pandas_dataframe_with_strings PASSED [ 26%]2021-01-20 04:21:26,354 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_save_read_pandas_dataframe PASSED [ 26%]2021-01-20 04:21:27,209 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_save_read_empty_dataframe PASSED [ 26%]2021-01-20 04:21:28,059 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_save_read_pandas_dataframe2 PASSED [ 26%]2021-01-20 04:21:28,904 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_save_read_pandas_dataframe_strings PASSED [ 26%]2021-01-20 04:21:29,756 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_save_read_pandas_dataframe_empty_multiindex PASSED [ 26%]2021-01-20 04:21:30,616 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_save_read_pandas_dataframe_empty_multiindex_and_no_columns PASSED [ 26%]2021-01-20 04:21:31,465 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_save_read_pandas_dataframe_multiindex_and_no_columns PASSED [ 26%]2021-01-20 04:21:32,319 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_append_pandas_multi_columns_dataframe PASSED [ 26%]2021-01-20 04:21:33,191 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_append_pandas_multi_columns_dataframe_new_column PASSED [ 26%]2021-01-20 04:21:34,079 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_save_read_pandas_multi_columns_empty_dataframe PASSED [ 27%]2021-01-20 04:21:34,942 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_save_read_pandas_multi_columns_dataframe PASSED [ 27%]2021-01-20 04:21:35,804 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_save_read_pandas_multi_columns_no_names_dataframe PASSED [ 27%]2021-01-20 04:21:36,647 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_save_read_pandas_multi_columns_dataframe_with_int_levels PASSED [ 27%]2021-01-20 04:21:37,494 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_save_read_multi_index_and_multi_columns_dataframe PASSED [ 27%]2021-01-20 04:21:38,349 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_append_pandas_dataframe PASSED [ 27%]2021-01-20 04:21:39,200 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_empty_dataframe_multindex PASSED [ 27%]2021-01-20 04:21:40,043 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_dataframe_append_empty PASSED [ 27%]2021-01-20 04:21:40,893 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_empy_dataframe_append PASSED [ 27%]2021-01-20 04:21:41,740 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_dataframe_append_empty_multiindex PASSED [ 27%]2021-01-20 04:21:42,593 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_empty_dataframe_append_multiindex PASSED [ 27%]2021-01-20 04:21:43,452 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_empty_dataframe_should_ignore_dtype PASSED [ 27%]2021-01-20 04:21:44,312 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_empty_dataframe_should_ignore_dtype2 PASSED [ 27%]2021-01-20 04:21:45,164 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_dataframe_append_should_promote_string_column PASSED [ 28%]2021-01-20 04:21:46,024 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_dataframe_append_should_add_new_column PASSED [ 28%]2021-01-20 04:21:46,875 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_dataframe_append_should_add_new_columns_and_reorder PASSED [ 28%]2021-01-20 04:21:47,734 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_dataframe_save_read[df_size0] PASSED [ 28%]2021-01-20 04:21:48,569 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_dataframe_save_read[df_size1] PASSED [ 28%]2021-01-20 04:21:49,409 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_dataframe_save_read[df_size2] PASSED [ 28%]2021-01-20 04:21:50,250 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_dataframe_save_read[df_size3] PASSED [ 28%]2021-01-20 04:21:51,094 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_dataframe_save_read[df_size4] PASSED [ 28%]2021-01-20 04:21:51,933 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_dataframe_save_read[df_size5] PASSED [ 28%]2021-01-20 04:21:52,772 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_dataframe_save_read[df_size6] PASSED [ 28%]2021-01-20 04:21:53,607 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_dataframe_save_read[df_size7] PASSED [ 28%]2021-01-20 04:21:54,441 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_dataframe_save_read[df_size8] PASSED [ 28%]2021-01-20 04:21:55,281 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_dataframe_save_read[df_size9] PASSED [ 28%]2021-01-20 04:21:56,120 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_dataframe_save_read[df_size10] PASSED [ 28%]2021-01-20 04:21:56,958 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_dataframe_save_read[df_size11] PASSED [ 29%]2021-01-20 04:21:57,798 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_dataframe_save_read[df_size12] PASSED [ 29%]2021-01-20 04:21:58,638 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_dataframe_save_read[df_size13] PASSED [ 29%]2021-01-20 04:21:59,479 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_dataframe_save_read[df_size14] PASSED [ 29%]2021-01-20 04:22:00,321 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_dataframe_save_read[df_size15] PASSED [ 29%]2021-01-20 04:22:01,168 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_dataframe_save_read[df_size16] PASSED [ 29%]2021-01-20 04:22:02,019 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_dataframe_save_read[df_size17] PASSED [ 29%]2021-01-20 04:22:02,866 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_dataframe_save_read[df_size18] PASSED [ 29%]2021-01-20 04:22:03,715 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_dataframe_save_read[df_size19] PASSED [ 29%]2021-01-20 04:22:04,569 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_dataframe_save_append_read[df_size0] PASSED [ 29%]2021-01-20 04:22:05,409 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_dataframe_save_append_read[df_size1] PASSED [ 29%]2021-01-20 04:22:06,249 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_dataframe_save_append_read[df_size2] PASSED [ 29%]2021-01-20 04:22:07,091 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_dataframe_save_append_read[df_size3] PASSED [ 29%]2021-01-20 04:22:07,935 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_dataframe_save_append_read[df_size4] PASSED [ 30%]2021-01-20 04:22:08,779 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_dataframe_save_append_read[df_size5] PASSED [ 30%]2021-01-20 04:22:09,626 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_dataframe_save_append_read[df_size6] PASSED [ 30%]2021-01-20 04:22:10,465 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_dataframe_save_append_read[df_size7] PASSED [ 30%]2021-01-20 04:22:11,312 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_dataframe_save_append_read[df_size8] PASSED [ 30%]2021-01-20 04:22:12,158 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_dataframe_save_append_read[df_size9] PASSED [ 30%]2021-01-20 04:22:13,004 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_dataframe_save_append_read[df_size10] PASSED [ 30%]2021-01-20 04:22:13,845 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_dataframe_save_append_read[df_size11] PASSED [ 30%]2021-01-20 04:22:14,696 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_dataframe_save_append_read[df_size12] PASSED [ 30%]2021-01-20 04:22:15,546 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_dataframe_save_append_read[df_size13] PASSED [ 30%]2021-01-20 04:22:16,390 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_dataframe_save_append_read[df_size14] PASSED [ 30%]2021-01-20 04:22:17,237 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_dataframe_save_append_read[df_size15] PASSED [ 30%]2021-01-20 04:22:18,082 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_dataframe_save_append_read[df_size16] PASSED [ 30%]2021-01-20 04:22:18,932 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_dataframe_save_append_read[df_size17] PASSED [ 30%]2021-01-20 04:22:19,782 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_dataframe_save_append_read[df_size18] PASSED [ 31%]2021-01-20 04:22:20,628 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_dataframe_save_append_read[df_size19] PASSED [ 31%]2021-01-20 04:22:21,475 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_large_dataframe_append_rewrite_same_item PASSED [ 31%]2021-01-20 04:22:22,752 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_large_dataframe_rewrite_same_item PASSED [ 31%]2021-01-20 04:22:25,020 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_append_after_truncate_after_append PASSED [ 31%]2021-01-20 04:22:25,902 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_can_write_pandas_df_with_object_columns PASSED [ 31%]2021-01-20 04:22:26,758 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_panel_save_read[df_size0] XFAIL [ 31%]
tests/integration/store/test_pandas_store.py::test_panel_save_read[df_size1] XFAIL [ 31%]
tests/integration/store/test_pandas_store.py::test_panel_save_read[df_size2] XFAIL [ 31%]
tests/integration/store/test_pandas_store.py::test_panel_save_read[df_size3] XFAIL [ 31%]
tests/integration/store/test_pandas_store.py::test_panel_save_read[df_size4] XFAIL [ 31%]
tests/integration/store/test_pandas_store.py::test_panel_save_read[df_size5] 2021-01-20 04:22:32,465 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
2021-01-20 04:22:32,465 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
2021-01-20 04:22:32,465 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
2021-01-20 04:22:32,466 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
2021-01-20 04:22:32,466 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
XFAIL [ 31%]
tests/integration/store/test_pandas_store.py::test_panel_save_read[df_size6] XFAIL [ 31%]
tests/integration/store/test_pandas_store.py::test_panel_save_read[df_size7] XFAIL [ 32%]
tests/integration/store/test_pandas_store.py::test_panel_save_read[df_size8] XFAIL [ 32%]
tests/integration/store/test_pandas_store.py::test_panel_save_read[df_size9] XFAIL [ 32%]
tests/integration/store/test_pandas_store.py::test_panel_save_read_with_nans XFAIL [ 32%]
tests/integration/store/test_pandas_store.py::test_save_read_ints PASSED [ 32%]2021-01-20 04:22:38,053 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_save_read_datetimes PASSED [ 32%]2021-01-20 04:22:38,905 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_labels PASSED         [ 32%]2021-01-20 04:22:39,753 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_duplicate_labels PASSED [ 32%]2021-01-20 04:22:40,613 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_no_labels PASSED      [ 32%]2021-01-20 04:22:41,479 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_no_index_labels 2021-01-20 04:22:42,439 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
2021-01-20 04:22:42,439 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
2021-01-20 04:22:42,440 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
2021-01-20 04:22:42,440 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
2021-01-20 04:22:42,440 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
2021-01-20 04:22:42,440 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
XFAIL [ 32%]
tests/integration/store/test_pandas_store.py::test_not_unique PASSED     [ 32%]2021-01-20 04:22:43,355 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_daterange_end PASSED  [ 32%]2021-01-20 04:22:44,629 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_daterange_start PASSED [ 32%]2021-01-20 04:22:45,901 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_daterange_with_zero_index PASSED [ 33%]2021-01-20 04:22:46,775 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_daterange_large_DataFrame PASSED [ 33%]2021-01-20 04:22:48,267 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_daterange_large_DataFrame_middle PASSED [ 33%]2021-01-20 04:22:54,220 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_daterange[df0-assert_frame_equal] PASSED [ 33%]2021-01-20 04:22:55,186 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_daterange[df1-assert_series_equal] PASSED [ 33%]2021-01-20 04:22:56,143 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_daterange_append PASSED [ 33%]2021-01-20 04:22:57,928 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_daterange_single_chunk PASSED [ 33%]2021-01-20 04:22:58,796 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_daterange_when_end_beyond_chunk_index PASSED [ 33%]2021-01-20 04:22:59,658 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_daterange_when_end_beyond_chunk_index_no_start PASSED [ 33%]2021-01-20 04:23:00,520 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_daterange_fails_with_timezone_start PASSED [ 33%]2021-01-20 04:23:01,371 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_data_info_series PASSED [ 33%]2021-01-20 04:23:02,220 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_data_info_df PASSED   [ 33%]2021-01-20 04:23:03,067 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_data_info_cols PASSED [ 33%]2021-01-20 04:23:03,914 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_read_write_multiindex_store_keeps_timezone PASSED [ 33%]2021-01-20 04:23:04,779 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_mutable_df PASSED     [ 34%]2021-01-20 04:23:05,625 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_forced_encodings_with_df_mixed_types SKIPPED [ 34%]
tests/integration/store/test_pandas_store.py::test_forced_encodings_with_df SKIPPED [ 34%]
tests/integration/store/test_pandas_store.py::test_forced_encodings_with_df_py3 PASSED [ 34%]2021-01-20 04:23:06,503 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pandas_store.py::test_forced_encodings_with_df_py3_multi_index PASSED [ 34%]2021-01-20 04:23:07,393 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pickle_store.py::test_save_read_bson PASSED [ 34%]2021-01-20 04:23:08,229 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pickle_store.py::test_save_read_big_encodable PASSED [ 34%]2021-01-20 04:23:09,222 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pickle_store.py::test_save_read_bson_object PASSED [ 34%]2021-01-20 04:23:10,067 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pickle_store.py::test_get_info_bson_object PASSED [ 34%]2021-01-20 04:23:10,909 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pickle_store.py::test_bson_large_object PASSED [ 34%]2021-01-20 04:23:12,072 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pickle_store.py::test_bson_leak_objects_delete PASSED [ 34%]2021-01-20 04:23:12,927 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pickle_store.py::test_bson_leak_objects_prune_previous PASSED [ 34%]2021-01-20 04:23:13,778 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pickle_store.py::test_prune_previous_doesnt_kill_other_objects PASSED [ 34%]2021-01-20 04:23:14,639 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_pickle_store.py::test_write_metadata PASSED [ 35%]2021-01-20 04:23:15,485 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_store_item_new_version PASSED [ 35%]2021-01-20 04:23:16,333 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_store_item_read_preference XFAIL [ 35%]
tests/integration/store/test_version_store.py::test_read_item_read_preference_SECONDARY XFAIL [ 35%]
tests/integration/store/test_version_store.py::test_store_item_metadata[FwPointersCfg.DISABLED] PASSED [ 35%]2021-01-20 04:23:19,081 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_store_item_metadata[FwPointersCfg.HYBRID] PASSED [ 35%]2021-01-20 04:23:19,931 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_store_item_metadata[FwPointersCfg.ENABLED] PASSED [ 35%]2021-01-20 04:23:20,778 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_read_metadata[FwPointersCfg.DISABLED] PASSED [ 35%]2021-01-20 04:23:21,615 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_read_metadata[FwPointersCfg.HYBRID] PASSED [ 35%]2021-01-20 04:23:22,453 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_read_metadata[FwPointersCfg.ENABLED] PASSED [ 35%]2021-01-20 04:23:23,301 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_read_metadata_newer_version_with_lower_id[FwPointersCfg.DISABLED] PASSED [ 35%]2021-01-20 04:23:24,157 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_read_metadata_newer_version_with_lower_id[FwPointersCfg.HYBRID] PASSED [ 35%]2021-01-20 04:23:25,014 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_read_metadata_newer_version_with_lower_id[FwPointersCfg.ENABLED] PASSED [ 35%]2021-01-20 04:23:25,868 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_read_metadata_throws_on_deleted_symbol[FwPointersCfg.DISABLED] PASSED [ 35%]2021-01-20 04:23:26,725 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_read_metadata_throws_on_deleted_symbol[FwPointersCfg.HYBRID] PASSED [ 36%]2021-01-20 04:23:27,578 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_read_metadata_throws_on_deleted_symbol[FwPointersCfg.ENABLED] PASSED [ 36%]2021-01-20 04:23:28,432 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_store_item_and_update[FwPointersCfg.DISABLED] PASSED [ 36%]2021-01-20 04:23:32,333 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_store_item_and_update[FwPointersCfg.HYBRID] PASSED [ 36%]2021-01-20 04:23:36,243 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_store_item_and_update[FwPointersCfg.ENABLED] PASSED [ 36%]2021-01-20 04:23:40,147 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_append_update[FwPointersCfg.DISABLED] PASSED [ 36%]2021-01-20 04:23:41,091 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_append_update[FwPointersCfg.HYBRID] PASSED [ 36%]2021-01-20 04:23:42,031 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_append_update[FwPointersCfg.ENABLED] PASSED [ 36%]2021-01-20 04:23:42,967 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_append[FwPointersCfg.DISABLED] PASSED [ 36%]2021-01-20 04:23:43,813 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_append[FwPointersCfg.HYBRID] PASSED [ 36%]2021-01-20 04:23:44,654 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_append[FwPointersCfg.ENABLED] PASSED [ 36%]2021-01-20 04:23:45,492 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_append_should_overwrite_after_delete[FwPointersCfg.DISABLED] PASSED [ 36%]2021-01-20 04:23:46,364 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_append_should_overwrite_after_delete[FwPointersCfg.HYBRID] PASSED [ 36%]2021-01-20 04:23:47,237 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_append_should_overwrite_after_delete[FwPointersCfg.ENABLED] PASSED [ 37%]2021-01-20 04:23:48,112 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_append_empty_ts[FwPointersCfg.DISABLED] PASSED [ 37%]2021-01-20 04:23:48,958 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_append_empty_ts[FwPointersCfg.HYBRID] PASSED [ 37%]2021-01-20 04:23:49,802 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_append_empty_ts[FwPointersCfg.ENABLED] PASSED [ 37%]2021-01-20 04:23:50,645 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_append_corrupted_new_version[FwPointersCfg.DISABLED] PASSED [ 37%]2021-01-20 04:23:51,513 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_append_corrupted_new_version[FwPointersCfg.HYBRID] PASSED [ 37%]2021-01-20 04:23:52,378 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_append_corrupted_new_version[FwPointersCfg.ENABLED] PASSED [ 37%]2021-01-20 04:23:53,249 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_query_version_as_of_int PASSED [ 37%]2021-01-20 04:23:54,107 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_list_version[FwPointersCfg.DISABLED] PASSED [ 37%]2021-01-20 04:23:54,971 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_list_version[FwPointersCfg.HYBRID] PASSED [ 37%]2021-01-20 04:23:55,831 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_list_version[FwPointersCfg.ENABLED] PASSED [ 37%]2021-01-20 04:23:56,692 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_list_version_deleted PASSED [ 37%]2021-01-20 04:23:57,538 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_list_version_latest_only PASSED [ 37%]2021-01-20 04:23:58,402 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_list_version_snapshot PASSED [ 38%]2021-01-20 04:23:59,282 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_delete_versions[FwPointersCfg.DISABLED] PASSED [ 38%]2021-01-20 04:24:00,171 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_delete_versions[FwPointersCfg.HYBRID] PASSED [ 38%]2021-01-20 04:24:01,060 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_delete_versions[FwPointersCfg.ENABLED] PASSED [ 38%]2021-01-20 04:24:01,945 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_delete_bson_versions[FwPointersCfg.DISABLED] PASSED [ 38%]2021-01-20 04:24:02,801 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_delete_bson_versions[FwPointersCfg.HYBRID] PASSED [ 38%]2021-01-20 04:24:03,668 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_delete_bson_versions[FwPointersCfg.ENABLED] PASSED [ 38%]2021-01-20 04:24:04,537 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_read_none_does_not_exception[FwPointersCfg.DISABLED] PASSED [ 38%]2021-01-20 04:24:05,378 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_read_none_does_not_exception[FwPointersCfg.HYBRID] PASSED [ 38%]2021-01-20 04:24:06,220 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_read_none_does_not_exception[FwPointersCfg.ENABLED] PASSED [ 38%]2021-01-20 04:24:07,063 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_delete_item_has_symbol[FwPointersCfg.DISABLED] PASSED [ 38%]2021-01-20 04:24:07,954 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_delete_item_has_symbol[FwPointersCfg.HYBRID] PASSED [ 38%]2021-01-20 04:24:08,835 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_delete_item_has_symbol[FwPointersCfg.ENABLED] PASSED [ 38%]2021-01-20 04:24:09,712 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_delete_item_snapshot[FwPointersCfg.DISABLED] PASSED [ 38%]2021-01-20 04:24:10,616 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_delete_item_snapshot[FwPointersCfg.HYBRID] PASSED [ 39%]2021-01-20 04:24:11,527 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_delete_item_snapshot[FwPointersCfg.ENABLED] PASSED [ 39%]2021-01-20 04:24:12,432 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_has_symbol PASSED    [ 39%]2021-01-20 04:24:13,274 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_snapshot[FwPointersCfg.DISABLED] PASSED [ 39%]2021-01-20 04:24:14,181 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_snapshot[FwPointersCfg.HYBRID] PASSED [ 39%]2021-01-20 04:24:15,087 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_snapshot[FwPointersCfg.ENABLED] PASSED [ 39%]2021-01-20 04:24:15,994 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_snapshot_with_versions[FwPointersCfg.DISABLED] PASSED [ 39%]2021-01-20 04:24:16,893 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_snapshot_with_versions[FwPointersCfg.HYBRID] PASSED [ 39%]2021-01-20 04:24:17,786 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_snapshot_with_versions[FwPointersCfg.ENABLED] PASSED [ 39%]2021-01-20 04:24:18,673 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_snapshot_exclusion[FwPointersCfg.DISABLED] PASSED [ 39%]2021-01-20 04:24:19,526 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_snapshot_exclusion[FwPointersCfg.HYBRID] PASSED [ 39%]2021-01-20 04:24:20,378 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_snapshot_exclusion[FwPointersCfg.ENABLED] PASSED [ 39%]2021-01-20 04:24:21,230 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_snapshot_delete[FwPointersCfg.DISABLED] PASSED [ 39%]2021-01-20 04:24:22,108 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_snapshot_delete[FwPointersCfg.HYBRID] PASSED [ 40%]2021-01-20 04:24:22,986 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_snapshot_delete[FwPointersCfg.ENABLED] PASSED [ 40%]2021-01-20 04:24:23,864 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_multiple_snapshots[FwPointersCfg.DISABLED] PASSED [ 40%]2021-01-20 04:24:24,754 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_multiple_snapshots[FwPointersCfg.HYBRID] PASSED [ 40%]2021-01-20 04:24:25,654 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_multiple_snapshots[FwPointersCfg.ENABLED] PASSED [ 40%]2021-01-20 04:24:26,543 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_delete_identical_snapshots PASSED [ 40%]2021-01-20 04:24:27,411 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_list_snapshots PASSED [ 40%]2021-01-20 04:24:28,259 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_duplicate_snapshots PASSED [ 40%]2021-01-20 04:24:29,100 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_prunes_multiple_versions[FwPointersCfg.DISABLED] PASSED [ 40%]2021-01-20 04:24:29,953 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_prunes_multiple_versions[FwPointersCfg.HYBRID] PASSED [ 40%]2021-01-20 04:24:30,812 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_prunes_multiple_versions[FwPointersCfg.ENABLED] PASSED [ 40%]2021-01-20 04:24:31,672 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_prunes_doesnt_prune_snapshots[FwPointersCfg.DISABLED] PASSED [ 40%]2021-01-20 04:24:32,548 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_prunes_doesnt_prune_snapshots[FwPointersCfg.HYBRID] PASSED [ 40%]2021-01-20 04:24:33,419 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_prunes_doesnt_prune_snapshots[FwPointersCfg.ENABLED] PASSED [ 41%]2021-01-20 04:24:34,291 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_prunes_multiple_versions_ts[FwPointersCfg.DISABLED] PASSED [ 41%]2021-01-20 04:24:35,183 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_prunes_multiple_versions_ts[FwPointersCfg.HYBRID] PASSED [ 41%]2021-01-20 04:24:36,070 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_prunes_multiple_versions_ts[FwPointersCfg.ENABLED] PASSED [ 41%]2021-01-20 04:24:36,971 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_prunes_doesnt_prune_snapshots_ts[FwPointersCfg.DISABLED] PASSED [ 41%]2021-01-20 04:24:37,911 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_prunes_doesnt_prune_snapshots_ts[FwPointersCfg.HYBRID] PASSED [ 41%]2021-01-20 04:24:38,847 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_prunes_doesnt_prune_snapshots_ts[FwPointersCfg.ENABLED] PASSED [ 41%]2021-01-20 04:24:39,779 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_prunes_multiple_versions_fully_different_tss[FwPointersCfg.DISABLED] PASSED [ 41%]2021-01-20 04:24:40,687 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_prunes_multiple_versions_fully_different_tss[FwPointersCfg.HYBRID] PASSED [ 41%]2021-01-20 04:24:41,601 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_prunes_multiple_versions_fully_different_tss[FwPointersCfg.ENABLED] PASSED [ 41%]2021-01-20 04:24:42,488 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_prunes_doesnt_prune_snapshots_fully_different_tss[FwPointersCfg.DISABLED] PASSED [ 41%]2021-01-20 04:24:43,432 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_prunes_doesnt_prune_snapshots_fully_different_tss[FwPointersCfg.HYBRID] PASSED [ 41%]2021-01-20 04:24:44,380 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_prunes_doesnt_prune_snapshots_fully_different_tss[FwPointersCfg.ENABLED] PASSED [ 41%]2021-01-20 04:24:45,314 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_prunes_previous_version_append_interaction[FwPointersCfg.DISABLED] PASSED [ 41%]2021-01-20 04:24:46,286 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_prunes_previous_version_append_interaction[FwPointersCfg.HYBRID] PASSED [ 42%]2021-01-20 04:24:47,259 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_prunes_previous_version_append_interaction[FwPointersCfg.ENABLED] PASSED [ 42%]2021-01-20 04:24:48,224 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_list_symbols[FwPointersCfg.DISABLED] PASSED [ 42%]2021-01-20 04:24:49,080 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_list_symbols[FwPointersCfg.HYBRID] PASSED [ 42%]2021-01-20 04:24:49,928 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_list_symbols[FwPointersCfg.ENABLED] PASSED [ 42%]2021-01-20 04:24:50,782 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_list_symbols_regex[FwPointersCfg.DISABLED] PASSED [ 42%]2021-01-20 04:24:51,636 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_list_symbols_regex[FwPointersCfg.HYBRID] PASSED [ 42%]2021-01-20 04:24:52,499 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_list_symbols_regex[FwPointersCfg.ENABLED] PASSED [ 42%]2021-01-20 04:24:53,354 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_list_symbols_newer_version_with_lower_id[FwPointersCfg.DISABLED] PASSED [ 42%]2021-01-20 04:24:54,204 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_list_symbols_newer_version_with_lower_id[FwPointersCfg.HYBRID] PASSED [ 42%]2021-01-20 04:24:55,058 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_list_symbols_newer_version_with_lower_id[FwPointersCfg.ENABLED] PASSED [ 42%]2021-01-20 04:24:55,911 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_list_symbols_write_snapshot_write_delete[FwPointersCfg.DISABLED] PASSED [ 42%]2021-01-20 04:24:56,773 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_list_symbols_write_snapshot_write_delete[FwPointersCfg.HYBRID] PASSED [ 42%]2021-01-20 04:24:57,630 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_list_symbols_write_snapshot_write_delete[FwPointersCfg.ENABLED] PASSED [ 43%]2021-01-20 04:24:58,488 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_list_symbols_delete_write[FwPointersCfg.DISABLED] PASSED [ 43%]2021-01-20 04:24:59,344 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_list_symbols_delete_write[FwPointersCfg.HYBRID] PASSED [ 43%]2021-01-20 04:25:00,198 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_list_symbols_delete_write[FwPointersCfg.ENABLED] PASSED [ 43%]2021-01-20 04:25:01,055 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_date_range_large[FwPointersCfg.DISABLED] PASSED [ 43%]2021-01-20 04:25:02,065 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_date_range_large[FwPointersCfg.HYBRID] PASSED [ 43%]2021-01-20 04:25:03,070 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_date_range_large[FwPointersCfg.ENABLED] PASSED [ 43%]2021-01-20 04:25:04,076 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_append_after_empty[FwPointersCfg.DISABLED] PASSED [ 43%]2021-01-20 04:25:07,881 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_append_after_empty[FwPointersCfg.HYBRID] PASSED [ 43%]2021-01-20 04:25:11,803 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_append_after_empty[FwPointersCfg.ENABLED] PASSED [ 43%]2021-01-20 04:25:15,788 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_write_metadata[FwPointersCfg.DISABLED] PASSED [ 43%]2021-01-20 04:25:16,688 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_write_metadata[FwPointersCfg.HYBRID] PASSED [ 43%]2021-01-20 04:25:17,567 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_write_metadata[FwPointersCfg.ENABLED] PASSED [ 43%]2021-01-20 04:25:18,443 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_write_metadata_followed_by_append[FwPointersCfg.DISABLED] PASSED [ 43%]2021-01-20 04:25:21,323 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_write_metadata_followed_by_append[FwPointersCfg.HYBRID] PASSED [ 44%]2021-01-20 04:25:24,198 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_write_metadata_followed_by_append[FwPointersCfg.ENABLED] PASSED [ 44%]2021-01-20 04:25:27,079 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_write_metadata_new_symbol[FwPointersCfg.DISABLED] PASSED [ 44%]2021-01-20 04:25:27,926 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_write_metadata_new_symbol[FwPointersCfg.HYBRID] PASSED [ 44%]2021-01-20 04:25:28,767 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_write_metadata_new_symbol[FwPointersCfg.ENABLED] PASSED [ 44%]2021-01-20 04:25:29,615 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_write_metadata_after_append[FwPointersCfg.DISABLED] PASSED [ 44%]2021-01-20 04:25:30,486 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_write_metadata_after_append[FwPointersCfg.HYBRID] PASSED [ 44%]2021-01-20 04:25:31,352 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_write_metadata_after_append[FwPointersCfg.ENABLED] PASSED [ 44%]2021-01-20 04:25:32,225 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_write_metadata_purge_previous_versions[FwPointersCfg.DISABLED] PASSED [ 44%]2021-01-20 04:25:35,119 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_write_metadata_purge_previous_versions[FwPointersCfg.HYBRID] PASSED [ 44%]2021-01-20 04:25:38,009 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_write_metadata_purge_previous_versions[FwPointersCfg.ENABLED] PASSED [ 44%]2021-01-20 04:25:40,898 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_write_metadata_delete_symbol[FwPointersCfg.DISABLED] PASSED [ 44%]2021-01-20 04:25:41,786 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_write_metadata_delete_symbol[FwPointersCfg.HYBRID] PASSED [ 44%]2021-01-20 04:25:42,675 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_write_metadata_delete_symbol[FwPointersCfg.ENABLED] PASSED [ 45%]2021-01-20 04:25:43,552 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_write_metadata_snapshots[FwPointersCfg.DISABLED] PASSED [ 45%]2021-01-20 04:25:44,432 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_write_metadata_snapshots[FwPointersCfg.HYBRID] PASSED [ 45%]2021-01-20 04:25:45,319 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_write_metadata_snapshots[FwPointersCfg.ENABLED] PASSED [ 45%]2021-01-20 04:25:46,202 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_restore_version[FwPointersCfg.DISABLED] PASSED [ 45%]2021-01-20 04:25:47,081 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_restore_version[FwPointersCfg.HYBRID] PASSED [ 45%]2021-01-20 04:25:47,956 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_restore_version[FwPointersCfg.ENABLED] PASSED [ 45%]2021-01-20 04:25:48,832 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_restore_version_followed_by_append[FwPointersCfg.DISABLED] PASSED [ 45%]2021-01-20 04:25:51,721 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_restore_version_followed_by_append[FwPointersCfg.HYBRID] PASSED [ 45%]2021-01-20 04:25:54,601 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_restore_version_followed_by_append[FwPointersCfg.ENABLED] PASSED [ 45%]2021-01-20 04:25:57,486 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_restore_version_purging_previous_versions[FwPointersCfg.DISABLED] PASSED [ 45%]2021-01-20 04:26:00,363 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_restore_version_purging_previous_versions[FwPointersCfg.HYBRID] PASSED [ 45%]2021-01-20 04:26:03,246 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_restore_version_purging_previous_versions[FwPointersCfg.ENABLED] PASSED [ 45%]2021-01-20 04:26:06,125 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_restore_version_non_existent_version[FwPointersCfg.DISABLED] PASSED [ 46%]2021-01-20 04:26:06,972 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_restore_version_non_existent_version[FwPointersCfg.HYBRID] PASSED [ 46%]2021-01-20 04:26:07,826 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_restore_version_non_existent_version[FwPointersCfg.ENABLED] PASSED [ 46%]2021-01-20 04:26:08,669 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_restore_version_which_updated_only_metadata[FwPointersCfg.DISABLED] PASSED [ 46%]2021-01-20 04:26:09,540 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_restore_version_which_updated_only_metadata[FwPointersCfg.HYBRID] PASSED [ 46%]2021-01-20 04:26:10,406 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_restore_version_which_updated_only_metadata[FwPointersCfg.ENABLED] PASSED [ 46%]2021-01-20 04:26:11,276 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_restore_version_then_snapshot[FwPointersCfg.DISABLED] PASSED [ 46%]2021-01-20 04:26:12,149 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_restore_version_then_snapshot[FwPointersCfg.HYBRID] PASSED [ 46%]2021-01-20 04:26:13,018 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_restore_version_then_snapshot[FwPointersCfg.ENABLED] PASSED [ 46%]2021-01-20 04:26:13,889 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_restore_version_latest_snapshot_noop[FwPointersCfg.DISABLED] PASSED [ 46%]2021-01-20 04:26:14,739 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_restore_version_latest_snapshot_noop[FwPointersCfg.HYBRID] PASSED [ 46%]2021-01-20 04:26:15,590 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_restore_version_latest_snapshot_noop[FwPointersCfg.ENABLED] PASSED [ 46%]2021-01-20 04:26:16,441 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_restore_version_latest_version_noop[FwPointersCfg.DISABLED] PASSED [ 46%]2021-01-20 04:26:17,284 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_restore_version_latest_version_noop[FwPointersCfg.HYBRID] PASSED [ 46%]2021-01-20 04:26:18,138 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_restore_version_latest_version_noop[FwPointersCfg.ENABLED] PASSED [ 47%]2021-01-20 04:26:18,987 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_restore_version_snap_delete_symbol_restore[FwPointersCfg.DISABLED] PASSED [ 47%]2021-01-20 04:26:19,870 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_restore_version_snap_delete_symbol_restore[FwPointersCfg.HYBRID] PASSED [ 47%]2021-01-20 04:26:20,756 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_restore_version_snap_delete_symbol_restore[FwPointersCfg.ENABLED] PASSED [ 47%]2021-01-20 04:26:21,635 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_restore_from_version_with_deleted_symbol[FwPointersCfg.DISABLED] PASSED [ 47%]2021-01-20 04:26:22,488 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_restore_from_version_with_deleted_symbol[FwPointersCfg.HYBRID] PASSED [ 47%]2021-01-20 04:26:23,350 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_restore_from_version_with_deleted_symbol[FwPointersCfg.ENABLED] PASSED [ 47%]2021-01-20 04:26:24,200 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_prune_previous_versions_retries_on_cleanup_error[FwPointersCfg.DISABLED] PASSED [ 47%]2021-01-20 04:26:25,080 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_prune_previous_versions_retries_on_cleanup_error[FwPointersCfg.HYBRID] PASSED [ 47%]2021-01-20 04:26:25,957 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_prune_previous_versions_retries_on_cleanup_error[FwPointersCfg.ENABLED] PASSED [ 47%]2021-01-20 04:26:26,842 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_prune_previous_versions_retries_find_calls[FwPointersCfg.DISABLED] PASSED [ 47%]2021-01-20 04:26:27,715 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_prune_previous_versions_retries_find_calls[FwPointersCfg.HYBRID] PASSED [ 47%]2021-01-20 04:26:28,586 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_prune_previous_versions_retries_find_calls[FwPointersCfg.ENABLED] PASSED [ 47%]2021-01-20 04:26:29,453 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_append_does_not_duplicate_data_when_prune_fails[FwPointersCfg.DISABLED] PASSED [ 48%]
tests/integration/store/test_version_store.py::test_append_does_not_duplicate_data_when_prune_fails[FwPointersCfg.HYBRID] PASSED [ 48%]
tests/integration/store/test_version_store.py::test_append_does_not_duplicate_data_when_prune_fails[FwPointersCfg.ENABLED] PASSED [ 48%]
tests/integration/store/test_version_store.py::test_write_does_not_succeed_with_a_prune_error[FwPointersCfg.DISABLED] PASSED [ 48%]2021-01-20 04:26:33,092 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_write_does_not_succeed_with_a_prune_error[FwPointersCfg.HYBRID] PASSED [ 48%]2021-01-20 04:26:33,969 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_write_does_not_succeed_with_a_prune_error[FwPointersCfg.ENABLED] PASSED [ 48%]2021-01-20 04:26:34,847 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_prune_keeps_version[FwPointersCfg.DISABLED] PASSED [ 48%]2021-01-20 04:26:35,726 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_prune_keeps_version[FwPointersCfg.HYBRID] PASSED [ 48%]2021-01-20 04:26:36,606 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_prune_keeps_version[FwPointersCfg.ENABLED] PASSED [ 48%]2021-01-20 04:26:37,450 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_empty_string_column_name PASSED [ 48%]2021-01-20 04:26:38,302 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_snapshot_list_versions_after_delete[FwPointersCfg.DISABLED] PASSED [ 48%]2021-01-20 04:26:39,169 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_snapshot_list_versions_after_delete[FwPointersCfg.HYBRID] PASSED [ 48%]2021-01-20 04:26:40,030 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_snapshot_list_versions_after_delete[FwPointersCfg.ENABLED] PASSED [ 48%]2021-01-20 04:26:40,890 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_write_non_serializable_throws PASSED [ 48%]2021-01-20 04:26:41,742 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_write_non_serializable_pickling_default[FwPointersCfg.DISABLED] PASSED [ 49%]2021-01-20 04:26:42,590 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_write_non_serializable_pickling_default[FwPointersCfg.HYBRID] PASSED [ 49%]2021-01-20 04:26:43,437 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_write_non_serializable_pickling_default[FwPointersCfg.ENABLED] PASSED [ 49%]2021-01-20 04:26:44,294 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_write_strict_no_daterange[FwPointersCfg.DISABLED] PASSED [ 49%]2021-01-20 04:26:45,139 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_write_strict_no_daterange[FwPointersCfg.HYBRID] PASSED [ 49%]2021-01-20 04:26:45,978 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_write_strict_no_daterange[FwPointersCfg.ENABLED] PASSED [ 49%]2021-01-20 04:26:46,816 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_handler_check_default_false PASSED [ 49%]2021-01-20 04:26:47,638 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_handler_check_default_osenviron PASSED [ 49%]2021-01-20 04:26:48,461 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_handler_check_set_false PASSED [ 49%]2021-01-20 04:26:49,285 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_handler_check_set_true PASSED [ 49%]2021-01-20 04:26:50,112 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_write_df_with_objects_in_index PASSED [ 49%]2021-01-20 04:26:50,979 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_write_series_with_objects_in_index PASSED [ 49%]2021-01-20 04:26:51,844 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_write_series_with_some_objects[input_series0] PASSED [ 49%]2021-01-20 04:26:52,696 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_write_series_with_some_objects[input_series1] PASSED [ 50%]2021-01-20 04:26:53,545 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_can_write_tz_aware_data_df[FwPointersCfg.DISABLED] PASSED [ 50%]2021-01-20 04:26:54,397 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_can_write_tz_aware_data_df[FwPointersCfg.HYBRID] PASSED [ 50%]2021-01-20 04:26:55,248 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_can_write_tz_aware_data_df[FwPointersCfg.ENABLED] PASSED [ 50%]2021-01-20 04:26:56,112 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_can_write_tz_aware_data_series[FwPointersCfg.DISABLED] PASSED [ 50%]2021-01-20 04:26:56,961 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_can_write_tz_aware_data_series[FwPointersCfg.HYBRID] PASSED [ 50%]2021-01-20 04:26:57,806 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_can_write_tz_aware_data_series[FwPointersCfg.ENABLED] PASSED [ 50%]2021-01-20 04:26:58,644 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_fwpointers_mixed_scenarios[FwPointersCfg.DISABLED-FwPointersCfg.DISABLED-FwPointersCfg.DISABLED-FwPointersCfg.DISABLED] PASSED [ 50%]2021-01-20 04:26:59,541 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_fwpointers_mixed_scenarios[FwPointersCfg.ENABLED-FwPointersCfg.ENABLED-FwPointersCfg.ENABLED-FwPointersCfg.ENABLED] PASSED [ 50%]2021-01-20 04:27:00,443 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_fwpointers_mixed_scenarios[FwPointersCfg.HYBRID-FwPointersCfg.HYBRID-FwPointersCfg.HYBRID-FwPointersCfg.HYBRID] PASSED [ 50%]2021-01-20 04:27:01,350 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_fwpointers_mixed_scenarios[FwPointersCfg.HYBRID-FwPointersCfg.DISABLED-FwPointersCfg.HYBRID-FwPointersCfg.DISABLED] PASSED [ 50%]2021-01-20 04:27:02,250 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_fwpointers_mixed_scenarios[FwPointersCfg.HYBRID-FwPointersCfg.ENABLED-FwPointersCfg.HYBRID-FwPointersCfg.ENABLED] PASSED [ 50%]2021-01-20 04:27:03,156 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_fwpointers_mixed_scenarios[FwPointersCfg.ENABLED-FwPointersCfg.HYBRID-FwPointersCfg.ENABLED-FwPointersCfg.HYBRID] PASSED [ 50%]2021-01-20 04:27:04,055 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_fwpointers_mixed_scenarios[FwPointersCfg.DISABLED-FwPointersCfg.HYBRID-FwPointersCfg.DISABLED-FwPointersCfg.HYBRID] PASSED [ 51%]2021-01-20 04:27:04,963 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_fwpointers_mixed_scenarios[FwPointersCfg.DISABLED-FwPointersCfg.ENABLED-FwPointersCfg.DISABLED-FwPointersCfg.ENABLED] PASSED [ 51%]2021-01-20 04:27:05,871 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_fwpointers_mixed_scenarios[FwPointersCfg.ENABLED-FwPointersCfg.DISABLED-FwPointersCfg.ENABLED-FwPointersCfg.DISABLED] PASSED [ 51%]2021-01-20 04:27:06,775 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_fwpointers_mixed_scenarios[FwPointersCfg.ENABLED-FwPointersCfg.ENABLED-FwPointersCfg.DISABLED-FwPointersCfg.DISABLED] PASSED [ 51%]2021-01-20 04:27:07,723 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_fwpointers_mixed_scenarios[FwPointersCfg.ENABLED-FwPointersCfg.ENABLED-FwPointersCfg.HYBRID-FwPointersCfg.DISABLED] PASSED [ 51%]2021-01-20 04:27:08,675 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_fwpointers_mixed_scenarios[FwPointersCfg.ENABLED-FwPointersCfg.ENABLED-FwPointersCfg.HYBRID-FwPointersCfg.ENABLED] PASSED [ 51%]2021-01-20 04:27:09,622 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_fwpointers_writemetadata_enabled_disabled PASSED [ 51%]2021-01-20 04:27:10,553 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_fwpointer_enabled_write_delete_keep_version_append PASSED [ 51%]2021-01-20 04:27:11,438 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_version_arctic_version PASSED [ 51%]2021-01-20 04:27:12,282 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_prune_mixed_fwpointer_configs PASSED [ 51%]2021-01-20 04:27:20,062 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_prune_crossref_fwpointer_configs[FwPointersCfg.DISABLED-FwPointersCfg.HYBRID] PASSED [ 51%]2021-01-20 04:27:24,641 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_prune_crossref_fwpointer_configs[FwPointersCfg.DISABLED-FwPointersCfg.ENABLED] PASSED [ 51%]2021-01-20 04:27:29,149 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_prune_crossref_fwpointer_configs[FwPointersCfg.HYBRID-FwPointersCfg.DISABLED] PASSED [ 51%]2021-01-20 04:27:33,716 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_prune_crossref_fwpointer_configs[FwPointersCfg.HYBRID-FwPointersCfg.ENABLED] PASSED [ 51%]2021-01-20 04:27:38,213 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_prune_crossref_fwpointer_configs[FwPointersCfg.ENABLED-FwPointersCfg.HYBRID] PASSED [ 52%]2021-01-20 04:27:42,759 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store.py::test_prune_crossref_fwpointer_configs[FwPointersCfg.ENABLED-FwPointersCfg.DISABLED] PASSED [ 52%]2021-01-20 04:27:47,492 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store_audit.py::test_ArcticTransaction_can_do_first_writes PASSED [ 52%]2021-01-20 04:27:48,359 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store_audit.py::test_ArcticTransaction_detects_concurrent_writes PASSED [ 52%]2021-01-20 04:27:49,260 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store_audit.py::test_audit_writes PASSED [ 52%]2021-01-20 04:27:50,150 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store_audit.py::test_metadata_changes_writes PASSED [ 52%]2021-01-20 04:27:51,034 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store_audit.py::test_audit_read PASSED [ 52%]2021-01-20 04:27:51,931 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store_audit.py::test_cleanup_orphaned_versions_integration PASSED [ 52%]2021-01-20 04:27:52,796 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store_audit.py::test_corrupted_read_writes_new PASSED [ 52%]
tests/integration/store/test_version_store_audit.py::test_write_after_delete PASSED [ 52%]2021-01-20 04:27:54,587 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store_audit.py::test_ArcticTransaction_write_skips_for_exact_match PASSED [ 52%]2021-01-20 04:27:55,465 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store_audit.py::test_ArcticTransaction_write_doesnt_skip_for_close_ts PASSED [ 52%]2021-01-20 04:27:56,344 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store_corruption.py::test_no_corruption_restore_append_overlapping PASSED [ 52%]2021-01-20 04:27:58,737 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store_corruption.py::test_no_corruption_restore_writemeta_append PASSED [ 53%]2021-01-20 04:28:00,905 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store_corruption.py::test_no_corruption_restore_append_non_overlapping_tstamps PASSED [ 53%]2021-01-20 04:28:04,576 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store_corruption.py::test_restore_append_overlapping_corrupts_old PASSED [ 53%]2021-01-20 04:28:06,165 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store_corruption.py::test_restore_append_overlapping_corrupts_last PASSED [ 53%]2021-01-20 04:28:07,803 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store_corruption.py::test_append_fail_after_delete_noupsert SKIPPED [ 53%]
tests/integration/store/test_version_store_corruption.py::test_append_without_corrupt_check PASSED [ 53%]2021-01-20 04:28:15,805 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store_corruption.py::test_append_with_corrupt_check PASSED [ 53%]2021-01-20 04:28:17,424 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store_corruption.py::test_fast_check_corruption PASSED [ 53%]2021-01-20 04:28:18,352 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/store/test_version_store_corruption.py::test_fast_is_safe_to_append PASSED [ 53%]2021-01-20 04:28:32,131 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/tickstore/test_toplevel.py::test_should_return_libraries_for_the_given_daterange[start0-end0-expected0] PASSED [ 53%]2021-01-20 04:28:32,855 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/tickstore/test_toplevel.py::test_should_return_libraries_for_the_given_daterange[start1-end1-expected1] PASSED [ 53%]2021-01-20 04:28:33,574 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/tickstore/test_toplevel.py::test_should_return_libraries_for_the_given_daterange[start2-end2-expected2] PASSED [ 53%]2021-01-20 04:28:34,288 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/tickstore/test_toplevel.py::test_should_return_libraries_for_the_given_daterange[start3-end3-expected3] PASSED [ 53%]2021-01-20 04:28:35,002 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/tickstore/test_toplevel.py::test_should_return_libraries_for_the_given_daterange[start4-end4-expected4] PASSED [ 53%]2021-01-20 04:28:35,719 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/tickstore/test_toplevel.py::test_should_return_libraries_for_the_given_daterange[start5-end5-expected5] PASSED [ 54%]2021-01-20 04:28:36,434 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/tickstore/test_toplevel.py::test_should_return_libraries_for_the_given_daterange[start6-end6-expected6] PASSED [ 54%]2021-01-20 04:28:37,150 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/tickstore/test_toplevel.py::test_should_return_libraries_for_the_given_daterange[start7-end7-expected7] PASSED [ 54%]2021-01-20 04:28:37,867 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/tickstore/test_toplevel.py::test_should_return_libraries_for_the_given_daterange[start8-end8-expected8] PASSED [ 54%]2021-01-20 04:28:38,580 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/tickstore/test_toplevel.py::test_should_raise_exceptions_if_no_libraries_are_found_in_the_date_range_when_reading_data PASSED [ 54%]
tests/integration/tickstore/test_toplevel.py::test_should_return_data_when_date_range_falls_in_a_single_underlying_library FAILED [ 54%]
tests/integration/tickstore/test_toplevel.py::test_should_return_data_when_date_range_spans_libraries PASSED [ 54%]2021-01-20 04:28:41,074 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/tickstore/test_toplevel.py::test_should_return_data_when_date_range_spans_libraries_even_if_one_returns_nothing FAILED [ 54%]
tests/integration/tickstore/test_toplevel.py::test_should_add_underlying_library_where_none_exists PASSED [ 54%]2021-01-20 04:28:42,764 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/tickstore/test_toplevel.py::test_should_add_underlying_library_where_another_library_exists_in_a_non_overlapping_daterange PASSED [ 54%]2021-01-20 04:28:43,553 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/tickstore/test_toplevel.py::test_should_raise_exception_if_library_does_not_exist PASSED [ 54%]
tests/integration/tickstore/test_toplevel.py::test_should_raise_exception_if_date_range_for_library_overlaps_with_existing_libraries PASSED [ 54%]
tests/integration/tickstore/test_toplevel.py::test_should_successfully_do_a_roundtrip_write_and_read_spanning_multiple_underlying_libraries XFAIL [ 54%]
tests/integration/tickstore/test_toplevel.py::test_should_list_symbols_from_the_underlying_library[start0-end0-0-10] PASSED [ 55%]2021-01-20 04:28:47,001 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/tickstore/test_toplevel.py::test_should_list_symbols_from_the_underlying_library[start1-end1-0-8] PASSED [ 55%]2021-01-20 04:28:47,948 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/tickstore/test_toplevel.py::test_should_list_symbols_from_the_underlying_library[start2-end2-7-10] PASSED [ 55%]2021-01-20 04:28:48,885 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/tickstore/test_toplevel.py::test_should_add_underlying_libraries_when_intialized PASSED [ 55%]2021-01-20 04:28:49,750 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/tickstore/test_toplevel.py::test_should_write_top_level_with_list_of_dicts FAILED [ 55%]
tests/integration/tickstore/test_toplevel.py::test_should_write_top_level_with_correct_timezone 2021-01-20 04:28:51,538 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
FAILED [ 55%]
tests/integration/tickstore/test_toplevel.py::test_min_max_date PASSED   [ 55%]2021-01-20 04:28:52,312 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/tickstore/test_toplevel.py::test_no_min_max_date PASSED [ 55%]2021-01-20 04:28:53,057 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/tickstore/test_toplevel.py::test_get_libraries_no_data_raises_exception PASSED [ 55%]2021-01-20 04:28:53,771 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/tickstore/test_toplevel.py::test_get_libraries_no_data_raises_exception_tzinfo_given PASSED [ 55%]2021-01-20 04:28:54,485 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/tickstore/test_toplevel.py::test_get_library_metadata PASSED [ 55%]2021-01-20 04:28:55,340 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/tickstore/test_ts_delete.py::test_delete[tickstore] PASSED [ 55%]2021-01-20 04:28:56,097 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/tickstore/test_ts_delete.py::test_delete_daterange[tickstore] PASSED [ 55%]2021-01-20 04:28:56,843 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/tickstore/test_ts_read.py::test_read[tickstore] PASSED [ 56%]2021-01-20 04:28:57,593 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/tickstore/test_ts_read.py::test_read_data_is_modifiable[tickstore] PASSED [ 56%]2021-01-20 04:28:58,343 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/tickstore/test_ts_read.py::test_read_allow_secondary[tickstore] PASSED [ 56%]2021-01-20 04:28:59,097 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/tickstore/test_ts_read.py::test_read_symbol_as_column[tickstore] PASSED [ 56%]2021-01-20 04:28:59,847 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/tickstore/test_ts_read.py::test_read_multiple_symbols[tickstore] PASSED [ 56%]2021-01-20 04:29:00,597 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/tickstore/test_ts_read.py::test_read_all_cols_all_dtypes[tickstore-1] PASSED [ 56%]2021-01-20 04:29:01,361 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/tickstore/test_ts_read.py::test_read_all_cols_all_dtypes[tickstore-100] PASSED [ 56%]2021-01-20 04:29:02,119 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/tickstore/test_ts_read.py::test_date_range[tickstore] PASSED [ 56%]2021-01-20 04:29:02,944 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/tickstore/test_ts_read.py::test_date_range_end_not_in_range[tickstore] PASSED [ 56%]2021-01-20 04:29:03,695 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/tickstore/test_ts_read.py::test_date_range_default_timezone[tickstore-UTC] PASSED [ 56%]2021-01-20 04:29:04,459 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/tickstore/test_ts_read.py::test_date_range_default_timezone[tickstore-Europe/London] PASSED [ 56%]2021-01-20 04:29:05,221 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/tickstore/test_ts_read.py::test_date_range_default_timezone[tickstore-America/New_York] PASSED [ 56%]2021-01-20 04:29:05,984 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/tickstore/test_ts_read.py::test_date_range_no_bounds[tickstore] PASSED [ 56%]2021-01-20 04:29:06,754 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/tickstore/test_ts_read.py::test_date_range_BST[tickstore] PASSED [ 56%]2021-01-20 04:29:07,512 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/tickstore/test_ts_read.py::test_read_no_data[tickstore] PASSED [ 57%]2021-01-20 04:29:08,251 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/tickstore/test_ts_read.py::test_write_no_tz[tickstore] PASSED [ 57%]2021-01-20 04:29:08,991 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/tickstore/test_ts_read.py::test_read_out_of_order[tickstore] PASSED [ 57%]2021-01-20 04:29:09,752 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/tickstore/test_ts_read.py::test_read_chunk_boundaries[tickstore] PASSED [ 57%]2021-01-20 04:29:10,508 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/tickstore/test_ts_read.py::test_read_spanning_chunks[tickstore] PASSED [ 57%]2021-01-20 04:29:11,254 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/tickstore/test_ts_read.py::test_read_inside_range[tickstore] PASSED [ 57%]2021-01-20 04:29:12,003 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/tickstore/test_ts_read.py::test_read_longs[tickstore] PASSED [ 57%]2021-01-20 04:29:12,757 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/tickstore/test_ts_read.py::test_read_with_image[tickstore] PASSED [ 57%]2021-01-20 04:29:13,526 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/tickstore/test_ts_read.py::test_read_with_metadata[tickstore] PASSED [ 57%]2021-01-20 04:29:14,269 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/tickstore/test_ts_read.py::test_read_strings[tickstore] PASSED [ 57%]2021-01-20 04:29:15,019 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/tickstore/test_ts_read.py::test_read_utf8_strings[tickstore] PASSED [ 57%]2021-01-20 04:29:15,765 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/tickstore/test_ts_read.py::test_read_unicode_strings[tickstore] PASSED [ 57%]2021-01-20 04:29:16,513 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/tickstore/test_ts_read.py::test_objects_fail[tickstore] PASSED [ 57%]
tests/integration/tickstore/test_ts_write.py::test_ts_write_simple[tickstore] PASSED [ 58%]2021-01-20 04:29:18,018 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/tickstore/test_ts_write.py::test_overlapping_load[tickstore] PASSED [ 58%]2021-01-20 04:29:18,769 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/tickstore/test_ts_write.py::test_ts_write_pandas[tickstore] PASSED [ 58%]2021-01-20 04:29:19,527 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/tickstore/test_ts_write.py::test_ts_write_named_col[tickstore] PASSED [ 58%]2021-01-20 04:29:20,282 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
tests/integration/tickstore/test_ts_write.py::test_millisecond_roundtrip[tickstore] PASSED [ 58%]2021-01-20 04:29:21,028 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
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
toplevel_tickstore = <arctic.tickstore.toplevel.TopLevelTickStore object at 0x7fd75d2e0320>
arctic = <Arctic at 0x7fd7603f3668, connected to MongoClient(host=['127.112.217.158:31816'], document_class=dict, tz_aware=False, connect=True)>
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
        res = toplevel_tickstore.read('blah', DateRange(start=dt(2010, 1, 1), end=dt(2010, 1, 6)), list('ABCD'))
    
>       assert_frame_equal(df, res.tz_convert(mktz('Europe/London')))
E       AssertionError: (<Day>, None)
tests/integration/tickstore/test_toplevel.py:65: AssertionError
---------------------------- Captured stdout setup -----------------------------
2021-01-20T04:28:39.319+0000 I CONTROL  [main] Automatically disabling TLS 1.0, to force-enable TLS 1.0 specify --sslDisabledProtocols 'none'
2021-01-20T04:28:39.321+0000 I CONTROL  [initandlisten] MongoDB starting : pid=31739 port=31816 dbpath=/tmp/tmp2l0trmct 64-bit host=travis-job-36a0a3d3-bff5-4832-a5cc-28dd585378fb
2021-01-20T04:28:39.321+0000 I CONTROL  [initandlisten] db version v4.0.19
2021-01-20T04:28:39.321+0000 I CONTROL  [initandlisten] git version: 7e28f4296a04d858a2e3dd84a1e79c9ba59a9568
2021-01-20T04:28:39.321+0000 I CONTROL  [initandlisten] OpenSSL version: OpenSSL 1.0.2g  1 Mar 2016
2021-01-20T04:28:39.321+0000 I CONTROL  [initandlisten] allocator: tcmalloc
2021-01-20T04:28:39.321+0000 I CONTROL  [initandlisten] modules: none
2021-01-20T04:28:39.321+0000 I CONTROL  [initandlisten] build environment:
2021-01-20T04:28:39.321+0000 I CONTROL  [initandlisten]     distmod: ubuntu1604
2021-01-20T04:28:39.321+0000 I CONTROL  [initandlisten]     distarch: x86_64
2021-01-20T04:28:39.321+0000 I CONTROL  [initandlisten]     target_arch: x86_64
2021-01-20T04:28:39.321+0000 I CONTROL  [initandlisten] options: { net: { bindIp: "127.112.217.158", port: 31816, unixDomainSocket: { enabled: false } }, storage: { dbPath: "/tmp/tmp2l0trmct", journal: { enabled: false }, syncPeriodSecs: 0.0 }, systemLog: { quiet: true } }
2021-01-20T04:28:39.321+0000 I STORAGE  [initandlisten] 
2021-01-20T04:28:39.321+0000 I STORAGE  [initandlisten] ** WARNING: Using the XFS filesystem is strongly recommended with the WiredTiger storage engine
2021-01-20T04:28:39.321+0000 I STORAGE  [initandlisten] **          See http://dochub.mongodb.org/core/prodnotes-filesystem
2021-01-20T04:28:39.321+0000 I STORAGE  [initandlisten] wiredtiger_open config: create,cache_size=3476M,cache_overflow=(file_max=0M),session_max=20000,eviction=(threads_min=4,threads_max=4),config_base=false,statistics=(fast),log=(enabled=true,archive=true,path=journal,compressor=snappy),file_manager=(close_idle_time=100000),statistics_log=(wait=0),verbose=(recovery_progress),,log=(enabled=false),
2021-01-20T04:28:39.803+0000 I STORAGE  [initandlisten] WiredTiger message [1611116919:803552][31739:0x7fad5b468a80], txn-recover: Set global recovery timestamp: 0
2021-01-20T04:28:39.813+0000 I RECOVERY [initandlisten] WiredTiger recoveryTimestamp. Ts: Timestamp(0, 0)
2021-01-20T04:28:39.830+0000 I CONTROL  [initandlisten] 
2021-01-20T04:28:39.830+0000 I CONTROL  [initandlisten] ** WARNING: Access control is not enabled for the database.
2021-01-20T04:28:39.830+0000 I CONTROL  [initandlisten] **          Read and write access to data and configuration is unrestricted.
2021-01-20T04:28:39.830+0000 I CONTROL  [initandlisten] 
2021-01-20T04:28:39.830+0000 I STORAGE  [initandlisten] createCollection: admin.system.version with provided UUID: 801df653-858b-427d-8788-7001fd627e0a
2021-01-20T04:28:39.843+0000 I SHARDING [initandlisten] Marking collection admin.system.version as collection version: <unsharded>
2021-01-20T04:28:39.844+0000 I COMMAND  [initandlisten] setting featureCompatibilityVersion to 4.0
2021-01-20T04:28:39.844+0000 I SHARDING [initandlisten] Marking collection local.system.replset as collection version: <unsharded>
2021-01-20T04:28:39.844+0000 I SHARDING [initandlisten] Marking collection admin.system.roles as collection version: <unsharded>
2021-01-20T04:28:39.844+0000 I STORAGE  [initandlisten] createCollection: local.startup_log with generated UUID: 43e59073-e926-458a-8415-82205b65b369
2021-01-20T04:28:39.858+0000 I SHARDING [initandlisten] Marking collection local.startup_log as collection version: <unsharded>
2021-01-20T04:28:39.858+0000 I FTDC     [initandlisten] Initializing full-time diagnostic data capture with directory '/tmp/tmp2l0trmct/diagnostic.data'
2021-01-20T04:28:39.859+0000 I SHARDING [LogicalSessionCacheRefresh] Marking collection config.system.sessions as collection version: <unsharded>
2021-01-20T04:28:39.860+0000 I STORAGE  [LogicalSessionCacheRefresh] createCollection: config.system.sessions with generated UUID: 5b982c8c-1198-4a7e-8248-5b3d6e42ebdf
2021-01-20T04:28:39.860+0000 I NETWORK  [initandlisten] waiting for connections on port 31816
2021-01-20T04:28:39.882+0000 I INDEX    [LogicalSessionCacheRefresh] build index on: config.system.sessions properties: { v: 2, key: { lastUse: 1 }, name: "lsidTTLIndex", ns: "config.system.sessions", expireAfterSeconds: 1800 }
2021-01-20T04:28:39.882+0000 I INDEX    [LogicalSessionCacheRefresh] 	 building index using bulk method; build may temporarily use up to 500 megabytes of RAM
2021-01-20T04:28:39.882+0000 W STORAGE  [LogicalSessionCacheRefresh] failed to create WiredTiger bulk cursor: Device or resource busy
2021-01-20T04:28:39.882+0000 W STORAGE  [LogicalSessionCacheRefresh] falling back to non-bulk cursor for index table:index-6--3065130373757965571
2021-01-20T04:28:39.882+0000 I INDEX    [LogicalSessionCacheRefresh] build index done.  scanned 0 total records. 0 secs
2021-01-20T04:28:39.882+0000 I SHARDING [LogicalSessionCacheReap] Marking collection config.transactions as collection version: <unsharded>
2021-01-20T04:28:39.914+0000 I NETWORK  [conn1] received client metadata from 127.0.0.1:35946 conn1: { driver: { name: "PyMongo", version: "3.11.2" }, os: { type: "Linux", name: "Linux", architecture: "x86_64", version: "4.15.0-1077-gcp" }, platform: "CPython 3.6.7.final.0" }
2021-01-20T04:28:39.915+0000 I NETWORK  [conn2] received client metadata from 127.0.0.1:35948 conn2: { driver: { name: "PyMongo", version: "3.11.2" }, os: { type: "Linux", name: "Linux", architecture: "x86_64", version: "4.15.0-1077-gcp" }, platform: "CPython 3.6.7.final.0" }
2021-01-20T04:28:39.919+0000 I NETWORK  [conn3] received client metadata from 127.0.0.1:35950 conn3: { driver: { name: "PyMongo", version: "3.11.2" }, os: { type: "Linux", name: "Linux", architecture: "x86_64", version: "4.15.0-1077-gcp" }, platform: "CPython 3.6.7.final.0" }
2021-01-20T04:28:39.921+0000 I NETWORK  [conn4] received client metadata from 127.0.0.1:35952 conn4: { driver: { name: "PyMongo", version: "3.11.2" }, os: { type: "Linux", name: "Linux", architecture: "x86_64", version: "4.15.0-1077-gcp" }, platform: "CPython 3.6.7.final.0" }
2021-01-20T04:28:39.924+0000 I SHARDING [conn4] Marking collection meta_db.cache as collection version: <unsharded>
2021-01-20T04:28:39.924+0000 I STORAGE  [conn4] createCollection: meta_db.cache with generated UUID: 4a9aba11-28db-4baa-a595-073ad84bba39
2021-01-20T04:28:39.946+0000 I INDEX    [conn4] build index on: meta_db.cache properties: { v: 2, key: { date: 1 }, name: "date_1", ns: "meta_db.cache", expireAfterSeconds: 3600 }
2021-01-20T04:28:39.946+0000 I INDEX    [conn4] 	 building index using bulk method; build may temporarily use up to 500 megabytes of RAM
2021-01-20T04:28:39.946+0000 W STORAGE  [conn4] failed to create WiredTiger bulk cursor: Device or resource busy
2021-01-20T04:28:39.946+0000 W STORAGE  [conn4] falling back to non-bulk cursor for index table:index-9--3065130373757965571
2021-01-20T04:28:39.946+0000 I INDEX    [conn4] build index done.  scanned 0 total records. 0 secs
2021-01-20T04:28:39.948+0000 I SHARDING [conn4] Marking collection arctic_test.toplevel_tickstore.ARCTIC as collection version: <unsharded>
2021-01-20T04:28:39.948+0000 I STORAGE  [conn4] createCollection: arctic_test.toplevel_tickstore.ARCTIC with generated UUID: e10f1d92-b8b7-4e66-a059-88c519b789c8
2021-01-20T04:28:39.961+0000 I SHARDING [conn4] Marking collection meta_db.settings as collection version: <unsharded>
2021-01-20T04:28:39.965+0000 I STORAGE  [conn4] createCollection: arctic_test.toplevel_tickstore with generated UUID: e576e5b9-59fc-4531-a1c4-6f8d699ecabe
2021-01-20T04:28:39.989+0000 I INDEX    [conn4] build index on: arctic_test.toplevel_tickstore properties: { v: 2, key: { start: 1 }, name: "start_1", ns: "arctic_test.toplevel_tickstore", background: true }
2021-01-20T04:28:39.989+0000 I INDEX    [conn4] build index done.  scanned 0 total records. 0 secs
---------------------------- Captured stderr setup -----------------------------
2021-01-20 04:28:39,295 DEBUG pytest_shutil.workspace 
2021-01-20 04:28:39,295 DEBUG pytest_shutil.workspace =======================================================
2021-01-20 04:28:39,295 DEBUG pytest_shutil.workspace pytest_shutil created workspace /tmp/tmp2l0trmct
2021-01-20 04:28:39,295 DEBUG pytest_shutil.workspace This workspace will delete itself on teardown
2021-01-20 04:28:39,295 DEBUG pytest_shutil.workspace =======================================================
2021-01-20 04:28:39,295 DEBUG pytest_shutil.workspace 
2021-01-20 04:28:39,296 DEBUG pytest_server_fixtures.serverclass.thread Launching thread server.
2021-01-20 04:28:39,304 DEBUG pytest_server_fixtures.serverclass.thread Running server: mongod --bind_ip=127.112.217.158 --port=31816 --nounixsocket --syncdelay=0 --nojournal --quiet --dbpath=/tmp/tmp2l0trmct
2021-01-20 04:28:39,304 DEBUG pytest_server_fixtures.serverclass.thread CWD: /home/travis/build/man-group/arctic
2021-01-20 04:28:39,305 DEBUG pytest_server_fixtures.base2 sleeping for 0.1 before retrying (1 of 28)
2021-01-20 04:28:39,305 INFO pytest_server_fixtures.mongo Connecting to Mongo at 127.112.217.158:31816
2021-01-20 04:28:39,309 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
2021-01-20 04:28:39,911 DEBUG pytest_server_fixtures.base2 sleeping for 0.1 before retrying (2 of 28)
2021-01-20 04:28:39,911 INFO pytest_server_fixtures.mongo Connecting to Mongo at 127.112.217.158:31816
2021-01-20 04:28:39,919 DEBUG pytest_server_fixtures.base2 waited 0:00:00.614513 for server to start successfully
2021-01-20 04:28:39,919 DEBUG pytest_server_fixtures.base2 Server now awake
2021-01-20 04:28:39,920 INFO arctic.fixtures.arctic arctic.fixtures: arctic init()
2021-01-20 04:28:39,962 DEBUG root Cache has expired data, fetching from slow path and reloading cache.
------------------------------ Captured log setup ------------------------------
DEBUG    pytest_shutil.workspace:workspace.py:52 
DEBUG    pytest_shutil.workspace:workspace.py:53 =======================================================
DEBUG    pytest_shutil.workspace:workspace.py:56 pytest_shutil created workspace /tmp/tmp2l0trmct
DEBUG    pytest_shutil.workspace:workspace.py:64 This workspace will delete itself on teardown
DEBUG    pytest_shutil.workspace:workspace.py:65 =======================================================
DEBUG    pytest_shutil.workspace:workspace.py:66 
DEBUG    pytest_server_fixtures.serverclass.thread:thread.py:77 Launching thread server.
DEBUG    pytest_server_fixtures.serverclass.thread:thread.py:89 Running server: mongod --bind_ip=127.112.217.158 --port=31816 --nounixsocket --syncdelay=0 --nojournal --quiet --dbpath=/tmp/tmp2l0trmct
DEBUG    pytest_server_fixtures.serverclass.thread:thread.py:90 CWD: /home/travis/build/man-group/arctic
DEBUG    pytest_server_fixtures.base2:base2.py:226 sleeping for 0.1 before retrying (1 of 28)
INFO     pytest_server_fixtures.mongo:mongo.py:128 Connecting to Mongo at 127.112.217.158:31816
DEBUG    pytest_server_fixtures.base2:base2.py:82 Server is already killed, skipping
DEBUG    pytest_server_fixtures.base2:base2.py:226 sleeping for 0.1 before retrying (2 of 28)
INFO     pytest_server_fixtures.mongo:mongo.py:128 Connecting to Mongo at 127.112.217.158:31816
DEBUG    pytest_server_fixtures.base2:base2.py:229 waited 0:00:00.614513 for server to start successfully
DEBUG    pytest_server_fixtures.base2:base2.py:69 Server now awake
INFO     arctic.fixtures.arctic:arctic.py:23 arctic.fixtures: arctic init()
DEBUG    root:arctic.py:234 Cache has expired data, fetching from slow path and reloading cache.
----------------------------- Captured stdout call -----------------------------
2021-01-20T04:28:39.994+0000 I SHARDING [conn4] Marking collection arctic_FEED_2010.LEVEL1.ARCTIC as collection version: <unsharded>
2021-01-20T04:28:39.994+0000 I STORAGE  [conn4] createCollection: arctic_FEED_2010.LEVEL1.ARCTIC with generated UUID: ea432dc8-3aa7-45b3-a2bb-b06c67e7393e
2021-01-20T04:28:40.001+0000 I SHARDING [ftdc] Marking collection local.oplog.rs as collection version: <unsharded>
2021-01-20T04:28:40.008+0000 I STORAGE  [conn4] createCollection: arctic_FEED_2010.LEVEL1 with generated UUID: c177b4a3-1757-440b-9182-7e8eda4ee96a
2021-01-20T04:28:40.029+0000 I INDEX    [conn4] build index on: arctic_FEED_2010.LEVEL1 properties: { v: 2, key: { sy: 1, s: 1 }, name: "sy_1_s_1", ns: "arctic_FEED_2010.LEVEL1", background: true }
2021-01-20T04:28:40.029+0000 I INDEX    [conn4] build index done.  scanned 0 total records. 0 secs
2021-01-20T04:28:40.037+0000 I INDEX    [conn4] build index on: arctic_FEED_2010.LEVEL1 properties: { v: 2, key: { s: 1 }, name: "s_1", ns: "arctic_FEED_2010.LEVEL1", background: true }
2021-01-20T04:28:40.037+0000 I INDEX    [conn4] build index done.  scanned 0 total records. 0 secs
2021-01-20T04:28:40.037+0000 I STORAGE  [conn4] createCollection: arctic_FEED_2010.LEVEL1.metadata with generated UUID: 7ef95ddd-dc68-4695-834d-b9bbfdec5345
2021-01-20T04:28:40.053+0000 I SHARDING [conn4] Marking collection arctic_FEED_2010.LEVEL1.metadata as collection version: <unsharded>
2021-01-20T04:28:40.059+0000 I INDEX    [conn4] build index on: arctic_FEED_2010.LEVEL1.metadata properties: { v: 2, unique: true, key: { sy: 1 }, name: "sy_1", ns: "arctic_FEED_2010.LEVEL1.metadata", background: true }
2021-01-20T04:28:40.059+0000 I INDEX    [conn4] build index done.  scanned 0 total records. 0 secs
2021-01-20T04:28:40.063+0000 I SHARDING [conn4] Marking collection arctic_test_current.toplevel_tickstore.ARCTIC as collection version: <unsharded>
2021-01-20T04:28:40.063+0000 I STORAGE  [conn4] createCollection: arctic_test_current.toplevel_tickstore.ARCTIC with generated UUID: 1416c5dd-4e4c-4cc7-bbfe-945fc36f54a9
2021-01-20T04:28:40.077+0000 I STORAGE  [conn4] createCollection: arctic_test_current.toplevel_tickstore with generated UUID: 1685117e-248d-4efb-a1a3-188baa9a1ce0
2021-01-20T04:28:40.099+0000 I INDEX    [conn4] build index on: arctic_test_current.toplevel_tickstore properties: { v: 2, key: { sy: 1, s: 1 }, name: "sy_1_s_1", ns: "arctic_test_current.toplevel_tickstore", background: true }
2021-01-20T04:28:40.099+0000 I INDEX    [conn4] build index done.  scanned 0 total records. 0 secs
2021-01-20T04:28:40.108+0000 I INDEX    [conn4] build index on: arctic_test_current.toplevel_tickstore properties: { v: 2, key: { s: 1 }, name: "s_1", ns: "arctic_test_current.toplevel_tickstore", background: true }
2021-01-20T04:28:40.108+0000 I INDEX    [conn4] build index done.  scanned 0 total records. 0 secs
2021-01-20T04:28:40.108+0000 I STORAGE  [conn4] createCollection: arctic_test_current.toplevel_tickstore.metadata with generated UUID: fce138fa-b80f-4c2c-9a71-22583b18b8e8
2021-01-20T04:28:40.123+0000 I SHARDING [conn4] Marking collection arctic_test_current.toplevel_tickstore.metadata as collection version: <unsharded>
2021-01-20T04:28:40.132+0000 I INDEX    [conn4] build index on: arctic_test_current.toplevel_tickstore.metadata properties: { v: 2, unique: true, key: { sy: 1 }, name: "sy_1", ns: "arctic_test_current.toplevel_tickstore.metadata", background: true }
2021-01-20T04:28:40.132+0000 I INDEX    [conn4] build index done.  scanned 0 total records. 0 secs
2021-01-20T04:28:40.135+0000 I SHARDING [conn4] Marking collection arctic_test.toplevel_tickstore as collection version: <unsharded>
2021-01-20T04:28:40.139+0000 I SHARDING [conn4] Marking collection arctic_FEED_2010.LEVEL1 as collection version: <unsharded>
2021-01-20T04:28:40.144+0000 I SHARDING [conn4] Marking collection arctic_test_current.toplevel_tickstore as collection version: <unsharded>
----------------------------- Captured stderr call -----------------------------
2021-01-20 04:28:40,139 WARNING arctic.tickstore.tickstore NB treating all values as 'exists' - no longer sparse
2021-01-20 04:28:40,143 DEBUG arctic.tickstore.tickstore 1 buckets in 0.000822: approx 121654501 ticks/sec
2021-01-20 04:28:40,144 WARNING arctic.tickstore.tickstore NB treating all values as 'exists' - no longer sparse
2021-01-20 04:28:40,147 DEBUG arctic.tickstore.tickstore 1 buckets in 0.000731: approx 136798905 ticks/sec
2021-01-20 04:28:40,152 INFO arctic.tickstore.tickstore Got data in 0.003641 secs, creating DataFrame...
2021-01-20 04:28:40,153 INFO arctic.tickstore.tickstore 6 rows in 0.004856 secs: 1235 ticks/sec
------------------------------ Captured log call -------------------------------
WARNING  arctic.tickstore.tickstore:tickstore.py:706 NB treating all values as 'exists' - no longer sparse
DEBUG    arctic.tickstore.tickstore:tickstore.py:612 1 buckets in 0.000822: approx 121654501 ticks/sec
WARNING  arctic.tickstore.tickstore:tickstore.py:706 NB treating all values as 'exists' - no longer sparse
DEBUG    arctic.tickstore.tickstore:tickstore.py:612 1 buckets in 0.000731: approx 136798905 ticks/sec
INFO     arctic.tickstore.tickstore:tickstore.py:355 Got data in 0.003641 secs, creating DataFrame...
INFO     arctic.tickstore.tickstore:tickstore.py:364 6 rows in 0.004856 secs: 1235 ticks/sec
--------------------------- Captured stderr teardown ---------------------------
2021-01-20 04:28:40,181 DEBUG pytest_server_fixtures.serverclass.thread Killing process tree for 31739 (total_procs_to_kill=1)
2021-01-20 04:28:40,181 DEBUG pytest_server_fixtures.serverclass.thread Killing 1 processes with signal Signals.SIGKILL
2021-01-20 04:28:40,182 DEBUG pytest_server_fixtures.serverclass.thread Waiting for 1 processes to die
2021-01-20 04:28:40,186 DEBUG pytest_server_fixtures.serverclass.thread All processes are terminated
2021-01-20 04:28:40,186 DEBUG pytest_shutil.workspace 
2021-01-20 04:28:40,186 DEBUG pytest_shutil.workspace =======================================================
2021-01-20 04:28:40,186 DEBUG pytest_shutil.workspace pytest_shutil deleting workspace /tmp/tmp2l0trmct
2021-01-20 04:28:40,186 DEBUG pytest_shutil.workspace =======================================================
2021-01-20 04:28:40,186 DEBUG pytest_shutil.workspace 
---------------------------- Captured log teardown -----------------------------
DEBUG    pytest_server_fixtures.serverclass.thread:thread.py:54 Killing process tree for 31739 (total_procs_to_kill=1)
DEBUG    pytest_server_fixtures.serverclass.thread:thread.py:35 Killing 1 processes with signal Signals.SIGKILL
DEBUG    pytest_server_fixtures.serverclass.thread:thread.py:39 Waiting for 1 processes to die
DEBUG    pytest_server_fixtures.serverclass.thread:thread.py:43 All processes are terminated
DEBUG    pytest_shutil.workspace:workspace.py:140 
DEBUG    pytest_shutil.workspace:workspace.py:141 =======================================================
DEBUG    pytest_shutil.workspace:workspace.py:142 pytest_shutil deleting workspace /tmp/tmp2l0trmct
DEBUG    pytest_shutil.workspace:workspace.py:143 =======================================================
DEBUG    pytest_shutil.workspace:workspace.py:144
_ test_should_return_data_when_date_range_spans_libraries_even_if_one_returns_nothing _
toplevel_tickstore = <arctic.tickstore.toplevel.TopLevelTickStore object at 0x7fd75d3f45c0>
arctic = <Arctic at 0x7fd75d433a90, connected to MongoClient(host=['127.112.217.158:17064'], document_class=dict, tz_aware=False, connect=True)>
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
2021-01-20T04:28:41.099+0000 I CONTROL  [main] Automatically disabling TLS 1.0, to force-enable TLS 1.0 specify --sslDisabledProtocols 'none'
2021-01-20T04:28:41.102+0000 I CONTROL  [initandlisten] MongoDB starting : pid=31809 port=17064 dbpath=/tmp/tmpqqw6zt6b 64-bit host=travis-job-36a0a3d3-bff5-4832-a5cc-28dd585378fb
2021-01-20T04:28:41.102+0000 I CONTROL  [initandlisten] db version v4.0.19
2021-01-20T04:28:41.102+0000 I CONTROL  [initandlisten] git version: 7e28f4296a04d858a2e3dd84a1e79c9ba59a9568
2021-01-20T04:28:41.102+0000 I CONTROL  [initandlisten] OpenSSL version: OpenSSL 1.0.2g  1 Mar 2016
2021-01-20T04:28:41.102+0000 I CONTROL  [initandlisten] allocator: tcmalloc
2021-01-20T04:28:41.102+0000 I CONTROL  [initandlisten] modules: none
2021-01-20T04:28:41.102+0000 I CONTROL  [initandlisten] build environment:
2021-01-20T04:28:41.102+0000 I CONTROL  [initandlisten]     distmod: ubuntu1604
2021-01-20T04:28:41.102+0000 I CONTROL  [initandlisten]     distarch: x86_64
2021-01-20T04:28:41.102+0000 I CONTROL  [initandlisten]     target_arch: x86_64
2021-01-20T04:28:41.102+0000 I CONTROL  [initandlisten] options: { net: { bindIp: "127.112.217.158", port: 17064, unixDomainSocket: { enabled: false } }, storage: { dbPath: "/tmp/tmpqqw6zt6b", journal: { enabled: false }, syncPeriodSecs: 0.0 }, systemLog: { quiet: true } }
2021-01-20T04:28:41.102+0000 I STORAGE  [initandlisten] 
2021-01-20T04:28:41.102+0000 I STORAGE  [initandlisten] ** WARNING: Using the XFS filesystem is strongly recommended with the WiredTiger storage engine
2021-01-20T04:28:41.102+0000 I STORAGE  [initandlisten] **          See http://dochub.mongodb.org/core/prodnotes-filesystem
2021-01-20T04:28:41.102+0000 I STORAGE  [initandlisten] wiredtiger_open config: create,cache_size=3476M,cache_overflow=(file_max=0M),session_max=20000,eviction=(threads_min=4,threads_max=4),config_base=false,statistics=(fast),log=(enabled=true,archive=true,path=journal,compressor=snappy),file_manager=(close_idle_time=100000),statistics_log=(wait=0),verbose=(recovery_progress),,log=(enabled=false),
2021-01-20T04:28:41.583+0000 I STORAGE  [initandlisten] WiredTiger message [1611116921:583051][31809:0x7f19c25c2a80], txn-recover: Set global recovery timestamp: 0
2021-01-20T04:28:41.592+0000 I RECOVERY [initandlisten] WiredTiger recoveryTimestamp. Ts: Timestamp(0, 0)
2021-01-20T04:28:41.611+0000 I CONTROL  [initandlisten] 
2021-01-20T04:28:41.611+0000 I CONTROL  [initandlisten] ** WARNING: Access control is not enabled for the database.
2021-01-20T04:28:41.611+0000 I CONTROL  [initandlisten] **          Read and write access to data and configuration is unrestricted.
2021-01-20T04:28:41.611+0000 I CONTROL  [initandlisten] 
2021-01-20T04:28:41.611+0000 I STORAGE  [initandlisten] createCollection: admin.system.version with provided UUID: 53e1c5b9-3354-46d9-874f-e4977930cbe4
2021-01-20T04:28:41.625+0000 I SHARDING [initandlisten] Marking collection admin.system.version as collection version: <unsharded>
2021-01-20T04:28:41.625+0000 I COMMAND  [initandlisten] setting featureCompatibilityVersion to 4.0
2021-01-20T04:28:41.625+0000 I SHARDING [initandlisten] Marking collection local.system.replset as collection version: <unsharded>
2021-01-20T04:28:41.625+0000 I SHARDING [initandlisten] Marking collection admin.system.roles as collection version: <unsharded>
2021-01-20T04:28:41.625+0000 I STORAGE  [initandlisten] createCollection: local.startup_log with generated UUID: 4e2cbf1d-51dc-4c1f-9146-9cbf2b5035e3
2021-01-20T04:28:41.639+0000 I SHARDING [initandlisten] Marking collection local.startup_log as collection version: <unsharded>
2021-01-20T04:28:41.639+0000 I FTDC     [initandlisten] Initializing full-time diagnostic data capture with directory '/tmp/tmpqqw6zt6b/diagnostic.data'
2021-01-20T04:28:41.640+0000 I SHARDING [LogicalSessionCacheRefresh] Marking collection config.system.sessions as collection version: <unsharded>
2021-01-20T04:28:41.640+0000 I STORAGE  [LogicalSessionCacheRefresh] createCollection: config.system.sessions with generated UUID: 7a397838-34af-4098-969d-e4cdf1a8f903
2021-01-20T04:28:41.641+0000 I NETWORK  [initandlisten] waiting for connections on port 17064
2021-01-20T04:28:41.662+0000 I INDEX    [LogicalSessionCacheRefresh] build index on: config.system.sessions properties: { v: 2, key: { lastUse: 1 }, name: "lsidTTLIndex", ns: "config.system.sessions", expireAfterSeconds: 1800 }
2021-01-20T04:28:41.662+0000 I INDEX    [LogicalSessionCacheRefresh] 	 building index using bulk method; build may temporarily use up to 500 megabytes of RAM
2021-01-20T04:28:41.662+0000 W STORAGE  [LogicalSessionCacheRefresh] failed to create WiredTiger bulk cursor: Device or resource busy
2021-01-20T04:28:41.662+0000 W STORAGE  [LogicalSessionCacheRefresh] falling back to non-bulk cursor for index table:index-6-7868337935534128271
2021-01-20T04:28:41.662+0000 I INDEX    [LogicalSessionCacheRefresh] build index done.  scanned 0 total records. 0 secs
2021-01-20T04:28:41.662+0000 I SHARDING [LogicalSessionCacheReap] Marking collection config.transactions as collection version: <unsharded>
2021-01-20T04:28:41.695+0000 I NETWORK  [conn1] received client metadata from 127.0.0.1:40990 conn1: { driver: { name: "PyMongo", version: "3.11.2" }, os: { type: "Linux", name: "Linux", architecture: "x86_64", version: "4.15.0-1077-gcp" }, platform: "CPython 3.6.7.final.0" }
2021-01-20T04:28:41.696+0000 I NETWORK  [conn2] received client metadata from 127.0.0.1:40992 conn2: { driver: { name: "PyMongo", version: "3.11.2" }, os: { type: "Linux", name: "Linux", architecture: "x86_64", version: "4.15.0-1077-gcp" }, platform: "CPython 3.6.7.final.0" }
2021-01-20T04:28:41.699+0000 I NETWORK  [conn3] received client metadata from 127.0.0.1:40994 conn3: { driver: { name: "PyMongo", version: "3.11.2" }, os: { type: "Linux", name: "Linux", architecture: "x86_64", version: "4.15.0-1077-gcp" }, platform: "CPython 3.6.7.final.0" }
2021-01-20T04:28:41.701+0000 I NETWORK  [conn4] received client metadata from 127.0.0.1:40996 conn4: { driver: { name: "PyMongo", version: "3.11.2" }, os: { type: "Linux", name: "Linux", architecture: "x86_64", version: "4.15.0-1077-gcp" }, platform: "CPython 3.6.7.final.0" }
2021-01-20T04:28:41.704+0000 I SHARDING [conn4] Marking collection meta_db.cache as collection version: <unsharded>
2021-01-20T04:28:41.704+0000 I STORAGE  [conn4] createCollection: meta_db.cache with generated UUID: f11e174e-9d3d-401a-aad0-a89c0fdac898
2021-01-20T04:28:41.725+0000 I INDEX    [conn4] build index on: meta_db.cache properties: { v: 2, key: { date: 1 }, name: "date_1", ns: "meta_db.cache", expireAfterSeconds: 3600 }
2021-01-20T04:28:41.725+0000 I INDEX    [conn4] 	 building index using bulk method; build may temporarily use up to 500 megabytes of RAM
2021-01-20T04:28:41.725+0000 W STORAGE  [conn4] failed to create WiredTiger bulk cursor: Device or resource busy
2021-01-20T04:28:41.725+0000 W STORAGE  [conn4] falling back to non-bulk cursor for index table:index-9-7868337935534128271
2021-01-20T04:28:41.725+0000 I INDEX    [conn4] build index done.  scanned 0 total records. 0 secs
2021-01-20T04:28:41.727+0000 I SHARDING [conn4] Marking collection arctic_test.toplevel_tickstore.ARCTIC as collection version: <unsharded>
2021-01-20T04:28:41.727+0000 I STORAGE  [conn4] createCollection: arctic_test.toplevel_tickstore.ARCTIC with generated UUID: e742e59d-9be7-4559-bdd0-bf2b2a992f7c
2021-01-20T04:28:41.741+0000 I SHARDING [conn4] Marking collection meta_db.settings as collection version: <unsharded>
2021-01-20T04:28:41.744+0000 I STORAGE  [conn4] createCollection: arctic_test.toplevel_tickstore with generated UUID: 3095d0eb-c38c-45fa-98a2-0594e7574955
2021-01-20T04:28:41.767+0000 I INDEX    [conn4] build index on: arctic_test.toplevel_tickstore properties: { v: 2, key: { start: 1 }, name: "start_1", ns: "arctic_test.toplevel_tickstore", background: true }
2021-01-20T04:28:41.767+0000 I INDEX    [conn4] build index done.  scanned 0 total records. 0 secs
---------------------------- Captured stderr setup -----------------------------
2021-01-20 04:28:41,076 DEBUG pytest_shutil.workspace 
2021-01-20 04:28:41,076 DEBUG pytest_shutil.workspace =======================================================
2021-01-20 04:28:41,076 DEBUG pytest_shutil.workspace pytest_shutil created workspace /tmp/tmpqqw6zt6b
2021-01-20 04:28:41,076 DEBUG pytest_shutil.workspace This workspace will delete itself on teardown
2021-01-20 04:28:41,076 DEBUG pytest_shutil.workspace =======================================================
2021-01-20 04:28:41,077 DEBUG pytest_shutil.workspace 
2021-01-20 04:28:41,077 DEBUG pytest_server_fixtures.serverclass.thread Launching thread server.
2021-01-20 04:28:41,085 DEBUG pytest_server_fixtures.serverclass.thread Running server: mongod --bind_ip=127.112.217.158 --port=17064 --nounixsocket --syncdelay=0 --nojournal --quiet --dbpath=/tmp/tmpqqw6zt6b
2021-01-20 04:28:41,085 DEBUG pytest_server_fixtures.serverclass.thread CWD: /home/travis/build/man-group/arctic
2021-01-20 04:28:41,086 DEBUG pytest_server_fixtures.base2 sleeping for 0.1 before retrying (1 of 28)
2021-01-20 04:28:41,086 INFO pytest_server_fixtures.mongo Connecting to Mongo at 127.112.217.158:17064
2021-01-20 04:28:41,691 DEBUG pytest_server_fixtures.base2 sleeping for 0.1 before retrying (2 of 28)
2021-01-20 04:28:41,692 INFO pytest_server_fixtures.mongo Connecting to Mongo at 127.112.217.158:17064
2021-01-20 04:28:41,699 DEBUG pytest_server_fixtures.base2 waited 0:00:00.613322 for server to start successfully
2021-01-20 04:28:41,700 DEBUG pytest_server_fixtures.base2 Server now awake
2021-01-20 04:28:41,700 INFO arctic.fixtures.arctic arctic.fixtures: arctic init()
2021-01-20 04:28:41,741 DEBUG root Cache has expired data, fetching from slow path and reloading cache.
------------------------------ Captured log setup ------------------------------
DEBUG    pytest_shutil.workspace:workspace.py:52 
DEBUG    pytest_shutil.workspace:workspace.py:53 =======================================================
DEBUG    pytest_shutil.workspace:workspace.py:56 pytest_shutil created workspace /tmp/tmpqqw6zt6b
DEBUG    pytest_shutil.workspace:workspace.py:64 This workspace will delete itself on teardown
DEBUG    pytest_shutil.workspace:workspace.py:65 =======================================================
DEBUG    pytest_shutil.workspace:workspace.py:66 
DEBUG    pytest_server_fixtures.serverclass.thread:thread.py:77 Launching thread server.
DEBUG    pytest_server_fixtures.serverclass.thread:thread.py:89 Running server: mongod --bind_ip=127.112.217.158 --port=17064 --nounixsocket --syncdelay=0 --nojournal --quiet --dbpath=/tmp/tmpqqw6zt6b
DEBUG    pytest_server_fixtures.serverclass.thread:thread.py:90 CWD: /home/travis/build/man-group/arctic
DEBUG    pytest_server_fixtures.base2:base2.py:226 sleeping for 0.1 before retrying (1 of 28)
INFO     pytest_server_fixtures.mongo:mongo.py:128 Connecting to Mongo at 127.112.217.158:17064
DEBUG    pytest_server_fixtures.base2:base2.py:226 sleeping for 0.1 before retrying (2 of 28)
INFO     pytest_server_fixtures.mongo:mongo.py:128 Connecting to Mongo at 127.112.217.158:17064
DEBUG    pytest_server_fixtures.base2:base2.py:229 waited 0:00:00.613322 for server to start successfully
DEBUG    pytest_server_fixtures.base2:base2.py:69 Server now awake
INFO     arctic.fixtures.arctic:arctic.py:23 arctic.fixtures: arctic init()
DEBUG    root:arctic.py:234 Cache has expired data, fetching from slow path and reloading cache.
----------------------------- Captured stdout call -----------------------------
2021-01-20T04:28:41.772+0000 I SHARDING [conn4] Marking collection arctic_FEED_2010.LEVEL1.ARCTIC as collection version: <unsharded>
2021-01-20T04:28:41.772+0000 I STORAGE  [conn4] createCollection: arctic_FEED_2010.LEVEL1.ARCTIC with generated UUID: e679b19e-7b84-471e-9498-f158697bbaad
2021-01-20T04:28:41.788+0000 I STORAGE  [conn4] createCollection: arctic_FEED_2010.LEVEL1 with generated UUID: 8631d4ac-1ae1-49b9-a52b-bf5f543044ae
2021-01-20T04:28:41.812+0000 I INDEX    [conn4] build index on: arctic_FEED_2010.LEVEL1 properties: { v: 2, key: { sy: 1, s: 1 }, name: "sy_1_s_1", ns: "arctic_FEED_2010.LEVEL1", background: true }
2021-01-20T04:28:41.812+0000 I INDEX    [conn4] build index done.  scanned 0 total records. 0 secs
2021-01-20T04:28:41.820+0000 I INDEX    [conn4] build index on: arctic_FEED_2010.LEVEL1 properties: { v: 2, key: { s: 1 }, name: "s_1", ns: "arctic_FEED_2010.LEVEL1", background: true }
2021-01-20T04:28:41.820+0000 I INDEX    [conn4] build index done.  scanned 0 total records. 0 secs
2021-01-20T04:28:41.821+0000 I STORAGE  [conn4] createCollection: arctic_FEED_2010.LEVEL1.metadata with generated UUID: 6a0470cd-1533-48b1-a38e-b77b4103f334
2021-01-20T04:28:41.836+0000 I SHARDING [conn4] Marking collection arctic_FEED_2010.LEVEL1.metadata as collection version: <unsharded>
2021-01-20T04:28:41.844+0000 I INDEX    [conn4] build index on: arctic_FEED_2010.LEVEL1.metadata properties: { v: 2, unique: true, key: { sy: 1 }, name: "sy_1", ns: "arctic_FEED_2010.LEVEL1.metadata", background: true }
2021-01-20T04:28:41.844+0000 I INDEX    [conn4] build index done.  scanned 0 total records. 0 secs
2021-01-20T04:28:41.847+0000 I SHARDING [conn4] Marking collection arctic_FEED_2011.LEVEL1.ARCTIC as collection version: <unsharded>
2021-01-20T04:28:41.847+0000 I STORAGE  [conn4] createCollection: arctic_FEED_2011.LEVEL1.ARCTIC with generated UUID: c55d32c6-5862-43d5-a4a1-d327712856bf
2021-01-20T04:28:41.861+0000 I STORAGE  [conn4] createCollection: arctic_FEED_2011.LEVEL1 with generated UUID: 877656a8-cf62-4f81-954d-44455d0c6e66
2021-01-20T04:28:41.882+0000 I INDEX    [conn4] build index on: arctic_FEED_2011.LEVEL1 properties: { v: 2, key: { sy: 1, s: 1 }, name: "sy_1_s_1", ns: "arctic_FEED_2011.LEVEL1", background: true }
2021-01-20T04:28:41.882+0000 I INDEX    [conn4] build index done.  scanned 0 total records. 0 secs
2021-01-20T04:28:41.891+0000 I INDEX    [conn4] build index on: arctic_FEED_2011.LEVEL1 properties: { v: 2, key: { s: 1 }, name: "s_1", ns: "arctic_FEED_2011.LEVEL1", background: true }
2021-01-20T04:28:41.891+0000 I INDEX    [conn4] build index done.  scanned 0 total records. 0 secs
2021-01-20T04:28:41.891+0000 I STORAGE  [conn4] createCollection: arctic_FEED_2011.LEVEL1.metadata with generated UUID: e4987029-08dd-4411-98f0-5e3d6c461412
2021-01-20T04:28:41.906+0000 I SHARDING [conn4] Marking collection arctic_FEED_2011.LEVEL1.metadata as collection version: <unsharded>
2021-01-20T04:28:41.914+0000 I INDEX    [conn4] build index on: arctic_FEED_2011.LEVEL1.metadata properties: { v: 2, unique: true, key: { sy: 1 }, name: "sy_1", ns: "arctic_FEED_2011.LEVEL1.metadata", background: true }
2021-01-20T04:28:41.914+0000 I INDEX    [conn4] build index done.  scanned 0 total records. 0 secs
2021-01-20T04:28:41.919+0000 I SHARDING [conn4] Marking collection arctic_test.toplevel_tickstore as collection version: <unsharded>
2021-01-20T04:28:41.924+0000 I SHARDING [conn4] Marking collection arctic_FEED_2010.LEVEL1 as collection version: <unsharded>
2021-01-20T04:28:41.929+0000 I SHARDING [conn4] Marking collection arctic_FEED_2011.LEVEL1 as collection version: <unsharded>
----------------------------- Captured stderr call -----------------------------
2021-01-20 04:28:41,925 WARNING arctic.tickstore.tickstore NB treating all values as 'exists' - no longer sparse
2021-01-20 04:28:41,928 DEBUG arctic.tickstore.tickstore 1 buckets in 0.000796: approx 125628140 ticks/sec
2021-01-20 04:28:41,930 WARNING arctic.tickstore.tickstore NB treating all values as 'exists' - no longer sparse
2021-01-20 04:28:41,932 DEBUG arctic.tickstore.tickstore 1 buckets in 0.000627: approx 159489633 ticks/sec
2021-01-20 04:28:41,937 INFO arctic.tickstore.tickstore Got data in 0.003614 secs, creating DataFrame...
2021-01-20 04:28:41,938 INFO arctic.tickstore.tickstore 6 rows in 0.004779 secs: 1255 ticks/sec
------------------------------ Captured log call -------------------------------
WARNING  arctic.tickstore.tickstore:tickstore.py:706 NB treating all values as 'exists' - no longer sparse
DEBUG    arctic.tickstore.tickstore:tickstore.py:612 1 buckets in 0.000796: approx 125628140 ticks/sec
WARNING  arctic.tickstore.tickstore:tickstore.py:706 NB treating all values as 'exists' - no longer sparse
DEBUG    arctic.tickstore.tickstore:tickstore.py:612 1 buckets in 0.000627: approx 159489633 ticks/sec
INFO     arctic.tickstore.tickstore:tickstore.py:355 Got data in 0.003614 secs, creating DataFrame...
INFO     arctic.tickstore.tickstore:tickstore.py:364 6 rows in 0.004779 secs: 1255 ticks/sec
--------------------------- Captured stderr teardown ---------------------------
2021-01-20 04:28:41,968 DEBUG pytest_server_fixtures.serverclass.thread Killing process tree for 31809 (total_procs_to_kill=1)
2021-01-20 04:28:41,968 DEBUG pytest_server_fixtures.serverclass.thread Killing 1 processes with signal Signals.SIGKILL
2021-01-20 04:28:41,968 DEBUG pytest_server_fixtures.serverclass.thread Waiting for 1 processes to die
2021-01-20 04:28:41,972 DEBUG pytest_server_fixtures.serverclass.thread All processes are terminated
2021-01-20 04:28:41,972 DEBUG pytest_shutil.workspace 
2021-01-20 04:28:41,973 DEBUG pytest_shutil.workspace =======================================================
2021-01-20 04:28:41,973 DEBUG pytest_shutil.workspace pytest_shutil deleting workspace /tmp/tmpqqw6zt6b
2021-01-20 04:28:41,973 DEBUG pytest_shutil.workspace =======================================================
2021-01-20 04:28:41,973 DEBUG pytest_shutil.workspace 
---------------------------- Captured log teardown -----------------------------
DEBUG    pytest_server_fixtures.serverclass.thread:thread.py:54 Killing process tree for 31809 (total_procs_to_kill=1)
DEBUG    pytest_server_fixtures.serverclass.thread:thread.py:35 Killing 1 processes with signal Signals.SIGKILL
DEBUG    pytest_server_fixtures.serverclass.thread:thread.py:39 Waiting for 1 processes to die
DEBUG    pytest_server_fixtures.serverclass.thread:thread.py:43 All processes are terminated
DEBUG    pytest_shutil.workspace:workspace.py:140 
DEBUG    pytest_shutil.workspace:workspace.py:141 =======================================================
DEBUG    pytest_shutil.workspace:workspace.py:142 pytest_shutil deleting workspace /tmp/tmpqqw6zt6b
DEBUG    pytest_shutil.workspace:workspace.py:143 =======================================================
DEBUG    pytest_shutil.workspace:workspace.py:144
________________ test_should_write_top_level_with_list_of_dicts ________________
arctic = <Arctic at 0x7fd763231588, connected to MongoClient(host=['127.112.217.158:23681'], document_class=dict, tz_aware=False, connect=True)>
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
2021-01-20T04:28:49.775+0000 I CONTROL  [main] Automatically disabling TLS 1.0, to force-enable TLS 1.0 specify --sslDisabledProtocols 'none'
2021-01-20T04:28:49.777+0000 I CONTROL  [initandlisten] MongoDB starting : pid=32159 port=23681 dbpath=/tmp/tmpvwnk38gh 64-bit host=travis-job-36a0a3d3-bff5-4832-a5cc-28dd585378fb
2021-01-20T04:28:49.777+0000 I CONTROL  [initandlisten] db version v4.0.19
2021-01-20T04:28:49.777+0000 I CONTROL  [initandlisten] git version: 7e28f4296a04d858a2e3dd84a1e79c9ba59a9568
2021-01-20T04:28:49.777+0000 I CONTROL  [initandlisten] OpenSSL version: OpenSSL 1.0.2g  1 Mar 2016
2021-01-20T04:28:49.777+0000 I CONTROL  [initandlisten] allocator: tcmalloc
2021-01-20T04:28:49.777+0000 I CONTROL  [initandlisten] modules: none
2021-01-20T04:28:49.777+0000 I CONTROL  [initandlisten] build environment:
2021-01-20T04:28:49.777+0000 I CONTROL  [initandlisten]     distmod: ubuntu1604
2021-01-20T04:28:49.777+0000 I CONTROL  [initandlisten]     distarch: x86_64
2021-01-20T04:28:49.777+0000 I CONTROL  [initandlisten]     target_arch: x86_64
2021-01-20T04:28:49.777+0000 I CONTROL  [initandlisten] options: { net: { bindIp: "127.112.217.158", port: 23681, unixDomainSocket: { enabled: false } }, storage: { dbPath: "/tmp/tmpvwnk38gh", journal: { enabled: false }, syncPeriodSecs: 0.0 }, systemLog: { quiet: true } }
2021-01-20T04:28:49.777+0000 I STORAGE  [initandlisten] 
2021-01-20T04:28:49.777+0000 I STORAGE  [initandlisten] ** WARNING: Using the XFS filesystem is strongly recommended with the WiredTiger storage engine
2021-01-20T04:28:49.777+0000 I STORAGE  [initandlisten] **          See http://dochub.mongodb.org/core/prodnotes-filesystem
2021-01-20T04:28:49.777+0000 I STORAGE  [initandlisten] wiredtiger_open config: create,cache_size=3476M,cache_overflow=(file_max=0M),session_max=20000,eviction=(threads_min=4,threads_max=4),config_base=false,statistics=(fast),log=(enabled=true,archive=true,path=journal,compressor=snappy),file_manager=(close_idle_time=100000),statistics_log=(wait=0),verbose=(recovery_progress),,log=(enabled=false),
2021-01-20T04:28:50.260+0000 I STORAGE  [initandlisten] WiredTiger message [1611116930:260976][32159:0x7f27d2087a80], txn-recover: Set global recovery timestamp: 0
2021-01-20T04:28:50.270+0000 I RECOVERY [initandlisten] WiredTiger recoveryTimestamp. Ts: Timestamp(0, 0)
2021-01-20T04:28:50.291+0000 I CONTROL  [initandlisten] 
2021-01-20T04:28:50.291+0000 I CONTROL  [initandlisten] ** WARNING: Access control is not enabled for the database.
2021-01-20T04:28:50.291+0000 I CONTROL  [initandlisten] **          Read and write access to data and configuration is unrestricted.
2021-01-20T04:28:50.291+0000 I CONTROL  [initandlisten] 
2021-01-20T04:28:50.291+0000 I STORAGE  [initandlisten] createCollection: admin.system.version with provided UUID: 3134aa1d-f6e3-4095-ad49-6efadb2556f5
2021-01-20T04:28:50.305+0000 I SHARDING [initandlisten] Marking collection admin.system.version as collection version: <unsharded>
2021-01-20T04:28:50.305+0000 I COMMAND  [initandlisten] setting featureCompatibilityVersion to 4.0
2021-01-20T04:28:50.305+0000 I SHARDING [initandlisten] Marking collection local.system.replset as collection version: <unsharded>
2021-01-20T04:28:50.305+0000 I SHARDING [initandlisten] Marking collection admin.system.roles as collection version: <unsharded>
2021-01-20T04:28:50.305+0000 I STORAGE  [initandlisten] createCollection: local.startup_log with generated UUID: 13470e15-456c-4660-baea-a73568afdbf6
2021-01-20T04:28:50.320+0000 I SHARDING [initandlisten] Marking collection local.startup_log as collection version: <unsharded>
2021-01-20T04:28:50.320+0000 I FTDC     [initandlisten] Initializing full-time diagnostic data capture with directory '/tmp/tmpvwnk38gh/diagnostic.data'
2021-01-20T04:28:50.321+0000 I SHARDING [LogicalSessionCacheRefresh] Marking collection config.system.sessions as collection version: <unsharded>
2021-01-20T04:28:50.321+0000 I STORAGE  [LogicalSessionCacheRefresh] createCollection: config.system.sessions with generated UUID: 35d6c0e9-5f42-4773-9adb-3af768e9aba8
2021-01-20T04:28:50.321+0000 I NETWORK  [initandlisten] waiting for connections on port 23681
2021-01-20T04:28:50.342+0000 I INDEX    [LogicalSessionCacheRefresh] build index on: config.system.sessions properties: { v: 2, key: { lastUse: 1 }, name: "lsidTTLIndex", ns: "config.system.sessions", expireAfterSeconds: 1800 }
2021-01-20T04:28:50.342+0000 I INDEX    [LogicalSessionCacheRefresh] 	 building index using bulk method; build may temporarily use up to 500 megabytes of RAM
2021-01-20T04:28:50.342+0000 W STORAGE  [LogicalSessionCacheRefresh] failed to create WiredTiger bulk cursor: Device or resource busy
2021-01-20T04:28:50.342+0000 W STORAGE  [LogicalSessionCacheRefresh] falling back to non-bulk cursor for index table:index-6-2927029555325635272
2021-01-20T04:28:50.342+0000 I INDEX    [LogicalSessionCacheRefresh] build index done.  scanned 0 total records. 0 secs
2021-01-20T04:28:50.342+0000 I SHARDING [LogicalSessionCacheReap] Marking collection config.transactions as collection version: <unsharded>
2021-01-20T04:28:50.370+0000 I NETWORK  [conn1] received client metadata from 127.0.0.1:41582 conn1: { driver: { name: "PyMongo", version: "3.11.2" }, os: { type: "Linux", name: "Linux", architecture: "x86_64", version: "4.15.0-1077-gcp" }, platform: "CPython 3.6.7.final.0" }
2021-01-20T04:28:50.371+0000 I NETWORK  [conn2] received client metadata from 127.0.0.1:41584 conn2: { driver: { name: "PyMongo", version: "3.11.2" }, os: { type: "Linux", name: "Linux", architecture: "x86_64", version: "4.15.0-1077-gcp" }, platform: "CPython 3.6.7.final.0" }
2021-01-20T04:28:50.374+0000 I NETWORK  [conn3] received client metadata from 127.0.0.1:41586 conn3: { driver: { name: "PyMongo", version: "3.11.2" }, os: { type: "Linux", name: "Linux", architecture: "x86_64", version: "4.15.0-1077-gcp" }, platform: "CPython 3.6.7.final.0" }
2021-01-20T04:28:50.376+0000 I NETWORK  [conn4] received client metadata from 127.0.0.1:41588 conn4: { driver: { name: "PyMongo", version: "3.11.2" }, os: { type: "Linux", name: "Linux", architecture: "x86_64", version: "4.15.0-1077-gcp" }, platform: "CPython 3.6.7.final.0" }
2021-01-20T04:28:50.379+0000 I SHARDING [conn4] Marking collection meta_db.cache as collection version: <unsharded>
2021-01-20T04:28:50.379+0000 I STORAGE  [conn4] createCollection: meta_db.cache with generated UUID: b081f043-cd19-4f40-b5d8-bd074ea2b543
2021-01-20T04:28:50.401+0000 I INDEX    [conn4] build index on: meta_db.cache properties: { v: 2, key: { date: 1 }, name: "date_1", ns: "meta_db.cache", expireAfterSeconds: 3600 }
2021-01-20T04:28:50.401+0000 I INDEX    [conn4] 	 building index using bulk method; build may temporarily use up to 500 megabytes of RAM
2021-01-20T04:28:50.401+0000 W STORAGE  [conn4] failed to create WiredTiger bulk cursor: Device or resource busy
2021-01-20T04:28:50.401+0000 W STORAGE  [conn4] falling back to non-bulk cursor for index table:index-9-2927029555325635272
2021-01-20T04:28:50.401+0000 I INDEX    [conn4] build index done.  scanned 0 total records. 0 secs
---------------------------- Captured stderr setup -----------------------------
2021-01-20 04:28:49,752 DEBUG pytest_shutil.workspace 
2021-01-20 04:28:49,752 DEBUG pytest_shutil.workspace =======================================================
2021-01-20 04:28:49,752 DEBUG pytest_shutil.workspace pytest_shutil created workspace /tmp/tmpvwnk38gh
2021-01-20 04:28:49,752 DEBUG pytest_shutil.workspace This workspace will delete itself on teardown
2021-01-20 04:28:49,752 DEBUG pytest_shutil.workspace =======================================================
2021-01-20 04:28:49,752 DEBUG pytest_shutil.workspace 
2021-01-20 04:28:49,753 DEBUG pytest_server_fixtures.serverclass.thread Launching thread server.
2021-01-20 04:28:49,761 DEBUG pytest_server_fixtures.serverclass.thread Running server: mongod --bind_ip=127.112.217.158 --port=23681 --nounixsocket --syncdelay=0 --nojournal --quiet --dbpath=/tmp/tmpvwnk38gh
2021-01-20 04:28:49,761 DEBUG pytest_server_fixtures.serverclass.thread CWD: /home/travis/build/man-group/arctic
2021-01-20 04:28:49,762 DEBUG pytest_server_fixtures.base2 sleeping for 0.1 before retrying (1 of 28)
2021-01-20 04:28:49,762 INFO pytest_server_fixtures.mongo Connecting to Mongo at 127.112.217.158:23681
2021-01-20 04:28:50,367 DEBUG pytest_server_fixtures.base2 sleeping for 0.1 before retrying (2 of 28)
2021-01-20 04:28:50,367 INFO pytest_server_fixtures.mongo Connecting to Mongo at 127.112.217.158:23681
2021-01-20 04:28:50,375 DEBUG pytest_server_fixtures.base2 waited 0:00:00.613001 for server to start successfully
2021-01-20 04:28:50,375 DEBUG pytest_server_fixtures.base2 Server now awake
2021-01-20 04:28:50,375 INFO arctic.fixtures.arctic arctic.fixtures: arctic init()
------------------------------ Captured log setup ------------------------------
DEBUG    pytest_shutil.workspace:workspace.py:52 
DEBUG    pytest_shutil.workspace:workspace.py:53 =======================================================
DEBUG    pytest_shutil.workspace:workspace.py:56 pytest_shutil created workspace /tmp/tmpvwnk38gh
DEBUG    pytest_shutil.workspace:workspace.py:64 This workspace will delete itself on teardown
DEBUG    pytest_shutil.workspace:workspace.py:65 =======================================================
DEBUG    pytest_shutil.workspace:workspace.py:66 
DEBUG    pytest_server_fixtures.serverclass.thread:thread.py:77 Launching thread server.
DEBUG    pytest_server_fixtures.serverclass.thread:thread.py:89 Running server: mongod --bind_ip=127.112.217.158 --port=23681 --nounixsocket --syncdelay=0 --nojournal --quiet --dbpath=/tmp/tmpvwnk38gh
DEBUG    pytest_server_fixtures.serverclass.thread:thread.py:90 CWD: /home/travis/build/man-group/arctic
DEBUG    pytest_server_fixtures.base2:base2.py:226 sleeping for 0.1 before retrying (1 of 28)
INFO     pytest_server_fixtures.mongo:mongo.py:128 Connecting to Mongo at 127.112.217.158:23681
DEBUG    pytest_server_fixtures.base2:base2.py:226 sleeping for 0.1 before retrying (2 of 28)
INFO     pytest_server_fixtures.mongo:mongo.py:128 Connecting to Mongo at 127.112.217.158:23681
DEBUG    pytest_server_fixtures.base2:base2.py:229 waited 0:00:00.613001 for server to start successfully
DEBUG    pytest_server_fixtures.base2:base2.py:69 Server now awake
INFO     arctic.fixtures.arctic:arctic.py:23 arctic.fixtures: arctic init()
----------------------------- Captured stdout call -----------------------------
2021-01-20T04:28:50.404+0000 I SHARDING [conn4] Marking collection arctic_FEED_2010.LEVEL1.ARCTIC as collection version: <unsharded>
2021-01-20T04:28:50.404+0000 I STORAGE  [conn4] createCollection: arctic_FEED_2010.LEVEL1.ARCTIC with generated UUID: 9d0fd1a9-c1a4-406a-9501-458021da9e9d
2021-01-20T04:28:50.418+0000 I STORAGE  [conn4] createCollection: arctic_FEED_2010.LEVEL1 with generated UUID: 9725e5d5-328a-410f-92a0-9cfe08b0bfa7
2021-01-20T04:28:50.442+0000 I INDEX    [conn4] build index on: arctic_FEED_2010.LEVEL1 properties: { v: 2, key: { sy: 1, s: 1 }, name: "sy_1_s_1", ns: "arctic_FEED_2010.LEVEL1", background: true }
2021-01-20T04:28:50.442+0000 I INDEX    [conn4] build index done.  scanned 0 total records. 0 secs
2021-01-20T04:28:50.451+0000 I INDEX    [conn4] build index on: arctic_FEED_2010.LEVEL1 properties: { v: 2, key: { s: 1 }, name: "s_1", ns: "arctic_FEED_2010.LEVEL1", background: true }
2021-01-20T04:28:50.451+0000 I INDEX    [conn4] build index done.  scanned 0 total records. 0 secs
2021-01-20T04:28:50.451+0000 I STORAGE  [conn4] createCollection: arctic_FEED_2010.LEVEL1.metadata with generated UUID: 2daef4b2-e973-48fb-b001-7997cd3b8097
2021-01-20T04:28:50.467+0000 I SHARDING [conn4] Marking collection arctic_FEED_2010.LEVEL1.metadata as collection version: <unsharded>
2021-01-20T04:28:50.474+0000 I INDEX    [conn4] build index on: arctic_FEED_2010.LEVEL1.metadata properties: { v: 2, unique: true, key: { sy: 1 }, name: "sy_1", ns: "arctic_FEED_2010.LEVEL1.metadata", background: true }
2021-01-20T04:28:50.474+0000 I INDEX    [conn4] build index done.  scanned 0 total records. 0 secs
2021-01-20T04:28:50.477+0000 I SHARDING [conn4] Marking collection arctic_FEED_2011.LEVEL1.ARCTIC as collection version: <unsharded>
2021-01-20T04:28:50.478+0000 I STORAGE  [conn4] createCollection: arctic_FEED_2011.LEVEL1.ARCTIC with generated UUID: 40d60a89-99de-482d-836f-7d4925671b13
2021-01-20T04:28:50.493+0000 I STORAGE  [conn4] createCollection: arctic_FEED_2011.LEVEL1 with generated UUID: f6bcb42b-ba23-4a46-8110-a4139dfdcf0c
2021-01-20T04:28:50.514+0000 I INDEX    [conn4] build index on: arctic_FEED_2011.LEVEL1 properties: { v: 2, key: { sy: 1, s: 1 }, name: "sy_1_s_1", ns: "arctic_FEED_2011.LEVEL1", background: true }
2021-01-20T04:28:50.514+0000 I INDEX    [conn4] build index done.  scanned 0 total records. 0 secs
2021-01-20T04:28:50.523+0000 I INDEX    [conn4] build index on: arctic_FEED_2011.LEVEL1 properties: { v: 2, key: { s: 1 }, name: "s_1", ns: "arctic_FEED_2011.LEVEL1", background: true }
2021-01-20T04:28:50.523+0000 I INDEX    [conn4] build index done.  scanned 0 total records. 0 secs
2021-01-20T04:28:50.524+0000 I STORAGE  [conn4] createCollection: arctic_FEED_2011.LEVEL1.metadata with generated UUID: 2c1f5e1a-b2d1-4bea-81ac-b915e6146f68
2021-01-20T04:28:50.540+0000 I SHARDING [conn4] Marking collection arctic_FEED_2011.LEVEL1.metadata as collection version: <unsharded>
2021-01-20T04:28:50.547+0000 I INDEX    [conn4] build index on: arctic_FEED_2011.LEVEL1.metadata properties: { v: 2, unique: true, key: { sy: 1 }, name: "sy_1", ns: "arctic_FEED_2011.LEVEL1.metadata", background: true }
2021-01-20T04:28:50.547+0000 I INDEX    [conn4] build index done.  scanned 0 total records. 0 secs
2021-01-20T04:28:50.550+0000 I SHARDING [conn4] Marking collection arctic_FEED.LEVEL1.ARCTIC as collection version: <unsharded>
2021-01-20T04:28:50.550+0000 I STORAGE  [conn4] createCollection: arctic_FEED.LEVEL1.ARCTIC with generated UUID: 79a45195-08f0-48cd-9378-f9821ac309d3
2021-01-20T04:28:50.566+0000 I SHARDING [conn4] Marking collection meta_db.settings as collection version: <unsharded>
2021-01-20T04:28:50.569+0000 I SHARDING [conn4] Marking collection arctic_FEED.LEVEL1 as collection version: <unsharded>
2021-01-20T04:28:50.569+0000 I STORAGE  [conn4] createCollection: arctic_FEED.LEVEL1 with generated UUID: 7d8cb7b3-81dc-420d-b4db-e69aef7f3d69
2021-01-20T04:28:50.598+0000 I INDEX    [conn4] build index on: arctic_FEED.LEVEL1 properties: { v: 2, key: { start: 1 }, name: "start_1", ns: "arctic_FEED.LEVEL1", background: true }
2021-01-20T04:28:50.598+0000 I INDEX    [conn4] build index done.  scanned 2 total records. 0 secs
2021-01-20T04:28:50.607+0000 I SHARDING [conn4] Marking collection arctic_FEED_2010.LEVEL1 as collection version: <unsharded>
2021-01-20T04:28:50.614+0000 I SHARDING [conn4] Marking collection arctic_FEED_2011.LEVEL1 as collection version: <unsharded>
----------------------------- Captured stderr call -----------------------------
2021-01-20 04:28:50,612 DEBUG arctic.tickstore.tickstore 1 buckets in 0.001178: approx 84889643 ticks/sec
2021-01-20 04:28:50,617 DEBUG arctic.tickstore.tickstore 1 buckets in 0.000873: approx 114547537 ticks/sec
2021-01-20 04:28:50,623 INFO arctic.tickstore.tickstore Got data in 0.004375 secs, creating DataFrame...
2021-01-20 04:28:50,624 INFO arctic.tickstore.tickstore 31 rows in 0.005442 secs: 5696 ticks/sec
2021-01-20 04:28:50,630 INFO arctic.tickstore.tickstore Got data in 0.003901 secs, creating DataFrame...
2021-01-20 04:28:50,631 INFO arctic.tickstore.tickstore 26 rows in 0.004938 secs: 5265 ticks/sec
------------------------------ Captured log call -------------------------------
DEBUG    arctic.tickstore.tickstore:tickstore.py:612 1 buckets in 0.001178: approx 84889643 ticks/sec
DEBUG    arctic.tickstore.tickstore:tickstore.py:612 1 buckets in 0.000873: approx 114547537 ticks/sec
INFO     arctic.tickstore.tickstore:tickstore.py:355 Got data in 0.004375 secs, creating DataFrame...
INFO     arctic.tickstore.tickstore:tickstore.py:364 31 rows in 0.005442 secs: 5696 ticks/sec
INFO     arctic.tickstore.tickstore:tickstore.py:355 Got data in 0.003901 secs, creating DataFrame...
INFO     arctic.tickstore.tickstore:tickstore.py:364 26 rows in 0.004938 secs: 5265 ticks/sec
--------------------------- Captured stderr teardown ---------------------------
2021-01-20 04:28:50,659 DEBUG pytest_server_fixtures.serverclass.thread Killing process tree for 32159 (total_procs_to_kill=1)
2021-01-20 04:28:50,659 DEBUG pytest_server_fixtures.serverclass.thread Killing 1 processes with signal Signals.SIGKILL
2021-01-20 04:28:50,660 DEBUG pytest_server_fixtures.serverclass.thread Waiting for 1 processes to die
2021-01-20 04:28:50,664 DEBUG pytest_server_fixtures.serverclass.thread All processes are terminated
2021-01-20 04:28:50,664 DEBUG pytest_shutil.workspace 
2021-01-20 04:28:50,664 DEBUG pytest_shutil.workspace =======================================================
2021-01-20 04:28:50,664 DEBUG pytest_shutil.workspace pytest_shutil deleting workspace /tmp/tmpvwnk38gh
2021-01-20 04:28:50,664 DEBUG pytest_shutil.workspace =======================================================
2021-01-20 04:28:50,664 DEBUG pytest_shutil.workspace 
---------------------------- Captured log teardown -----------------------------
DEBUG    pytest_server_fixtures.serverclass.thread:thread.py:54 Killing process tree for 32159 (total_procs_to_kill=1)
DEBUG    pytest_server_fixtures.serverclass.thread:thread.py:35 Killing 1 processes with signal Signals.SIGKILL
DEBUG    pytest_server_fixtures.serverclass.thread:thread.py:39 Waiting for 1 processes to die
DEBUG    pytest_server_fixtures.serverclass.thread:thread.py:43 All processes are terminated
DEBUG    pytest_shutil.workspace:workspace.py:140 
DEBUG    pytest_shutil.workspace:workspace.py:141 =======================================================
DEBUG    pytest_shutil.workspace:workspace.py:142 pytest_shutil deleting workspace /tmp/tmpvwnk38gh
DEBUG    pytest_shutil.workspace:workspace.py:143 =======================================================
DEBUG    pytest_shutil.workspace:workspace.py:144
______________ test_should_write_top_level_with_correct_timezone _______________
arctic = <Arctic at 0x7fd75d297780, connected to MongoClient(host=['127.112.217.158:20341'], document_class=dict, tz_aware=False, connect=True)>
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
2021-01-20T04:28:50.691+0000 I CONTROL  [main] Automatically disabling TLS 1.0, to force-enable TLS 1.0 specify --sslDisabledProtocols 'none'
2021-01-20T04:28:50.693+0000 I CONTROL  [initandlisten] MongoDB starting : pid=32195 port=20341 dbpath=/tmp/tmpcgxhkan_ 64-bit host=travis-job-36a0a3d3-bff5-4832-a5cc-28dd585378fb
2021-01-20T04:28:50.693+0000 I CONTROL  [initandlisten] db version v4.0.19
2021-01-20T04:28:50.693+0000 I CONTROL  [initandlisten] git version: 7e28f4296a04d858a2e3dd84a1e79c9ba59a9568
2021-01-20T04:28:50.693+0000 I CONTROL  [initandlisten] OpenSSL version: OpenSSL 1.0.2g  1 Mar 2016
2021-01-20T04:28:50.693+0000 I CONTROL  [initandlisten] allocator: tcmalloc
2021-01-20T04:28:50.693+0000 I CONTROL  [initandlisten] modules: none
2021-01-20T04:28:50.693+0000 I CONTROL  [initandlisten] build environment:
2021-01-20T04:28:50.693+0000 I CONTROL  [initandlisten]     distmod: ubuntu1604
2021-01-20T04:28:50.693+0000 I CONTROL  [initandlisten]     distarch: x86_64
2021-01-20T04:28:50.693+0000 I CONTROL  [initandlisten]     target_arch: x86_64
2021-01-20T04:28:50.693+0000 I CONTROL  [initandlisten] options: { net: { bindIp: "127.112.217.158", port: 20341, unixDomainSocket: { enabled: false } }, storage: { dbPath: "/tmp/tmpcgxhkan_", journal: { enabled: false }, syncPeriodSecs: 0.0 }, systemLog: { quiet: true } }
2021-01-20T04:28:50.693+0000 I STORAGE  [initandlisten] 
2021-01-20T04:28:50.693+0000 I STORAGE  [initandlisten] ** WARNING: Using the XFS filesystem is strongly recommended with the WiredTiger storage engine
2021-01-20T04:28:50.693+0000 I STORAGE  [initandlisten] **          See http://dochub.mongodb.org/core/prodnotes-filesystem
2021-01-20T04:28:50.693+0000 I STORAGE  [initandlisten] wiredtiger_open config: create,cache_size=3476M,cache_overflow=(file_max=0M),session_max=20000,eviction=(threads_min=4,threads_max=4),config_base=false,statistics=(fast),log=(enabled=true,archive=true,path=journal,compressor=snappy),file_manager=(close_idle_time=100000),statistics_log=(wait=0),verbose=(recovery_progress),,log=(enabled=false),
2021-01-20T04:28:51.176+0000 I STORAGE  [initandlisten] WiredTiger message [1611116931:176947][32195:0x7fe761127a80], txn-recover: Set global recovery timestamp: 0
2021-01-20T04:28:51.187+0000 I RECOVERY [initandlisten] WiredTiger recoveryTimestamp. Ts: Timestamp(0, 0)
2021-01-20T04:28:51.207+0000 I CONTROL  [initandlisten] 
2021-01-20T04:28:51.207+0000 I CONTROL  [initandlisten] ** WARNING: Access control is not enabled for the database.
2021-01-20T04:28:51.207+0000 I CONTROL  [initandlisten] **          Read and write access to data and configuration is unrestricted.
2021-01-20T04:28:51.207+0000 I CONTROL  [initandlisten] 
2021-01-20T04:28:51.207+0000 I STORAGE  [initandlisten] createCollection: admin.system.version with provided UUID: e1a259b6-6ecd-4f00-b489-78c5b2da76a9
2021-01-20T04:28:51.222+0000 I SHARDING [initandlisten] Marking collection admin.system.version as collection version: <unsharded>
2021-01-20T04:28:51.222+0000 I COMMAND  [initandlisten] setting featureCompatibilityVersion to 4.0
2021-01-20T04:28:51.222+0000 I SHARDING [initandlisten] Marking collection local.system.replset as collection version: <unsharded>
2021-01-20T04:28:51.222+0000 I SHARDING [initandlisten] Marking collection admin.system.roles as collection version: <unsharded>
2021-01-20T04:28:51.222+0000 I STORAGE  [initandlisten] createCollection: local.startup_log with generated UUID: 72caf613-033a-4a39-bea8-5a50e4a3fbd4
2021-01-20T04:28:51.236+0000 I SHARDING [initandlisten] Marking collection local.startup_log as collection version: <unsharded>
2021-01-20T04:28:51.236+0000 I FTDC     [initandlisten] Initializing full-time diagnostic data capture with directory '/tmp/tmpcgxhkan_/diagnostic.data'
2021-01-20T04:28:51.237+0000 I SHARDING [LogicalSessionCacheRefresh] Marking collection config.system.sessions as collection version: <unsharded>
2021-01-20T04:28:51.237+0000 I NETWORK  [initandlisten] waiting for connections on port 20341
2021-01-20T04:28:51.238+0000 I STORAGE  [LogicalSessionCacheRefresh] createCollection: config.system.sessions with generated UUID: ee778cf1-8eec-480f-b5a1-5f93ebcdcd25
2021-01-20T04:28:51.238+0000 I CONTROL  [LogicalSessionCacheReap] Sessions collection is not set up; waiting until next sessions reap interval: config.system.sessions does not exist
2021-01-20T04:28:51.259+0000 I INDEX    [LogicalSessionCacheRefresh] build index on: config.system.sessions properties: { v: 2, key: { lastUse: 1 }, name: "lsidTTLIndex", ns: "config.system.sessions", expireAfterSeconds: 1800 }
2021-01-20T04:28:51.259+0000 I INDEX    [LogicalSessionCacheRefresh] 	 building index using bulk method; build may temporarily use up to 500 megabytes of RAM
2021-01-20T04:28:51.259+0000 W STORAGE  [LogicalSessionCacheRefresh] failed to create WiredTiger bulk cursor: Device or resource busy
2021-01-20T04:28:51.259+0000 W STORAGE  [LogicalSessionCacheRefresh] falling back to non-bulk cursor for index table:index-6--3518140250955501074
2021-01-20T04:28:51.259+0000 I INDEX    [LogicalSessionCacheRefresh] build index done.  scanned 0 total records. 0 secs
2021-01-20T04:28:51.285+0000 I NETWORK  [conn1] received client metadata from 127.0.0.1:53548 conn1: { driver: { name: "PyMongo", version: "3.11.2" }, os: { type: "Linux", name: "Linux", architecture: "x86_64", version: "4.15.0-1077-gcp" }, platform: "CPython 3.6.7.final.0" }
2021-01-20T04:28:51.287+0000 I NETWORK  [conn2] received client metadata from 127.0.0.1:53550 conn2: { driver: { name: "PyMongo", version: "3.11.2" }, os: { type: "Linux", name: "Linux", architecture: "x86_64", version: "4.15.0-1077-gcp" }, platform: "CPython 3.6.7.final.0" }
2021-01-20T04:28:51.290+0000 I NETWORK  [conn3] received client metadata from 127.0.0.1:53552 conn3: { driver: { name: "PyMongo", version: "3.11.2" }, os: { type: "Linux", name: "Linux", architecture: "x86_64", version: "4.15.0-1077-gcp" }, platform: "CPython 3.6.7.final.0" }
2021-01-20T04:28:51.292+0000 I NETWORK  [conn4] received client metadata from 127.0.0.1:53554 conn4: { driver: { name: "PyMongo", version: "3.11.2" }, os: { type: "Linux", name: "Linux", architecture: "x86_64", version: "4.15.0-1077-gcp" }, platform: "CPython 3.6.7.final.0" }
2021-01-20T04:28:51.295+0000 I SHARDING [conn4] Marking collection meta_db.cache as collection version: <unsharded>
2021-01-20T04:28:51.295+0000 I STORAGE  [conn4] createCollection: meta_db.cache with generated UUID: 02f2ec94-20ce-4f68-918f-66803497c01a
2021-01-20T04:28:51.316+0000 I INDEX    [conn4] build index on: meta_db.cache properties: { v: 2, key: { date: 1 }, name: "date_1", ns: "meta_db.cache", expireAfterSeconds: 3600 }
2021-01-20T04:28:51.316+0000 I INDEX    [conn4] 	 building index using bulk method; build may temporarily use up to 500 megabytes of RAM
2021-01-20T04:28:51.316+0000 W STORAGE  [conn4] failed to create WiredTiger bulk cursor: Device or resource busy
2021-01-20T04:28:51.316+0000 W STORAGE  [conn4] falling back to non-bulk cursor for index table:index-9--3518140250955501074
2021-01-20T04:28:51.316+0000 I INDEX    [conn4] build index done.  scanned 0 total records. 0 secs
---------------------------- Captured stderr setup -----------------------------
2021-01-20 04:28:50,667 DEBUG pytest_shutil.workspace 
2021-01-20 04:28:50,667 DEBUG pytest_shutil.workspace =======================================================
2021-01-20 04:28:50,667 DEBUG pytest_shutil.workspace pytest_shutil created workspace /tmp/tmpcgxhkan_
2021-01-20 04:28:50,668 DEBUG pytest_shutil.workspace This workspace will delete itself on teardown
2021-01-20 04:28:50,668 DEBUG pytest_shutil.workspace =======================================================
2021-01-20 04:28:50,668 DEBUG pytest_shutil.workspace 
2021-01-20 04:28:50,668 DEBUG pytest_server_fixtures.serverclass.thread Launching thread server.
2021-01-20 04:28:50,676 DEBUG pytest_server_fixtures.serverclass.thread Running server: mongod --bind_ip=127.112.217.158 --port=20341 --nounixsocket --syncdelay=0 --nojournal --quiet --dbpath=/tmp/tmpcgxhkan_
2021-01-20 04:28:50,677 DEBUG pytest_server_fixtures.serverclass.thread CWD: /home/travis/build/man-group/arctic
2021-01-20 04:28:50,677 DEBUG pytest_server_fixtures.base2 sleeping for 0.1 before retrying (1 of 28)
2021-01-20 04:28:50,677 INFO pytest_server_fixtures.mongo Connecting to Mongo at 127.112.217.158:20341
2021-01-20 04:28:51,283 DEBUG pytest_server_fixtures.base2 sleeping for 0.1 before retrying (2 of 28)
2021-01-20 04:28:51,283 INFO pytest_server_fixtures.mongo Connecting to Mongo at 127.112.217.158:20341
2021-01-20 04:28:51,290 DEBUG pytest_server_fixtures.base2 waited 0:00:00.613254 for server to start successfully
2021-01-20 04:28:51,291 DEBUG pytest_server_fixtures.base2 Server now awake
2021-01-20 04:28:51,292 INFO arctic.fixtures.arctic arctic.fixtures: arctic init()
------------------------------ Captured log setup ------------------------------
DEBUG    pytest_shutil.workspace:workspace.py:52 
DEBUG    pytest_shutil.workspace:workspace.py:53 =======================================================
DEBUG    pytest_shutil.workspace:workspace.py:56 pytest_shutil created workspace /tmp/tmpcgxhkan_
DEBUG    pytest_shutil.workspace:workspace.py:64 This workspace will delete itself on teardown
DEBUG    pytest_shutil.workspace:workspace.py:65 =======================================================
DEBUG    pytest_shutil.workspace:workspace.py:66 
DEBUG    pytest_server_fixtures.serverclass.thread:thread.py:77 Launching thread server.
DEBUG    pytest_server_fixtures.serverclass.thread:thread.py:89 Running server: mongod --bind_ip=127.112.217.158 --port=20341 --nounixsocket --syncdelay=0 --nojournal --quiet --dbpath=/tmp/tmpcgxhkan_
DEBUG    pytest_server_fixtures.serverclass.thread:thread.py:90 CWD: /home/travis/build/man-group/arctic
DEBUG    pytest_server_fixtures.base2:base2.py:226 sleeping for 0.1 before retrying (1 of 28)
INFO     pytest_server_fixtures.mongo:mongo.py:128 Connecting to Mongo at 127.112.217.158:20341
DEBUG    pytest_server_fixtures.base2:base2.py:226 sleeping for 0.1 before retrying (2 of 28)
INFO     pytest_server_fixtures.mongo:mongo.py:128 Connecting to Mongo at 127.112.217.158:20341
DEBUG    pytest_server_fixtures.base2:base2.py:229 waited 0:00:00.613254 for server to start successfully
DEBUG    pytest_server_fixtures.base2:base2.py:69 Server now awake
INFO     arctic.fixtures.arctic:arctic.py:23 arctic.fixtures: arctic init()
----------------------------- Captured stdout call -----------------------------
2021-01-20T04:28:51.319+0000 I SHARDING [conn4] Marking collection arctic_FEED_2010.LEVEL1.ARCTIC as collection version: <unsharded>
2021-01-20T04:28:51.319+0000 I STORAGE  [conn4] createCollection: arctic_FEED_2010.LEVEL1.ARCTIC with generated UUID: 8ac351b6-ed97-42db-b292-0a5066469359
2021-01-20T04:28:51.333+0000 I STORAGE  [conn4] createCollection: arctic_FEED_2010.LEVEL1 with generated UUID: 356545f6-4f74-4f10-ae4d-5bc038d41914
2021-01-20T04:28:51.359+0000 I INDEX    [conn4] build index on: arctic_FEED_2010.LEVEL1 properties: { v: 2, key: { sy: 1, s: 1 }, name: "sy_1_s_1", ns: "arctic_FEED_2010.LEVEL1", background: true }
2021-01-20T04:28:51.359+0000 I INDEX    [conn4] build index done.  scanned 0 total records. 0 secs
2021-01-20T04:28:51.366+0000 I INDEX    [conn4] build index on: arctic_FEED_2010.LEVEL1 properties: { v: 2, key: { s: 1 }, name: "s_1", ns: "arctic_FEED_2010.LEVEL1", background: true }
2021-01-20T04:28:51.366+0000 I INDEX    [conn4] build index done.  scanned 0 total records. 0 secs
2021-01-20T04:28:51.367+0000 I STORAGE  [conn4] createCollection: arctic_FEED_2010.LEVEL1.metadata with generated UUID: 9ebf9d6d-91bc-4541-baef-7e205e30895d
2021-01-20T04:28:51.381+0000 I SHARDING [conn4] Marking collection arctic_FEED_2010.LEVEL1.metadata as collection version: <unsharded>
2021-01-20T04:28:51.389+0000 I INDEX    [conn4] build index on: arctic_FEED_2010.LEVEL1.metadata properties: { v: 2, unique: true, key: { sy: 1 }, name: "sy_1", ns: "arctic_FEED_2010.LEVEL1.metadata", background: true }
2021-01-20T04:28:51.389+0000 I INDEX    [conn4] build index done.  scanned 0 total records. 0 secs
2021-01-20T04:28:51.393+0000 I SHARDING [conn4] Marking collection arctic_FEED_2011.LEVEL1.ARCTIC as collection version: <unsharded>
2021-01-20T04:28:51.393+0000 I STORAGE  [conn4] createCollection: arctic_FEED_2011.LEVEL1.ARCTIC with generated UUID: 55bdc3a6-f9a8-4a25-bb57-85feb5a10c77
2021-01-20T04:28:51.406+0000 I STORAGE  [conn4] createCollection: arctic_FEED_2011.LEVEL1 with generated UUID: 14963704-67bd-463c-818a-24737017b39f
2021-01-20T04:28:51.427+0000 I INDEX    [conn4] build index on: arctic_FEED_2011.LEVEL1 properties: { v: 2, key: { sy: 1, s: 1 }, name: "sy_1_s_1", ns: "arctic_FEED_2011.LEVEL1", background: true }
2021-01-20T04:28:51.427+0000 I INDEX    [conn4] build index done.  scanned 0 total records. 0 secs
2021-01-20T04:28:51.434+0000 I INDEX    [conn4] build index on: arctic_FEED_2011.LEVEL1 properties: { v: 2, key: { s: 1 }, name: "s_1", ns: "arctic_FEED_2011.LEVEL1", background: true }
2021-01-20T04:28:51.434+0000 I INDEX    [conn4] build index done.  scanned 0 total records. 0 secs
2021-01-20T04:28:51.435+0000 I STORAGE  [conn4] createCollection: arctic_FEED_2011.LEVEL1.metadata with generated UUID: ce69313a-d22c-40a6-8318-30359b89776f
2021-01-20T04:28:51.449+0000 I SHARDING [conn4] Marking collection arctic_FEED_2011.LEVEL1.metadata as collection version: <unsharded>
2021-01-20T04:28:51.457+0000 I INDEX    [conn4] build index on: arctic_FEED_2011.LEVEL1.metadata properties: { v: 2, unique: true, key: { sy: 1 }, name: "sy_1", ns: "arctic_FEED_2011.LEVEL1.metadata", background: true }
2021-01-20T04:28:51.457+0000 I INDEX    [conn4] build index done.  scanned 0 total records. 0 secs
2021-01-20T04:28:51.461+0000 I SHARDING [conn4] Marking collection arctic_FEED.LEVEL1.ARCTIC as collection version: <unsharded>
2021-01-20T04:28:51.461+0000 I STORAGE  [conn4] createCollection: arctic_FEED.LEVEL1.ARCTIC with generated UUID: 39004ae7-6f39-4c91-8618-a6d3a4ec1780
2021-01-20T04:28:51.475+0000 I SHARDING [conn4] Marking collection meta_db.settings as collection version: <unsharded>
2021-01-20T04:28:51.478+0000 I SHARDING [conn4] Marking collection arctic_FEED.LEVEL1 as collection version: <unsharded>
2021-01-20T04:28:51.479+0000 I STORAGE  [conn4] createCollection: arctic_FEED.LEVEL1 with generated UUID: fff9e4e6-5f8b-4d96-83dd-573cc9017f5a
2021-01-20T04:28:51.506+0000 I INDEX    [conn4] build index on: arctic_FEED.LEVEL1 properties: { v: 2, key: { start: 1 }, name: "start_1", ns: "arctic_FEED.LEVEL1", background: true }
2021-01-20T04:28:51.506+0000 I INDEX    [conn4] build index done.  scanned 2 total records. 0 secs
2021-01-20T04:28:51.513+0000 I SHARDING [conn4] Marking collection arctic_FEED_2010.LEVEL1 as collection version: <unsharded>
2021-01-20T04:28:51.516+0000 I SHARDING [conn4] Marking collection arctic_FEED_2011.LEVEL1 as collection version: <unsharded>
----------------------------- Captured stderr call -----------------------------
2021-01-20 04:28:51,515 DEBUG arctic.tickstore.tickstore 1 buckets in 0.000984: approx 101626016 ticks/sec
2021-01-20 04:28:51,519 DEBUG arctic.tickstore.tickstore 1 buckets in 0.000899: approx 111234705 ticks/sec
2021-01-20 04:28:51,523 INFO arctic.tickstore.tickstore Got data in 0.003031 secs, creating DataFrame...
2021-01-20 04:28:51,524 INFO arctic.tickstore.tickstore 1 rows in 0.004003 secs: 249 ticks/sec
2021-01-20 04:28:51,528 INFO arctic.tickstore.tickstore Got data in 0.002516 secs, creating DataFrame...
2021-01-20 04:28:51,529 INFO arctic.tickstore.tickstore 9 rows in 0.003394 secs: 2651 ticks/sec
------------------------------ Captured log call -------------------------------
DEBUG    arctic.tickstore.tickstore:tickstore.py:612 1 buckets in 0.000984: approx 101626016 ticks/sec
DEBUG    arctic.tickstore.tickstore:tickstore.py:612 1 buckets in 0.000899: approx 111234705 ticks/sec
INFO     arctic.tickstore.tickstore:tickstore.py:355 Got data in 0.003031 secs, creating DataFrame...
INFO     arctic.tickstore.tickstore:tickstore.py:364 1 rows in 0.004003 secs: 249 ticks/sec
INFO     arctic.tickstore.tickstore:tickstore.py:355 Got data in 0.002516 secs, creating DataFrame...
INFO     arctic.tickstore.tickstore:tickstore.py:364 9 rows in 0.003394 secs: 2651 ticks/sec
--------------------------- Captured stderr teardown ---------------------------
2021-01-20 04:28:51,558 DEBUG pytest_server_fixtures.serverclass.thread Killing process tree for 32195 (total_procs_to_kill=1)
2021-01-20 04:28:51,559 DEBUG pytest_server_fixtures.serverclass.thread Killing 1 processes with signal Signals.SIGKILL
2021-01-20 04:28:51,559 DEBUG pytest_server_fixtures.serverclass.thread Waiting for 1 processes to die
2021-01-20 04:28:51,563 DEBUG pytest_server_fixtures.serverclass.thread All processes are terminated
2021-01-20 04:28:51,563 DEBUG pytest_shutil.workspace 
2021-01-20 04:28:51,563 DEBUG pytest_shutil.workspace =======================================================
2021-01-20 04:28:51,563 DEBUG pytest_shutil.workspace pytest_shutil deleting workspace /tmp/tmpcgxhkan_
2021-01-20 04:28:51,563 DEBUG pytest_shutil.workspace =======================================================
2021-01-20 04:28:51,563 DEBUG pytest_shutil.workspace 
---------------------------- Captured log teardown -----------------------------
DEBUG    pytest_server_fixtures.serverclass.thread:thread.py:54 Killing process tree for 32195 (total_procs_to_kill=1)
DEBUG    pytest_server_fixtures.serverclass.thread:thread.py:35 Killing 1 processes with signal Signals.SIGKILL
DEBUG    pytest_server_fixtures.serverclass.thread:thread.py:39 Waiting for 1 processes to die
DEBUG    pytest_server_fixtures.serverclass.thread:thread.py:43 All processes are terminated
DEBUG    pytest_shutil.workspace:workspace.py:140 
DEBUG    pytest_shutil.workspace:workspace.py:141 =======================================================
DEBUG    pytest_shutil.workspace:workspace.py:142 pytest_shutil deleting workspace /tmp/tmpcgxhkan_
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
_mock_self = <Mock name='mock._delete_version' id='140561829182208'>
args = (sentinel.symbol, 3), kwargs = {}
self = <Mock name='mock._delete_version' id='140561829182208'>
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
2021-01-20 04:32:25,535 INFO arctic.store.audit MT: None@None: [sentinel.user] sentinel.log: sentinel.symbol
Exception in thread Thread-773:
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
= 5 failed, 1311 passed, 3 skipped, 19 xfailed, 1 xpassed, 60744 warnings in 1272.69s (0:21:12) =
The command "python setup.py test --pytest-args=-v" exited with 1.
1.26s$ pycodestyle arctic
The command "pycodestyle arctic" exited with 0.
Done. Your build exited with 1.
```