
tests/integration/chunkstore/test_chunkstore.py::test_overwrite_series [31mFAILED[0m[31m [  6%][0m
tests/integration/chunkstore/test_chunkstore.py::test_overwrite_series_monthly [32mPASSED[0m[31m [  6%][0m2021-01-13 15:23:25,206 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping

tests/integration/chunkstore/test_chunkstore.py::test_unnamed_colums [32mPASSED[0m[31m [  7%][0m
tests/integration/chunkstore/test_chunkstore.py::test_quarterly_data 2021-01-13 15:24:09,559 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
2021-01-13 15:24:09,650 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
[31mFAILED[0m[31m [  8%][0m
tests/integration/chunkstore/test_chunkstore.py::test_list_symbols [32mPASSED[0m[31m [  8%][0m2021-01-13 15:24:14,701 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping

tests/integration/chunkstore/test_fixes.py::test_date_interval [31mFAILED[0m[31m    [  9%][0m
tests/integration/chunkstore/test_fixes.py::test_rewrite [32mPASSED[0m[31m          [  9%][0m2021-01-13 15:24:38,763 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping

tests/integration/chunkstore/test_fixes.py::test_missing_cols [31mFAILED[0m[31m     [  9%][0m
tests/integration/chunkstore/test_fixes.py::test_column_copy [32mPASSED[0m[31m      [  9%][0m2021-01-13 15:24:41,929 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping

tests/integration/store/test_pandas_store.py::test_save_read_pandas_series_with_unicode_index_name 2021-01-13 15:28:42,565 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
[31mFAILED[0m[31m [ 25%][0m
tests/integration/store/test_pandas_store.py::test_save_read_pandas_dataframe_with_multiindex [32mPASSED[0m[31m [ 25%][0m2021-01-13 15:28:43,579 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping

tests/integration/store/test_pandas_store.py::test_save_read_pandas_dataframe_with_unicode_index_name [31mFAILED[0m[31m [ 25%][0m
tests/integration/store/test_pandas_store.py::test_cant_write_pandas_series_with_tuple_values [32mPASSED[0m[31m [ 25%][0m2021-01-13 15:28:46,494 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping

tests/integration/store/test_pandas_store.py::test_daterange_large_DataFrame [31mFAILED[0m[31m [ 33%][0m
tests/integration/store/test_pandas_store.py::test_daterange_large_DataFrame_middle [31mFAILED[0m[31m [ 33%][0m
tests/integration/store/test_pandas_store.py::test_daterange[df0-assert_frame_equal] [31mFAILED[0m[31m [ 33%][0m
tests/integration/store/test_pandas_store.py::test_daterange[df1-assert_series_equal] [31mFAILED[0m[31m [ 33%][0m
tests/integration/store/test_pandas_store.py::test_daterange_append [31mFAILED[0m[31m [ 33%][0m
tests/integration/store/test_pandas_store.py::test_daterange_single_chunk [32mPASSED[0m[31m [ 33%][0m2021-01-13 15:30:30,416 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping

tests/integration/store/test_version_store.py::test_write_metadata[FwPointersCfg.DISABLED] [31mFAILED[0m[31m [ 43%][0m
tests/integration/store/test_version_store.py::test_write_metadata[FwPointersCfg.HYBRID] 2021-01-13 15:33:03,618 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
[31mFAILED[0m[31m [ 43%][0m
tests/integration/store/test_version_store.py::test_write_metadata[FwPointersCfg.ENABLED] [31mFAILED[0m[31m [ 43%][0m
tests/integration/store/test_version_store.py::test_write_metadata_followed_by_append[FwPointersCfg.DISABLED] [31mFAILED[0m[31m [ 43%][0m
tests/integration/store/test_version_store.py::test_write_metadata_followed_by_append[FwPointersCfg.HYBRID] [31mFAILED[0m[31m [ 44%][0m
tests/integration/store/test_version_store.py::test_write_metadata_followed_by_append[FwPointersCfg.ENABLED] 2021-01-13 15:33:13,981 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
2021-01-13 15:33:13,982 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
2021-01-13 15:33:13,982 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
2021-01-13 15:33:13,982 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
[31mFAILED[0m[31m [ 44%][0m
tests/integration/store/test_version_store.py::test_write_metadata_new_symbol[FwPointersCfg.DISABLED] [32mPASSED[0m[31m [ 44%][0m2021-01-13 15:33:14,992 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping

tests/integration/store/test_version_store.py::test_write_metadata_purge_previous_versions[FwPointersCfg.DISABLED] [31mFAILED[0m[31m [ 44%][0m
tests/integration/store/test_version_store.py::test_write_metadata_purge_previous_versions[FwPointersCfg.HYBRID] [31mFAILED[0m[31m [ 44%][0m
tests/integration/store/test_version_store.py::test_write_metadata_purge_previous_versions[FwPointersCfg.ENABLED] [31mFAILED[0m[31m [ 44%][0m
tests/integration/store/test_version_store.py::test_write_metadata_delete_symbol[FwPointersCfg.DISABLED] 2021-01-13 15:33:29,924 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
2021-01-13 15:33:29,925 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
2021-01-13 15:33:29,925 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
2021-01-13 15:33:29,925 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
[31mFAILED[0m[31m [ 44%][0m
tests/integration/store/test_version_store.py::test_write_metadata_delete_symbol[FwPointersCfg.HYBRID] [31mFAILED[0m[31m [ 44%][0m
tests/integration/store/test_version_store.py::test_write_metadata_delete_symbol[FwPointersCfg.ENABLED] [31mFAILED[0m[31m [ 45%][0m
tests/integration/store/test_version_store.py::test_write_metadata_snapshots[FwPointersCfg.DISABLED] [31mFAILED[0m[31m [ 45%][0m
tests/integration/store/test_version_store.py::test_write_metadata_snapshots[FwPointersCfg.HYBRID] 2021-01-13 15:33:34,236 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
2021-01-13 15:33:34,236 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
2021-01-13 15:33:34,237 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
2021-01-13 15:33:34,237 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
[31mFAILED[0m[31m [ 45%][0m
tests/integration/store/test_version_store.py::test_write_metadata_snapshots[FwPointersCfg.ENABLED] [31mFAILED[0m[31m [ 45%][0m
tests/integration/store/test_version_store.py::test_restore_version[FwPointersCfg.DISABLED] [31mFAILED[0m[31m [ 45%][0m
tests/integration/store/test_version_store.py::test_restore_version[FwPointersCfg.HYBRID] [31mFAILED[0m[31m [ 45%][0m
tests/integration/store/test_version_store.py::test_restore_version[FwPointersCfg.ENABLED] 2021-01-13 15:33:38,512 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
2021-01-13 15:33:38,513 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
2021-01-13 15:33:38,513 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
2021-01-13 15:33:38,513 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
[31mFAILED[0m[31m [ 45%][0m
tests/integration/store/test_version_store.py::test_restore_version_followed_by_append[FwPointersCfg.DISABLED] [32mPASSED[0m[31m [ 45%][0m2021-01-13 15:33:41,564 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping

tests/integration/store/test_version_store.py::test_restore_version_followed_by_append[FwPointersCfg.HYBRID] [32mPASSED[0m[31m [ 45%][0m2021-01-13 15:33:44,563 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping

tests/integration/store/test_version_store.py::test_restore_version_followed_by_append[FwPointersCfg.ENABLED] [32mPASSED[0m[31m [ 45%][0m2021-01-13 15:33:47,531 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping

tests/integration/store/test_version_store.py::test_restore_version_purging_previous_versions[FwPointersCfg.DISABLED] [31mFAILED[0m[31m [ 45%][0m
tests/integration/store/test_version_store.py::test_restore_version_purging_previous_versions[FwPointersCfg.HYBRID] [31mFAILED[0m[31m [ 45%][0m
tests/integration/store/test_version_store.py::test_restore_version_purging_previous_versions[FwPointersCfg.ENABLED] [31mFAILED[0m[31m [ 45%][0m
tests/integration/store/test_version_store.py::test_restore_version_non_existent_version[FwPointersCfg.DISABLED] [31mFAILED[0m[31m [ 46%][0m
tests/integration/store/test_version_store.py::test_restore_version_non_existent_version[FwPointersCfg.HYBRID] 2021-01-13 15:33:58,752 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
2021-01-13 15:33:58,753 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
2021-01-13 15:33:58,754 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
2021-01-13 15:33:58,754 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
2021-01-13 15:33:58,754 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
[31mFAILED[0m[31m [ 46%][0m
tests/integration/store/test_version_store.py::test_restore_version_non_existent_version[FwPointersCfg.ENABLED] [31mFAILED[0m[31m [ 46%][0m
tests/integration/store/test_version_store.py::test_restore_version_which_updated_only_metadata[FwPointersCfg.DISABLED] [31mFAILED[0m[31m [ 46%][0m
tests/integration/store/test_version_store.py::test_restore_version_which_updated_only_metadata[FwPointersCfg.HYBRID] [31mFAILED[0m[31m [ 46%][0m
tests/integration/store/test_version_store.py::test_restore_version_which_updated_only_metadata[FwPointersCfg.ENABLED] [31mFAILED[0m[31m [ 46%][0m
tests/integration/store/test_version_store.py::test_restore_version_then_snapshot[FwPointersCfg.DISABLED] [31mFAILED[0m[31m [ 46%][0m
tests/integration/store/test_version_store.py::test_restore_version_then_snapshot[FwPointersCfg.HYBRID] [31mFAILED[0m[31m [ 46%][0m
tests/integration/store/test_version_store.py::test_restore_version_then_snapshot[FwPointersCfg.ENABLED] 2021-01-13 15:34:06,213 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
2021-01-13 15:34:06,214 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
2021-01-13 15:34:06,214 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
[31mFAILED[0m[31m [ 46%][0m
tests/integration/store/test_version_store.py::test_restore_version_latest_snapshot_noop[FwPointersCfg.DISABLED] [31mFAILED[0m[31m [ 46%][0m
tests/integration/store/test_version_store.py::test_restore_version_latest_snapshot_noop[FwPointersCfg.HYBRID] [31mFAILED[0m[31m [ 46%][0m
tests/integration/store/test_version_store.py::test_restore_version_latest_snapshot_noop[FwPointersCfg.ENABLED] [31mFAILED[0m[31m [ 46%][0m
tests/integration/store/test_version_store.py::test_restore_version_latest_version_noop[FwPointersCfg.DISABLED] [31mFAILED[0m[31m [ 46%][0m
tests/integration/store/test_version_store.py::test_restore_version_latest_version_noop[FwPointersCfg.HYBRID] 2021-01-13 15:34:11,403 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
2021-01-13 15:34:11,403 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
2021-01-13 15:34:11,403 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
2021-01-13 15:34:11,403 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
2021-01-13 15:34:11,404 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
[31mFAILED[0m[31m [ 46%][0m
tests/integration/store/test_version_store.py::test_restore_version_latest_version_noop[FwPointersCfg.ENABLED] [31mFAILED[0m[31m [ 47%][0m
tests/integration/store/test_version_store.py::test_restore_version_snap_delete_symbol_restore[FwPointersCfg.DISABLED] [31mFAILED[0m[31m [ 47%][0m
tests/integration/store/test_version_store.py::test_restore_version_snap_delete_symbol_restore[FwPointersCfg.HYBRID] [31mFAILED[0m[31m [ 47%][0m
tests/integration/store/test_version_store.py::test_restore_version_snap_delete_symbol_restore[FwPointersCfg.ENABLED] 2021-01-13 15:34:15,683 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
2021-01-13 15:34:15,683 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
2021-01-13 15:34:15,684 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
2021-01-13 15:34:15,684 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
[31mFAILED[0m[31m [ 47%][0m
tests/integration/store/test_version_store.py::test_restore_from_version_with_deleted_symbol[FwPointersCfg.DISABLED] [32mPASSED[0m[31m [ 47%][0m2021-01-13 15:34:16,686 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping

tests/integration/store/test_version_store.py::test_can_write_tz_aware_data_df[FwPointersCfg.DISABLED] [31mFAILED[0m[31m [ 50%][0m
tests/integration/store/test_version_store.py::test_can_write_tz_aware_data_df[FwPointersCfg.HYBRID] [31mFAILED[0m[31m [ 50%][0m
tests/integration/store/test_version_store.py::test_can_write_tz_aware_data_df[FwPointersCfg.ENABLED] [31mFAILED[0m[31m [ 50%][0m
tests/integration/store/test_version_store.py::test_can_write_tz_aware_data_series[FwPointersCfg.DISABLED] 2021-01-13 15:34:54,218 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
2021-01-13 15:34:54,219 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
2021-01-13 15:34:54,219 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
2021-01-13 15:34:54,219 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
[31mFAILED[0m[31m [ 50%][0m
tests/integration/store/test_version_store.py::test_can_write_tz_aware_data_series[FwPointersCfg.HYBRID] [31mFAILED[0m[31m [ 50%][0m
tests/integration/store/test_version_store.py::test_can_write_tz_aware_data_series[FwPointersCfg.ENABLED] [31mFAILED[0m[31m [ 50%][0m
tests/integration/store/test_version_store.py::test_fwpointers_mixed_scenarios[FwPointersCfg.DISABLED-FwPointersCfg.DISABLED-FwPointersCfg.DISABLED-FwPointersCfg.DISABLED] [32mPASSED[0m[31m [ 50%][0m2021-01-13 15:34:57,304 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping

tests/integration/tickstore/test_toplevel.py::test_should_return_data_when_date_range_falls_in_a_single_underlying_library [31mFAILED[0m[31m [ 54%][0m
tests/integration/tickstore/test_toplevel.py::test_should_return_data_when_date_range_spans_libraries [32mPASSED[0m[31m [ 54%][0m2021-01-13 15:36:43,453 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping

tests/integration/tickstore/test_toplevel.py::test_should_write_top_level_with_list_of_dicts [31mFAILED[0m[31m [ 55%][0m
tests/integration/tickstore/test_toplevel.py::test_should_write_top_level_with_correct_timezone [31mFAILED[0m[31m [ 55%][0m
tests/integration/tickstore/test_toplevel.py::test_min_max_date [32mPASSED[0m[31m   [ 55%][0m2021-01-13 15:36:55,849 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping

===============================================================================
=================================== FAILURES ===================================
[31m[1m____________________________ test_overwrite_series _____________________________[0m

chunkstore_lib = <ChunkStore at 0x7f84f56b62e8>
    <ArcticLibrary at 0x7f84f56b6f98, arctic_test.TEST>
        <Arctic at 0x7f84f56b6e10, connected to MongoClient(host=['127.67.249.105:29765'], document_class=dict, tz_aware=False, connect=True)>

    def test_overwrite_series(chunkstore_lib):
        s = pd.Series([1], index=pd.date_range('2016-01-01',
                                               '2016-01-01',
                                               name='date'),
                      name='vals')
    
        chunkstore_lib.write('test', s)
        chunkstore_lib.write('test', s + 1)
>       assert_series_equal(chunkstore_lib.read('test'), s + 1)
[1m[31mE       AssertionError: (None, <Day>)[0m

[1m[31mtests/integration/chunkstore/test_chunkstore.py[0m:716: AssertionError

===============================================================================

chunkstore_lib = <ChunkStore at 0x7f84f54430b8>
    <ArcticLibrary at 0x7f84f5445160, arctic_test.TEST>
        <Arctic at 0x7f84f5466710, connected to MongoClient(host=['127.67.249.105:1069'], document_class=dict, tz_aware=False, connect=True)>

    def test_quarterly_data(chunkstore_lib):
        df = DataFrame(data={'data': np.random.randint(0, 100, size=366)},
                       index=pd.date_range('2016-01-01', '2016-12-31'))
        df.index.name = 'date'
    
        chunkstore_lib.write('quarterly', df, chunk_size='Q')
>       assert_frame_equal(df, chunkstore_lib.read('quarterly'))
[1m[31mE       AssertionError: (<Day>, None)[0m

[1m[31mtests/integration/chunkstore/test_chunkstore.py[0m:1037: AssertionError

===============================================================================

chunkstore_lib = <ChunkStore at 0x7f84f4814470>
    <ArcticLibrary at 0x7f84f48306d8, arctic_test.TEST>
        <Arctic at 0x7f84f4814f28, connected to MongoClient(host=['127.67.249.105:7530'], document_class=dict, tz_aware=False, connect=True)>

    def test_date_interval(chunkstore_lib):
        date_range = pd.date_range(start=dt(2017, 5, 1), periods=8, freq='D')
    
        df = DataFrame(data={'data': range(8)},
                       index=DatetimeIndex(date_range, name='date'))
    
        # test with index
        chunkstore_lib.write('test', df, chunk_size='D')
    
        ret = chunkstore_lib.read('test', chunk_range=DateRange(dt(2017, 5, 2), dt(2017, 5, 5), CLOSED_OPEN))
>       assert_frame_equal(ret, df[1:4])
[1m[31mE       AssertionError: (None, <Day>)[0m

[1m[31mtests/integration/chunkstore/test_fixes.py[0m:75: AssertionError

===============================================================================

    def test_missing_cols(chunkstore_lib):
        index = DatetimeIndex(pd.date_range('2019-01-01', periods=3, freq='D'), name='date')
        index2 = DatetimeIndex(pd.date_range('2019-01-04', periods=3, freq='D'), name='date')
        expected_index = DatetimeIndex(pd.date_range('2019-01-01', periods=6, freq='D'), name='date')
        expected_df = DataFrame({'A': [1, 2, 3, 40, 50, 60], 'B': [5.0,6.0,7.0, np.nan, np.nan, np.nan]}, index=expected_index)
    
        df = pd.DataFrame({'A': [1, 2, 3], 'B': [5,6,7]}, index=index)
        chunkstore_lib.write('test', df, chunk_size='D')
    
        df = pd.DataFrame({'A': [40, 50, 60]}, index=index2)
        chunkstore_lib.append('test', df, chunk_size='D')
    
    
>       assert_frame_equal(chunkstore_lib.read('test'), expected_df)
[1m[31mE       AssertionError: (None, <Day>)[0m

[1m[31mtests/integration/chunkstore/test_fixes.py[0m:166: AssertionError

===============================================================================

    def test_save_read_pandas_series_with_unicode_index_name(library):
        df = Series(data=['A', 'BC', 'DEF'],
                    index=MultiIndex.from_tuples([(np.datetime64(dt(2013, 1, 1)),),
                                                  (np.datetime64(dt(2013, 1, 2)),),
                                                  (np.datetime64(dt(2013, 1, 3)),)], names=[u'DATETIME']))
        library.write('pandas', df)
>       saved_df = library.read('pandas').data

===============================================================================

[1m[31mpandas/_libs/tslibs/timezones.pyx[0m:114: TypeError

===============================================================================

library = <VersionStore at 0x7f84e47c3a58>
    <ArcticLibrary at 0x7f84e47c3b38, arctic_test.TEST>
        <Arctic at 0x7f84f4042fd0, connected to MongoClient(host=['127.67.249.105:25202'], document_class=dict, tz_aware=False, connect=True)>

    def test_save_read_pandas_dataframe_with_unicode_index_name(library):
        df = DataFrame(data=['A', 'BC', 'DEF'],
                       index=MultiIndex.from_tuples([(np.datetime64(dt(2013, 1, 1)),),
                                                     (np.datetime64(dt(2013, 1, 2)),),
                                                     (np.datetime64(dt(2013, 1, 3)),)], names=[u'DATETIME']))
        library.write('pandas', df)
>       saved_df = library.read('pandas').data

[1m[31mtests/integration/store/test_pandas_store.py[0m:102: 

===============================================================================

library = <VersionStore at 0x7f84e7649f28>
    <ArcticLibrary at 0x7f84e47a8550, arctic_test.TEST>
        <Arctic at 0x7f84f415b5c0, connected to MongoClient(host=['127.67.249.105:4954'], document_class=dict, tz_aware=False, connect=True)>

    def test_daterange_large_DataFrame(library):
        df = DataFrame(index=date_range(dt(2001, 1, 1), freq='S', periods=30 * 1024),
                       data=np.tile(np.arange(30 * 1024), 100).reshape((-1, 100)))
        df.columns = [str(c) for c in df.columns]
        library.write('MYARR', df)
        # assert saved
        saved_arr = library.read('MYARR').data
>       assert_frame_equal(df, saved_arr, check_names=False)
[1m[31mE       AssertionError: (<Second>, None)[0m

[1m[31mtests/integration/store/test_pandas_store.py[0m:805: AssertionError
===============================================================================


library = <VersionStore at 0x7f84e76d15c0>
    <ArcticLibrary at 0x7f84f4045908, arctic_test.TEST>
        <Arctic at 0x7f84f5f80be0, connected to MongoClient(host=['127.67.249.105:20876'], document_class=dict, tz_aware=False, connect=True)>

    def test_daterange_large_DataFrame_middle(library):
        df = DataFrame(index=date_range(dt(2001, 1, 1), freq='S', periods=30 * 1024),
                       data=np.tile(np.arange(30 * 1024), 100).reshape((-1, 100)))
        df.columns = [str(c) for c in df.columns]
        library.write('MYARR', df)
        # middle
        start = 100
        for end in np.arange(200, 30000, 1000):
            result = library.read('MYARR', date_range=DateRange(df.index[start], df.index[end])).data
>           assert_frame_equal(df[df.index[start]:df.index[end]], result, check_names=False)
[1m[31mE           AssertionError: (<Second>, None)[0m

[1m[31mtests/integration/store/test_pandas_store.py[0m:841: AssertionError

===============================================================================


===============================================================================

assert_equal = <function assert_frame_equal at 0x7f84fc5fd730>

    @pytest.mark.parametrize("df,assert_equal", [
        (DataFrame(index=date_range(dt(2001, 1, 1), freq='D', periods=30000),
                   data=list(range(30000)), columns=['A']), assert_frame_equal),
        (Series(index=date_range(dt(2001, 1, 1), freq='D', periods=30000),
                data=range(30000)), assert_series_equal),
    ])
    def test_daterange(library, df, assert_equal):
        df.index.name = 'idx'
        df.name = 'FOO'
        library.write('MYARR', df)
        # whole array
        saved_arr = library.read('MYARR').data
>       assert_equal(df, saved_arr)
[1m[31mE       AssertionError: (<Day>, None)[0m

[1m[31mtests/integration/store/test_pandas_store.py[0m:862: AssertionError

===============================================================================

    @pytest.mark.parametrize("df,assert_equal", [
        (DataFrame(index=date_range(dt(2001, 1, 1), freq='D', periods=30000),
                   data=list(range(30000)), columns=['A']), assert_frame_equal),
        (Series(index=date_range(dt(2001, 1, 1), freq='D', periods=30000),
                data=range(30000)), assert_series_equal),
    ])
    def test_daterange(library, df, assert_equal):
        df.index.name = 'idx'
        df.name = 'FOO'
        library.write('MYARR', df)
        # whole array
        saved_arr = library.read('MYARR').data
>       assert_equal(df, saved_arr)
[1m[31mE       AssertionError: (<Day>, None)[0m

[1m[31mtests/integration/store/test_pandas_store.py[0m:862: AssertionError

===============================================================================

    def test_daterange_append(library):
        df = DataFrame(index=date_range(dt(2001, 1, 1), freq='S', periods=30 * 1024),
                       data=np.tile(np.arange(30 * 1024), 100).reshape((-1, 100)))
        df.columns = [str(c) for c in df.columns]
        df.index.name = 'idx'
        library.write('MYARR', df)
        # assert saved
        saved_arr = library.read('MYARR').data
>       assert_frame_equal(df, saved_arr, check_names=False)
[1m[31mE       AssertionError: (<Second>, None)[0m

[1m[31mtests/integration/store/test_pandas_store.py[0m:888: AssertionError

===============================================================================

                v = library.read(symbol)
>               assert_frame_equal(v.data, mydf_b)
[1m[31mE               AssertionError: (None, <Second>)[0m

[1m[31mtests/integration/store/test_version_store.py[0m:1161: AssertionError

===============================================================================

    @pytest.mark.parametrize('fw_pointers_cfg', [FwPointersCfg.DISABLED, FwPointersCfg.HYBRID, FwPointersCfg.ENABLED])
    def test_write_metadata(library, fw_pointers_cfg):
        with FwPointersCtx(fw_pointers_cfg):
            symbol = 'FTL'
            mydf_a, mydf_b = _rnd_df(10, 5), _rnd_df(10, 5)
            with patch('arctic.arctic.logger.info') as info:
                library.write(symbol, data=mydf_a, metadata={'field_a': 1})  # creates version 1
                library.write(symbol, data=mydf_b, metadata={'field_a': 2})  # creates version 2
                library.write_metadata(symbol, metadata={'field_b': 1})  # creates version 3 (only metadata)
    
                v_doc_2 = library._versions.find_one({'symbol': symbol, 'version': 2})
                v_doc_3 = library._versions.find_one({'symbol': symbol, 'version': 3})
                assert get_fwptr_config(v_doc_2) is fw_pointers_cfg
                assert v_doc_2.get(FW_POINTERS_REFS_KEY) == v_doc_3.get(FW_POINTERS_REFS_KEY)
    
                v = library.read(symbol)
>               assert_frame_equal(v.data, mydf_b)
[1m[31mE               AssertionError: (None, <Second>)[0m

[1m[31mtests/integration/store/test_version_store.py[0m:1161: AssertionError

===============================================================================

    @pytest.mark.parametrize('fw_pointers_cfg', [FwPointersCfg.DISABLED, FwPointersCfg.HYBRID, FwPointersCfg.ENABLED])
    def test_write_metadata(library, fw_pointers_cfg):
        with FwPointersCtx(fw_pointers_cfg):
            symbol = 'FTL'
            mydf_a, mydf_b = _rnd_df(10, 5), _rnd_df(10, 5)
            with patch('arctic.arctic.logger.info') as info:
                library.write(symbol, data=mydf_a, metadata={'field_a': 1})  # creates version 1
                library.write(symbol, data=mydf_b, metadata={'field_a': 2})  # creates version 2
                library.write_metadata(symbol, metadata={'field_b': 1})  # creates version 3 (only metadata)
    
                v_doc_2 = library._versions.find_one({'symbol': symbol, 'version': 2})
                v_doc_3 = library._versions.find_one({'symbol': symbol, 'version': 3})
                assert get_fwptr_config(v_doc_2) is fw_pointers_cfg
                assert v_doc_2.get(FW_POINTERS_REFS_KEY) == v_doc_3.get(FW_POINTERS_REFS_KEY)
    
                v = library.read(symbol)
>               assert_frame_equal(v.data, mydf_b)
[1m[31mE               AssertionError: (None, <Second>)[0m

[1m[31mtests/integration/store/test_version_store.py[0m:1161: AssertionError

===============================================================================

    @pytest.mark.parametrize('fw_pointers_cfg', [FwPointersCfg.DISABLED, FwPointersCfg.HYBRID, FwPointersCfg.ENABLED])
    def test_write_metadata_followed_by_append(library, fw_pointers_cfg):
        with FwPointersCtx(fw_pointers_cfg):
            symbol = 'FTL'
            mydf_a, mydf_b = _rnd_df(10, 5), _rnd_df(10, 5)
            with patch('arctic.arctic.logger.info') as info:
                library.write(symbol, data=mydf_a, metadata={'field_a': 1})  # creates version 1
                library.write_metadata(symbol, metadata={'field_b': 1})  # creates version 2 (only metadata)
                library.append(symbol, data=mydf_b, metadata={'field_c': 1})  # creates version 3
    
                # Trigger GC now
                time.sleep(2)
                library._prune_previous_versions(symbol, 0)
    
                v = library.read(symbol)
                assert_frame_equal(v.data, mydf_a.append(mydf_b))
                assert v.metadata == {'field_c': 1}
                assert library._read_metadata(symbol).get('version') == 3
>               assert_frame_equal(library.read(symbol, as_of=1).data, mydf_a)
[1m[31mE               AssertionError: (None, <Second>)[0m

[1m[31mtests/integration/store/test_version_store.py[0m:1185: AssertionError

===============================================================================

    @pytest.mark.parametrize('fw_pointers_cfg', [FwPointersCfg.DISABLED, FwPointersCfg.HYBRID, FwPointersCfg.ENABLED])
    def test_write_metadata_followed_by_append(library, fw_pointers_cfg):
        with FwPointersCtx(fw_pointers_cfg):
            symbol = 'FTL'
            mydf_a, mydf_b = _rnd_df(10, 5), _rnd_df(10, 5)
            with patch('arctic.arctic.logger.info') as info:
                library.write(symbol, data=mydf_a, metadata={'field_a': 1})  # creates version 1
                library.write_metadata(symbol, metadata={'field_b': 1})  # creates version 2 (only metadata)
                library.append(symbol, data=mydf_b, metadata={'field_c': 1})  # creates version 3
    
                # Trigger GC now
                time.sleep(2)
                library._prune_previous_versions(symbol, 0)
    
                v = library.read(symbol)
                assert_frame_equal(v.data, mydf_a.append(mydf_b))
                assert v.metadata == {'field_c': 1}
                assert library._read_metadata(symbol).get('version') == 3
>               assert_frame_equal(library.read(symbol, as_of=1).data, mydf_a)
[1m[31mE               AssertionError: (None, <Second>)[0m

[1m[31mtests/integration/store/test_version_store.py[0m:1185: AssertionError

===============================================================================

    @pytest.mark.parametrize('fw_pointers_cfg', [FwPointersCfg.DISABLED, FwPointersCfg.HYBRID, FwPointersCfg.ENABLED])
    def test_write_metadata_followed_by_append(library, fw_pointers_cfg):
        with FwPointersCtx(fw_pointers_cfg):
            symbol = 'FTL'
            mydf_a, mydf_b = _rnd_df(10, 5), _rnd_df(10, 5)
            with patch('arctic.arctic.logger.info') as info:
                library.write(symbol, data=mydf_a, metadata={'field_a': 1})  # creates version 1
                library.write_metadata(symbol, metadata={'field_b': 1})  # creates version 2 (only metadata)
                library.append(symbol, data=mydf_b, metadata={'field_c': 1})  # creates version 3
    
                # Trigger GC now
                time.sleep(2)
                library._prune_previous_versions(symbol, 0)
    
                v = library.read(symbol)
                assert_frame_equal(v.data, mydf_a.append(mydf_b))
                assert v.metadata == {'field_c': 1}
                assert library._read_metadata(symbol).get('version') == 3
>               assert_frame_equal(library.read(symbol, as_of=1).data, mydf_a)
[1m[31mE               AssertionError: (None, <Second>)[0m

[1m[31mtests/integration/store/test_version_store.py[0m:1185: AssertionError

===============================================================================

    @pytest.mark.parametrize('fw_pointers_cfg', [FwPointersCfg.DISABLED, FwPointersCfg.HYBRID, FwPointersCfg.ENABLED])
    def test_write_metadata_purge_previous_versions(library, fw_pointers_cfg):
        with FwPointersCtx(fw_pointers_cfg):
            symbol = 'FTL'
            mydf_a, mydf_b, mydf_c = _rnd_df(10, 5), _rnd_df(10, 5), _rnd_df(10, 5)
            with patch('arctic.arctic.logger.info') as info:
                with FwPointersCtx(fw_pointers_cfg):
                    library.write(symbol, data=mydf_a, metadata={'field_a': 1})  # creates version 1
                    library.write(symbol, data=mydf_b, metadata={'field_a': 2})  # creates version 2
                    assert library._read_metadata(symbol).get('version') == 2
                    library.write_metadata(symbol, metadata={'field_b': 1})  # creates version 3 (only metadata)
    
                    # Trigger GC now
                    library._prune_previous_versions(symbol, 0)
                    time.sleep(2)
    
                    # Assert the data
                    v = library.read(symbol)
>                   assert_frame_equal(v.data, mydf_b)
[1m[31mE                   AssertionError: (None, <Second>)[0m

[1m[31mtests/integration/store/test_version_store.py[0m:1233: AssertionError

===============================================================================

    @pytest.mark.parametrize('fw_pointers_cfg', [FwPointersCfg.DISABLED, FwPointersCfg.HYBRID, FwPointersCfg.ENABLED])
    def test_write_metadata_purge_previous_versions(library, fw_pointers_cfg):
        with FwPointersCtx(fw_pointers_cfg):
            symbol = 'FTL'
            mydf_a, mydf_b, mydf_c = _rnd_df(10, 5), _rnd_df(10, 5), _rnd_df(10, 5)
            with patch('arctic.arctic.logger.info') as info:
                with FwPointersCtx(fw_pointers_cfg):
                    library.write(symbol, data=mydf_a, metadata={'field_a': 1})  # creates version 1
                    library.write(symbol, data=mydf_b, metadata={'field_a': 2})  # creates version 2
                    assert library._read_metadata(symbol).get('version') == 2
                    library.write_metadata(symbol, metadata={'field_b': 1})  # creates version 3 (only metadata)
    
                    # Trigger GC now
                    library._prune_previous_versions(symbol, 0)
                    time.sleep(2)
    
                    # Assert the data
                    v = library.read(symbol)
>                   assert_frame_equal(v.data, mydf_b)
[1m[31mE                   AssertionError: (None, <Second>)[0m

[1m[31mtests/integration/store/test_version_store.py[0m:1233: AssertionError

===============================================================================

    @pytest.mark.parametrize('fw_pointers_cfg', [FwPointersCfg.DISABLED, FwPointersCfg.HYBRID, FwPointersCfg.ENABLED])
    def test_write_metadata_purge_previous_versions(library, fw_pointers_cfg):
        with FwPointersCtx(fw_pointers_cfg):
            symbol = 'FTL'
            mydf_a, mydf_b, mydf_c = _rnd_df(10, 5), _rnd_df(10, 5), _rnd_df(10, 5)
            with patch('arctic.arctic.logger.info') as info:
                with FwPointersCtx(fw_pointers_cfg):
                    library.write(symbol, data=mydf_a, metadata={'field_a': 1})  # creates version 1
                    library.write(symbol, data=mydf_b, metadata={'field_a': 2})  # creates version 2
                    assert library._read_metadata(symbol).get('version') == 2
                    library.write_metadata(symbol, metadata={'field_b': 1})  # creates version 3 (only metadata)
    
                    # Trigger GC now
                    library._prune_previous_versions(symbol, 0)
                    time.sleep(2)
    
                    # Assert the data
                    v = library.read(symbol)
>                   assert_frame_equal(v.data, mydf_b)
[1m[31mE                   AssertionError: (None, <Second>)[0m

[1m[31mtests/integration/store/test_version_store.py[0m:1233: AssertionError

===============================================================================

    @pytest.mark.parametrize('fw_pointers_cfg', [FwPointersCfg.DISABLED, FwPointersCfg.HYBRID, FwPointersCfg.ENABLED])
    def test_write_metadata_delete_symbol(library, fw_pointers_cfg):
        with FwPointersCtx(fw_pointers_cfg):
            symbol = 'FTL'
            mydf_a = _rnd_df(10, 5)
            mydf_b = _rnd_df(10, 5)
            with patch('arctic.arctic.logger.info') as info:
                library.write(symbol, data=mydf_a, metadata={'field_a': 1})  # creates version 1
                library.write_metadata(symbol, metadata={'field_b': 1})  # creates version 2 (only metadata)
    
                library.delete(symbol)
    
                with pytest.raises(NoDataFoundException):
                    library.read(symbol)
    
                library.write(symbol, data=mydf_b, metadata={'field_a': 1})  # creates version 1
>               assert_frame_equal(library.read(symbol).data, mydf_b)
[1m[31mE               AssertionError: (None, <Second>)[0m

[1m[31mtests/integration/store/test_version_store.py[0m:1261: AssertionError

===============================================================================

    @pytest.mark.parametrize('fw_pointers_cfg', [FwPointersCfg.DISABLED, FwPointersCfg.HYBRID, FwPointersCfg.ENABLED])
    def test_write_metadata_delete_symbol(library, fw_pointers_cfg):
        with FwPointersCtx(fw_pointers_cfg):
            symbol = 'FTL'
            mydf_a = _rnd_df(10, 5)
            mydf_b = _rnd_df(10, 5)
            with patch('arctic.arctic.logger.info') as info:
                library.write(symbol, data=mydf_a, metadata={'field_a': 1})  # creates version 1
                library.write_metadata(symbol, metadata={'field_b': 1})  # creates version 2 (only metadata)
    
                library.delete(symbol)
    
                with pytest.raises(NoDataFoundException):
                    library.read(symbol)
    
                library.write(symbol, data=mydf_b, metadata={'field_a': 1})  # creates version 1
>               assert_frame_equal(library.read(symbol).data, mydf_b)
[1m[31mE               AssertionError: (None, <Second>)[0m

[1m[31mtests/integration/store/test_version_store.py[0m:1261: AssertionError

===============================================================================

    @pytest.mark.parametrize('fw_pointers_cfg', [FwPointersCfg.DISABLED, FwPointersCfg.HYBRID, FwPointersCfg.ENABLED])
    def test_write_metadata_delete_symbol(library, fw_pointers_cfg):
        with FwPointersCtx(fw_pointers_cfg):
            symbol = 'FTL'
            mydf_a = _rnd_df(10, 5)
            mydf_b = _rnd_df(10, 5)
            with patch('arctic.arctic.logger.info') as info:
                library.write(symbol, data=mydf_a, metadata={'field_a': 1})  # creates version 1
                library.write_metadata(symbol, metadata={'field_b': 1})  # creates version 2 (only metadata)
    
                library.delete(symbol)
    
                with pytest.raises(NoDataFoundException):
                    library.read(symbol)
    
                library.write(symbol, data=mydf_b, metadata={'field_a': 1})  # creates version 1
>               assert_frame_equal(library.read(symbol).data, mydf_b)
[1m[31mE               AssertionError: (None, <Second>)[0m

[1m[31mtests/integration/store/test_version_store.py[0m:1261: AssertionError

===============================================================================

    @pytest.mark.parametrize('fw_pointers_cfg', [FwPointersCfg.DISABLED, FwPointersCfg.HYBRID, FwPointersCfg.ENABLED])
    def test_write_metadata_snapshots(library, fw_pointers_cfg):
        with FwPointersCtx(fw_pointers_cfg):
            symbol = 'FTL'
            mydf_a, mydf_b = _rnd_df(10, 5), _rnd_df(10, 5)
            with patch('arctic.arctic.logger.info') as info:
                library.write(symbol, data=mydf_a, metadata={'field_a': 1})  # creates version 1
                library.snapshot('SNAP_1')
                library.write_metadata(symbol, metadata={'field_b': 1})  # creates version 2 (only metadata)
                library.snapshot('SNAP_2')
                library.write(symbol, data=mydf_b, metadata={'field_c': 1})  # creates version 3
                library.snapshot('SNAP_3')
    
                library._prune_previous_versions(symbol, keep_mins=0)
    
                v = library.read(symbol)
>               assert_frame_equal(v.data, mydf_b)
[1m[31mE               AssertionError: (None, <Second>)[0m

[1m[31mtests/integration/store/test_version_store.py[0m:1280: AssertionError

===============================================================================

    @pytest.mark.parametrize('fw_pointers_cfg', [FwPointersCfg.DISABLED, FwPointersCfg.HYBRID, FwPointersCfg.ENABLED])
    def test_write_metadata_snapshots(library, fw_pointers_cfg):
        with FwPointersCtx(fw_pointers_cfg):
            symbol = 'FTL'
            mydf_a, mydf_b = _rnd_df(10, 5), _rnd_df(10, 5)
            with patch('arctic.arctic.logger.info') as info:
                library.write(symbol, data=mydf_a, metadata={'field_a': 1})  # creates version 1
                library.snapshot('SNAP_1')
                library.write_metadata(symbol, metadata={'field_b': 1})  # creates version 2 (only metadata)
                library.snapshot('SNAP_2')
                library.write(symbol, data=mydf_b, metadata={'field_c': 1})  # creates version 3
                library.snapshot('SNAP_3')
    
                library._prune_previous_versions(symbol, keep_mins=0)
    
                v = library.read(symbol)
>               assert_frame_equal(v.data, mydf_b)
[1m[31mE               AssertionError: (None, <Second>)[0m

[1m[31mtests/integration/store/test_version_store.py[0m:1280: AssertionError

===============================================================================

    @pytest.mark.parametrize('fw_pointers_cfg', [FwPointersCfg.DISABLED, FwPointersCfg.HYBRID, FwPointersCfg.ENABLED])
    def test_write_metadata_snapshots(library, fw_pointers_cfg):
        with FwPointersCtx(fw_pointers_cfg):
            symbol = 'FTL'
            mydf_a, mydf_b = _rnd_df(10, 5), _rnd_df(10, 5)
            with patch('arctic.arctic.logger.info') as info:
                library.write(symbol, data=mydf_a, metadata={'field_a': 1})  # creates version 1
                library.snapshot('SNAP_1')
                library.write_metadata(symbol, metadata={'field_b': 1})  # creates version 2 (only metadata)
                library.snapshot('SNAP_2')
                library.write(symbol, data=mydf_b, metadata={'field_c': 1})  # creates version 3
                library.snapshot('SNAP_3')
    
                library._prune_previous_versions(symbol, keep_mins=0)
    
                v = library.read(symbol)
>               assert_frame_equal(v.data, mydf_b)
[1m[31mE               AssertionError: (None, <Second>)[0m

[1m[31mtests/integration/store/test_version_store.py[0m:1280: AssertionError

===============================================================================

    @pytest.mark.parametrize('fw_pointers_cfg', [FwPointersCfg.DISABLED, FwPointersCfg.HYBRID, FwPointersCfg.ENABLED])
    def test_restore_version(library, fw_pointers_cfg):
        with FwPointersCtx(fw_pointers_cfg):
            symbol = 'FTL'
            mydf_a = _rnd_df(10, 5)
            mydf_b = _rnd_df(10, 5)
            with patch('arctic.arctic.logger.info') as info:
                library.write(symbol, data=mydf_a, metadata={'field_a': 1})  # creates version 1
                library.write(symbol, data=mydf_b, metadata={'field_a': 2})  # creates version 2
    
                item = library.read(symbol)
>               assert_frame_equal(item.data, mydf_b)
[1m[31mE               AssertionError: (None, <Second>)[0m

[1m[31mtests/integration/store/test_version_store.py[0m:1303: AssertionError

===============================================================================

    @pytest.mark.parametrize('fw_pointers_cfg', [FwPointersCfg.DISABLED, FwPointersCfg.HYBRID, FwPointersCfg.ENABLED])
    def test_restore_version(library, fw_pointers_cfg):
        with FwPointersCtx(fw_pointers_cfg):
            symbol = 'FTL'
            mydf_a = _rnd_df(10, 5)
            mydf_b = _rnd_df(10, 5)
            with patch('arctic.arctic.logger.info') as info:
                library.write(symbol, data=mydf_a, metadata={'field_a': 1})  # creates version 1
                library.write(symbol, data=mydf_b, metadata={'field_a': 2})  # creates version 2
    
                item = library.read(symbol)
>               assert_frame_equal(item.data, mydf_b)
[1m[31mE               AssertionError: (None, <Second>)[0m

[1m[31mtests/integration/store/test_version_store.py[0m:1303: AssertionError

===============================================================================

    @pytest.mark.parametrize('fw_pointers_cfg', [FwPointersCfg.DISABLED, FwPointersCfg.HYBRID, FwPointersCfg.ENABLED])
    def test_restore_version(library, fw_pointers_cfg):
        with FwPointersCtx(fw_pointers_cfg):
            symbol = 'FTL'
            mydf_a = _rnd_df(10, 5)
            mydf_b = _rnd_df(10, 5)
            with patch('arctic.arctic.logger.info') as info:
                library.write(symbol, data=mydf_a, metadata={'field_a': 1})  # creates version 1
                library.write(symbol, data=mydf_b, metadata={'field_a': 2})  # creates version 2
    
                item = library.read(symbol)
>               assert_frame_equal(item.data, mydf_b)
[1m[31mE               AssertionError: (None, <Second>)[0m

[1m[31mtests/integration/store/test_version_store.py[0m:1303: AssertionError

===============================================================================

    @pytest.mark.parametrize('fw_pointers_cfg', [FwPointersCfg.DISABLED, FwPointersCfg.HYBRID, FwPointersCfg.ENABLED])
    def test_restore_version_purging_previous_versions(library, fw_pointers_cfg):
        with FwPointersCtx(fw_pointers_cfg):
            symbol = 'FTL'
            mydf_a = _rnd_df(10, 5)
            mydf_b = _rnd_df(10, 5)
            with patch('arctic.arctic.logger.info') as info:
                library.write(symbol, data=mydf_a, metadata={'field_a': 1})  # creates version 1
                library.write(symbol, data=mydf_b, metadata={'field_a': 2})  # creates version 2
    
                restore_item = library.restore_version(symbol, as_of=1)  # creates version 3
                assert restore_item.version == 3
                assert restore_item.metadata == {'field_a': 1}
    
                # Trigger GC now
                library._prune_previous_versions(symbol, 0)
                time.sleep(2)
    
                # library._delete_version(symbol, 1)  # delete the original version to test further the robustness/dependency
    
                item = library.read(symbol)
>               assert_frame_equal(item.data, mydf_a)
[1m[31mE               AssertionError: (None, <Second>)[0m

[1m[31mtests/integration/store/test_version_store.py[0m:1365: AssertionError

===============================================================================

    @pytest.mark.parametrize('fw_pointers_cfg', [FwPointersCfg.DISABLED, FwPointersCfg.HYBRID, FwPointersCfg.ENABLED])
    def test_restore_version_purging_previous_versions(library, fw_pointers_cfg):
        with FwPointersCtx(fw_pointers_cfg):
            symbol = 'FTL'
            mydf_a = _rnd_df(10, 5)
            mydf_b = _rnd_df(10, 5)
            with patch('arctic.arctic.logger.info') as info:
                library.write(symbol, data=mydf_a, metadata={'field_a': 1})  # creates version 1
                library.write(symbol, data=mydf_b, metadata={'field_a': 2})  # creates version 2
    
                restore_item = library.restore_version(symbol, as_of=1)  # creates version 3
                assert restore_item.version == 3
                assert restore_item.metadata == {'field_a': 1}
    
                # Trigger GC now
                library._prune_previous_versions(symbol, 0)
                time.sleep(2)
    
                # library._delete_version(symbol, 1)  # delete the original version to test further the robustness/dependency
    
                item = library.read(symbol)
>               assert_frame_equal(item.data, mydf_a)
[1m[31mE               AssertionError: (None, <Second>)[0m

[1m[31mtests/integration/store/test_version_store.py[0m:1365: AssertionError

===============================================================================

    @pytest.mark.parametrize('fw_pointers_cfg', [FwPointersCfg.DISABLED, FwPointersCfg.HYBRID, FwPointersCfg.ENABLED])
    def test_restore_version_purging_previous_versions(library, fw_pointers_cfg):
        with FwPointersCtx(fw_pointers_cfg):
            symbol = 'FTL'
            mydf_a = _rnd_df(10, 5)
            mydf_b = _rnd_df(10, 5)
            with patch('arctic.arctic.logger.info') as info:
                library.write(symbol, data=mydf_a, metadata={'field_a': 1})  # creates version 1
                library.write(symbol, data=mydf_b, metadata={'field_a': 2})  # creates version 2
    
                restore_item = library.restore_version(symbol, as_of=1)  # creates version 3
                assert restore_item.version == 3
                assert restore_item.metadata == {'field_a': 1}
    
                # Trigger GC now
                library._prune_previous_versions(symbol, 0)
                time.sleep(2)
    
                # library._delete_version(symbol, 1)  # delete the original version to test further the robustness/dependency
    
                item = library.read(symbol)
>               assert_frame_equal(item.data, mydf_a)
[1m[31mE               AssertionError: (None, <Second>)[0m

[1m[31mtests/integration/store/test_version_store.py[0m:1365: AssertionError

===============================================================================

    @pytest.mark.parametrize('fw_pointers_cfg', [FwPointersCfg.DISABLED, FwPointersCfg.HYBRID, FwPointersCfg.ENABLED])
    def test_restore_version_non_existent_version(library, fw_pointers_cfg):
        with FwPointersCtx(fw_pointers_cfg):
            symbol = 'FTL'
            mydf_a = _rnd_df(10, 5)
            with patch('arctic.arctic.logger.info') as info:
                library.write(symbol, data=mydf_a, metadata={'field_a': 1})  # creates version 1
    
                with pytest.raises(NoDataFoundException):
                    library.restore_version(symbol, as_of=3)
    
                item = library.read(symbol)
>               assert_frame_equal(item.data, mydf_a)
[1m[31mE               AssertionError: (None, <Second>)[0m

[1m[31mtests/integration/store/test_version_store.py[0m:1382: AssertionError

===============================================================================

    @pytest.mark.parametrize('fw_pointers_cfg', [FwPointersCfg.DISABLED, FwPointersCfg.HYBRID, FwPointersCfg.ENABLED])
    def test_restore_version_non_existent_version(library, fw_pointers_cfg):
        with FwPointersCtx(fw_pointers_cfg):
            symbol = 'FTL'
            mydf_a = _rnd_df(10, 5)
            with patch('arctic.arctic.logger.info') as info:
                library.write(symbol, data=mydf_a, metadata={'field_a': 1})  # creates version 1
    
                with pytest.raises(NoDataFoundException):
                    library.restore_version(symbol, as_of=3)
    
                item = library.read(symbol)
>               assert_frame_equal(item.data, mydf_a)
[1m[31mE               AssertionError: (None, <Second>)[0m

[1m[31mtests/integration/store/test_version_store.py[0m:1382: AssertionError

===============================================================================

    @pytest.mark.parametrize('fw_pointers_cfg', [FwPointersCfg.DISABLED, FwPointersCfg.HYBRID, FwPointersCfg.ENABLED])
    def test_restore_version_non_existent_version(library, fw_pointers_cfg):
        with FwPointersCtx(fw_pointers_cfg):
            symbol = 'FTL'
            mydf_a = _rnd_df(10, 5)
            with patch('arctic.arctic.logger.info') as info:
                library.write(symbol, data=mydf_a, metadata={'field_a': 1})  # creates version 1
    
                with pytest.raises(NoDataFoundException):
                    library.restore_version(symbol, as_of=3)
    
                item = library.read(symbol)
>               assert_frame_equal(item.data, mydf_a)
[1m[31mE               AssertionError: (None, <Second>)[0m

[1m[31mtests/integration/store/test_version_store.py[0m:1382: AssertionError

===============================================================================

    @pytest.mark.parametrize('fw_pointers_cfg', [FwPointersCfg.DISABLED, FwPointersCfg.HYBRID, FwPointersCfg.ENABLED])
    def test_restore_version_which_updated_only_metadata(library, fw_pointers_cfg):
        with FwPointersCtx(fw_pointers_cfg):
            symbol = 'FTL'
            mydf_a = _rnd_df(10, 5)
            mydf_b = _rnd_df(10, 5)
            with patch('arctic.arctic.logger.info') as info:
                library.write(symbol, data=mydf_a, metadata={'field_a': 1})  # creates version 1
                library.write_metadata(symbol, metadata={'field_b': 1})  # creates version 2
                library.write(symbol, data=mydf_b)  # creates version 3
    
                restore_item = library.restore_version(symbol, as_of=2)  # creates version 4
                assert restore_item.version == 4
                assert restore_item.metadata == {'field_b': 1}
    
                item = library.read(symbol)
>               assert_frame_equal(item.data, mydf_a)
[1m[31mE               AssertionError: (None, <Second>)[0m

[1m[31mtests/integration/store/test_version_store.py[0m:1403: AssertionError

===============================================================================

    @pytest.mark.parametrize('fw_pointers_cfg', [FwPointersCfg.DISABLED, FwPointersCfg.HYBRID, FwPointersCfg.ENABLED])
    def test_restore_version_which_updated_only_metadata(library, fw_pointers_cfg):
        with FwPointersCtx(fw_pointers_cfg):
            symbol = 'FTL'
            mydf_a = _rnd_df(10, 5)
            mydf_b = _rnd_df(10, 5)
            with patch('arctic.arctic.logger.info') as info:
                library.write(symbol, data=mydf_a, metadata={'field_a': 1})  # creates version 1
                library.write_metadata(symbol, metadata={'field_b': 1})  # creates version 2
                library.write(symbol, data=mydf_b)  # creates version 3
    
                restore_item = library.restore_version(symbol, as_of=2)  # creates version 4
                assert restore_item.version == 4
                assert restore_item.metadata == {'field_b': 1}
    
                item = library.read(symbol)
>               assert_frame_equal(item.data, mydf_a)
[1m[31mE               AssertionError: (None, <Second>)[0m

[1m[31mtests/integration/store/test_version_store.py[0m:1403: AssertionError

===============================================================================

    @pytest.mark.parametrize('fw_pointers_cfg', [FwPointersCfg.DISABLED, FwPointersCfg.HYBRID, FwPointersCfg.ENABLED])
    def test_restore_version_which_updated_only_metadata(library, fw_pointers_cfg):
        with FwPointersCtx(fw_pointers_cfg):
            symbol = 'FTL'
            mydf_a = _rnd_df(10, 5)
            mydf_b = _rnd_df(10, 5)
            with patch('arctic.arctic.logger.info') as info:
                library.write(symbol, data=mydf_a, metadata={'field_a': 1})  # creates version 1
                library.write_metadata(symbol, metadata={'field_b': 1})  # creates version 2
                library.write(symbol, data=mydf_b)  # creates version 3
    
                restore_item = library.restore_version(symbol, as_of=2)  # creates version 4
                assert restore_item.version == 4
                assert restore_item.metadata == {'field_b': 1}
    
                item = library.read(symbol)
>               assert_frame_equal(item.data, mydf_a)
[1m[31mE               AssertionError: (None, <Second>)[0m

[1m[31mtests/integration/store/test_version_store.py[0m:1403: AssertionError

===============================================================================

    @pytest.mark.parametrize('fw_pointers_cfg', [FwPointersCfg.DISABLED, FwPointersCfg.HYBRID, FwPointersCfg.ENABLED])
    def test_restore_version_then_snapshot(library, fw_pointers_cfg):
        with FwPointersCtx(fw_pointers_cfg):
            symbol = 'FTL'
            mydf_a = _rnd_df(10, 5)
            mydf_b = _rnd_df(10, 5)
            with patch('arctic.arctic.logger.info') as info:
                library.write(symbol, data=mydf_a, metadata={'field_a': 1})  # creates version 1
                library.write_metadata(symbol, metadata={'field_b': 1})  # creates version 2
    
                restore_item = library.restore_version(symbol, as_of=1)  # creates version 3
                assert restore_item.metadata == {'field_a': 1}
                assert restore_item.version == 3
    
                library.snapshot('SNAP_1')
                library.write(symbol, data=mydf_b)  # creates version 3
    
                item = library.read(symbol, as_of='SNAP_1')
>               assert_frame_equal(item.data, mydf_a)
[1m[31mE               AssertionError: (None, <Second>)[0m

[1m[31mtests/integration/store/test_version_store.py[0m:1426: AssertionError

===============================================================================

    @pytest.mark.parametrize('fw_pointers_cfg', [FwPointersCfg.DISABLED, FwPointersCfg.HYBRID, FwPointersCfg.ENABLED])
    def test_restore_version_then_snapshot(library, fw_pointers_cfg):
        with FwPointersCtx(fw_pointers_cfg):
            symbol = 'FTL'
            mydf_a = _rnd_df(10, 5)
            mydf_b = _rnd_df(10, 5)
            with patch('arctic.arctic.logger.info') as info:
                library.write(symbol, data=mydf_a, metadata={'field_a': 1})  # creates version 1
                library.write_metadata(symbol, metadata={'field_b': 1})  # creates version 2
    
                restore_item = library.restore_version(symbol, as_of=1)  # creates version 3
                assert restore_item.metadata == {'field_a': 1}
                assert restore_item.version == 3
    
                library.snapshot('SNAP_1')
                library.write(symbol, data=mydf_b)  # creates version 3
    
                item = library.read(symbol, as_of='SNAP_1')
>               assert_frame_equal(item.data, mydf_a)
[1m[31mE               AssertionError: (None, <Second>)[0m

[1m[31mtests/integration/store/test_version_store.py[0m:1426: AssertionError

===============================================================================

    @pytest.mark.parametrize('fw_pointers_cfg', [FwPointersCfg.DISABLED, FwPointersCfg.HYBRID, FwPointersCfg.ENABLED])
    def test_restore_version_then_snapshot(library, fw_pointers_cfg):
        with FwPointersCtx(fw_pointers_cfg):
            symbol = 'FTL'
            mydf_a = _rnd_df(10, 5)
            mydf_b = _rnd_df(10, 5)
            with patch('arctic.arctic.logger.info') as info:
                library.write(symbol, data=mydf_a, metadata={'field_a': 1})  # creates version 1
                library.write_metadata(symbol, metadata={'field_b': 1})  # creates version 2
    
                restore_item = library.restore_version(symbol, as_of=1)  # creates version 3
                assert restore_item.metadata == {'field_a': 1}
                assert restore_item.version == 3
    
                library.snapshot('SNAP_1')
                library.write(symbol, data=mydf_b)  # creates version 3
    
                item = library.read(symbol, as_of='SNAP_1')
>               assert_frame_equal(item.data, mydf_a)
[1m[31mE               AssertionError: (None, <Second>)[0m

[1m[31mtests/integration/store/test_version_store.py[0m:1426: AssertionError

===============================================================================

    @pytest.mark.parametrize('fw_pointers_cfg', [FwPointersCfg.DISABLED, FwPointersCfg.HYBRID, FwPointersCfg.ENABLED])
    def test_restore_version_latest_snapshot_noop(library, fw_pointers_cfg):
        with FwPointersCtx(fw_pointers_cfg):
            symbol = 'FTL'
            mydf_a = _rnd_df(10, 5)
            with patch('arctic.arctic.logger.info') as info:
                library.write(symbol, data=mydf_a, metadata={'field_a': 1})  # creates version 1
                library.write_metadata(symbol, metadata={'field_b': 1})  # creates version 2
                library.snapshot('SNAP_1')
    
                restore_item = library.restore_version(symbol, as_of='SNAP_1')  # does not create a new version
                assert restore_item.metadata == {'field_b': 1}
                assert restore_item.version == 2
    
                item = library.read(symbol)
>               assert_frame_equal(item.data, mydf_a)
[1m[31mE               AssertionError: (None, <Second>)[0m

[1m[31mtests/integration/store/test_version_store.py[0m:1446: AssertionError

===============================================================================

    @pytest.mark.parametrize('fw_pointers_cfg', [FwPointersCfg.DISABLED, FwPointersCfg.HYBRID, FwPointersCfg.ENABLED])
    def test_restore_version_latest_snapshot_noop(library, fw_pointers_cfg):
        with FwPointersCtx(fw_pointers_cfg):
            symbol = 'FTL'
            mydf_a = _rnd_df(10, 5)
            with patch('arctic.arctic.logger.info') as info:
                library.write(symbol, data=mydf_a, metadata={'field_a': 1})  # creates version 1
                library.write_metadata(symbol, metadata={'field_b': 1})  # creates version 2
                library.snapshot('SNAP_1')
    
                restore_item = library.restore_version(symbol, as_of='SNAP_1')  # does not create a new version
                assert restore_item.metadata == {'field_b': 1}
                assert restore_item.version == 2
    
                item = library.read(symbol)
>               assert_frame_equal(item.data, mydf_a)
[1m[31mE               AssertionError: (None, <Second>)[0m

[1m[31mtests/integration/store/test_version_store.py[0m:1446: AssertionError

===============================================================================

    @pytest.mark.parametrize('fw_pointers_cfg', [FwPointersCfg.DISABLED, FwPointersCfg.HYBRID, FwPointersCfg.ENABLED])
    def test_restore_version_latest_snapshot_noop(library, fw_pointers_cfg):
        with FwPointersCtx(fw_pointers_cfg):
            symbol = 'FTL'
            mydf_a = _rnd_df(10, 5)
            with patch('arctic.arctic.logger.info') as info:
                library.write(symbol, data=mydf_a, metadata={'field_a': 1})  # creates version 1
                library.write_metadata(symbol, metadata={'field_b': 1})  # creates version 2
                library.snapshot('SNAP_1')
    
                restore_item = library.restore_version(symbol, as_of='SNAP_1')  # does not create a new version
                assert restore_item.metadata == {'field_b': 1}
                assert restore_item.version == 2
    
                item = library.read(symbol)
>               assert_frame_equal(item.data, mydf_a)
[1m[31mE               AssertionError: (None, <Second>)[0m

[1m[31mtests/integration/store/test_version_store.py[0m:1446: AssertionError

===============================================================================

    @pytest.mark.parametrize('fw_pointers_cfg', [FwPointersCfg.DISABLED, FwPointersCfg.HYBRID, FwPointersCfg.ENABLED])
    def test_restore_version_latest_version_noop(library, fw_pointers_cfg):
        with FwPointersCtx(fw_pointers_cfg):
            symbol = 'FTL'
            mydf_a = _rnd_df(10, 5)
            with patch('arctic.arctic.logger.info') as info:
                library.write(symbol, data=mydf_a, metadata={'field_a': 1})  # creates version 1
                library.write_metadata(symbol, metadata={'field_b': 1})  # creates version 2
    
                restore_item = library.restore_version(symbol, as_of=2)  # does not create a new version
                assert restore_item.metadata == {'field_b': 1}
                assert restore_item.version == 2
    
                item = library.read(symbol)
>               assert_frame_equal(item.data, mydf_a)
[1m[31mE               AssertionError: (None, <Second>)[0m

[1m[31mtests/integration/store/test_version_store.py[0m:1465: AssertionError

===============================================================================

@pytest.mark.parametrize('fw_pointers_cfg', [FwPointersCfg.DISABLED, FwPointersCfg.HYBRID, FwPointersCfg.ENABLED])
    def test_restore_version_latest_version_noop(library, fw_pointers_cfg):
        with FwPointersCtx(fw_pointers_cfg):
            symbol = 'FTL'
            mydf_a = _rnd_df(10, 5)
            with patch('arctic.arctic.logger.info') as info:
                library.write(symbol, data=mydf_a, metadata={'field_a': 1})  # creates version 1
                library.write_metadata(symbol, metadata={'field_b': 1})  # creates version 2
    
                restore_item = library.restore_version(symbol, as_of=2)  # does not create a new version
                assert restore_item.metadata == {'field_b': 1}
                assert restore_item.version == 2
    
                item = library.read(symbol)
>               assert_frame_equal(item.data, mydf_a)
[1m[31mE               AssertionError: (None, <Second>)[0m

[1m[31mtests/integration/store/test_version_store.py[0m:1465: AssertionError

===============================================================================

    @pytest.mark.parametrize('fw_pointers_cfg', [FwPointersCfg.DISABLED, FwPointersCfg.HYBRID, FwPointersCfg.ENABLED])
    def test_restore_version_latest_version_noop(library, fw_pointers_cfg):
        with FwPointersCtx(fw_pointers_cfg):
            symbol = 'FTL'
            mydf_a = _rnd_df(10, 5)
            with patch('arctic.arctic.logger.info') as info:
                library.write(symbol, data=mydf_a, metadata={'field_a': 1})  # creates version 1
                library.write_metadata(symbol, metadata={'field_b': 1})  # creates version 2
    
                restore_item = library.restore_version(symbol, as_of=2)  # does not create a new version
                assert restore_item.metadata == {'field_b': 1}
                assert restore_item.version == 2
    
                item = library.read(symbol)
>               assert_frame_equal(item.data, mydf_a)
[1m[31mE               AssertionError: (None, <Second>)[0m

[1m[31mtests/integration/store/test_version_store.py[0m:1465: AssertionError

===============================================================================

    @pytest.mark.parametrize('fw_pointers_cfg', [FwPointersCfg.DISABLED, FwPointersCfg.HYBRID, FwPointersCfg.ENABLED])
    def test_restore_version_snap_delete_symbol_restore(library, fw_pointers_cfg):
        with FwPointersCtx(fw_pointers_cfg):
            symbol = 'FTL'
            mydf = _rnd_df(20, 5)
            with patch('arctic.arctic.logger.info') as info:
                library.write(symbol, data=mydf[:10], metadata={'field_a': 1})  # creates version 1
                library.append(symbol, data=mydf[10:15])  # version 2
                library.snapshot('snapA')
    
                library.append(symbol, data=mydf[15:20])  # version 3
                library.delete(symbol)  # version 4
    
                restored_item = library.restore_version(symbol, as_of='snapA')  # version 5
                assert restored_item.metadata == {'field_a': 1}
                assert restored_item.version == 5
    
                item = library.read(symbol)
>               assert_frame_equal(item.data, mydf[:15])
[1m[31mE               AssertionError: (None, <Second>)[0m

[1m[31mtests/integration/store/test_version_store.py[0m:1488: AssertionError

===============================================================================

    @pytest.mark.parametrize('fw_pointers_cfg', [FwPointersCfg.DISABLED, FwPointersCfg.HYBRID, FwPointersCfg.ENABLED])
    def test_restore_version_snap_delete_symbol_restore(library, fw_pointers_cfg):
        with FwPointersCtx(fw_pointers_cfg):
            symbol = 'FTL'
            mydf = _rnd_df(20, 5)
            with patch('arctic.arctic.logger.info') as info:
                library.write(symbol, data=mydf[:10], metadata={'field_a': 1})  # creates version 1
                library.append(symbol, data=mydf[10:15])  # version 2
                library.snapshot('snapA')
    
                library.append(symbol, data=mydf[15:20])  # version 3
                library.delete(symbol)  # version 4
    
                restored_item = library.restore_version(symbol, as_of='snapA')  # version 5
                assert restored_item.metadata == {'field_a': 1}
                assert restored_item.version == 5
    
                item = library.read(symbol)
>               assert_frame_equal(item.data, mydf[:15])
[1m[31mE               AssertionError: (None, <Second>)[0m

[1m[31mtests/integration/store/test_version_store.py[0m:1488: AssertionError

===============================================================================

    @pytest.mark.parametrize('fw_pointers_cfg', [FwPointersCfg.DISABLED, FwPointersCfg.HYBRID, FwPointersCfg.ENABLED])
    def test_restore_version_snap_delete_symbol_restore(library, fw_pointers_cfg):
        with FwPointersCtx(fw_pointers_cfg):
            symbol = 'FTL'
            mydf = _rnd_df(20, 5)
            with patch('arctic.arctic.logger.info') as info:
                library.write(symbol, data=mydf[:10], metadata={'field_a': 1})  # creates version 1
                library.append(symbol, data=mydf[10:15])  # version 2
                library.snapshot('snapA')
    
                library.append(symbol, data=mydf[15:20])  # version 3
                library.delete(symbol)  # version 4
    
                restored_item = library.restore_version(symbol, as_of='snapA')  # version 5
                assert restored_item.metadata == {'field_a': 1}
                assert restored_item.version == 5
    
                item = library.read(symbol)
>               assert_frame_equal(item.data, mydf[:15])
[1m[31mE               AssertionError: (None, <Second>)[0m

[1m[31mtests/integration/store/test_version_store.py[0m:1488: AssertionError

===============================================================================

    @pytest.mark.parametrize('fw_pointers_cfg', [FwPointersCfg.DISABLED, FwPointersCfg.HYBRID, FwPointersCfg.ENABLED])
    def test_can_write_tz_aware_data_df(library, fw_pointers_cfg):
        with FwPointersCtx(fw_pointers_cfg):
            mydf = _mixed_test_data()['index_tz_aware'][0]
            library.write(symbol='symTz', data=mydf)
            read_data = library.read(symbol='symTz').data
            # Arctic converts by default the data to UTC, convert back
            read_data.colB = read_data.colB.dt.tz_localize('UTC').dt.tz_convert(read_data.index.tzinfo)
            assert library._versions.find_one({'symbol': 'symTz'})['type'] == PandasDataFrameStore.TYPE
>           assert_frame_equal(mydf, read_data)
[1m[31mE           AssertionError: (<Day>, None)[0m

[1m[31mtests/integration/store/test_version_store.py[0m:1720: AssertionError

===============================================================================

    @pytest.mark.parametrize('fw_pointers_cfg', [FwPointersCfg.DISABLED, FwPointersCfg.HYBRID, FwPointersCfg.ENABLED])
    def test_can_write_tz_aware_data_df(library, fw_pointers_cfg):
        with FwPointersCtx(fw_pointers_cfg):
            mydf = _mixed_test_data()['index_tz_aware'][0]
            library.write(symbol='symTz', data=mydf)
            read_data = library.read(symbol='symTz').data
            # Arctic converts by default the data to UTC, convert back
            read_data.colB = read_data.colB.dt.tz_localize('UTC').dt.tz_convert(read_data.index.tzinfo)
            assert library._versions.find_one({'symbol': 'symTz'})['type'] == PandasDataFrameStore.TYPE
>           assert_frame_equal(mydf, read_data)
[1m[31mE           AssertionError: (<Day>, None)[0m

[1m[31mtests/integration/store/test_version_store.py[0m:1720: AssertionError

===============================================================================

    @pytest.mark.parametrize('fw_pointers_cfg', [FwPointersCfg.DISABLED, FwPointersCfg.HYBRID, FwPointersCfg.ENABLED])
    def test_can_write_tz_aware_data_df(library, fw_pointers_cfg):
        with FwPointersCtx(fw_pointers_cfg):
            mydf = _mixed_test_data()['index_tz_aware'][0]
            library.write(symbol='symTz', data=mydf)
            read_data = library.read(symbol='symTz').data
            # Arctic converts by default the data to UTC, convert back
            read_data.colB = read_data.colB.dt.tz_localize('UTC').dt.tz_convert(read_data.index.tzinfo)
            assert library._versions.find_one({'symbol': 'symTz'})['type'] == PandasDataFrameStore.TYPE
>           assert_frame_equal(mydf, read_data)
[1m[31mE           AssertionError: (<Day>, None)[0m

[1m[31mtests/integration/store/test_version_store.py[0m:1720: AssertionError

===============================================================================

    @pytest.mark.parametrize('fw_pointers_cfg', [FwPointersCfg.DISABLED, FwPointersCfg.HYBRID, FwPointersCfg.ENABLED])
    def test_can_write_tz_aware_data_series(library, fw_pointers_cfg):
        with FwPointersCtx(fw_pointers_cfg):
            myseries = _mixed_test_data()['index_tz_aware'][0]['colB']
            library.write(symbol='symTzSer', data=myseries)
            read_data = library.read(symbol='symTzSer').data
            # Arctic converts by default the data to UTC, convert back
            read_data = read_data.dt.tz_localize('UTC').dt.tz_convert(read_data.index.tzinfo)
            assert library._versions.find_one({'symbol': 'symTzSer'})['type'] == PandasSeriesStore.TYPE
>           assert_series_equal(myseries, read_data)
[1m[31mE           AssertionError: (<Day>, None)[0m

[1m[31mtests/integration/store/test_version_store.py[0m:1732: AssertionError

===============================================================================

    @pytest.mark.parametrize('fw_pointers_cfg', [FwPointersCfg.DISABLED, FwPointersCfg.HYBRID, FwPointersCfg.ENABLED])
    def test_can_write_tz_aware_data_series(library, fw_pointers_cfg):
        with FwPointersCtx(fw_pointers_cfg):
            myseries = _mixed_test_data()['index_tz_aware'][0]['colB']
            library.write(symbol='symTzSer', data=myseries)
            read_data = library.read(symbol='symTzSer').data
            # Arctic converts by default the data to UTC, convert back
            read_data = read_data.dt.tz_localize('UTC').dt.tz_convert(read_data.index.tzinfo)
            assert library._versions.find_one({'symbol': 'symTzSer'})['type'] == PandasSeriesStore.TYPE
>           assert_series_equal(myseries, read_data)
[1m[31mE           AssertionError: (<Day>, None)[0m

[1m[31mtests/integration/store/test_version_store.py[0m:1732: AssertionError

===============================================================================

    @pytest.mark.parametrize('fw_pointers_cfg', [FwPointersCfg.DISABLED, FwPointersCfg.HYBRID, FwPointersCfg.ENABLED])
    def test_can_write_tz_aware_data_series(library, fw_pointers_cfg):
        with FwPointersCtx(fw_pointers_cfg):
            myseries = _mixed_test_data()['index_tz_aware'][0]['colB']
            library.write(symbol='symTzSer', data=myseries)
            read_data = library.read(symbol='symTzSer').data
            # Arctic converts by default the data to UTC, convert back
            read_data = read_data.dt.tz_localize('UTC').dt.tz_convert(read_data.index.tzinfo)
            assert library._versions.find_one({'symbol': 'symTzSer'})['type'] == PandasSeriesStore.TYPE
>           assert_series_equal(myseries, read_data)
[1m[31mE           AssertionError: (<Day>, None)[0m

[1m[31mtests/integration/store/test_version_store.py[0m:1732: AssertionError

===============================================================================

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
[1m[31mE       AssertionError: (<Day>, None)[0m

[1m[31mtests/integration/tickstore/test_toplevel.py[0m:65: AssertionError

===============================================================================

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
[1m[31mE       AssertionError: (<Day>, None)[0m

[1m[31mtests/integration/tickstore/test_toplevel.py[0m:101: AssertionError

===============================================================================

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
[1m[31mE       AssertionError: (<Day>, None)[0m

[1m[31mtests/integration/tickstore/test_toplevel.py[0m:197: AssertionError

===============================================================================

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
[1m[31mE       AssertionError: (<Day>, None)[0m

[1m[31mtests/integration/tickstore/test_toplevel.py[0m:215: AssertionError

===============================================================================

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

[1m[31mtests/unit/store/test_version_store_audit.py[0m:221: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

_mock_self = <Mock name='mock._delete_version' id='140207817640312'>
args = (sentinel.symbol, 3), kwargs = {}
self = <Mock name='mock._delete_version' id='140207817640312'>
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
[1m[31mE           AssertionError: Expected '_delete_version' to be called once. Called 0 times.[0m

[1m[31m../../../virtualenv/python3.6.7/lib/python3.6/site-packages/mock/mock.py[0m:925: AssertionError

===============================================================================

----------------------------- Captured stderr call -----------------------------
2021-01-13 15:40:04,084 INFO arctic.store.audit MT: None@None: [sentinel.user] sentinel.log: sentinel.symbol
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
[32mINFO    [0m arctic.store.audit:audit.py:87 MT: None@None: [sentinel.user] sentinel.log: sentinel.symbol

===============================================================================
===============================================================================

[33m=============================== warnings summary ===============================[0m
tests/integration/test_arctic.py:6
  /home/travis/build/man-group/arctic/tests/integration/test_arctic.py:6: FutureWarning: pandas.util.testing is deprecated. Use the functions in the public API at pandas.testing instead.
    from pandas.util.testing import assert_frame_equal

tests/integration/tickstore/test_ts_read.py:9
  /home/travis/build/man-group/arctic/tests/integration/tickstore/test_ts_read.py:9: DeprecationWarning: Importing from numpy.testing.utils is deprecated since 1.15.0, import from numpy.testing instead.
    from numpy.testing.utils import assert_array_equal

tests/integration/test_arctic.py: 4 warnings
tests/integration/test_concurrent_append.py: 1 warning
tests/integration/test_howtos.py: 3 warnings
tests/integration/scripts/test_arctic_fsck.py: 45 warnings
tests/integration/scripts/test_copy_data.py: 23 warnings
tests/integration/store/test_bitemporal_store.py: 43 warnings
tests/integration/store/test_ndarray_store.py: 37 warnings
tests/integration/store/test_ndarray_store_append.py: 69 warnings
tests/integration/store/test_pandas_store.py: 378 warnings
tests/integration/store/test_version_store.py: 647 warnings
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
tests/integration/store/test_version_store.py: 570 warnings
tests/integration/store/test_version_store_audit.py: 21 warnings
tests/integration/store/test_version_store_corruption.py: 18 warnings
  /home/travis/build/man-group/arctic/arctic/store/_ndarray_store.py:657: DeprecationWarning: tostring() is deprecated. Use tobytes() instead.
    chunks = [(item[i * rows_per_chunk: (i + 1) * rows_per_chunk]).tostring() for i in idxs]

tests/integration/test_arctic.py: 3 warnings
tests/integration/test_howtos.py: 3 warnings
tests/integration/scripts/test_arctic_fsck.py: 42 warnings
tests/integration/scripts/test_copy_data.py: 21 warnings
tests/integration/store/test_bitemporal_store.py: 29 warnings
tests/integration/store/test_pandas_store.py: 37 warnings
tests/integration/store/test_version_store.py: 1976 warnings
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
tests/integration/chunkstore/test_fixes.py: 91 warnings
tests/integration/chunkstore/test_utils.py: 2 warnings
tests/integration/chunkstore/tools/test_tools.py: 52 warnings
tests/unit/serialization/test_numpy_arrays.py: 26 warnings
  /home/travis/build/man-group/arctic/arctic/serialization/numpy_arrays.py:119: DeprecationWarning: tostring() is deprecated. Use tobytes() instead.
    arrays.append(arr.tostring())

tests/integration/store/test_ndarray_store.py: 3 warnings
tests/integration/store/test_ndarray_store_append.py: 583 warnings
tests/integration/store/test_pandas_store.py: 19 warnings
tests/integration/store/test_version_store.py: 1546 warnings
tests/integration/store/test_version_store_corruption.py: 124 warnings
  /home/travis/build/man-group/arctic/arctic/store/_ndarray_store.py:449: DeprecationWarning: tostring() is deprecated. Use tobytes() instead.
    data = item.tostring()

tests/integration/store/test_ndarray_store.py::test_save_read_large_ndarray
  /home/travis/build/man-group/arctic/tests/integration/store/test_ndarray_store.py:146: DeprecationWarning: tostring() is deprecated. Use tobytes() instead.
    assert len(ndarr.tostring()) > 16 * 1024 * 1024

tests/integration/store/test_ndarray_store_append.py::test_append_read_large_ndarray[FwPointersCfg.DISABLED]
tests/integration/store/test_ndarray_store_append.py::test_append_read_large_ndarray[FwPointersCfg.HYBRID]
tests/integration/store/test_ndarray_store_append.py::test_append_read_large_ndarray[FwPointersCfg.ENABLED]
  /home/travis/build/man-group/arctic/tests/integration/store/test_ndarray_store_append.py:112: DeprecationWarning: tostring() is deprecated. Use tobytes() instead.
    assert len(ndarr.tostring()) > 16 * 1024 * 1024

tests/integration/store/test_ndarray_store_append.py::test_save_append_read_ndarray[FwPointersCfg.DISABLED]
tests/integration/store/test_ndarray_store_append.py::test_save_append_read_ndarray[FwPointersCfg.HYBRID]
tests/integration/store/test_ndarray_store_append.py::test_save_append_read_ndarray[FwPointersCfg.ENABLED]
  /home/travis/build/man-group/arctic/tests/integration/store/test_ndarray_store_append.py:138: DeprecationWarning: tostring() is deprecated. Use tobytes() instead.
    assert len(ndarr.tostring()) > 16 * 1024 * 1024

tests/integration/store/test_ndarray_store_append.py::test_save_append_read_1row_ndarray
  /home/travis/build/man-group/arctic/tests/integration/store/test_ndarray_store_append.py:155: DeprecationWarning: tostring() is deprecated. Use tobytes() instead.
    assert len(ndarr.tostring()) > 16 * 1024 * 1024

tests/integration/store/test_ndarray_store_append.py::test_append_too_large_ndarray
  /home/travis/build/man-group/arctic/tests/integration/store/test_ndarray_store_append.py:172: DeprecationWarning: tostring() is deprecated. Use tobytes() instead.
    assert len(ndarr.tostring()) > 16 * 1024 * 1024

tests/integration/store/test_pandas_store.py::test_save_read_pandas_empty_series_with_datetime_multiindex_with_timezone
  /home/travis/build/man-group/arctic/tests/integration/store/test_pandas_store.py:150: DeprecationWarning: The default dtype for empty Series will be 'object' instead of 'float64' in a future version. Specify a dtype explicitly to silence this warning.
    df = Series(data=[], index=empty_index)

tests/integration/store/test_pandas_store.py::test_duplicate_labels
tests/integration/store/test_pandas_store.py::test_duplicate_labels
tests/integration/store/test_pandas_store.py::test_duplicate_labels
tests/integration/store/test_pandas_store.py::test_duplicate_labels
  /home/travis/virtualenv/python3.6.7/lib/python3.6/site-packages/numpy/core/numeric.py:2378: DeprecationWarning: elementwise comparison failed; this will raise an error in the future.
    return bool(asarray(a1 == a2).all())

tests/integration/store/test_pickle_store.py::test_bson_large_object
  /home/travis/build/man-group/arctic/tests/integration/store/test_pickle_store.py:53: DeprecationWarning: tostring() is deprecated. Use tobytes() instead.
    'large_thing': np.random.rand(int(2.1 * 1024 * 1024)).tostring()}

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

tests/unit/serialization/test_incremental.py: 38 warnings
  /home/travis/build/man-group/arctic/tests/unit/serialization/test_incremental.py:53: DeprecationWarning: tostring() is deprecated. Use tobytes() instead.
    matching = expectation[0].tostring() == incr_ser_data.tostring()

tests/unit/serialization/test_incremental.py: 41846 warnings
  /home/travis/build/man-group/arctic/arctic/serialization/incremental.py:223: DeprecationWarning: tostring() is deprecated. Use tobytes() instead.
    chunk = chunk.tostring() if chunk is not None and get_bytes else chunk

tests/unit/serialization/test_incremental.py: 19 warnings
  /home/travis/build/man-group/arctic/tests/unit/serialization/test_incremental.py:73: DeprecationWarning: tostring() is deprecated. Use tobytes() instead.
    matching = expectation[0].tostring() == b''.join(chunk_bytes)

tests/unit/serialization/test_incremental.py: 57 warnings
  /home/travis/build/man-group/arctic/tests/unit/serialization/test_incremental.py:101: DeprecationWarning: tostring() is deprecated. Use tobytes() instead.
    matching = expectation[0].tostring() == b''.join(chunk_bytes)

tests/unit/serialization/test_incremental.py: 10 warnings
  /home/travis/build/man-group/arctic/tests/unit/serialization/test_incremental.py:136: DeprecationWarning: tostring() is deprecated. Use tobytes() instead.
    matching = expectation[0][from_idx:to_idx].tostring() == b''.join(chunk_bytes)

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

===============================================================================
=========================== short test summary info ============================
FAILED tests/integration/chunkstore/test_chunkstore.py::test_overwrite_series
FAILED tests/integration/chunkstore/test_chunkstore.py::test_quarterly_data
FAILED tests/integration/chunkstore/test_fixes.py::test_date_interval - Asser...
FAILED tests/integration/chunkstore/test_fixes.py::test_missing_cols - Assert...
FAILED tests/integration/store/test_pandas_store.py::test_save_read_pandas_series_with_unicode_index_name
FAILED tests/integration/store/test_pandas_store.py::test_save_read_pandas_dataframe_with_unicode_index_name
FAILED tests/integration/store/test_pandas_store.py::test_daterange_large_DataFrame
FAILED tests/integration/store/test_pandas_store.py::test_daterange_large_DataFrame_middle
FAILED tests/integration/store/test_pandas_store.py::test_daterange[df0-assert_frame_equal]
FAILED tests/integration/store/test_pandas_store.py::test_daterange[df1-assert_series_equal]
FAILED tests/integration/store/test_pandas_store.py::test_daterange_append - ...
FAILED tests/integration/store/test_version_store.py::test_write_metadata[FwPointersCfg.DISABLED]
FAILED tests/integration/store/test_version_store.py::test_write_metadata[FwPointersCfg.HYBRID]
FAILED tests/integration/store/test_version_store.py::test_write_metadata[FwPointersCfg.ENABLED]
FAILED tests/integration/store/test_version_store.py::test_write_metadata_followed_by_append[FwPointersCfg.DISABLED]
FAILED tests/integration/store/test_version_store.py::test_write_metadata_followed_by_append[FwPointersCfg.HYBRID]
FAILED tests/integration/store/test_version_store.py::test_write_metadata_followed_by_append[FwPointersCfg.ENABLED]
FAILED tests/integration/store/test_version_store.py::test_write_metadata_purge_previous_versions[FwPointersCfg.DISABLED]
FAILED tests/integration/store/test_version_store.py::test_write_metadata_purge_previous_versions[FwPointersCfg.HYBRID]
FAILED tests/integration/store/test_version_store.py::test_write_metadata_purge_previous_versions[FwPointersCfg.ENABLED]
FAILED tests/integration/store/test_version_store.py::test_write_metadata_delete_symbol[FwPointersCfg.DISABLED]
FAILED tests/integration/store/test_version_store.py::test_write_metadata_delete_symbol[FwPointersCfg.HYBRID]
FAILED tests/integration/store/test_version_store.py::test_write_metadata_delete_symbol[FwPointersCfg.ENABLED]
FAILED tests/integration/store/test_version_store.py::test_write_metadata_snapshots[FwPointersCfg.DISABLED]
FAILED tests/integration/store/test_version_store.py::test_write_metadata_snapshots[FwPointersCfg.HYBRID]
FAILED tests/integration/store/test_version_store.py::test_write_metadata_snapshots[FwPointersCfg.ENABLED]
FAILED tests/integration/store/test_version_store.py::test_restore_version[FwPointersCfg.DISABLED]
FAILED tests/integration/store/test_version_store.py::test_restore_version[FwPointersCfg.HYBRID]
FAILED tests/integration/store/test_version_store.py::test_restore_version[FwPointersCfg.ENABLED]
FAILED tests/integration/store/test_version_store.py::test_restore_version_purging_previous_versions[FwPointersCfg.DISABLED]
FAILED tests/integration/store/test_version_store.py::test_restore_version_purging_previous_versions[FwPointersCfg.HYBRID]
FAILED tests/integration/store/test_version_store.py::test_restore_version_purging_previous_versions[FwPointersCfg.ENABLED]
FAILED tests/integration/store/test_version_store.py::test_restore_version_non_existent_version[FwPointersCfg.DISABLED]
FAILED tests/integration/store/test_version_store.py::test_restore_version_non_existent_version[FwPointersCfg.HYBRID]
FAILED tests/integration/store/test_version_store.py::test_restore_version_non_existent_version[FwPointersCfg.ENABLED]
FAILED tests/integration/store/test_version_store.py::test_restore_version_which_updated_only_metadata[FwPointersCfg.DISABLED]
FAILED tests/integration/store/test_version_store.py::test_restore_version_which_updated_only_metadata[FwPointersCfg.HYBRID]
FAILED tests/integration/store/test_version_store.py::test_restore_version_which_updated_only_metadata[FwPointersCfg.ENABLED]
FAILED tests/integration/store/test_version_store.py::test_restore_version_then_snapshot[FwPointersCfg.DISABLED]
FAILED tests/integration/store/test_version_store.py::test_restore_version_then_snapshot[FwPointersCfg.HYBRID]
FAILED tests/integration/store/test_version_store.py::test_restore_version_then_snapshot[FwPointersCfg.ENABLED]
FAILED tests/integration/store/test_version_store.py::test_restore_version_latest_snapshot_noop[FwPointersCfg.DISABLED]
FAILED tests/integration/store/test_version_store.py::test_restore_version_latest_snapshot_noop[FwPointersCfg.HYBRID]
FAILED tests/integration/store/test_version_store.py::test_restore_version_latest_snapshot_noop[FwPointersCfg.ENABLED]
FAILED tests/integration/store/test_version_store.py::test_restore_version_latest_version_noop[FwPointersCfg.DISABLED]
FAILED tests/integration/store/test_version_store.py::test_restore_version_latest_version_noop[FwPointersCfg.HYBRID]
FAILED tests/integration/store/test_version_store.py::test_restore_version_latest_version_noop[FwPointersCfg.ENABLED]
FAILED tests/integration/store/test_version_store.py::test_restore_version_snap_delete_symbol_restore[FwPointersCfg.DISABLED]
FAILED tests/integration/store/test_version_store.py::test_restore_version_snap_delete_symbol_restore[FwPointersCfg.HYBRID]
FAILED tests/integration/store/test_version_store.py::test_restore_version_snap_delete_symbol_restore[FwPointersCfg.ENABLED]
FAILED tests/integration/store/test_version_store.py::test_can_write_tz_aware_data_df[FwPointersCfg.DISABLED]
FAILED tests/integration/store/test_version_store.py::test_can_write_tz_aware_data_df[FwPointersCfg.HYBRID]
FAILED tests/integration/store/test_version_store.py::test_can_write_tz_aware_data_df[FwPointersCfg.ENABLED]
FAILED tests/integration/store/test_version_store.py::test_can_write_tz_aware_data_series[FwPointersCfg.DISABLED]
FAILED tests/integration/store/test_version_store.py::test_can_write_tz_aware_data_series[FwPointersCfg.HYBRID]
FAILED tests/integration/store/test_version_store.py::test_can_write_tz_aware_data_series[FwPointersCfg.ENABLED]
FAILED tests/integration/tickstore/test_toplevel.py::test_should_return_data_when_date_range_falls_in_a_single_underlying_library
FAILED tests/integration/tickstore/test_toplevel.py::test_should_return_data_when_date_range_spans_libraries_even_if_one_returns_nothing
FAILED tests/integration/tickstore/test_toplevel.py::test_should_write_top_level_with_list_of_dicts
FAILED tests/integration/tickstore/test_toplevel.py::test_should_write_top_level_with_correct_timezone
FAILED tests/unit/store/test_version_store_audit.py::test_ArcticTransaction_detects_concurrent_writes

===============================================================================

     61 failed
   1255 passed
      3 skipped
     19 xfailed
      1 xpassed
  60848 warnings
1322.83s (0:22:02)

===============================================================================

