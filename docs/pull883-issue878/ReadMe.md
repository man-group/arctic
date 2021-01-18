# [#878: v1.80 test failures - are these expected?](https://github.com/man-group/arctic/issues/878) 

> Note: Revised `tox.ini` to more closely match `.travis.yml`

The following steps were taken to address issue #878:

1. Previous work was done using a manually configured Python 3.6 virtual 
   environment.  
2. Some errors and warnings were thought to come from package version 
   differences in the manually configured py36 environment.
3. A basic tox implementation was added to this current work to automate 
   the creation of virtual environments and run the tests.   
4. Running `tox` as configured will install `setup.py develop` and run 
   `setup.py tests` for both `dev27`, `dev36` and `dev37`.
   > Note: the setup.py was revised to not include Python 3.4 and 3.5

| venv  |            tox test run              |
|:-----:|:------------------------------------:|
| dev27 | /.tox/dev27/bin/python setup.py test |
| dev36 | /.tox/dev36/bin/python setup.py test |
| dev37 | /.tox/dev37/bin/python setup.py test |

## Local `tox` Test Results
* `/before` directory logs the tox test run - before code changes.
* `/after` directory logs the tox test run - after code changes.


### Python 2.7 (dev27) Test Pareto
|   Status |  before |   after |    delta |
|---------:|--------:|--------:|---------:|
|   failed |      27 |      28 |       +1 |
|   passed |    1290 |    1289 |       -1 |
|  skipped |       3 |       3 |        0 |
|  xfailed |       7 |       7 |        0 |
|  xpassed |      12 |      12 |        0 |
| warnings |      26 |      41 |      +15 |
| test sec | 5331.36 | 2233.08 | -3098.28 |

=========================== short test summary info ============================
 1 tests/integration/tickstore/test_toplevel.py:65: test_should_return_data_when_date_range_falls_in_a_single_underlying_library
 2 tests/integration/tickstore/test_toplevel.py:83: test_should_return_data_when_date_range_spans_libraries
 3 tests/integration/tickstore/test_toplevel.py:101: test_should_return_data_when_date_range_spans_libraries_even_if_one_returns_nothing
 4 tests/integration/tickstore/test_toplevel.py:113: test_should_add_underlying_library_where_another_library_exists_in_a_non_overlapping_daterange
 5 tests/integration/tickstore/test_toplevel.py:197 test_should_write_top_level_with_list_of_dicts
 6 tests/integration/tickstore/test_toplevel.py:215 test_should_write_top_level_with_correct_timezone
 7 tests/integration/tickstore/test_ts_read.py:234: AssertionError test_date_range(tickstore_lib)
 8 tests/integration/tickstore/test_ts_read.py:300: AssertionError test_date_range_end_not_in_range
 9 tests/integration/tickstore/test_ts_read.py:369: AssertionError test_date_range_no_bounds(tickstore_lib)
10 tests/unit/tickstore/test_tickstore.py:43: AssertionError test_mongo_date_range_query
11 tests/unit/tickstore/test_tickstore.py:97: AssertionError test_tickstore_to_bucket_with_image
12 tests/unit/tickstore/test_tickstore.py:162: AssertionError test_tickstore_pandas_to_bucket_image


### Python 3.6 (dev36) Test Pareto
|   Status |  before |   after |    delta |
|---------:|--------:|--------:|---------:|
|   failed |      84 |      28 |      -52 |
|   passed |    1232 |    1288 |      +56 |
|  skipped |       3 |       3 |        0 |
|  xfailed |      19 |      19 |        0 |
|  xpassed |       1 |       1 |        0 |
| warnings |   60836 |   60732 |     -104 |
| test sec | 4895.18 | 2611.78 | -2283.40 |

=========================== short test summary info ============================
not found in dev27
FAILED tests/integration/test_arctic.py::test_indexes - AssertionError: asser...
FAILED tests/integration/scripts/test_arctic_fsck.py::test_cleanup_orphaned_chunks[False-data6-FwPointersCfg.DISABLED]
FAILED tests/integration/scripts/test_arctic_fsck.py::test_cleanup_orphaned_chunks[False-data7-FwPointersCfg.HYBRID]
FAILED tests/integration/scripts/test_arctic_fsck.py::test_cleanup_orphaned_chunks[False-data8-FwPointersCfg.ENABLED]
FAILED tests/integration/scripts/test_arctic_fsck.py::test_cleanup_orphaned_chunks[False-data9-FwPointersCfg.DISABLED]
FAILED tests/integration/scripts/test_arctic_fsck.py::test_cleanup_orphaned_chunks[False-data10-FwPointersCfg.HYBRID]
FAILED tests/integration/scripts/test_arctic_fsck.py::test_cleanup_orphaned_chunks[False-data11-FwPointersCfg.ENABLED]
FAILED tests/integration/scripts/test_arctic_fsck.py::test_cleanup_orphaned_snapshots[False-data6-FwPointersCfg.DISABLED]
FAILED tests/integration/scripts/test_arctic_fsck.py::test_cleanup_orphaned_snapshots[False-data7-FwPointersCfg.HYBRID]
FAILED tests/integration/scripts/test_arctic_fsck.py::test_cleanup_orphaned_snapshots[False-data8-FwPointersCfg.ENABLED]
FAILED tests/integration/scripts/test_arctic_fsck.py::test_cleanup_orphaned_snapshots[False-data9-FwPointersCfg.DISABLED]
FAILED tests/integration/scripts/test_arctic_fsck.py::test_cleanup_orphaned_snapshots[False-data10-FwPointersCfg.HYBRID]
FAILED tests/integration/scripts/test_arctic_fsck.py::test_cleanup_orphaned_snapshots[False-data11-FwPointersCfg.ENABLED]
FAILED tests/integration/scripts/test_prune_versions.py::test_fix_broken_snapshot_references
FAILED tests/integration/scripts/test_prune_versions.py::test_keep_only_one_version
10 FAILED tests/unit/store/test_version_store_audit.py::test_ArcticTransaction_detects_concurrent_writes

also found in dev27
 1 FAILED tests/integration/tickstore/test_toplevel.py::test_should_return_data_when_date_range_falls_in_a_single_underlying_library
 2 FAILED tests/integration/tickstore/test_toplevel.py::test_should_return_data_when_date_range_spans_libraries
 3 FAILED tests/integration/tickstore/test_toplevel.py::test_should_return_data_when_date_range_spans_libraries_even_if_one_returns_nothing
 4 FAILED tests/integration/tickstore/test_toplevel.py::test_should_add_underlying_library_where_another_library_exists_in_a_non_overlapping_daterange
 5 FAILED tests/integration/tickstore/test_toplevel.py::test_should_write_top_level_with_list_of_dicts
 6 FAILED tests/integration/tickstore/test_toplevel.py::test_should_write_top_level_with_correct_timezone
 7 FAILED tests/integration/tickstore/test_ts_read.py::test_date_range[tickstore]
 8 FAILED tests/integration/tickstore/test_ts_read.py::test_date_range_end_not_in_range[tickstore]
 9 FAILED tests/integration/tickstore/test_ts_read.py::test_date_range_no_bounds[tickstore]
10 FAILED tests/unit/tickstore/test_tickstore.py::test_mongo_date_range_query - ...
11 FAILED tests/unit/tickstore/test_tickstore.py::test_tickstore_to_bucket_with_image
12 FAILED tests/unit/tickstore/test_tickstore.py::test_tickstore_pandas_to_bucket_image

### Python 3.7 (dev37) Test Pareto
|   Status |  before |   after |    delta |
|---------:|--------:|--------:|---------:|
|   failed |  broken |     230 |          |
|   passed |  broken |    1086 |          |
|  skipped |  broken |       3 |          |
|  xfailed |  broken |      20 |          |
|  xpassed |  broken |       0 |          |
| warnings |  broken |   58860 |          |
| test sec |  broken | 2560.64 |          |

> Note: dev37 was broken due to the `pandas Panel`

=========================== short test summary info ============================
FAILED tests/integration/test_arctic.py::test_indexes - AssertionError: asser...
FAILED tests/integration/test_arctic.py::test_quota - NameError: name 'Panel'...
FAILED tests/integration/test_arctic.py::test_lib_rename - NameError: name 'P...
FAILED tests/integration/test_arctic.py::test_lib_rename_namespace - NameErro...
FAILED tests/integration/test_arctic_multithreading.py::test_multiprocessing_safety
FAILED tests/integration/test_arctic_multithreading.py::test_multiprocessing_safety_parent_children_race
FAILED tests/integration/test_howtos.py::test_howto[how_to_use_arctic.py] - N...
FAILED tests/integration/scripts/test_arctic_fsck.py::test_cleanup_orphaned_chunks[True-data0-FwPointersCfg.DISABLED]
FAILED tests/integration/scripts/test_arctic_fsck.py::test_cleanup_orphaned_chunks[True-data1-FwPointersCfg.HYBRID]
FAILED tests/integration/scripts/test_arctic_fsck.py::test_cleanup_orphaned_chunks[True-data2-FwPointersCfg.ENABLED]
FAILED tests/integration/scripts/test_arctic_fsck.py::test_cleanup_orphaned_chunks[False-data6-FwPointersCfg.DISABLED]
FAILED tests/integration/scripts/test_arctic_fsck.py::test_cleanup_orphaned_chunks[False-data7-FwPointersCfg.HYBRID]
FAILED tests/integration/scripts/test_arctic_fsck.py::test_cleanup_orphaned_chunks[False-data8-FwPointersCfg.ENABLED]
FAILED tests/integration/scripts/test_arctic_fsck.py::test_cleanup_orphaned_chunks[False-data9-FwPointersCfg.DISABLED]
FAILED tests/integration/scripts/test_arctic_fsck.py::test_cleanup_orphaned_chunks[False-data10-FwPointersCfg.HYBRID]
FAILED tests/integration/scripts/test_arctic_fsck.py::test_cleanup_orphaned_chunks[False-data11-FwPointersCfg.ENABLED]
FAILED tests/integration/scripts/test_arctic_fsck.py::test_cleanup_noop[True-data0-FwPointersCfg.DISABLED]
FAILED tests/integration/scripts/test_arctic_fsck.py::test_cleanup_noop[True-data1-FwPointersCfg.HYBRID]
FAILED tests/integration/scripts/test_arctic_fsck.py::test_cleanup_noop[True-data2-FwPointersCfg.ENABLED]
FAILED tests/integration/scripts/test_arctic_fsck.py::test_cleanup_noop[False-data6-FwPointersCfg.DISABLED]
FAILED tests/integration/scripts/test_arctic_fsck.py::test_cleanup_noop[False-data7-FwPointersCfg.HYBRID]
FAILED tests/integration/scripts/test_arctic_fsck.py::test_cleanup_noop[False-data8-FwPointersCfg.ENABLED]
FAILED tests/integration/scripts/test_arctic_fsck.py::test_cleanup_orphaned_chunks_ignores_recent[True-data0-FwPointersCfg.DISABLED]
FAILED tests/integration/scripts/test_arctic_fsck.py::test_cleanup_orphaned_chunks_ignores_recent[True-data1-FwPointersCfg.HYBRID]
FAILED tests/integration/scripts/test_arctic_fsck.py::test_cleanup_orphaned_chunks_ignores_recent[True-data2-FwPointersCfg.ENABLED]
FAILED tests/integration/scripts/test_arctic_fsck.py::test_cleanup_orphaned_chunks_ignores_recent[False-data6-FwPointersCfg.DISABLED]
FAILED tests/integration/scripts/test_arctic_fsck.py::test_cleanup_orphaned_chunks_ignores_recent[False-data7-FwPointersCfg.HYBRID]
FAILED tests/integration/scripts/test_arctic_fsck.py::test_cleanup_orphaned_chunks_ignores_recent[False-data8-FwPointersCfg.ENABLED]
FAILED tests/integration/scripts/test_arctic_fsck.py::test_cleanup_orphaned_chunk_doesnt_break_versions[data0-FwPointersCfg.DISABLED]
FAILED tests/integration/scripts/test_arctic_fsck.py::test_cleanup_orphaned_chunk_doesnt_break_versions[data1-FwPointersCfg.HYBRID]
FAILED tests/integration/scripts/test_arctic_fsck.py::test_cleanup_orphaned_chunk_doesnt_break_versions[data2-FwPointersCfg.ENABLED]
FAILED tests/integration/scripts/test_arctic_fsck.py::test_cleanup_orphaned_chunk_doesnt_break_versions[data3-FwPointersCfg.DISABLED]
FAILED tests/integration/scripts/test_arctic_fsck.py::test_cleanup_orphaned_chunk_doesnt_break_versions[data4-FwPointersCfg.HYBRID]
FAILED tests/integration/scripts/test_arctic_fsck.py::test_cleanup_orphaned_chunk_doesnt_break_versions[data5-FwPointersCfg.ENABLED]
FAILED tests/integration/scripts/test_arctic_fsck.py::test_cleanup_orphaned_snapshots[True-data0-FwPointersCfg.DISABLED]
FAILED tests/integration/scripts/test_arctic_fsck.py::test_cleanup_orphaned_snapshots[True-data1-FwPointersCfg.HYBRID]
FAILED tests/integration/scripts/test_arctic_fsck.py::test_cleanup_orphaned_snapshots[True-data2-FwPointersCfg.ENABLED]
FAILED tests/integration/scripts/test_arctic_fsck.py::test_cleanup_orphaned_snapshots[False-data6-FwPointersCfg.DISABLED]
FAILED tests/integration/scripts/test_arctic_fsck.py::test_cleanup_orphaned_snapshots[False-data7-FwPointersCfg.HYBRID]
FAILED tests/integration/scripts/test_arctic_fsck.py::test_cleanup_orphaned_snapshots[False-data8-FwPointersCfg.ENABLED]
FAILED tests/integration/scripts/test_arctic_fsck.py::test_cleanup_orphaned_snapshots[False-data9-FwPointersCfg.DISABLED]
FAILED tests/integration/scripts/test_arctic_fsck.py::test_cleanup_orphaned_snapshots[False-data10-FwPointersCfg.HYBRID]
FAILED tests/integration/scripts/test_arctic_fsck.py::test_cleanup_orphaned_snapshots[False-data11-FwPointersCfg.ENABLED]
FAILED tests/integration/scripts/test_arctic_fsck.py::test_cleanup_orphaned_snapshots_nop[True-data0-FwPointersCfg.DISABLED]
FAILED tests/integration/scripts/test_arctic_fsck.py::test_cleanup_orphaned_snapshots_nop[True-data1-FwPointersCfg.HYBRID]
FAILED tests/integration/scripts/test_arctic_fsck.py::test_cleanup_orphaned_snapshots_nop[True-data2-FwPointersCfg.ENABLED]
FAILED tests/integration/scripts/test_arctic_fsck.py::test_cleanup_orphaned_snapshots_nop[False-data6-FwPointersCfg.DISABLED]
FAILED tests/integration/scripts/test_arctic_fsck.py::test_cleanup_orphaned_snapshots_nop[False-data7-FwPointersCfg.HYBRID]
FAILED tests/integration/scripts/test_arctic_fsck.py::test_cleanup_orphaned_snapshots_nop[False-data8-FwPointersCfg.ENABLED]
FAILED tests/integration/scripts/test_arctic_fsck.py::test_dont_cleanup_recent_orphaned_snapshots[True-data0-FwPointersCfg.DISABLED]
FAILED tests/integration/scripts/test_arctic_fsck.py::test_dont_cleanup_recent_orphaned_snapshots[True-data1-FwPointersCfg.HYBRID]
FAILED tests/integration/scripts/test_arctic_fsck.py::test_dont_cleanup_recent_orphaned_snapshots[True-data2-FwPointersCfg.ENABLED]
FAILED tests/integration/scripts/test_arctic_fsck.py::test_dont_cleanup_recent_orphaned_snapshots[False-data6-FwPointersCfg.DISABLED]
FAILED tests/integration/scripts/test_arctic_fsck.py::test_dont_cleanup_recent_orphaned_snapshots[False-data7-FwPointersCfg.HYBRID]
FAILED tests/integration/scripts/test_arctic_fsck.py::test_dont_cleanup_recent_orphaned_snapshots[False-data8-FwPointersCfg.ENABLED]
FAILED tests/integration/scripts/test_initialize_library.py::test_init_library
FAILED tests/integration/scripts/test_initialize_library.py::test_init_library_no_arctic_prefix
FAILED tests/integration/scripts/test_prune_versions.py::test_prune_versions_full
FAILED tests/integration/scripts/test_prune_versions.py::test_keep_recent_snapshots
FAILED tests/integration/scripts/test_prune_versions.py::test_fix_broken_snapshot_references
FAILED tests/integration/scripts/test_prune_versions.py::test_keep_only_one_version
FAILED tests/integration/store/test_bitemporal_store.py::test_write_ts_with_column_name_same_as_observed_dt_ok
FAILED tests/integration/store/test_ndarray_store.py::test_write_new_column_name_to_arctic_1_40_data
FAILED tests/integration/store/test_ndarray_store.py::test_save_read_simple_ndarray
FAILED tests/integration/store/test_ndarray_store.py::test_save_read_big_1darray[FwPointersCfg.DISABLED]
FAILED tests/integration/store/test_ndarray_store.py::test_save_read_big_1darray[FwPointersCfg.HYBRID]
FAILED tests/integration/store/test_ndarray_store.py::test_save_read_big_1darray[FwPointersCfg.ENABLED]
FAILED tests/integration/store/test_ndarray_store.py::test_save_and_resave_reuses_chunks[FwPointersCfg.DISABLED]
FAILED tests/integration/store/test_ndarray_store.py::test_save_and_resave_reuses_chunks[FwPointersCfg.HYBRID]
FAILED tests/integration/store/test_ndarray_store.py::test_save_and_resave_reuses_chunks[FwPointersCfg.ENABLED]
FAILED tests/integration/store/test_ndarray_store.py::test_save_read_big_2darray[FwPointersCfg.DISABLED]
FAILED tests/integration/store/test_ndarray_store.py::test_save_read_big_2darray[FwPointersCfg.HYBRID]
FAILED tests/integration/store/test_ndarray_store.py::test_save_read_big_2darray[FwPointersCfg.ENABLED]
FAILED tests/integration/store/test_ndarray_store.py::test_get_info_bson_object
FAILED tests/integration/store/test_ndarray_store.py::test_save_read_ndarray_with_array_field
FAILED tests/integration/store/test_ndarray_store.py::test_save_read_ndarray
FAILED tests/integration/store/test_ndarray_store.py::test_multiple_write[FwPointersCfg.DISABLED]
FAILED tests/integration/store/test_ndarray_store.py::test_multiple_write[FwPointersCfg.HYBRID]
FAILED tests/integration/store/test_ndarray_store.py::test_multiple_write[FwPointersCfg.ENABLED]
FAILED tests/integration/store/test_ndarray_store.py::test_save_read_large_ndarray
FAILED tests/integration/store/test_ndarray_store.py::test_mutable_ndarray - ...
FAILED tests/integration/store/test_ndarray_store_append.py::test_append_simple_ndarray[FwPointersCfg.DISABLED]
FAILED tests/integration/store/test_ndarray_store_append.py::test_append_simple_ndarray[FwPointersCfg.HYBRID]
FAILED tests/integration/store/test_ndarray_store_append.py::test_append_simple_ndarray[FwPointersCfg.ENABLED]
FAILED tests/integration/store/test_ndarray_store_append.py::test_append_simple_ndarray_promoting_types[FwPointersCfg.DISABLED]
FAILED tests/integration/store/test_ndarray_store_append.py::test_append_simple_ndarray_promoting_types[FwPointersCfg.HYBRID]
FAILED tests/integration/store/test_ndarray_store_append.py::test_append_simple_ndarray_promoting_types[FwPointersCfg.ENABLED]
FAILED tests/integration/store/test_ndarray_store_append.py::test_promote_types
FAILED tests/integration/store/test_ndarray_store_append.py::test_promote_types2
FAILED tests/integration/store/test_ndarray_store_append.py::test_promote_types_smaller_sizes
FAILED tests/integration/store/test_ndarray_store_append.py::test_promote_types_larger_sizes
FAILED tests/integration/store/test_ndarray_store_append.py::test_promote_field_types_smaller_sizes
FAILED tests/integration/store/test_ndarray_store_append.py::test_promote_field_types_larger_sizes
FAILED tests/integration/store/test_ndarray_store_append.py::test_append_ndarray_with_field_shape[FwPointersCfg.DISABLED]
FAILED tests/integration/store/test_ndarray_store_append.py::test_append_ndarray_with_field_shape[FwPointersCfg.HYBRID]
FAILED tests/integration/store/test_ndarray_store_append.py::test_append_ndarray_with_field_shape[FwPointersCfg.ENABLED]
FAILED tests/integration/store/test_ndarray_store_append.py::test_append_read_large_ndarray[FwPointersCfg.DISABLED]
FAILED tests/integration/store/test_ndarray_store_append.py::test_append_read_large_ndarray[FwPointersCfg.HYBRID]
FAILED tests/integration/store/test_ndarray_store_append.py::test_append_read_large_ndarray[FwPointersCfg.ENABLED]
FAILED tests/integration/store/test_ndarray_store_append.py::test_save_append_read_ndarray[FwPointersCfg.DISABLED]
FAILED tests/integration/store/test_ndarray_store_append.py::test_save_append_read_ndarray[FwPointersCfg.HYBRID]
FAILED tests/integration/store/test_ndarray_store_append.py::test_save_append_read_ndarray[FwPointersCfg.ENABLED]
FAILED tests/integration/store/test_ndarray_store_append.py::test_save_append_read_1row_ndarray
FAILED tests/integration/store/test_ndarray_store_append.py::test_append_too_large_ndarray
FAILED tests/integration/store/test_ndarray_store_append.py::test_empty_field_append_keeps_all_columns
FAILED tests/integration/store/test_ndarray_store_append.py::test_empty_append_promotes_dtype[FwPointersCfg.DISABLED]
FAILED tests/integration/store/test_ndarray_store_append.py::test_empty_append_promotes_dtype[FwPointersCfg.HYBRID]
FAILED tests/integration/store/test_ndarray_store_append.py::test_empty_append_promotes_dtype[FwPointersCfg.ENABLED]
FAILED tests/integration/store/test_ndarray_store_append.py::test_empty_append_promotes_dtype2
FAILED tests/integration/store/test_ndarray_store_append.py::test_empty_append_promotes_dtype3
FAILED tests/integration/store/test_ndarray_store_append.py::test_convert_to_structured_array
FAILED tests/integration/store/test_ndarray_store_append.py::test_empty_append_concat_and_rewrite[FwPointersCfg.DISABLED]
FAILED tests/integration/store/test_ndarray_store_append.py::test_empty_append_concat_and_rewrite[FwPointersCfg.HYBRID]
FAILED tests/integration/store/test_ndarray_store_append.py::test_empty_append_concat_and_rewrite[FwPointersCfg.ENABLED]
FAILED tests/integration/store/test_ndarray_store_append.py::test_empty_append_concat_and_rewrite_2[FwPointersCfg.DISABLED]
FAILED tests/integration/store/test_ndarray_store_append.py::test_empty_append_concat_and_rewrite_2[FwPointersCfg.HYBRID]
FAILED tests/integration/store/test_ndarray_store_append.py::test_empty_append_concat_and_rewrite_2[FwPointersCfg.ENABLED]
FAILED tests/integration/store/test_ndarray_store_append.py::test_empty_append_concat_and_rewrite_3[FwPointersCfg.DISABLED]
FAILED tests/integration/store/test_ndarray_store_append.py::test_empty_append_concat_and_rewrite_3[FwPointersCfg.HYBRID]
FAILED tests/integration/store/test_ndarray_store_append.py::test_empty_append_concat_and_rewrite_3[FwPointersCfg.ENABLED]
FAILED tests/integration/store/test_ndarray_store_append.py::test_append_with_extra_columns
FAILED tests/integration/store/test_ndarray_store_append.py::test_save_append_delete_append[FwPointersCfg.DISABLED]
FAILED tests/integration/store/test_ndarray_store_append.py::test_save_append_delete_append[FwPointersCfg.HYBRID]
FAILED tests/integration/store/test_ndarray_store_append.py::test_save_append_delete_append[FwPointersCfg.ENABLED]
FAILED tests/integration/store/test_ndarray_store_append.py::test_append_after_failed_append[FwPointersCfg.DISABLED]
FAILED tests/integration/store/test_ndarray_store_append.py::test_append_after_failed_append[FwPointersCfg.HYBRID]
FAILED tests/integration/store/test_ndarray_store_append.py::test_append_after_failed_append[FwPointersCfg.ENABLED]
FAILED tests/integration/store/test_ndarray_store_append.py::test_append_reorder_columns
FAILED tests/integration/store/test_pandas_store.py::test_can_write_pandas_df_with_object_columns
FAILED tests/integration/store/test_pandas_store.py::test_duplicate_labels - ...
FAILED tests/integration/store/test_pandas_store.py::test_no_labels - NameErr...
FAILED tests/integration/store/test_pickle_store.py::test_save_read_bson - Na...
FAILED tests/integration/store/test_pickle_store.py::test_save_read_big_encodable
FAILED tests/integration/store/test_pickle_store.py::test_save_read_bson_object
FAILED tests/integration/store/test_pickle_store.py::test_get_info_bson_object
FAILED tests/integration/store/test_pickle_store.py::test_bson_large_object
FAILED tests/integration/store/test_pickle_store.py::test_bson_leak_objects_delete
FAILED tests/integration/store/test_pickle_store.py::test_bson_leak_objects_prune_previous
FAILED tests/integration/store/test_pickle_store.py::test_prune_previous_doesnt_kill_other_objects
FAILED tests/integration/store/test_pickle_store.py::test_write_metadata - Na...
FAILED tests/integration/store/test_version_store.py::test_read_metadata_throws_on_deleted_symbol[FwPointersCfg.DISABLED]
FAILED tests/integration/store/test_version_store.py::test_read_metadata_throws_on_deleted_symbol[FwPointersCfg.HYBRID]
FAILED tests/integration/store/test_version_store.py::test_read_metadata_throws_on_deleted_symbol[FwPointersCfg.ENABLED]
FAILED tests/integration/store/test_version_store.py::test_append_should_overwrite_after_delete[FwPointersCfg.DISABLED]
FAILED tests/integration/store/test_version_store.py::test_append_should_overwrite_after_delete[FwPointersCfg.HYBRID]
FAILED tests/integration/store/test_version_store.py::test_append_should_overwrite_after_delete[FwPointersCfg.ENABLED]
FAILED tests/integration/store/test_version_store.py::test_list_version_deleted
FAILED tests/integration/store/test_version_store.py::test_delete_bson_versions[FwPointersCfg.DISABLED]
FAILED tests/integration/store/test_version_store.py::test_delete_bson_versions[FwPointersCfg.HYBRID]
FAILED tests/integration/store/test_version_store.py::test_delete_bson_versions[FwPointersCfg.ENABLED]
FAILED tests/integration/store/test_version_store.py::test_read_none_does_not_exception[FwPointersCfg.DISABLED]
FAILED tests/integration/store/test_version_store.py::test_read_none_does_not_exception[FwPointersCfg.HYBRID]
FAILED tests/integration/store/test_version_store.py::test_read_none_does_not_exception[FwPointersCfg.ENABLED]
FAILED tests/integration/store/test_version_store.py::test_delete_item_has_symbol[FwPointersCfg.DISABLED]
FAILED tests/integration/store/test_version_store.py::test_delete_item_has_symbol[FwPointersCfg.HYBRID]
FAILED tests/integration/store/test_version_store.py::test_delete_item_has_symbol[FwPointersCfg.ENABLED]
FAILED tests/integration/store/test_version_store.py::test_delete_item_snapshot[FwPointersCfg.DISABLED]
FAILED tests/integration/store/test_version_store.py::test_delete_item_snapshot[FwPointersCfg.HYBRID]
FAILED tests/integration/store/test_version_store.py::test_delete_item_snapshot[FwPointersCfg.ENABLED]
FAILED tests/integration/store/test_version_store.py::test_prunes_multiple_versions[FwPointersCfg.DISABLED]
FAILED tests/integration/store/test_version_store.py::test_prunes_multiple_versions[FwPointersCfg.HYBRID]
FAILED tests/integration/store/test_version_store.py::test_prunes_multiple_versions[FwPointersCfg.ENABLED]
FAILED tests/integration/store/test_version_store.py::test_prunes_doesnt_prune_snapshots[FwPointersCfg.DISABLED]
FAILED tests/integration/store/test_version_store.py::test_prunes_doesnt_prune_snapshots[FwPointersCfg.HYBRID]
FAILED tests/integration/store/test_version_store.py::test_prunes_doesnt_prune_snapshots[FwPointersCfg.ENABLED]
FAILED tests/integration/store/test_version_store.py::test_list_symbols[FwPointersCfg.DISABLED]
FAILED tests/integration/store/test_version_store.py::test_list_symbols[FwPointersCfg.HYBRID]
FAILED tests/integration/store/test_version_store.py::test_list_symbols[FwPointersCfg.ENABLED]
FAILED tests/integration/store/test_version_store.py::test_list_symbols_regex[FwPointersCfg.DISABLED]
FAILED tests/integration/store/test_version_store.py::test_list_symbols_regex[FwPointersCfg.HYBRID]
FAILED tests/integration/store/test_version_store.py::test_list_symbols_regex[FwPointersCfg.ENABLED]
FAILED tests/integration/store/test_version_store.py::test_list_symbols_newer_version_with_lower_id[FwPointersCfg.DISABLED]
FAILED tests/integration/store/test_version_store.py::test_list_symbols_newer_version_with_lower_id[FwPointersCfg.HYBRID]
FAILED tests/integration/store/test_version_store.py::test_list_symbols_newer_version_with_lower_id[FwPointersCfg.ENABLED]
FAILED tests/integration/store/test_version_store.py::test_list_symbols_write_snapshot_write_delete[FwPointersCfg.DISABLED]
FAILED tests/integration/store/test_version_store.py::test_list_symbols_write_snapshot_write_delete[FwPointersCfg.HYBRID]
FAILED tests/integration/store/test_version_store.py::test_list_symbols_write_snapshot_write_delete[FwPointersCfg.ENABLED]
FAILED tests/integration/store/test_version_store.py::test_list_symbols_delete_write[FwPointersCfg.DISABLED]
FAILED tests/integration/store/test_version_store.py::test_list_symbols_delete_write[FwPointersCfg.HYBRID]
FAILED tests/integration/store/test_version_store.py::test_list_symbols_delete_write[FwPointersCfg.ENABLED]
FAILED tests/integration/store/test_version_store.py::test_write_metadata_new_symbol[FwPointersCfg.DISABLED]
FAILED tests/integration/store/test_version_store.py::test_write_metadata_new_symbol[FwPointersCfg.HYBRID]
FAILED tests/integration/store/test_version_store.py::test_write_metadata_new_symbol[FwPointersCfg.ENABLED]
FAILED tests/integration/store/test_version_store.py::test_write_metadata_purge_previous_versions[FwPointersCfg.DISABLED]
FAILED tests/integration/store/test_version_store.py::test_write_metadata_purge_previous_versions[FwPointersCfg.HYBRID]
FAILED tests/integration/store/test_version_store.py::test_write_metadata_purge_previous_versions[FwPointersCfg.ENABLED]
FAILED tests/integration/store/test_version_store.py::test_write_metadata_delete_symbol[FwPointersCfg.DISABLED]
FAILED tests/integration/store/test_version_store.py::test_write_metadata_delete_symbol[FwPointersCfg.HYBRID]
FAILED tests/integration/store/test_version_store.py::test_write_metadata_delete_symbol[FwPointersCfg.ENABLED]
FAILED tests/integration/store/test_version_store.py::test_restore_version_snap_delete_symbol_restore[FwPointersCfg.DISABLED]
FAILED tests/integration/store/test_version_store.py::test_restore_version_snap_delete_symbol_restore[FwPointersCfg.HYBRID]
FAILED tests/integration/store/test_version_store.py::test_restore_version_snap_delete_symbol_restore[FwPointersCfg.ENABLED]
FAILED tests/integration/store/test_version_store.py::test_restore_from_version_with_deleted_symbol[FwPointersCfg.DISABLED]
FAILED tests/integration/store/test_version_store.py::test_restore_from_version_with_deleted_symbol[FwPointersCfg.HYBRID]
FAILED tests/integration/store/test_version_store.py::test_restore_from_version_with_deleted_symbol[FwPointersCfg.ENABLED]
FAILED tests/integration/store/test_version_store.py::test_snapshot_list_versions_after_delete[FwPointersCfg.DISABLED]
FAILED tests/integration/store/test_version_store.py::test_snapshot_list_versions_after_delete[FwPointersCfg.HYBRID]
FAILED tests/integration/store/test_version_store.py::test_snapshot_list_versions_after_delete[FwPointersCfg.ENABLED]
FAILED tests/integration/store/test_version_store.py::test_write_non_serializable_pickling_default[FwPointersCfg.DISABLED]
FAILED tests/integration/store/test_version_store.py::test_write_non_serializable_pickling_default[FwPointersCfg.HYBRID]
FAILED tests/integration/store/test_version_store.py::test_write_non_serializable_pickling_default[FwPointersCfg.ENABLED]
FAILED tests/integration/store/test_version_store.py::test_write_strict_no_daterange[FwPointersCfg.DISABLED]
FAILED tests/integration/store/test_version_store.py::test_write_strict_no_daterange[FwPointersCfg.HYBRID]
FAILED tests/integration/store/test_version_store.py::test_write_strict_no_daterange[FwPointersCfg.ENABLED]
FAILED tests/integration/store/test_version_store.py::test_write_df_with_objects_in_index
FAILED tests/integration/store/test_version_store.py::test_write_series_with_objects_in_index
FAILED tests/integration/store/test_version_store.py::test_write_series_with_some_objects[input_series0]
FAILED tests/integration/store/test_version_store.py::test_write_series_with_some_objects[input_series1]
FAILED tests/integration/store/test_version_store.py::test_fwpointer_enabled_write_delete_keep_version_append
FAILED tests/integration/store/test_version_store.py::test_version_arctic_version
FAILED tests/integration/store/test_version_store.py::test_prune_crossref_fwpointer_configs[FwPointersCfg.DISABLED-FwPointersCfg.HYBRID]
FAILED tests/integration/store/test_version_store.py::test_prune_crossref_fwpointer_configs[FwPointersCfg.DISABLED-FwPointersCfg.ENABLED]
FAILED tests/integration/store/test_version_store.py::test_prune_crossref_fwpointer_configs[FwPointersCfg.HYBRID-FwPointersCfg.DISABLED]
FAILED tests/integration/store/test_version_store.py::test_prune_crossref_fwpointer_configs[FwPointersCfg.HYBRID-FwPointersCfg.ENABLED]
FAILED tests/integration/store/test_version_store.py::test_prune_crossref_fwpointer_configs[FwPointersCfg.ENABLED-FwPointersCfg.HYBRID]
FAILED tests/integration/store/test_version_store.py::test_prune_crossref_fwpointer_configs[FwPointersCfg.ENABLED-FwPointersCfg.DISABLED]
FAILED tests/integration/store/test_version_store_audit.py::test_write_after_delete
FAILED tests/integration/tickstore/test_toplevel.py::test_should_return_data_when_date_range_falls_in_a_single_underlying_library
FAILED tests/integration/tickstore/test_toplevel.py::test_should_return_data_when_date_range_spans_libraries
FAILED tests/integration/tickstore/test_toplevel.py::test_should_return_data_when_date_range_spans_libraries_even_if_one_returns_nothing
FAILED tests/integration/tickstore/test_toplevel.py::test_should_add_underlying_library_where_another_library_exists_in_a_non_overlapping_daterange
FAILED tests/integration/tickstore/test_toplevel.py::test_should_write_top_level_with_list_of_dicts
FAILED tests/integration/tickstore/test_toplevel.py::test_should_write_top_level_with_correct_timezone
FAILED tests/integration/tickstore/test_ts_read.py::test_date_range[tickstore]
FAILED tests/integration/tickstore/test_ts_read.py::test_date_range_end_not_in_range[tickstore]
FAILED tests/integration/tickstore/test_ts_read.py::test_date_range_no_bounds[tickstore]
FAILED tests/unit/store/test_version_store_audit.py::test_ArcticTransaction_detects_concurrent_writes
FAILED tests/unit/tickstore/test_tickstore.py::test_mongo_date_range_query - ...
FAILED tests/unit/tickstore/test_tickstore.py::test_tickstore_to_bucket_with_image
FAILED tests/unit/tickstore/test_tickstore.py::test_tickstore_pandas_to_bucket_image


## Pull Request `travis` Test Results

We expect `travis` to fail, so it is the delta improvement that is important.

### [PR #881](https://travis-ci.org/github/man-group/arctic/builds/754296999) (before) vs. PR [#883](https://travis-ci.org/github/man-group/arctic/builds/754792688) (after)

### Python 2.7:
* PR #881:job [#2416.1 - PASSED](https://travis-ci.org/github/man-group/arctic/jobs/754297000)

|    Status |  before |   after |   delta |
|----------:|--------:|--------:|--------:|
|    failed |       0 |       0 |       0 |
|    passed |    1317 |    1317 |       0 |
|   skipped |       3 |       3 |       0 |
|   xfailed |       6 |       6 |       0 |
|   xpassed |      13 |      13 |       0 |
|  warnings |      41 |      41 |       0 |
| test time | 1301.89 | 1375.97 |     ~74 |


#### Python 3.6:
* PR #881:job [#2416.2 - FAILED](https://travis-ci.org/github/man-group/arctic/jobs/754297001) 

|    Status |  before |   after |   delta |
|----------:|--------:|--------:|--------:|
|    failed |      61 |       7 |     -54 |
|    passed |    1255 |    1309 |     +46 |
|   skipped |       3 |       3 |       0 |
|   xfailed |      19 |      19 |       0 |
|   xpassed |       1 |       1 |       0 |
|  warnings |   60848 |   60747 |      -1 |
| test time | 0:22:02 | 0:22:21 | +0:0:19 |

##### dev36 travis log
```shell
=========================== short test summary info ============================
FAILED tests/integration/store/test_pandas_store.py::test_save_read_pandas_series_with_unicode_index_name
FAILED tests/integration/store/test_pandas_store.py::test_save_read_pandas_dataframe_with_unicode_index_name
FAILED tests/integration/tickstore/test_toplevel.py::test_should_return_data_when_date_range_falls_in_a_single_underlying_library
FAILED tests/integration/tickstore/test_toplevel.py::test_should_return_data_when_date_range_spans_libraries_even_if_one_returns_nothing
FAILED tests/integration/tickstore/test_toplevel.py::test_should_write_top_level_with_list_of_dicts
FAILED tests/integration/tickstore/test_toplevel.py::test_should_write_top_level_with_correct_timezone
FAILED tests/unit/store/test_version_store_audit.py::test_ArcticTransaction_detects_concurrent_writes
= 7 failed, 1309 passed, 3 skipped, 19 xfailed, 1 xpassed, 60747 warnings in 1341.21s (0:22:21) =
The command "python setup.py test --pytest-args=-v" exited with 1.
1.24s$ pycodestyle arctic
The command "pycodestyle arctic" exited with 0.
```

#### Python 3.7:
* PR #881:job [#2416.3 - ERRORED](https://travis-ci.org/github/man-group/arctic/jobs/754297000) 

```shell
File "/home/travis/build/man-group/arctic/arctic/store/_pandas_ndarray_store.py", line 6, in <module>
    from pandas import DataFrame, Series, Panel

ImportError: Error importing plugin "arctic.fixtures.arctic": cannot import name 'Panel' from 'pandas'
```

