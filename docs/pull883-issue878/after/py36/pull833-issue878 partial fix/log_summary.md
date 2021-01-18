
tests/integration/store/test_pandas_store.py::test_save_read_pandas_series_with_unicode_index_name [31mFAILED[0m[31m [ 25%][0m
tests/integration/store/test_pandas_store.py::test_save_read_pandas_dataframe_with_multiindex [32mPASSED[0m[31m [ 25%][0m2021-01-16 17:58:54,016 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping

tests/integration/store/test_pandas_store.py::test_save_read_pandas_dataframe_with_unicode_index_name [31mFAILED[0m[31m [ 25%][0m
tests/integration/store/test_pandas_store.py::test_cant_write_pandas_series_with_tuple_values [32mPASSED[0m[31m [ 25%][0m2021-01-16 17:58:56,943 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping

tests/integration/tickstore/test_toplevel.py::test_should_return_data_when_date_range_falls_in_a_single_underlying_library [31mFAILED[0m[31m [ 54%][0m
tests/integration/tickstore/test_toplevel.py::test_should_return_data_when_date_range_spans_libraries [32mPASSED[0m[31m [ 54%][0m2021-01-16 18:06:47,154 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping

tests/integration/tickstore/test_toplevel.py::test_should_return_data_when_date_range_spans_libraries_even_if_one_returns_nothing 2021-01-16 18:06:48,109 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping
[31mFAILED[0m[31m [ 54%][0m
tests/integration/tickstore/test_toplevel.py::test_should_add_underlying_library_where_none_exists [32mPASSED[0m[31m [ 54%][0m2021-01-16 18:06:48,984 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping

tests/integration/tickstore/test_toplevel.py::test_should_write_top_level_with_list_of_dicts [31mFAILED[0m[31m [ 55%][0m
tests/integration/tickstore/test_toplevel.py::test_should_write_top_level_with_correct_timezone [31mFAILED[0m[31m [ 55%][0m
tests/integration/tickstore/test_toplevel.py::test_min_max_date [32mPASSED[0m[31m   [ 55%][0m2021-01-16 18:06:59,328 DEBUG pytest_server_fixtures.base2 Server is already killed, skipping

tests/unit/store/test_version_store_audit.py::test_ArcticTransaction_detects_concurrent_writes [31mFAILED[0m[31m [ 96%][0m

===============================================================================
=================================== FAILURES ===================================
[31m[1m_____________ test_save_read_pandas_series_with_unicode_index_name _____________[0m

library = <VersionStore at 0x7f9129f6a3c8>
    <ArcticLibrary at 0x7f9129f6ae48, arctic_test.TEST>
        <Arctic at 0x7f9129fbf908, connected to MongoClient(host=['127.23.25.166:13953'], document_class=dict, tz_aware=False, connect=True)>

    def test_save_read_pandas_series_with_unicode_index_name(library):
        df = Series(data=['A', 'BC', 'DEF'],
                    index=MultiIndex.from_tuples([(np.datetime64(dt(2013, 1, 1)),),
                                                  (np.datetime64(dt(2013, 1, 2)),),
                                                  (np.datetime64(dt(2013, 1, 3)),)], names=[u'DATETIME']))
        library.write('pandas', df)
>       saved_df = library.read('pandas').data
===============================================================================

library = <VersionStore at 0x7f912a1cf828>
    <ArcticLibrary at 0x7f912a1cfbe0, arctic_test.TEST>
        <Arctic at 0x7f912972b400, connected to MongoClient(host=['127.23.25.166:5223'], document_class=dict, tz_aware=False, connect=True)>

    def test_save_read_pandas_dataframe_with_unicode_index_name(library):
        df = DataFrame(data=['A', 'BC', 'DEF'],
                       index=MultiIndex.from_tuples([(np.datetime64(dt(2013, 1, 1)),),
                                                     (np.datetime64(dt(2013, 1, 2)),),
                                                     (np.datetime64(dt(2013, 1, 3)),)], names=[u'DATETIME']))
        library.write('pandas', df)
>       saved_df = library.read('pandas').data
===============================================================================

>       assert_frame_equal(df, res.tz_convert(mktz('Europe/London')))
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
arctic = <Arctic at 0x7f9129102470, connected to MongoClient(host=['127.23.25.166:9419'], document_class=dict, tz_aware=False, connect=True)>

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

===============================================================================

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
  /home/travis/build/man-group/arctic/arctic/store/_pandas_ndarray_store.py:58: DeprecationWarning: tostring() is deprecated. Use tobytes() instead.
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

tests/integration/store/test_ndarray_store.py::test_save_read_large_ndarray
  /home/travis/build/man-group/arctic/tests/integration/store/test_ndarray_store.py:146: DeprecationWarning: tostring() is deprecated. Use tobytes() instead.
    assert len(ndarr.tostring()) > 16 * 1024 * 1024                         # FIXME: deprecated tostring

tests/integration/store/test_pandas_store.py::test_save_read_pandas_empty_series_with_datetime_multiindex_with_timezone
  /home/travis/build/man-group/arctic/tests/integration/store/test_pandas_store.py:147: DeprecationWarning: The default dtype for empty Series will be 'object' instead of 'float64' in a future version. Specify a dtype explicitly to silence this warning.
    df = Series(data=[], index=empty_index)

tests/integration/store/test_pandas_store.py::test_duplicate_labels
tests/integration/store/test_pandas_store.py::test_duplicate_labels
tests/integration/store/test_pandas_store.py::test_duplicate_labels
tests/integration/store/test_pandas_store.py::test_duplicate_labels
  /home/travis/virtualenv/python3.6.7/lib/python3.6/site-packages/numpy/core/numeric.py:2378: DeprecationWarning: elementwise comparison failed; this will raise an error in the future.
    return bool(asarray(a1 == a2).all())

tests/integration/store/test_pickle_store.py::test_bson_large_object
  /home/travis/build/man-group/arctic/tests/integration/store/test_pickle_store.py:53: DeprecationWarning: tostring() is deprecated. Use tobytes() instead.
    'large_thing': np.random.rand(int(2.1 * 1024 * 1024)).tostring()}       # FIXME: deprecated tostring

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
FAILED tests/integration/store/test_pandas_store.py::test_save_read_pandas_series_with_unicode_index_name
FAILED tests/integration/store/test_pandas_store.py::test_save_read_pandas_dataframe_with_unicode_index_name
FAILED tests/integration/tickstore/test_toplevel.py::test_should_return_data_when_date_range_falls_in_a_single_underlying_library
FAILED tests/integration/tickstore/test_toplevel.py::test_should_return_data_when_date_range_spans_libraries_even_if_one_returns_nothing
FAILED tests/integration/tickstore/test_toplevel.py::test_should_write_top_level_with_list_of_dicts
FAILED tests/integration/tickstore/test_toplevel.py::test_should_write_top_level_with_correct_timezone
FAILED tests/unit/store/test_version_store_audit.py::test_ArcticTransaction_detects_concurrent_writes

===============================================================================

       7 failed
    1309 passed
       3 skipped
      19 xfailed
       1 xpassed
   60747 warnings
 0:22:21 test time


===============================================================================

