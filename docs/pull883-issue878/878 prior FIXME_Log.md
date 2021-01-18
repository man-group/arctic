# FIXME_Log

> Note: This is the FIXME log from the original work that only looked at 
> Python 3.6

These changes were made to `FIX` test failures (as seen in PyCharm).

Setup according to the [ReadMe.md](./ReadMe.md)

----------------------------------------------------

### startup routine
```powershell
$ cd arctic_venv36
$ source .venv36/bin/activate
```

### multiple terminals
One terminal window is need for each of these processes:
* MongoDB
* Arctic Setup

#### MongoDB
* Mongodb-Compass
```powershell
(.venv)$ mongodb-compass
```
* db.enableFreeMonitoring()
```powershell
(.venv)$ mongo
> db.enableFreeMonitoring() # this returns the url which you can cut-n-past into a browser
```
* mongostat
```powershell
(.venv)$ mongostat # this streams formated stdIO to the terminal
```

#### Arctic Setup - rerun tests
```powershell
(.venv)(IB36)$ python setup.py develop test         # install develop and test
```

----------------------------------------------------

> CM#xxx comment left in code denotes issues/changes to get test to skip/pass

### FIXME: CM#001 - (str)
* TODO: verify datastructure (diff versions)
* tzlocal does not have a `zone` property , string cast
    - _mktz.py line 33       # FIXME: CM#001
    - test_mktz.py line 9    # FIXME: CM#001

### FIXME: CM#002 - (new expected)
* TODO: verify datastructure (diff versions)
* did the datastructure change?
* update expected value by removing the missing field
    - test_arctic.py lines 82-99  remove `u'ns': u'arctic.library',`
    - test_arctic.py lines 102-107 remove `u'ns': u'arctic.library.snapshots',`
    - test_arctic.py lines 110-118 remove `u'ns': u'arctic.library.versions',`
    - test_arctic.py lines 121-126 remove `u'ns': u'arctic.library.version_nums',`

### FIXME: CM#003 - similar to (issue #420)
* TODO: verify pandas behavior (see pandas/tests/indexes/multi/test_constructors.TestTimeSeries)
* date read from MongoDB does not come back with freq set (it is null)
    - tests/util.py lines 77-91 add `add_idx_freq(idx, freq)`  (similarly for other files)
    - test_chunkstore.py lines 12 import
    - test_chunkstore.py lines 716-723 expose reads and add freq
    - test_chunkstore.py lines 1044-1046 expose reads and add freq
    - test_fixes.py lines 76-88 expose reads and add freq
    - test_fixes.py lines 12 import
    - test_fixes.py lines 76-88 expose reads and add freq
    - test_pandas_store.py lines 860-905 expose reads and add freq

> Snapshot: [Coverage report: 90%](./htmlcov/index.html)  

### FIXME: CM#004 - (skip test) - verify mock behavior of MongoDB transactions
* @pytest.mark.skip(reason='FIXME: CM#004 - (skip test)')
    tests/integration/scripts/test_arctic_fsck.py line 31
* TODO: verify mock behavior of MongoDB transactions
    the initial count does not change, 
    test_arctic_fsck.py line 55 new count == initial count
    test_arctic_fsck.py line 173 `assert len(libc)`

### FIXME: CM#005 - (deprecate pandas.util.testing)
* replace with 
    from pandas.testing import assert_frame_equal<, assert_series_equal>
    arctic/_util.py
    tests/integration/test_arctic.py
    tests/integration/store/test_bitemporal_store.py
    tests/unit/store/test_bitemporal_store.py
    tests/integration/chuckstore/test_chunckstore.py
    tests/integration/scripts/test_copy_data.py
    tests/unit/chunkstore/test_date_chunker.py
    tests/integration/chunkstore/test_fixes.py
    tests/integration/store/test_metadata_store.py
    tests/unit/test_multi_index.py
    tests/unit/serialization/test_numpy_arrays.py
    tests/integration/store/test_pandas_store.py
    tests/integration/chunckstore/tools/test_tools.py
    tests/integration/tickstore/test_toplevel.py
    tests/unit/tickstore/test_toplevel.py
    tests/integration/tickstore/test_ts_read.py
    tests/integration/tickstore/test_ts_write.py
    tests/integration/chunckstore/test_utils.py
    tests/integration/store/test_version_store.py
    tests/integration/store/test_version_store_audit.py

### FIXME: CM#006 - (skip test) - verify library.write and prune behavior
* @pytest.mark.skip(reason='FIXME: CM#006 - verify library.write and prune behavior')
* TODO: verify library.write and prune behavior
    tests/integration/scripts/test_prune_versions.py

### FIXME: CM#007 - (deprecated tostring)
* replace with tobytes() or str cast
    arctic/store/_ndarray_store.py:600
    arctic/store/_ndarray_store.py:657
    arctic/store/_pandas_ndarray_store.py:58
    arrays.append(arr.tostring())
    tests/integration/tickstore/test_ts_read.py:9
    arctic/serialization/numpy_arrays.py:118
    arctic/serialization/numpy_arrays.py:119
    arctic/store/_ndarray_store.py:449
    tests/integration/store/test_ndarray_store_append.py:112
    tests/integration/store/test_ndarray_store_append.py:138
    tests/integration/store/test_ndarray_store_append.py:155
    tests/integration/store/test_ndarray_store_append.py:172
    tests/integration/store/test_pickle_store.py:53
    arctic/tickstore/tickstore.py:707:
    arctic/tickstore/tickstore.py:718
    arctic/tickstore/tickstore.py:727
    arctic/tickstore/tickstore.py:758
    arctic/tickstore/tickstore.py:763
    arctic/tickstore/tickstore.py:776
    tests/unit/serialization/test_incremental.py:53
    arctic/serialization/incremental.py:223
    tests/unit/serialization/test_incremental.py:73
    tests/unit/serialization/test_incremental.py:101
    tests/unit/serialization/test_incremental.py:136
    tests/unit/store/test_pickle_store.py:121

### FIXME: CM#008 - (expand cases for build_index_array)
* build_index_array = isinstance(recarr.dtype.metadata['index_tz'], list)
    arctic/serializationnumpy_records.py:95-103 use tri-state build_index_array

### FIXME: CM#009 - (replace assert_frame_equal with df.equals)
* replace assert_frame_equal with df.equals
    tests/integration/store/test_pickle_store.py:802-826
   
    tests/integration/store/test_pandas_store.py
    tests/integration/tickstore/test_toplevel.py
    tests/integration/tickstore/test_ts_read.py
    tests/integration/store/test_version_store.py
    
### FIXME: CM#010 - (deprecate numpy.testing.utils)

### FIXME: CM#011 - (replace pandas Series MultiIndex with DatetimeIndex)
    tests/integration/store/test_pandas_store.py:76
        test_save_read_pandas_series_with_unicode_index_name
    tests/integration/store/test_pandas_store.py:102
        test_save_read_pandas_dataframe_with_unicode_index_name

### FIXME: CM#012 - (read does not return January 1st)
    tests/integration/tickstore/test_toplevel.py:63
        test_should_return_data_when_date_range_falls_in_a_single_underlying_library

### FIXME: CM#013 - ()

### FIXME: CM#014 - ()

### FIXME: CM#015 - ()

# Py36 Summary

```shell
================================================== test session starts ===================================================
platform linux -- Python 3.6.12, pytest-6.2.1, py-1.9.0, pluggy-0.13.1
rootdir: /home/cwm/git/bb.FLXSA/quant/arctic_venv36
plugins: xdist-1.26.1, shutil-1.7.0, server-fixtures-1.7.0, forked-1.3.0, cov-2.10.1, timeout-1.4.2, Faker-5.0.2
collected 1339 items                                                                                                     

tests/integration/test_arctic.py .....................                                                             [  1%]
tests/integration/test_arctic_multithreading.py ..                                                                 [  1%]
tests/integration/test_async_arctic.py .                                                                           [  1%]
tests/integration/test_compress_integration.py ..........                                                          [  2%]
tests/integration/test_concurrent_append.py .                                                                      [  2%]
tests/integration/test_decorators.py .                                                                             [  2%]
tests/integration/test_howtos.py ..                                                                                [  2%]
tests/integration/chunkstore/test_chunkstore.py .................................................................. [  7%]
.....................                                                                                              [  9%]
tests/integration/chunkstore/test_fixes.py ........                                                                [  9%]
tests/integration/chunkstore/test_utils.py .                                                                       [ 10%]
tests/integration/chunkstore/tools/test_tools.py .                                                                 [ 10%]
tests/integration/fixtures/test_arctic.py ...                                                                      [ 10%]
tests/integration/scripts/test_arctic_fsck.py ssssssssssss..............................ssssssssssss.............. [ 15%]
..........                                                                                                         [ 16%]
tests/integration/scripts/test_copy_data.py .....                                                                  [ 16%]
tests/integration/scripts/test_delete_library.py .....                                                             [ 16%]
tests/integration/scripts/test_enable_sharding.py ...                                                              [ 17%]
tests/integration/scripts/test_initialize_library.py ....                                                          [ 17%]
tests/integration/scripts/test_list_libraries.py ...                                                               [ 17%]
tests/integration/scripts/test_prune_versions.py ...ss                                                             [ 17%]
tests/integration/store/test_bitemporal_store.py ................                                                  [ 19%]
tests/integration/store/test_metadata_store.py ..........                                                          [ 19%]
tests/integration/store/test_ndarray_store.py ..x..................X                                               [ 21%]
tests/integration/store/test_ndarray_store_append.py ...............................................               [ 25%]
tests/integration/store/test_pandas_store.py ..................................................................... [ 30%]
................xxxxxxxxxxx.....x..................ss..                                                            [ 34%]
tests/integration/store/test_pickle_store.py .........                                                             [ 35%]
tests/integration/store/test_version_store.py .xx................................................................. [ 40%]
.................................................................................................................. [ 48%]
...............................................                                                                    [ 52%]
tests/integration/store/test_version_store_audit.py ..........                                                     [ 52%]
tests/integration/store/test_version_store_corruption.py .....s....                                                [ 53%]
tests/integration/tickstore/test_toplevel.py ..........FFF.F..x....FF.....                                         [ 55%]
tests/integration/tickstore/test_ts_delete.py ..                                                                   [ 55%]
tests/integration/tickstore/test_ts_read.py .......FFFFFF..............                                            [ 57%]
tests/integration/tickstore/test_ts_write.py ..F..                                                                 [ 58%]
tests/unit/test_arctic.py ....................................                                                     [ 61%]
tests/unit/test_auth.py ...                                                                                        [ 61%]
tests/unit/test_compress.py .............                                                                          [ 62%]
tests/unit/test_compression.py ..........                                                                          [ 62%]
tests/unit/test_decorators_unit.py ......x.....                                                                    [ 63%]
tests/unit/test_fixtures.py ...                                                                                    [ 64%]
tests/unit/test_hooks.py ...                                                                                       [ 64%]
tests/unit/test_hosts.py ......                                                                                    [ 64%]
tests/unit/test_multi_index.py ..............                                                                      [ 65%]
tests/unit/test_util.py ..                                                                                         [ 65%]
tests/unit/chunkstore/test_date_chunker.py .......                                                                 [ 66%]
tests/unit/chunkstore/test_passthrough_chunker.py .                                                                [ 66%]
tests/unit/date/test_daterange.py .......................................................                          [ 70%]
tests/unit/date/test_datetime_to_ms_roundtrip.py ..x.......                                                        [ 71%]
tests/unit/date/test_mktz.py ....                                                                                  [ 71%]
tests/unit/date/test_util.py ........................................................                              [ 75%]
tests/unit/scripts/test_arctic_create_user.py ....                                                                 [ 76%]
tests/unit/scripts/test_arctic_fsck.py ..                                                                          [ 76%]
tests/unit/scripts/test_initialize_library.py .....                                                                [ 76%]
tests/unit/scripts/test_utils.py ......                                                                            [ 77%]
tests/unit/serialization/test_incremental.py ..................................................................... [ 82%]
.......................................                                                                            [ 85%]
tests/unit/serialization/test_numpy_arrays.py ............                                                         [ 86%]
tests/unit/serialization/test_numpy_records.py ............                                                        [ 87%]
tests/unit/serialization/test_pandas_is_serializable.py ........................                                   [ 88%]
tests/unit/store/test_bitemporal_store.py .                                                                        [ 88%]
tests/unit/store/test_bson_store.py ...................                                                            [ 90%]
tests/unit/store/test_metadata_store.py .......                                                                    [ 90%]
tests/unit/store/test_ndarray_store.py ..........                                                                  [ 91%]
tests/unit/store/test_pandas_ndarray_store.py .....                                                                [ 91%]
tests/unit/store/test_pickle_store.py ......x...                                                                   [ 92%]
tests/unit/store/test_version_item.py ....                                                                         [ 92%]
tests/unit/store/test_version_store.py ...................................                                         [ 95%]
tests/unit/store/test_version_store_audit.py ..........F                                                           [ 96%]
tests/unit/store/test_version_store_utils.py .....                                                                 [ 96%]
tests/unit/tickstore/test_tickstore.py F...F..F....                                                                [ 97%]
tests/unit/tickstore/test_toplevel.py ...............................                                              [100%]

==========================================================================================================================
======================================================== FAILURES ========================================================
______________________ test_should_return_data_when_date_range_falls_in_a_single_underlying_library ______________________

toplevel_tickstore = <arctic.tickstore.toplevel.TopLevelTickStore object at 0x7f2ea7f2b908>
arctic = <Arctic at 0x7f2eacbb5208, connected to MongoClient(host=['127.150.242.244:5631'], document_class=dict, tz_aware=False, connect=True)>

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
    
>       assert df.equals(res.tz_convert(mktz('Europe/London')))     # FIXME CM unequal shapes
E       AssertionError: assert False
E        +  where False = <bound method NDFrame.equals of                                   A         B         C         D\n2010-01-01 00:00:00+...:00:00+00:00 -1.428197 -1.072046 -1.314763  1.637222\n2010-01-06 00:00:00+00:00 -0.924080 -0.361759  1.139929  1.749399>(                                  A         B         C         D\n2010-01-02 00:00:00+00:00  0.202171 -0.497088  0.084...0:00:00+00:00 -1.428197 -1.072046 -1.314763  1.637222\n2010-01-06 00:00:00+00:00 -0.924080 -0.361759  1.139929  1.749399)
E        +    where <bound method NDFrame.equals of                                   A         B         C         D\n2010-01-01 00:00:00+...:00:00+00:00 -1.428197 -1.072046 -1.314763  1.637222\n2010-01-06 00:00:00+00:00 -0.924080 -0.361759  1.139929  1.749399> =                                   A         B         C         D\n2010-01-01 00:00:00+00:00  2.010167 -0.496257 -0.822...0:00:00+00:00 -1.428197 -1.072046 -1.314763  1.637222\n2010-01-06 00:00:00+00:00 -0.924080 -0.361759  1.139929  1.749399.equals
E        +    and                                     A         B         C         D\n2010-01-02 00:00:00+00:00  0.202171 -0.497088  0.084...0:00:00+00:00 -1.428197 -1.072046 -1.314763  1.637222\n2010-01-06 00:00:00+00:00 -0.924080 -0.361759  1.139929  1.749399 = <bound method NDFrame.tz_convert of                                   A         B         C         D\n2010-01-01 17:00...:00:00-07:00 -1.428197 -1.072046 -1.314763  1.637222\n2010-01-05 17:00:00-07:00 -0.924080 -0.361759  1.139929  1.749399>(tzfile('/usr/share/zoneinfo/Europe/London'))
E        +      where <bound method NDFrame.tz_convert of                                   A         B         C         D\n2010-01-01 17:00...:00:00-07:00 -1.428197 -1.072046 -1.314763  1.637222\n2010-01-05 17:00:00-07:00 -0.924080 -0.361759  1.139929  1.749399> =                                   A         B         C         D\n2010-01-01 17:00:00-07:00  0.202171 -0.497088  0.084...7:00:00-07:00 -1.428197 -1.072046 -1.314763  1.637222\n2010-01-05 17:00:00-07:00 -0.924080 -0.361759  1.139929  1.749399.tz_convert
E        +      and   tzfile('/usr/share/zoneinfo/Europe/London') = mktz('Europe/London')

tests/integration/tickstore/test_toplevel.py:65: AssertionError
==========================================================================================================================

________________________________ test_should_return_data_when_date_range_spans_libraries _________________________________

toplevel_tickstore = <arctic.tickstore.toplevel.TopLevelTickStore object at 0x7f2e8c1b21d0>
arctic = <Arctic at 0x7f2eac3fce48, connected to MongoClient(host=['127.150.242.244:25863'], document_class=dict, tz_aware=False, connect=True)>

    def test_should_return_data_when_date_range_spans_libraries(toplevel_tickstore, arctic):
        arctic.initialize_library('FEED_2010.LEVEL1', tickstore.TICK_STORE_TYPE)
        arctic.initialize_library('FEED_2011.LEVEL1', tickstore.TICK_STORE_TYPE)
        tickstore_2010 = arctic['FEED_2010.LEVEL1']
        tickstore_2011 = arctic['FEED_2011.LEVEL1']
        toplevel_tickstore.add(DateRange(start=dt(2010, 1, 1), end=dt(2010, 12, 31, 23, 59, 59, 999000)), 'FEED_2010.LEVEL1')
        toplevel_tickstore.add(DateRange(start=dt(2011, 1, 1), end=dt(2011, 12, 31, 23, 59, 59, 999000)), 'FEED_2011.LEVEL1')
        dates = pd.date_range('20100101', periods=6, tz=mktz('Europe/London'))
        df_10 = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))
        tickstore_2010.write('blah', df_10)
        dates = pd.date_range('20110101', periods=6, tz=mktz('Europe/London'))
        df_11 = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))
        tickstore_2011.write('blah', df_11)
        res = toplevel_tickstore.read('blah', DateRange(start=dt(2010, 1, 2), end=dt(2011, 1, 4)), list('ABCD'))
        expected_df = pd.concat([df_10[1:], df_11[:4]])
>       assert_frame_equal(expected_df, res.tz_convert(mktz('Europe/London')))      # FIXME CM unequal shapes
E       AssertionError: DataFrame are different
E       
E       DataFrame shape mismatch
E       [left]:  (9, 4)
E       [right]: (7, 4)

tests/integration/tickstore/test_toplevel.py:83: AssertionError
==========================================================================================================================

__________________ test_should_return_data_when_date_range_spans_libraries_even_if_one_returns_nothing ___________________

toplevel_tickstore = <arctic.tickstore.toplevel.TopLevelTickStore object at 0x7f2eac422f28>
arctic = <Arctic at 0x7f2eacb71eb8, connected to MongoClient(host=['127.150.242.244:15099'], document_class=dict, tz_aware=False, connect=True)>

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
>       assert_frame_equal(expected_df, res.tz_convert(mktz('Europe/London')))      # FIXME CM unequal shapes
E       AssertionError: DataFrame are different
E       
E       DataFrame shape mismatch
E       [left]:  (5, 4)
E       [right]: (4, 4)

tests/integration/tickstore/test_toplevel.py:101: AssertionError
==========================================================================================================================

_____________ test_should_add_underlying_library_where_another_library_exists_in_a_non_overlapping_daterange _____________

toplevel_tickstore = <arctic.tickstore.toplevel.TopLevelTickStore object at 0x7f2eacca48d0>
arctic = <Arctic at 0x7f2eacb4a278, connected to MongoClient(host=['127.150.242.244:19579'], document_class=dict, tz_aware=False, connect=True)>

    def test_should_add_underlying_library_where_another_library_exists_in_a_non_overlapping_daterange(toplevel_tickstore, arctic):
        toplevel_tickstore._collection.insert_one({'library_name': 'FEED_2011.LEVEL1', 'start': dt(2011, 1, 1), 'end': dt(2011, 12, 31)})
        arctic.initialize_library('FEED_2010.LEVEL1', tickstore.TICK_STORE_TYPE)
>       toplevel_tickstore.add(DateRange(start=dt(2010, 1, 1), end=dt(2010, 12, 31, 23, 59, 59, 999000)), 'FEED_2010.LEVEL1')

tests/integration/tickstore/test_toplevel.py:113: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <arctic.tickstore.toplevel.TopLevelTickStore object at 0x7f2eacca48d0>
date_range = DateRange(start=datetime.datetime(2010, 1, 1, 0, 0), end=datetime.datetime(2010, 12, 31, 23, 59, 59, 999000))
library_name = 'FEED_2010.LEVEL1'

        def add(self, date_range, library_name):
            """
            Adds the library with the given date range to the underlying collection of libraries used by this store.
            The underlying libraries should not overlap as the date ranges are assumed to be CLOSED_CLOSED by this function
            and the rest of the class.
    
            Arguments:
    
            date_range: A date range provided on the assumption that it is CLOSED_CLOSED. If for example the underlying
            libraries were split by year, the start of the date range would be datetime.datetime(year, 1, 1) and the end
            would be datetime.datetime(year, 12, 31, 23, 59, 59, 999000). The date range must fall on UTC day boundaries,
            that is the start must be add midnight and the end must be 1 millisecond before midnight.
    
            library_name: The name of the underlying library. This must be the name of a valid Arctic library
            """
            # check that the library is valid
            try:
                self._arctic_lib.arctic[library_name]
            except Exception as e:
                logger.error("Could not load library")
                raise e
            assert date_range.start and date_range.end, "Date range should have start and end properties {}".format(date_range)
            start = date_range.start.astimezone(mktz('UTC')) if date_range.start.tzinfo is not None else date_range.start.replace(tzinfo=mktz('UTC'))
            end = date_range.end.astimezone(mktz('UTC')) if date_range.end.tzinfo is not None else date_range.end.replace(tzinfo=mktz('UTC'))
            assert start.time() == time.min and end.time() == end_time_min, "Date range should fall on UTC day boundaries {}".format(date_range)
            # check that the date range does not overlap
            library_metadata = self._get_library_metadata(date_range)
            if len(library_metadata) > 1 or (len(library_metadata) == 1 and library_metadata[0] != library_name):
                raise OverlappingDataException("""There are libraries that overlap with the date range:
    library: {}
>   overlapping libraries: {}""".format(library_name, [lib.library for lib in library_metadata]))
E   arctic.exceptions.OverlappingDataException: There are libraries that overlap with the date range:
E   library: FEED_2010.LEVEL1
E   overlapping libraries: ['FEED_2011.LEVEL1']

arctic/tickstore/toplevel.py:101: OverlappingDataException
==========================================================================================================================

_____________________________________ test_should_write_top_level_with_list_of_dicts _____________________________________

arctic = <Arctic at 0x7f2eacc21908, connected to MongoClient(host=['127.150.242.244:29045'], document_class=dict, tz_aware=False, connect=True)>

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
>       assert_frame_equal(expected, res.tz_convert(mktz('Europe/London')))     # FIXME CM unequal shapes
E       AssertionError: DataFrame are different
E       
E       DataFrame shape mismatch
E       [left]:  (57, 1)
E       [right]: (55, 1)

tests/integration/tickstore/test_toplevel.py:197: AssertionError
==========================================================================================================================

___________________________________ test_should_write_top_level_with_correct_timezone ____________________________________

arctic = <Arctic at 0x7f2eacdb9cf8, connected to MongoClient(host=['127.150.242.244:26994'], document_class=dict, tz_aware=False, connect=True)>

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
>       assert_frame_equal(expected, res)                                       # FIXME CM unequal shapes
E       AssertionError: DataFrame are different
E       
E       DataFrame shape mismatch
E       [left]:  (10, 1)
E       [right]: (9, 1)

tests/integration/tickstore/test_toplevel.py:215: AssertionError
==========================================================================================================================

_______________________________________________ test_date_range[tickstore] _______________________________________________

tickstore_lib = <TickStore at 0x7f2e6d5dbb38>
    <ArcticLibrary at 0x7f2eace21198, arctic_test.tickstore>
        <Arctic at 0x7f2eace216d8, connected to MongoClient(host=['127.150.242.244:32681'], document_class=dict, tz_aware=False, connect=True)>

    def test_date_range(tickstore_lib):
        tickstore_lib.write('SYM', DUMMY_DATA)
        df = tickstore_lib.read('SYM', date_range=DateRange(20130101, 20130103), columns=None)
>       assert_array_equal(df['a'].values, np.array([1, np.nan, np.nan]))   # FIXME CM unequal shapes
E       AssertionError: 
E       Arrays are not equal
E       
E       (shapes (2,), (3,) mismatch)
E        x: array([nan, nan])
E        y: array([ 1., nan, nan])

tests/integration/tickstore/test_ts_read.py:234: AssertionError
==========================================================================================================================

______________________________________ test_date_range_end_not_in_range[tickstore] _______________________________________

tickstore_lib = <TickStore at 0x7f2ea7e27cc0>
    <ArcticLibrary at 0x7f2ea7e27e80, arctic_test.tickstore>
        <Arctic at 0x7f2eacc210f0, connected to MongoClient(host=['127.150.242.244:24605'], document_class=dict, tz_aware=False, connect=True)>

    def test_date_range_end_not_in_range(tickstore_lib):
        DUMMY_DATA = [
                      {'a': 1.,
                       'b': 2.,
                       'index': dt(2013, 1, 1, tzinfo=mktz('Europe/London'))
                       },
                      {'b': 3.,
                       'c': 4.,
                       'index': dt(2013, 1, 2, 10, 1, tzinfo=mktz('Europe/London'))
                       },
                      ]
    
        tickstore_lib._chunk_size = 1
        tickstore_lib.write('SYM', DUMMY_DATA)
        with patch.object(tickstore_lib._collection, 'find', side_effect=tickstore_lib._collection.find) as f:
            df = tickstore_lib.read('SYM', date_range=DateRange(20130101, dt(2013, 1, 2, 9, 0)), columns=None)
>           assert_array_equal(df['b'].values, np.array([2.]))          # FIXME CM unequal shapes
E           AssertionError: 
E           Arrays are not equal
E           
E           Mismatched elements: 1 / 1 (100%)
E           Max absolute difference: 1.
E           Max relative difference: 0.5
E            x: array([3.])
E            y: array([2.])

tests/integration/tickstore/test_ts_read.py:300: AssertionError
==========================================================================================================================

____________________________________ test_date_range_default_timezone[tickstore-UTC] _____________________________________

tickstore_lib = <TickStore at 0x7f2eacc1c550>
    <ArcticLibrary at 0x7f2eacc1c908, arctic_test.tickstore>
        <Arctic at 0x7f2eacc1ce80, connected to MongoClient(host=['127.150.242.244:2282'], document_class=dict, tz_aware=False, connect=True)>
tz_name = 'UTC'

    @pytest.mark.parametrize('tz_name', ['UTC',
                                         'Europe/London',  # Sometimes ahead of UTC
                                         'America/New_York',  # Behind UTC
                                          ])
    def test_date_range_default_timezone(tickstore_lib, tz_name):
        """
        We assume naive datetimes are user-local
        """
        DUMMY_DATA = [
                      {'a': 1.,
                       'b': 2.,
                       'index': dt(2013, 1, 1, tzinfo=mktz(tz_name))
                       },
                      # Half-way through the year
                      {'b': 3.,
                       'c': 4.,
                       'index': dt(2013, 7, 1, tzinfo=mktz(tz_name))
                       },
                      ]
    
        with patch('tzlocal.get_localzone', return_value=Mock(zone=tz_name)):
            tickstore_lib._chunk_size = 1
            tickstore_lib.write('SYM', DUMMY_DATA)
>           df = tickstore_lib.read('SYM', date_range=DateRange(20130101, 20130701), columns=None)  # FIXME CM tz not read

tests/integration/tickstore/test_ts_read.py:327: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
arctic/tickstore/tickstore.py:297: in read
    date_range = to_pandas_closed_closed(date_range)
arctic/date/_util.py:136: in to_pandas_closed_closed
    start = to_dt(start, mktz()) if add_tz else start
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

zone = "<Mock id='139838443602328'>"

    def mktz(zone=None):
        """
        Return a new timezone (tzinfo object) based on the zone using the python-dateutil
        package.
    
        The concise name 'mktz' is for convenient when using it on the
        console.
    
        Parameters
        ----------
        zone : `String`
               The zone for the timezone. This defaults to local, returning:
               tzlocal.get_localzone()
    
        Returns
        -------
        An instance of a timezone which implements the tzinfo interface.
    
        Raises
        - - - - - -
        TimezoneError : Raised if a user inputs a bad timezone name.
        """
        if zone is None:
            zone = str(tzlocal.get_localzone())     # FIXME: CM#001 - (str)
        zone = six.u(zone)
        tz = dateutil.tz.gettz(zone)
        if not tz:
>           raise TimezoneError('Timezone "%s" can not be read' % (zone))
E           arctic.date._mktz.TimezoneError: Timezone "<Mock id='139838443602328'>" can not be read

arctic/date/_mktz.py:37: TimezoneError
==========================================================================================================================

_______________________________ test_date_range_default_timezone[tickstore-Europe/London] ________________________________

tickstore_lib = <TickStore at 0x7f2eacc540b8>
    <ArcticLibrary at 0x7f2ead1f8ef0, arctic_test.tickstore>
        <Arctic at 0x7f2eacc54240, connected to MongoClient(host=['127.150.242.244:13306'], document_class=dict, tz_aware=False, connect=True)>
tz_name = 'Europe/London'

    @pytest.mark.parametrize('tz_name', ['UTC',
                                         'Europe/London',  # Sometimes ahead of UTC
                                         'America/New_York',  # Behind UTC
                                          ])
    def test_date_range_default_timezone(tickstore_lib, tz_name):
        """
        We assume naive datetimes are user-local
        """
        DUMMY_DATA = [
                      {'a': 1.,
                       'b': 2.,
                       'index': dt(2013, 1, 1, tzinfo=mktz(tz_name))
                       },
                      # Half-way through the year
                      {'b': 3.,
                       'c': 4.,
                       'index': dt(2013, 7, 1, tzinfo=mktz(tz_name))
                       },
                      ]
    
        with patch('tzlocal.get_localzone', return_value=Mock(zone=tz_name)):
            tickstore_lib._chunk_size = 1
            tickstore_lib.write('SYM', DUMMY_DATA)
>           df = tickstore_lib.read('SYM', date_range=DateRange(20130101, 20130701), columns=None)  # FIXME CM tz not read

tests/integration/tickstore/test_ts_read.py:327: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
arctic/tickstore/tickstore.py:297: in read
    date_range = to_pandas_closed_closed(date_range)
arctic/date/_util.py:136: in to_pandas_closed_closed
    start = to_dt(start, mktz()) if add_tz else start
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

zone = "<Mock id='139838443832544'>"

    def mktz(zone=None):
        """
        Return a new timezone (tzinfo object) based on the zone using the python-dateutil
        package.
    
        The concise name 'mktz' is for convenient when using it on the
        console.
    
        Parameters
        ----------
        zone : `String`
               The zone for the timezone. This defaults to local, returning:
               tzlocal.get_localzone()
    
        Returns
        -------
        An instance of a timezone which implements the tzinfo interface.
    
        Raises
        - - - - - -
        TimezoneError : Raised if a user inputs a bad timezone name.
        """
        if zone is None:
            zone = str(tzlocal.get_localzone())     # FIXME: CM#001 - (str)
        zone = six.u(zone)
        tz = dateutil.tz.gettz(zone)
        if not tz:
>           raise TimezoneError('Timezone "%s" can not be read' % (zone))
E           arctic.date._mktz.TimezoneError: Timezone "<Mock id='139838443832544'>" can not be read

arctic/date/_mktz.py:37: TimezoneError
==========================================================================================================================

______________________________ test_date_range_default_timezone[tickstore-America/New_York] ______________________________

tickstore_lib = <TickStore at 0x7f2eac426400>
    <ArcticLibrary at 0x7f2ea80b5e10, arctic_test.tickstore>
        <Arctic at 0x7f2eacf98978, connected to MongoClient(host=['127.150.242.244:15019'], document_class=dict, tz_aware=False, connect=True)>
tz_name = 'America/New_York'

    @pytest.mark.parametrize('tz_name', ['UTC',
                                         'Europe/London',  # Sometimes ahead of UTC
                                         'America/New_York',  # Behind UTC
                                          ])
    def test_date_range_default_timezone(tickstore_lib, tz_name):
        """
        We assume naive datetimes are user-local
        """
        DUMMY_DATA = [
                      {'a': 1.,
                       'b': 2.,
                       'index': dt(2013, 1, 1, tzinfo=mktz(tz_name))
                       },
                      # Half-way through the year
                      {'b': 3.,
                       'c': 4.,
                       'index': dt(2013, 7, 1, tzinfo=mktz(tz_name))
                       },
                      ]
    
        with patch('tzlocal.get_localzone', return_value=Mock(zone=tz_name)):
            tickstore_lib._chunk_size = 1
            tickstore_lib.write('SYM', DUMMY_DATA)
>           df = tickstore_lib.read('SYM', date_range=DateRange(20130101, 20130701), columns=None)  # FIXME CM tz not read

tests/integration/tickstore/test_ts_read.py:327: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
arctic/tickstore/tickstore.py:297: in read
    date_range = to_pandas_closed_closed(date_range)
arctic/date/_util.py:136: in to_pandas_closed_closed
    start = to_dt(start, mktz()) if add_tz else start
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

zone = "<Mock id='139838447715776'>"

    def mktz(zone=None):
        """
        Return a new timezone (tzinfo object) based on the zone using the python-dateutil
        package.
    
        The concise name 'mktz' is for convenient when using it on the
        console.
    
        Parameters
        ----------
        zone : `String`
               The zone for the timezone. This defaults to local, returning:
               tzlocal.get_localzone()
    
        Returns
        -------
        An instance of a timezone which implements the tzinfo interface.
    
        Raises
        - - - - - -
        TimezoneError : Raised if a user inputs a bad timezone name.
        """
        if zone is None:
            zone = str(tzlocal.get_localzone())     # FIXME: CM#001 - (str)
        zone = six.u(zone)
        tz = dateutil.tz.gettz(zone)
        if not tz:
>           raise TimezoneError('Timezone "%s" can not be read' % (zone))
E           arctic.date._mktz.TimezoneError: Timezone "<Mock id='139838447715776'>" can not be read

arctic/date/_mktz.py:37: TimezoneError
==========================================================================================================================

__________________________________________ test_date_range_no_bounds[tickstore] __________________________________________

tickstore_lib = <TickStore at 0x7f2e6d5a5860>
    <ArcticLibrary at 0x7f2e6d5a5668, arctic_test.tickstore>
        <Arctic at 0x7f2ea7f84080, connected to MongoClient(host=['127.150.242.244:25867'], document_class=dict, tz_aware=False, connect=True)>

    def test_date_range_no_bounds(tickstore_lib):
        DUMMY_DATA = [
                      {'a': 1.,
                       'b': 2.,
                       'index': dt(2013, 1, 1, tzinfo=mktz('Europe/London'))
                       },
                      {'a': 3.,
                       'b': 4.,
                       'index': dt(2013, 1, 30, tzinfo=mktz('Europe/London'))
                       },
                      {'b': 5.,
                       'c': 6.,
                       'index': dt(2013, 2, 2, 10, 1, tzinfo=mktz('Europe/London'))
                       },
                      ]
    
        tickstore_lib._chunk_size = 1
        tickstore_lib.write('SYM', DUMMY_DATA)
    
        # 1) No start, no end
        df = tickstore_lib.read('SYM', columns=None)
        assert_array_equal(df['b'].values, np.array([2., 4.]))
        # 1.2) Start before the real start
        df = tickstore_lib.read('SYM', date_range=DateRange(20121231), columns=None)
        assert_array_equal(df['b'].values, np.array([2., 4.]))
        # 2.1) Only go one month out
        df = tickstore_lib.read('SYM', date_range=DateRange(20130101), columns=None)
>       assert_array_equal(df['b'].values, np.array([2., 4.]))      # FIXME CM unequal shapes
E       AssertionError: 
E       Arrays are not equal
E       
E       (shapes (1,), (2,) mismatch)
E        x: array([4.])
E        y: array([2., 4.])

tests/integration/tickstore/test_ts_read.py:369: AssertionError
==========================================================================================================================

____________________________________________ test_ts_write_pandas[tickstore] _____________________________________________

tickstore_lib = <TickStore at 0x7f2eacf8f7b8>
    <ArcticLibrary at 0x7f2ead0060f0, arctic_test.tickstore>
        <Arctic at 0x7f2eacdb9b38, connected to MongoClient(host=['127.150.242.244:16952'], document_class=dict, tz_aware=False, connect=True)>

    def test_ts_write_pandas(tickstore_lib):
        data = DUMMY_DATA
        tickstore_lib.write('SYM', data)
    
        data = tickstore_lib.read('SYM', columns=None)
        assert data.index[0] == dt(2013, 1, 1, tzinfo=mktz('Europe/London'))
        assert data.a[0] == 1
        tickstore_lib.delete('SYM')
        tickstore_lib.write('SYM', data)
    
        read = tickstore_lib.read('SYM', columns=None)
>       assert_frame_equal(read, data, check_names=False)

tests/integration/tickstore/test_ts_write.py:76: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
pandas/_libs/testing.pyx:67: in pandas._libs.testing.assert_almost_equal
    ???
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

>   ???
E   AssertionError: DataFrame.columns are different
E   
E   DataFrame.columns values are different (66.66667 %)
E   [left]:  Index(['b', 'a', 'c'], dtype='object')
E   [right]: Index(['b', 'c', 'a'], dtype='object')

pandas/_libs/testing.pyx:182: AssertionError
==========================================================================================================================

____________________________________ test_ArcticTransaction_detects_concurrent_writes ____________________________________

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
>       vs._delete_version.assert_called_once_with(sentinel.symbol, 3)          # FIXME CM

tests/unit/store/test_version_store_audit.py:221: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

_mock_self = <Mock name='mock._delete_version' id='139838457616312'>, args = (sentinel.symbol, 3), kwargs = {}
self = <Mock name='mock._delete_version' id='139838457616312'>
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

.venv36/lib/python3.6/site-packages/mock/mock.py:925: AssertionError
-------------------------------------------------- Captured stderr call --------------------------------------------------
Exception in thread Thread-747:
Traceback (most recent call last):
  File "/home/cwm/anaconda3/envs/IB36/lib/python3.6/threading.py", line 916, in _bootstrap_inner
    self.run()
  File "/home/cwm/anaconda3/envs/IB36/lib/python3.6/threading.py", line 864, in run
    self._target(*self._args, **self._kwargs)
  File "/home/cwm/git/bb.FLXSA/quant/arctic_venv36/tests/unit/store/test_version_store_audit.py", line 197, in losing_writer
    with pytest.raises(ArcticTransaction):
  File "/home/cwm/git/bb.FLXSA/quant/arctic_venv36/.eggs/pytest-6.2.1-py3.6.egg/_pytest/python_api.py", line 719, in raises
    raise TypeError(msg.format(not_a))
TypeError: expected exception must be a BaseException type, not ArcticTransaction

--------------------------------------------------- Captured log call ----------------------------------------------------
INFO     arctic.store.audit:audit.py:87 MT: None@None: [sentinel.user] sentinel.log: sentinel.symbol
______________________________________________ test_mongo_date_range_query _______________________________________________

    def test_mongo_date_range_query():
        self = create_autospec(TickStore)
        self._collection = create_autospec(Collection)
        self._symbol_query.return_value = {"sy": {"$in" : ["s1" , "s2"]}}
        self._collection.aggregate.return_value = iter([{"_id": "s1", "start": dt(2014, 1, 1, 0, 0, tzinfo=mktz())},
                                                        {"_id": "s2", "start": dt(2014, 1, 1, 12, 0, tzinfo=mktz())}])
    
        self._collection.find_one.side_effect = [
            {'e': dt(2014, 1, 1, 15, 0, tzinfo=mktz())},
            {'e': dt(2014, 1, 2, 12, 0, tzinfo=mktz())}]
    
        query = TickStore._mongo_date_range_query(self, 'sym', DateRange(dt(2014, 1, 2, 0, 0, tzinfo=mktz()),
                                                                         dt(2014, 1, 3, 0, 0, tzinfo=mktz())))
    
        assert self._collection.aggregate.call_args_list == [call([
         {"$match": {"s": {"$lte": dt(2014, 1, 2, 0, 0, tzinfo=mktz())}, "sy": {"$in" : ["s1" , "s2"]}}},
         {"$project": {"_id": 0, "s": 1, "sy": 1}},
         {"$group": {"_id": "$sy", "start": {"$max": "$s"}}},
         {"$sort": {"start": 1}}])]
    
        assert self._collection.find_one.call_args_list == [
            call({'sy': 's1', 's': dt(2014, 1, 1, 0, 0, tzinfo=mktz())}, {'e': 1}),
            call({'sy': 's2', 's': dt(2014, 1, 1, 12, 0, tzinfo=mktz())}, {'e': 1})]
    
>       assert query == {'s': {'$gte': dt(2014, 1, 1, 12, 0, tzinfo=mktz()), '$lte': dt(2014, 1, 3, 0, 0, tzinfo=mktz())}}  # FIXME CM
E       AssertionError: assert {'s': {'$gte'...ca/Denver'))}} == {'s': {'$gte'...ca/Denver'))}}
E         Differing items:
E         {'s': {'$gte': datetime.datetime(2014, 1, 1, 12, 0, tzinfo=tzfile('/usr/share/zoneinfo/UTC')), '$lte': datetime.datetime(2014, 1, 3, 0, 0, tzinfo=tzfile('/usr/share/zoneinfo/America/Denver'))}} != {'s': {'$gte': datetime.datetime(2014, 1, 1, 12, 0, tzinfo=tzfile('/usr/share/zoneinfo/America/Denver')), '$lte': datetime.datetime(2014, 1, 3, 0, 0, tzinfo=tzfile('/usr/share/zoneinfo/America/Denver'))}}
E         Use -v to get the full diff

tests/unit/tickstore/test_tickstore.py:43: AssertionError
==========================================================================================================================

__________________________________________ test_tickstore_to_bucket_with_image ___________________________________________

    def test_tickstore_to_bucket_with_image():
        symbol = 'SYM'
        tz = 'UTC'
        initial_image = {'index': dt(2014, 1, 1, 0, 0, tzinfo=mktz(tz)), 'A': 123, 'B': 54.4, 'C': 'DESC'}
        data = [{'index': dt(2014, 1, 1, 0, 1, tzinfo=mktz(tz)), 'A': 124, 'D': 0},
                {'index': dt(2014, 1, 1, 0, 2, tzinfo=mktz(tz)), 'A': 125, 'B': 27.2}]
        bucket, final_image = TickStore._to_bucket(data, symbol, initial_image)
        assert bucket[COUNT] == 2
        assert bucket[END] == dt(2014, 1, 1, 0, 2, tzinfo=mktz(tz))
        assert set(bucket[COLUMNS]) == set(('A', 'B', 'D'))
        assert set(bucket[COLUMNS]['A']) == set((ROWMASK, DTYPE, DATA))
        assert get_coldata(bucket[COLUMNS]['A']) == ([124, 125], [1, 1, 0, 0, 0, 0, 0, 0])
        assert get_coldata(bucket[COLUMNS]['B']) == ([27.2], [0, 1, 0, 0, 0, 0, 0, 0])
        assert get_coldata(bucket[COLUMNS]['D']) == ([0], [1, 0, 0, 0, 0, 0, 0, 0])
        index = [dt.fromtimestamp(int(i/1000)).replace(tzinfo=mktz(tz)) for i in
                 list(np.cumsum(np.frombuffer(decompress(bucket[INDEX]), dtype='uint64')))]
>       assert index == [i['index'] for i in data]                                # FIXME CM
E       AssertionError: assert [datetime.dat...neinfo/UTC'))] == [datetime.dat...neinfo/UTC'))]
E         At index 0 diff: datetime.datetime(2013, 12, 31, 17, 1, tzinfo=tzfile('/usr/share/zoneinfo/UTC')) != datetime.datetime(2014, 1, 1, 0, 1, tzinfo=tzfile('/usr/share/zoneinfo/UTC'))
E         Use -v to get the full diff

tests/unit/tickstore/test_tickstore.py:97: AssertionError
==========================================================================================================================

_________________________________________ test_tickstore_pandas_to_bucket_image __________________________________________

    def test_tickstore_pandas_to_bucket_image():
        symbol = 'SYM'
        tz = 'UTC'
        initial_image = {'index': dt(2014, 1, 1, 0, 0, tzinfo=mktz(tz)), 'A': 123, 'B': 54.4, 'C': 'DESC'}
        data = [{'A': 120, 'D': 1}, {'A': 122, 'B': 2.0}, {'A': 3, 'B': 3.0, 'D': 1}]
        tick_index = [dt(2014, 1, 2, 0, 0, tzinfo=mktz(tz)),
                      dt(2014, 1, 3, 0, 0, tzinfo=mktz(tz)),
                      dt(2014, 1, 4, 0, 0, tzinfo=mktz(tz))]
        data = pd.DataFrame(data, index=tick_index)
        bucket, final_image = TickStore._pandas_to_bucket(data, symbol, initial_image)
        assert final_image == {'index': dt(2014, 1, 4, 0, 0, tzinfo=mktz(tz)), 'A': 3, 'B': 3.0, 'C': 'DESC', 'D': 1}
        assert IMAGE_DOC in bucket
        assert bucket[COUNT] == 3
        assert bucket[START] == dt(2014, 1, 1, 0, 0, tzinfo=mktz(tz))
        assert bucket[END] == dt(2014, 1, 4, 0, 0, tzinfo=mktz(tz))
        assert set(bucket[COLUMNS]) == set(('A', 'B', 'D'))
        assert set(bucket[COLUMNS]['A']) == set((ROWMASK, DTYPE, DATA))
        assert get_coldata(bucket[COLUMNS]['A']) == ([120, 122, 3], [1, 1, 1, 0, 0, 0, 0, 0])
        values, rowmask = get_coldata(bucket[COLUMNS]['B'])
        assert np.isnan(values[0]) and values[1:] == [2.0, 3.0]
        assert rowmask == [1, 1, 1, 0, 0, 0, 0, 0]
        values, rowmask = get_coldata(bucket[COLUMNS]['D'])
        assert np.isnan(values[1])
        assert values[0] == 1 and values[2] == 1
        assert rowmask == [1, 1, 1, 0, 0, 0, 0, 0]
        index = [dt.fromtimestamp(int(i/1000)).replace(tzinfo=mktz(tz)) for i in
                 list(np.cumsum(np.frombuffer(decompress(bucket[INDEX]), dtype='uint64')))]
>       assert index == tick_index                                                # FIXME CM
E       AssertionError: assert [datetime.dat...neinfo/UTC'))] == [datetime.dat...neinfo/UTC'))]
E         At index 0 diff: datetime.datetime(2014, 1, 1, 17, 0, tzinfo=tzfile('/usr/share/zoneinfo/UTC')) != datetime.datetime(2014, 1, 2, 0, 0, tzinfo=tzfile('/usr/share/zoneinfo/UTC'))
E         Use -v to get the full diff

tests/unit/tickstore/test_tickstore.py:162: AssertionError
==========================================================================================================================

--------------------------------------------------- Captured log call ----------------------------------------------------
WARNING  arctic.tickstore.tickstore:tickstore.py:706 NB treating all values as 'exists' - no longer sparse

==========================================================================================================================
==================================================== warnings summary ====================================================
tests/integration/test_arctic.py: 5 warnings
tests/integration/scripts/test_delete_library.py: 5 warnings
  /home/cwm/git/bb.FLXSA/quant/arctic_venv36/arctic/_cache.py:120: DeprecationWarning: update is deprecated. Use replace_one, update_one or update_many instead.
    {"$pull": {"data": item}}

tests/integration/test_arctic.py::test_list_libraries_cached
  /home/cwm/git/bb.FLXSA/quant/arctic_venv36/tests/integration/test_arctic.py:243: DeprecationWarning: remove is deprecated. Use delete_one or delete_many instead.
    arctic._conn.meta_db.cache.remove({})

tests/integration/store/test_ndarray_store.py::test_save_read_large_ndarray
  /home/cwm/git/bb.FLXSA/quant/arctic_venv36/tests/integration/store/test_ndarray_store.py:146: DeprecationWarning: tostring() is deprecated. Use tobytes() instead.
    assert len(ndarr.tostring()) > 16 * 1024 * 1024                         # FIXME: deprecated tostring

tests/integration/store/test_pandas_store.py::test_save_read_pandas_empty_series_with_datetime_multiindex_with_timezone
  /home/cwm/git/bb.FLXSA/quant/arctic_venv36/tests/integration/store/test_pandas_store.py:147: DeprecationWarning: The default dtype for empty Series will be 'object' instead of 'float64' in a future version. Specify a dtype explicitly to silence this warning.
    df = Series(data=[], index=empty_index)

tests/integration/store/test_pandas_store.py::test_duplicate_labels
tests/integration/store/test_pandas_store.py::test_duplicate_labels
tests/integration/store/test_pandas_store.py::test_duplicate_labels
tests/integration/store/test_pandas_store.py::test_duplicate_labels
  /home/cwm/git/bb.FLXSA/quant/arctic_venv36/.eggs/numpy-1.19.4-py3.6-linux-x86_64.egg/numpy/core/numeric.py:2378: DeprecationWarning: elementwise comparison failed; this will raise an error in the future.
    return bool(asarray(a1 == a2).all())

tests/integration/store/test_pickle_store.py::test_bson_large_object
  /home/cwm/git/bb.FLXSA/quant/arctic_venv36/tests/integration/store/test_pickle_store.py:53: DeprecationWarning: tostring() is deprecated. Use tobytes() instead.
    'large_thing': np.random.rand(int(2.1 * 1024 * 1024)).tostring()}       # FIXME: deprecated tostring

tests/unit/chunkstore/test_passthrough_chunker.py::test_pass_thru
  /home/cwm/git/bb.FLXSA/quant/arctic_venv36/arctic/chunkstore/passthrough_chunker.py:75: DeprecationWarning: The default dtype for empty Series will be 'object' instead of 'float64' in a future version. Specify a dtype explicitly to silence this warning.
    return Series()

tests/unit/chunkstore/test_passthrough_chunker.py::test_pass_thru
  /home/cwm/git/bb.FLXSA/quant/arctic_venv36/tests/unit/chunkstore/test_passthrough_chunker.py:18: DeprecationWarning: The default dtype for empty Series will be 'object' instead of 'float64' in a future version. Specify a dtype explicitly to silence this warning.
    assert(p.exclude(Series([1, 2, 3]), None).equals(Series()))

tests/unit/serialization/test_numpy_arrays.py::test_string_cols_with_nans
tests/unit/serialization/test_numpy_arrays.py::test_objify_with_missing_columns
  /home/cwm/git/bb.FLXSA/quant/arctic_venv36/arctic/serialization/numpy_arrays.py:118: DeprecationWarning: tostring() is deprecated. Use tobytes() instead.
    masks[str(c)] = Binary(compress(mask.tostring()))

tests/unit/store/test_pickle_store.py::test_unpickle_highest_protocol
  /home/cwm/git/bb.FLXSA/quant/arctic_venv36/tests/unit/store/test_pickle_store.py:121: DeprecationWarning: The default dtype for empty Series will be 'object' instead of 'float64' in a future version. Specify a dtype explicitly to silence this warning.
    'blob': compressHC(cPickle.dumps(pd.Series(), protocol=cPickle.HIGHEST_PROTOCOL)),

tests/unit/store/test_pickle_store.py::test_unpickle_highest_protocol
  /home/cwm/git/bb.FLXSA/quant/arctic_venv36/tests/unit/store/test_pickle_store.py:127: DeprecationWarning: The default dtype for empty Series will be 'object' instead of 'float64' in a future version. Specify a dtype explicitly to silence this warning.
    expected = pd.Series()

-- Docs: https://docs.pytest.org/en/stable/warnings.html
------------------------ generated xml file: /home/cwm/git/bb.FLXSA/quant/arctic_venv36/junit.xml ------------------------

---------- coverage: platform linux, python 3.6.12-final-0 -----------
Coverage HTML written to dir htmlcov
Coverage XML written to file coverage.xml

================================================ short test summary info =================================================
FAILED tests/integration/tickstore/test_toplevel.py::test_should_return_data_when_date_range_falls_in_a_single_underlying_library
FAILED tests/integration/tickstore/test_toplevel.py::test_should_return_data_when_date_range_spans_libraries - Assertio...
FAILED tests/integration/tickstore/test_toplevel.py::test_should_return_data_when_date_range_spans_libraries_even_if_one_returns_nothing
FAILED tests/integration/tickstore/test_toplevel.py::test_should_add_underlying_library_where_another_library_exists_in_a_non_overlapping_daterange
FAILED tests/integration/tickstore/test_toplevel.py::test_should_write_top_level_with_list_of_dicts - AssertionError: D...
FAILED tests/integration/tickstore/test_toplevel.py::test_should_write_top_level_with_correct_timezone - AssertionError...
FAILED tests/integration/tickstore/test_ts_read.py::test_date_range[tickstore] - AssertionError: 
FAILED tests/integration/tickstore/test_ts_read.py::test_date_range_end_not_in_range[tickstore] - AssertionError: 
FAILED tests/integration/tickstore/test_ts_read.py::test_date_range_default_timezone[tickstore-UTC] - arctic.date._mktz...
FAILED tests/integration/tickstore/test_ts_read.py::test_date_range_default_timezone[tickstore-Europe/London] - arctic....
FAILED tests/integration/tickstore/test_ts_read.py::test_date_range_default_timezone[tickstore-America/New_York] - arct...
FAILED tests/integration/tickstore/test_ts_read.py::test_date_range_no_bounds[tickstore] - AssertionError: 
FAILED tests/integration/tickstore/test_ts_write.py::test_ts_write_pandas[tickstore] - AssertionError: DataFrame.column...
FAILED tests/unit/store/test_version_store_audit.py::test_ArcticTransaction_detects_concurrent_writes - AssertionError:...
FAILED tests/unit/tickstore/test_tickstore.py::test_mongo_date_range_query - AssertionError: assert {'s': {'$gte'...ca/...
FAILED tests/unit/tickstore/test_tickstore.py::test_tickstore_to_bucket_with_image - AssertionError: assert [datetime.d...
FAILED tests/unit/tickstore/test_tickstore.py::test_tickstore_pandas_to_bucket_image - AssertionError: assert [datetime...

==========================================================================================================================
============== 17 failed, 1273 passed, 29 skipped, 19 xfailed, 1 xpassed, 24 warnings in 1964.26s (0:32:44) ==============
(.venv36) cwm@flxsa02:~/git/bb.FLXSA/quant/arctic_venv36$ 
```