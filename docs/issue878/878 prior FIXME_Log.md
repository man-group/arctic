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

### FIXME: CM#011 - ()

### FIXME: CM#012 - ()

### FIXME: CM#013 - ()

### FIXME: CM#014 - ()

### FIXME: CM#015 - ()

```powershell

(.venv36) cwm@flxsa02:~/git/bb.FLXSA/quant/arctic_venv36$ python setup.py develop test
running develop
running egg_info
writing arctic.egg-info/PKG-INFO
writing dependency_links to arctic.egg-info/dependency_links.txt
writing entry points to arctic.egg-info/entry_points.txt
writing requirements to arctic.egg-info/requires.txt
writing top-level names to arctic.egg-info/top_level.txt
writing manifest file 'arctic.egg-info/SOURCES.txt'
running build_ext
Creating /home/cwm/git/bb.FLXSA/quant/arctic_venv36/.venv36/lib/python3.6/site-packages/arctic.egg-link (link to .)
arctic 1.80.0 is already the active version in easy-install.pth
Installing arctic_copy_data script to /home/cwm/git/bb.FLXSA/quant/arctic_venv36/.venv36/bin
Installing arctic_create_user script to /home/cwm/git/bb.FLXSA/quant/arctic_venv36/.venv36/bin
Installing arctic_delete_library script to /home/cwm/git/bb.FLXSA/quant/arctic_venv36/.venv36/bin
Installing arctic_enable_sharding script to /home/cwm/git/bb.FLXSA/quant/arctic_venv36/.venv36/bin
Installing arctic_fsck script to /home/cwm/git/bb.FLXSA/quant/arctic_venv36/.venv36/bin
Installing arctic_init_library script to /home/cwm/git/bb.FLXSA/quant/arctic_venv36/.venv36/bin
Installing arctic_list_libraries script to /home/cwm/git/bb.FLXSA/quant/arctic_venv36/.venv36/bin
Installing arctic_prune_versions script to /home/cwm/git/bb.FLXSA/quant/arctic_venv36/.venv36/bin

Installed /home/cwm/git/bb.FLXSA/quant/arctic_venv36
Processing dependencies for arctic==1.80.0
Searching for lz4==3.1.1
Best match: lz4 3.1.1
Processing lz4-3.1.1-py3.6-linux-x86_64.egg
lz4 3.1.1 is already the active version in easy-install.pth

Using /home/cwm/git/bb.FLXSA/quant/arctic_venv36/.venv36/lib/python3.6/site-packages/lz4-3.1.1-py3.6-linux-x86_64.egg
Searching for tzlocal==2.1
Best match: tzlocal 2.1
Processing tzlocal-2.1-py3.6.egg
tzlocal 2.1 is already the active version in easy-install.pth

Using /home/cwm/git/bb.FLXSA/quant/arctic_venv36/.venv36/lib/python3.6/site-packages/tzlocal-2.1-py3.6.egg
Searching for pytz==2020.4
Best match: pytz 2020.4
Processing pytz-2020.4-py3.6.egg
pytz 2020.4 is already the active version in easy-install.pth

Using /home/cwm/git/bb.FLXSA/quant/arctic_venv36/.venv36/lib/python3.6/site-packages/pytz-2020.4-py3.6.egg
Searching for python-dateutil==2.8.1
Best match: python-dateutil 2.8.1
Adding python-dateutil 2.8.1 to easy-install.pth file

Using /home/cwm/git/bb.FLXSA/quant/arctic_venv36/.venv36/lib/python3.6/site-packages
Searching for pymongo==3.11.2
Best match: pymongo 3.11.2
Processing pymongo-3.11.2-py3.6-linux-x86_64.egg
pymongo 3.11.2 is already the active version in easy-install.pth

Using /home/cwm/git/bb.FLXSA/quant/arctic_venv36/.venv36/lib/python3.6/site-packages/pymongo-3.11.2-py3.6-linux-x86_64.egg
Searching for pandas==1.1.5
Best match: pandas 1.1.5
Processing pandas-1.1.5-py3.6-linux-x86_64.egg
pandas 1.1.5 is already the active version in easy-install.pth

Using /home/cwm/git/bb.FLXSA/quant/arctic_venv36/.venv36/lib/python3.6/site-packages/pandas-1.1.5-py3.6-linux-x86_64.egg
Searching for mockextras==1.0.2
Best match: mockextras 1.0.2
Processing mockextras-1.0.2-py3.6.egg
mockextras 1.0.2 is already the active version in easy-install.pth

Using /home/cwm/git/bb.FLXSA/quant/arctic_venv36/.venv36/lib/python3.6/site-packages/mockextras-1.0.2-py3.6.egg
Searching for enum-compat==0.0.3
Best match: enum-compat 0.0.3
Processing enum_compat-0.0.3-py3.6.egg
enum-compat 0.0.3 is already the active version in easy-install.pth

Using /home/cwm/git/bb.FLXSA/quant/arctic_venv36/.venv36/lib/python3.6/site-packages/enum_compat-0.0.3-py3.6.egg
Searching for decorator==4.4.2
Best match: decorator 4.4.2
Adding decorator 4.4.2 to easy-install.pth file

Using /home/cwm/git/bb.FLXSA/quant/arctic_venv36/.venv36/lib/python3.6/site-packages
Searching for six==1.15.0
Best match: six 1.15.0
Adding six 1.15.0 to easy-install.pth file

Using /home/cwm/git/bb.FLXSA/quant/arctic_venv36/.venv36/lib/python3.6/site-packages
Searching for numpy==1.19.4
Best match: numpy 1.19.4
Processing numpy-1.19.4-py3.6-linux-x86_64.egg
numpy 1.19.4 is already the active version in easy-install.pth
Installing f2py script to /home/cwm/git/bb.FLXSA/quant/arctic_venv36/.venv36/bin
Installing f2py3 script to /home/cwm/git/bb.FLXSA/quant/arctic_venv36/.venv36/bin
Installing f2py3.6 script to /home/cwm/git/bb.FLXSA/quant/arctic_venv36/.venv36/bin

Using /home/cwm/git/bb.FLXSA/quant/arctic_venv36/.eggs/numpy-1.19.4-py3.6-linux-x86_64.egg
Finished processing dependencies for arctic==1.80.0
running test
WARNING: Testing via this command is deprecated and will be removed in a future version. Users looking for a generic test entry point independent of test runner are encouraged to use tox.
running build_ext



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
------------------------------------------------- Captured stdout setup --------------------------------------------------
{"t":{"$date":"2020-12-25T22:52:48.115-07:00"},"s":"I",  "c":"CONTROL",  "id":23285,   "ctx":"main","msg":"Automatically disabling TLS 1.0, to force-enable TLS 1.0 specify --sslDisabledProtocols 'none'"}
{"t":{"$date":"2020-12-25T22:52:48.117-07:00"},"s":"W",  "c":"ASIO",     "id":22601,   "ctx":"main","msg":"No TransportLayer configured during NetworkInterface startup"}
{"t":{"$date":"2020-12-25T22:52:48.117-07:00"},"s":"I",  "c":"NETWORK",  "id":4648601, "ctx":"main","msg":"Implicit TCP FastOpen unavailable. If TCP FastOpen is required, set tcpFastOpenServer, tcpFastOpenClient, and tcpFastOpenQueueSize."}
{"t":{"$date":"2020-12-25T22:52:48.118-07:00"},"s":"I",  "c":"STORAGE",  "id":4615611, "ctx":"initandlisten","msg":"MongoDB starting","attr":{"pid":3663,"port":5631,"dbPath":"/tmp/tmp4w17xckk","architecture":"64-bit","host":"flxsa02"}}
{"t":{"$date":"2020-12-25T22:52:48.118-07:00"},"s":"I",  "c":"CONTROL",  "id":23403,   "ctx":"initandlisten","msg":"Build Info","attr":{"buildInfo":{"version":"4.4.2","gitVersion":"15e73dc5738d2278b688f8929aee605fe4279b0e","openSSLVersion":"OpenSSL 1.0.2g  1 Mar 2016","modules":[],"allocator":"tcmalloc","environment":{"distmod":"ubuntu1604","distarch":"x86_64","target_arch":"x86_64"}}}}
{"t":{"$date":"2020-12-25T22:52:48.118-07:00"},"s":"I",  "c":"CONTROL",  "id":51765,   "ctx":"initandlisten","msg":"Operating System","attr":{"os":{"name":"Ubuntu","version":"16.04"}}}
{"t":{"$date":"2020-12-25T22:52:48.118-07:00"},"s":"I",  "c":"CONTROL",  "id":21951,   "ctx":"initandlisten","msg":"Options set by command line","attr":{"options":{"net":{"bindIp":"127.150.242.244","port":5631,"unixDomainSocket":{"enabled":false}},"storage":{"dbPath":"/tmp/tmp4w17xckk","journal":{"enabled":false},"syncPeriodSecs":0.0},"systemLog":{"quiet":true}}}}
{"t":{"$date":"2020-12-25T22:52:48.118-07:00"},"s":"I",  "c":"STORAGE",  "id":22297,   "ctx":"initandlisten","msg":"Using the XFS filesystem is strongly recommended with the WiredTiger storage engine. See http://dochub.mongodb.org/core/prodnotes-filesystem","tags":["startupWarnings"]}
{"t":{"$date":"2020-12-25T22:52:48.118-07:00"},"s":"I",  "c":"STORAGE",  "id":22315,   "ctx":"initandlisten","msg":"Opening WiredTiger","attr":{"config":"create,cache_size=11497M,session_max=33000,eviction=(threads_min=4,threads_max=4),config_base=false,statistics=(fast),log=(enabled=true,archive=true,path=journal,compressor=snappy),file_manager=(close_idle_time=100000,close_scan_interval=10,close_handle_minimum=250),statistics_log=(wait=0),verbose=[recovery_progress,checkpoint_progress,compact_progress],,log=(enabled=false),"}}
{"t":{"$date":"2020-12-25T22:52:48.654-07:00"},"s":"I",  "c":"STORAGE",  "id":22430,   "ctx":"initandlisten","msg":"WiredTiger message","attr":{"message":"[1608961968:654760][3663:0x7ff3e17afa80], txn-recover: [WT_VERB_RECOVERY | WT_VERB_RECOVERY_PROGRESS] Set global recovery timestamp: (0, 0)"}}
{"t":{"$date":"2020-12-25T22:52:48.654-07:00"},"s":"I",  "c":"STORAGE",  "id":22430,   "ctx":"initandlisten","msg":"WiredTiger message","attr":{"message":"[1608961968:654816][3663:0x7ff3e17afa80], txn-recover: [WT_VERB_RECOVERY | WT_VERB_RECOVERY_PROGRESS] Set global oldest timestamp: (0, 0)"}}
{"t":{"$date":"2020-12-25T22:52:48.700-07:00"},"s":"I",  "c":"STORAGE",  "id":4795906, "ctx":"initandlisten","msg":"WiredTiger opened","attr":{"durationMillis":582}}
{"t":{"$date":"2020-12-25T22:52:48.700-07:00"},"s":"I",  "c":"RECOVERY", "id":23987,   "ctx":"initandlisten","msg":"WiredTiger recoveryTimestamp","attr":{"recoveryTimestamp":{"$timestamp":{"t":0,"i":0}}}}
{"t":{"$date":"2020-12-25T22:52:48.761-07:00"},"s":"I",  "c":"STORAGE",  "id":4366408, "ctx":"initandlisten","msg":"No table logging settings modifications are required for existing WiredTiger tables","attr":{"loggingEnabled":true}}
{"t":{"$date":"2020-12-25T22:52:48.761-07:00"},"s":"I",  "c":"STORAGE",  "id":22262,   "ctx":"initandlisten","msg":"Timestamp monitor starting"}
{"t":{"$date":"2020-12-25T22:52:48.781-07:00"},"s":"W",  "c":"CONTROL",  "id":22120,   "ctx":"initandlisten","msg":"Access control is not enabled for the database. Read and write access to data and configuration is unrestricted","tags":["startupWarnings"]}
{"t":{"$date":"2020-12-25T22:52:48.781-07:00"},"s":"W",  "c":"CONTROL",  "id":22184,   "ctx":"initandlisten","msg":"Soft rlimits too low","attr":{"currentValue":1024,"recommendedMinimum":64000},"tags":["startupWarnings"]}
{"t":{"$date":"2020-12-25T22:52:48.781-07:00"},"s":"I",  "c":"STORAGE",  "id":20320,   "ctx":"initandlisten","msg":"createCollection","attr":{"namespace":"admin.system.version","uuidDisposition":"provided","uuid":{"uuid":{"$uuid":"83bfef33-df5f-4053-8f87-118c7045f122"}},"options":{"uuid":{"$uuid":"83bfef33-df5f-4053-8f87-118c7045f122"}}}}
{"t":{"$date":"2020-12-25T22:52:48.844-07:00"},"s":"I",  "c":"INDEX",    "id":20345,   "ctx":"initandlisten","msg":"Index build: done building","attr":{"buildUUID":null,"namespace":"admin.system.version","index":"_id_","commitTimestamp":{"$timestamp":{"t":0,"i":0}}}}
{"t":{"$date":"2020-12-25T22:52:48.844-07:00"},"s":"I",  "c":"COMMAND",  "id":20459,   "ctx":"initandlisten","msg":"Setting featureCompatibilityVersion","attr":{"newVersion":"4.4"}}
{"t":{"$date":"2020-12-25T22:52:48.844-07:00"},"s":"I",  "c":"STORAGE",  "id":20536,   "ctx":"initandlisten","msg":"Flow Control is enabled on this deployment"}
{"t":{"$date":"2020-12-25T22:52:48.845-07:00"},"s":"I",  "c":"STORAGE",  "id":20320,   "ctx":"initandlisten","msg":"createCollection","attr":{"namespace":"local.startup_log","uuidDisposition":"generated","uuid":{"uuid":{"$uuid":"a17e825c-5c8d-4940-a48c-615546243830"}},"options":{"capped":true,"size":10485760}}}
{"t":{"$date":"2020-12-25T22:52:48.906-07:00"},"s":"I",  "c":"INDEX",    "id":20345,   "ctx":"initandlisten","msg":"Index build: done building","attr":{"buildUUID":null,"namespace":"local.startup_log","index":"_id_","commitTimestamp":{"$timestamp":{"t":0,"i":0}}}}
{"t":{"$date":"2020-12-25T22:52:48.906-07:00"},"s":"I",  "c":"FTDC",     "id":20625,   "ctx":"initandlisten","msg":"Initializing full-time diagnostic data capture","attr":{"dataDirectory":"/tmp/tmp4w17xckk/diagnostic.data"}}
{"t":{"$date":"2020-12-25T22:52:48.907-07:00"},"s":"I",  "c":"NETWORK",  "id":23015,   "ctx":"listener","msg":"Listening on","attr":{"address":"127.150.242.244"}}
{"t":{"$date":"2020-12-25T22:52:48.907-07:00"},"s":"I",  "c":"CONTROL",  "id":20712,   "ctx":"LogicalSessionCacheReap","msg":"Sessions collection is not set up; waiting until next sessions reap interval","attr":{"error":"NamespaceNotFound: config.system.sessions does not exist"}}
{"t":{"$date":"2020-12-25T22:52:48.907-07:00"},"s":"I",  "c":"NETWORK",  "id":23016,   "ctx":"listener","msg":"Waiting for connections","attr":{"port":5631,"ssl":"off"}}
{"t":{"$date":"2020-12-25T22:52:48.907-07:00"},"s":"I",  "c":"STORAGE",  "id":20320,   "ctx":"LogicalSessionCacheRefresh","msg":"createCollection","attr":{"namespace":"config.system.sessions","uuidDisposition":"generated","uuid":{"uuid":{"$uuid":"83ef7a38-c428-46ad-b6b6-fd6198bcc4fc"}},"options":{}}}
{"t":{"$date":"2020-12-25T22:52:49.002-07:00"},"s":"I",  "c":"INDEX",    "id":20345,   "ctx":"LogicalSessionCacheRefresh","msg":"Index build: done building","attr":{"buildUUID":null,"namespace":"config.system.sessions","index":"_id_","commitTimestamp":{"$timestamp":{"t":0,"i":0}}}}
{"t":{"$date":"2020-12-25T22:52:49.002-07:00"},"s":"I",  "c":"INDEX",    "id":20345,   "ctx":"LogicalSessionCacheRefresh","msg":"Index build: done building","attr":{"buildUUID":null,"namespace":"config.system.sessions","index":"lsidTTLIndex","commitTimestamp":{"$timestamp":{"t":0,"i":0}}}}
{"t":{"$date":"2020-12-25T22:52:49.194-07:00"},"s":"I",  "c":"NETWORK",  "id":51800,   "ctx":"conn1","msg":"client metadata","attr":{"remote":"127.0.0.1:50828","client":"conn1","doc":{"driver":{"name":"PyMongo","version":"3.11.2"},"os":{"type":"Linux","name":"Linux","architecture":"x86_64","version":"4.15.0-128-generic"},"platform":"CPython 3.6.12.final.0"}}}
{"t":{"$date":"2020-12-25T22:52:49.195-07:00"},"s":"I",  "c":"NETWORK",  "id":51800,   "ctx":"conn2","msg":"client metadata","attr":{"remote":"127.0.0.1:50830","client":"conn2","doc":{"driver":{"name":"PyMongo","version":"3.11.2"},"os":{"type":"Linux","name":"Linux","architecture":"x86_64","version":"4.15.0-128-generic"},"platform":"CPython 3.6.12.final.0"}}}
{"t":{"$date":"2020-12-25T22:52:49.299-07:00"},"s":"I",  "c":"NETWORK",  "id":51800,   "ctx":"conn3","msg":"client metadata","attr":{"remote":"127.0.0.1:50832","client":"conn3","doc":{"driver":{"name":"PyMongo","version":"3.11.2"},"os":{"type":"Linux","name":"Linux","architecture":"x86_64","version":"4.15.0-128-generic"},"platform":"CPython 3.6.12.final.0"}}}
{"t":{"$date":"2020-12-25T22:52:49.301-07:00"},"s":"I",  "c":"NETWORK",  "id":51800,   "ctx":"conn4","msg":"client metadata","attr":{"remote":"127.0.0.1:50834","client":"conn4","doc":{"driver":{"name":"PyMongo","version":"3.11.2"},"os":{"type":"Linux","name":"Linux","architecture":"x86_64","version":"4.15.0-128-generic"},"platform":"CPython 3.6.12.final.0"}}}
{"t":{"$date":"2020-12-25T22:52:49.301-07:00"},"s":"I",  "c":"NETWORK",  "id":51800,   "ctx":"conn5","msg":"client metadata","attr":{"remote":"127.0.0.1:50836","client":"conn5","doc":{"driver":{"name":"PyMongo","version":"3.11.2"},"os":{"type":"Linux","name":"Linux","architecture":"x86_64","version":"4.15.0-128-generic"},"platform":"CPython 3.6.12.final.0"}}}
{"t":{"$date":"2020-12-25T22:52:49.304-07:00"},"s":"I",  "c":"NETWORK",  "id":51800,   "ctx":"conn6","msg":"client metadata","attr":{"remote":"127.0.0.1:50838","client":"conn6","doc":{"driver":{"name":"PyMongo","version":"3.11.2"},"os":{"type":"Linux","name":"Linux","architecture":"x86_64","version":"4.15.0-128-generic"},"platform":"CPython 3.6.12.final.0"}}}
{"t":{"$date":"2020-12-25T22:52:49.306-07:00"},"s":"I",  "c":"NETWORK",  "id":51800,   "ctx":"conn7","msg":"client metadata","attr":{"remote":"127.0.0.1:50840","client":"conn7","doc":{"driver":{"name":"PyMongo","version":"3.11.2"},"os":{"type":"Linux","name":"Linux","architecture":"x86_64","version":"4.15.0-128-generic"},"platform":"CPython 3.6.12.final.0"}}}
{"t":{"$date":"2020-12-25T22:52:49.306-07:00"},"s":"I",  "c":"NETWORK",  "id":51800,   "ctx":"conn8","msg":"client metadata","attr":{"remote":"127.0.0.1:50842","client":"conn8","doc":{"driver":{"name":"PyMongo","version":"3.11.2"},"os":{"type":"Linux","name":"Linux","architecture":"x86_64","version":"4.15.0-128-generic"},"platform":"CPython 3.6.12.final.0"}}}
{"t":{"$date":"2020-12-25T22:52:49.308-07:00"},"s":"I",  "c":"STORAGE",  "id":20320,   "ctx":"conn8","msg":"createCollection","attr":{"namespace":"meta_db.cache","uuidDisposition":"generated","uuid":{"uuid":{"$uuid":"87f4b100-bed9-4099-9c12-ce8bb8bcee65"}},"options":{}}}
{"t":{"$date":"2020-12-25T22:52:49.375-07:00"},"s":"I",  "c":"INDEX",    "id":20345,   "ctx":"conn8","msg":"Index build: done building","attr":{"buildUUID":null,"namespace":"meta_db.cache","index":"_id_","commitTimestamp":{"$timestamp":{"t":0,"i":0}}}}
{"t":{"$date":"2020-12-25T22:52:49.376-07:00"},"s":"I",  "c":"INDEX",    "id":20438,   "ctx":"conn8","msg":"Index build: registering","attr":{"buildUUID":{"uuid":{"$uuid":"cd38d21e-424b-4722-92f2-f92afed929aa"}},"namespace":"meta_db.cache","collectionUUID":{"uuid":{"$uuid":"87f4b100-bed9-4099-9c12-ce8bb8bcee65"}},"indexes":1,"firstIndex":{"name":"date_1"}}}
{"t":{"$date":"2020-12-25T22:52:49.404-07:00"},"s":"I",  "c":"INDEX",    "id":20345,   "ctx":"conn8","msg":"Index build: done building","attr":{"buildUUID":null,"namespace":"meta_db.cache","index":"date_1","commitTimestamp":{"$timestamp":{"t":0,"i":0}}}}
{"t":{"$date":"2020-12-25T22:52:49.404-07:00"},"s":"I",  "c":"INDEX",    "id":20440,   "ctx":"conn8","msg":"Index build: waiting for index build to complete","attr":{"buildUUID":{"uuid":{"$uuid":"cd38d21e-424b-4722-92f2-f92afed929aa"}},"deadline":{"$date":{"$numberLong":"9223372036854775807"}}}}
{"t":{"$date":"2020-12-25T22:52:49.405-07:00"},"s":"I",  "c":"INDEX",    "id":20447,   "ctx":"conn8","msg":"Index build: completed","attr":{"buildUUID":{"uuid":{"$uuid":"cd38d21e-424b-4722-92f2-f92afed929aa"}}}}
{"t":{"$date":"2020-12-25T22:52:49.406-07:00"},"s":"I",  "c":"STORAGE",  "id":20320,   "ctx":"conn8","msg":"createCollection","attr":{"namespace":"arctic_test.toplevel_tickstore.ARCTIC","uuidDisposition":"generated","uuid":{"uuid":{"$uuid":"4e4a01d2-bdf1-4b6e-be95-7b32796943cc"}},"options":{}}}
{"t":{"$date":"2020-12-25T22:52:49.470-07:00"},"s":"I",  "c":"INDEX",    "id":20345,   "ctx":"conn8","msg":"Index build: done building","attr":{"buildUUID":null,"namespace":"arctic_test.toplevel_tickstore.ARCTIC","index":"_id_","commitTimestamp":{"$timestamp":{"t":0,"i":0}}}}
{"t":{"$date":"2020-12-25T22:52:49.473-07:00"},"s":"I",  "c":"STORAGE",  "id":20320,   "ctx":"conn8","msg":"createCollection","attr":{"namespace":"arctic_test.toplevel_tickstore","uuidDisposition":"generated","uuid":{"uuid":{"$uuid":"b47cf09e-4532-412a-825e-611102cf29fb"}},"options":{}}}
{"t":{"$date":"2020-12-25T22:52:49.590-07:00"},"s":"I",  "c":"INDEX",    "id":20345,   "ctx":"conn8","msg":"Index build: done building","attr":{"buildUUID":null,"namespace":"arctic_test.toplevel_tickstore","index":"_id_","commitTimestamp":{"$timestamp":{"t":0,"i":0}}}}
{"t":{"$date":"2020-12-25T22:52:49.590-07:00"},"s":"I",  "c":"INDEX",    "id":20345,   "ctx":"conn8","msg":"Index build: done building","attr":{"buildUUID":null,"namespace":"arctic_test.toplevel_tickstore","index":"start_1","commitTimestamp":{"$timestamp":{"t":0,"i":0}}}}
{"t":{"$date":"2020-12-25T22:52:49.590-07:00"},"s":"I",  "c":"COMMAND",  "id":51803,   "ctx":"conn8","msg":"Slow query","attr":{"type":"command","ns":"arctic_test.toplevel_tickstore","command":{"createIndexes":"toplevel_tickstore","indexes":[{"background":true,"name":"start_1","key":{"start":1}}],"lsid":{"id":{"$uuid":"4337d5da-2b4d-4425-a6ff-ea6f63bd3945"}},"$db":"arctic_test","$readPreference":{"mode":"primary"}},"numYields":0,"reslen":114,"locks":{"ParallelBatchWriterMode":{"acquireCount":{"r":5}},"ReplicationStateTransition":{"acquireCount":{"w":5}},"Global":{"acquireCount":{"r":2,"w":3}},"Database":{"acquireCount":{"r":2,"w":3}},"Collection":{"acquireCount":{"r":4,"w":2}},"Mutex":{"acquireCount":{"r":5}}},"flowControl":{"acquireCount":1},"storage":{},"protocol":"op_msg","durationMillis":116}}
--------------------------------------------------- Captured log setup ---------------------------------------------------
DEBUG    pytest_shutil.workspace:workspace.py:52 
DEBUG    pytest_shutil.workspace:workspace.py:53 =======================================================
DEBUG    pytest_shutil.workspace:workspace.py:56 pytest_shutil created workspace /tmp/tmp4w17xckk
DEBUG    pytest_shutil.workspace:workspace.py:64 This workspace will delete itself on teardown
DEBUG    pytest_shutil.workspace:workspace.py:65 =======================================================
DEBUG    pytest_shutil.workspace:workspace.py:66 
DEBUG    pytest_server_fixtures.serverclass.thread:thread.py:77 Launching thread server.
DEBUG    pytest_server_fixtures.serverclass.thread:thread.py:89 Running server: mongod --bind_ip=127.150.242.244 --port=5631 --nounixsocket --syncdelay=0 --nojournal --quiet --dbpath=/tmp/tmp4w17xckk
DEBUG    pytest_server_fixtures.serverclass.thread:thread.py:90 CWD: /home/cwm/git/bb.FLXSA/quant/arctic_venv36
DEBUG    pytest_server_fixtures.base2:base2.py:226 sleeping for 0.1 before retrying (1 of 28)
INFO     pytest_server_fixtures.mongo:mongo.py:128 Connecting to Mongo at 127.150.242.244:5631
DEBUG    pytest_server_fixtures.base2:base2.py:226 sleeping for 0.1 before retrying (2 of 28)
INFO     pytest_server_fixtures.mongo:mongo.py:128 Connecting to Mongo at 127.150.242.244:5631
DEBUG    pytest_server_fixtures.base2:base2.py:226 sleeping for 0.1 before retrying (3 of 28)
INFO     pytest_server_fixtures.mongo:mongo.py:128 Connecting to Mongo at 127.150.242.244:5631
DEBUG    pytest_server_fixtures.base2:base2.py:229 waited 0:00:01.218457 for server to start successfully
DEBUG    pytest_server_fixtures.base2:base2.py:69 Server now awake
INFO     arctic.fixtures.arctic:arctic.py:23 arctic.fixtures: arctic init(mongo_server.api=MongoClient(host=['127.150.242.244:5631'], document_class=dict, tz_aware=False, connect=True))
DEBUG    root:arctic.py:234 Cache has expired data, fetching from slow path and reloading cache.
-------------------------------------------------- Captured stdout call --------------------------------------------------
{"t":{"$date":"2020-12-25T22:52:49.595-07:00"},"s":"I",  "c":"STORAGE",  "id":20320,   "ctx":"conn8","msg":"createCollection","attr":{"namespace":"arctic_FEED_2010.LEVEL1.ARCTIC","uuidDisposition":"generated","uuid":{"uuid":{"$uuid":"1eadfda2-9fc1-4165-a16f-472f70522d45"}},"options":{}}}
{"t":{"$date":"2020-12-25T22:52:49.658-07:00"},"s":"I",  "c":"INDEX",    "id":20345,   "ctx":"conn8","msg":"Index build: done building","attr":{"buildUUID":null,"namespace":"arctic_FEED_2010.LEVEL1.ARCTIC","index":"_id_","commitTimestamp":{"$timestamp":{"t":0,"i":0}}}}
{"t":{"$date":"2020-12-25T22:52:49.659-07:00"},"s":"I",  "c":"STORAGE",  "id":20320,   "ctx":"conn8","msg":"createCollection","attr":{"namespace":"arctic_FEED_2010.LEVEL1","uuidDisposition":"generated","uuid":{"uuid":{"$uuid":"9c5524b4-b5da-4f24-a546-a9a7e467ae52"}},"options":{}}}
{"t":{"$date":"2020-12-25T22:52:49.696-07:00"},"s":"I",  "c":"-",        "id":20883,   "ctx":"conn1","msg":"Interrupted operation as its client disconnected","attr":{"opId":15}}
{"t":{"$date":"2020-12-25T22:52:49.760-07:00"},"s":"I",  "c":"INDEX",    "id":20345,   "ctx":"conn8","msg":"Index build: done building","attr":{"buildUUID":null,"namespace":"arctic_FEED_2010.LEVEL1","index":"_id_","commitTimestamp":{"$timestamp":{"t":0,"i":0}}}}
{"t":{"$date":"2020-12-25T22:52:49.760-07:00"},"s":"I",  "c":"INDEX",    "id":20345,   "ctx":"conn8","msg":"Index build: done building","attr":{"buildUUID":null,"namespace":"arctic_FEED_2010.LEVEL1","index":"sy_1_s_1","commitTimestamp":{"$timestamp":{"t":0,"i":0}}}}
{"t":{"$date":"2020-12-25T22:52:49.760-07:00"},"s":"I",  "c":"COMMAND",  "id":51803,   "ctx":"conn8","msg":"Slow query","attr":{"type":"command","ns":"arctic_FEED_2010.LEVEL1","command":{"createIndexes":"LEVEL1","indexes":[{"background":true,"name":"sy_1_s_1","key":{"sy":1,"s":1}}],"lsid":{"id":{"$uuid":"4337d5da-2b4d-4425-a6ff-ea6f63bd3945"}},"$db":"arctic_FEED_2010","$readPreference":{"mode":"primary"}},"numYields":0,"reslen":114,"locks":{"ParallelBatchWriterMode":{"acquireCount":{"r":5}},"ReplicationStateTransition":{"acquireCount":{"w":5}},"Global":{"acquireCount":{"r":2,"w":3}},"Database":{"acquireCount":{"r":2,"w":3}},"Collection":{"acquireCount":{"r":4,"w":2}},"Mutex":{"acquireCount":{"r":5}}},"flowControl":{"acquireCount":1},"storage":{},"protocol":"op_msg","durationMillis":100}}
{"t":{"$date":"2020-12-25T22:52:49.761-07:00"},"s":"I",  "c":"INDEX",    "id":20438,   "ctx":"conn8","msg":"Index build: registering","attr":{"buildUUID":{"uuid":{"$uuid":"aa146d50-6fa8-4ee0-86e2-b4734ac49935"}},"namespace":"arctic_FEED_2010.LEVEL1","collectionUUID":{"uuid":{"$uuid":"9c5524b4-b5da-4f24-a546-a9a7e467ae52"}},"indexes":1,"firstIndex":{"name":"s_1"}}}
{"t":{"$date":"2020-12-25T22:52:49.785-07:00"},"s":"I",  "c":"INDEX",    "id":20345,   "ctx":"conn8","msg":"Index build: done building","attr":{"buildUUID":null,"namespace":"arctic_FEED_2010.LEVEL1","index":"s_1","commitTimestamp":{"$timestamp":{"t":0,"i":0}}}}
{"t":{"$date":"2020-12-25T22:52:49.785-07:00"},"s":"I",  "c":"INDEX",    "id":20440,   "ctx":"conn8","msg":"Index build: waiting for index build to complete","attr":{"buildUUID":{"uuid":{"$uuid":"aa146d50-6fa8-4ee0-86e2-b4734ac49935"}},"deadline":{"$date":{"$numberLong":"9223372036854775807"}}}}
{"t":{"$date":"2020-12-25T22:52:49.785-07:00"},"s":"I",  "c":"INDEX",    "id":20447,   "ctx":"conn8","msg":"Index build: completed","attr":{"buildUUID":{"uuid":{"$uuid":"aa146d50-6fa8-4ee0-86e2-b4734ac49935"}}}}
{"t":{"$date":"2020-12-25T22:52:49.786-07:00"},"s":"I",  "c":"STORAGE",  "id":20320,   "ctx":"conn8","msg":"createCollection","attr":{"namespace":"arctic_FEED_2010.LEVEL1.metadata","uuidDisposition":"generated","uuid":{"uuid":{"$uuid":"03b48bef-1419-4732-a6ae-7c19971a5dae"}},"options":{}}}
{"t":{"$date":"2020-12-25T22:52:49.801-07:00"},"s":"I",  "c":"-",        "id":20883,   "ctx":"conn3","msg":"Interrupted operation as its client disconnected","attr":{"opId":18}}
{"t":{"$date":"2020-12-25T22:52:49.878-07:00"},"s":"I",  "c":"INDEX",    "id":20345,   "ctx":"conn8","msg":"Index build: done building","attr":{"buildUUID":null,"namespace":"arctic_FEED_2010.LEVEL1.metadata","index":"_id_","commitTimestamp":{"$timestamp":{"t":0,"i":0}}}}
{"t":{"$date":"2020-12-25T22:52:49.878-07:00"},"s":"I",  "c":"INDEX",    "id":20345,   "ctx":"conn8","msg":"Index build: done building","attr":{"buildUUID":null,"namespace":"arctic_FEED_2010.LEVEL1.metadata","index":"sy_1","commitTimestamp":{"$timestamp":{"t":0,"i":0}}}}
{"t":{"$date":"2020-12-25T22:52:49.882-07:00"},"s":"I",  "c":"STORAGE",  "id":20320,   "ctx":"conn8","msg":"createCollection","attr":{"namespace":"arctic_test_current.toplevel_tickstore.ARCTIC","uuidDisposition":"generated","uuid":{"uuid":{"$uuid":"2df851bf-4f2a-4590-96ab-ac92f3d6a986"}},"options":{}}}
{"t":{"$date":"2020-12-25T22:52:49.949-07:00"},"s":"I",  "c":"INDEX",    "id":20345,   "ctx":"conn8","msg":"Index build: done building","attr":{"buildUUID":null,"namespace":"arctic_test_current.toplevel_tickstore.ARCTIC","index":"_id_","commitTimestamp":{"$timestamp":{"t":0,"i":0}}}}
{"t":{"$date":"2020-12-25T22:52:49.950-07:00"},"s":"I",  "c":"STORAGE",  "id":20320,   "ctx":"conn8","msg":"createCollection","attr":{"namespace":"arctic_test_current.toplevel_tickstore","uuidDisposition":"generated","uuid":{"uuid":{"$uuid":"56e2189a-8cf2-4fb5-b7b3-0101837f806d"}},"options":{}}}
{"t":{"$date":"2020-12-25T22:52:50.044-07:00"},"s":"I",  "c":"INDEX",    "id":20345,   "ctx":"conn8","msg":"Index build: done building","attr":{"buildUUID":null,"namespace":"arctic_test_current.toplevel_tickstore","index":"_id_","commitTimestamp":{"$timestamp":{"t":0,"i":0}}}}
{"t":{"$date":"2020-12-25T22:52:50.044-07:00"},"s":"I",  "c":"INDEX",    "id":20345,   "ctx":"conn8","msg":"Index build: done building","attr":{"buildUUID":null,"namespace":"arctic_test_current.toplevel_tickstore","index":"sy_1_s_1","commitTimestamp":{"$timestamp":{"t":0,"i":0}}}}
{"t":{"$date":"2020-12-25T22:52:50.045-07:00"},"s":"I",  "c":"INDEX",    "id":20438,   "ctx":"conn8","msg":"Index build: registering","attr":{"buildUUID":{"uuid":{"$uuid":"fdd6f661-2f91-49c7-bc01-d400bb14f695"}},"namespace":"arctic_test_current.toplevel_tickstore","collectionUUID":{"uuid":{"$uuid":"56e2189a-8cf2-4fb5-b7b3-0101837f806d"}},"indexes":1,"firstIndex":{"name":"s_1"}}}
{"t":{"$date":"2020-12-25T22:52:50.073-07:00"},"s":"I",  "c":"INDEX",    "id":20345,   "ctx":"conn8","msg":"Index build: done building","attr":{"buildUUID":null,"namespace":"arctic_test_current.toplevel_tickstore","index":"s_1","commitTimestamp":{"$timestamp":{"t":0,"i":0}}}}
{"t":{"$date":"2020-12-25T22:52:50.073-07:00"},"s":"I",  "c":"INDEX",    "id":20440,   "ctx":"conn8","msg":"Index build: waiting for index build to complete","attr":{"buildUUID":{"uuid":{"$uuid":"fdd6f661-2f91-49c7-bc01-d400bb14f695"}},"deadline":{"$date":{"$numberLong":"9223372036854775807"}}}}
{"t":{"$date":"2020-12-25T22:52:50.073-07:00"},"s":"I",  "c":"INDEX",    "id":20447,   "ctx":"conn8","msg":"Index build: completed","attr":{"buildUUID":{"uuid":{"$uuid":"fdd6f661-2f91-49c7-bc01-d400bb14f695"}}}}
{"t":{"$date":"2020-12-25T22:52:50.074-07:00"},"s":"I",  "c":"STORAGE",  "id":20320,   "ctx":"conn8","msg":"createCollection","attr":{"namespace":"arctic_test_current.toplevel_tickstore.metadata","uuidDisposition":"generated","uuid":{"uuid":{"$uuid":"5e1034de-d873-4cad-bad7-7cfa5ed44397"}},"options":{}}}
{"t":{"$date":"2020-12-25T22:52:50.159-07:00"},"s":"I",  "c":"INDEX",    "id":20345,   "ctx":"conn8","msg":"Index build: done building","attr":{"buildUUID":null,"namespace":"arctic_test_current.toplevel_tickstore.metadata","index":"_id_","commitTimestamp":{"$timestamp":{"t":0,"i":0}}}}
{"t":{"$date":"2020-12-25T22:52:50.159-07:00"},"s":"I",  "c":"INDEX",    "id":20345,   "ctx":"conn8","msg":"Index build: done building","attr":{"buildUUID":null,"namespace":"arctic_test_current.toplevel_tickstore.metadata","index":"sy_1","commitTimestamp":{"$timestamp":{"t":0,"i":0}}}}
--------------------------------------------------- Captured log call ----------------------------------------------------
WARNING  arctic.tickstore.tickstore:tickstore.py:706 NB treating all values as 'exists' - no longer sparse
DEBUG    arctic.tickstore.tickstore:tickstore.py:612 1 buckets in 0.000834: approx 119904076 ticks/sec
WARNING  arctic.tickstore.tickstore:tickstore.py:706 NB treating all values as 'exists' - no longer sparse
DEBUG    arctic.tickstore.tickstore:tickstore.py:612 1 buckets in 0.000736: approx 135869565 ticks/sec
INFO     arctic.tickstore.tickstore:tickstore.py:355 Got data in 0.003931 secs, creating DataFrame...
INFO     arctic.tickstore.tickstore:tickstore.py:364 6 rows in 0.005082 secs: 1180 ticks/sec
------------------------------------------------- Captured log teardown --------------------------------------------------
DEBUG    pytest_server_fixtures.serverclass.thread:thread.py:54 Killing process tree for 3663 (total_procs_to_kill=1)
DEBUG    pytest_server_fixtures.serverclass.thread:thread.py:35 Killing 1 processes with signal Signals.SIGKILL
DEBUG    pytest_server_fixtures.serverclass.thread:thread.py:39 Waiting for 1 processes to die
DEBUG    pytest_server_fixtures.serverclass.thread:thread.py:43 All processes are terminated
DEBUG    pytest_shutil.workspace:workspace.py:140 
DEBUG    pytest_shutil.workspace:workspace.py:141 =======================================================
DEBUG    pytest_shutil.workspace:workspace.py:142 pytest_shutil deleting workspace /tmp/tmp4w17xckk
DEBUG    pytest_shutil.workspace:workspace.py:143 =======================================================
DEBUG    pytest_shutil.workspace:workspace.py:144
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
------------------------------------------------- Captured stdout setup --------------------------------------------------
{"t":{"$date":"2020-12-25T22:52:50.301-07:00"},"s":"I",  "c":"CONTROL",  "id":23285,   "ctx":"main","msg":"Automatically disabling TLS 1.0, to force-enable TLS 1.0 specify --sslDisabledProtocols 'none'"}
{"t":{"$date":"2020-12-25T22:52:50.302-07:00"},"s":"W",  "c":"ASIO",     "id":22601,   "ctx":"main","msg":"No TransportLayer configured during NetworkInterface startup"}
{"t":{"$date":"2020-12-25T22:52:50.302-07:00"},"s":"I",  "c":"NETWORK",  "id":4648601, "ctx":"main","msg":"Implicit TCP FastOpen unavailable. If TCP FastOpen is required, set tcpFastOpenServer, tcpFastOpenClient, and tcpFastOpenQueueSize."}
{"t":{"$date":"2020-12-25T22:52:50.302-07:00"},"s":"I",  "c":"STORAGE",  "id":4615611, "ctx":"initandlisten","msg":"MongoDB starting","attr":{"pid":3720,"port":25863,"dbPath":"/tmp/tmpi3afyecs","architecture":"64-bit","host":"flxsa02"}}
{"t":{"$date":"2020-12-25T22:52:50.302-07:00"},"s":"I",  "c":"CONTROL",  "id":23403,   "ctx":"initandlisten","msg":"Build Info","attr":{"buildInfo":{"version":"4.4.2","gitVersion":"15e73dc5738d2278b688f8929aee605fe4279b0e","openSSLVersion":"OpenSSL 1.0.2g  1 Mar 2016","modules":[],"allocator":"tcmalloc","environment":{"distmod":"ubuntu1604","distarch":"x86_64","target_arch":"x86_64"}}}}
{"t":{"$date":"2020-12-25T22:52:50.302-07:00"},"s":"I",  "c":"CONTROL",  "id":51765,   "ctx":"initandlisten","msg":"Operating System","attr":{"os":{"name":"Ubuntu","version":"16.04"}}}
{"t":{"$date":"2020-12-25T22:52:50.302-07:00"},"s":"I",  "c":"CONTROL",  "id":21951,   "ctx":"initandlisten","msg":"Options set by command line","attr":{"options":{"net":{"bindIp":"127.150.242.244","port":25863,"unixDomainSocket":{"enabled":false}},"storage":{"dbPath":"/tmp/tmpi3afyecs","journal":{"enabled":false},"syncPeriodSecs":0.0},"systemLog":{"quiet":true}}}}
{"t":{"$date":"2020-12-25T22:52:50.303-07:00"},"s":"I",  "c":"STORAGE",  "id":22297,   "ctx":"initandlisten","msg":"Using the XFS filesystem is strongly recommended with the WiredTiger storage engine. See http://dochub.mongodb.org/core/prodnotes-filesystem","tags":["startupWarnings"]}
{"t":{"$date":"2020-12-25T22:52:50.303-07:00"},"s":"I",  "c":"STORAGE",  "id":22315,   "ctx":"initandlisten","msg":"Opening WiredTiger","attr":{"config":"create,cache_size=11497M,session_max=33000,eviction=(threads_min=4,threads_max=4),config_base=false,statistics=(fast),log=(enabled=true,archive=true,path=journal,compressor=snappy),file_manager=(close_idle_time=100000,close_scan_interval=10,close_handle_minimum=250),statistics_log=(wait=0),verbose=[recovery_progress,checkpoint_progress,compact_progress],,log=(enabled=false),"}}
{"t":{"$date":"2020-12-25T22:52:50.834-07:00"},"s":"I",  "c":"STORAGE",  "id":22430,   "ctx":"initandlisten","msg":"WiredTiger message","attr":{"message":"[1608961970:834533][3720:0x7f5acb859a80], txn-recover: [WT_VERB_RECOVERY | WT_VERB_RECOVERY_PROGRESS] Set global recovery timestamp: (0, 0)"}}
{"t":{"$date":"2020-12-25T22:52:50.834-07:00"},"s":"I",  "c":"STORAGE",  "id":22430,   "ctx":"initandlisten","msg":"WiredTiger message","attr":{"message":"[1608961970:834589][3720:0x7f5acb859a80], txn-recover: [WT_VERB_RECOVERY | WT_VERB_RECOVERY_PROGRESS] Set global oldest timestamp: (0, 0)"}}
{"t":{"$date":"2020-12-25T22:52:50.878-07:00"},"s":"I",  "c":"STORAGE",  "id":4795906, "ctx":"initandlisten","msg":"WiredTiger opened","attr":{"durationMillis":575}}
{"t":{"$date":"2020-12-25T22:52:50.878-07:00"},"s":"I",  "c":"RECOVERY", "id":23987,   "ctx":"initandlisten","msg":"WiredTiger recoveryTimestamp","attr":{"recoveryTimestamp":{"$timestamp":{"t":0,"i":0}}}}
{"t":{"$date":"2020-12-25T22:52:50.937-07:00"},"s":"I",  "c":"STORAGE",  "id":4366408, "ctx":"initandlisten","msg":"No table logging settings modifications are required for existing WiredTiger tables","attr":{"loggingEnabled":true}}
{"t":{"$date":"2020-12-25T22:52:50.937-07:00"},"s":"I",  "c":"STORAGE",  "id":22262,   "ctx":"initandlisten","msg":"Timestamp monitor starting"}
{"t":{"$date":"2020-12-25T22:52:50.956-07:00"},"s":"W",  "c":"CONTROL",  "id":22120,   "ctx":"initandlisten","msg":"Access control is not enabled for the database. Read and write access to data and configuration is unrestricted","tags":["startupWarnings"]}
{"t":{"$date":"2020-12-25T22:52:50.956-07:00"},"s":"W",  "c":"CONTROL",  "id":22184,   "ctx":"initandlisten","msg":"Soft rlimits too low","attr":{"currentValue":1024,"recommendedMinimum":64000},"tags":["startupWarnings"]}
{"t":{"$date":"2020-12-25T22:52:50.956-07:00"},"s":"I",  "c":"STORAGE",  "id":20320,   "ctx":"initandlisten","msg":"createCollection","attr":{"namespace":"admin.system.version","uuidDisposition":"provided","uuid":{"uuid":{"$uuid":"85e71c58-885e-4d6f-b696-57e0e6db2fe7"}},"options":{"uuid":{"$uuid":"85e71c58-885e-4d6f-b696-57e0e6db2fe7"}}}}
{"t":{"$date":"2020-12-25T22:52:51.025-07:00"},"s":"I",  "c":"INDEX",    "id":20345,   "ctx":"initandlisten","msg":"Index build: done building","attr":{"buildUUID":null,"namespace":"admin.system.version","index":"_id_","commitTimestamp":{"$timestamp":{"t":0,"i":0}}}}
{"t":{"$date":"2020-12-25T22:52:51.025-07:00"},"s":"I",  "c":"COMMAND",  "id":20459,   "ctx":"initandlisten","msg":"Setting featureCompatibilityVersion","attr":{"newVersion":"4.4"}}
{"t":{"$date":"2020-12-25T22:52:51.025-07:00"},"s":"I",  "c":"STORAGE",  "id":20536,   "ctx":"initandlisten","msg":"Flow Control is enabled on this deployment"}
{"t":{"$date":"2020-12-25T22:52:51.026-07:00"},"s":"I",  "c":"STORAGE",  "id":20320,   "ctx":"initandlisten","msg":"createCollection","attr":{"namespace":"local.startup_log","uuidDisposition":"generated","uuid":{"uuid":{"$uuid":"d5c2cec1-0994-48df-b441-ba7f47f63a9c"}},"options":{"capped":true,"size":10485760}}}
{"t":{"$date":"2020-12-25T22:52:51.084-07:00"},"s":"I",  "c":"INDEX",    "id":20345,   "ctx":"initandlisten","msg":"Index build: done building","attr":{"buildUUID":null,"namespace":"local.startup_log","index":"_id_","commitTimestamp":{"$timestamp":{"t":0,"i":0}}}}
{"t":{"$date":"2020-12-25T22:52:51.084-07:00"},"s":"I",  "c":"FTDC",     "id":20625,   "ctx":"initandlisten","msg":"Initializing full-time diagnostic data capture","attr":{"dataDirectory":"/tmp/tmpi3afyecs/diagnostic.data"}}
{"t":{"$date":"2020-12-25T22:52:51.085-07:00"},"s":"I",  "c":"CONTROL",  "id":20712,   "ctx":"LogicalSessionCacheReap","msg":"Sessions collection is not set up; waiting until next sessions reap interval","attr":{"error":"NamespaceNotFound: config.system.sessions does not exist"}}
{"t":{"$date":"2020-12-25T22:52:51.085-07:00"},"s":"I",  "c":"NETWORK",  "id":23015,   "ctx":"listener","msg":"Listening on","attr":{"address":"127.150.242.244"}}
{"t":{"$date":"2020-12-25T22:52:51.085-07:00"},"s":"I",  "c":"NETWORK",  "id":23016,   "ctx":"listener","msg":"Waiting for connections","attr":{"port":25863,"ssl":"off"}}
{"t":{"$date":"2020-12-25T22:52:51.085-07:00"},"s":"I",  "c":"STORAGE",  "id":20320,   "ctx":"LogicalSessionCacheRefresh","msg":"createCollection","attr":{"namespace":"config.system.sessions","uuidDisposition":"generated","uuid":{"uuid":{"$uuid":"3308968a-0cc6-46e2-bf04-cb3722c56836"}},"options":{}}}
{"t":{"$date":"2020-12-25T22:52:51.176-07:00"},"s":"I",  "c":"INDEX",    "id":20345,   "ctx":"LogicalSessionCacheRefresh","msg":"Index build: done building","attr":{"buildUUID":null,"namespace":"config.system.sessions","index":"_id_","commitTimestamp":{"$timestamp":{"t":0,"i":0}}}}
{"t":{"$date":"2020-12-25T22:52:51.176-07:00"},"s":"I",  "c":"INDEX",    "id":20345,   "ctx":"LogicalSessionCacheRefresh","msg":"Index build: done building","attr":{"buildUUID":null,"namespace":"config.system.sessions","index":"lsidTTLIndex","commitTimestamp":{"$timestamp":{"t":0,"i":0}}}}
{"t":{"$date":"2020-12-25T22:52:51.375-07:00"},"s":"I",  "c":"NETWORK",  "id":51800,   "ctx":"conn1","msg":"client metadata","attr":{"remote":"127.0.0.1:52176","client":"conn1","doc":{"driver":{"name":"PyMongo","version":"3.11.2"},"os":{"type":"Linux","name":"Linux","architecture":"x86_64","version":"4.15.0-128-generic"},"platform":"CPython 3.6.12.final.0"}}}
{"t":{"$date":"2020-12-25T22:52:51.377-07:00"},"s":"I",  "c":"NETWORK",  "id":51800,   "ctx":"conn2","msg":"client metadata","attr":{"remote":"127.0.0.1:52178","client":"conn2","doc":{"driver":{"name":"PyMongo","version":"3.11.2"},"os":{"type":"Linux","name":"Linux","architecture":"x86_64","version":"4.15.0-128-generic"},"platform":"CPython 3.6.12.final.0"}}}
{"t":{"$date":"2020-12-25T22:52:51.478-07:00"},"s":"I",  "c":"NETWORK",  "id":51800,   "ctx":"conn3","msg":"client metadata","attr":{"remote":"127.0.0.1:52180","client":"conn3","doc":{"driver":{"name":"PyMongo","version":"3.11.2"},"os":{"type":"Linux","name":"Linux","architecture":"x86_64","version":"4.15.0-128-generic"},"platform":"CPython 3.6.12.final.0"}}}
{"t":{"$date":"2020-12-25T22:52:51.479-07:00"},"s":"I",  "c":"NETWORK",  "id":51800,   "ctx":"conn4","msg":"client metadata","attr":{"remote":"127.0.0.1:52182","client":"conn4","doc":{"driver":{"name":"PyMongo","version":"3.11.2"},"os":{"type":"Linux","name":"Linux","architecture":"x86_64","version":"4.15.0-128-generic"},"platform":"CPython 3.6.12.final.0"}}}
{"t":{"$date":"2020-12-25T22:52:51.480-07:00"},"s":"I",  "c":"NETWORK",  "id":51800,   "ctx":"conn5","msg":"client metadata","attr":{"remote":"127.0.0.1:52184","client":"conn5","doc":{"driver":{"name":"PyMongo","version":"3.11.2"},"os":{"type":"Linux","name":"Linux","architecture":"x86_64","version":"4.15.0-128-generic"},"platform":"CPython 3.6.12.final.0"}}}
{"t":{"$date":"2020-12-25T22:52:51.482-07:00"},"s":"I",  "c":"NETWORK",  "id":51800,   "ctx":"conn6","msg":"client metadata","attr":{"remote":"127.0.0.1:52186","client":"conn6","doc":{"driver":{"name":"PyMongo","version":"3.11.2"},"os":{"type":"Linux","name":"Linux","architecture":"x86_64","version":"4.15.0-128-generic"},"platform":"CPython 3.6.12.final.0"}}}
{"t":{"$date":"2020-12-25T22:52:51.485-07:00"},"s":"I",  "c":"NETWORK",  "id":51800,   "ctx":"conn7","msg":"client metadata","attr":{"remote":"127.0.0.1:52188","client":"conn7","doc":{"driver":{"name":"PyMongo","version":"3.11.2"},"os":{"type":"Linux","name":"Linux","architecture":"x86_64","version":"4.15.0-128-generic"},"platform":"CPython 3.6.12.final.0"}}}
{"t":{"$date":"2020-12-25T22:52:51.485-07:00"},"s":"I",  "c":"NETWORK",  "id":51800,   "ctx":"conn8","msg":"client metadata","attr":{"remote":"127.0.0.1:52190","client":"conn8","doc":{"driver":{"name":"PyMongo","version":"3.11.2"},"os":{"type":"Linux","name":"Linux","architecture":"x86_64","version":"4.15.0-128-generic"},"platform":"CPython 3.6.12.final.0"}}}
{"t":{"$date":"2020-12-25T22:52:51.489-07:00"},"s":"I",  "c":"STORAGE",  "id":20320,   "ctx":"conn8","msg":"createCollection","attr":{"namespace":"meta_db.cache","uuidDisposition":"generated","uuid":{"uuid":{"$uuid":"5ae6a461-a245-42f9-84fb-7e32b5b618bc"}},"options":{}}}
{"t":{"$date":"2020-12-25T22:52:51.556-07:00"},"s":"I",  "c":"INDEX",    "id":20345,   "ctx":"conn8","msg":"Index build: done building","attr":{"buildUUID":null,"namespace":"meta_db.cache","index":"_id_","commitTimestamp":{"$timestamp":{"t":0,"i":0}}}}
{"t":{"$date":"2020-12-25T22:52:51.557-07:00"},"s":"I",  "c":"INDEX",    "id":20438,   "ctx":"conn8","msg":"Index build: registering","attr":{"buildUUID":{"uuid":{"$uuid":"1203582e-e6e4-4d96-b0cf-722d0c8d2de7"}},"namespace":"meta_db.cache","collectionUUID":{"uuid":{"$uuid":"5ae6a461-a245-42f9-84fb-7e32b5b618bc"}},"indexes":1,"firstIndex":{"name":"date_1"}}}
{"t":{"$date":"2020-12-25T22:52:51.582-07:00"},"s":"I",  "c":"INDEX",    "id":20345,   "ctx":"conn8","msg":"Index build: done building","attr":{"buildUUID":null,"namespace":"meta_db.cache","index":"date_1","commitTimestamp":{"$timestamp":{"t":0,"i":0}}}}
{"t":{"$date":"2020-12-25T22:52:51.582-07:00"},"s":"I",  "c":"INDEX",    "id":20440,   "ctx":"conn8","msg":"Index build: waiting for index build to complete","attr":{"buildUUID":{"uuid":{"$uuid":"1203582e-e6e4-4d96-b0cf-722d0c8d2de7"}},"deadline":{"$date":{"$numberLong":"9223372036854775807"}}}}
{"t":{"$date":"2020-12-25T22:52:51.582-07:00"},"s":"I",  "c":"INDEX",    "id":20447,   "ctx":"conn8","msg":"Index build: completed","attr":{"buildUUID":{"uuid":{"$uuid":"1203582e-e6e4-4d96-b0cf-722d0c8d2de7"}}}}
{"t":{"$date":"2020-12-25T22:52:51.583-07:00"},"s":"I",  "c":"STORAGE",  "id":20320,   "ctx":"conn8","msg":"createCollection","attr":{"namespace":"arctic_test.toplevel_tickstore.ARCTIC","uuidDisposition":"generated","uuid":{"uuid":{"$uuid":"bdc18dee-5a18-451d-8850-e932d67b87e9"}},"options":{}}}
{"t":{"$date":"2020-12-25T22:52:51.653-07:00"},"s":"I",  "c":"INDEX",    "id":20345,   "ctx":"conn8","msg":"Index build: done building","attr":{"buildUUID":null,"namespace":"arctic_test.toplevel_tickstore.ARCTIC","index":"_id_","commitTimestamp":{"$timestamp":{"t":0,"i":0}}}}
{"t":{"$date":"2020-12-25T22:52:51.657-07:00"},"s":"I",  "c":"STORAGE",  "id":20320,   "ctx":"conn8","msg":"createCollection","attr":{"namespace":"arctic_test.toplevel_tickstore","uuidDisposition":"generated","uuid":{"uuid":{"$uuid":"3d31536d-3b66-4fa4-9f43-adbbf0be7ad8"}},"options":{}}}
{"t":{"$date":"2020-12-25T22:52:51.766-07:00"},"s":"I",  "c":"INDEX",    "id":20345,   "ctx":"conn8","msg":"Index build: done building","attr":{"buildUUID":null,"namespace":"arctic_test.toplevel_tickstore","index":"_id_","commitTimestamp":{"$timestamp":{"t":0,"i":0}}}}
{"t":{"$date":"2020-12-25T22:52:51.766-07:00"},"s":"I",  "c":"INDEX",    "id":20345,   "ctx":"conn8","msg":"Index build: done building","attr":{"buildUUID":null,"namespace":"arctic_test.toplevel_tickstore","index":"start_1","commitTimestamp":{"$timestamp":{"t":0,"i":0}}}}
{"t":{"$date":"2020-12-25T22:52:51.766-07:00"},"s":"I",  "c":"COMMAND",  "id":51803,   "ctx":"conn8","msg":"Slow query","attr":{"type":"command","ns":"arctic_test.toplevel_tickstore","command":{"createIndexes":"toplevel_tickstore","indexes":[{"background":true,"name":"start_1","key":{"start":1}}],"lsid":{"id":{"$uuid":"d0eae24a-83dd-4172-aa57-ee80ea17f9b8"}},"$db":"arctic_test","$readPreference":{"mode":"primary"}},"numYields":0,"reslen":114,"locks":{"ParallelBatchWriterMode":{"acquireCount":{"r":5}},"ReplicationStateTransition":{"acquireCount":{"w":5}},"Global":{"acquireCount":{"r":2,"w":3}},"Database":{"acquireCount":{"r":2,"w":3}},"Collection":{"acquireCount":{"r":4,"w":2}},"Mutex":{"acquireCount":{"r":5}}},"flowControl":{"acquireCount":1},"storage":{},"protocol":"op_msg","durationMillis":108}}
--------------------------------------------------- Captured log setup ---------------------------------------------------
DEBUG    pytest_shutil.workspace:workspace.py:52 
DEBUG    pytest_shutil.workspace:workspace.py:53 =======================================================
DEBUG    pytest_shutil.workspace:workspace.py:56 pytest_shutil created workspace /tmp/tmpi3afyecs
DEBUG    pytest_shutil.workspace:workspace.py:64 This workspace will delete itself on teardown
DEBUG    pytest_shutil.workspace:workspace.py:65 =======================================================
DEBUG    pytest_shutil.workspace:workspace.py:66 
DEBUG    pytest_server_fixtures.serverclass.thread:thread.py:77 Launching thread server.
DEBUG    pytest_server_fixtures.serverclass.thread:thread.py:89 Running server: mongod --bind_ip=127.150.242.244 --port=25863 --nounixsocket --syncdelay=0 --nojournal --quiet --dbpath=/tmp/tmpi3afyecs
DEBUG    pytest_server_fixtures.serverclass.thread:thread.py:90 CWD: /home/cwm/git/bb.FLXSA/quant/arctic_venv36
DEBUG    pytest_server_fixtures.base2:base2.py:226 sleeping for 0.1 before retrying (1 of 28)
INFO     pytest_server_fixtures.mongo:mongo.py:128 Connecting to Mongo at 127.150.242.244:25863
DEBUG    pytest_server_fixtures.base2:base2.py:226 sleeping for 0.1 before retrying (2 of 28)
INFO     pytest_server_fixtures.mongo:mongo.py:128 Connecting to Mongo at 127.150.242.244:25863
DEBUG    pytest_server_fixtures.base2:base2.py:226 sleeping for 0.1 before retrying (3 of 28)
INFO     pytest_server_fixtures.mongo:mongo.py:128 Connecting to Mongo at 127.150.242.244:25863
DEBUG    pytest_server_fixtures.base2:base2.py:229 waited 0:00:01.216667 for server to start successfully
DEBUG    pytest_server_fixtures.base2:base2.py:69 Server now awake
INFO     arctic.fixtures.arctic:arctic.py:23 arctic.fixtures: arctic init(mongo_server.api=MongoClient(host=['127.150.242.244:25863'], document_class=dict, tz_aware=False, connect=True))
DEBUG    root:arctic.py:234 Cache has expired data, fetching from slow path and reloading cache.
-------------------------------------------------- Captured stdout call --------------------------------------------------
{"t":{"$date":"2020-12-25T22:52:51.771-07:00"},"s":"I",  "c":"STORAGE",  "id":20320,   "ctx":"conn8","msg":"createCollection","attr":{"namespace":"arctic_FEED_2010.LEVEL1.ARCTIC","uuidDisposition":"generated","uuid":{"uuid":{"$uuid":"adafebc7-b7ae-456b-b507-05f758a1af8b"}},"options":{}}}
{"t":{"$date":"2020-12-25T22:52:51.826-07:00"},"s":"I",  "c":"INDEX",    "id":20345,   "ctx":"conn8","msg":"Index build: done building","attr":{"buildUUID":null,"namespace":"arctic_FEED_2010.LEVEL1.ARCTIC","index":"_id_","commitTimestamp":{"$timestamp":{"t":0,"i":0}}}}
{"t":{"$date":"2020-12-25T22:52:51.827-07:00"},"s":"I",  "c":"STORAGE",  "id":20320,   "ctx":"conn8","msg":"createCollection","attr":{"namespace":"arctic_FEED_2010.LEVEL1","uuidDisposition":"generated","uuid":{"uuid":{"$uuid":"087063e0-8fa6-4a87-8571-0c313c3a2759"}},"options":{}}}
{"t":{"$date":"2020-12-25T22:52:51.877-07:00"},"s":"I",  "c":"-",        "id":20883,   "ctx":"conn1","msg":"Interrupted operation as its client disconnected","attr":{"opId":13}}
{"t":{"$date":"2020-12-25T22:52:51.924-07:00"},"s":"I",  "c":"INDEX",    "id":20345,   "ctx":"conn8","msg":"Index build: done building","attr":{"buildUUID":null,"namespace":"arctic_FEED_2010.LEVEL1","index":"_id_","commitTimestamp":{"$timestamp":{"t":0,"i":0}}}}
{"t":{"$date":"2020-12-25T22:52:51.924-07:00"},"s":"I",  "c":"INDEX",    "id":20345,   "ctx":"conn8","msg":"Index build: done building","attr":{"buildUUID":null,"namespace":"arctic_FEED_2010.LEVEL1","index":"sy_1_s_1","commitTimestamp":{"$timestamp":{"t":0,"i":0}}}}
{"t":{"$date":"2020-12-25T22:52:51.925-07:00"},"s":"I",  "c":"INDEX",    "id":20438,   "ctx":"conn8","msg":"Index build: registering","attr":{"buildUUID":{"uuid":{"$uuid":"a23eba8d-cac9-454b-a0b8-66204c0568f0"}},"namespace":"arctic_FEED_2010.LEVEL1","collectionUUID":{"uuid":{"$uuid":"087063e0-8fa6-4a87-8571-0c313c3a2759"}},"indexes":1,"firstIndex":{"name":"s_1"}}}
{"t":{"$date":"2020-12-25T22:52:51.953-07:00"},"s":"I",  "c":"INDEX",    "id":20345,   "ctx":"conn8","msg":"Index build: done building","attr":{"buildUUID":null,"namespace":"arctic_FEED_2010.LEVEL1","index":"s_1","commitTimestamp":{"$timestamp":{"t":0,"i":0}}}}
{"t":{"$date":"2020-12-25T22:52:51.954-07:00"},"s":"I",  "c":"INDEX",    "id":20440,   "ctx":"conn8","msg":"Index build: waiting for index build to complete","attr":{"buildUUID":{"uuid":{"$uuid":"a23eba8d-cac9-454b-a0b8-66204c0568f0"}},"deadline":{"$date":{"$numberLong":"9223372036854775807"}}}}
{"t":{"$date":"2020-12-25T22:52:51.954-07:00"},"s":"I",  "c":"INDEX",    "id":20447,   "ctx":"conn8","msg":"Index build: completed","attr":{"buildUUID":{"uuid":{"$uuid":"a23eba8d-cac9-454b-a0b8-66204c0568f0"}}}}
{"t":{"$date":"2020-12-25T22:52:51.954-07:00"},"s":"I",  "c":"STORAGE",  "id":20320,   "ctx":"conn8","msg":"createCollection","attr":{"namespace":"arctic_FEED_2010.LEVEL1.metadata","uuidDisposition":"generated","uuid":{"uuid":{"$uuid":"451efa07-649e-4890-bdcb-4d3a8153593b"}},"options":{}}}
{"t":{"$date":"2020-12-25T22:52:51.980-07:00"},"s":"I",  "c":"-",        "id":20883,   "ctx":"conn3","msg":"Interrupted operation as its client disconnected","attr":{"opId":16}}
{"t":{"$date":"2020-12-25T22:52:52.048-07:00"},"s":"I",  "c":"INDEX",    "id":20345,   "ctx":"conn8","msg":"Index build: done building","attr":{"buildUUID":null,"namespace":"arctic_FEED_2010.LEVEL1.metadata","index":"_id_","commitTimestamp":{"$timestamp":{"t":0,"i":0}}}}
{"t":{"$date":"2020-12-25T22:52:52.048-07:00"},"s":"I",  "c":"INDEX",    "id":20345,   "ctx":"conn8","msg":"Index build: done building","attr":{"buildUUID":null,"namespace":"arctic_FEED_2010.LEVEL1.metadata","index":"sy_1","commitTimestamp":{"$timestamp":{"t":0,"i":0}}}}
{"t":{"$date":"2020-12-25T22:52:52.051-07:00"},"s":"I",  "c":"STORAGE",  "id":20320,   "ctx":"conn8","msg":"createCollection","attr":{"namespace":"arctic_FEED_2011.LEVEL1.ARCTIC","uuidDisposition":"generated","uuid":{"uuid":{"$uuid":"713db8d9-993f-438d-b769-01b2cc0c2c46"}},"options":{}}}
{"t":{"$date":"2020-12-25T22:52:52.117-07:00"},"s":"I",  "c":"INDEX",    "id":20345,   "ctx":"conn8","msg":"Index build: done building","attr":{"buildUUID":null,"namespace":"arctic_FEED_2011.LEVEL1.ARCTIC","index":"_id_","commitTimestamp":{"$timestamp":{"t":0,"i":0}}}}
{"t":{"$date":"2020-12-25T22:52:52.118-07:00"},"s":"I",  "c":"STORAGE",  "id":20320,   "ctx":"conn8","msg":"createCollection","attr":{"namespace":"arctic_FEED_2011.LEVEL1","uuidDisposition":"generated","uuid":{"uuid":{"$uuid":"3aa41244-eda1-462b-af3c-6529e70da6c4"}},"options":{}}}
{"t":{"$date":"2020-12-25T22:52:52.203-07:00"},"s":"I",  "c":"INDEX",    "id":20345,   "ctx":"conn8","msg":"Index build: done building","attr":{"buildUUID":null,"namespace":"arctic_FEED_2011.LEVEL1","index":"_id_","commitTimestamp":{"$timestamp":{"t":0,"i":0}}}}
{"t":{"$date":"2020-12-25T22:52:52.203-07:00"},"s":"I",  "c":"INDEX",    "id":20345,   "ctx":"conn8","msg":"Index build: done building","attr":{"buildUUID":null,"namespace":"arctic_FEED_2011.LEVEL1","index":"sy_1_s_1","commitTimestamp":{"$timestamp":{"t":0,"i":0}}}}
{"t":{"$date":"2020-12-25T22:52:52.204-07:00"},"s":"I",  "c":"INDEX",    "id":20438,   "ctx":"conn8","msg":"Index build: registering","attr":{"buildUUID":{"uuid":{"$uuid":"289766a2-c706-4392-b486-cb50d9c7c31e"}},"namespace":"arctic_FEED_2011.LEVEL1","collectionUUID":{"uuid":{"$uuid":"3aa41244-eda1-462b-af3c-6529e70da6c4"}},"indexes":1,"firstIndex":{"name":"s_1"}}}
{"t":{"$date":"2020-12-25T22:52:52.228-07:00"},"s":"I",  "c":"INDEX",    "id":20345,   "ctx":"conn8","msg":"Index build: done building","attr":{"buildUUID":null,"namespace":"arctic_FEED_2011.LEVEL1","index":"s_1","commitTimestamp":{"$timestamp":{"t":0,"i":0}}}}
{"t":{"$date":"2020-12-25T22:52:52.229-07:00"},"s":"I",  "c":"INDEX",    "id":20440,   "ctx":"conn8","msg":"Index build: waiting for index build to complete","attr":{"buildUUID":{"uuid":{"$uuid":"289766a2-c706-4392-b486-cb50d9c7c31e"}},"deadline":{"$date":{"$numberLong":"9223372036854775807"}}}}
{"t":{"$date":"2020-12-25T22:52:52.229-07:00"},"s":"I",  "c":"INDEX",    "id":20447,   "ctx":"conn8","msg":"Index build: completed","attr":{"buildUUID":{"uuid":{"$uuid":"289766a2-c706-4392-b486-cb50d9c7c31e"}}}}
{"t":{"$date":"2020-12-25T22:52:52.229-07:00"},"s":"I",  "c":"STORAGE",  "id":20320,   "ctx":"conn8","msg":"createCollection","attr":{"namespace":"arctic_FEED_2011.LEVEL1.metadata","uuidDisposition":"generated","uuid":{"uuid":{"$uuid":"a6ae0fdc-a7a4-4f55-909b-2150cb7fd713"}},"options":{}}}
{"t":{"$date":"2020-12-25T22:52:52.317-07:00"},"s":"I",  "c":"INDEX",    "id":20345,   "ctx":"conn8","msg":"Index build: done building","attr":{"buildUUID":null,"namespace":"arctic_FEED_2011.LEVEL1.metadata","index":"_id_","commitTimestamp":{"$timestamp":{"t":0,"i":0}}}}
{"t":{"$date":"2020-12-25T22:52:52.318-07:00"},"s":"I",  "c":"INDEX",    "id":20345,   "ctx":"conn8","msg":"Index build: done building","attr":{"buildUUID":null,"namespace":"arctic_FEED_2011.LEVEL1.metadata","index":"sy_1","commitTimestamp":{"$timestamp":{"t":0,"i":0}}}}
--------------------------------------------------- Captured log call ----------------------------------------------------
WARNING  arctic.tickstore.tickstore:tickstore.py:706 NB treating all values as 'exists' - no longer sparse
DEBUG    arctic.tickstore.tickstore:tickstore.py:612 1 buckets in 0.000647: approx 154559505 ticks/sec
WARNING  arctic.tickstore.tickstore:tickstore.py:706 NB treating all values as 'exists' - no longer sparse
DEBUG    arctic.tickstore.tickstore:tickstore.py:612 1 buckets in 0.000549: approx 182149362 ticks/sec
INFO     arctic.tickstore.tickstore:tickstore.py:355 Got data in 0.003327 secs, creating DataFrame...
INFO     arctic.tickstore.tickstore:tickstore.py:364 6 rows in 0.004124 secs: 1454 ticks/sec
INFO     arctic.tickstore.tickstore:tickstore.py:355 Got data in 0.00317 secs, creating DataFrame...
INFO     arctic.tickstore.tickstore:tickstore.py:364 6 rows in 0.00401 secs: 1496 ticks/sec
------------------------------------------------- Captured log teardown --------------------------------------------------
DEBUG    pytest_server_fixtures.serverclass.thread:thread.py:54 Killing process tree for 3720 (total_procs_to_kill=1)
DEBUG    pytest_server_fixtures.serverclass.thread:thread.py:35 Killing 1 processes with signal Signals.SIGKILL
DEBUG    pytest_server_fixtures.serverclass.thread:thread.py:39 Waiting for 1 processes to die
DEBUG    pytest_server_fixtures.serverclass.thread:thread.py:43 All processes are terminated
DEBUG    pytest_shutil.workspace:workspace.py:140 
DEBUG    pytest_shutil.workspace:workspace.py:141 =======================================================
DEBUG    pytest_shutil.workspace:workspace.py:142 pytest_shutil deleting workspace /tmp/tmpi3afyecs
DEBUG    pytest_shutil.workspace:workspace.py:143 =======================================================
DEBUG    pytest_shutil.workspace:workspace.py:144
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
------------------------------------------------- Captured stdout setup --------------------------------------------------
{"t":{"$date":"2020-12-25T22:52:52.420-07:00"},"s":"I",  "c":"CONTROL",  "id":23285,   "ctx":"main","msg":"Automatically disabling TLS 1.0, to force-enable TLS 1.0 specify --sslDisabledProtocols 'none'"}
{"t":{"$date":"2020-12-25T22:52:52.422-07:00"},"s":"W",  "c":"ASIO",     "id":22601,   "ctx":"main","msg":"No TransportLayer configured during NetworkInterface startup"}
{"t":{"$date":"2020-12-25T22:52:52.422-07:00"},"s":"I",  "c":"NETWORK",  "id":4648601, "ctx":"main","msg":"Implicit TCP FastOpen unavailable. If TCP FastOpen is required, set tcpFastOpenServer, tcpFastOpenClient, and tcpFastOpenQueueSize."}
{"t":{"$date":"2020-12-25T22:52:52.422-07:00"},"s":"I",  "c":"STORAGE",  "id":4615611, "ctx":"initandlisten","msg":"MongoDB starting","attr":{"pid":3772,"port":15099,"dbPath":"/tmp/tmpzf17v36z","architecture":"64-bit","host":"flxsa02"}}
{"t":{"$date":"2020-12-25T22:52:52.422-07:00"},"s":"I",  "c":"CONTROL",  "id":23403,   "ctx":"initandlisten","msg":"Build Info","attr":{"buildInfo":{"version":"4.4.2","gitVersion":"15e73dc5738d2278b688f8929aee605fe4279b0e","openSSLVersion":"OpenSSL 1.0.2g  1 Mar 2016","modules":[],"allocator":"tcmalloc","environment":{"distmod":"ubuntu1604","distarch":"x86_64","target_arch":"x86_64"}}}}
{"t":{"$date":"2020-12-25T22:52:52.422-07:00"},"s":"I",  "c":"CONTROL",  "id":51765,   "ctx":"initandlisten","msg":"Operating System","attr":{"os":{"name":"Ubuntu","version":"16.04"}}}
{"t":{"$date":"2020-12-25T22:52:52.422-07:00"},"s":"I",  "c":"CONTROL",  "id":21951,   "ctx":"initandlisten","msg":"Options set by command line","attr":{"options":{"net":{"bindIp":"127.150.242.244","port":15099,"unixDomainSocket":{"enabled":false}},"storage":{"dbPath":"/tmp/tmpzf17v36z","journal":{"enabled":false},"syncPeriodSecs":0.0},"systemLog":{"quiet":true}}}}
{"t":{"$date":"2020-12-25T22:52:52.423-07:00"},"s":"I",  "c":"STORAGE",  "id":22297,   "ctx":"initandlisten","msg":"Using the XFS filesystem is strongly recommended with the WiredTiger storage engine. See http://dochub.mongodb.org/core/prodnotes-filesystem","tags":["startupWarnings"]}
{"t":{"$date":"2020-12-25T22:52:52.423-07:00"},"s":"I",  "c":"STORAGE",  "id":22315,   "ctx":"initandlisten","msg":"Opening WiredTiger","attr":{"config":"create,cache_size=11497M,session_max=33000,eviction=(threads_min=4,threads_max=4),config_base=false,statistics=(fast),log=(enabled=true,archive=true,path=journal,compressor=snappy),file_manager=(close_idle_time=100000,close_scan_interval=10,close_handle_minimum=250),statistics_log=(wait=0),verbose=[recovery_progress,checkpoint_progress,compact_progress],,log=(enabled=false),"}}
{"t":{"$date":"2020-12-25T22:52:52.957-07:00"},"s":"I",  "c":"STORAGE",  "id":22430,   "ctx":"initandlisten","msg":"WiredTiger message","attr":{"message":"[1608961972:957611][3772:0x7fe7d197ba80], txn-recover: [WT_VERB_RECOVERY | WT_VERB_RECOVERY_PROGRESS] Set global recovery timestamp: (0, 0)"}}
{"t":{"$date":"2020-12-25T22:52:52.957-07:00"},"s":"I",  "c":"STORAGE",  "id":22430,   "ctx":"initandlisten","msg":"WiredTiger message","attr":{"message":"[1608961972:957667][3772:0x7fe7d197ba80], txn-recover: [WT_VERB_RECOVERY | WT_VERB_RECOVERY_PROGRESS] Set global oldest timestamp: (0, 0)"}}
{"t":{"$date":"2020-12-25T22:52:53.004-07:00"},"s":"I",  "c":"STORAGE",  "id":4795906, "ctx":"initandlisten","msg":"WiredTiger opened","attr":{"durationMillis":581}}
{"t":{"$date":"2020-12-25T22:52:53.004-07:00"},"s":"I",  "c":"RECOVERY", "id":23987,   "ctx":"initandlisten","msg":"WiredTiger recoveryTimestamp","attr":{"recoveryTimestamp":{"$timestamp":{"t":0,"i":0}}}}
{"t":{"$date":"2020-12-25T22:52:53.063-07:00"},"s":"I",  "c":"STORAGE",  "id":4366408, "ctx":"initandlisten","msg":"No table logging settings modifications are required for existing WiredTiger tables","attr":{"loggingEnabled":true}}
{"t":{"$date":"2020-12-25T22:52:53.063-07:00"},"s":"I",  "c":"STORAGE",  "id":22262,   "ctx":"initandlisten","msg":"Timestamp monitor starting"}
{"t":{"$date":"2020-12-25T22:52:53.083-07:00"},"s":"W",  "c":"CONTROL",  "id":22120,   "ctx":"initandlisten","msg":"Access control is not enabled for the database. Read and write access to data and configuration is unrestricted","tags":["startupWarnings"]}
{"t":{"$date":"2020-12-25T22:52:53.083-07:00"},"s":"W",  "c":"CONTROL",  "id":22184,   "ctx":"initandlisten","msg":"Soft rlimits too low","attr":{"currentValue":1024,"recommendedMinimum":64000},"tags":["startupWarnings"]}
{"t":{"$date":"2020-12-25T22:52:53.084-07:00"},"s":"I",  "c":"STORAGE",  "id":20320,   "ctx":"initandlisten","msg":"createCollection","attr":{"namespace":"admin.system.version","uuidDisposition":"provided","uuid":{"uuid":{"$uuid":"d8fd3ff1-b8f7-41c5-a884-b0deda865e66"}},"options":{"uuid":{"$uuid":"d8fd3ff1-b8f7-41c5-a884-b0deda865e66"}}}}
{"t":{"$date":"2020-12-25T22:52:53.145-07:00"},"s":"I",  "c":"INDEX",    "id":20345,   "ctx":"initandlisten","msg":"Index build: done building","attr":{"buildUUID":null,"namespace":"admin.system.version","index":"_id_","commitTimestamp":{"$timestamp":{"t":0,"i":0}}}}
{"t":{"$date":"2020-12-25T22:52:53.145-07:00"},"s":"I",  "c":"COMMAND",  "id":20459,   "ctx":"initandlisten","msg":"Setting featureCompatibilityVersion","attr":{"newVersion":"4.4"}}
{"t":{"$date":"2020-12-25T22:52:53.146-07:00"},"s":"I",  "c":"STORAGE",  "id":20536,   "ctx":"initandlisten","msg":"Flow Control is enabled on this deployment"}
{"t":{"$date":"2020-12-25T22:52:53.146-07:00"},"s":"I",  "c":"STORAGE",  "id":20320,   "ctx":"initandlisten","msg":"createCollection","attr":{"namespace":"local.startup_log","uuidDisposition":"generated","uuid":{"uuid":{"$uuid":"961a5fd2-4ed0-4371-97d5-4dca122cbd15"}},"options":{"capped":true,"size":10485760}}}
{"t":{"$date":"2020-12-25T22:52:53.209-07:00"},"s":"I",  "c":"INDEX",    "id":20345,   "ctx":"initandlisten","msg":"Index build: done building","attr":{"buildUUID":null,"namespace":"local.startup_log","index":"_id_","commitTimestamp":{"$timestamp":{"t":0,"i":0}}}}
{"t":{"$date":"2020-12-25T22:52:53.209-07:00"},"s":"I",  "c":"FTDC",     "id":20625,   "ctx":"initandlisten","msg":"Initializing full-time diagnostic data capture","attr":{"dataDirectory":"/tmp/tmpzf17v36z/diagnostic.data"}}
{"t":{"$date":"2020-12-25T22:52:53.211-07:00"},"s":"I",  "c":"CONTROL",  "id":20712,   "ctx":"LogicalSessionCacheReap","msg":"Sessions collection is not set up; waiting until next sessions reap interval","attr":{"error":"NamespaceNotFound: config.system.sessions does not exist"}}
{"t":{"$date":"2020-12-25T22:52:53.211-07:00"},"s":"I",  "c":"NETWORK",  "id":23015,   "ctx":"listener","msg":"Listening on","attr":{"address":"127.150.242.244"}}
{"t":{"$date":"2020-12-25T22:52:53.211-07:00"},"s":"I",  "c":"NETWORK",  "id":23016,   "ctx":"listener","msg":"Waiting for connections","attr":{"port":15099,"ssl":"off"}}
{"t":{"$date":"2020-12-25T22:52:53.211-07:00"},"s":"I",  "c":"STORAGE",  "id":20320,   "ctx":"LogicalSessionCacheRefresh","msg":"createCollection","attr":{"namespace":"config.system.sessions","uuidDisposition":"generated","uuid":{"uuid":{"$uuid":"25aff499-19dd-4af0-a4a2-853767fc8ec4"}},"options":{}}}
{"t":{"$date":"2020-12-25T22:52:53.305-07:00"},"s":"I",  "c":"INDEX",    "id":20345,   "ctx":"LogicalSessionCacheRefresh","msg":"Index build: done building","attr":{"buildUUID":null,"namespace":"config.system.sessions","index":"_id_","commitTimestamp":{"$timestamp":{"t":0,"i":0}}}}
{"t":{"$date":"2020-12-25T22:52:53.305-07:00"},"s":"I",  "c":"INDEX",    "id":20345,   "ctx":"LogicalSessionCacheRefresh","msg":"Index build: done building","attr":{"buildUUID":null,"namespace":"config.system.sessions","index":"lsidTTLIndex","commitTimestamp":{"$timestamp":{"t":0,"i":0}}}}
{"t":{"$date":"2020-12-25T22:52:53.495-07:00"},"s":"I",  "c":"NETWORK",  "id":51800,   "ctx":"conn1","msg":"client metadata","attr":{"remote":"127.0.0.1:38174","client":"conn1","doc":{"driver":{"name":"PyMongo","version":"3.11.2"},"os":{"type":"Linux","name":"Linux","architecture":"x86_64","version":"4.15.0-128-generic"},"platform":"CPython 3.6.12.final.0"}}}
{"t":{"$date":"2020-12-25T22:52:53.496-07:00"},"s":"I",  "c":"NETWORK",  "id":51800,   "ctx":"conn2","msg":"client metadata","attr":{"remote":"127.0.0.1:38176","client":"conn2","doc":{"driver":{"name":"PyMongo","version":"3.11.2"},"os":{"type":"Linux","name":"Linux","architecture":"x86_64","version":"4.15.0-128-generic"},"platform":"CPython 3.6.12.final.0"}}}
{"t":{"$date":"2020-12-25T22:52:53.599-07:00"},"s":"I",  "c":"NETWORK",  "id":51800,   "ctx":"conn3","msg":"client metadata","attr":{"remote":"127.0.0.1:38178","client":"conn3","doc":{"driver":{"name":"PyMongo","version":"3.11.2"},"os":{"type":"Linux","name":"Linux","architecture":"x86_64","version":"4.15.0-128-generic"},"platform":"CPython 3.6.12.final.0"}}}
{"t":{"$date":"2020-12-25T22:52:53.601-07:00"},"s":"I",  "c":"NETWORK",  "id":51800,   "ctx":"conn4","msg":"client metadata","attr":{"remote":"127.0.0.1:38180","client":"conn4","doc":{"driver":{"name":"PyMongo","version":"3.11.2"},"os":{"type":"Linux","name":"Linux","architecture":"x86_64","version":"4.15.0-128-generic"},"platform":"CPython 3.6.12.final.0"}}}
{"t":{"$date":"2020-12-25T22:52:53.601-07:00"},"s":"I",  "c":"NETWORK",  "id":51800,   "ctx":"conn5","msg":"client metadata","attr":{"remote":"127.0.0.1:38182","client":"conn5","doc":{"driver":{"name":"PyMongo","version":"3.11.2"},"os":{"type":"Linux","name":"Linux","architecture":"x86_64","version":"4.15.0-128-generic"},"platform":"CPython 3.6.12.final.0"}}}
{"t":{"$date":"2020-12-25T22:52:53.605-07:00"},"s":"I",  "c":"NETWORK",  "id":51800,   "ctx":"conn6","msg":"client metadata","attr":{"remote":"127.0.0.1:38184","client":"conn6","doc":{"driver":{"name":"PyMongo","version":"3.11.2"},"os":{"type":"Linux","name":"Linux","architecture":"x86_64","version":"4.15.0-128-generic"},"platform":"CPython 3.6.12.final.0"}}}
{"t":{"$date":"2020-12-25T22:52:53.607-07:00"},"s":"I",  "c":"NETWORK",  "id":51800,   "ctx":"conn7","msg":"client metadata","attr":{"remote":"127.0.0.1:38186","client":"conn7","doc":{"driver":{"name":"PyMongo","version":"3.11.2"},"os":{"type":"Linux","name":"Linux","architecture":"x86_64","version":"4.15.0-128-generic"},"platform":"CPython 3.6.12.final.0"}}}
{"t":{"$date":"2020-12-25T22:52:53.608-07:00"},"s":"I",  "c":"NETWORK",  "id":51800,   "ctx":"conn8","msg":"client metadata","attr":{"remote":"127.0.0.1:38188","client":"conn8","doc":{"driver":{"name":"PyMongo","version":"3.11.2"},"os":{"type":"Linux","name":"Linux","architecture":"x86_64","version":"4.15.0-128-generic"},"platform":"CPython 3.6.12.final.0"}}}
{"t":{"$date":"2020-12-25T22:52:53.611-07:00"},"s":"I",  "c":"STORAGE",  "id":20320,   "ctx":"conn7","msg":"createCollection","attr":{"namespace":"meta_db.cache","uuidDisposition":"generated","uuid":{"uuid":{"$uuid":"38794cc2-61d3-49a4-804d-70be1d043016"}},"options":{}}}
{"t":{"$date":"2020-12-25T22:52:53.675-07:00"},"s":"I",  "c":"INDEX",    "id":20345,   "ctx":"conn7","msg":"Index build: done building","attr":{"buildUUID":null,"namespace":"meta_db.cache","index":"_id_","commitTimestamp":{"$timestamp":{"t":0,"i":0}}}}
{"t":{"$date":"2020-12-25T22:52:53.676-07:00"},"s":"I",  "c":"INDEX",    "id":20438,   "ctx":"conn7","msg":"Index build: registering","attr":{"buildUUID":{"uuid":{"$uuid":"d7357efb-f6e0-4e98-b185-69de9f201f86"}},"namespace":"meta_db.cache","collectionUUID":{"uuid":{"$uuid":"38794cc2-61d3-49a4-804d-70be1d043016"}},"indexes":1,"firstIndex":{"name":"date_1"}}}
{"t":{"$date":"2020-12-25T22:52:53.704-07:00"},"s":"I",  "c":"INDEX",    "id":20345,   "ctx":"conn7","msg":"Index build: done building","attr":{"buildUUID":null,"namespace":"meta_db.cache","index":"date_1","commitTimestamp":{"$timestamp":{"t":0,"i":0}}}}
{"t":{"$date":"2020-12-25T22:52:53.704-07:00"},"s":"I",  "c":"INDEX",    "id":20440,   "ctx":"conn7","msg":"Index build: waiting for index build to complete","attr":{"buildUUID":{"uuid":{"$uuid":"d7357efb-f6e0-4e98-b185-69de9f201f86"}},"deadline":{"$date":{"$numberLong":"9223372036854775807"}}}}
{"t":{"$date":"2020-12-25T22:52:53.704-07:00"},"s":"I",  "c":"INDEX",    "id":20447,   "ctx":"conn7","msg":"Index build: completed","attr":{"buildUUID":{"uuid":{"$uuid":"d7357efb-f6e0-4e98-b185-69de9f201f86"}}}}
{"t":{"$date":"2020-12-25T22:52:53.706-07:00"},"s":"I",  "c":"STORAGE",  "id":20320,   "ctx":"conn7","msg":"createCollection","attr":{"namespace":"arctic_test.toplevel_tickstore.ARCTIC","uuidDisposition":"generated","uuid":{"uuid":{"$uuid":"cf34519a-26ea-4809-adf3-647535f01abc"}},"options":{}}}
{"t":{"$date":"2020-12-25T22:52:53.769-07:00"},"s":"I",  "c":"INDEX",    "id":20345,   "ctx":"conn7","msg":"Index build: done building","attr":{"buildUUID":null,"namespace":"arctic_test.toplevel_tickstore.ARCTIC","index":"_id_","commitTimestamp":{"$timestamp":{"t":0,"i":0}}}}
{"t":{"$date":"2020-12-25T22:52:53.773-07:00"},"s":"I",  "c":"STORAGE",  "id":20320,   "ctx":"conn7","msg":"createCollection","attr":{"namespace":"arctic_test.toplevel_tickstore","uuidDisposition":"generated","uuid":{"uuid":{"$uuid":"aa9316e9-6ec3-4364-89fe-c9bd9ad17da1"}},"options":{}}}
{"t":{"$date":"2020-12-25T22:52:53.878-07:00"},"s":"I",  "c":"INDEX",    "id":20345,   "ctx":"conn7","msg":"Index build: done building","attr":{"buildUUID":null,"namespace":"arctic_test.toplevel_tickstore","index":"_id_","commitTimestamp":{"$timestamp":{"t":0,"i":0}}}}
{"t":{"$date":"2020-12-25T22:52:53.878-07:00"},"s":"I",  "c":"INDEX",    "id":20345,   "ctx":"conn7","msg":"Index build: done building","attr":{"buildUUID":null,"namespace":"arctic_test.toplevel_tickstore","index":"start_1","commitTimestamp":{"$timestamp":{"t":0,"i":0}}}}
{"t":{"$date":"2020-12-25T22:52:53.878-07:00"},"s":"I",  "c":"COMMAND",  "id":51803,   "ctx":"conn7","msg":"Slow query","attr":{"type":"command","ns":"arctic_test.toplevel_tickstore","command":{"createIndexes":"toplevel_tickstore","indexes":[{"background":true,"name":"start_1","key":{"start":1}}],"lsid":{"id":{"$uuid":"83f0a199-ce65-4b45-b286-5860de292c3a"}},"$db":"arctic_test","$readPreference":{"mode":"primary"}},"numYields":0,"reslen":114,"locks":{"ParallelBatchWriterMode":{"acquireCount":{"r":5}},"ReplicationStateTransition":{"acquireCount":{"w":5}},"Global":{"acquireCount":{"r":2,"w":3}},"Database":{"acquireCount":{"r":2,"w":3}},"Collection":{"acquireCount":{"r":4,"w":2}},"Mutex":{"acquireCount":{"r":5}}},"flowControl":{"acquireCount":1,"timeAcquiringMicros":1},"storage":{},"protocol":"op_msg","durationMillis":105}}
--------------------------------------------------- Captured log setup ---------------------------------------------------
DEBUG    pytest_shutil.workspace:workspace.py:52 
DEBUG    pytest_shutil.workspace:workspace.py:53 =======================================================
DEBUG    pytest_shutil.workspace:workspace.py:56 pytest_shutil created workspace /tmp/tmpzf17v36z
DEBUG    pytest_shutil.workspace:workspace.py:64 This workspace will delete itself on teardown
DEBUG    pytest_shutil.workspace:workspace.py:65 =======================================================
DEBUG    pytest_shutil.workspace:workspace.py:66 
DEBUG    pytest_server_fixtures.serverclass.thread:thread.py:77 Launching thread server.
DEBUG    pytest_server_fixtures.serverclass.thread:thread.py:89 Running server: mongod --bind_ip=127.150.242.244 --port=15099 --nounixsocket --syncdelay=0 --nojournal --quiet --dbpath=/tmp/tmpzf17v36z
DEBUG    pytest_server_fixtures.serverclass.thread:thread.py:90 CWD: /home/cwm/git/bb.FLXSA/quant/arctic_venv36
DEBUG    pytest_server_fixtures.base2:base2.py:226 sleeping for 0.1 before retrying (1 of 28)
INFO     pytest_server_fixtures.mongo:mongo.py:128 Connecting to Mongo at 127.150.242.244:15099
DEBUG    pytest_server_fixtures.base2:base2.py:226 sleeping for 0.1 before retrying (2 of 28)
INFO     pytest_server_fixtures.mongo:mongo.py:128 Connecting to Mongo at 127.150.242.244:15099
DEBUG    pytest_server_fixtures.base2:base2.py:226 sleeping for 0.1 before retrying (3 of 28)
INFO     pytest_server_fixtures.mongo:mongo.py:128 Connecting to Mongo at 127.150.242.244:15099
DEBUG    pytest_server_fixtures.base2:base2.py:229 waited 0:00:01.217104 for server to start successfully
DEBUG    pytest_server_fixtures.base2:base2.py:69 Server now awake
INFO     arctic.fixtures.arctic:arctic.py:23 arctic.fixtures: arctic init(mongo_server.api=MongoClient(host=['127.150.242.244:15099'], document_class=dict, tz_aware=False, connect=True))
DEBUG    root:arctic.py:234 Cache has expired data, fetching from slow path and reloading cache.
-------------------------------------------------- Captured stdout call --------------------------------------------------
{"t":{"$date":"2020-12-25T22:52:53.883-07:00"},"s":"I",  "c":"STORAGE",  "id":20320,   "ctx":"conn7","msg":"createCollection","attr":{"namespace":"arctic_FEED_2010.LEVEL1.ARCTIC","uuidDisposition":"generated","uuid":{"uuid":{"$uuid":"5b8c3e0e-829e-449b-88e9-432a773117f0"}},"options":{}}}
{"t":{"$date":"2020-12-25T22:52:53.946-07:00"},"s":"I",  "c":"INDEX",    "id":20345,   "ctx":"conn7","msg":"Index build: done building","attr":{"buildUUID":null,"namespace":"arctic_FEED_2010.LEVEL1.ARCTIC","index":"_id_","commitTimestamp":{"$timestamp":{"t":0,"i":0}}}}
{"t":{"$date":"2020-12-25T22:52:53.948-07:00"},"s":"I",  "c":"STORAGE",  "id":20320,   "ctx":"conn7","msg":"createCollection","attr":{"namespace":"arctic_FEED_2010.LEVEL1","uuidDisposition":"generated","uuid":{"uuid":{"$uuid":"87f64ca1-d724-4751-868f-037394610453"}},"options":{}}}
{"t":{"$date":"2020-12-25T22:52:53.997-07:00"},"s":"I",  "c":"-",        "id":20883,   "ctx":"conn1","msg":"Interrupted operation as its client disconnected","attr":{"opId":13}}
{"t":{"$date":"2020-12-25T22:52:54.047-07:00"},"s":"I",  "c":"INDEX",    "id":20345,   "ctx":"conn7","msg":"Index build: done building","attr":{"buildUUID":null,"namespace":"arctic_FEED_2010.LEVEL1","index":"_id_","commitTimestamp":{"$timestamp":{"t":0,"i":0}}}}
{"t":{"$date":"2020-12-25T22:52:54.047-07:00"},"s":"I",  "c":"INDEX",    "id":20345,   "ctx":"conn7","msg":"Index build: done building","attr":{"buildUUID":null,"namespace":"arctic_FEED_2010.LEVEL1","index":"sy_1_s_1","commitTimestamp":{"$timestamp":{"t":0,"i":0}}}}
{"t":{"$date":"2020-12-25T22:52:54.048-07:00"},"s":"I",  "c":"INDEX",    "id":20438,   "ctx":"conn7","msg":"Index build: registering","attr":{"buildUUID":{"uuid":{"$uuid":"1ac5a670-568a-442f-a0cc-36b9f1117e61"}},"namespace":"arctic_FEED_2010.LEVEL1","collectionUUID":{"uuid":{"$uuid":"87f64ca1-d724-4751-868f-037394610453"}},"indexes":1,"firstIndex":{"name":"s_1"}}}
{"t":{"$date":"2020-12-25T22:52:54.073-07:00"},"s":"I",  "c":"INDEX",    "id":20345,   "ctx":"conn7","msg":"Index build: done building","attr":{"buildUUID":null,"namespace":"arctic_FEED_2010.LEVEL1","index":"s_1","commitTimestamp":{"$timestamp":{"t":0,"i":0}}}}
{"t":{"$date":"2020-12-25T22:52:54.073-07:00"},"s":"I",  "c":"INDEX",    "id":20440,   "ctx":"conn7","msg":"Index build: waiting for index build to complete","attr":{"buildUUID":{"uuid":{"$uuid":"1ac5a670-568a-442f-a0cc-36b9f1117e61"}},"deadline":{"$date":{"$numberLong":"9223372036854775807"}}}}
{"t":{"$date":"2020-12-25T22:52:54.073-07:00"},"s":"I",  "c":"INDEX",    "id":20447,   "ctx":"conn7","msg":"Index build: completed","attr":{"buildUUID":{"uuid":{"$uuid":"1ac5a670-568a-442f-a0cc-36b9f1117e61"}}}}
{"t":{"$date":"2020-12-25T22:52:54.074-07:00"},"s":"I",  "c":"STORAGE",  "id":20320,   "ctx":"conn7","msg":"createCollection","attr":{"namespace":"arctic_FEED_2010.LEVEL1.metadata","uuidDisposition":"generated","uuid":{"uuid":{"$uuid":"441120b0-f19d-47a8-82ee-71e03c6987f7"}},"options":{}}}
{"t":{"$date":"2020-12-25T22:52:54.101-07:00"},"s":"I",  "c":"-",        "id":20883,   "ctx":"conn3","msg":"Interrupted operation as its client disconnected","attr":{"opId":16}}
{"t":{"$date":"2020-12-25T22:52:54.166-07:00"},"s":"I",  "c":"INDEX",    "id":20345,   "ctx":"conn7","msg":"Index build: done building","attr":{"buildUUID":null,"namespace":"arctic_FEED_2010.LEVEL1.metadata","index":"_id_","commitTimestamp":{"$timestamp":{"t":0,"i":0}}}}
{"t":{"$date":"2020-12-25T22:52:54.166-07:00"},"s":"I",  "c":"INDEX",    "id":20345,   "ctx":"conn7","msg":"Index build: done building","attr":{"buildUUID":null,"namespace":"arctic_FEED_2010.LEVEL1.metadata","index":"sy_1","commitTimestamp":{"$timestamp":{"t":0,"i":0}}}}
{"t":{"$date":"2020-12-25T22:52:54.170-07:00"},"s":"I",  "c":"STORAGE",  "id":20320,   "ctx":"conn7","msg":"createCollection","attr":{"namespace":"arctic_FEED_2011.LEVEL1.ARCTIC","uuidDisposition":"generated","uuid":{"uuid":{"$uuid":"f1dbc14e-9e32-414a-ab5e-9881ca01c961"}},"options":{}}}
{"t":{"$date":"2020-12-25T22:52:54.236-07:00"},"s":"I",  "c":"INDEX",    "id":20345,   "ctx":"conn7","msg":"Index build: done building","attr":{"buildUUID":null,"namespace":"arctic_FEED_2011.LEVEL1.ARCTIC","index":"_id_","commitTimestamp":{"$timestamp":{"t":0,"i":0}}}}
{"t":{"$date":"2020-12-25T22:52:54.237-07:00"},"s":"I",  "c":"STORAGE",  "id":20320,   "ctx":"conn7","msg":"createCollection","attr":{"namespace":"arctic_FEED_2011.LEVEL1","uuidDisposition":"generated","uuid":{"uuid":{"$uuid":"64e1a42b-6c27-4bec-a5a7-2c84ccdc89b6"}},"options":{}}}
{"t":{"$date":"2020-12-25T22:52:54.323-07:00"},"s":"I",  "c":"INDEX",    "id":20345,   "ctx":"conn7","msg":"Index build: done building","attr":{"buildUUID":null,"namespace":"arctic_FEED_2011.LEVEL1","index":"_id_","commitTimestamp":{"$timestamp":{"t":0,"i":0}}}}
{"t":{"$date":"2020-12-25T22:52:54.323-07:00"},"s":"I",  "c":"INDEX",    "id":20345,   "ctx":"conn7","msg":"Index build: done building","attr":{"buildUUID":null,"namespace":"arctic_FEED_2011.LEVEL1","index":"sy_1_s_1","commitTimestamp":{"$timestamp":{"t":0,"i":0}}}}
{"t":{"$date":"2020-12-25T22:52:54.323-07:00"},"s":"I",  "c":"INDEX",    "id":20438,   "ctx":"conn7","msg":"Index build: registering","attr":{"buildUUID":{"uuid":{"$uuid":"c32dd342-7e3b-42b3-9f8b-9c016b27d818"}},"namespace":"arctic_FEED_2011.LEVEL1","collectionUUID":{"uuid":{"$uuid":"64e1a42b-6c27-4bec-a5a7-2c84ccdc89b6"}},"indexes":1,"firstIndex":{"name":"s_1"}}}
{"t":{"$date":"2020-12-25T22:52:54.352-07:00"},"s":"I",  "c":"INDEX",    "id":20345,   "ctx":"conn7","msg":"Index build: done building","attr":{"buildUUID":null,"namespace":"arctic_FEED_2011.LEVEL1","index":"s_1","commitTimestamp":{"$timestamp":{"t":0,"i":0}}}}
{"t":{"$date":"2020-12-25T22:52:54.352-07:00"},"s":"I",  "c":"INDEX",    "id":20440,   "ctx":"conn7","msg":"Index build: waiting for index build to complete","attr":{"buildUUID":{"uuid":{"$uuid":"c32dd342-7e3b-42b3-9f8b-9c016b27d818"}},"deadline":{"$date":{"$numberLong":"9223372036854775807"}}}}
{"t":{"$date":"2020-12-25T22:52:54.352-07:00"},"s":"I",  "c":"INDEX",    "id":20447,   "ctx":"conn7","msg":"Index build: completed","attr":{"buildUUID":{"uuid":{"$uuid":"c32dd342-7e3b-42b3-9f8b-9c016b27d818"}}}}
{"t":{"$date":"2020-12-25T22:52:54.353-07:00"},"s":"I",  "c":"STORAGE",  "id":20320,   "ctx":"conn7","msg":"createCollection","attr":{"namespace":"arctic_FEED_2011.LEVEL1.metadata","uuidDisposition":"generated","uuid":{"uuid":{"$uuid":"bde03ce0-a2c3-422f-b84b-72c17ddfe0ad"}},"options":{}}}
{"t":{"$date":"2020-12-25T22:52:54.437-07:00"},"s":"I",  "c":"INDEX",    "id":20345,   "ctx":"conn7","msg":"Index build: done building","attr":{"buildUUID":null,"namespace":"arctic_FEED_2011.LEVEL1.metadata","index":"_id_","commitTimestamp":{"$timestamp":{"t":0,"i":0}}}}
{"t":{"$date":"2020-12-25T22:52:54.437-07:00"},"s":"I",  "c":"INDEX",    "id":20345,   "ctx":"conn7","msg":"Index build: done building","attr":{"buildUUID":null,"namespace":"arctic_FEED_2011.LEVEL1.metadata","index":"sy_1","commitTimestamp":{"$timestamp":{"t":0,"i":0}}}}
--------------------------------------------------- Captured log call ----------------------------------------------------
WARNING  arctic.tickstore.tickstore:tickstore.py:706 NB treating all values as 'exists' - no longer sparse
DEBUG    arctic.tickstore.tickstore:tickstore.py:612 1 buckets in 0.000675: approx 148148148 ticks/sec
WARNING  arctic.tickstore.tickstore:tickstore.py:706 NB treating all values as 'exists' - no longer sparse
DEBUG    arctic.tickstore.tickstore:tickstore.py:612 1 buckets in 0.000645: approx 155038759 ticks/sec
INFO     arctic.tickstore.tickstore:tickstore.py:355 Got data in 0.003569 secs, creating DataFrame...
INFO     arctic.tickstore.tickstore:tickstore.py:364 6 rows in 0.004537 secs: 1322 ticks/sec
------------------------------------------------- Captured log teardown --------------------------------------------------
DEBUG    pytest_server_fixtures.serverclass.thread:thread.py:54 Killing process tree for 3772 (total_procs_to_kill=1)
DEBUG    pytest_server_fixtures.serverclass.thread:thread.py:35 Killing 1 processes with signal Signals.SIGKILL
DEBUG    pytest_server_fixtures.serverclass.thread:thread.py:39 Waiting for 1 processes to die
DEBUG    pytest_server_fixtures.serverclass.thread:thread.py:43 All processes are terminated
DEBUG    pytest_shutil.workspace:workspace.py:140 
DEBUG    pytest_shutil.workspace:workspace.py:141 =======================================================
DEBUG    pytest_shutil.workspace:workspace.py:142 pytest_shutil deleting workspace /tmp/tmpzf17v36z
DEBUG    pytest_shutil.workspace:workspace.py:143 =======================================================
DEBUG    pytest_shutil.workspace:workspace.py:144
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
------------------------------------------------- Captured stdout setup --------------------------------------------------
{"t":{"$date":"2020-12-25T22:52:56.353-07:00"},"s":"I",  "c":"CONTROL",  "id":23285,   "ctx":"main","msg":"Automatically disabling TLS 1.0, to force-enable TLS 1.0 specify --sslDisabledProtocols 'none'"}
{"t":{"$date":"2020-12-25T22:52:56.355-07:00"},"s":"W",  "c":"ASIO",     "id":22601,   "ctx":"main","msg":"No TransportLayer configured during NetworkInterface startup"}
{"t":{"$date":"2020-12-25T22:52:56.355-07:00"},"s":"I",  "c":"NETWORK",  "id":4648601, "ctx":"main","msg":"Implicit TCP FastOpen unavailable. If TCP FastOpen is required, set tcpFastOpenServer, tcpFastOpenClient, and tcpFastOpenQueueSize."}
{"t":{"$date":"2020-12-25T22:52:56.356-07:00"},"s":"I",  "c":"STORAGE",  "id":4615611, "ctx":"initandlisten","msg":"MongoDB starting","attr":{"pid":3878,"port":19579,"dbPath":"/tmp/tmpwm4nsk6r","architecture":"64-bit","host":"flxsa02"}}
{"t":{"$date":"2020-12-25T22:52:56.356-07:00"},"s":"I",  "c":"CONTROL",  "id":23403,   "ctx":"initandlisten","msg":"Build Info","attr":{"buildInfo":{"version":"4.4.2","gitVersion":"15e73dc5738d2278b688f8929aee605fe4279b0e","openSSLVersion":"OpenSSL 1.0.2g  1 Mar 2016","modules":[],"allocator":"tcmalloc","environment":{"distmod":"ubuntu1604","distarch":"x86_64","target_arch":"x86_64"}}}}
{"t":{"$date":"2020-12-25T22:52:56.356-07:00"},"s":"I",  "c":"CONTROL",  "id":51765,   "ctx":"initandlisten","msg":"Operating System","attr":{"os":{"name":"Ubuntu","version":"16.04"}}}
{"t":{"$date":"2020-12-25T22:52:56.356-07:00"},"s":"I",  "c":"CONTROL",  "id":21951,   "ctx":"initandlisten","msg":"Options set by command line","attr":{"options":{"net":{"bindIp":"127.150.242.244","port":19579,"unixDomainSocket":{"enabled":false}},"storage":{"dbPath":"/tmp/tmpwm4nsk6r","journal":{"enabled":false},"syncPeriodSecs":0.0},"systemLog":{"quiet":true}}}}
{"t":{"$date":"2020-12-25T22:52:56.357-07:00"},"s":"I",  "c":"STORAGE",  "id":22297,   "ctx":"initandlisten","msg":"Using the XFS filesystem is strongly recommended with the WiredTiger storage engine. See http://dochub.mongodb.org/core/prodnotes-filesystem","tags":["startupWarnings"]}
{"t":{"$date":"2020-12-25T22:52:56.357-07:00"},"s":"I",  "c":"STORAGE",  "id":22315,   "ctx":"initandlisten","msg":"Opening WiredTiger","attr":{"config":"create,cache_size=11497M,session_max=33000,eviction=(threads_min=4,threads_max=4),config_base=false,statistics=(fast),log=(enabled=true,archive=true,path=journal,compressor=snappy),file_manager=(close_idle_time=100000,close_scan_interval=10,close_handle_minimum=250),statistics_log=(wait=0),verbose=[recovery_progress,checkpoint_progress,compact_progress],,log=(enabled=false),"}}
{"t":{"$date":"2020-12-25T22:52:56.888-07:00"},"s":"I",  "c":"STORAGE",  "id":22430,   "ctx":"initandlisten","msg":"WiredTiger message","attr":{"message":"[1608961976:888404][3878:0x7efe0adafa80], txn-recover: [WT_VERB_RECOVERY | WT_VERB_RECOVERY_PROGRESS] Set global recovery timestamp: (0, 0)"}}
{"t":{"$date":"2020-12-25T22:52:56.888-07:00"},"s":"I",  "c":"STORAGE",  "id":22430,   "ctx":"initandlisten","msg":"WiredTiger message","attr":{"message":"[1608961976:888456][3878:0x7efe0adafa80], txn-recover: [WT_VERB_RECOVERY | WT_VERB_RECOVERY_PROGRESS] Set global oldest timestamp: (0, 0)"}}
{"t":{"$date":"2020-12-25T22:52:56.930-07:00"},"s":"I",  "c":"STORAGE",  "id":4795906, "ctx":"initandlisten","msg":"WiredTiger opened","attr":{"durationMillis":573}}
{"t":{"$date":"2020-12-25T22:52:56.930-07:00"},"s":"I",  "c":"RECOVERY", "id":23987,   "ctx":"initandlisten","msg":"WiredTiger recoveryTimestamp","attr":{"recoveryTimestamp":{"$timestamp":{"t":0,"i":0}}}}
{"t":{"$date":"2020-12-25T22:52:56.993-07:00"},"s":"I",  "c":"STORAGE",  "id":4366408, "ctx":"initandlisten","msg":"No table logging settings modifications are required for existing WiredTiger tables","attr":{"loggingEnabled":true}}
{"t":{"$date":"2020-12-25T22:52:56.994-07:00"},"s":"I",  "c":"STORAGE",  "id":22262,   "ctx":"initandlisten","msg":"Timestamp monitor starting"}
{"t":{"$date":"2020-12-25T22:52:57.011-07:00"},"s":"W",  "c":"CONTROL",  "id":22120,   "ctx":"initandlisten","msg":"Access control is not enabled for the database. Read and write access to data and configuration is unrestricted","tags":["startupWarnings"]}
{"t":{"$date":"2020-12-25T22:52:57.011-07:00"},"s":"W",  "c":"CONTROL",  "id":22184,   "ctx":"initandlisten","msg":"Soft rlimits too low","attr":{"currentValue":1024,"recommendedMinimum":64000},"tags":["startupWarnings"]}
{"t":{"$date":"2020-12-25T22:52:57.011-07:00"},"s":"I",  "c":"STORAGE",  "id":20320,   "ctx":"initandlisten","msg":"createCollection","attr":{"namespace":"admin.system.version","uuidDisposition":"provided","uuid":{"uuid":{"$uuid":"e43053f2-e48c-43dd-9895-1bdefdccb2e6"}},"options":{"uuid":{"$uuid":"e43053f2-e48c-43dd-9895-1bdefdccb2e6"}}}}
{"t":{"$date":"2020-12-25T22:52:57.077-07:00"},"s":"I",  "c":"INDEX",    "id":20345,   "ctx":"initandlisten","msg":"Index build: done building","attr":{"buildUUID":null,"namespace":"admin.system.version","index":"_id_","commitTimestamp":{"$timestamp":{"t":0,"i":0}}}}
{"t":{"$date":"2020-12-25T22:52:57.077-07:00"},"s":"I",  "c":"COMMAND",  "id":20459,   "ctx":"initandlisten","msg":"Setting featureCompatibilityVersion","attr":{"newVersion":"4.4"}}
{"t":{"$date":"2020-12-25T22:52:57.078-07:00"},"s":"I",  "c":"STORAGE",  "id":20536,   "ctx":"initandlisten","msg":"Flow Control is enabled on this deployment"}
{"t":{"$date":"2020-12-25T22:52:57.078-07:00"},"s":"I",  "c":"STORAGE",  "id":20320,   "ctx":"initandlisten","msg":"createCollection","attr":{"namespace":"local.startup_log","uuidDisposition":"generated","uuid":{"uuid":{"$uuid":"a3027798-6851-4f45-bdca-6645dc533e3a"}},"options":{"capped":true,"size":10485760}}}
{"t":{"$date":"2020-12-25T22:52:57.137-07:00"},"s":"I",  "c":"INDEX",    "id":20345,   "ctx":"initandlisten","msg":"Index build: done building","attr":{"buildUUID":null,"namespace":"local.startup_log","index":"_id_","commitTimestamp":{"$timestamp":{"t":0,"i":0}}}}
{"t":{"$date":"2020-12-25T22:52:57.137-07:00"},"s":"I",  "c":"FTDC",     "id":20625,   "ctx":"initandlisten","msg":"Initializing full-time diagnostic data capture","attr":{"dataDirectory":"/tmp/tmpwm4nsk6r/diagnostic.data"}}
{"t":{"$date":"2020-12-25T22:52:57.138-07:00"},"s":"I",  "c":"CONTROL",  "id":20712,   "ctx":"LogicalSessionCacheReap","msg":"Sessions collection is not set up; waiting until next sessions reap interval","attr":{"error":"NamespaceNotFound: config.system.sessions does not exist"}}
{"t":{"$date":"2020-12-25T22:52:57.138-07:00"},"s":"I",  "c":"NETWORK",  "id":23015,   "ctx":"listener","msg":"Listening on","attr":{"address":"127.150.242.244"}}
{"t":{"$date":"2020-12-25T22:52:57.138-07:00"},"s":"I",  "c":"NETWORK",  "id":23016,   "ctx":"listener","msg":"Waiting for connections","attr":{"port":19579,"ssl":"off"}}
{"t":{"$date":"2020-12-25T22:52:57.139-07:00"},"s":"I",  "c":"STORAGE",  "id":20320,   "ctx":"LogicalSessionCacheRefresh","msg":"createCollection","attr":{"namespace":"config.system.sessions","uuidDisposition":"generated","uuid":{"uuid":{"$uuid":"ab27e9f8-8eba-42b4-be34-c68562830cdc"}},"options":{}}}
{"t":{"$date":"2020-12-25T22:52:57.232-07:00"},"s":"I",  "c":"INDEX",    "id":20345,   "ctx":"LogicalSessionCacheRefresh","msg":"Index build: done building","attr":{"buildUUID":null,"namespace":"config.system.sessions","index":"_id_","commitTimestamp":{"$timestamp":{"t":0,"i":0}}}}
{"t":{"$date":"2020-12-25T22:52:57.232-07:00"},"s":"I",  "c":"INDEX",    "id":20345,   "ctx":"LogicalSessionCacheRefresh","msg":"Index build: done building","attr":{"buildUUID":null,"namespace":"config.system.sessions","index":"lsidTTLIndex","commitTimestamp":{"$timestamp":{"t":0,"i":0}}}}
{"t":{"$date":"2020-12-25T22:52:57.429-07:00"},"s":"I",  "c":"NETWORK",  "id":51800,   "ctx":"conn1","msg":"client metadata","attr":{"remote":"127.0.0.1:47198","client":"conn1","doc":{"driver":{"name":"PyMongo","version":"3.11.2"},"os":{"type":"Linux","name":"Linux","architecture":"x86_64","version":"4.15.0-128-generic"},"platform":"CPython 3.6.12.final.0"}}}
{"t":{"$date":"2020-12-25T22:52:57.430-07:00"},"s":"I",  "c":"NETWORK",  "id":51800,   "ctx":"conn2","msg":"client metadata","attr":{"remote":"127.0.0.1:47200","client":"conn2","doc":{"driver":{"name":"PyMongo","version":"3.11.2"},"os":{"type":"Linux","name":"Linux","architecture":"x86_64","version":"4.15.0-128-generic"},"platform":"CPython 3.6.12.final.0"}}}
{"t":{"$date":"2020-12-25T22:52:57.530-07:00"},"s":"I",  "c":"NETWORK",  "id":51800,   "ctx":"conn3","msg":"client metadata","attr":{"remote":"127.0.0.1:47202","client":"conn3","doc":{"driver":{"name":"PyMongo","version":"3.11.2"},"os":{"type":"Linux","name":"Linux","architecture":"x86_64","version":"4.15.0-128-generic"},"platform":"CPython 3.6.12.final.0"}}}
{"t":{"$date":"2020-12-25T22:52:57.532-07:00"},"s":"I",  "c":"NETWORK",  "id":51800,   "ctx":"conn4","msg":"client metadata","attr":{"remote":"127.0.0.1:47204","client":"conn4","doc":{"driver":{"name":"PyMongo","version":"3.11.2"},"os":{"type":"Linux","name":"Linux","architecture":"x86_64","version":"4.15.0-128-generic"},"platform":"CPython 3.6.12.final.0"}}}
{"t":{"$date":"2020-12-25T22:52:57.532-07:00"},"s":"I",  "c":"NETWORK",  "id":51800,   "ctx":"conn5","msg":"client metadata","attr":{"remote":"127.0.0.1:47206","client":"conn5","doc":{"driver":{"name":"PyMongo","version":"3.11.2"},"os":{"type":"Linux","name":"Linux","architecture":"x86_64","version":"4.15.0-128-generic"},"platform":"CPython 3.6.12.final.0"}}}
{"t":{"$date":"2020-12-25T22:52:57.535-07:00"},"s":"I",  "c":"NETWORK",  "id":51800,   "ctx":"conn6","msg":"client metadata","attr":{"remote":"127.0.0.1:47208","client":"conn6","doc":{"driver":{"name":"PyMongo","version":"3.11.2"},"os":{"type":"Linux","name":"Linux","architecture":"x86_64","version":"4.15.0-128-generic"},"platform":"CPython 3.6.12.final.0"}}}
{"t":{"$date":"2020-12-25T22:52:57.537-07:00"},"s":"I",  "c":"NETWORK",  "id":51800,   "ctx":"conn7","msg":"client metadata","attr":{"remote":"127.0.0.1:47210","client":"conn7","doc":{"driver":{"name":"PyMongo","version":"3.11.2"},"os":{"type":"Linux","name":"Linux","architecture":"x86_64","version":"4.15.0-128-generic"},"platform":"CPython 3.6.12.final.0"}}}
{"t":{"$date":"2020-12-25T22:52:57.537-07:00"},"s":"I",  "c":"NETWORK",  "id":51800,   "ctx":"conn8","msg":"client metadata","attr":{"remote":"127.0.0.1:47212","client":"conn8","doc":{"driver":{"name":"PyMongo","version":"3.11.2"},"os":{"type":"Linux","name":"Linux","architecture":"x86_64","version":"4.15.0-128-generic"},"platform":"CPython 3.6.12.final.0"}}}
{"t":{"$date":"2020-12-25T22:52:57.541-07:00"},"s":"I",  "c":"STORAGE",  "id":20320,   "ctx":"conn8","msg":"createCollection","attr":{"namespace":"meta_db.cache","uuidDisposition":"generated","uuid":{"uuid":{"$uuid":"c6171757-c33b-4372-9662-489e478c6880"}},"options":{}}}
{"t":{"$date":"2020-12-25T22:52:57.608-07:00"},"s":"I",  "c":"INDEX",    "id":20345,   "ctx":"conn8","msg":"Index build: done building","attr":{"buildUUID":null,"namespace":"meta_db.cache","index":"_id_","commitTimestamp":{"$timestamp":{"t":0,"i":0}}}}
{"t":{"$date":"2020-12-25T22:52:57.608-07:00"},"s":"I",  "c":"INDEX",    "id":20438,   "ctx":"conn8","msg":"Index build: registering","attr":{"buildUUID":{"uuid":{"$uuid":"6033cc2b-6117-4c96-bc22-14140c7d6b2e"}},"namespace":"meta_db.cache","collectionUUID":{"uuid":{"$uuid":"c6171757-c33b-4372-9662-489e478c6880"}},"indexes":1,"firstIndex":{"name":"date_1"}}}
{"t":{"$date":"2020-12-25T22:52:57.633-07:00"},"s":"I",  "c":"INDEX",    "id":20345,   "ctx":"conn8","msg":"Index build: done building","attr":{"buildUUID":null,"namespace":"meta_db.cache","index":"date_1","commitTimestamp":{"$timestamp":{"t":0,"i":0}}}}
{"t":{"$date":"2020-12-25T22:52:57.633-07:00"},"s":"I",  "c":"INDEX",    "id":20440,   "ctx":"conn8","msg":"Index build: waiting for index build to complete","attr":{"buildUUID":{"uuid":{"$uuid":"6033cc2b-6117-4c96-bc22-14140c7d6b2e"}},"deadline":{"$date":{"$numberLong":"9223372036854775807"}}}}
{"t":{"$date":"2020-12-25T22:52:57.634-07:00"},"s":"I",  "c":"INDEX",    "id":20447,   "ctx":"conn8","msg":"Index build: completed","attr":{"buildUUID":{"uuid":{"$uuid":"6033cc2b-6117-4c96-bc22-14140c7d6b2e"}}}}
{"t":{"$date":"2020-12-25T22:52:57.636-07:00"},"s":"I",  "c":"STORAGE",  "id":20320,   "ctx":"conn8","msg":"createCollection","attr":{"namespace":"arctic_test.toplevel_tickstore.ARCTIC","uuidDisposition":"generated","uuid":{"uuid":{"$uuid":"bfb28988-1f1b-4130-a0e2-888153fe6e87"}},"options":{}}}
{"t":{"$date":"2020-12-25T22:52:57.702-07:00"},"s":"I",  "c":"INDEX",    "id":20345,   "ctx":"conn8","msg":"Index build: done building","attr":{"buildUUID":null,"namespace":"arctic_test.toplevel_tickstore.ARCTIC","index":"_id_","commitTimestamp":{"$timestamp":{"t":0,"i":0}}}}
{"t":{"$date":"2020-12-25T22:52:57.705-07:00"},"s":"I",  "c":"STORAGE",  "id":20320,   "ctx":"conn8","msg":"createCollection","attr":{"namespace":"arctic_test.toplevel_tickstore","uuidDisposition":"generated","uuid":{"uuid":{"$uuid":"606caee4-71a3-47ab-aafb-39fd07a073db"}},"options":{}}}
{"t":{"$date":"2020-12-25T22:52:57.814-07:00"},"s":"I",  "c":"INDEX",    "id":20345,   "ctx":"conn8","msg":"Index build: done building","attr":{"buildUUID":null,"namespace":"arctic_test.toplevel_tickstore","index":"_id_","commitTimestamp":{"$timestamp":{"t":0,"i":0}}}}
{"t":{"$date":"2020-12-25T22:52:57.814-07:00"},"s":"I",  "c":"INDEX",    "id":20345,   "ctx":"conn8","msg":"Index build: done building","attr":{"buildUUID":null,"namespace":"arctic_test.toplevel_tickstore","index":"start_1","commitTimestamp":{"$timestamp":{"t":0,"i":0}}}}
{"t":{"$date":"2020-12-25T22:52:57.814-07:00"},"s":"I",  "c":"COMMAND",  "id":51803,   "ctx":"conn8","msg":"Slow query","attr":{"type":"command","ns":"arctic_test.toplevel_tickstore","command":{"createIndexes":"toplevel_tickstore","indexes":[{"background":true,"name":"start_1","key":{"start":1}}],"lsid":{"id":{"$uuid":"48ea4d44-0686-4bce-b5a7-cf78a973c79a"}},"$db":"arctic_test","$readPreference":{"mode":"primary"}},"numYields":0,"reslen":114,"locks":{"ParallelBatchWriterMode":{"acquireCount":{"r":5}},"ReplicationStateTransition":{"acquireCount":{"w":5}},"Global":{"acquireCount":{"r":2,"w":3}},"Database":{"acquireCount":{"r":2,"w":3}},"Collection":{"acquireCount":{"r":4,"w":2}},"Mutex":{"acquireCount":{"r":5}}},"flowControl":{"acquireCount":1},"storage":{},"protocol":"op_msg","durationMillis":108}}
--------------------------------------------------- Captured log setup ---------------------------------------------------
DEBUG    pytest_shutil.workspace:workspace.py:52 
DEBUG    pytest_shutil.workspace:workspace.py:53 =======================================================
DEBUG    pytest_shutil.workspace:workspace.py:56 pytest_shutil created workspace /tmp/tmpwm4nsk6r
DEBUG    pytest_shutil.workspace:workspace.py:64 This workspace will delete itself on teardown
DEBUG    pytest_shutil.workspace:workspace.py:65 =======================================================
DEBUG    pytest_shutil.workspace:workspace.py:66 
DEBUG    pytest_server_fixtures.serverclass.thread:thread.py:77 Launching thread server.
DEBUG    pytest_server_fixtures.serverclass.thread:thread.py:89 Running server: mongod --bind_ip=127.150.242.244 --port=19579 --nounixsocket --syncdelay=0 --nojournal --quiet --dbpath=/tmp/tmpwm4nsk6r
DEBUG    pytest_server_fixtures.serverclass.thread:thread.py:90 CWD: /home/cwm/git/bb.FLXSA/quant/arctic_venv36
DEBUG    pytest_server_fixtures.base2:base2.py:226 sleeping for 0.1 before retrying (1 of 28)
INFO     pytest_server_fixtures.mongo:mongo.py:128 Connecting to Mongo at 127.150.242.244:19579
DEBUG    pytest_server_fixtures.base2:base2.py:226 sleeping for 0.1 before retrying (2 of 28)
INFO     pytest_server_fixtures.mongo:mongo.py:128 Connecting to Mongo at 127.150.242.244:19579
DEBUG    pytest_server_fixtures.base2:base2.py:226 sleeping for 0.1 before retrying (3 of 28)
INFO     pytest_server_fixtures.mongo:mongo.py:128 Connecting to Mongo at 127.150.242.244:19579
DEBUG    pytest_server_fixtures.base2:base2.py:229 waited 0:00:01.212868 for server to start successfully
DEBUG    pytest_server_fixtures.base2:base2.py:69 Server now awake
INFO     arctic.fixtures.arctic:arctic.py:23 arctic.fixtures: arctic init(mongo_server.api=MongoClient(host=['127.150.242.244:19579'], document_class=dict, tz_aware=False, connect=True))
DEBUG    root:arctic.py:234 Cache has expired data, fetching from slow path and reloading cache.
-------------------------------------------------- Captured stdout call --------------------------------------------------
{"t":{"$date":"2020-12-25T22:52:57.820-07:00"},"s":"I",  "c":"STORAGE",  "id":20320,   "ctx":"conn8","msg":"createCollection","attr":{"namespace":"arctic_FEED_2010.LEVEL1.ARCTIC","uuidDisposition":"generated","uuid":{"uuid":{"$uuid":"871f9172-8643-4fdf-856c-fc9ba83f03e6"}},"options":{}}}
{"t":{"$date":"2020-12-25T22:52:57.878-07:00"},"s":"I",  "c":"INDEX",    "id":20345,   "ctx":"conn8","msg":"Index build: done building","attr":{"buildUUID":null,"namespace":"arctic_FEED_2010.LEVEL1.ARCTIC","index":"_id_","commitTimestamp":{"$timestamp":{"t":0,"i":0}}}}
{"t":{"$date":"2020-12-25T22:52:57.880-07:00"},"s":"I",  "c":"STORAGE",  "id":20320,   "ctx":"conn8","msg":"createCollection","attr":{"namespace":"arctic_FEED_2010.LEVEL1","uuidDisposition":"generated","uuid":{"uuid":{"$uuid":"4ce3b93c-799e-4e04-90c7-336c1b3ee754"}},"options":{}}}
{"t":{"$date":"2020-12-25T22:52:57.930-07:00"},"s":"I",  "c":"-",        "id":20883,   "ctx":"conn1","msg":"Interrupted operation as its client disconnected","attr":{"opId":13}}
{"t":{"$date":"2020-12-25T22:52:57.979-07:00"},"s":"I",  "c":"INDEX",    "id":20345,   "ctx":"conn8","msg":"Index build: done building","attr":{"buildUUID":null,"namespace":"arctic_FEED_2010.LEVEL1","index":"_id_","commitTimestamp":{"$timestamp":{"t":0,"i":0}}}}
{"t":{"$date":"2020-12-25T22:52:57.979-07:00"},"s":"I",  "c":"INDEX",    "id":20345,   "ctx":"conn8","msg":"Index build: done building","attr":{"buildUUID":null,"namespace":"arctic_FEED_2010.LEVEL1","index":"sy_1_s_1","commitTimestamp":{"$timestamp":{"t":0,"i":0}}}}
{"t":{"$date":"2020-12-25T22:52:57.980-07:00"},"s":"I",  "c":"INDEX",    "id":20438,   "ctx":"conn8","msg":"Index build: registering","attr":{"buildUUID":{"uuid":{"$uuid":"8be03a5e-cac1-4555-8d6c-069f6d5523f2"}},"namespace":"arctic_FEED_2010.LEVEL1","collectionUUID":{"uuid":{"$uuid":"4ce3b93c-799e-4e04-90c7-336c1b3ee754"}},"indexes":1,"firstIndex":{"name":"s_1"}}}
{"t":{"$date":"2020-12-25T22:52:58.004-07:00"},"s":"I",  "c":"INDEX",    "id":20345,   "ctx":"conn8","msg":"Index build: done building","attr":{"buildUUID":null,"namespace":"arctic_FEED_2010.LEVEL1","index":"s_1","commitTimestamp":{"$timestamp":{"t":0,"i":0}}}}
{"t":{"$date":"2020-12-25T22:52:58.004-07:00"},"s":"I",  "c":"INDEX",    "id":20440,   "ctx":"conn8","msg":"Index build: waiting for index build to complete","attr":{"buildUUID":{"uuid":{"$uuid":"8be03a5e-cac1-4555-8d6c-069f6d5523f2"}},"deadline":{"$date":{"$numberLong":"9223372036854775807"}}}}
{"t":{"$date":"2020-12-25T22:52:58.004-07:00"},"s":"I",  "c":"INDEX",    "id":20447,   "ctx":"conn8","msg":"Index build: completed","attr":{"buildUUID":{"uuid":{"$uuid":"8be03a5e-cac1-4555-8d6c-069f6d5523f2"}}}}
{"t":{"$date":"2020-12-25T22:52:58.005-07:00"},"s":"I",  "c":"STORAGE",  "id":20320,   "ctx":"conn8","msg":"createCollection","attr":{"namespace":"arctic_FEED_2010.LEVEL1.metadata","uuidDisposition":"generated","uuid":{"uuid":{"$uuid":"6ee752ae-5244-4b70-a825-b0c17cefc512"}},"options":{}}}
{"t":{"$date":"2020-12-25T22:52:58.032-07:00"},"s":"I",  "c":"-",        "id":20883,   "ctx":"conn3","msg":"Interrupted operation as its client disconnected","attr":{"opId":16}}
{"t":{"$date":"2020-12-25T22:52:58.100-07:00"},"s":"I",  "c":"INDEX",    "id":20345,   "ctx":"conn8","msg":"Index build: done building","attr":{"buildUUID":null,"namespace":"arctic_FEED_2010.LEVEL1.metadata","index":"_id_","commitTimestamp":{"$timestamp":{"t":0,"i":0}}}}
{"t":{"$date":"2020-12-25T22:52:58.100-07:00"},"s":"I",  "c":"INDEX",    "id":20345,   "ctx":"conn8","msg":"Index build: done building","attr":{"buildUUID":null,"namespace":"arctic_FEED_2010.LEVEL1.metadata","index":"sy_1","commitTimestamp":{"$timestamp":{"t":0,"i":0}}}}
------------------------------------------------- Captured log teardown --------------------------------------------------
DEBUG    pytest_server_fixtures.serverclass.thread:thread.py:54 Killing process tree for 3878 (total_procs_to_kill=1)
DEBUG    pytest_server_fixtures.serverclass.thread:thread.py:35 Killing 1 processes with signal Signals.SIGKILL
DEBUG    pytest_server_fixtures.serverclass.thread:thread.py:39 Waiting for 1 processes to die
DEBUG    pytest_server_fixtures.serverclass.thread:thread.py:43 All processes are terminated
DEBUG    pytest_shutil.workspace:workspace.py:140 
DEBUG    pytest_shutil.workspace:workspace.py:141 =======================================================
DEBUG    pytest_shutil.workspace:workspace.py:142 pytest_shutil deleting workspace /tmp/tmpwm4nsk6r
DEBUG    pytest_shutil.workspace:workspace.py:143 =======================================================
DEBUG    pytest_shutil.workspace:workspace.py:144
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
------------------------------------------------- Captured stdout setup --------------------------------------------------
{"t":{"$date":"2020-12-25T22:53:12.821-07:00"},"s":"I",  "c":"CONTROL",  "id":23285,   "ctx":"main","msg":"Automatically disabling TLS 1.0, to force-enable TLS 1.0 specify --sslDisabledProtocols 'none'"}
{"t":{"$date":"2020-12-25T22:53:12.823-07:00"},"s":"W",  "c":"ASIO",     "id":22601,   "ctx":"main","msg":"No TransportLayer configured during NetworkInterface startup"}
{"t":{"$date":"2020-12-25T22:53:12.824-07:00"},"s":"I",  "c":"NETWORK",  "id":4648601, "ctx":"main","msg":"Implicit TCP FastOpen unavailable. If TCP FastOpen is required, set tcpFastOpenServer, tcpFastOpenClient, and tcpFastOpenQueueSize."}
{"t":{"$date":"2020-12-25T22:53:12.824-07:00"},"s":"I",  "c":"STORAGE",  "id":4615611, "ctx":"initandlisten","msg":"MongoDB starting","attr":{"pid":4314,"port":29045,"dbPath":"/tmp/tmp4e22l3s4","architecture":"64-bit","host":"flxsa02"}}
{"t":{"$date":"2020-12-25T22:53:12.824-07:00"},"s":"I",  "c":"CONTROL",  "id":23403,   "ctx":"initandlisten","msg":"Build Info","attr":{"buildInfo":{"version":"4.4.2","gitVersion":"15e73dc5738d2278b688f8929aee605fe4279b0e","openSSLVersion":"OpenSSL 1.0.2g  1 Mar 2016","modules":[],"allocator":"tcmalloc","environment":{"distmod":"ubuntu1604","distarch":"x86_64","target_arch":"x86_64"}}}}
{"t":{"$date":"2020-12-25T22:53:12.824-07:00"},"s":"I",  "c":"CONTROL",  "id":51765,   "ctx":"initandlisten","msg":"Operating System","attr":{"os":{"name":"Ubuntu","version":"16.04"}}}
{"t":{"$date":"2020-12-25T22:53:12.824-07:00"},"s":"I",  "c":"CONTROL",  "id":21951,   "ctx":"initandlisten","msg":"Options set by command line","attr":{"options":{"net":{"bindIp":"127.150.242.244","port":29045,"unixDomainSocket":{"enabled":false}},"storage":{"dbPath":"/tmp/tmp4e22l3s4","journal":{"enabled":false},"syncPeriodSecs":0.0},"systemLog":{"quiet":true}}}}
{"t":{"$date":"2020-12-25T22:53:12.825-07:00"},"s":"I",  "c":"STORAGE",  "id":22297,   "ctx":"initandlisten","msg":"Using the XFS filesystem is strongly recommended with the WiredTiger storage engine. See http://dochub.mongodb.org/core/prodnotes-filesystem","tags":["startupWarnings"]}
{"t":{"$date":"2020-12-25T22:53:12.825-07:00"},"s":"I",  "c":"STORAGE",  "id":22315,   "ctx":"initandlisten","msg":"Opening WiredTiger","attr":{"config":"create,cache_size=11497M,session_max=33000,eviction=(threads_min=4,threads_max=4),config_base=false,statistics=(fast),log=(enabled=true,archive=true,path=journal,compressor=snappy),file_manager=(close_idle_time=100000,close_scan_interval=10,close_handle_minimum=250),statistics_log=(wait=0),verbose=[recovery_progress,checkpoint_progress,compact_progress],,log=(enabled=false),"}}
{"t":{"$date":"2020-12-25T22:53:13.374-07:00"},"s":"I",  "c":"STORAGE",  "id":22430,   "ctx":"initandlisten","msg":"WiredTiger message","attr":{"message":"[1608961993:374749][4314:0x7fb6b1f4fa80], txn-recover: [WT_VERB_RECOVERY | WT_VERB_RECOVERY_PROGRESS] Set global recovery timestamp: (0, 0)"}}
{"t":{"$date":"2020-12-25T22:53:13.374-07:00"},"s":"I",  "c":"STORAGE",  "id":22430,   "ctx":"initandlisten","msg":"WiredTiger message","attr":{"message":"[1608961993:374796][4314:0x7fb6b1f4fa80], txn-recover: [WT_VERB_RECOVERY | WT_VERB_RECOVERY_PROGRESS] Set global oldest timestamp: (0, 0)"}}
{"t":{"$date":"2020-12-25T22:53:13.416-07:00"},"s":"I",  "c":"STORAGE",  "id":4795906, "ctx":"initandlisten","msg":"WiredTiger opened","attr":{"durationMillis":591}}
{"t":{"$date":"2020-12-25T22:53:13.416-07:00"},"s":"I",  "c":"RECOVERY", "id":23987,   "ctx":"initandlisten","msg":"WiredTiger recoveryTimestamp","attr":{"recoveryTimestamp":{"$timestamp":{"t":0,"i":0}}}}
{"t":{"$date":"2020-12-25T22:53:13.478-07:00"},"s":"I",  "c":"STORAGE",  "id":4366408, "ctx":"initandlisten","msg":"No table logging settings modifications are required for existing WiredTiger tables","attr":{"loggingEnabled":true}}
{"t":{"$date":"2020-12-25T22:53:13.478-07:00"},"s":"I",  "c":"STORAGE",  "id":22262,   "ctx":"initandlisten","msg":"Timestamp monitor starting"}
{"t":{"$date":"2020-12-25T22:53:13.495-07:00"},"s":"W",  "c":"CONTROL",  "id":22120,   "ctx":"initandlisten","msg":"Access control is not enabled for the database. Read and write access to data and configuration is unrestricted","tags":["startupWarnings"]}
{"t":{"$date":"2020-12-25T22:53:13.495-07:00"},"s":"W",  "c":"CONTROL",  "id":22184,   "ctx":"initandlisten","msg":"Soft rlimits too low","attr":{"currentValue":1024,"recommendedMinimum":64000},"tags":["startupWarnings"]}
{"t":{"$date":"2020-12-25T22:53:13.495-07:00"},"s":"I",  "c":"STORAGE",  "id":20320,   "ctx":"initandlisten","msg":"createCollection","attr":{"namespace":"admin.system.version","uuidDisposition":"provided","uuid":{"uuid":{"$uuid":"e4dcfa41-2871-4b71-9cc2-28b306dff162"}},"options":{"uuid":{"$uuid":"e4dcfa41-2871-4b71-9cc2-28b306dff162"}}}}
{"t":{"$date":"2020-12-25T22:53:13.559-07:00"},"s":"I",  "c":"INDEX",    "id":20345,   "ctx":"initandlisten","msg":"Index build: done building","attr":{"buildUUID":null,"namespace":"admin.system.version","index":"_id_","commitTimestamp":{"$timestamp":{"t":0,"i":0}}}}
{"t":{"$date":"2020-12-25T22:53:13.559-07:00"},"s":"I",  "c":"COMMAND",  "id":20459,   "ctx":"initandlisten","msg":"Setting featureCompatibilityVersion","attr":{"newVersion":"4.4"}}
{"t":{"$date":"2020-12-25T22:53:13.560-07:00"},"s":"I",  "c":"STORAGE",  "id":20536,   "ctx":"initandlisten","msg":"Flow Control is enabled on this deployment"}
{"t":{"$date":"2020-12-25T22:53:13.560-07:00"},"s":"I",  "c":"STORAGE",  "id":20320,   "ctx":"initandlisten","msg":"createCollection","attr":{"namespace":"local.startup_log","uuidDisposition":"generated","uuid":{"uuid":{"$uuid":"6ac9753c-1cd5-4d1b-bcbc-5aaee038b753"}},"options":{"capped":true,"size":10485760}}}
{"t":{"$date":"2020-12-25T22:53:13.617-07:00"},"s":"I",  "c":"INDEX",    "id":20345,   "ctx":"initandlisten","msg":"Index build: done building","attr":{"buildUUID":null,"namespace":"local.startup_log","index":"_id_","commitTimestamp":{"$timestamp":{"t":0,"i":0}}}}
{"t":{"$date":"2020-12-25T22:53:13.617-07:00"},"s":"I",  "c":"FTDC",     "id":20625,   "ctx":"initandlisten","msg":"Initializing full-time diagnostic data capture","attr":{"dataDirectory":"/tmp/tmp4e22l3s4/diagnostic.data"}}
{"t":{"$date":"2020-12-25T22:53:13.618-07:00"},"s":"I",  "c":"NETWORK",  "id":23015,   "ctx":"listener","msg":"Listening on","attr":{"address":"127.150.242.244"}}
{"t":{"$date":"2020-12-25T22:53:13.618-07:00"},"s":"I",  "c":"NETWORK",  "id":23016,   "ctx":"listener","msg":"Waiting for connections","attr":{"port":29045,"ssl":"off"}}
{"t":{"$date":"2020-12-25T22:53:13.618-07:00"},"s":"I",  "c":"CONTROL",  "id":20712,   "ctx":"LogicalSessionCacheReap","msg":"Sessions collection is not set up; waiting until next sessions reap interval","attr":{"error":"NamespaceNotFound: config.system.sessions does not exist"}}
{"t":{"$date":"2020-12-25T22:53:13.619-07:00"},"s":"I",  "c":"STORAGE",  "id":20320,   "ctx":"LogicalSessionCacheRefresh","msg":"createCollection","attr":{"namespace":"config.system.sessions","uuidDisposition":"generated","uuid":{"uuid":{"$uuid":"5bde3e36-fd46-4100-b181-fc5f6176f207"}},"options":{}}}
{"t":{"$date":"2020-12-25T22:53:13.710-07:00"},"s":"I",  "c":"INDEX",    "id":20345,   "ctx":"LogicalSessionCacheRefresh","msg":"Index build: done building","attr":{"buildUUID":null,"namespace":"config.system.sessions","index":"_id_","commitTimestamp":{"$timestamp":{"t":0,"i":0}}}}
{"t":{"$date":"2020-12-25T22:53:13.710-07:00"},"s":"I",  "c":"INDEX",    "id":20345,   "ctx":"LogicalSessionCacheRefresh","msg":"Index build: done building","attr":{"buildUUID":null,"namespace":"config.system.sessions","index":"lsidTTLIndex","commitTimestamp":{"$timestamp":{"t":0,"i":0}}}}
{"t":{"$date":"2020-12-25T22:53:13.896-07:00"},"s":"I",  "c":"NETWORK",  "id":51800,   "ctx":"conn1","msg":"client metadata","attr":{"remote":"127.0.0.1:37124","client":"conn1","doc":{"driver":{"name":"PyMongo","version":"3.11.2"},"os":{"type":"Linux","name":"Linux","architecture":"x86_64","version":"4.15.0-128-generic"},"platform":"CPython 3.6.12.final.0"}}}
{"t":{"$date":"2020-12-25T22:53:13.897-07:00"},"s":"I",  "c":"NETWORK",  "id":51800,   "ctx":"conn2","msg":"client metadata","attr":{"remote":"127.0.0.1:37126","client":"conn2","doc":{"driver":{"name":"PyMongo","version":"3.11.2"},"os":{"type":"Linux","name":"Linux","architecture":"x86_64","version":"4.15.0-128-generic"},"platform":"CPython 3.6.12.final.0"}}}
{"t":{"$date":"2020-12-25T22:53:13.999-07:00"},"s":"I",  "c":"NETWORK",  "id":51800,   "ctx":"conn3","msg":"client metadata","attr":{"remote":"127.0.0.1:37128","client":"conn3","doc":{"driver":{"name":"PyMongo","version":"3.11.2"},"os":{"type":"Linux","name":"Linux","architecture":"x86_64","version":"4.15.0-128-generic"},"platform":"CPython 3.6.12.final.0"}}}
{"t":{"$date":"2020-12-25T22:53:14.002-07:00"},"s":"I",  "c":"NETWORK",  "id":51800,   "ctx":"conn4","msg":"client metadata","attr":{"remote":"127.0.0.1:37130","client":"conn4","doc":{"driver":{"name":"PyMongo","version":"3.11.2"},"os":{"type":"Linux","name":"Linux","architecture":"x86_64","version":"4.15.0-128-generic"},"platform":"CPython 3.6.12.final.0"}}}
{"t":{"$date":"2020-12-25T22:53:14.002-07:00"},"s":"I",  "c":"NETWORK",  "id":51800,   "ctx":"conn5","msg":"client metadata","attr":{"remote":"127.0.0.1:37132","client":"conn5","doc":{"driver":{"name":"PyMongo","version":"3.11.2"},"os":{"type":"Linux","name":"Linux","architecture":"x86_64","version":"4.15.0-128-generic"},"platform":"CPython 3.6.12.final.0"}}}
{"t":{"$date":"2020-12-25T22:53:14.006-07:00"},"s":"I",  "c":"NETWORK",  "id":51800,   "ctx":"conn6","msg":"client metadata","attr":{"remote":"127.0.0.1:37134","client":"conn6","doc":{"driver":{"name":"PyMongo","version":"3.11.2"},"os":{"type":"Linux","name":"Linux","architecture":"x86_64","version":"4.15.0-128-generic"},"platform":"CPython 3.6.12.final.0"}}}
{"t":{"$date":"2020-12-25T22:53:14.008-07:00"},"s":"I",  "c":"NETWORK",  "id":51800,   "ctx":"conn7","msg":"client metadata","attr":{"remote":"127.0.0.1:37136","client":"conn7","doc":{"driver":{"name":"PyMongo","version":"3.11.2"},"os":{"type":"Linux","name":"Linux","architecture":"x86_64","version":"4.15.0-128-generic"},"platform":"CPython 3.6.12.final.0"}}}
{"t":{"$date":"2020-12-25T22:53:14.008-07:00"},"s":"I",  "c":"NETWORK",  "id":51800,   "ctx":"conn8","msg":"client metadata","attr":{"remote":"127.0.0.1:37138","client":"conn8","doc":{"driver":{"name":"PyMongo","version":"3.11.2"},"os":{"type":"Linux","name":"Linux","architecture":"x86_64","version":"4.15.0-128-generic"},"platform":"CPython 3.6.12.final.0"}}}
{"t":{"$date":"2020-12-25T22:53:14.011-07:00"},"s":"I",  "c":"STORAGE",  "id":20320,   "ctx":"conn8","msg":"createCollection","attr":{"namespace":"meta_db.cache","uuidDisposition":"generated","uuid":{"uuid":{"$uuid":"ae3314bf-31ab-49e0-9253-c967a9729a23"}},"options":{}}}
{"t":{"$date":"2020-12-25T22:53:14.080-07:00"},"s":"I",  "c":"INDEX",    "id":20345,   "ctx":"conn8","msg":"Index build: done building","attr":{"buildUUID":null,"namespace":"meta_db.cache","index":"_id_","commitTimestamp":{"$timestamp":{"t":0,"i":0}}}}
{"t":{"$date":"2020-12-25T22:53:14.081-07:00"},"s":"I",  "c":"INDEX",    "id":20438,   "ctx":"conn8","msg":"Index build: registering","attr":{"buildUUID":{"uuid":{"$uuid":"23492d71-082f-4327-8a58-9ca7d3ce518c"}},"namespace":"meta_db.cache","collectionUUID":{"uuid":{"$uuid":"ae3314bf-31ab-49e0-9253-c967a9729a23"}},"indexes":1,"firstIndex":{"name":"date_1"}}}
{"t":{"$date":"2020-12-25T22:53:14.106-07:00"},"s":"I",  "c":"INDEX",    "id":20345,   "ctx":"conn8","msg":"Index build: done building","attr":{"buildUUID":null,"namespace":"meta_db.cache","index":"date_1","commitTimestamp":{"$timestamp":{"t":0,"i":0}}}}
{"t":{"$date":"2020-12-25T22:53:14.106-07:00"},"s":"I",  "c":"INDEX",    "id":20440,   "ctx":"conn8","msg":"Index build: waiting for index build to complete","attr":{"buildUUID":{"uuid":{"$uuid":"23492d71-082f-4327-8a58-9ca7d3ce518c"}},"deadline":{"$date":{"$numberLong":"9223372036854775807"}}}}
{"t":{"$date":"2020-12-25T22:53:14.106-07:00"},"s":"I",  "c":"INDEX",    "id":20447,   "ctx":"conn8","msg":"Index build: completed","attr":{"buildUUID":{"uuid":{"$uuid":"23492d71-082f-4327-8a58-9ca7d3ce518c"}}}}
--------------------------------------------------- Captured log setup ---------------------------------------------------
DEBUG    pytest_shutil.workspace:workspace.py:52 
DEBUG    pytest_shutil.workspace:workspace.py:53 =======================================================
DEBUG    pytest_shutil.workspace:workspace.py:56 pytest_shutil created workspace /tmp/tmp4e22l3s4
DEBUG    pytest_shutil.workspace:workspace.py:64 This workspace will delete itself on teardown
DEBUG    pytest_shutil.workspace:workspace.py:65 =======================================================
DEBUG    pytest_shutil.workspace:workspace.py:66 
DEBUG    pytest_server_fixtures.serverclass.thread:thread.py:77 Launching thread server.
DEBUG    pytest_server_fixtures.serverclass.thread:thread.py:89 Running server: mongod --bind_ip=127.150.242.244 --port=29045 --nounixsocket --syncdelay=0 --nojournal --quiet --dbpath=/tmp/tmp4e22l3s4
DEBUG    pytest_server_fixtures.serverclass.thread:thread.py:90 CWD: /home/cwm/git/bb.FLXSA/quant/arctic_venv36
DEBUG    pytest_server_fixtures.base2:base2.py:226 sleeping for 0.1 before retrying (1 of 28)
INFO     pytest_server_fixtures.mongo:mongo.py:128 Connecting to Mongo at 127.150.242.244:29045
DEBUG    pytest_server_fixtures.base2:base2.py:226 sleeping for 0.1 before retrying (2 of 28)
INFO     pytest_server_fixtures.mongo:mongo.py:128 Connecting to Mongo at 127.150.242.244:29045
DEBUG    pytest_server_fixtures.base2:base2.py:226 sleeping for 0.1 before retrying (3 of 28)
INFO     pytest_server_fixtures.mongo:mongo.py:128 Connecting to Mongo at 127.150.242.244:29045
DEBUG    pytest_server_fixtures.base2:base2.py:229 waited 0:00:01.216752 for server to start successfully
DEBUG    pytest_server_fixtures.base2:base2.py:69 Server now awake
INFO     arctic.fixtures.arctic:arctic.py:23 arctic.fixtures: arctic init(mongo_server.api=MongoClient(host=['127.150.242.244:29045'], document_class=dict, tz_aware=False, connect=True))
-------------------------------------------------- Captured stdout call --------------------------------------------------
{"t":{"$date":"2020-12-25T22:53:14.108-07:00"},"s":"I",  "c":"STORAGE",  "id":20320,   "ctx":"conn8","msg":"createCollection","attr":{"namespace":"arctic_FEED_2010.LEVEL1.ARCTIC","uuidDisposition":"generated","uuid":{"uuid":{"$uuid":"d3eb570a-4cd2-4e5f-8c40-f008c804d368"}},"options":{}}}
{"t":{"$date":"2020-12-25T22:53:14.174-07:00"},"s":"I",  "c":"INDEX",    "id":20345,   "ctx":"conn8","msg":"Index build: done building","attr":{"buildUUID":null,"namespace":"arctic_FEED_2010.LEVEL1.ARCTIC","index":"_id_","commitTimestamp":{"$timestamp":{"t":0,"i":0}}}}
{"t":{"$date":"2020-12-25T22:53:14.175-07:00"},"s":"I",  "c":"STORAGE",  "id":20320,   "ctx":"conn8","msg":"createCollection","attr":{"namespace":"arctic_FEED_2010.LEVEL1","uuidDisposition":"generated","uuid":{"uuid":{"$uuid":"53a000d2-12fe-46bd-9550-396c96a716cc"}},"options":{}}}
{"t":{"$date":"2020-12-25T22:53:14.290-07:00"},"s":"I",  "c":"INDEX",    "id":20345,   "ctx":"conn8","msg":"Index build: done building","attr":{"buildUUID":null,"namespace":"arctic_FEED_2010.LEVEL1","index":"_id_","commitTimestamp":{"$timestamp":{"t":0,"i":0}}}}
{"t":{"$date":"2020-12-25T22:53:14.290-07:00"},"s":"I",  "c":"INDEX",    "id":20345,   "ctx":"conn8","msg":"Index build: done building","attr":{"buildUUID":null,"namespace":"arctic_FEED_2010.LEVEL1","index":"sy_1_s_1","commitTimestamp":{"$timestamp":{"t":0,"i":0}}}}
{"t":{"$date":"2020-12-25T22:53:14.290-07:00"},"s":"I",  "c":"COMMAND",  "id":51803,   "ctx":"conn8","msg":"Slow query","attr":{"type":"command","ns":"arctic_FEED_2010.LEVEL1","command":{"createIndexes":"LEVEL1","indexes":[{"background":true,"name":"sy_1_s_1","key":{"sy":1,"s":1}}],"lsid":{"id":{"$uuid":"18ffce66-4e8b-404b-a639-415b4c08f59e"}},"$db":"arctic_FEED_2010","$readPreference":{"mode":"primary"}},"numYields":0,"reslen":114,"locks":{"ParallelBatchWriterMode":{"acquireCount":{"r":5}},"ReplicationStateTransition":{"acquireCount":{"w":5}},"Global":{"acquireCount":{"r":2,"w":3}},"Database":{"acquireCount":{"r":2,"w":3}},"Collection":{"acquireCount":{"r":4,"w":2}},"Mutex":{"acquireCount":{"r":5}}},"flowControl":{"acquireCount":1},"storage":{},"protocol":"op_msg","durationMillis":114}}
{"t":{"$date":"2020-12-25T22:53:14.291-07:00"},"s":"I",  "c":"INDEX",    "id":20438,   "ctx":"conn8","msg":"Index build: registering","attr":{"buildUUID":{"uuid":{"$uuid":"f4bc111e-7248-4531-9dac-e62f23571284"}},"namespace":"arctic_FEED_2010.LEVEL1","collectionUUID":{"uuid":{"$uuid":"53a000d2-12fe-46bd-9550-396c96a716cc"}},"indexes":1,"firstIndex":{"name":"s_1"}}}
{"t":{"$date":"2020-12-25T22:53:14.324-07:00"},"s":"I",  "c":"INDEX",    "id":20345,   "ctx":"conn8","msg":"Index build: done building","attr":{"buildUUID":null,"namespace":"arctic_FEED_2010.LEVEL1","index":"s_1","commitTimestamp":{"$timestamp":{"t":0,"i":0}}}}
{"t":{"$date":"2020-12-25T22:53:14.324-07:00"},"s":"I",  "c":"INDEX",    "id":20440,   "ctx":"conn8","msg":"Index build: waiting for index build to complete","attr":{"buildUUID":{"uuid":{"$uuid":"f4bc111e-7248-4531-9dac-e62f23571284"}},"deadline":{"$date":{"$numberLong":"9223372036854775807"}}}}
{"t":{"$date":"2020-12-25T22:53:14.324-07:00"},"s":"I",  "c":"INDEX",    "id":20447,   "ctx":"conn8","msg":"Index build: completed","attr":{"buildUUID":{"uuid":{"$uuid":"f4bc111e-7248-4531-9dac-e62f23571284"}}}}
{"t":{"$date":"2020-12-25T22:53:14.325-07:00"},"s":"I",  "c":"STORAGE",  "id":20320,   "ctx":"conn8","msg":"createCollection","attr":{"namespace":"arctic_FEED_2010.LEVEL1.metadata","uuidDisposition":"generated","uuid":{"uuid":{"$uuid":"5eb76f05-2413-4c40-bfc7-6c7ff86fcc02"}},"options":{}}}
{"t":{"$date":"2020-12-25T22:53:14.397-07:00"},"s":"I",  "c":"-",        "id":20883,   "ctx":"conn1","msg":"Interrupted operation as its client disconnected","attr":{"opId":13}}
{"t":{"$date":"2020-12-25T22:53:14.419-07:00"},"s":"I",  "c":"INDEX",    "id":20345,   "ctx":"conn8","msg":"Index build: done building","attr":{"buildUUID":null,"namespace":"arctic_FEED_2010.LEVEL1.metadata","index":"_id_","commitTimestamp":{"$timestamp":{"t":0,"i":0}}}}
{"t":{"$date":"2020-12-25T22:53:14.419-07:00"},"s":"I",  "c":"INDEX",    "id":20345,   "ctx":"conn8","msg":"Index build: done building","attr":{"buildUUID":null,"namespace":"arctic_FEED_2010.LEVEL1.metadata","index":"sy_1","commitTimestamp":{"$timestamp":{"t":0,"i":0}}}}
{"t":{"$date":"2020-12-25T22:53:14.423-07:00"},"s":"I",  "c":"STORAGE",  "id":20320,   "ctx":"conn8","msg":"createCollection","attr":{"namespace":"arctic_FEED_2011.LEVEL1.ARCTIC","uuidDisposition":"generated","uuid":{"uuid":{"$uuid":"e6d56ccf-ce89-42d2-bdb5-4fd9c22c94b0"}},"options":{}}}
{"t":{"$date":"2020-12-25T22:53:14.480-07:00"},"s":"I",  "c":"INDEX",    "id":20345,   "ctx":"conn8","msg":"Index build: done building","attr":{"buildUUID":null,"namespace":"arctic_FEED_2011.LEVEL1.ARCTIC","index":"_id_","commitTimestamp":{"$timestamp":{"t":0,"i":0}}}}
{"t":{"$date":"2020-12-25T22:53:14.481-07:00"},"s":"I",  "c":"STORAGE",  "id":20320,   "ctx":"conn8","msg":"createCollection","attr":{"namespace":"arctic_FEED_2011.LEVEL1","uuidDisposition":"generated","uuid":{"uuid":{"$uuid":"9f201154-851a-4862-a0d3-ffb43061ba61"}},"options":{}}}
{"t":{"$date":"2020-12-25T22:53:14.502-07:00"},"s":"I",  "c":"-",        "id":20883,   "ctx":"conn3","msg":"Interrupted operation as its client disconnected","attr":{"opId":18}}
{"t":{"$date":"2020-12-25T22:53:14.572-07:00"},"s":"I",  "c":"INDEX",    "id":20345,   "ctx":"conn8","msg":"Index build: done building","attr":{"buildUUID":null,"namespace":"arctic_FEED_2011.LEVEL1","index":"_id_","commitTimestamp":{"$timestamp":{"t":0,"i":0}}}}
{"t":{"$date":"2020-12-25T22:53:14.572-07:00"},"s":"I",  "c":"INDEX",    "id":20345,   "ctx":"conn8","msg":"Index build: done building","attr":{"buildUUID":null,"namespace":"arctic_FEED_2011.LEVEL1","index":"sy_1_s_1","commitTimestamp":{"$timestamp":{"t":0,"i":0}}}}
{"t":{"$date":"2020-12-25T22:53:14.573-07:00"},"s":"I",  "c":"INDEX",    "id":20438,   "ctx":"conn8","msg":"Index build: registering","attr":{"buildUUID":{"uuid":{"$uuid":"4c06f2b2-ba06-4e72-99d0-99dd1a42b44b"}},"namespace":"arctic_FEED_2011.LEVEL1","collectionUUID":{"uuid":{"$uuid":"9f201154-851a-4862-a0d3-ffb43061ba61"}},"indexes":1,"firstIndex":{"name":"s_1"}}}
{"t":{"$date":"2020-12-25T22:53:14.608-07:00"},"s":"I",  "c":"INDEX",    "id":20345,   "ctx":"conn8","msg":"Index build: done building","attr":{"buildUUID":null,"namespace":"arctic_FEED_2011.LEVEL1","index":"s_1","commitTimestamp":{"$timestamp":{"t":0,"i":0}}}}
{"t":{"$date":"2020-12-25T22:53:14.608-07:00"},"s":"I",  "c":"INDEX",    "id":20440,   "ctx":"conn8","msg":"Index build: waiting for index build to complete","attr":{"buildUUID":{"uuid":{"$uuid":"4c06f2b2-ba06-4e72-99d0-99dd1a42b44b"}},"deadline":{"$date":{"$numberLong":"9223372036854775807"}}}}
{"t":{"$date":"2020-12-25T22:53:14.608-07:00"},"s":"I",  "c":"INDEX",    "id":20447,   "ctx":"conn8","msg":"Index build: completed","attr":{"buildUUID":{"uuid":{"$uuid":"4c06f2b2-ba06-4e72-99d0-99dd1a42b44b"}}}}
{"t":{"$date":"2020-12-25T22:53:14.608-07:00"},"s":"I",  "c":"STORAGE",  "id":20320,   "ctx":"conn8","msg":"createCollection","attr":{"namespace":"arctic_FEED_2011.LEVEL1.metadata","uuidDisposition":"generated","uuid":{"uuid":{"$uuid":"48664862-001c-4dec-95ae-93ce8a8e2d4c"}},"options":{}}}
{"t":{"$date":"2020-12-25T22:53:14.701-07:00"},"s":"I",  "c":"INDEX",    "id":20345,   "ctx":"conn8","msg":"Index build: done building","attr":{"buildUUID":null,"namespace":"arctic_FEED_2011.LEVEL1.metadata","index":"_id_","commitTimestamp":{"$timestamp":{"t":0,"i":0}}}}
{"t":{"$date":"2020-12-25T22:53:14.701-07:00"},"s":"I",  "c":"INDEX",    "id":20345,   "ctx":"conn8","msg":"Index build: done building","attr":{"buildUUID":null,"namespace":"arctic_FEED_2011.LEVEL1.metadata","index":"sy_1","commitTimestamp":{"$timestamp":{"t":0,"i":0}}}}
{"t":{"$date":"2020-12-25T22:53:14.704-07:00"},"s":"I",  "c":"STORAGE",  "id":20320,   "ctx":"conn8","msg":"createCollection","attr":{"namespace":"arctic_FEED.LEVEL1.ARCTIC","uuidDisposition":"generated","uuid":{"uuid":{"$uuid":"c5944b8a-6239-4ce1-8df5-86791c2b395c"}},"options":{}}}
{"t":{"$date":"2020-12-25T22:53:14.758-07:00"},"s":"I",  "c":"INDEX",    "id":20345,   "ctx":"conn8","msg":"Index build: done building","attr":{"buildUUID":null,"namespace":"arctic_FEED.LEVEL1.ARCTIC","index":"_id_","commitTimestamp":{"$timestamp":{"t":0,"i":0}}}}
{"t":{"$date":"2020-12-25T22:53:14.762-07:00"},"s":"I",  "c":"STORAGE",  "id":20320,   "ctx":"conn8","msg":"createCollection","attr":{"namespace":"arctic_FEED.LEVEL1","uuidDisposition":"generated","uuid":{"uuid":{"$uuid":"846e0dc4-d41a-4b0b-9843-576fb12a0627"}},"options":{}}}
{"t":{"$date":"2020-12-25T22:53:14.820-07:00"},"s":"I",  "c":"INDEX",    "id":20345,   "ctx":"conn8","msg":"Index build: done building","attr":{"buildUUID":null,"namespace":"arctic_FEED.LEVEL1","index":"_id_","commitTimestamp":{"$timestamp":{"t":0,"i":0}}}}
{"t":{"$date":"2020-12-25T22:53:14.824-07:00"},"s":"I",  "c":"INDEX",    "id":20438,   "ctx":"conn8","msg":"Index build: registering","attr":{"buildUUID":{"uuid":{"$uuid":"7827cca2-e416-4dac-b312-3f13d21ec592"}},"namespace":"arctic_FEED.LEVEL1","collectionUUID":{"uuid":{"$uuid":"846e0dc4-d41a-4b0b-9843-576fb12a0627"}},"indexes":1,"firstIndex":{"name":"start_1"}}}
{"t":{"$date":"2020-12-25T22:53:14.881-07:00"},"s":"I",  "c":"INDEX",    "id":20384,   "ctx":"IndexBuildsCoordinatorMongod-0","msg":"Index build: starting","attr":{"namespace":"arctic_FEED.LEVEL1","buildUUID":null,"properties":{"v":2,"key":{"start":1},"name":"start_1","background":true},"method":"Hybrid","maxTemporaryMemoryUsageMB":200}}
{"t":{"$date":"2020-12-25T22:53:14.881-07:00"},"s":"I",  "c":"INDEX",    "id":20440,   "ctx":"conn8","msg":"Index build: waiting for index build to complete","attr":{"buildUUID":{"uuid":{"$uuid":"7827cca2-e416-4dac-b312-3f13d21ec592"}},"deadline":{"$date":{"$numberLong":"9223372036854775807"}}}}
{"t":{"$date":"2020-12-25T22:53:14.881-07:00"},"s":"I",  "c":"INDEX",    "id":20391,   "ctx":"IndexBuildsCoordinatorMongod-0","msg":"Index build: collection scan done","attr":{"buildUUID":null,"totalRecords":2,"durationMillis":0}}
{"t":{"$date":"2020-12-25T22:53:14.882-07:00"},"s":"I",  "c":"INDEX",    "id":20685,   "ctx":"IndexBuildsCoordinatorMongod-0","msg":"Index build: inserted keys from external sorter into index","attr":{"namespace":"arctic_FEED.LEVEL1","index":"start_1","keysInserted":2,"durationMillis":0}}
{"t":{"$date":"2020-12-25T22:53:14.889-07:00"},"s":"I",  "c":"STORAGE",  "id":3856203, "ctx":"IndexBuildsCoordinatorMongod-0","msg":"Index build: waiting for next action before completing final phase","attr":{"buildUUID":{"uuid":{"$uuid":"7827cca2-e416-4dac-b312-3f13d21ec592"}}}}
{"t":{"$date":"2020-12-25T22:53:14.889-07:00"},"s":"I",  "c":"STORAGE",  "id":3856204, "ctx":"IndexBuildsCoordinatorMongod-0","msg":"Index build: received signal","attr":{"buildUUID":{"uuid":{"$uuid":"7827cca2-e416-4dac-b312-3f13d21ec592"}},"action":"Single-phase commit"}}
{"t":{"$date":"2020-12-25T22:53:14.889-07:00"},"s":"I",  "c":"INDEX",    "id":20345,   "ctx":"IndexBuildsCoordinatorMongod-0","msg":"Index build: done building","attr":{"buildUUID":null,"namespace":"arctic_FEED.LEVEL1","index":"start_1","commitTimestamp":{"$timestamp":{"t":0,"i":0}}}}
{"t":{"$date":"2020-12-25T22:53:14.905-07:00"},"s":"I",  "c":"STORAGE",  "id":20663,   "ctx":"IndexBuildsCoordinatorMongod-0","msg":"Index build: completed successfully","attr":{"buildUUID":{"uuid":{"$uuid":"7827cca2-e416-4dac-b312-3f13d21ec592"}},"namespace":"arctic_FEED.LEVEL1","uuid":{"uuid":{"$uuid":"846e0dc4-d41a-4b0b-9843-576fb12a0627"}},"indexesBuilt":1,"numIndexesBefore":1,"numIndexesAfter":2}}
{"t":{"$date":"2020-12-25T22:53:14.905-07:00"},"s":"I",  "c":"INDEX",    "id":20447,   "ctx":"conn8","msg":"Index build: completed","attr":{"buildUUID":{"uuid":{"$uuid":"7827cca2-e416-4dac-b312-3f13d21ec592"}}}}
--------------------------------------------------- Captured log call ----------------------------------------------------
DEBUG    arctic.tickstore.tickstore:tickstore.py:612 1 buckets in 0.001325: approx 75471698 ticks/sec
DEBUG    arctic.tickstore.tickstore:tickstore.py:612 1 buckets in 0.001016: approx 98425196 ticks/sec
INFO     arctic.tickstore.tickstore:tickstore.py:355 Got data in 0.003871 secs, creating DataFrame...
INFO     arctic.tickstore.tickstore:tickstore.py:364 31 rows in 0.004661 secs: 6650 ticks/sec
INFO     arctic.tickstore.tickstore:tickstore.py:355 Got data in 0.003258 secs, creating DataFrame...
INFO     arctic.tickstore.tickstore:tickstore.py:364 26 rows in 0.003979 secs: 6534 ticks/sec
------------------------------------------------- Captured log teardown --------------------------------------------------
DEBUG    pytest_server_fixtures.serverclass.thread:thread.py:54 Killing process tree for 4314 (total_procs_to_kill=1)
DEBUG    pytest_server_fixtures.serverclass.thread:thread.py:35 Killing 1 processes with signal Signals.SIGKILL
DEBUG    pytest_server_fixtures.serverclass.thread:thread.py:39 Waiting for 1 processes to die
DEBUG    pytest_server_fixtures.serverclass.thread:thread.py:43 All processes are terminated
DEBUG    pytest_shutil.workspace:workspace.py:140 
DEBUG    pytest_shutil.workspace:workspace.py:141 =======================================================
DEBUG    pytest_shutil.workspace:workspace.py:142 pytest_shutil deleting workspace /tmp/tmp4e22l3s4
DEBUG    pytest_shutil.workspace:workspace.py:143 =======================================================
DEBUG    pytest_shutil.workspace:workspace.py:144
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
------------------------------------------------- Captured stdout setup --------------------------------------------------
{"t":{"$date":"2020-12-25T22:53:15.014-07:00"},"s":"I",  "c":"CONTROL",  "id":23285,   "ctx":"main","msg":"Automatically disabling TLS 1.0, to force-enable TLS 1.0 specify --sslDisabledProtocols 'none'"}
{"t":{"$date":"2020-12-25T22:53:15.018-07:00"},"s":"W",  "c":"ASIO",     "id":22601,   "ctx":"main","msg":"No TransportLayer configured during NetworkInterface startup"}
{"t":{"$date":"2020-12-25T22:53:15.018-07:00"},"s":"I",  "c":"NETWORK",  "id":4648601, "ctx":"main","msg":"Implicit TCP FastOpen unavailable. If TCP FastOpen is required, set tcpFastOpenServer, tcpFastOpenClient, and tcpFastOpenQueueSize."}
{"t":{"$date":"2020-12-25T22:53:15.018-07:00"},"s":"I",  "c":"STORAGE",  "id":4615611, "ctx":"initandlisten","msg":"MongoDB starting","attr":{"pid":4371,"port":26994,"dbPath":"/tmp/tmpvhfie1tc","architecture":"64-bit","host":"flxsa02"}}
{"t":{"$date":"2020-12-25T22:53:15.018-07:00"},"s":"I",  "c":"CONTROL",  "id":23403,   "ctx":"initandlisten","msg":"Build Info","attr":{"buildInfo":{"version":"4.4.2","gitVersion":"15e73dc5738d2278b688f8929aee605fe4279b0e","openSSLVersion":"OpenSSL 1.0.2g  1 Mar 2016","modules":[],"allocator":"tcmalloc","environment":{"distmod":"ubuntu1604","distarch":"x86_64","target_arch":"x86_64"}}}}
{"t":{"$date":"2020-12-25T22:53:15.018-07:00"},"s":"I",  "c":"CONTROL",  "id":51765,   "ctx":"initandlisten","msg":"Operating System","attr":{"os":{"name":"Ubuntu","version":"16.04"}}}
{"t":{"$date":"2020-12-25T22:53:15.018-07:00"},"s":"I",  "c":"CONTROL",  "id":21951,   "ctx":"initandlisten","msg":"Options set by command line","attr":{"options":{"net":{"bindIp":"127.150.242.244","port":26994,"unixDomainSocket":{"enabled":false}},"storage":{"dbPath":"/tmp/tmpvhfie1tc","journal":{"enabled":false},"syncPeriodSecs":0.0},"systemLog":{"quiet":true}}}}
{"t":{"$date":"2020-12-25T22:53:15.019-07:00"},"s":"I",  "c":"STORAGE",  "id":22297,   "ctx":"initandlisten","msg":"Using the XFS filesystem is strongly recommended with the WiredTiger storage engine. See http://dochub.mongodb.org/core/prodnotes-filesystem","tags":["startupWarnings"]}
{"t":{"$date":"2020-12-25T22:53:15.019-07:00"},"s":"I",  "c":"STORAGE",  "id":22315,   "ctx":"initandlisten","msg":"Opening WiredTiger","attr":{"config":"create,cache_size=11497M,session_max=33000,eviction=(threads_min=4,threads_max=4),config_base=false,statistics=(fast),log=(enabled=true,archive=true,path=journal,compressor=snappy),file_manager=(close_idle_time=100000,close_scan_interval=10,close_handle_minimum=250),statistics_log=(wait=0),verbose=[recovery_progress,checkpoint_progress,compact_progress],,log=(enabled=false),"}}
{"t":{"$date":"2020-12-25T22:53:15.554-07:00"},"s":"I",  "c":"STORAGE",  "id":22430,   "ctx":"initandlisten","msg":"WiredTiger message","attr":{"message":"[1608961995:554861][4371:0x7f224ec0da80], txn-recover: [WT_VERB_RECOVERY | WT_VERB_RECOVERY_PROGRESS] Set global recovery timestamp: (0, 0)"}}
{"t":{"$date":"2020-12-25T22:53:15.554-07:00"},"s":"I",  "c":"STORAGE",  "id":22430,   "ctx":"initandlisten","msg":"WiredTiger message","attr":{"message":"[1608961995:554920][4371:0x7f224ec0da80], txn-recover: [WT_VERB_RECOVERY | WT_VERB_RECOVERY_PROGRESS] Set global oldest timestamp: (0, 0)"}}
{"t":{"$date":"2020-12-25T22:53:15.597-07:00"},"s":"I",  "c":"STORAGE",  "id":4795906, "ctx":"initandlisten","msg":"WiredTiger opened","attr":{"durationMillis":578}}
{"t":{"$date":"2020-12-25T22:53:15.597-07:00"},"s":"I",  "c":"RECOVERY", "id":23987,   "ctx":"initandlisten","msg":"WiredTiger recoveryTimestamp","attr":{"recoveryTimestamp":{"$timestamp":{"t":0,"i":0}}}}
{"t":{"$date":"2020-12-25T22:53:15.660-07:00"},"s":"I",  "c":"STORAGE",  "id":4366408, "ctx":"initandlisten","msg":"No table logging settings modifications are required for existing WiredTiger tables","attr":{"loggingEnabled":true}}
{"t":{"$date":"2020-12-25T22:53:15.660-07:00"},"s":"I",  "c":"STORAGE",  "id":22262,   "ctx":"initandlisten","msg":"Timestamp monitor starting"}
{"t":{"$date":"2020-12-25T22:53:15.678-07:00"},"s":"W",  "c":"CONTROL",  "id":22120,   "ctx":"initandlisten","msg":"Access control is not enabled for the database. Read and write access to data and configuration is unrestricted","tags":["startupWarnings"]}
{"t":{"$date":"2020-12-25T22:53:15.678-07:00"},"s":"W",  "c":"CONTROL",  "id":22184,   "ctx":"initandlisten","msg":"Soft rlimits too low","attr":{"currentValue":1024,"recommendedMinimum":64000},"tags":["startupWarnings"]}
{"t":{"$date":"2020-12-25T22:53:15.678-07:00"},"s":"I",  "c":"STORAGE",  "id":20320,   "ctx":"initandlisten","msg":"createCollection","attr":{"namespace":"admin.system.version","uuidDisposition":"provided","uuid":{"uuid":{"$uuid":"350cd555-6788-4bac-bab2-93fcc8330554"}},"options":{"uuid":{"$uuid":"350cd555-6788-4bac-bab2-93fcc8330554"}}}}
{"t":{"$date":"2020-12-25T22:53:15.743-07:00"},"s":"I",  "c":"INDEX",    "id":20345,   "ctx":"initandlisten","msg":"Index build: done building","attr":{"buildUUID":null,"namespace":"admin.system.version","index":"_id_","commitTimestamp":{"$timestamp":{"t":0,"i":0}}}}
{"t":{"$date":"2020-12-25T22:53:15.744-07:00"},"s":"I",  "c":"COMMAND",  "id":20459,   "ctx":"initandlisten","msg":"Setting featureCompatibilityVersion","attr":{"newVersion":"4.4"}}
{"t":{"$date":"2020-12-25T22:53:15.744-07:00"},"s":"I",  "c":"STORAGE",  "id":20536,   "ctx":"initandlisten","msg":"Flow Control is enabled on this deployment"}
{"t":{"$date":"2020-12-25T22:53:15.744-07:00"},"s":"I",  "c":"STORAGE",  "id":20320,   "ctx":"initandlisten","msg":"createCollection","attr":{"namespace":"local.startup_log","uuidDisposition":"generated","uuid":{"uuid":{"$uuid":"56ca936d-b1ac-44f1-8267-cb3f10fb3d5f"}},"options":{"capped":true,"size":10485760}}}
{"t":{"$date":"2020-12-25T22:53:15.803-07:00"},"s":"I",  "c":"INDEX",    "id":20345,   "ctx":"initandlisten","msg":"Index build: done building","attr":{"buildUUID":null,"namespace":"local.startup_log","index":"_id_","commitTimestamp":{"$timestamp":{"t":0,"i":0}}}}
{"t":{"$date":"2020-12-25T22:53:15.803-07:00"},"s":"I",  "c":"FTDC",     "id":20625,   "ctx":"initandlisten","msg":"Initializing full-time diagnostic data capture","attr":{"dataDirectory":"/tmp/tmpvhfie1tc/diagnostic.data"}}
{"t":{"$date":"2020-12-25T22:53:15.804-07:00"},"s":"I",  "c":"CONTROL",  "id":20712,   "ctx":"LogicalSessionCacheReap","msg":"Sessions collection is not set up; waiting until next sessions reap interval","attr":{"error":"NamespaceNotFound: config.system.sessions does not exist"}}
{"t":{"$date":"2020-12-25T22:53:15.804-07:00"},"s":"I",  "c":"NETWORK",  "id":23015,   "ctx":"listener","msg":"Listening on","attr":{"address":"127.150.242.244"}}
{"t":{"$date":"2020-12-25T22:53:15.804-07:00"},"s":"I",  "c":"NETWORK",  "id":23016,   "ctx":"listener","msg":"Waiting for connections","attr":{"port":26994,"ssl":"off"}}
{"t":{"$date":"2020-12-25T22:53:15.804-07:00"},"s":"I",  "c":"STORAGE",  "id":20320,   "ctx":"LogicalSessionCacheRefresh","msg":"createCollection","attr":{"namespace":"config.system.sessions","uuidDisposition":"generated","uuid":{"uuid":{"$uuid":"093fb211-fad5-4765-aae0-a385fe823b53"}},"options":{}}}
{"t":{"$date":"2020-12-25T22:53:15.899-07:00"},"s":"I",  "c":"INDEX",    "id":20345,   "ctx":"LogicalSessionCacheRefresh","msg":"Index build: done building","attr":{"buildUUID":null,"namespace":"config.system.sessions","index":"_id_","commitTimestamp":{"$timestamp":{"t":0,"i":0}}}}
{"t":{"$date":"2020-12-25T22:53:15.899-07:00"},"s":"I",  "c":"INDEX",    "id":20345,   "ctx":"LogicalSessionCacheRefresh","msg":"Index build: done building","attr":{"buildUUID":null,"namespace":"config.system.sessions","index":"lsidTTLIndex","commitTimestamp":{"$timestamp":{"t":0,"i":0}}}}
{"t":{"$date":"2020-12-25T22:53:16.089-07:00"},"s":"I",  "c":"NETWORK",  "id":51800,   "ctx":"conn1","msg":"client metadata","attr":{"remote":"127.0.0.1:53690","client":"conn1","doc":{"driver":{"name":"PyMongo","version":"3.11.2"},"os":{"type":"Linux","name":"Linux","architecture":"x86_64","version":"4.15.0-128-generic"},"platform":"CPython 3.6.12.final.0"}}}
{"t":{"$date":"2020-12-25T22:53:16.092-07:00"},"s":"I",  "c":"NETWORK",  "id":51800,   "ctx":"conn2","msg":"client metadata","attr":{"remote":"127.0.0.1:53692","client":"conn2","doc":{"driver":{"name":"PyMongo","version":"3.11.2"},"os":{"type":"Linux","name":"Linux","architecture":"x86_64","version":"4.15.0-128-generic"},"platform":"CPython 3.6.12.final.0"}}}
{"t":{"$date":"2020-12-25T22:53:16.194-07:00"},"s":"I",  "c":"NETWORK",  "id":51800,   "ctx":"conn3","msg":"client metadata","attr":{"remote":"127.0.0.1:53694","client":"conn3","doc":{"driver":{"name":"PyMongo","version":"3.11.2"},"os":{"type":"Linux","name":"Linux","architecture":"x86_64","version":"4.15.0-128-generic"},"platform":"CPython 3.6.12.final.0"}}}
{"t":{"$date":"2020-12-25T22:53:16.197-07:00"},"s":"I",  "c":"NETWORK",  "id":51800,   "ctx":"conn4","msg":"client metadata","attr":{"remote":"127.0.0.1:53696","client":"conn4","doc":{"driver":{"name":"PyMongo","version":"3.11.2"},"os":{"type":"Linux","name":"Linux","architecture":"x86_64","version":"4.15.0-128-generic"},"platform":"CPython 3.6.12.final.0"}}}
{"t":{"$date":"2020-12-25T22:53:16.198-07:00"},"s":"I",  "c":"NETWORK",  "id":51800,   "ctx":"conn5","msg":"client metadata","attr":{"remote":"127.0.0.1:53698","client":"conn5","doc":{"driver":{"name":"PyMongo","version":"3.11.2"},"os":{"type":"Linux","name":"Linux","architecture":"x86_64","version":"4.15.0-128-generic"},"platform":"CPython 3.6.12.final.0"}}}
{"t":{"$date":"2020-12-25T22:53:16.205-07:00"},"s":"I",  "c":"NETWORK",  "id":51800,   "ctx":"conn6","msg":"client metadata","attr":{"remote":"127.0.0.1:53700","client":"conn6","doc":{"driver":{"name":"PyMongo","version":"3.11.2"},"os":{"type":"Linux","name":"Linux","architecture":"x86_64","version":"4.15.0-128-generic"},"platform":"CPython 3.6.12.final.0"}}}
{"t":{"$date":"2020-12-25T22:53:16.207-07:00"},"s":"I",  "c":"NETWORK",  "id":51800,   "ctx":"conn8","msg":"client metadata","attr":{"remote":"127.0.0.1:53704","client":"conn8","doc":{"driver":{"name":"PyMongo","version":"3.11.2"},"os":{"type":"Linux","name":"Linux","architecture":"x86_64","version":"4.15.0-128-generic"},"platform":"CPython 3.6.12.final.0"}}}
{"t":{"$date":"2020-12-25T22:53:16.207-07:00"},"s":"I",  "c":"NETWORK",  "id":51800,   "ctx":"conn7","msg":"client metadata","attr":{"remote":"127.0.0.1:53702","client":"conn7","doc":{"driver":{"name":"PyMongo","version":"3.11.2"},"os":{"type":"Linux","name":"Linux","architecture":"x86_64","version":"4.15.0-128-generic"},"platform":"CPython 3.6.12.final.0"}}}
{"t":{"$date":"2020-12-25T22:53:16.211-07:00"},"s":"I",  "c":"STORAGE",  "id":20320,   "ctx":"conn8","msg":"createCollection","attr":{"namespace":"meta_db.cache","uuidDisposition":"generated","uuid":{"uuid":{"$uuid":"1f490514-b215-4961-92ee-541adef3e7b0"}},"options":{}}}
{"t":{"$date":"2020-12-25T22:53:16.280-07:00"},"s":"I",  "c":"INDEX",    "id":20345,   "ctx":"conn8","msg":"Index build: done building","attr":{"buildUUID":null,"namespace":"meta_db.cache","index":"_id_","commitTimestamp":{"$timestamp":{"t":0,"i":0}}}}
{"t":{"$date":"2020-12-25T22:53:16.280-07:00"},"s":"I",  "c":"INDEX",    "id":20438,   "ctx":"conn8","msg":"Index build: registering","attr":{"buildUUID":{"uuid":{"$uuid":"83ba21cd-75eb-4ddb-b1a8-8b91b9b218aa"}},"namespace":"meta_db.cache","collectionUUID":{"uuid":{"$uuid":"1f490514-b215-4961-92ee-541adef3e7b0"}},"indexes":1,"firstIndex":{"name":"date_1"}}}
{"t":{"$date":"2020-12-25T22:53:16.319-07:00"},"s":"I",  "c":"INDEX",    "id":20345,   "ctx":"conn8","msg":"Index build: done building","attr":{"buildUUID":null,"namespace":"meta_db.cache","index":"date_1","commitTimestamp":{"$timestamp":{"t":0,"i":0}}}}
{"t":{"$date":"2020-12-25T22:53:16.320-07:00"},"s":"I",  "c":"INDEX",    "id":20440,   "ctx":"conn8","msg":"Index build: waiting for index build to complete","attr":{"buildUUID":{"uuid":{"$uuid":"83ba21cd-75eb-4ddb-b1a8-8b91b9b218aa"}},"deadline":{"$date":{"$numberLong":"9223372036854775807"}}}}
{"t":{"$date":"2020-12-25T22:53:16.320-07:00"},"s":"I",  "c":"INDEX",    "id":20447,   "ctx":"conn8","msg":"Index build: completed","attr":{"buildUUID":{"uuid":{"$uuid":"83ba21cd-75eb-4ddb-b1a8-8b91b9b218aa"}}}}
--------------------------------------------------- Captured log setup ---------------------------------------------------
DEBUG    pytest_shutil.workspace:workspace.py:52 
DEBUG    pytest_shutil.workspace:workspace.py:53 =======================================================
DEBUG    pytest_shutil.workspace:workspace.py:56 pytest_shutil created workspace /tmp/tmpvhfie1tc
DEBUG    pytest_shutil.workspace:workspace.py:64 This workspace will delete itself on teardown
DEBUG    pytest_shutil.workspace:workspace.py:65 =======================================================
DEBUG    pytest_shutil.workspace:workspace.py:66 
DEBUG    pytest_server_fixtures.serverclass.thread:thread.py:77 Launching thread server.
DEBUG    pytest_server_fixtures.serverclass.thread:thread.py:89 Running server: mongod --bind_ip=127.150.242.244 --port=26994 --nounixsocket --syncdelay=0 --nojournal --quiet --dbpath=/tmp/tmpvhfie1tc
DEBUG    pytest_server_fixtures.serverclass.thread:thread.py:90 CWD: /home/cwm/git/bb.FLXSA/quant/arctic_venv36
DEBUG    pytest_server_fixtures.base2:base2.py:226 sleeping for 0.1 before retrying (1 of 28)
INFO     pytest_server_fixtures.mongo:mongo.py:128 Connecting to Mongo at 127.150.242.244:26994
DEBUG    pytest_server_fixtures.base2:base2.py:226 sleeping for 0.1 before retrying (2 of 28)
INFO     pytest_server_fixtures.mongo:mongo.py:128 Connecting to Mongo at 127.150.242.244:26994
DEBUG    pytest_server_fixtures.base2:base2.py:226 sleeping for 0.1 before retrying (3 of 28)
INFO     pytest_server_fixtures.mongo:mongo.py:128 Connecting to Mongo at 127.150.242.244:26994
DEBUG    pytest_server_fixtures.base2:base2.py:229 waited 0:00:01.223901 for server to start successfully
DEBUG    pytest_server_fixtures.base2:base2.py:69 Server now awake
INFO     arctic.fixtures.arctic:arctic.py:23 arctic.fixtures: arctic init(mongo_server.api=MongoClient(host=['127.150.242.244:26994'], document_class=dict, tz_aware=False, connect=True))
-------------------------------------------------- Captured stdout call --------------------------------------------------
{"t":{"$date":"2020-12-25T22:53:16.322-07:00"},"s":"I",  "c":"STORAGE",  "id":20320,   "ctx":"conn8","msg":"createCollection","attr":{"namespace":"arctic_FEED_2010.LEVEL1.ARCTIC","uuidDisposition":"generated","uuid":{"uuid":{"$uuid":"24e01899-1781-4e75-959f-38b8c2de124b"}},"options":{}}}
{"t":{"$date":"2020-12-25T22:53:16.391-07:00"},"s":"I",  "c":"INDEX",    "id":20345,   "ctx":"conn8","msg":"Index build: done building","attr":{"buildUUID":null,"namespace":"arctic_FEED_2010.LEVEL1.ARCTIC","index":"_id_","commitTimestamp":{"$timestamp":{"t":0,"i":0}}}}
{"t":{"$date":"2020-12-25T22:53:16.392-07:00"},"s":"I",  "c":"STORAGE",  "id":20320,   "ctx":"conn8","msg":"createCollection","attr":{"namespace":"arctic_FEED_2010.LEVEL1","uuidDisposition":"generated","uuid":{"uuid":{"$uuid":"331b2e87-e693-4d22-ac5e-904f996138f4"}},"options":{}}}
{"t":{"$date":"2020-12-25T22:53:16.501-07:00"},"s":"I",  "c":"INDEX",    "id":20345,   "ctx":"conn8","msg":"Index build: done building","attr":{"buildUUID":null,"namespace":"arctic_FEED_2010.LEVEL1","index":"_id_","commitTimestamp":{"$timestamp":{"t":0,"i":0}}}}
{"t":{"$date":"2020-12-25T22:53:16.501-07:00"},"s":"I",  "c":"INDEX",    "id":20345,   "ctx":"conn8","msg":"Index build: done building","attr":{"buildUUID":null,"namespace":"arctic_FEED_2010.LEVEL1","index":"sy_1_s_1","commitTimestamp":{"$timestamp":{"t":0,"i":0}}}}
{"t":{"$date":"2020-12-25T22:53:16.502-07:00"},"s":"I",  "c":"COMMAND",  "id":51803,   "ctx":"conn8","msg":"Slow query","attr":{"type":"command","ns":"arctic_FEED_2010.LEVEL1","command":{"createIndexes":"LEVEL1","indexes":[{"background":true,"name":"sy_1_s_1","key":{"sy":1,"s":1}}],"lsid":{"id":{"$uuid":"42833d53-b7a0-49bc-8e64-045cf923aaaf"}},"$db":"arctic_FEED_2010","$readPreference":{"mode":"primary"}},"numYields":0,"reslen":114,"locks":{"ParallelBatchWriterMode":{"acquireCount":{"r":5}},"ReplicationStateTransition":{"acquireCount":{"w":5}},"Global":{"acquireCount":{"r":2,"w":3}},"Database":{"acquireCount":{"r":2,"w":3}},"Collection":{"acquireCount":{"r":4,"w":2}},"Mutex":{"acquireCount":{"r":5}}},"flowControl":{"acquireCount":1},"storage":{},"protocol":"op_msg","durationMillis":109}}
{"t":{"$date":"2020-12-25T22:53:16.502-07:00"},"s":"I",  "c":"INDEX",    "id":20438,   "ctx":"conn8","msg":"Index build: registering","attr":{"buildUUID":{"uuid":{"$uuid":"b04e19a1-680a-4015-ae2c-1ec90123b385"}},"namespace":"arctic_FEED_2010.LEVEL1","collectionUUID":{"uuid":{"$uuid":"331b2e87-e693-4d22-ac5e-904f996138f4"}},"indexes":1,"firstIndex":{"name":"s_1"}}}
{"t":{"$date":"2020-12-25T22:53:16.534-07:00"},"s":"I",  "c":"INDEX",    "id":20345,   "ctx":"conn8","msg":"Index build: done building","attr":{"buildUUID":null,"namespace":"arctic_FEED_2010.LEVEL1","index":"s_1","commitTimestamp":{"$timestamp":{"t":0,"i":0}}}}
{"t":{"$date":"2020-12-25T22:53:16.534-07:00"},"s":"I",  "c":"INDEX",    "id":20440,   "ctx":"conn8","msg":"Index build: waiting for index build to complete","attr":{"buildUUID":{"uuid":{"$uuid":"b04e19a1-680a-4015-ae2c-1ec90123b385"}},"deadline":{"$date":{"$numberLong":"9223372036854775807"}}}}
{"t":{"$date":"2020-12-25T22:53:16.534-07:00"},"s":"I",  "c":"INDEX",    "id":20447,   "ctx":"conn8","msg":"Index build: completed","attr":{"buildUUID":{"uuid":{"$uuid":"b04e19a1-680a-4015-ae2c-1ec90123b385"}}}}
{"t":{"$date":"2020-12-25T22:53:16.535-07:00"},"s":"I",  "c":"STORAGE",  "id":20320,   "ctx":"conn8","msg":"createCollection","attr":{"namespace":"arctic_FEED_2010.LEVEL1.metadata","uuidDisposition":"generated","uuid":{"uuid":{"$uuid":"060ff2c5-c7f3-422e-9dba-e0e57d261bcb"}},"options":{}}}
{"t":{"$date":"2020-12-25T22:53:16.591-07:00"},"s":"I",  "c":"-",        "id":20883,   "ctx":"conn1","msg":"Interrupted operation as its client disconnected","attr":{"opId":15}}
{"t":{"$date":"2020-12-25T22:53:16.627-07:00"},"s":"I",  "c":"INDEX",    "id":20345,   "ctx":"conn8","msg":"Index build: done building","attr":{"buildUUID":null,"namespace":"arctic_FEED_2010.LEVEL1.metadata","index":"_id_","commitTimestamp":{"$timestamp":{"t":0,"i":0}}}}
{"t":{"$date":"2020-12-25T22:53:16.627-07:00"},"s":"I",  "c":"INDEX",    "id":20345,   "ctx":"conn8","msg":"Index build: done building","attr":{"buildUUID":null,"namespace":"arctic_FEED_2010.LEVEL1.metadata","index":"sy_1","commitTimestamp":{"$timestamp":{"t":0,"i":0}}}}
{"t":{"$date":"2020-12-25T22:53:16.631-07:00"},"s":"I",  "c":"STORAGE",  "id":20320,   "ctx":"conn8","msg":"createCollection","attr":{"namespace":"arctic_FEED_2011.LEVEL1.ARCTIC","uuidDisposition":"generated","uuid":{"uuid":{"$uuid":"ff48acdf-f4ce-4b8e-93c9-a34a321d636f"}},"options":{}}}
{"t":{"$date":"2020-12-25T22:53:16.691-07:00"},"s":"I",  "c":"INDEX",    "id":20345,   "ctx":"conn8","msg":"Index build: done building","attr":{"buildUUID":null,"namespace":"arctic_FEED_2011.LEVEL1.ARCTIC","index":"_id_","commitTimestamp":{"$timestamp":{"t":0,"i":0}}}}
{"t":{"$date":"2020-12-25T22:53:16.693-07:00"},"s":"I",  "c":"STORAGE",  "id":20320,   "ctx":"conn8","msg":"createCollection","attr":{"namespace":"arctic_FEED_2011.LEVEL1","uuidDisposition":"generated","uuid":{"uuid":{"$uuid":"4dae70f6-66b6-4e65-8f4e-846a5996323a"}},"options":{}}}
{"t":{"$date":"2020-12-25T22:53:16.697-07:00"},"s":"I",  "c":"-",        "id":20883,   "ctx":"conn3","msg":"Interrupted operation as its client disconnected","attr":{"opId":18}}
{"t":{"$date":"2020-12-25T22:53:16.784-07:00"},"s":"I",  "c":"INDEX",    "id":20345,   "ctx":"conn8","msg":"Index build: done building","attr":{"buildUUID":null,"namespace":"arctic_FEED_2011.LEVEL1","index":"_id_","commitTimestamp":{"$timestamp":{"t":0,"i":0}}}}
{"t":{"$date":"2020-12-25T22:53:16.785-07:00"},"s":"I",  "c":"INDEX",    "id":20345,   "ctx":"conn8","msg":"Index build: done building","attr":{"buildUUID":null,"namespace":"arctic_FEED_2011.LEVEL1","index":"sy_1_s_1","commitTimestamp":{"$timestamp":{"t":0,"i":0}}}}
{"t":{"$date":"2020-12-25T22:53:16.785-07:00"},"s":"I",  "c":"INDEX",    "id":20438,   "ctx":"conn8","msg":"Index build: registering","attr":{"buildUUID":{"uuid":{"$uuid":"da129a28-de54-4c3d-91a2-bb06818214d4"}},"namespace":"arctic_FEED_2011.LEVEL1","collectionUUID":{"uuid":{"$uuid":"4dae70f6-66b6-4e65-8f4e-846a5996323a"}},"indexes":1,"firstIndex":{"name":"s_1"}}}
{"t":{"$date":"2020-12-25T22:53:16.820-07:00"},"s":"I",  "c":"INDEX",    "id":20345,   "ctx":"conn8","msg":"Index build: done building","attr":{"buildUUID":null,"namespace":"arctic_FEED_2011.LEVEL1","index":"s_1","commitTimestamp":{"$timestamp":{"t":0,"i":0}}}}
{"t":{"$date":"2020-12-25T22:53:16.820-07:00"},"s":"I",  "c":"INDEX",    "id":20440,   "ctx":"conn8","msg":"Index build: waiting for index build to complete","attr":{"buildUUID":{"uuid":{"$uuid":"da129a28-de54-4c3d-91a2-bb06818214d4"}},"deadline":{"$date":{"$numberLong":"9223372036854775807"}}}}
{"t":{"$date":"2020-12-25T22:53:16.820-07:00"},"s":"I",  "c":"INDEX",    "id":20447,   "ctx":"conn8","msg":"Index build: completed","attr":{"buildUUID":{"uuid":{"$uuid":"da129a28-de54-4c3d-91a2-bb06818214d4"}}}}
{"t":{"$date":"2020-12-25T22:53:16.821-07:00"},"s":"I",  "c":"STORAGE",  "id":20320,   "ctx":"conn8","msg":"createCollection","attr":{"namespace":"arctic_FEED_2011.LEVEL1.metadata","uuidDisposition":"generated","uuid":{"uuid":{"$uuid":"f51d103a-56c2-434a-ba18-eb7745d0a54f"}},"options":{}}}
{"t":{"$date":"2020-12-25T22:53:16.912-07:00"},"s":"I",  "c":"INDEX",    "id":20345,   "ctx":"conn8","msg":"Index build: done building","attr":{"buildUUID":null,"namespace":"arctic_FEED_2011.LEVEL1.metadata","index":"_id_","commitTimestamp":{"$timestamp":{"t":0,"i":0}}}}
{"t":{"$date":"2020-12-25T22:53:16.912-07:00"},"s":"I",  "c":"INDEX",    "id":20345,   "ctx":"conn8","msg":"Index build: done building","attr":{"buildUUID":null,"namespace":"arctic_FEED_2011.LEVEL1.metadata","index":"sy_1","commitTimestamp":{"$timestamp":{"t":0,"i":0}}}}
{"t":{"$date":"2020-12-25T22:53:16.915-07:00"},"s":"I",  "c":"STORAGE",  "id":20320,   "ctx":"conn8","msg":"createCollection","attr":{"namespace":"arctic_FEED.LEVEL1.ARCTIC","uuidDisposition":"generated","uuid":{"uuid":{"$uuid":"0050c151-653f-4eee-841b-e1d4e8900099"}},"options":{}}}
{"t":{"$date":"2020-12-25T22:53:16.967-07:00"},"s":"I",  "c":"INDEX",    "id":20345,   "ctx":"conn8","msg":"Index build: done building","attr":{"buildUUID":null,"namespace":"arctic_FEED.LEVEL1.ARCTIC","index":"_id_","commitTimestamp":{"$timestamp":{"t":0,"i":0}}}}
{"t":{"$date":"2020-12-25T22:53:16.971-07:00"},"s":"I",  "c":"STORAGE",  "id":20320,   "ctx":"conn8","msg":"createCollection","attr":{"namespace":"arctic_FEED.LEVEL1","uuidDisposition":"generated","uuid":{"uuid":{"$uuid":"8555e220-3c15-480e-ad55-047c7279298e"}},"options":{}}}
{"t":{"$date":"2020-12-25T22:53:17.034-07:00"},"s":"I",  "c":"INDEX",    "id":20345,   "ctx":"conn8","msg":"Index build: done building","attr":{"buildUUID":null,"namespace":"arctic_FEED.LEVEL1","index":"_id_","commitTimestamp":{"$timestamp":{"t":0,"i":0}}}}
{"t":{"$date":"2020-12-25T22:53:17.037-07:00"},"s":"I",  "c":"INDEX",    "id":20438,   "ctx":"conn8","msg":"Index build: registering","attr":{"buildUUID":{"uuid":{"$uuid":"1e2f7236-1a60-479e-b8fb-4509e484f028"}},"namespace":"arctic_FEED.LEVEL1","collectionUUID":{"uuid":{"$uuid":"8555e220-3c15-480e-ad55-047c7279298e"}},"indexes":1,"firstIndex":{"name":"start_1"}}}
{"t":{"$date":"2020-12-25T22:53:17.094-07:00"},"s":"I",  "c":"INDEX",    "id":20384,   "ctx":"IndexBuildsCoordinatorMongod-0","msg":"Index build: starting","attr":{"namespace":"arctic_FEED.LEVEL1","buildUUID":null,"properties":{"v":2,"key":{"start":1},"name":"start_1","background":true},"method":"Hybrid","maxTemporaryMemoryUsageMB":200}}
{"t":{"$date":"2020-12-25T22:53:17.094-07:00"},"s":"I",  "c":"INDEX",    "id":20440,   "ctx":"conn8","msg":"Index build: waiting for index build to complete","attr":{"buildUUID":{"uuid":{"$uuid":"1e2f7236-1a60-479e-b8fb-4509e484f028"}},"deadline":{"$date":{"$numberLong":"9223372036854775807"}}}}
{"t":{"$date":"2020-12-25T22:53:17.094-07:00"},"s":"I",  "c":"INDEX",    "id":20391,   "ctx":"IndexBuildsCoordinatorMongod-0","msg":"Index build: collection scan done","attr":{"buildUUID":null,"totalRecords":2,"durationMillis":0}}
{"t":{"$date":"2020-12-25T22:53:17.095-07:00"},"s":"I",  "c":"INDEX",    "id":20685,   "ctx":"IndexBuildsCoordinatorMongod-0","msg":"Index build: inserted keys from external sorter into index","attr":{"namespace":"arctic_FEED.LEVEL1","index":"start_1","keysInserted":2,"durationMillis":0}}
{"t":{"$date":"2020-12-25T22:53:17.103-07:00"},"s":"I",  "c":"STORAGE",  "id":3856203, "ctx":"IndexBuildsCoordinatorMongod-0","msg":"Index build: waiting for next action before completing final phase","attr":{"buildUUID":{"uuid":{"$uuid":"1e2f7236-1a60-479e-b8fb-4509e484f028"}}}}
{"t":{"$date":"2020-12-25T22:53:17.103-07:00"},"s":"I",  "c":"STORAGE",  "id":3856204, "ctx":"IndexBuildsCoordinatorMongod-0","msg":"Index build: received signal","attr":{"buildUUID":{"uuid":{"$uuid":"1e2f7236-1a60-479e-b8fb-4509e484f028"}},"action":"Single-phase commit"}}
{"t":{"$date":"2020-12-25T22:53:17.103-07:00"},"s":"I",  "c":"INDEX",    "id":20345,   "ctx":"IndexBuildsCoordinatorMongod-0","msg":"Index build: done building","attr":{"buildUUID":null,"namespace":"arctic_FEED.LEVEL1","index":"start_1","commitTimestamp":{"$timestamp":{"t":0,"i":0}}}}
{"t":{"$date":"2020-12-25T22:53:17.119-07:00"},"s":"I",  "c":"STORAGE",  "id":20663,   "ctx":"IndexBuildsCoordinatorMongod-0","msg":"Index build: completed successfully","attr":{"buildUUID":{"uuid":{"$uuid":"1e2f7236-1a60-479e-b8fb-4509e484f028"}},"namespace":"arctic_FEED.LEVEL1","uuid":{"uuid":{"$uuid":"8555e220-3c15-480e-ad55-047c7279298e"}},"indexesBuilt":1,"numIndexesBefore":1,"numIndexesAfter":2}}
{"t":{"$date":"2020-12-25T22:53:17.119-07:00"},"s":"I",  "c":"INDEX",    "id":20447,   "ctx":"conn8","msg":"Index build: completed","attr":{"buildUUID":{"uuid":{"$uuid":"1e2f7236-1a60-479e-b8fb-4509e484f028"}}}}
--------------------------------------------------- Captured log call ----------------------------------------------------
DEBUG    arctic.tickstore.tickstore:tickstore.py:612 1 buckets in 0.001593: approx 62774639 ticks/sec
DEBUG    arctic.tickstore.tickstore:tickstore.py:612 1 buckets in 0.000726: approx 137741046 ticks/sec
INFO     arctic.tickstore.tickstore:tickstore.py:355 Got data in 0.002862 secs, creating DataFrame...
INFO     arctic.tickstore.tickstore:tickstore.py:364 1 rows in 0.003646 secs: 274 ticks/sec
INFO     arctic.tickstore.tickstore:tickstore.py:355 Got data in 0.00312 secs, creating DataFrame...
INFO     arctic.tickstore.tickstore:tickstore.py:364 9 rows in 0.003809 secs: 2362 ticks/sec
------------------------------------------------- Captured log teardown --------------------------------------------------
DEBUG    pytest_server_fixtures.serverclass.thread:thread.py:54 Killing process tree for 4371 (total_procs_to_kill=1)
DEBUG    pytest_server_fixtures.serverclass.thread:thread.py:35 Killing 1 processes with signal Signals.SIGKILL
DEBUG    pytest_server_fixtures.serverclass.thread:thread.py:39 Waiting for 1 processes to die
DEBUG    pytest_server_fixtures.serverclass.thread:thread.py:43 All processes are terminated
DEBUG    pytest_shutil.workspace:workspace.py:140 
DEBUG    pytest_shutil.workspace:workspace.py:141 =======================================================
DEBUG    pytest_shutil.workspace:workspace.py:142 pytest_shutil deleting workspace /tmp/tmpvhfie1tc
DEBUG    pytest_shutil.workspace:workspace.py:143 =======================================================
DEBUG    pytest_shutil.workspace:workspace.py:144
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
------------------------------------------------- Captured stdout setup --------------------------------------------------
{"t":{"$date":"2020-12-25T22:53:40.960-07:00"},"s":"I",  "c":"CONTROL",  "id":23285,   "ctx":"main","msg":"Automatically disabling TLS 1.0, to force-enable TLS 1.0 specify --sslDisabledProtocols 'none'"}
{"t":{"$date":"2020-12-25T22:53:40.961-07:00"},"s":"W",  "c":"ASIO",     "id":22601,   "ctx":"main","msg":"No TransportLayer configured during NetworkInterface startup"}
{"t":{"$date":"2020-12-25T22:53:40.962-07:00"},"s":"I",  "c":"NETWORK",  "id":4648601, "ctx":"main","msg":"Implicit TCP FastOpen unavailable. If TCP FastOpen is required, set tcpFastOpenServer, tcpFastOpenClient, and tcpFastOpenQueueSize."}
{"t":{"$date":"2020-12-25T22:53:40.962-07:00"},"s":"I",  "c":"STORAGE",  "id":4615611, "ctx":"initandlisten","msg":"MongoDB starting","attr":{"pid":5464,"port":32681,"dbPath":"/tmp/tmp_eno13ot","architecture":"64-bit","host":"flxsa02"}}
{"t":{"$date":"2020-12-25T22:53:40.962-07:00"},"s":"I",  "c":"CONTROL",  "id":23403,   "ctx":"initandlisten","msg":"Build Info","attr":{"buildInfo":{"version":"4.4.2","gitVersion":"15e73dc5738d2278b688f8929aee605fe4279b0e","openSSLVersion":"OpenSSL 1.0.2g  1 Mar 2016","modules":[],"allocator":"tcmalloc","environment":{"distmod":"ubuntu1604","distarch":"x86_64","target_arch":"x86_64"}}}}
{"t":{"$date":"2020-12-25T22:53:40.962-07:00"},"s":"I",  "c":"CONTROL",  "id":51765,   "ctx":"initandlisten","msg":"Operating System","attr":{"os":{"name":"Ubuntu","version":"16.04"}}}
{"t":{"$date":"2020-12-25T22:53:40.962-07:00"},"s":"I",  "c":"CONTROL",  "id":21951,   "ctx":"initandlisten","msg":"Options set by command line","attr":{"options":{"net":{"bindIp":"127.150.242.244","port":32681,"unixDomainSocket":{"enabled":false}},"storage":{"dbPath":"/tmp/tmp_eno13ot","journal":{"enabled":false},"syncPeriodSecs":0.0},"systemLog":{"quiet":true}}}}
{"t":{"$date":"2020-12-25T22:53:40.962-07:00"},"s":"I",  "c":"STORAGE",  "id":22297,   "ctx":"initandlisten","msg":"Using the XFS filesystem is strongly recommended with the WiredTiger storage engine. See http://dochub.mongodb.org/core/prodnotes-filesystem","tags":["startupWarnings"]}
{"t":{"$date":"2020-12-25T22:53:40.962-07:00"},"s":"I",  "c":"STORAGE",  "id":22315,   "ctx":"initandlisten","msg":"Opening WiredTiger","attr":{"config":"create,cache_size=11497M,session_max=33000,eviction=(threads_min=4,threads_max=4),config_base=false,statistics=(fast),log=(enabled=true,archive=true,path=journal,compressor=snappy),file_manager=(close_idle_time=100000,close_scan_interval=10,close_handle_minimum=250),statistics_log=(wait=0),verbose=[recovery_progress,checkpoint_progress,compact_progress],,log=(enabled=false),"}}
{"t":{"$date":"2020-12-25T22:53:41.498-07:00"},"s":"I",  "c":"STORAGE",  "id":22430,   "ctx":"initandlisten","msg":"WiredTiger message","attr":{"message":"[1608962021:498598][5464:0x7f5997663a80], txn-recover: [WT_VERB_RECOVERY | WT_VERB_RECOVERY_PROGRESS] Set global recovery timestamp: (0, 0)"}}
{"t":{"$date":"2020-12-25T22:53:41.498-07:00"},"s":"I",  "c":"STORAGE",  "id":22430,   "ctx":"initandlisten","msg":"WiredTiger message","attr":{"message":"[1608962021:498656][5464:0x7f5997663a80], txn-recover: [WT_VERB_RECOVERY | WT_VERB_RECOVERY_PROGRESS] Set global oldest timestamp: (0, 0)"}}
{"t":{"$date":"2020-12-25T22:53:41.543-07:00"},"s":"I",  "c":"STORAGE",  "id":4795906, "ctx":"initandlisten","msg":"WiredTiger opened","attr":{"durationMillis":581}}
{"t":{"$date":"2020-12-25T22:53:41.543-07:00"},"s":"I",  "c":"RECOVERY", "id":23987,   "ctx":"initandlisten","msg":"WiredTiger recoveryTimestamp","attr":{"recoveryTimestamp":{"$timestamp":{"t":0,"i":0}}}}
{"t":{"$date":"2020-12-25T22:53:41.604-07:00"},"s":"I",  "c":"STORAGE",  "id":4366408, "ctx":"initandlisten","msg":"No table logging settings modifications are required for existing WiredTiger tables","attr":{"loggingEnabled":true}}
{"t":{"$date":"2020-12-25T22:53:41.604-07:00"},"s":"I",  "c":"STORAGE",  "id":22262,   "ctx":"initandlisten","msg":"Timestamp monitor starting"}
{"t":{"$date":"2020-12-25T22:53:41.624-07:00"},"s":"W",  "c":"CONTROL",  "id":22120,   "ctx":"initandlisten","msg":"Access control is not enabled for the database. Read and write access to data and configuration is unrestricted","tags":["startupWarnings"]}
{"t":{"$date":"2020-12-25T22:53:41.624-07:00"},"s":"W",  "c":"CONTROL",  "id":22184,   "ctx":"initandlisten","msg":"Soft rlimits too low","attr":{"currentValue":1024,"recommendedMinimum":64000},"tags":["startupWarnings"]}
{"t":{"$date":"2020-12-25T22:53:41.624-07:00"},"s":"I",  "c":"STORAGE",  "id":20320,   "ctx":"initandlisten","msg":"createCollection","attr":{"namespace":"admin.system.version","uuidDisposition":"provided","uuid":{"uuid":{"$uuid":"615987e9-3dfb-4b5f-aad4-9cfb607c528c"}},"options":{"uuid":{"$uuid":"615987e9-3dfb-4b5f-aad4-9cfb607c528c"}}}}
{"t":{"$date":"2020-12-25T22:53:41.687-07:00"},"s":"I",  "c":"INDEX",    "id":20345,   "ctx":"initandlisten","msg":"Index build: done building","attr":{"buildUUID":null,"namespace":"admin.system.version","index":"_id_","commitTimestamp":{"$timestamp":{"t":0,"i":0}}}}
{"t":{"$date":"2020-12-25T22:53:41.687-07:00"},"s":"I",  "c":"COMMAND",  "id":20459,   "ctx":"initandlisten","msg":"Setting featureCompatibilityVersion","attr":{"newVersion":"4.4"}}
{"t":{"$date":"2020-12-25T22:53:41.687-07:00"},"s":"I",  "c":"STORAGE",  "id":20536,   "ctx":"initandlisten","msg":"Flow Control is enabled on this deployment"}
{"t":{"$date":"2020-12-25T22:53:41.688-07:00"},"s":"I",  "c":"STORAGE",  "id":20320,   "ctx":"initandlisten","msg":"createCollection","attr":{"namespace":"local.startup_log","uuidDisposition":"generated","uuid":{"uuid":{"$uuid":"0664491e-1d6f-4fc6-a22c-67e740552d2f"}},"options":{"capped":true,"size":10485760}}}
{"t":{"$date":"2020-12-25T22:53:41.749-07:00"},"s":"I",  "c":"INDEX",    "id":20345,   "ctx":"initandlisten","msg":"Index build: done building","attr":{"buildUUID":null,"namespace":"local.startup_log","index":"_id_","commitTimestamp":{"$timestamp":{"t":0,"i":0}}}}
{"t":{"$date":"2020-12-25T22:53:41.749-07:00"},"s":"I",  "c":"FTDC",     "id":20625,   "ctx":"initandlisten","msg":"Initializing full-time diagnostic data capture","attr":{"dataDirectory":"/tmp/tmp_eno13ot/diagnostic.data"}}
{"t":{"$date":"2020-12-25T22:53:41.751-07:00"},"s":"I",  "c":"CONTROL",  "id":20712,   "ctx":"LogicalSessionCacheReap","msg":"Sessions collection is not set up; waiting until next sessions reap interval","attr":{"error":"NamespaceNotFound: config.system.sessions does not exist"}}
{"t":{"$date":"2020-12-25T22:53:41.751-07:00"},"s":"I",  "c":"NETWORK",  "id":23015,   "ctx":"listener","msg":"Listening on","attr":{"address":"127.150.242.244"}}
{"t":{"$date":"2020-12-25T22:53:41.751-07:00"},"s":"I",  "c":"NETWORK",  "id":23016,   "ctx":"listener","msg":"Waiting for connections","attr":{"port":32681,"ssl":"off"}}
{"t":{"$date":"2020-12-25T22:53:41.751-07:00"},"s":"I",  "c":"STORAGE",  "id":20320,   "ctx":"LogicalSessionCacheRefresh","msg":"createCollection","attr":{"namespace":"config.system.sessions","uuidDisposition":"generated","uuid":{"uuid":{"$uuid":"517bbfa9-e9c2-4d4d-b932-d801f13303fe"}},"options":{}}}
{"t":{"$date":"2020-12-25T22:53:41.846-07:00"},"s":"I",  "c":"INDEX",    "id":20345,   "ctx":"LogicalSessionCacheRefresh","msg":"Index build: done building","attr":{"buildUUID":null,"namespace":"config.system.sessions","index":"_id_","commitTimestamp":{"$timestamp":{"t":0,"i":0}}}}
{"t":{"$date":"2020-12-25T22:53:41.846-07:00"},"s":"I",  "c":"INDEX",    "id":20345,   "ctx":"LogicalSessionCacheRefresh","msg":"Index build: done building","attr":{"buildUUID":null,"namespace":"config.system.sessions","index":"lsidTTLIndex","commitTimestamp":{"$timestamp":{"t":0,"i":0}}}}
{"t":{"$date":"2020-12-25T22:53:42.032-07:00"},"s":"I",  "c":"NETWORK",  "id":51800,   "ctx":"conn1","msg":"client metadata","attr":{"remote":"127.0.0.1:33684","client":"conn1","doc":{"driver":{"name":"PyMongo","version":"3.11.2"},"os":{"type":"Linux","name":"Linux","architecture":"x86_64","version":"4.15.0-128-generic"},"platform":"CPython 3.6.12.final.0"}}}
{"t":{"$date":"2020-12-25T22:53:42.033-07:00"},"s":"I",  "c":"NETWORK",  "id":51800,   "ctx":"conn2","msg":"client metadata","attr":{"remote":"127.0.0.1:33686","client":"conn2","doc":{"driver":{"name":"PyMongo","version":"3.11.2"},"os":{"type":"Linux","name":"Linux","architecture":"x86_64","version":"4.15.0-128-generic"},"platform":"CPython 3.6.12.final.0"}}}
{"t":{"$date":"2020-12-25T22:53:42.134-07:00"},"s":"I",  "c":"NETWORK",  "id":51800,   "ctx":"conn3","msg":"client metadata","attr":{"remote":"127.0.0.1:33688","client":"conn3","doc":{"driver":{"name":"PyMongo","version":"3.11.2"},"os":{"type":"Linux","name":"Linux","architecture":"x86_64","version":"4.15.0-128-generic"},"platform":"CPython 3.6.12.final.0"}}}
{"t":{"$date":"2020-12-25T22:53:42.135-07:00"},"s":"I",  "c":"NETWORK",  "id":51800,   "ctx":"conn4","msg":"client metadata","attr":{"remote":"127.0.0.1:33690","client":"conn4","doc":{"driver":{"name":"PyMongo","version":"3.11.2"},"os":{"type":"Linux","name":"Linux","architecture":"x86_64","version":"4.15.0-128-generic"},"platform":"CPython 3.6.12.final.0"}}}
{"t":{"$date":"2020-12-25T22:53:42.135-07:00"},"s":"I",  "c":"NETWORK",  "id":51800,   "ctx":"conn5","msg":"client metadata","attr":{"remote":"127.0.0.1:33692","client":"conn5","doc":{"driver":{"name":"PyMongo","version":"3.11.2"},"os":{"type":"Linux","name":"Linux","architecture":"x86_64","version":"4.15.0-128-generic"},"platform":"CPython 3.6.12.final.0"}}}
{"t":{"$date":"2020-12-25T22:53:42.138-07:00"},"s":"I",  "c":"NETWORK",  "id":51800,   "ctx":"conn6","msg":"client metadata","attr":{"remote":"127.0.0.1:33694","client":"conn6","doc":{"driver":{"name":"PyMongo","version":"3.11.2"},"os":{"type":"Linux","name":"Linux","architecture":"x86_64","version":"4.15.0-128-generic"},"platform":"CPython 3.6.12.final.0"}}}
{"t":{"$date":"2020-12-25T22:53:42.140-07:00"},"s":"I",  "c":"NETWORK",  "id":51800,   "ctx":"conn7","msg":"client metadata","attr":{"remote":"127.0.0.1:33696","client":"conn7","doc":{"driver":{"name":"PyMongo","version":"3.11.2"},"os":{"type":"Linux","name":"Linux","architecture":"x86_64","version":"4.15.0-128-generic"},"platform":"CPython 3.6.12.final.0"}}}
{"t":{"$date":"2020-12-25T22:53:42.140-07:00"},"s":"I",  "c":"NETWORK",  "id":51800,   "ctx":"conn8","msg":"client metadata","attr":{"remote":"127.0.0.1:33698","client":"conn8","doc":{"driver":{"name":"PyMongo","version":"3.11.2"},"os":{"type":"Linux","name":"Linux","architecture":"x86_64","version":"4.15.0-128-generic"},"platform":"CPython 3.6.12.final.0"}}}
{"t":{"$date":"2020-12-25T22:53:42.144-07:00"},"s":"I",  "c":"STORAGE",  "id":20320,   "ctx":"conn8","msg":"createCollection","attr":{"namespace":"meta_db.cache","uuidDisposition":"generated","uuid":{"uuid":{"$uuid":"e16f5a09-fca4-4472-bd4a-71845bdbd617"}},"options":{}}}
{"t":{"$date":"2020-12-25T22:53:42.210-07:00"},"s":"I",  "c":"INDEX",    "id":20345,   "ctx":"conn8","msg":"Index build: done building","attr":{"buildUUID":null,"namespace":"meta_db.cache","index":"_id_","commitTimestamp":{"$timestamp":{"t":0,"i":0}}}}
{"t":{"$date":"2020-12-25T22:53:42.211-07:00"},"s":"I",  "c":"INDEX",    "id":20438,   "ctx":"conn8","msg":"Index build: registering","attr":{"buildUUID":{"uuid":{"$uuid":"151169a4-3997-401a-8c1a-6d5fe388210d"}},"namespace":"meta_db.cache","collectionUUID":{"uuid":{"$uuid":"e16f5a09-fca4-4472-bd4a-71845bdbd617"}},"indexes":1,"firstIndex":{"name":"date_1"}}}
{"t":{"$date":"2020-12-25T22:53:42.239-07:00"},"s":"I",  "c":"INDEX",    "id":20345,   "ctx":"conn8","msg":"Index build: done building","attr":{"buildUUID":null,"namespace":"meta_db.cache","index":"date_1","commitTimestamp":{"$timestamp":{"t":0,"i":0}}}}
{"t":{"$date":"2020-12-25T22:53:42.239-07:00"},"s":"I",  "c":"INDEX",    "id":20440,   "ctx":"conn8","msg":"Index build: waiting for index build to complete","attr":{"buildUUID":{"uuid":{"$uuid":"151169a4-3997-401a-8c1a-6d5fe388210d"}},"deadline":{"$date":{"$numberLong":"9223372036854775807"}}}}
{"t":{"$date":"2020-12-25T22:53:42.239-07:00"},"s":"I",  "c":"INDEX",    "id":20447,   "ctx":"conn8","msg":"Index build: completed","attr":{"buildUUID":{"uuid":{"$uuid":"151169a4-3997-401a-8c1a-6d5fe388210d"}}}}
{"t":{"$date":"2020-12-25T22:53:42.241-07:00"},"s":"I",  "c":"STORAGE",  "id":20320,   "ctx":"conn8","msg":"createCollection","attr":{"namespace":"arctic_test.tickstore.ARCTIC","uuidDisposition":"generated","uuid":{"uuid":{"$uuid":"bed89ffe-c126-4a0d-bb66-3beb3956b44b"}},"options":{}}}
{"t":{"$date":"2020-12-25T22:53:42.300-07:00"},"s":"I",  "c":"INDEX",    "id":20345,   "ctx":"conn8","msg":"Index build: done building","attr":{"buildUUID":null,"namespace":"arctic_test.tickstore.ARCTIC","index":"_id_","commitTimestamp":{"$timestamp":{"t":0,"i":0}}}}
{"t":{"$date":"2020-12-25T22:53:42.301-07:00"},"s":"I",  "c":"STORAGE",  "id":20320,   "ctx":"conn8","msg":"createCollection","attr":{"namespace":"arctic_test.tickstore","uuidDisposition":"generated","uuid":{"uuid":{"$uuid":"6b52d4b1-1b16-4ee9-8813-e0797759a8a7"}},"options":{}}}
{"t":{"$date":"2020-12-25T22:53:42.422-07:00"},"s":"I",  "c":"INDEX",    "id":20345,   "ctx":"conn8","msg":"Index build: done building","attr":{"buildUUID":null,"namespace":"arctic_test.tickstore","index":"_id_","commitTimestamp":{"$timestamp":{"t":0,"i":0}}}}
{"t":{"$date":"2020-12-25T22:53:42.422-07:00"},"s":"I",  "c":"INDEX",    "id":20345,   "ctx":"conn8","msg":"Index build: done building","attr":{"buildUUID":null,"namespace":"arctic_test.tickstore","index":"sy_1_s_1","commitTimestamp":{"$timestamp":{"t":0,"i":0}}}}
{"t":{"$date":"2020-12-25T22:53:42.422-07:00"},"s":"I",  "c":"COMMAND",  "id":51803,   "ctx":"conn8","msg":"Slow query","attr":{"type":"command","ns":"arctic_test.tickstore","command":{"createIndexes":"tickstore","indexes":[{"background":true,"name":"sy_1_s_1","key":{"sy":1,"s":1}}],"lsid":{"id":{"$uuid":"493768b9-d31b-4ee6-b1bd-ffaa6ace4e25"}},"$db":"arctic_test","$readPreference":{"mode":"primary"}},"numYields":0,"reslen":114,"locks":{"ParallelBatchWriterMode":{"acquireCount":{"r":5}},"ReplicationStateTransition":{"acquireCount":{"w":5}},"Global":{"acquireCount":{"r":2,"w":3}},"Database":{"acquireCount":{"r":2,"w":3}},"Collection":{"acquireCount":{"r":4,"w":2}},"Mutex":{"acquireCount":{"r":5}}},"flowControl":{"acquireCount":1},"storage":{},"protocol":"op_msg","durationMillis":121}}
{"t":{"$date":"2020-12-25T22:53:42.423-07:00"},"s":"I",  "c":"INDEX",    "id":20438,   "ctx":"conn8","msg":"Index build: registering","attr":{"buildUUID":{"uuid":{"$uuid":"261c9066-4585-43cd-97e2-9a3378848ced"}},"namespace":"arctic_test.tickstore","collectionUUID":{"uuid":{"$uuid":"6b52d4b1-1b16-4ee9-8813-e0797759a8a7"}},"indexes":1,"firstIndex":{"name":"s_1"}}}
{"t":{"$date":"2020-12-25T22:53:42.458-07:00"},"s":"I",  "c":"INDEX",    "id":20345,   "ctx":"conn8","msg":"Index build: done building","attr":{"buildUUID":null,"namespace":"arctic_test.tickstore","index":"s_1","commitTimestamp":{"$timestamp":{"t":0,"i":0}}}}
{"t":{"$date":"2020-12-25T22:53:42.458-07:00"},"s":"I",  "c":"INDEX",    "id":20440,   "ctx":"conn8","msg":"Index build: waiting for index build to complete","attr":{"buildUUID":{"uuid":{"$uuid":"261c9066-4585-43cd-97e2-9a3378848ced"}},"deadline":{"$date":{"$numberLong":"9223372036854775807"}}}}
{"t":{"$date":"2020-12-25T22:53:42.458-07:00"},"s":"I",  "c":"INDEX",    "id":20447,   "ctx":"conn8","msg":"Index build: completed","attr":{"buildUUID":{"uuid":{"$uuid":"261c9066-4585-43cd-97e2-9a3378848ced"}}}}
{"t":{"$date":"2020-12-25T22:53:42.459-07:00"},"s":"I",  "c":"STORAGE",  "id":20320,   "ctx":"conn8","msg":"createCollection","attr":{"namespace":"arctic_test.tickstore.metadata","uuidDisposition":"generated","uuid":{"uuid":{"$uuid":"ca1b22d0-7087-4aea-9f30-efe5e496b923"}},"options":{}}}
{"t":{"$date":"2020-12-25T22:53:42.534-07:00"},"s":"I",  "c":"-",        "id":20883,   "ctx":"conn1","msg":"Interrupted operation as its client disconnected","attr":{"opId":15}}
{"t":{"$date":"2020-12-25T22:53:42.553-07:00"},"s":"I",  "c":"INDEX",    "id":20345,   "ctx":"conn8","msg":"Index build: done building","attr":{"buildUUID":null,"namespace":"arctic_test.tickstore.metadata","index":"_id_","commitTimestamp":{"$timestamp":{"t":0,"i":0}}}}
{"t":{"$date":"2020-12-25T22:53:42.553-07:00"},"s":"I",  "c":"INDEX",    "id":20345,   "ctx":"conn8","msg":"Index build: done building","attr":{"buildUUID":null,"namespace":"arctic_test.tickstore.metadata","index":"sy_1","commitTimestamp":{"$timestamp":{"t":0,"i":0}}}}
--------------------------------------------------- Captured log setup ---------------------------------------------------
DEBUG    pytest_shutil.workspace:workspace.py:52 
DEBUG    pytest_shutil.workspace:workspace.py:53 =======================================================
DEBUG    pytest_shutil.workspace:workspace.py:56 pytest_shutil created workspace /tmp/tmp_eno13ot
DEBUG    pytest_shutil.workspace:workspace.py:64 This workspace will delete itself on teardown
DEBUG    pytest_shutil.workspace:workspace.py:65 =======================================================
DEBUG    pytest_shutil.workspace:workspace.py:66 
DEBUG    pytest_server_fixtures.serverclass.thread:thread.py:77 Launching thread server.
DEBUG    pytest_server_fixtures.serverclass.thread:thread.py:89 Running server: mongod --bind_ip=127.150.242.244 --port=32681 --nounixsocket --syncdelay=0 --nojournal --quiet --dbpath=/tmp/tmp_eno13ot
DEBUG    pytest_server_fixtures.serverclass.thread:thread.py:90 CWD: /home/cwm/git/bb.FLXSA/quant/arctic_venv36
DEBUG    pytest_server_fixtures.base2:base2.py:226 sleeping for 0.1 before retrying (1 of 28)
INFO     pytest_server_fixtures.mongo:mongo.py:128 Connecting to Mongo at 127.150.242.244:32681
DEBUG    pytest_server_fixtures.base2:base2.py:226 sleeping for 0.1 before retrying (2 of 28)
INFO     pytest_server_fixtures.mongo:mongo.py:128 Connecting to Mongo at 127.150.242.244:32681
DEBUG    pytest_server_fixtures.base2:base2.py:226 sleeping for 0.1 before retrying (3 of 28)
INFO     pytest_server_fixtures.mongo:mongo.py:128 Connecting to Mongo at 127.150.242.244:32681
DEBUG    pytest_server_fixtures.base2:base2.py:229 waited 0:00:01.213972 for server to start successfully
DEBUG    pytest_server_fixtures.base2:base2.py:69 Server now awake
INFO     arctic.fixtures.arctic:arctic.py:23 arctic.fixtures: arctic init(mongo_server.api=MongoClient(host=['127.150.242.244:32681'], document_class=dict, tz_aware=False, connect=True))
--------------------------------------------------- Captured log call ----------------------------------------------------
DEBUG    arctic.tickstore.tickstore:tickstore.py:612 1 buckets in 0.000609: approx 164203612 ticks/sec
INFO     arctic.tickstore.tickstore:tickstore.py:355 Got data in 0.003595 secs, creating DataFrame...
INFO     arctic.tickstore.tickstore:tickstore.py:364 5 rows in 0.00447 secs: 1118 ticks/sec
------------------------------------------------- Captured log teardown --------------------------------------------------
DEBUG    pytest_server_fixtures.serverclass.thread:thread.py:54 Killing process tree for 5464 (total_procs_to_kill=1)
DEBUG    pytest_server_fixtures.serverclass.thread:thread.py:35 Killing 1 processes with signal Signals.SIGKILL
DEBUG    pytest_server_fixtures.serverclass.thread:thread.py:39 Waiting for 1 processes to die
DEBUG    pytest_server_fixtures.serverclass.thread:thread.py:43 All processes are terminated
DEBUG    pytest_shutil.workspace:workspace.py:140 
DEBUG    pytest_shutil.workspace:workspace.py:141 =======================================================
DEBUG    pytest_shutil.workspace:workspace.py:142 pytest_shutil deleting workspace /tmp/tmp_eno13ot
DEBUG    pytest_shutil.workspace:workspace.py:143 =======================================================
DEBUG    pytest_shutil.workspace:workspace.py:144
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
------------------------------------------------- Captured stdout setup --------------------------------------------------
{"t":{"$date":"2020-12-25T22:53:42.651-07:00"},"s":"I",  "c":"CONTROL",  "id":23285,   "ctx":"main","msg":"Automatically disabling TLS 1.0, to force-enable TLS 1.0 specify --sslDisabledProtocols 'none'"}
{"t":{"$date":"2020-12-25T22:53:42.653-07:00"},"s":"W",  "c":"ASIO",     "id":22601,   "ctx":"main","msg":"No TransportLayer configured during NetworkInterface startup"}
{"t":{"$date":"2020-12-25T22:53:42.653-07:00"},"s":"I",  "c":"NETWORK",  "id":4648601, "ctx":"main","msg":"Implicit TCP FastOpen unavailable. If TCP FastOpen is required, set tcpFastOpenServer, tcpFastOpenClient, and tcpFastOpenQueueSize."}
{"t":{"$date":"2020-12-25T22:53:42.653-07:00"},"s":"I",  "c":"STORAGE",  "id":4615611, "ctx":"initandlisten","msg":"MongoDB starting","attr":{"pid":5517,"port":24605,"dbPath":"/tmp/tmph9v91_dy","architecture":"64-bit","host":"flxsa02"}}
{"t":{"$date":"2020-12-25T22:53:42.653-07:00"},"s":"I",  "c":"CONTROL",  "id":23403,   "ctx":"initandlisten","msg":"Build Info","attr":{"buildInfo":{"version":"4.4.2","gitVersion":"15e73dc5738d2278b688f8929aee605fe4279b0e","openSSLVersion":"OpenSSL 1.0.2g  1 Mar 2016","modules":[],"allocator":"tcmalloc","environment":{"distmod":"ubuntu1604","distarch":"x86_64","target_arch":"x86_64"}}}}
{"t":{"$date":"2020-12-25T22:53:42.653-07:00"},"s":"I",  "c":"CONTROL",  "id":51765,   "ctx":"initandlisten","msg":"Operating System","attr":{"os":{"name":"Ubuntu","version":"16.04"}}}
{"t":{"$date":"2020-12-25T22:53:42.653-07:00"},"s":"I",  "c":"CONTROL",  "id":21951,   "ctx":"initandlisten","msg":"Options set by command line","attr":{"options":{"net":{"bindIp":"127.150.242.244","port":24605,"unixDomainSocket":{"enabled":false}},"storage":{"dbPath":"/tmp/tmph9v91_dy","journal":{"enabled":false},"syncPeriodSecs":0.0},"systemLog":{"quiet":true}}}}
{"t":{"$date":"2020-12-25T22:53:42.654-07:00"},"s":"I",  "c":"STORAGE",  "id":22297,   "ctx":"initandlisten","msg":"Using the XFS filesystem is strongly recommended with the WiredTiger storage engine. See http://dochub.mongodb.org/core/prodnotes-filesystem","tags":["startupWarnings"]}
{"t":{"$date":"2020-12-25T22:53:42.654-07:00"},"s":"I",  "c":"STORAGE",  "id":22315,   "ctx":"initandlisten","msg":"Opening WiredTiger","attr":{"config":"create,cache_size=11497M,session_max=33000,eviction=(threads_min=4,threads_max=4),config_base=false,statistics=(fast),log=(enabled=true,archive=true,path=journal,compressor=snappy),file_manager=(close_idle_time=100000,close_scan_interval=10,close_handle_minimum=250),statistics_log=(wait=0),verbose=[recovery_progress,checkpoint_progress,compact_progress],,log=(enabled=false),"}}
{"t":{"$date":"2020-12-25T22:53:43.183-07:00"},"s":"I",  "c":"STORAGE",  "id":22430,   "ctx":"initandlisten","msg":"WiredTiger message","attr":{"message":"[1608962023:183374][5517:0x7f3b61ae5a80], txn-recover: [WT_VERB_RECOVERY | WT_VERB_RECOVERY_PROGRESS] Set global recovery timestamp: (0, 0)"}}
{"t":{"$date":"2020-12-25T22:53:43.183-07:00"},"s":"I",  "c":"STORAGE",  "id":22430,   "ctx":"initandlisten","msg":"WiredTiger message","attr":{"message":"[1608962023:183429][5517:0x7f3b61ae5a80], txn-recover: [WT_VERB_RECOVERY | WT_VERB_RECOVERY_PROGRESS] Set global oldest timestamp: (0, 0)"}}
{"t":{"$date":"2020-12-25T22:53:43.229-07:00"},"s":"I",  "c":"STORAGE",  "id":4795906, "ctx":"initandlisten","msg":"WiredTiger opened","attr":{"durationMillis":575}}
{"t":{"$date":"2020-12-25T22:53:43.229-07:00"},"s":"I",  "c":"RECOVERY", "id":23987,   "ctx":"initandlisten","msg":"WiredTiger recoveryTimestamp","attr":{"recoveryTimestamp":{"$timestamp":{"t":0,"i":0}}}}
{"t":{"$date":"2020-12-25T22:53:43.286-07:00"},"s":"I",  "c":"STORAGE",  "id":4366408, "ctx":"initandlisten","msg":"No table logging settings modifications are required for existing WiredTiger tables","attr":{"loggingEnabled":true}}
{"t":{"$date":"2020-12-25T22:53:43.287-07:00"},"s":"I",  "c":"STORAGE",  "id":22262,   "ctx":"initandlisten","msg":"Timestamp monitor starting"}
{"t":{"$date":"2020-12-25T22:53:43.306-07:00"},"s":"W",  "c":"CONTROL",  "id":22120,   "ctx":"initandlisten","msg":"Access control is not enabled for the database. Read and write access to data and configuration is unrestricted","tags":["startupWarnings"]}
{"t":{"$date":"2020-12-25T22:53:43.306-07:00"},"s":"W",  "c":"CONTROL",  "id":22184,   "ctx":"initandlisten","msg":"Soft rlimits too low","attr":{"currentValue":1024,"recommendedMinimum":64000},"tags":["startupWarnings"]}
{"t":{"$date":"2020-12-25T22:53:43.307-07:00"},"s":"I",  "c":"STORAGE",  "id":20320,   "ctx":"initandlisten","msg":"createCollection","attr":{"namespace":"admin.system.version","uuidDisposition":"provided","uuid":{"uuid":{"$uuid":"52a1b9ac-e7e4-4e00-9421-4ef14021db99"}},"options":{"uuid":{"$uuid":"52a1b9ac-e7e4-4e00-9421-4ef14021db99"}}}}
{"t":{"$date":"2020-12-25T22:53:43.371-07:00"},"s":"I",  "c":"INDEX",    "id":20345,   "ctx":"initandlisten","msg":"Index build: done building","attr":{"buildUUID":null,"namespace":"admin.system.version","index":"_id_","commitTimestamp":{"$timestamp":{"t":0,"i":0}}}}
{"t":{"$date":"2020-12-25T22:53:43.371-07:00"},"s":"I",  "c":"COMMAND",  "id":20459,   "ctx":"initandlisten","msg":"Setting featureCompatibilityVersion","attr":{"newVersion":"4.4"}}
{"t":{"$date":"2020-12-25T22:53:43.372-07:00"},"s":"I",  "c":"STORAGE",  "id":20536,   "ctx":"initandlisten","msg":"Flow Control is enabled on this deployment"}
{"t":{"$date":"2020-12-25T22:53:43.372-07:00"},"s":"I",  "c":"STORAGE",  "id":20320,   "ctx":"initandlisten","msg":"createCollection","attr":{"namespace":"local.startup_log","uuidDisposition":"generated","uuid":{"uuid":{"$uuid":"f92d414c-2f6e-451f-80d8-efdf2a94667f"}},"options":{"capped":true,"size":10485760}}}
{"t":{"$date":"2020-12-25T22:53:43.430-07:00"},"s":"I",  "c":"INDEX",    "id":20345,   "ctx":"initandlisten","msg":"Index build: done building","attr":{"buildUUID":null,"namespace":"local.startup_log","index":"_id_","commitTimestamp":{"$timestamp":{"t":0,"i":0}}}}
{"t":{"$date":"2020-12-25T22:53:43.430-07:00"},"s":"I",  "c":"FTDC",     "id":20625,   "ctx":"initandlisten","msg":"Initializing full-time diagnostic data capture","attr":{"dataDirectory":"/tmp/tmph9v91_dy/diagnostic.data"}}
{"t":{"$date":"2020-12-25T22:53:43.432-07:00"},"s":"I",  "c":"CONTROL",  "id":20712,   "ctx":"LogicalSessionCacheReap","msg":"Sessions collection is not set up; waiting until next sessions reap interval","attr":{"error":"NamespaceNotFound: config.system.sessions does not exist"}}
{"t":{"$date":"2020-12-25T22:53:43.432-07:00"},"s":"I",  "c":"NETWORK",  "id":23015,   "ctx":"listener","msg":"Listening on","attr":{"address":"127.150.242.244"}}
{"t":{"$date":"2020-12-25T22:53:43.432-07:00"},"s":"I",  "c":"NETWORK",  "id":23016,   "ctx":"listener","msg":"Waiting for connections","attr":{"port":24605,"ssl":"off"}}
{"t":{"$date":"2020-12-25T22:53:43.432-07:00"},"s":"I",  "c":"STORAGE",  "id":20320,   "ctx":"LogicalSessionCacheRefresh","msg":"createCollection","attr":{"namespace":"config.system.sessions","uuidDisposition":"generated","uuid":{"uuid":{"$uuid":"4e70b6f1-35d8-4868-b6ee-c769becb34e0"}},"options":{}}}
{"t":{"$date":"2020-12-25T22:53:43.525-07:00"},"s":"I",  "c":"INDEX",    "id":20345,   "ctx":"LogicalSessionCacheRefresh","msg":"Index build: done building","attr":{"buildUUID":null,"namespace":"config.system.sessions","index":"_id_","commitTimestamp":{"$timestamp":{"t":0,"i":0}}}}
{"t":{"$date":"2020-12-25T22:53:43.525-07:00"},"s":"I",  "c":"INDEX",    "id":20345,   "ctx":"LogicalSessionCacheRefresh","msg":"Index build: done building","attr":{"buildUUID":null,"namespace":"config.system.sessions","index":"lsidTTLIndex","commitTimestamp":{"$timestamp":{"t":0,"i":0}}}}
{"t":{"$date":"2020-12-25T22:53:43.729-07:00"},"s":"I",  "c":"NETWORK",  "id":51800,   "ctx":"conn1","msg":"client metadata","attr":{"remote":"127.0.0.1:40102","client":"conn1","doc":{"driver":{"name":"PyMongo","version":"3.11.2"},"os":{"type":"Linux","name":"Linux","architecture":"x86_64","version":"4.15.0-128-generic"},"platform":"CPython 3.6.12.final.0"}}}
{"t":{"$date":"2020-12-25T22:53:43.730-07:00"},"s":"I",  "c":"NETWORK",  "id":51800,   "ctx":"conn2","msg":"client metadata","attr":{"remote":"127.0.0.1:40104","client":"conn2","doc":{"driver":{"name":"PyMongo","version":"3.11.2"},"os":{"type":"Linux","name":"Linux","architecture":"x86_64","version":"4.15.0-128-generic"},"platform":"CPython 3.6.12.final.0"}}}
{"t":{"$date":"2020-12-25T22:53:43.831-07:00"},"s":"I",  "c":"NETWORK",  "id":51800,   "ctx":"conn3","msg":"client metadata","attr":{"remote":"127.0.0.1:40106","client":"conn3","doc":{"driver":{"name":"PyMongo","version":"3.11.2"},"os":{"type":"Linux","name":"Linux","architecture":"x86_64","version":"4.15.0-128-generic"},"platform":"CPython 3.6.12.final.0"}}}
{"t":{"$date":"2020-12-25T22:53:43.833-07:00"},"s":"I",  "c":"NETWORK",  "id":51800,   "ctx":"conn4","msg":"client metadata","attr":{"remote":"127.0.0.1:40108","client":"conn4","doc":{"driver":{"name":"PyMongo","version":"3.11.2"},"os":{"type":"Linux","name":"Linux","architecture":"x86_64","version":"4.15.0-128-generic"},"platform":"CPython 3.6.12.final.0"}}}
{"t":{"$date":"2020-12-25T22:53:43.833-07:00"},"s":"I",  "c":"NETWORK",  "id":51800,   "ctx":"conn5","msg":"client metadata","attr":{"remote":"127.0.0.1:40110","client":"conn5","doc":{"driver":{"name":"PyMongo","version":"3.11.2"},"os":{"type":"Linux","name":"Linux","architecture":"x86_64","version":"4.15.0-128-generic"},"platform":"CPython 3.6.12.final.0"}}}
{"t":{"$date":"2020-12-25T22:53:43.835-07:00"},"s":"I",  "c":"NETWORK",  "id":51800,   "ctx":"conn6","msg":"client metadata","attr":{"remote":"127.0.0.1:40112","client":"conn6","doc":{"driver":{"name":"PyMongo","version":"3.11.2"},"os":{"type":"Linux","name":"Linux","architecture":"x86_64","version":"4.15.0-128-generic"},"platform":"CPython 3.6.12.final.0"}}}
{"t":{"$date":"2020-12-25T22:53:43.837-07:00"},"s":"I",  "c":"NETWORK",  "id":51800,   "ctx":"conn8","msg":"client metadata","attr":{"remote":"127.0.0.1:40116","client":"conn8","doc":{"driver":{"name":"PyMongo","version":"3.11.2"},"os":{"type":"Linux","name":"Linux","architecture":"x86_64","version":"4.15.0-128-generic"},"platform":"CPython 3.6.12.final.0"}}}
{"t":{"$date":"2020-12-25T22:53:43.837-07:00"},"s":"I",  "c":"NETWORK",  "id":51800,   "ctx":"conn7","msg":"client metadata","attr":{"remote":"127.0.0.1:40114","client":"conn7","doc":{"driver":{"name":"PyMongo","version":"3.11.2"},"os":{"type":"Linux","name":"Linux","architecture":"x86_64","version":"4.15.0-128-generic"},"platform":"CPython 3.6.12.final.0"}}}
{"t":{"$date":"2020-12-25T22:53:43.840-07:00"},"s":"I",  "c":"STORAGE",  "id":20320,   "ctx":"conn8","msg":"createCollection","attr":{"namespace":"meta_db.cache","uuidDisposition":"generated","uuid":{"uuid":{"$uuid":"30e76551-902e-4720-8e94-45bf37d8caf8"}},"options":{}}}
{"t":{"$date":"2020-12-25T22:53:43.906-07:00"},"s":"I",  "c":"INDEX",    "id":20345,   "ctx":"conn8","msg":"Index build: done building","attr":{"buildUUID":null,"namespace":"meta_db.cache","index":"_id_","commitTimestamp":{"$timestamp":{"t":0,"i":0}}}}
{"t":{"$date":"2020-12-25T22:53:43.907-07:00"},"s":"I",  "c":"INDEX",    "id":20438,   "ctx":"conn8","msg":"Index build: registering","attr":{"buildUUID":{"uuid":{"$uuid":"7ae750b2-fa27-44ab-9616-62f2f9befd28"}},"namespace":"meta_db.cache","collectionUUID":{"uuid":{"$uuid":"30e76551-902e-4720-8e94-45bf37d8caf8"}},"indexes":1,"firstIndex":{"name":"date_1"}}}
{"t":{"$date":"2020-12-25T22:53:43.933-07:00"},"s":"I",  "c":"INDEX",    "id":20345,   "ctx":"conn8","msg":"Index build: done building","attr":{"buildUUID":null,"namespace":"meta_db.cache","index":"date_1","commitTimestamp":{"$timestamp":{"t":0,"i":0}}}}
{"t":{"$date":"2020-12-25T22:53:43.933-07:00"},"s":"I",  "c":"INDEX",    "id":20440,   "ctx":"conn8","msg":"Index build: waiting for index build to complete","attr":{"buildUUID":{"uuid":{"$uuid":"7ae750b2-fa27-44ab-9616-62f2f9befd28"}},"deadline":{"$date":{"$numberLong":"9223372036854775807"}}}}
{"t":{"$date":"2020-12-25T22:53:43.933-07:00"},"s":"I",  "c":"INDEX",    "id":20447,   "ctx":"conn8","msg":"Index build: completed","attr":{"buildUUID":{"uuid":{"$uuid":"7ae750b2-fa27-44ab-9616-62f2f9befd28"}}}}
{"t":{"$date":"2020-12-25T22:53:43.935-07:00"},"s":"I",  "c":"STORAGE",  "id":20320,   "ctx":"conn8","msg":"createCollection","attr":{"namespace":"arctic_test.tickstore.ARCTIC","uuidDisposition":"generated","uuid":{"uuid":{"$uuid":"b66a10fa-4c47-4211-91f2-a29f9e5078a7"}},"options":{}}}
{"t":{"$date":"2020-12-25T22:53:44.000-07:00"},"s":"I",  "c":"INDEX",    "id":20345,   "ctx":"conn8","msg":"Index build: done building","attr":{"buildUUID":null,"namespace":"arctic_test.tickstore.ARCTIC","index":"_id_","commitTimestamp":{"$timestamp":{"t":0,"i":0}}}}
{"t":{"$date":"2020-12-25T22:53:44.001-07:00"},"s":"I",  "c":"STORAGE",  "id":20320,   "ctx":"conn8","msg":"createCollection","attr":{"namespace":"arctic_test.tickstore","uuidDisposition":"generated","uuid":{"uuid":{"$uuid":"7a03f327-df7c-4e20-b5de-e2a7d86fda8e"}},"options":{}}}
{"t":{"$date":"2020-12-25T22:53:44.110-07:00"},"s":"I",  "c":"INDEX",    "id":20345,   "ctx":"conn8","msg":"Index build: done building","attr":{"buildUUID":null,"namespace":"arctic_test.tickstore","index":"_id_","commitTimestamp":{"$timestamp":{"t":0,"i":0}}}}
{"t":{"$date":"2020-12-25T22:53:44.110-07:00"},"s":"I",  "c":"INDEX",    "id":20345,   "ctx":"conn8","msg":"Index build: done building","attr":{"buildUUID":null,"namespace":"arctic_test.tickstore","index":"sy_1_s_1","commitTimestamp":{"$timestamp":{"t":0,"i":0}}}}
{"t":{"$date":"2020-12-25T22:53:44.110-07:00"},"s":"I",  "c":"COMMAND",  "id":51803,   "ctx":"conn8","msg":"Slow query","attr":{"type":"command","ns":"arctic_test.tickstore","command":{"createIndexes":"tickstore","indexes":[{"background":true,"name":"sy_1_s_1","key":{"sy":1,"s":1}}],"lsid":{"id":{"$uuid":"8ee0eed4-327c-45d1-88a6-172348b731d9"}},"$db":"arctic_test","$readPreference":{"mode":"primary"}},"numYields":0,"reslen":114,"locks":{"ParallelBatchWriterMode":{"acquireCount":{"r":5}},"ReplicationStateTransition":{"acquireCount":{"w":5}},"Global":{"acquireCount":{"r":2,"w":3}},"Database":{"acquireCount":{"r":2,"w":3}},"Collection":{"acquireCount":{"r":4,"w":2}},"Mutex":{"acquireCount":{"r":5}}},"flowControl":{"acquireCount":1},"storage":{},"protocol":"op_msg","durationMillis":108}}
{"t":{"$date":"2020-12-25T22:53:44.111-07:00"},"s":"I",  "c":"INDEX",    "id":20438,   "ctx":"conn8","msg":"Index build: registering","attr":{"buildUUID":{"uuid":{"$uuid":"48ef7369-8819-4e4d-9373-809e1dcc5412"}},"namespace":"arctic_test.tickstore","collectionUUID":{"uuid":{"$uuid":"7a03f327-df7c-4e20-b5de-e2a7d86fda8e"}},"indexes":1,"firstIndex":{"name":"s_1"}}}
{"t":{"$date":"2020-12-25T22:53:44.142-07:00"},"s":"I",  "c":"INDEX",    "id":20345,   "ctx":"conn8","msg":"Index build: done building","attr":{"buildUUID":null,"namespace":"arctic_test.tickstore","index":"s_1","commitTimestamp":{"$timestamp":{"t":0,"i":0}}}}
{"t":{"$date":"2020-12-25T22:53:44.142-07:00"},"s":"I",  "c":"INDEX",    "id":20440,   "ctx":"conn8","msg":"Index build: waiting for index build to complete","attr":{"buildUUID":{"uuid":{"$uuid":"48ef7369-8819-4e4d-9373-809e1dcc5412"}},"deadline":{"$date":{"$numberLong":"9223372036854775807"}}}}
{"t":{"$date":"2020-12-25T22:53:44.142-07:00"},"s":"I",  "c":"INDEX",    "id":20447,   "ctx":"conn8","msg":"Index build: completed","attr":{"buildUUID":{"uuid":{"$uuid":"48ef7369-8819-4e4d-9373-809e1dcc5412"}}}}
{"t":{"$date":"2020-12-25T22:53:44.143-07:00"},"s":"I",  "c":"STORAGE",  "id":20320,   "ctx":"conn8","msg":"createCollection","attr":{"namespace":"arctic_test.tickstore.metadata","uuidDisposition":"generated","uuid":{"uuid":{"$uuid":"4843185c-c294-4fc9-8fb2-617c4b17d041"}},"options":{}}}
{"t":{"$date":"2020-12-25T22:53:44.231-07:00"},"s":"I",  "c":"-",        "id":20883,   "ctx":"conn1","msg":"Interrupted operation as its client disconnected","attr":{"opId":13}}
{"t":{"$date":"2020-12-25T22:53:44.237-07:00"},"s":"I",  "c":"INDEX",    "id":20345,   "ctx":"conn8","msg":"Index build: done building","attr":{"buildUUID":null,"namespace":"arctic_test.tickstore.metadata","index":"_id_","commitTimestamp":{"$timestamp":{"t":0,"i":0}}}}
{"t":{"$date":"2020-12-25T22:53:44.237-07:00"},"s":"I",  "c":"INDEX",    "id":20345,   "ctx":"conn8","msg":"Index build: done building","attr":{"buildUUID":null,"namespace":"arctic_test.tickstore.metadata","index":"sy_1","commitTimestamp":{"$timestamp":{"t":0,"i":0}}}}
--------------------------------------------------- Captured log setup ---------------------------------------------------
DEBUG    pytest_shutil.workspace:workspace.py:52 
DEBUG    pytest_shutil.workspace:workspace.py:53 =======================================================
DEBUG    pytest_shutil.workspace:workspace.py:56 pytest_shutil created workspace /tmp/tmph9v91_dy
DEBUG    pytest_shutil.workspace:workspace.py:64 This workspace will delete itself on teardown
DEBUG    pytest_shutil.workspace:workspace.py:65 =======================================================
DEBUG    pytest_shutil.workspace:workspace.py:66 
DEBUG    pytest_server_fixtures.serverclass.thread:thread.py:77 Launching thread server.
DEBUG    pytest_server_fixtures.serverclass.thread:thread.py:89 Running server: mongod --bind_ip=127.150.242.244 --port=24605 --nounixsocket --syncdelay=0 --nojournal --quiet --dbpath=/tmp/tmph9v91_dy
DEBUG    pytest_server_fixtures.serverclass.thread:thread.py:90 CWD: /home/cwm/git/bb.FLXSA/quant/arctic_venv36
DEBUG    pytest_server_fixtures.base2:base2.py:226 sleeping for 0.1 before retrying (1 of 28)
INFO     pytest_server_fixtures.mongo:mongo.py:128 Connecting to Mongo at 127.150.242.244:24605
DEBUG    pytest_server_fixtures.base2:base2.py:226 sleeping for 0.1 before retrying (2 of 28)
INFO     pytest_server_fixtures.mongo:mongo.py:128 Connecting to Mongo at 127.150.242.244:24605
DEBUG    pytest_server_fixtures.base2:base2.py:226 sleeping for 0.1 before retrying (3 of 28)
INFO     pytest_server_fixtures.mongo:mongo.py:128 Connecting to Mongo at 127.150.242.244:24605
DEBUG    pytest_server_fixtures.base2:base2.py:229 waited 0:00:01.216308 for server to start successfully
DEBUG    pytest_server_fixtures.base2:base2.py:69 Server now awake
INFO     arctic.fixtures.arctic:arctic.py:23 arctic.fixtures: arctic init(mongo_server.api=MongoClient(host=['127.150.242.244:24605'], document_class=dict, tz_aware=False, connect=True))
--------------------------------------------------- Captured log call ----------------------------------------------------
DEBUG    arctic.tickstore.tickstore:tickstore.py:612 2 buckets in 0.000639: approx 3129 ticks/sec
INFO     arctic.tickstore.tickstore:tickstore.py:355 Got data in 0.003503 secs, creating DataFrame...
INFO     arctic.tickstore.tickstore:tickstore.py:364 1 rows in 0.004299 secs: 232 ticks/sec
------------------------------------------------- Captured log teardown --------------------------------------------------
DEBUG    pytest_server_fixtures.serverclass.thread:thread.py:54 Killing process tree for 5517 (total_procs_to_kill=1)
DEBUG    pytest_server_fixtures.serverclass.thread:thread.py:35 Killing 1 processes with signal Signals.SIGKILL
DEBUG    pytest_server_fixtures.serverclass.thread:thread.py:39 Waiting for 1 processes to die
DEBUG    pytest_server_fixtures.serverclass.thread:thread.py:43 All processes are terminated
DEBUG    pytest_shutil.workspace:workspace.py:140 
DEBUG    pytest_shutil.workspace:workspace.py:141 =======================================================
DEBUG    pytest_shutil.workspace:workspace.py:142 pytest_shutil deleting workspace /tmp/tmph9v91_dy
DEBUG    pytest_shutil.workspace:workspace.py:143 =======================================================
DEBUG    pytest_shutil.workspace:workspace.py:144
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
------------------------------------------------- Captured stdout setup --------------------------------------------------
{"t":{"$date":"2020-12-25T22:53:44.339-07:00"},"s":"I",  "c":"CONTROL",  "id":23285,   "ctx":"main","msg":"Automatically disabling TLS 1.0, to force-enable TLS 1.0 specify --sslDisabledProtocols 'none'"}
{"t":{"$date":"2020-12-25T22:53:44.340-07:00"},"s":"W",  "c":"ASIO",     "id":22601,   "ctx":"main","msg":"No TransportLayer configured during NetworkInterface startup"}
{"t":{"$date":"2020-12-25T22:53:44.340-07:00"},"s":"I",  "c":"NETWORK",  "id":4648601, "ctx":"main","msg":"Implicit TCP FastOpen unavailable. If TCP FastOpen is required, set tcpFastOpenServer, tcpFastOpenClient, and tcpFastOpenQueueSize."}
{"t":{"$date":"2020-12-25T22:53:44.341-07:00"},"s":"I",  "c":"STORAGE",  "id":4615611, "ctx":"initandlisten","msg":"MongoDB starting","attr":{"pid":5572,"port":2282,"dbPath":"/tmp/tmpsmp5dicy","architecture":"64-bit","host":"flxsa02"}}
{"t":{"$date":"2020-12-25T22:53:44.341-07:00"},"s":"I",  "c":"CONTROL",  "id":23403,   "ctx":"initandlisten","msg":"Build Info","attr":{"buildInfo":{"version":"4.4.2","gitVersion":"15e73dc5738d2278b688f8929aee605fe4279b0e","openSSLVersion":"OpenSSL 1.0.2g  1 Mar 2016","modules":[],"allocator":"tcmalloc","environment":{"distmod":"ubuntu1604","distarch":"x86_64","target_arch":"x86_64"}}}}
{"t":{"$date":"2020-12-25T22:53:44.341-07:00"},"s":"I",  "c":"CONTROL",  "id":51765,   "ctx":"initandlisten","msg":"Operating System","attr":{"os":{"name":"Ubuntu","version":"16.04"}}}
{"t":{"$date":"2020-12-25T22:53:44.341-07:00"},"s":"I",  "c":"CONTROL",  "id":21951,   "ctx":"initandlisten","msg":"Options set by command line","attr":{"options":{"net":{"bindIp":"127.150.242.244","port":2282,"unixDomainSocket":{"enabled":false}},"storage":{"dbPath":"/tmp/tmpsmp5dicy","journal":{"enabled":false},"syncPeriodSecs":0.0},"systemLog":{"quiet":true}}}}
{"t":{"$date":"2020-12-25T22:53:44.341-07:00"},"s":"I",  "c":"STORAGE",  "id":22297,   "ctx":"initandlisten","msg":"Using the XFS filesystem is strongly recommended with the WiredTiger storage engine. See http://dochub.mongodb.org/core/prodnotes-filesystem","tags":["startupWarnings"]}
{"t":{"$date":"2020-12-25T22:53:44.341-07:00"},"s":"I",  "c":"STORAGE",  "id":22315,   "ctx":"initandlisten","msg":"Opening WiredTiger","attr":{"config":"create,cache_size=11497M,session_max=33000,eviction=(threads_min=4,threads_max=4),config_base=false,statistics=(fast),log=(enabled=true,archive=true,path=journal,compressor=snappy),file_manager=(close_idle_time=100000,close_scan_interval=10,close_handle_minimum=250),statistics_log=(wait=0),verbose=[recovery_progress,checkpoint_progress,compact_progress],,log=(enabled=false),"}}
{"t":{"$date":"2020-12-25T22:53:44.876-07:00"},"s":"I",  "c":"STORAGE",  "id":22430,   "ctx":"initandlisten","msg":"WiredTiger message","attr":{"message":"[1608962024:876611][5572:0x7f2f56fb6a80], txn-recover: [WT_VERB_RECOVERY | WT_VERB_RECOVERY_PROGRESS] Set global recovery timestamp: (0, 0)"}}
{"t":{"$date":"2020-12-25T22:53:44.876-07:00"},"s":"I",  "c":"STORAGE",  "id":22430,   "ctx":"initandlisten","msg":"WiredTiger message","attr":{"message":"[1608962024:876666][5572:0x7f2f56fb6a80], txn-recover: [WT_VERB_RECOVERY | WT_VERB_RECOVERY_PROGRESS] Set global oldest timestamp: (0, 0)"}}
{"t":{"$date":"2020-12-25T22:53:44.922-07:00"},"s":"I",  "c":"STORAGE",  "id":4795906, "ctx":"initandlisten","msg":"WiredTiger opened","attr":{"durationMillis":580}}
{"t":{"$date":"2020-12-25T22:53:44.922-07:00"},"s":"I",  "c":"RECOVERY", "id":23987,   "ctx":"initandlisten","msg":"WiredTiger recoveryTimestamp","attr":{"recoveryTimestamp":{"$timestamp":{"t":0,"i":0}}}}
{"t":{"$date":"2020-12-25T22:53:44.982-07:00"},"s":"I",  "c":"STORAGE",  "id":4366408, "ctx":"initandlisten","msg":"No table logging settings modifications are required for existing WiredTiger tables","attr":{"loggingEnabled":true}}
{"t":{"$date":"2020-12-25T22:53:44.982-07:00"},"s":"I",  "c":"STORAGE",  "id":22262,   "ctx":"initandlisten","msg":"Timestamp monitor starting"}
{"t":{"$date":"2020-12-25T22:53:45.002-07:00"},"s":"W",  "c":"CONTROL",  "id":22120,   "ctx":"initandlisten","msg":"Access control is not enabled for the database. Read and write access to data and configuration is unrestricted","tags":["startupWarnings"]}
{"t":{"$date":"2020-12-25T22:53:45.002-07:00"},"s":"W",  "c":"CONTROL",  "id":22184,   "ctx":"initandlisten","msg":"Soft rlimits too low","attr":{"currentValue":1024,"recommendedMinimum":64000},"tags":["startupWarnings"]}
{"t":{"$date":"2020-12-25T22:53:45.003-07:00"},"s":"I",  "c":"STORAGE",  "id":20320,   "ctx":"initandlisten","msg":"createCollection","attr":{"namespace":"admin.system.version","uuidDisposition":"provided","uuid":{"uuid":{"$uuid":"8102259d-49ea-49ea-b57a-ad634ce5e870"}},"options":{"uuid":{"$uuid":"8102259d-49ea-49ea-b57a-ad634ce5e870"}}}}
{"t":{"$date":"2020-12-25T22:53:45.065-07:00"},"s":"I",  "c":"INDEX",    "id":20345,   "ctx":"initandlisten","msg":"Index build: done building","attr":{"buildUUID":null,"namespace":"admin.system.version","index":"_id_","commitTimestamp":{"$timestamp":{"t":0,"i":0}}}}
{"t":{"$date":"2020-12-25T22:53:45.065-07:00"},"s":"I",  "c":"COMMAND",  "id":20459,   "ctx":"initandlisten","msg":"Setting featureCompatibilityVersion","attr":{"newVersion":"4.4"}}
{"t":{"$date":"2020-12-25T22:53:45.065-07:00"},"s":"I",  "c":"STORAGE",  "id":20536,   "ctx":"initandlisten","msg":"Flow Control is enabled on this deployment"}
{"t":{"$date":"2020-12-25T22:53:45.066-07:00"},"s":"I",  "c":"STORAGE",  "id":20320,   "ctx":"initandlisten","msg":"createCollection","attr":{"namespace":"local.startup_log","uuidDisposition":"generated","uuid":{"uuid":{"$uuid":"543ddf96-cedc-4540-b619-ade15d1d65b1"}},"options":{"capped":true,"size":10485760}}}
{"t":{"$date":"2020-12-25T22:53:45.128-07:00"},"s":"I",  "c":"INDEX",    "id":20345,   "ctx":"initandlisten","msg":"Index build: done building","attr":{"buildUUID":null,"namespace":"local.startup_log","index":"_id_","commitTimestamp":{"$timestamp":{"t":0,"i":0}}}}
{"t":{"$date":"2020-12-25T22:53:45.128-07:00"},"s":"I",  "c":"FTDC",     "id":20625,   "ctx":"initandlisten","msg":"Initializing full-time diagnostic data capture","attr":{"dataDirectory":"/tmp/tmpsmp5dicy/diagnostic.data"}}
{"t":{"$date":"2020-12-25T22:53:45.129-07:00"},"s":"I",  "c":"NETWORK",  "id":23015,   "ctx":"listener","msg":"Listening on","attr":{"address":"127.150.242.244"}}
{"t":{"$date":"2020-12-25T22:53:45.129-07:00"},"s":"I",  "c":"NETWORK",  "id":23016,   "ctx":"listener","msg":"Waiting for connections","attr":{"port":2282,"ssl":"off"}}
{"t":{"$date":"2020-12-25T22:53:45.129-07:00"},"s":"I",  "c":"CONTROL",  "id":20712,   "ctx":"LogicalSessionCacheReap","msg":"Sessions collection is not set up; waiting until next sessions reap interval","attr":{"error":"NamespaceNotFound: config.system.sessions does not exist"}}
{"t":{"$date":"2020-12-25T22:53:45.129-07:00"},"s":"I",  "c":"STORAGE",  "id":20320,   "ctx":"LogicalSessionCacheRefresh","msg":"createCollection","attr":{"namespace":"config.system.sessions","uuidDisposition":"generated","uuid":{"uuid":{"$uuid":"04523c7a-3854-4b5f-9da4-701f2977c905"}},"options":{}}}
{"t":{"$date":"2020-12-25T22:53:45.223-07:00"},"s":"I",  "c":"INDEX",    "id":20345,   "ctx":"LogicalSessionCacheRefresh","msg":"Index build: done building","attr":{"buildUUID":null,"namespace":"config.system.sessions","index":"_id_","commitTimestamp":{"$timestamp":{"t":0,"i":0}}}}
{"t":{"$date":"2020-12-25T22:53:45.223-07:00"},"s":"I",  "c":"INDEX",    "id":20345,   "ctx":"LogicalSessionCacheRefresh","msg":"Index build: done building","attr":{"buildUUID":null,"namespace":"config.system.sessions","index":"lsidTTLIndex","commitTimestamp":{"$timestamp":{"t":0,"i":0}}}}
{"t":{"$date":"2020-12-25T22:53:45.412-07:00"},"s":"I",  "c":"NETWORK",  "id":51800,   "ctx":"conn1","msg":"client metadata","attr":{"remote":"127.0.0.1:50946","client":"conn1","doc":{"driver":{"name":"PyMongo","version":"3.11.2"},"os":{"type":"Linux","name":"Linux","architecture":"x86_64","version":"4.15.0-128-generic"},"platform":"CPython 3.6.12.final.0"}}}
{"t":{"$date":"2020-12-25T22:53:45.413-07:00"},"s":"I",  "c":"NETWORK",  "id":51800,   "ctx":"conn2","msg":"client metadata","attr":{"remote":"127.0.0.1:50948","client":"conn2","doc":{"driver":{"name":"PyMongo","version":"3.11.2"},"os":{"type":"Linux","name":"Linux","architecture":"x86_64","version":"4.15.0-128-generic"},"platform":"CPython 3.6.12.final.0"}}}
{"t":{"$date":"2020-12-25T22:53:45.517-07:00"},"s":"I",  "c":"NETWORK",  "id":51800,   "ctx":"conn3","msg":"client metadata","attr":{"remote":"127.0.0.1:50950","client":"conn3","doc":{"driver":{"name":"PyMongo","version":"3.11.2"},"os":{"type":"Linux","name":"Linux","architecture":"x86_64","version":"4.15.0-128-generic"},"platform":"CPython 3.6.12.final.0"}}}
{"t":{"$date":"2020-12-25T22:53:45.520-07:00"},"s":"I",  "c":"NETWORK",  "id":51800,   "ctx":"conn4","msg":"client metadata","attr":{"remote":"127.0.0.1:50952","client":"conn4","doc":{"driver":{"name":"PyMongo","version":"3.11.2"},"os":{"type":"Linux","name":"Linux","architecture":"x86_64","version":"4.15.0-128-generic"},"platform":"CPython 3.6.12.final.0"}}}
{"t":{"$date":"2020-12-25T22:53:45.520-07:00"},"s":"I",  "c":"NETWORK",  "id":51800,   "ctx":"conn5","msg":"client metadata","attr":{"remote":"127.0.0.1:50954","client":"conn5","doc":{"driver":{"name":"PyMongo","version":"3.11.2"},"os":{"type":"Linux","name":"Linux","architecture":"x86_64","version":"4.15.0-128-generic"},"platform":"CPython 3.6.12.final.0"}}}
{"t":{"$date":"2020-12-25T22:53:45.524-07:00"},"s":"I",  "c":"NETWORK",  "id":51800,   "ctx":"conn6","msg":"client metadata","attr":{"remote":"127.0.0.1:50956","client":"conn6","doc":{"driver":{"name":"PyMongo","version":"3.11.2"},"os":{"type":"Linux","name":"Linux","architecture":"x86_64","version":"4.15.0-128-generic"},"platform":"CPython 3.6.12.final.0"}}}
{"t":{"$date":"2020-12-25T22:53:45.525-07:00"},"s":"I",  "c":"NETWORK",  "id":51800,   "ctx":"conn7","msg":"client metadata","attr":{"remote":"127.0.0.1:50958","client":"conn7","doc":{"driver":{"name":"PyMongo","version":"3.11.2"},"os":{"type":"Linux","name":"Linux","architecture":"x86_64","version":"4.15.0-128-generic"},"platform":"CPython 3.6.12.final.0"}}}
{"t":{"$date":"2020-12-25T22:53:45.525-07:00"},"s":"I",  "c":"NETWORK",  "id":51800,   "ctx":"conn8","msg":"client metadata","attr":{"remote":"127.0.0.1:50960","client":"conn8","doc":{"driver":{"name":"PyMongo","version":"3.11.2"},"os":{"type":"Linux","name":"Linux","architecture":"x86_64","version":"4.15.0-128-generic"},"platform":"CPython 3.6.12.final.0"}}}
{"t":{"$date":"2020-12-25T22:53:45.528-07:00"},"s":"I",  "c":"STORAGE",  "id":20320,   "ctx":"conn7","msg":"createCollection","attr":{"namespace":"meta_db.cache","uuidDisposition":"generated","uuid":{"uuid":{"$uuid":"3b795131-acf3-4a19-ba1f-ae6db7fc28a0"}},"options":{}}}
{"t":{"$date":"2020-12-25T22:53:45.594-07:00"},"s":"I",  "c":"INDEX",    "id":20345,   "ctx":"conn7","msg":"Index build: done building","attr":{"buildUUID":null,"namespace":"meta_db.cache","index":"_id_","commitTimestamp":{"$timestamp":{"t":0,"i":0}}}}
{"t":{"$date":"2020-12-25T22:53:45.595-07:00"},"s":"I",  "c":"INDEX",    "id":20438,   "ctx":"conn7","msg":"Index build: registering","attr":{"buildUUID":{"uuid":{"$uuid":"1935aa97-ad2f-492a-9886-9d7c0bf62a4d"}},"namespace":"meta_db.cache","collectionUUID":{"uuid":{"$uuid":"3b795131-acf3-4a19-ba1f-ae6db7fc28a0"}},"indexes":1,"firstIndex":{"name":"date_1"}}}
{"t":{"$date":"2020-12-25T22:53:45.624-07:00"},"s":"I",  "c":"INDEX",    "id":20345,   "ctx":"conn7","msg":"Index build: done building","attr":{"buildUUID":null,"namespace":"meta_db.cache","index":"date_1","commitTimestamp":{"$timestamp":{"t":0,"i":0}}}}
{"t":{"$date":"2020-12-25T22:53:45.624-07:00"},"s":"I",  "c":"INDEX",    "id":20440,   "ctx":"conn7","msg":"Index build: waiting for index build to complete","attr":{"buildUUID":{"uuid":{"$uuid":"1935aa97-ad2f-492a-9886-9d7c0bf62a4d"}},"deadline":{"$date":{"$numberLong":"9223372036854775807"}}}}
{"t":{"$date":"2020-12-25T22:53:45.624-07:00"},"s":"I",  "c":"INDEX",    "id":20447,   "ctx":"conn7","msg":"Index build: completed","attr":{"buildUUID":{"uuid":{"$uuid":"1935aa97-ad2f-492a-9886-9d7c0bf62a4d"}}}}
{"t":{"$date":"2020-12-25T22:53:45.626-07:00"},"s":"I",  "c":"STORAGE",  "id":20320,   "ctx":"conn7","msg":"createCollection","attr":{"namespace":"arctic_test.tickstore.ARCTIC","uuidDisposition":"generated","uuid":{"uuid":{"$uuid":"b5d83981-007c-49d5-82e4-90723a776412"}},"options":{}}}
{"t":{"$date":"2020-12-25T22:53:45.690-07:00"},"s":"I",  "c":"INDEX",    "id":20345,   "ctx":"conn7","msg":"Index build: done building","attr":{"buildUUID":null,"namespace":"arctic_test.tickstore.ARCTIC","index":"_id_","commitTimestamp":{"$timestamp":{"t":0,"i":0}}}}
{"t":{"$date":"2020-12-25T22:53:45.691-07:00"},"s":"I",  "c":"STORAGE",  "id":20320,   "ctx":"conn7","msg":"createCollection","attr":{"namespace":"arctic_test.tickstore","uuidDisposition":"generated","uuid":{"uuid":{"$uuid":"8b71004a-729c-4034-911c-b97c67144db0"}},"options":{}}}
{"t":{"$date":"2020-12-25T22:53:45.794-07:00"},"s":"I",  "c":"INDEX",    "id":20345,   "ctx":"conn7","msg":"Index build: done building","attr":{"buildUUID":null,"namespace":"arctic_test.tickstore","index":"_id_","commitTimestamp":{"$timestamp":{"t":0,"i":0}}}}
{"t":{"$date":"2020-12-25T22:53:45.794-07:00"},"s":"I",  "c":"INDEX",    "id":20345,   "ctx":"conn7","msg":"Index build: done building","attr":{"buildUUID":null,"namespace":"arctic_test.tickstore","index":"sy_1_s_1","commitTimestamp":{"$timestamp":{"t":0,"i":0}}}}
{"t":{"$date":"2020-12-25T22:53:45.794-07:00"},"s":"I",  "c":"COMMAND",  "id":51803,   "ctx":"conn7","msg":"Slow query","attr":{"type":"command","ns":"arctic_test.tickstore","command":{"createIndexes":"tickstore","indexes":[{"background":true,"name":"sy_1_s_1","key":{"sy":1,"s":1}}],"lsid":{"id":{"$uuid":"241d9e76-d00e-45ef-b526-9c4c04cb4005"}},"$db":"arctic_test","$readPreference":{"mode":"primary"}},"numYields":0,"reslen":114,"locks":{"ParallelBatchWriterMode":{"acquireCount":{"r":5}},"ReplicationStateTransition":{"acquireCount":{"w":5}},"Global":{"acquireCount":{"r":2,"w":3}},"Database":{"acquireCount":{"r":2,"w":3}},"Collection":{"acquireCount":{"r":4,"w":2}},"Mutex":{"acquireCount":{"r":5}}},"flowControl":{"acquireCount":1,"timeAcquiringMicros":1},"storage":{},"protocol":"op_msg","durationMillis":103}}
{"t":{"$date":"2020-12-25T22:53:45.795-07:00"},"s":"I",  "c":"INDEX",    "id":20438,   "ctx":"conn7","msg":"Index build: registering","attr":{"buildUUID":{"uuid":{"$uuid":"7cae45c5-116d-4352-83f3-552cb34c8dad"}},"namespace":"arctic_test.tickstore","collectionUUID":{"uuid":{"$uuid":"8b71004a-729c-4034-911c-b97c67144db0"}},"indexes":1,"firstIndex":{"name":"s_1"}}}
{"t":{"$date":"2020-12-25T22:53:45.831-07:00"},"s":"I",  "c":"INDEX",    "id":20345,   "ctx":"conn7","msg":"Index build: done building","attr":{"buildUUID":null,"namespace":"arctic_test.tickstore","index":"s_1","commitTimestamp":{"$timestamp":{"t":0,"i":0}}}}
{"t":{"$date":"2020-12-25T22:53:45.831-07:00"},"s":"I",  "c":"INDEX",    "id":20440,   "ctx":"conn7","msg":"Index build: waiting for index build to complete","attr":{"buildUUID":{"uuid":{"$uuid":"7cae45c5-116d-4352-83f3-552cb34c8dad"}},"deadline":{"$date":{"$numberLong":"9223372036854775807"}}}}
{"t":{"$date":"2020-12-25T22:53:45.831-07:00"},"s":"I",  "c":"INDEX",    "id":20447,   "ctx":"conn7","msg":"Index build: completed","attr":{"buildUUID":{"uuid":{"$uuid":"7cae45c5-116d-4352-83f3-552cb34c8dad"}}}}
{"t":{"$date":"2020-12-25T22:53:45.831-07:00"},"s":"I",  "c":"STORAGE",  "id":20320,   "ctx":"conn7","msg":"createCollection","attr":{"namespace":"arctic_test.tickstore.metadata","uuidDisposition":"generated","uuid":{"uuid":{"$uuid":"10f17704-eb69-4704-bd3b-169b38d77d2b"}},"options":{}}}
{"t":{"$date":"2020-12-25T22:53:45.914-07:00"},"s":"I",  "c":"-",        "id":20883,   "ctx":"conn1","msg":"Interrupted operation as its client disconnected","attr":{"opId":13}}
{"t":{"$date":"2020-12-25T22:53:45.926-07:00"},"s":"I",  "c":"INDEX",    "id":20345,   "ctx":"conn7","msg":"Index build: done building","attr":{"buildUUID":null,"namespace":"arctic_test.tickstore.metadata","index":"_id_","commitTimestamp":{"$timestamp":{"t":0,"i":0}}}}
{"t":{"$date":"2020-12-25T22:53:45.926-07:00"},"s":"I",  "c":"INDEX",    "id":20345,   "ctx":"conn7","msg":"Index build: done building","attr":{"buildUUID":null,"namespace":"arctic_test.tickstore.metadata","index":"sy_1","commitTimestamp":{"$timestamp":{"t":0,"i":0}}}}
--------------------------------------------------- Captured log setup ---------------------------------------------------
DEBUG    pytest_shutil.workspace:workspace.py:52 
DEBUG    pytest_shutil.workspace:workspace.py:53 =======================================================
DEBUG    pytest_shutil.workspace:workspace.py:56 pytest_shutil created workspace /tmp/tmpsmp5dicy
DEBUG    pytest_shutil.workspace:workspace.py:64 This workspace will delete itself on teardown
DEBUG    pytest_shutil.workspace:workspace.py:65 =======================================================
DEBUG    pytest_shutil.workspace:workspace.py:66 
DEBUG    pytest_server_fixtures.serverclass.thread:thread.py:77 Launching thread server.
DEBUG    pytest_server_fixtures.serverclass.thread:thread.py:89 Running server: mongod --bind_ip=127.150.242.244 --port=2282 --nounixsocket --syncdelay=0 --nojournal --quiet --dbpath=/tmp/tmpsmp5dicy
DEBUG    pytest_server_fixtures.serverclass.thread:thread.py:90 CWD: /home/cwm/git/bb.FLXSA/quant/arctic_venv36
DEBUG    pytest_server_fixtures.base2:base2.py:226 sleeping for 0.1 before retrying (1 of 28)
INFO     pytest_server_fixtures.mongo:mongo.py:128 Connecting to Mongo at 127.150.242.244:2282
DEBUG    pytest_server_fixtures.base2:base2.py:226 sleeping for 0.1 before retrying (2 of 28)
INFO     pytest_server_fixtures.mongo:mongo.py:128 Connecting to Mongo at 127.150.242.244:2282
DEBUG    pytest_server_fixtures.base2:base2.py:226 sleeping for 0.1 before retrying (3 of 28)
INFO     pytest_server_fixtures.mongo:mongo.py:128 Connecting to Mongo at 127.150.242.244:2282
DEBUG    pytest_server_fixtures.base2:base2.py:229 waited 0:00:01.219951 for server to start successfully
DEBUG    pytest_server_fixtures.base2:base2.py:69 Server now awake
INFO     arctic.fixtures.arctic:arctic.py:23 arctic.fixtures: arctic init(mongo_server.api=MongoClient(host=['127.150.242.244:2282'], document_class=dict, tz_aware=False, connect=True))
-------------------------------------------------- Captured stdout call --------------------------------------------------
{"t":{"$date":"2020-12-25T22:53:46.020-07:00"},"s":"I",  "c":"-",        "id":20883,   "ctx":"conn3","msg":"Interrupted operation as its client disconnected","attr":{"opId":16}}
--------------------------------------------------- Captured log call ----------------------------------------------------
DEBUG    arctic.tickstore.tickstore:tickstore.py:612 2 buckets in 0.000636: approx 3144 ticks/sec
------------------------------------------------- Captured log teardown --------------------------------------------------
DEBUG    pytest_server_fixtures.serverclass.thread:thread.py:54 Killing process tree for 5572 (total_procs_to_kill=1)
DEBUG    pytest_server_fixtures.serverclass.thread:thread.py:35 Killing 1 processes with signal Signals.SIGKILL
DEBUG    pytest_server_fixtures.serverclass.thread:thread.py:39 Waiting for 1 processes to die
DEBUG    pytest_server_fixtures.serverclass.thread:thread.py:43 All processes are terminated
DEBUG    pytest_shutil.workspace:workspace.py:140 
DEBUG    pytest_shutil.workspace:workspace.py:141 =======================================================
DEBUG    pytest_shutil.workspace:workspace.py:142 pytest_shutil deleting workspace /tmp/tmpsmp5dicy
DEBUG    pytest_shutil.workspace:workspace.py:143 =======================================================
DEBUG    pytest_shutil.workspace:workspace.py:144
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
------------------------------------------------- Captured stdout setup --------------------------------------------------
{"t":{"$date":"2020-12-25T22:53:46.151-07:00"},"s":"I",  "c":"CONTROL",  "id":23285,   "ctx":"main","msg":"Automatically disabling TLS 1.0, to force-enable TLS 1.0 specify --sslDisabledProtocols 'none'"}
{"t":{"$date":"2020-12-25T22:53:46.153-07:00"},"s":"W",  "c":"ASIO",     "id":22601,   "ctx":"main","msg":"No TransportLayer configured during NetworkInterface startup"}
{"t":{"$date":"2020-12-25T22:53:46.153-07:00"},"s":"I",  "c":"NETWORK",  "id":4648601, "ctx":"main","msg":"Implicit TCP FastOpen unavailable. If TCP FastOpen is required, set tcpFastOpenServer, tcpFastOpenClient, and tcpFastOpenQueueSize."}
{"t":{"$date":"2020-12-25T22:53:46.153-07:00"},"s":"I",  "c":"STORAGE",  "id":4615611, "ctx":"initandlisten","msg":"MongoDB starting","attr":{"pid":5625,"port":13306,"dbPath":"/tmp/tmp6ks1irls","architecture":"64-bit","host":"flxsa02"}}
{"t":{"$date":"2020-12-25T22:53:46.153-07:00"},"s":"I",  "c":"CONTROL",  "id":23403,   "ctx":"initandlisten","msg":"Build Info","attr":{"buildInfo":{"version":"4.4.2","gitVersion":"15e73dc5738d2278b688f8929aee605fe4279b0e","openSSLVersion":"OpenSSL 1.0.2g  1 Mar 2016","modules":[],"allocator":"tcmalloc","environment":{"distmod":"ubuntu1604","distarch":"x86_64","target_arch":"x86_64"}}}}
{"t":{"$date":"2020-12-25T22:53:46.153-07:00"},"s":"I",  "c":"CONTROL",  "id":51765,   "ctx":"initandlisten","msg":"Operating System","attr":{"os":{"name":"Ubuntu","version":"16.04"}}}
{"t":{"$date":"2020-12-25T22:53:46.153-07:00"},"s":"I",  "c":"CONTROL",  "id":21951,   "ctx":"initandlisten","msg":"Options set by command line","attr":{"options":{"net":{"bindIp":"127.150.242.244","port":13306,"unixDomainSocket":{"enabled":false}},"storage":{"dbPath":"/tmp/tmp6ks1irls","journal":{"enabled":false},"syncPeriodSecs":0.0},"systemLog":{"quiet":true}}}}
{"t":{"$date":"2020-12-25T22:53:46.154-07:00"},"s":"I",  "c":"STORAGE",  "id":22297,   "ctx":"initandlisten","msg":"Using the XFS filesystem is strongly recommended with the WiredTiger storage engine. See http://dochub.mongodb.org/core/prodnotes-filesystem","tags":["startupWarnings"]}
{"t":{"$date":"2020-12-25T22:53:46.154-07:00"},"s":"I",  "c":"STORAGE",  "id":22315,   "ctx":"initandlisten","msg":"Opening WiredTiger","attr":{"config":"create,cache_size=11497M,session_max=33000,eviction=(threads_min=4,threads_max=4),config_base=false,statistics=(fast),log=(enabled=true,archive=true,path=journal,compressor=snappy),file_manager=(close_idle_time=100000,close_scan_interval=10,close_handle_minimum=250),statistics_log=(wait=0),verbose=[recovery_progress,checkpoint_progress,compact_progress],,log=(enabled=false),"}}
{"t":{"$date":"2020-12-25T22:53:46.699-07:00"},"s":"I",  "c":"STORAGE",  "id":22430,   "ctx":"initandlisten","msg":"WiredTiger message","attr":{"message":"[1608962026:699972][5625:0x7f89bd2b9a80], txn-recover: [WT_VERB_RECOVERY | WT_VERB_RECOVERY_PROGRESS] Set global recovery timestamp: (0, 0)"}}
{"t":{"$date":"2020-12-25T22:53:46.700-07:00"},"s":"I",  "c":"STORAGE",  "id":22430,   "ctx":"initandlisten","msg":"WiredTiger message","attr":{"message":"[1608962026:700038][5625:0x7f89bd2b9a80], txn-recover: [WT_VERB_RECOVERY | WT_VERB_RECOVERY_PROGRESS] Set global oldest timestamp: (0, 0)"}}
{"t":{"$date":"2020-12-25T22:53:46.740-07:00"},"s":"I",  "c":"STORAGE",  "id":4795906, "ctx":"initandlisten","msg":"WiredTiger opened","attr":{"durationMillis":586}}
{"t":{"$date":"2020-12-25T22:53:46.741-07:00"},"s":"I",  "c":"RECOVERY", "id":23987,   "ctx":"initandlisten","msg":"WiredTiger recoveryTimestamp","attr":{"recoveryTimestamp":{"$timestamp":{"t":0,"i":0}}}}
{"t":{"$date":"2020-12-25T22:53:46.803-07:00"},"s":"I",  "c":"STORAGE",  "id":4366408, "ctx":"initandlisten","msg":"No table logging settings modifications are required for existing WiredTiger tables","attr":{"loggingEnabled":true}}
{"t":{"$date":"2020-12-25T22:53:46.803-07:00"},"s":"I",  "c":"STORAGE",  "id":22262,   "ctx":"initandlisten","msg":"Timestamp monitor starting"}
{"t":{"$date":"2020-12-25T22:53:46.821-07:00"},"s":"W",  "c":"CONTROL",  "id":22120,   "ctx":"initandlisten","msg":"Access control is not enabled for the database. Read and write access to data and configuration is unrestricted","tags":["startupWarnings"]}
{"t":{"$date":"2020-12-25T22:53:46.821-07:00"},"s":"W",  "c":"CONTROL",  "id":22184,   "ctx":"initandlisten","msg":"Soft rlimits too low","attr":{"currentValue":1024,"recommendedMinimum":64000},"tags":["startupWarnings"]}
{"t":{"$date":"2020-12-25T22:53:46.821-07:00"},"s":"I",  "c":"STORAGE",  "id":20320,   "ctx":"initandlisten","msg":"createCollection","attr":{"namespace":"admin.system.version","uuidDisposition":"provided","uuid":{"uuid":{"$uuid":"9e887d1a-9361-4036-aae0-877374511807"}},"options":{"uuid":{"$uuid":"9e887d1a-9361-4036-aae0-877374511807"}}}}
{"t":{"$date":"2020-12-25T22:53:46.886-07:00"},"s":"I",  "c":"INDEX",    "id":20345,   "ctx":"initandlisten","msg":"Index build: done building","attr":{"buildUUID":null,"namespace":"admin.system.version","index":"_id_","commitTimestamp":{"$timestamp":{"t":0,"i":0}}}}
{"t":{"$date":"2020-12-25T22:53:46.886-07:00"},"s":"I",  "c":"COMMAND",  "id":20459,   "ctx":"initandlisten","msg":"Setting featureCompatibilityVersion","attr":{"newVersion":"4.4"}}
{"t":{"$date":"2020-12-25T22:53:46.886-07:00"},"s":"I",  "c":"STORAGE",  "id":20536,   "ctx":"initandlisten","msg":"Flow Control is enabled on this deployment"}
{"t":{"$date":"2020-12-25T22:53:46.886-07:00"},"s":"I",  "c":"STORAGE",  "id":20320,   "ctx":"initandlisten","msg":"createCollection","attr":{"namespace":"local.startup_log","uuidDisposition":"generated","uuid":{"uuid":{"$uuid":"d84b0bfe-b613-46d7-bb22-7c17910eeb21"}},"options":{"capped":true,"size":10485760}}}
{"t":{"$date":"2020-12-25T22:53:46.943-07:00"},"s":"I",  "c":"INDEX",    "id":20345,   "ctx":"initandlisten","msg":"Index build: done building","attr":{"buildUUID":null,"namespace":"local.startup_log","index":"_id_","commitTimestamp":{"$timestamp":{"t":0,"i":0}}}}
{"t":{"$date":"2020-12-25T22:53:46.943-07:00"},"s":"I",  "c":"FTDC",     "id":20625,   "ctx":"initandlisten","msg":"Initializing full-time diagnostic data capture","attr":{"dataDirectory":"/tmp/tmp6ks1irls/diagnostic.data"}}
{"t":{"$date":"2020-12-25T22:53:46.944-07:00"},"s":"I",  "c":"NETWORK",  "id":23015,   "ctx":"listener","msg":"Listening on","attr":{"address":"127.150.242.244"}}
{"t":{"$date":"2020-12-25T22:53:46.944-07:00"},"s":"I",  "c":"CONTROL",  "id":20712,   "ctx":"LogicalSessionCacheReap","msg":"Sessions collection is not set up; waiting until next sessions reap interval","attr":{"error":"NamespaceNotFound: config.system.sessions does not exist"}}
{"t":{"$date":"2020-12-25T22:53:46.944-07:00"},"s":"I",  "c":"NETWORK",  "id":23016,   "ctx":"listener","msg":"Waiting for connections","attr":{"port":13306,"ssl":"off"}}
{"t":{"$date":"2020-12-25T22:53:46.944-07:00"},"s":"I",  "c":"STORAGE",  "id":20320,   "ctx":"LogicalSessionCacheRefresh","msg":"createCollection","attr":{"namespace":"config.system.sessions","uuidDisposition":"generated","uuid":{"uuid":{"$uuid":"9042b056-a223-4b2a-8914-fde069fc9cdb"}},"options":{}}}
{"t":{"$date":"2020-12-25T22:53:47.037-07:00"},"s":"I",  "c":"INDEX",    "id":20345,   "ctx":"LogicalSessionCacheRefresh","msg":"Index build: done building","attr":{"buildUUID":null,"namespace":"config.system.sessions","index":"_id_","commitTimestamp":{"$timestamp":{"t":0,"i":0}}}}
{"t":{"$date":"2020-12-25T22:53:47.038-07:00"},"s":"I",  "c":"INDEX",    "id":20345,   "ctx":"LogicalSessionCacheRefresh","msg":"Index build: done building","attr":{"buildUUID":null,"namespace":"config.system.sessions","index":"lsidTTLIndex","commitTimestamp":{"$timestamp":{"t":0,"i":0}}}}
{"t":{"$date":"2020-12-25T22:53:47.228-07:00"},"s":"I",  "c":"NETWORK",  "id":51800,   "ctx":"conn1","msg":"client metadata","attr":{"remote":"127.0.0.1:34814","client":"conn1","doc":{"driver":{"name":"PyMongo","version":"3.11.2"},"os":{"type":"Linux","name":"Linux","architecture":"x86_64","version":"4.15.0-128-generic"},"platform":"CPython 3.6.12.final.0"}}}
{"t":{"$date":"2020-12-25T22:53:47.229-07:00"},"s":"I",  "c":"NETWORK",  "id":51800,   "ctx":"conn2","msg":"client metadata","attr":{"remote":"127.0.0.1:34816","client":"conn2","doc":{"driver":{"name":"PyMongo","version":"3.11.2"},"os":{"type":"Linux","name":"Linux","architecture":"x86_64","version":"4.15.0-128-generic"},"platform":"CPython 3.6.12.final.0"}}}
{"t":{"$date":"2020-12-25T22:53:47.332-07:00"},"s":"I",  "c":"NETWORK",  "id":51800,   "ctx":"conn3","msg":"client metadata","attr":{"remote":"127.0.0.1:34818","client":"conn3","doc":{"driver":{"name":"PyMongo","version":"3.11.2"},"os":{"type":"Linux","name":"Linux","architecture":"x86_64","version":"4.15.0-128-generic"},"platform":"CPython 3.6.12.final.0"}}}
{"t":{"$date":"2020-12-25T22:53:47.335-07:00"},"s":"I",  "c":"NETWORK",  "id":51800,   "ctx":"conn4","msg":"client metadata","attr":{"remote":"127.0.0.1:34820","client":"conn4","doc":{"driver":{"name":"PyMongo","version":"3.11.2"},"os":{"type":"Linux","name":"Linux","architecture":"x86_64","version":"4.15.0-128-generic"},"platform":"CPython 3.6.12.final.0"}}}
{"t":{"$date":"2020-12-25T22:53:47.336-07:00"},"s":"I",  "c":"NETWORK",  "id":51800,   "ctx":"conn5","msg":"client metadata","attr":{"remote":"127.0.0.1:34822","client":"conn5","doc":{"driver":{"name":"PyMongo","version":"3.11.2"},"os":{"type":"Linux","name":"Linux","architecture":"x86_64","version":"4.15.0-128-generic"},"platform":"CPython 3.6.12.final.0"}}}
{"t":{"$date":"2020-12-25T22:53:47.340-07:00"},"s":"I",  "c":"NETWORK",  "id":51800,   "ctx":"conn6","msg":"client metadata","attr":{"remote":"127.0.0.1:34824","client":"conn6","doc":{"driver":{"name":"PyMongo","version":"3.11.2"},"os":{"type":"Linux","name":"Linux","architecture":"x86_64","version":"4.15.0-128-generic"},"platform":"CPython 3.6.12.final.0"}}}
{"t":{"$date":"2020-12-25T22:53:47.342-07:00"},"s":"I",  "c":"NETWORK",  "id":51800,   "ctx":"conn7","msg":"client metadata","attr":{"remote":"127.0.0.1:34826","client":"conn7","doc":{"driver":{"name":"PyMongo","version":"3.11.2"},"os":{"type":"Linux","name":"Linux","architecture":"x86_64","version":"4.15.0-128-generic"},"platform":"CPython 3.6.12.final.0"}}}
{"t":{"$date":"2020-12-25T22:53:47.342-07:00"},"s":"I",  "c":"NETWORK",  "id":51800,   "ctx":"conn8","msg":"client metadata","attr":{"remote":"127.0.0.1:34828","client":"conn8","doc":{"driver":{"name":"PyMongo","version":"3.11.2"},"os":{"type":"Linux","name":"Linux","architecture":"x86_64","version":"4.15.0-128-generic"},"platform":"CPython 3.6.12.final.0"}}}
{"t":{"$date":"2020-12-25T22:53:47.345-07:00"},"s":"I",  "c":"STORAGE",  "id":20320,   "ctx":"conn7","msg":"createCollection","attr":{"namespace":"meta_db.cache","uuidDisposition":"generated","uuid":{"uuid":{"$uuid":"6ad8a64b-26cc-49bc-84f5-d723ce16e7e2"}},"options":{}}}
{"t":{"$date":"2020-12-25T22:53:47.415-07:00"},"s":"I",  "c":"INDEX",    "id":20345,   "ctx":"conn7","msg":"Index build: done building","attr":{"buildUUID":null,"namespace":"meta_db.cache","index":"_id_","commitTimestamp":{"$timestamp":{"t":0,"i":0}}}}
{"t":{"$date":"2020-12-25T22:53:47.416-07:00"},"s":"I",  "c":"INDEX",    "id":20438,   "ctx":"conn7","msg":"Index build: registering","attr":{"buildUUID":{"uuid":{"$uuid":"36d160a3-6217-4292-8d76-6bc10f5aa6a2"}},"namespace":"meta_db.cache","collectionUUID":{"uuid":{"$uuid":"6ad8a64b-26cc-49bc-84f5-d723ce16e7e2"}},"indexes":1,"firstIndex":{"name":"date_1"}}}
{"t":{"$date":"2020-12-25T22:53:47.441-07:00"},"s":"I",  "c":"INDEX",    "id":20345,   "ctx":"conn7","msg":"Index build: done building","attr":{"buildUUID":null,"namespace":"meta_db.cache","index":"date_1","commitTimestamp":{"$timestamp":{"t":0,"i":0}}}}
{"t":{"$date":"2020-12-25T22:53:47.441-07:00"},"s":"I",  "c":"INDEX",    "id":20440,   "ctx":"conn7","msg":"Index build: waiting for index build to complete","attr":{"buildUUID":{"uuid":{"$uuid":"36d160a3-6217-4292-8d76-6bc10f5aa6a2"}},"deadline":{"$date":{"$numberLong":"9223372036854775807"}}}}
{"t":{"$date":"2020-12-25T22:53:47.441-07:00"},"s":"I",  "c":"INDEX",    "id":20447,   "ctx":"conn7","msg":"Index build: completed","attr":{"buildUUID":{"uuid":{"$uuid":"36d160a3-6217-4292-8d76-6bc10f5aa6a2"}}}}
{"t":{"$date":"2020-12-25T22:53:47.443-07:00"},"s":"I",  "c":"STORAGE",  "id":20320,   "ctx":"conn7","msg":"createCollection","attr":{"namespace":"arctic_test.tickstore.ARCTIC","uuidDisposition":"generated","uuid":{"uuid":{"$uuid":"2dcf83a1-4cf7-45e6-b2bd-a070ac816f82"}},"options":{}}}
{"t":{"$date":"2020-12-25T22:53:47.508-07:00"},"s":"I",  "c":"INDEX",    "id":20345,   "ctx":"conn7","msg":"Index build: done building","attr":{"buildUUID":null,"namespace":"arctic_test.tickstore.ARCTIC","index":"_id_","commitTimestamp":{"$timestamp":{"t":0,"i":0}}}}
{"t":{"$date":"2020-12-25T22:53:47.509-07:00"},"s":"I",  "c":"STORAGE",  "id":20320,   "ctx":"conn7","msg":"createCollection","attr":{"namespace":"arctic_test.tickstore","uuidDisposition":"generated","uuid":{"uuid":{"$uuid":"66e46634-03db-4b64-ac7a-aba07d57db95"}},"options":{}}}
{"t":{"$date":"2020-12-25T22:53:47.625-07:00"},"s":"I",  "c":"INDEX",    "id":20345,   "ctx":"conn7","msg":"Index build: done building","attr":{"buildUUID":null,"namespace":"arctic_test.tickstore","index":"_id_","commitTimestamp":{"$timestamp":{"t":0,"i":0}}}}
{"t":{"$date":"2020-12-25T22:53:47.625-07:00"},"s":"I",  "c":"INDEX",    "id":20345,   "ctx":"conn7","msg":"Index build: done building","attr":{"buildUUID":null,"namespace":"arctic_test.tickstore","index":"sy_1_s_1","commitTimestamp":{"$timestamp":{"t":0,"i":0}}}}
{"t":{"$date":"2020-12-25T22:53:47.626-07:00"},"s":"I",  "c":"COMMAND",  "id":51803,   "ctx":"conn7","msg":"Slow query","attr":{"type":"command","ns":"arctic_test.tickstore","command":{"createIndexes":"tickstore","indexes":[{"background":true,"name":"sy_1_s_1","key":{"sy":1,"s":1}}],"lsid":{"id":{"$uuid":"d4e6c295-c4a0-402e-be75-efe387240692"}},"$db":"arctic_test","$readPreference":{"mode":"primary"}},"numYields":0,"reslen":114,"locks":{"ParallelBatchWriterMode":{"acquireCount":{"r":5}},"ReplicationStateTransition":{"acquireCount":{"w":5}},"Global":{"acquireCount":{"r":2,"w":3}},"Database":{"acquireCount":{"r":2,"w":3}},"Collection":{"acquireCount":{"r":4,"w":2}},"Mutex":{"acquireCount":{"r":5}}},"flowControl":{"acquireCount":1,"timeAcquiringMicros":1},"storage":{},"protocol":"op_msg","durationMillis":116}}
{"t":{"$date":"2020-12-25T22:53:47.626-07:00"},"s":"I",  "c":"INDEX",    "id":20438,   "ctx":"conn7","msg":"Index build: registering","attr":{"buildUUID":{"uuid":{"$uuid":"a63061fd-4bc6-46ba-9402-ac49051707ec"}},"namespace":"arctic_test.tickstore","collectionUUID":{"uuid":{"$uuid":"66e46634-03db-4b64-ac7a-aba07d57db95"}},"indexes":1,"firstIndex":{"name":"s_1"}}}
{"t":{"$date":"2020-12-25T22:53:47.659-07:00"},"s":"I",  "c":"INDEX",    "id":20345,   "ctx":"conn7","msg":"Index build: done building","attr":{"buildUUID":null,"namespace":"arctic_test.tickstore","index":"s_1","commitTimestamp":{"$timestamp":{"t":0,"i":0}}}}
{"t":{"$date":"2020-12-25T22:53:47.659-07:00"},"s":"I",  "c":"INDEX",    "id":20440,   "ctx":"conn7","msg":"Index build: waiting for index build to complete","attr":{"buildUUID":{"uuid":{"$uuid":"a63061fd-4bc6-46ba-9402-ac49051707ec"}},"deadline":{"$date":{"$numberLong":"9223372036854775807"}}}}
{"t":{"$date":"2020-12-25T22:53:47.659-07:00"},"s":"I",  "c":"INDEX",    "id":20447,   "ctx":"conn7","msg":"Index build: completed","attr":{"buildUUID":{"uuid":{"$uuid":"a63061fd-4bc6-46ba-9402-ac49051707ec"}}}}
{"t":{"$date":"2020-12-25T22:53:47.660-07:00"},"s":"I",  "c":"STORAGE",  "id":20320,   "ctx":"conn7","msg":"createCollection","attr":{"namespace":"arctic_test.tickstore.metadata","uuidDisposition":"generated","uuid":{"uuid":{"$uuid":"f4ae758a-85b4-452d-8cf6-5ed0e72f3e1d"}},"options":{}}}
{"t":{"$date":"2020-12-25T22:53:47.730-07:00"},"s":"I",  "c":"-",        "id":20883,   "ctx":"conn1","msg":"Interrupted operation as its client disconnected","attr":{"opId":15}}
{"t":{"$date":"2020-12-25T22:53:47.755-07:00"},"s":"I",  "c":"INDEX",    "id":20345,   "ctx":"conn7","msg":"Index build: done building","attr":{"buildUUID":null,"namespace":"arctic_test.tickstore.metadata","index":"_id_","commitTimestamp":{"$timestamp":{"t":0,"i":0}}}}
{"t":{"$date":"2020-12-25T22:53:47.755-07:00"},"s":"I",  "c":"INDEX",    "id":20345,   "ctx":"conn7","msg":"Index build: done building","attr":{"buildUUID":null,"namespace":"arctic_test.tickstore.metadata","index":"sy_1","commitTimestamp":{"$timestamp":{"t":0,"i":0}}}}
--------------------------------------------------- Captured log setup ---------------------------------------------------
DEBUG    pytest_shutil.workspace:workspace.py:52 
DEBUG    pytest_shutil.workspace:workspace.py:53 =======================================================
DEBUG    pytest_shutil.workspace:workspace.py:56 pytest_shutil created workspace /tmp/tmp6ks1irls
DEBUG    pytest_shutil.workspace:workspace.py:64 This workspace will delete itself on teardown
DEBUG    pytest_shutil.workspace:workspace.py:65 =======================================================
DEBUG    pytest_shutil.workspace:workspace.py:66 
DEBUG    pytest_server_fixtures.serverclass.thread:thread.py:77 Launching thread server.
DEBUG    pytest_server_fixtures.serverclass.thread:thread.py:89 Running server: mongod --bind_ip=127.150.242.244 --port=13306 --nounixsocket --syncdelay=0 --nojournal --quiet --dbpath=/tmp/tmp6ks1irls
DEBUG    pytest_server_fixtures.serverclass.thread:thread.py:90 CWD: /home/cwm/git/bb.FLXSA/quant/arctic_venv36
DEBUG    pytest_server_fixtures.base2:base2.py:226 sleeping for 0.1 before retrying (1 of 28)
INFO     pytest_server_fixtures.mongo:mongo.py:128 Connecting to Mongo at 127.150.242.244:13306
DEBUG    pytest_server_fixtures.base2:base2.py:226 sleeping for 0.1 before retrying (2 of 28)
INFO     pytest_server_fixtures.mongo:mongo.py:128 Connecting to Mongo at 127.150.242.244:13306
DEBUG    pytest_server_fixtures.base2:base2.py:226 sleeping for 0.1 before retrying (3 of 28)
INFO     pytest_server_fixtures.mongo:mongo.py:128 Connecting to Mongo at 127.150.242.244:13306
DEBUG    pytest_server_fixtures.base2:base2.py:229 waited 0:00:01.220147 for server to start successfully
DEBUG    pytest_server_fixtures.base2:base2.py:69 Server now awake
INFO     arctic.fixtures.arctic:arctic.py:23 arctic.fixtures: arctic init(mongo_server.api=MongoClient(host=['127.150.242.244:13306'], document_class=dict, tz_aware=False, connect=True))
--------------------------------------------------- Captured log call ----------------------------------------------------
DEBUG    arctic.tickstore.tickstore:tickstore.py:612 2 buckets in 0.00078: approx 2564 ticks/sec
------------------------------------------------- Captured log teardown --------------------------------------------------
DEBUG    pytest_server_fixtures.serverclass.thread:thread.py:54 Killing process tree for 5625 (total_procs_to_kill=1)
DEBUG    pytest_server_fixtures.serverclass.thread:thread.py:35 Killing 1 processes with signal Signals.SIGKILL
DEBUG    pytest_server_fixtures.serverclass.thread:thread.py:39 Waiting for 1 processes to die
DEBUG    pytest_server_fixtures.serverclass.thread:thread.py:43 All processes are terminated
DEBUG    pytest_shutil.workspace:workspace.py:140 
DEBUG    pytest_shutil.workspace:workspace.py:141 =======================================================
DEBUG    pytest_shutil.workspace:workspace.py:142 pytest_shutil deleting workspace /tmp/tmp6ks1irls
DEBUG    pytest_shutil.workspace:workspace.py:143 =======================================================
DEBUG    pytest_shutil.workspace:workspace.py:144
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
------------------------------------------------- Captured stdout setup --------------------------------------------------
{"t":{"$date":"2020-12-25T22:53:47.869-07:00"},"s":"I",  "c":"CONTROL",  "id":23285,   "ctx":"main","msg":"Automatically disabling TLS 1.0, to force-enable TLS 1.0 specify --sslDisabledProtocols 'none'"}
{"t":{"$date":"2020-12-25T22:53:47.872-07:00"},"s":"W",  "c":"ASIO",     "id":22601,   "ctx":"main","msg":"No TransportLayer configured during NetworkInterface startup"}
{"t":{"$date":"2020-12-25T22:53:47.872-07:00"},"s":"I",  "c":"NETWORK",  "id":4648601, "ctx":"main","msg":"Implicit TCP FastOpen unavailable. If TCP FastOpen is required, set tcpFastOpenServer, tcpFastOpenClient, and tcpFastOpenQueueSize."}
{"t":{"$date":"2020-12-25T22:53:47.873-07:00"},"s":"I",  "c":"STORAGE",  "id":4615611, "ctx":"initandlisten","msg":"MongoDB starting","attr":{"pid":5683,"port":15019,"dbPath":"/tmp/tmpiq8ozbpe","architecture":"64-bit","host":"flxsa02"}}
{"t":{"$date":"2020-12-25T22:53:47.873-07:00"},"s":"I",  "c":"CONTROL",  "id":23403,   "ctx":"initandlisten","msg":"Build Info","attr":{"buildInfo":{"version":"4.4.2","gitVersion":"15e73dc5738d2278b688f8929aee605fe4279b0e","openSSLVersion":"OpenSSL 1.0.2g  1 Mar 2016","modules":[],"allocator":"tcmalloc","environment":{"distmod":"ubuntu1604","distarch":"x86_64","target_arch":"x86_64"}}}}
{"t":{"$date":"2020-12-25T22:53:47.873-07:00"},"s":"I",  "c":"CONTROL",  "id":51765,   "ctx":"initandlisten","msg":"Operating System","attr":{"os":{"name":"Ubuntu","version":"16.04"}}}
{"t":{"$date":"2020-12-25T22:53:47.873-07:00"},"s":"I",  "c":"CONTROL",  "id":21951,   "ctx":"initandlisten","msg":"Options set by command line","attr":{"options":{"net":{"bindIp":"127.150.242.244","port":15019,"unixDomainSocket":{"enabled":false}},"storage":{"dbPath":"/tmp/tmpiq8ozbpe","journal":{"enabled":false},"syncPeriodSecs":0.0},"systemLog":{"quiet":true}}}}
{"t":{"$date":"2020-12-25T22:53:47.874-07:00"},"s":"I",  "c":"STORAGE",  "id":22297,   "ctx":"initandlisten","msg":"Using the XFS filesystem is strongly recommended with the WiredTiger storage engine. See http://dochub.mongodb.org/core/prodnotes-filesystem","tags":["startupWarnings"]}
{"t":{"$date":"2020-12-25T22:53:47.874-07:00"},"s":"I",  "c":"STORAGE",  "id":22315,   "ctx":"initandlisten","msg":"Opening WiredTiger","attr":{"config":"create,cache_size=11497M,session_max=33000,eviction=(threads_min=4,threads_max=4),config_base=false,statistics=(fast),log=(enabled=true,archive=true,path=journal,compressor=snappy),file_manager=(close_idle_time=100000,close_scan_interval=10,close_handle_minimum=250),statistics_log=(wait=0),verbose=[recovery_progress,checkpoint_progress,compact_progress],,log=(enabled=false),"}}
{"t":{"$date":"2020-12-25T22:53:48.408-07:00"},"s":"I",  "c":"STORAGE",  "id":22430,   "ctx":"initandlisten","msg":"WiredTiger message","attr":{"message":"[1608962028:408386][5683:0x7f001c695a80], txn-recover: [WT_VERB_RECOVERY | WT_VERB_RECOVERY_PROGRESS] Set global recovery timestamp: (0, 0)"}}
{"t":{"$date":"2020-12-25T22:53:48.408-07:00"},"s":"I",  "c":"STORAGE",  "id":22430,   "ctx":"initandlisten","msg":"WiredTiger message","attr":{"message":"[1608962028:408442][5683:0x7f001c695a80], txn-recover: [WT_VERB_RECOVERY | WT_VERB_RECOVERY_PROGRESS] Set global oldest timestamp: (0, 0)"}}
{"t":{"$date":"2020-12-25T22:53:48.454-07:00"},"s":"I",  "c":"STORAGE",  "id":4795906, "ctx":"initandlisten","msg":"WiredTiger opened","attr":{"durationMillis":580}}
{"t":{"$date":"2020-12-25T22:53:48.454-07:00"},"s":"I",  "c":"RECOVERY", "id":23987,   "ctx":"initandlisten","msg":"WiredTiger recoveryTimestamp","attr":{"recoveryTimestamp":{"$timestamp":{"t":0,"i":0}}}}
{"t":{"$date":"2020-12-25T22:53:48.511-07:00"},"s":"I",  "c":"STORAGE",  "id":4366408, "ctx":"initandlisten","msg":"No table logging settings modifications are required for existing WiredTiger tables","attr":{"loggingEnabled":true}}
{"t":{"$date":"2020-12-25T22:53:48.512-07:00"},"s":"I",  "c":"STORAGE",  "id":22262,   "ctx":"initandlisten","msg":"Timestamp monitor starting"}
{"t":{"$date":"2020-12-25T22:53:48.531-07:00"},"s":"W",  "c":"CONTROL",  "id":22120,   "ctx":"initandlisten","msg":"Access control is not enabled for the database. Read and write access to data and configuration is unrestricted","tags":["startupWarnings"]}
{"t":{"$date":"2020-12-25T22:53:48.531-07:00"},"s":"W",  "c":"CONTROL",  "id":22184,   "ctx":"initandlisten","msg":"Soft rlimits too low","attr":{"currentValue":1024,"recommendedMinimum":64000},"tags":["startupWarnings"]}
{"t":{"$date":"2020-12-25T22:53:48.532-07:00"},"s":"I",  "c":"STORAGE",  "id":20320,   "ctx":"initandlisten","msg":"createCollection","attr":{"namespace":"admin.system.version","uuidDisposition":"provided","uuid":{"uuid":{"$uuid":"3b9d6aec-6d06-4986-8bd3-e34ed542c61f"}},"options":{"uuid":{"$uuid":"3b9d6aec-6d06-4986-8bd3-e34ed542c61f"}}}}
{"t":{"$date":"2020-12-25T22:53:48.598-07:00"},"s":"I",  "c":"INDEX",    "id":20345,   "ctx":"initandlisten","msg":"Index build: done building","attr":{"buildUUID":null,"namespace":"admin.system.version","index":"_id_","commitTimestamp":{"$timestamp":{"t":0,"i":0}}}}
{"t":{"$date":"2020-12-25T22:53:48.598-07:00"},"s":"I",  "c":"COMMAND",  "id":20459,   "ctx":"initandlisten","msg":"Setting featureCompatibilityVersion","attr":{"newVersion":"4.4"}}
{"t":{"$date":"2020-12-25T22:53:48.598-07:00"},"s":"I",  "c":"STORAGE",  "id":20536,   "ctx":"initandlisten","msg":"Flow Control is enabled on this deployment"}
{"t":{"$date":"2020-12-25T22:53:48.599-07:00"},"s":"I",  "c":"STORAGE",  "id":20320,   "ctx":"initandlisten","msg":"createCollection","attr":{"namespace":"local.startup_log","uuidDisposition":"generated","uuid":{"uuid":{"$uuid":"7732b340-f042-415b-910e-7b42dd04eba8"}},"options":{"capped":true,"size":10485760}}}
{"t":{"$date":"2020-12-25T22:53:48.658-07:00"},"s":"I",  "c":"INDEX",    "id":20345,   "ctx":"initandlisten","msg":"Index build: done building","attr":{"buildUUID":null,"namespace":"local.startup_log","index":"_id_","commitTimestamp":{"$timestamp":{"t":0,"i":0}}}}
{"t":{"$date":"2020-12-25T22:53:48.658-07:00"},"s":"I",  "c":"FTDC",     "id":20625,   "ctx":"initandlisten","msg":"Initializing full-time diagnostic data capture","attr":{"dataDirectory":"/tmp/tmpiq8ozbpe/diagnostic.data"}}
{"t":{"$date":"2020-12-25T22:53:48.660-07:00"},"s":"I",  "c":"CONTROL",  "id":20712,   "ctx":"LogicalSessionCacheReap","msg":"Sessions collection is not set up; waiting until next sessions reap interval","attr":{"error":"NamespaceNotFound: config.system.sessions does not exist"}}
{"t":{"$date":"2020-12-25T22:53:48.660-07:00"},"s":"I",  "c":"NETWORK",  "id":23015,   "ctx":"listener","msg":"Listening on","attr":{"address":"127.150.242.244"}}
{"t":{"$date":"2020-12-25T22:53:48.660-07:00"},"s":"I",  "c":"NETWORK",  "id":23016,   "ctx":"listener","msg":"Waiting for connections","attr":{"port":15019,"ssl":"off"}}
{"t":{"$date":"2020-12-25T22:53:48.660-07:00"},"s":"I",  "c":"STORAGE",  "id":20320,   "ctx":"LogicalSessionCacheRefresh","msg":"createCollection","attr":{"namespace":"config.system.sessions","uuidDisposition":"generated","uuid":{"uuid":{"$uuid":"73200051-da4f-44f5-ab3f-e927e88c4b00"}},"options":{}}}
{"t":{"$date":"2020-12-25T22:53:48.753-07:00"},"s":"I",  "c":"INDEX",    "id":20345,   "ctx":"LogicalSessionCacheRefresh","msg":"Index build: done building","attr":{"buildUUID":null,"namespace":"config.system.sessions","index":"_id_","commitTimestamp":{"$timestamp":{"t":0,"i":0}}}}
{"t":{"$date":"2020-12-25T22:53:48.753-07:00"},"s":"I",  "c":"INDEX",    "id":20345,   "ctx":"LogicalSessionCacheRefresh","msg":"Index build: done building","attr":{"buildUUID":null,"namespace":"config.system.sessions","index":"lsidTTLIndex","commitTimestamp":{"$timestamp":{"t":0,"i":0}}}}
{"t":{"$date":"2020-12-25T22:53:48.941-07:00"},"s":"I",  "c":"NETWORK",  "id":51800,   "ctx":"conn1","msg":"client metadata","attr":{"remote":"127.0.0.1:55642","client":"conn1","doc":{"driver":{"name":"PyMongo","version":"3.11.2"},"os":{"type":"Linux","name":"Linux","architecture":"x86_64","version":"4.15.0-128-generic"},"platform":"CPython 3.6.12.final.0"}}}
{"t":{"$date":"2020-12-25T22:53:48.942-07:00"},"s":"I",  "c":"NETWORK",  "id":51800,   "ctx":"conn2","msg":"client metadata","attr":{"remote":"127.0.0.1:55644","client":"conn2","doc":{"driver":{"name":"PyMongo","version":"3.11.2"},"os":{"type":"Linux","name":"Linux","architecture":"x86_64","version":"4.15.0-128-generic"},"platform":"CPython 3.6.12.final.0"}}}
{"t":{"$date":"2020-12-25T22:53:49.045-07:00"},"s":"I",  "c":"NETWORK",  "id":51800,   "ctx":"conn3","msg":"client metadata","attr":{"remote":"127.0.0.1:55646","client":"conn3","doc":{"driver":{"name":"PyMongo","version":"3.11.2"},"os":{"type":"Linux","name":"Linux","architecture":"x86_64","version":"4.15.0-128-generic"},"platform":"CPython 3.6.12.final.0"}}}
{"t":{"$date":"2020-12-25T22:53:49.047-07:00"},"s":"I",  "c":"NETWORK",  "id":51800,   "ctx":"conn4","msg":"client metadata","attr":{"remote":"127.0.0.1:55648","client":"conn4","doc":{"driver":{"name":"PyMongo","version":"3.11.2"},"os":{"type":"Linux","name":"Linux","architecture":"x86_64","version":"4.15.0-128-generic"},"platform":"CPython 3.6.12.final.0"}}}
{"t":{"$date":"2020-12-25T22:53:49.047-07:00"},"s":"I",  "c":"NETWORK",  "id":51800,   "ctx":"conn5","msg":"client metadata","attr":{"remote":"127.0.0.1:55650","client":"conn5","doc":{"driver":{"name":"PyMongo","version":"3.11.2"},"os":{"type":"Linux","name":"Linux","architecture":"x86_64","version":"4.15.0-128-generic"},"platform":"CPython 3.6.12.final.0"}}}
{"t":{"$date":"2020-12-25T22:53:49.052-07:00"},"s":"I",  "c":"NETWORK",  "id":51800,   "ctx":"conn6","msg":"client metadata","attr":{"remote":"127.0.0.1:55652","client":"conn6","doc":{"driver":{"name":"PyMongo","version":"3.11.2"},"os":{"type":"Linux","name":"Linux","architecture":"x86_64","version":"4.15.0-128-generic"},"platform":"CPython 3.6.12.final.0"}}}
{"t":{"$date":"2020-12-25T22:53:49.054-07:00"},"s":"I",  "c":"NETWORK",  "id":51800,   "ctx":"conn7","msg":"client metadata","attr":{"remote":"127.0.0.1:55654","client":"conn7","doc":{"driver":{"name":"PyMongo","version":"3.11.2"},"os":{"type":"Linux","name":"Linux","architecture":"x86_64","version":"4.15.0-128-generic"},"platform":"CPython 3.6.12.final.0"}}}
{"t":{"$date":"2020-12-25T22:53:49.054-07:00"},"s":"I",  "c":"NETWORK",  "id":51800,   "ctx":"conn8","msg":"client metadata","attr":{"remote":"127.0.0.1:55656","client":"conn8","doc":{"driver":{"name":"PyMongo","version":"3.11.2"},"os":{"type":"Linux","name":"Linux","architecture":"x86_64","version":"4.15.0-128-generic"},"platform":"CPython 3.6.12.final.0"}}}
{"t":{"$date":"2020-12-25T22:53:49.058-07:00"},"s":"I",  "c":"STORAGE",  "id":20320,   "ctx":"conn7","msg":"createCollection","attr":{"namespace":"meta_db.cache","uuidDisposition":"generated","uuid":{"uuid":{"$uuid":"694575dd-b9db-40a4-a8ad-8daf2b2e1626"}},"options":{}}}
{"t":{"$date":"2020-12-25T22:53:49.123-07:00"},"s":"I",  "c":"INDEX",    "id":20345,   "ctx":"conn7","msg":"Index build: done building","attr":{"buildUUID":null,"namespace":"meta_db.cache","index":"_id_","commitTimestamp":{"$timestamp":{"t":0,"i":0}}}}
{"t":{"$date":"2020-12-25T22:53:49.124-07:00"},"s":"I",  "c":"INDEX",    "id":20438,   "ctx":"conn7","msg":"Index build: registering","attr":{"buildUUID":{"uuid":{"$uuid":"299afacb-7558-44b2-b451-fcafa232beb7"}},"namespace":"meta_db.cache","collectionUUID":{"uuid":{"$uuid":"694575dd-b9db-40a4-a8ad-8daf2b2e1626"}},"indexes":1,"firstIndex":{"name":"date_1"}}}
{"t":{"$date":"2020-12-25T22:53:49.150-07:00"},"s":"I",  "c":"INDEX",    "id":20345,   "ctx":"conn7","msg":"Index build: done building","attr":{"buildUUID":null,"namespace":"meta_db.cache","index":"date_1","commitTimestamp":{"$timestamp":{"t":0,"i":0}}}}
{"t":{"$date":"2020-12-25T22:53:49.150-07:00"},"s":"I",  "c":"INDEX",    "id":20440,   "ctx":"conn7","msg":"Index build: waiting for index build to complete","attr":{"buildUUID":{"uuid":{"$uuid":"299afacb-7558-44b2-b451-fcafa232beb7"}},"deadline":{"$date":{"$numberLong":"9223372036854775807"}}}}
{"t":{"$date":"2020-12-25T22:53:49.150-07:00"},"s":"I",  "c":"INDEX",    "id":20447,   "ctx":"conn7","msg":"Index build: completed","attr":{"buildUUID":{"uuid":{"$uuid":"299afacb-7558-44b2-b451-fcafa232beb7"}}}}
{"t":{"$date":"2020-12-25T22:53:49.151-07:00"},"s":"I",  "c":"STORAGE",  "id":20320,   "ctx":"conn7","msg":"createCollection","attr":{"namespace":"arctic_test.tickstore.ARCTIC","uuidDisposition":"generated","uuid":{"uuid":{"$uuid":"b55b19fa-609a-4fb9-b906-8b359caf9796"}},"options":{}}}
{"t":{"$date":"2020-12-25T22:53:49.218-07:00"},"s":"I",  "c":"INDEX",    "id":20345,   "ctx":"conn7","msg":"Index build: done building","attr":{"buildUUID":null,"namespace":"arctic_test.tickstore.ARCTIC","index":"_id_","commitTimestamp":{"$timestamp":{"t":0,"i":0}}}}
{"t":{"$date":"2020-12-25T22:53:49.219-07:00"},"s":"I",  "c":"STORAGE",  "id":20320,   "ctx":"conn7","msg":"createCollection","attr":{"namespace":"arctic_test.tickstore","uuidDisposition":"generated","uuid":{"uuid":{"$uuid":"7e1fe30b-9e37-40ac-af00-940dea4f6fa1"}},"options":{}}}
{"t":{"$date":"2020-12-25T22:53:49.326-07:00"},"s":"I",  "c":"INDEX",    "id":20345,   "ctx":"conn7","msg":"Index build: done building","attr":{"buildUUID":null,"namespace":"arctic_test.tickstore","index":"_id_","commitTimestamp":{"$timestamp":{"t":0,"i":0}}}}
{"t":{"$date":"2020-12-25T22:53:49.326-07:00"},"s":"I",  "c":"INDEX",    "id":20345,   "ctx":"conn7","msg":"Index build: done building","attr":{"buildUUID":null,"namespace":"arctic_test.tickstore","index":"sy_1_s_1","commitTimestamp":{"$timestamp":{"t":0,"i":0}}}}
{"t":{"$date":"2020-12-25T22:53:49.326-07:00"},"s":"I",  "c":"COMMAND",  "id":51803,   "ctx":"conn7","msg":"Slow query","attr":{"type":"command","ns":"arctic_test.tickstore","command":{"createIndexes":"tickstore","indexes":[{"background":true,"name":"sy_1_s_1","key":{"sy":1,"s":1}}],"lsid":{"id":{"$uuid":"a81936f6-cc43-4981-90c4-ef7b002914d0"}},"$db":"arctic_test","$readPreference":{"mode":"primary"}},"numYields":0,"reslen":114,"locks":{"ParallelBatchWriterMode":{"acquireCount":{"r":5}},"ReplicationStateTransition":{"acquireCount":{"w":5}},"Global":{"acquireCount":{"r":2,"w":3}},"Database":{"acquireCount":{"r":2,"w":3}},"Collection":{"acquireCount":{"r":4,"w":2}},"Mutex":{"acquireCount":{"r":5}}},"flowControl":{"acquireCount":1},"storage":{},"protocol":"op_msg","durationMillis":107}}
{"t":{"$date":"2020-12-25T22:53:49.327-07:00"},"s":"I",  "c":"INDEX",    "id":20438,   "ctx":"conn7","msg":"Index build: registering","attr":{"buildUUID":{"uuid":{"$uuid":"a31086fd-737e-4672-b1ac-e1bb8853d238"}},"namespace":"arctic_test.tickstore","collectionUUID":{"uuid":{"$uuid":"7e1fe30b-9e37-40ac-af00-940dea4f6fa1"}},"indexes":1,"firstIndex":{"name":"s_1"}}}
{"t":{"$date":"2020-12-25T22:53:49.358-07:00"},"s":"I",  "c":"INDEX",    "id":20345,   "ctx":"conn7","msg":"Index build: done building","attr":{"buildUUID":null,"namespace":"arctic_test.tickstore","index":"s_1","commitTimestamp":{"$timestamp":{"t":0,"i":0}}}}
{"t":{"$date":"2020-12-25T22:53:49.358-07:00"},"s":"I",  "c":"INDEX",    "id":20440,   "ctx":"conn7","msg":"Index build: waiting for index build to complete","attr":{"buildUUID":{"uuid":{"$uuid":"a31086fd-737e-4672-b1ac-e1bb8853d238"}},"deadline":{"$date":{"$numberLong":"9223372036854775807"}}}}
{"t":{"$date":"2020-12-25T22:53:49.358-07:00"},"s":"I",  "c":"INDEX",    "id":20447,   "ctx":"conn7","msg":"Index build: completed","attr":{"buildUUID":{"uuid":{"$uuid":"a31086fd-737e-4672-b1ac-e1bb8853d238"}}}}
{"t":{"$date":"2020-12-25T22:53:49.359-07:00"},"s":"I",  "c":"STORAGE",  "id":20320,   "ctx":"conn7","msg":"createCollection","attr":{"namespace":"arctic_test.tickstore.metadata","uuidDisposition":"generated","uuid":{"uuid":{"$uuid":"f832ef0f-9152-45f3-88fd-15acb0c39e73"}},"options":{}}}
{"t":{"$date":"2020-12-25T22:53:49.443-07:00"},"s":"I",  "c":"-",        "id":20883,   "ctx":"conn1","msg":"Interrupted operation as its client disconnected","attr":{"opId":13}}
{"t":{"$date":"2020-12-25T22:53:49.455-07:00"},"s":"I",  "c":"INDEX",    "id":20345,   "ctx":"conn7","msg":"Index build: done building","attr":{"buildUUID":null,"namespace":"arctic_test.tickstore.metadata","index":"_id_","commitTimestamp":{"$timestamp":{"t":0,"i":0}}}}
{"t":{"$date":"2020-12-25T22:53:49.455-07:00"},"s":"I",  "c":"INDEX",    "id":20345,   "ctx":"conn7","msg":"Index build: done building","attr":{"buildUUID":null,"namespace":"arctic_test.tickstore.metadata","index":"sy_1","commitTimestamp":{"$timestamp":{"t":0,"i":0}}}}
--------------------------------------------------- Captured log setup ---------------------------------------------------
DEBUG    pytest_shutil.workspace:workspace.py:52 
DEBUG    pytest_shutil.workspace:workspace.py:53 =======================================================
DEBUG    pytest_shutil.workspace:workspace.py:56 pytest_shutil created workspace /tmp/tmpiq8ozbpe
DEBUG    pytest_shutil.workspace:workspace.py:64 This workspace will delete itself on teardown
DEBUG    pytest_shutil.workspace:workspace.py:65 =======================================================
DEBUG    pytest_shutil.workspace:workspace.py:66 
DEBUG    pytest_server_fixtures.serverclass.thread:thread.py:77 Launching thread server.
DEBUG    pytest_server_fixtures.serverclass.thread:thread.py:89 Running server: mongod --bind_ip=127.150.242.244 --port=15019 --nounixsocket --syncdelay=0 --nojournal --quiet --dbpath=/tmp/tmpiq8ozbpe
DEBUG    pytest_server_fixtures.serverclass.thread:thread.py:90 CWD: /home/cwm/git/bb.FLXSA/quant/arctic_venv36
DEBUG    pytest_server_fixtures.base2:base2.py:226 sleeping for 0.1 before retrying (1 of 28)
INFO     pytest_server_fixtures.mongo:mongo.py:128 Connecting to Mongo at 127.150.242.244:15019
DEBUG    pytest_server_fixtures.base2:base2.py:226 sleeping for 0.1 before retrying (2 of 28)
INFO     pytest_server_fixtures.mongo:mongo.py:128 Connecting to Mongo at 127.150.242.244:15019
DEBUG    pytest_server_fixtures.base2:base2.py:226 sleeping for 0.1 before retrying (3 of 28)
INFO     pytest_server_fixtures.mongo:mongo.py:128 Connecting to Mongo at 127.150.242.244:15019
DEBUG    pytest_server_fixtures.base2:base2.py:229 waited 0:00:01.218521 for server to start successfully
DEBUG    pytest_server_fixtures.base2:base2.py:69 Server now awake
INFO     arctic.fixtures.arctic:arctic.py:23 arctic.fixtures: arctic init(mongo_server.api=MongoClient(host=['127.150.242.244:15019'], document_class=dict, tz_aware=False, connect=True))
--------------------------------------------------- Captured log call ----------------------------------------------------
DEBUG    arctic.tickstore.tickstore:tickstore.py:612 2 buckets in 0.000662: approx 3021 ticks/sec
------------------------------------------------- Captured log teardown --------------------------------------------------
DEBUG    pytest_server_fixtures.serverclass.thread:thread.py:54 Killing process tree for 5683 (total_procs_to_kill=1)
DEBUG    pytest_server_fixtures.serverclass.thread:thread.py:35 Killing 1 processes with signal Signals.SIGKILL
DEBUG    pytest_server_fixtures.serverclass.thread:thread.py:39 Waiting for 1 processes to die
DEBUG    pytest_server_fixtures.serverclass.thread:thread.py:43 All processes are terminated
DEBUG    pytest_shutil.workspace:workspace.py:140 
DEBUG    pytest_shutil.workspace:workspace.py:141 =======================================================
DEBUG    pytest_shutil.workspace:workspace.py:142 pytest_shutil deleting workspace /tmp/tmpiq8ozbpe
DEBUG    pytest_shutil.workspace:workspace.py:143 =======================================================
DEBUG    pytest_shutil.workspace:workspace.py:144
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
------------------------------------------------- Captured stdout setup --------------------------------------------------
{"t":{"$date":"2020-12-25T22:53:49.561-07:00"},"s":"I",  "c":"CONTROL",  "id":23285,   "ctx":"main","msg":"Automatically disabling TLS 1.0, to force-enable TLS 1.0 specify --sslDisabledProtocols 'none'"}
{"t":{"$date":"2020-12-25T22:53:49.562-07:00"},"s":"W",  "c":"ASIO",     "id":22601,   "ctx":"main","msg":"No TransportLayer configured during NetworkInterface startup"}
{"t":{"$date":"2020-12-25T22:53:49.562-07:00"},"s":"I",  "c":"NETWORK",  "id":4648601, "ctx":"main","msg":"Implicit TCP FastOpen unavailable. If TCP FastOpen is required, set tcpFastOpenServer, tcpFastOpenClient, and tcpFastOpenQueueSize."}
{"t":{"$date":"2020-12-25T22:53:49.563-07:00"},"s":"I",  "c":"STORAGE",  "id":4615611, "ctx":"initandlisten","msg":"MongoDB starting","attr":{"pid":5735,"port":25867,"dbPath":"/tmp/tmpqaj3l650","architecture":"64-bit","host":"flxsa02"}}
{"t":{"$date":"2020-12-25T22:53:49.563-07:00"},"s":"I",  "c":"CONTROL",  "id":23403,   "ctx":"initandlisten","msg":"Build Info","attr":{"buildInfo":{"version":"4.4.2","gitVersion":"15e73dc5738d2278b688f8929aee605fe4279b0e","openSSLVersion":"OpenSSL 1.0.2g  1 Mar 2016","modules":[],"allocator":"tcmalloc","environment":{"distmod":"ubuntu1604","distarch":"x86_64","target_arch":"x86_64"}}}}
{"t":{"$date":"2020-12-25T22:53:49.563-07:00"},"s":"I",  "c":"CONTROL",  "id":51765,   "ctx":"initandlisten","msg":"Operating System","attr":{"os":{"name":"Ubuntu","version":"16.04"}}}
{"t":{"$date":"2020-12-25T22:53:49.563-07:00"},"s":"I",  "c":"CONTROL",  "id":21951,   "ctx":"initandlisten","msg":"Options set by command line","attr":{"options":{"net":{"bindIp":"127.150.242.244","port":25867,"unixDomainSocket":{"enabled":false}},"storage":{"dbPath":"/tmp/tmpqaj3l650","journal":{"enabled":false},"syncPeriodSecs":0.0},"systemLog":{"quiet":true}}}}
{"t":{"$date":"2020-12-25T22:53:49.564-07:00"},"s":"I",  "c":"STORAGE",  "id":22297,   "ctx":"initandlisten","msg":"Using the XFS filesystem is strongly recommended with the WiredTiger storage engine. See http://dochub.mongodb.org/core/prodnotes-filesystem","tags":["startupWarnings"]}
{"t":{"$date":"2020-12-25T22:53:49.564-07:00"},"s":"I",  "c":"STORAGE",  "id":22315,   "ctx":"initandlisten","msg":"Opening WiredTiger","attr":{"config":"create,cache_size=11497M,session_max=33000,eviction=(threads_min=4,threads_max=4),config_base=false,statistics=(fast),log=(enabled=true,archive=true,path=journal,compressor=snappy),file_manager=(close_idle_time=100000,close_scan_interval=10,close_handle_minimum=250),statistics_log=(wait=0),verbose=[recovery_progress,checkpoint_progress,compact_progress],,log=(enabled=false),"}}
{"t":{"$date":"2020-12-25T22:53:50.106-07:00"},"s":"I",  "c":"STORAGE",  "id":22430,   "ctx":"initandlisten","msg":"WiredTiger message","attr":{"message":"[1608962030:106937][5735:0x7fb11b9daa80], txn-recover: [WT_VERB_RECOVERY | WT_VERB_RECOVERY_PROGRESS] Set global recovery timestamp: (0, 0)"}}
{"t":{"$date":"2020-12-25T22:53:50.106-07:00"},"s":"I",  "c":"STORAGE",  "id":22430,   "ctx":"initandlisten","msg":"WiredTiger message","attr":{"message":"[1608962030:106989][5735:0x7fb11b9daa80], txn-recover: [WT_VERB_RECOVERY | WT_VERB_RECOVERY_PROGRESS] Set global oldest timestamp: (0, 0)"}}
{"t":{"$date":"2020-12-25T22:53:50.152-07:00"},"s":"I",  "c":"STORAGE",  "id":4795906, "ctx":"initandlisten","msg":"WiredTiger opened","attr":{"durationMillis":588}}
{"t":{"$date":"2020-12-25T22:53:50.152-07:00"},"s":"I",  "c":"RECOVERY", "id":23987,   "ctx":"initandlisten","msg":"WiredTiger recoveryTimestamp","attr":{"recoveryTimestamp":{"$timestamp":{"t":0,"i":0}}}}
{"t":{"$date":"2020-12-25T22:53:50.213-07:00"},"s":"I",  "c":"STORAGE",  "id":4366408, "ctx":"initandlisten","msg":"No table logging settings modifications are required for existing WiredTiger tables","attr":{"loggingEnabled":true}}
{"t":{"$date":"2020-12-25T22:53:50.213-07:00"},"s":"I",  "c":"STORAGE",  "id":22262,   "ctx":"initandlisten","msg":"Timestamp monitor starting"}
{"t":{"$date":"2020-12-25T22:53:50.234-07:00"},"s":"W",  "c":"CONTROL",  "id":22120,   "ctx":"initandlisten","msg":"Access control is not enabled for the database. Read and write access to data and configuration is unrestricted","tags":["startupWarnings"]}
{"t":{"$date":"2020-12-25T22:53:50.234-07:00"},"s":"W",  "c":"CONTROL",  "id":22184,   "ctx":"initandlisten","msg":"Soft rlimits too low","attr":{"currentValue":1024,"recommendedMinimum":64000},"tags":["startupWarnings"]}
{"t":{"$date":"2020-12-25T22:53:50.234-07:00"},"s":"I",  "c":"STORAGE",  "id":20320,   "ctx":"initandlisten","msg":"createCollection","attr":{"namespace":"admin.system.version","uuidDisposition":"provided","uuid":{"uuid":{"$uuid":"93ae271b-39d0-4e12-84a1-3904b0e2d2b1"}},"options":{"uuid":{"$uuid":"93ae271b-39d0-4e12-84a1-3904b0e2d2b1"}}}}
{"t":{"$date":"2020-12-25T22:53:50.297-07:00"},"s":"I",  "c":"INDEX",    "id":20345,   "ctx":"initandlisten","msg":"Index build: done building","attr":{"buildUUID":null,"namespace":"admin.system.version","index":"_id_","commitTimestamp":{"$timestamp":{"t":0,"i":0}}}}
{"t":{"$date":"2020-12-25T22:53:50.297-07:00"},"s":"I",  "c":"COMMAND",  "id":20459,   "ctx":"initandlisten","msg":"Setting featureCompatibilityVersion","attr":{"newVersion":"4.4"}}
{"t":{"$date":"2020-12-25T22:53:50.297-07:00"},"s":"I",  "c":"STORAGE",  "id":20536,   "ctx":"initandlisten","msg":"Flow Control is enabled on this deployment"}
{"t":{"$date":"2020-12-25T22:53:50.298-07:00"},"s":"I",  "c":"STORAGE",  "id":20320,   "ctx":"initandlisten","msg":"createCollection","attr":{"namespace":"local.startup_log","uuidDisposition":"generated","uuid":{"uuid":{"$uuid":"d5c09448-decb-4c59-b290-5f6ed2842e5c"}},"options":{"capped":true,"size":10485760}}}
{"t":{"$date":"2020-12-25T22:53:50.359-07:00"},"s":"I",  "c":"INDEX",    "id":20345,   "ctx":"initandlisten","msg":"Index build: done building","attr":{"buildUUID":null,"namespace":"local.startup_log","index":"_id_","commitTimestamp":{"$timestamp":{"t":0,"i":0}}}}
{"t":{"$date":"2020-12-25T22:53:50.359-07:00"},"s":"I",  "c":"FTDC",     "id":20625,   "ctx":"initandlisten","msg":"Initializing full-time diagnostic data capture","attr":{"dataDirectory":"/tmp/tmpqaj3l650/diagnostic.data"}}
{"t":{"$date":"2020-12-25T22:53:50.360-07:00"},"s":"I",  "c":"NETWORK",  "id":23015,   "ctx":"listener","msg":"Listening on","attr":{"address":"127.150.242.244"}}
{"t":{"$date":"2020-12-25T22:53:50.361-07:00"},"s":"I",  "c":"NETWORK",  "id":23016,   "ctx":"listener","msg":"Waiting for connections","attr":{"port":25867,"ssl":"off"}}
{"t":{"$date":"2020-12-25T22:53:50.361-07:00"},"s":"I",  "c":"CONTROL",  "id":20712,   "ctx":"LogicalSessionCacheReap","msg":"Sessions collection is not set up; waiting until next sessions reap interval","attr":{"error":"NamespaceNotFound: config.system.sessions does not exist"}}
{"t":{"$date":"2020-12-25T22:53:50.361-07:00"},"s":"I",  "c":"STORAGE",  "id":20320,   "ctx":"LogicalSessionCacheRefresh","msg":"createCollection","attr":{"namespace":"config.system.sessions","uuidDisposition":"generated","uuid":{"uuid":{"$uuid":"e6ac8b57-1979-4725-b750-e87dfa2f3d3a"}},"options":{}}}
{"t":{"$date":"2020-12-25T22:53:50.475-07:00"},"s":"I",  "c":"INDEX",    "id":20345,   "ctx":"LogicalSessionCacheRefresh","msg":"Index build: done building","attr":{"buildUUID":null,"namespace":"config.system.sessions","index":"_id_","commitTimestamp":{"$timestamp":{"t":0,"i":0}}}}
{"t":{"$date":"2020-12-25T22:53:50.475-07:00"},"s":"I",  "c":"INDEX",    "id":20345,   "ctx":"LogicalSessionCacheRefresh","msg":"Index build: done building","attr":{"buildUUID":null,"namespace":"config.system.sessions","index":"lsidTTLIndex","commitTimestamp":{"$timestamp":{"t":0,"i":0}}}}
{"t":{"$date":"2020-12-25T22:53:50.475-07:00"},"s":"I",  "c":"COMMAND",  "id":51803,   "ctx":"LogicalSessionCacheRefresh","msg":"Slow query","attr":{"type":"command","ns":"config.system.sessions","command":{"createIndexes":"system.sessions","indexes":[{"key":{"lastUse":1},"name":"lsidTTLIndex","expireAfterSeconds":1800}],"writeConcern":{},"$db":"config"},"numYields":0,"reslen":114,"locks":{"ParallelBatchWriterMode":{"acquireCount":{"r":5}},"ReplicationStateTransition":{"acquireCount":{"w":5}},"Global":{"acquireCount":{"r":2,"w":3}},"Database":{"acquireCount":{"r":2,"w":3}},"Collection":{"acquireCount":{"r":3,"w":2}},"Mutex":{"acquireCount":{"r":6}}},"flowControl":{"acquireCount":1,"timeAcquiringMicros":1},"storage":{},"protocol":"op_msg","durationMillis":114}}
{"t":{"$date":"2020-12-25T22:53:50.637-07:00"},"s":"I",  "c":"NETWORK",  "id":51800,   "ctx":"conn1","msg":"client metadata","attr":{"remote":"127.0.0.1:58916","client":"conn1","doc":{"driver":{"name":"PyMongo","version":"3.11.2"},"os":{"type":"Linux","name":"Linux","architecture":"x86_64","version":"4.15.0-128-generic"},"platform":"CPython 3.6.12.final.0"}}}
{"t":{"$date":"2020-12-25T22:53:50.638-07:00"},"s":"I",  "c":"NETWORK",  "id":51800,   "ctx":"conn2","msg":"client metadata","attr":{"remote":"127.0.0.1:58918","client":"conn2","doc":{"driver":{"name":"PyMongo","version":"3.11.2"},"os":{"type":"Linux","name":"Linux","architecture":"x86_64","version":"4.15.0-128-generic"},"platform":"CPython 3.6.12.final.0"}}}
{"t":{"$date":"2020-12-25T22:53:50.738-07:00"},"s":"I",  "c":"NETWORK",  "id":51800,   "ctx":"conn3","msg":"client metadata","attr":{"remote":"127.0.0.1:58920","client":"conn3","doc":{"driver":{"name":"PyMongo","version":"3.11.2"},"os":{"type":"Linux","name":"Linux","architecture":"x86_64","version":"4.15.0-128-generic"},"platform":"CPython 3.6.12.final.0"}}}
{"t":{"$date":"2020-12-25T22:53:50.739-07:00"},"s":"I",  "c":"NETWORK",  "id":51800,   "ctx":"conn4","msg":"client metadata","attr":{"remote":"127.0.0.1:58922","client":"conn4","doc":{"driver":{"name":"PyMongo","version":"3.11.2"},"os":{"type":"Linux","name":"Linux","architecture":"x86_64","version":"4.15.0-128-generic"},"platform":"CPython 3.6.12.final.0"}}}
{"t":{"$date":"2020-12-25T22:53:50.739-07:00"},"s":"I",  "c":"NETWORK",  "id":51800,   "ctx":"conn5","msg":"client metadata","attr":{"remote":"127.0.0.1:58924","client":"conn5","doc":{"driver":{"name":"PyMongo","version":"3.11.2"},"os":{"type":"Linux","name":"Linux","architecture":"x86_64","version":"4.15.0-128-generic"},"platform":"CPython 3.6.12.final.0"}}}
{"t":{"$date":"2020-12-25T22:53:50.741-07:00"},"s":"I",  "c":"NETWORK",  "id":51800,   "ctx":"conn6","msg":"client metadata","attr":{"remote":"127.0.0.1:58926","client":"conn6","doc":{"driver":{"name":"PyMongo","version":"3.11.2"},"os":{"type":"Linux","name":"Linux","architecture":"x86_64","version":"4.15.0-128-generic"},"platform":"CPython 3.6.12.final.0"}}}
{"t":{"$date":"2020-12-25T22:53:50.743-07:00"},"s":"I",  "c":"NETWORK",  "id":51800,   "ctx":"conn7","msg":"client metadata","attr":{"remote":"127.0.0.1:58928","client":"conn7","doc":{"driver":{"name":"PyMongo","version":"3.11.2"},"os":{"type":"Linux","name":"Linux","architecture":"x86_64","version":"4.15.0-128-generic"},"platform":"CPython 3.6.12.final.0"}}}
{"t":{"$date":"2020-12-25T22:53:50.743-07:00"},"s":"I",  "c":"NETWORK",  "id":51800,   "ctx":"conn8","msg":"client metadata","attr":{"remote":"127.0.0.1:58930","client":"conn8","doc":{"driver":{"name":"PyMongo","version":"3.11.2"},"os":{"type":"Linux","name":"Linux","architecture":"x86_64","version":"4.15.0-128-generic"},"platform":"CPython 3.6.12.final.0"}}}
{"t":{"$date":"2020-12-25T22:53:50.746-07:00"},"s":"I",  "c":"STORAGE",  "id":20320,   "ctx":"conn7","msg":"createCollection","attr":{"namespace":"meta_db.cache","uuidDisposition":"generated","uuid":{"uuid":{"$uuid":"40d8dfd1-c04d-4e9a-bf8b-efecdf6a634c"}},"options":{}}}
{"t":{"$date":"2020-12-25T22:53:50.822-07:00"},"s":"I",  "c":"INDEX",    "id":20345,   "ctx":"conn7","msg":"Index build: done building","attr":{"buildUUID":null,"namespace":"meta_db.cache","index":"_id_","commitTimestamp":{"$timestamp":{"t":0,"i":0}}}}
{"t":{"$date":"2020-12-25T22:53:50.823-07:00"},"s":"I",  "c":"INDEX",    "id":20438,   "ctx":"conn7","msg":"Index build: registering","attr":{"buildUUID":{"uuid":{"$uuid":"8253ba48-2e9d-40d2-ad83-4fc0045a2788"}},"namespace":"meta_db.cache","collectionUUID":{"uuid":{"$uuid":"40d8dfd1-c04d-4e9a-bf8b-efecdf6a634c"}},"indexes":1,"firstIndex":{"name":"date_1"}}}
{"t":{"$date":"2020-12-25T22:53:50.858-07:00"},"s":"I",  "c":"INDEX",    "id":20345,   "ctx":"conn7","msg":"Index build: done building","attr":{"buildUUID":null,"namespace":"meta_db.cache","index":"date_1","commitTimestamp":{"$timestamp":{"t":0,"i":0}}}}
{"t":{"$date":"2020-12-25T22:53:50.858-07:00"},"s":"I",  "c":"INDEX",    "id":20440,   "ctx":"conn7","msg":"Index build: waiting for index build to complete","attr":{"buildUUID":{"uuid":{"$uuid":"8253ba48-2e9d-40d2-ad83-4fc0045a2788"}},"deadline":{"$date":{"$numberLong":"9223372036854775807"}}}}
{"t":{"$date":"2020-12-25T22:53:50.858-07:00"},"s":"I",  "c":"INDEX",    "id":20447,   "ctx":"conn7","msg":"Index build: completed","attr":{"buildUUID":{"uuid":{"$uuid":"8253ba48-2e9d-40d2-ad83-4fc0045a2788"}}}}
{"t":{"$date":"2020-12-25T22:53:50.860-07:00"},"s":"I",  "c":"STORAGE",  "id":20320,   "ctx":"conn7","msg":"createCollection","attr":{"namespace":"arctic_test.tickstore.ARCTIC","uuidDisposition":"generated","uuid":{"uuid":{"$uuid":"a9cba7f3-5d64-4cb0-9c5a-25a97da2445c"}},"options":{}}}
{"t":{"$date":"2020-12-25T22:53:50.951-07:00"},"s":"I",  "c":"INDEX",    "id":20345,   "ctx":"conn7","msg":"Index build: done building","attr":{"buildUUID":null,"namespace":"arctic_test.tickstore.ARCTIC","index":"_id_","commitTimestamp":{"$timestamp":{"t":0,"i":0}}}}
{"t":{"$date":"2020-12-25T22:53:50.952-07:00"},"s":"I",  "c":"STORAGE",  "id":20320,   "ctx":"conn7","msg":"createCollection","attr":{"namespace":"arctic_test.tickstore","uuidDisposition":"generated","uuid":{"uuid":{"$uuid":"3eeb4bde-b400-461d-acbb-3125486bfff0"}},"options":{}}}
{"t":{"$date":"2020-12-25T22:53:51.106-07:00"},"s":"I",  "c":"INDEX",    "id":20345,   "ctx":"conn7","msg":"Index build: done building","attr":{"buildUUID":null,"namespace":"arctic_test.tickstore","index":"_id_","commitTimestamp":{"$timestamp":{"t":0,"i":0}}}}
{"t":{"$date":"2020-12-25T22:53:51.106-07:00"},"s":"I",  "c":"INDEX",    "id":20345,   "ctx":"conn7","msg":"Index build: done building","attr":{"buildUUID":null,"namespace":"arctic_test.tickstore","index":"sy_1_s_1","commitTimestamp":{"$timestamp":{"t":0,"i":0}}}}
{"t":{"$date":"2020-12-25T22:53:51.106-07:00"},"s":"I",  "c":"COMMAND",  "id":51803,   "ctx":"conn7","msg":"Slow query","attr":{"type":"command","ns":"arctic_test.tickstore","command":{"createIndexes":"tickstore","indexes":[{"background":true,"name":"sy_1_s_1","key":{"sy":1,"s":1}}],"lsid":{"id":{"$uuid":"12337b82-dc05-4bae-a9b8-73aa0d5a0ba0"}},"$db":"arctic_test","$readPreference":{"mode":"primary"}},"numYields":0,"reslen":114,"locks":{"ParallelBatchWriterMode":{"acquireCount":{"r":5}},"ReplicationStateTransition":{"acquireCount":{"w":5}},"Global":{"acquireCount":{"r":2,"w":3}},"Database":{"acquireCount":{"r":2,"w":3}},"Collection":{"acquireCount":{"r":4,"w":2}},"Mutex":{"acquireCount":{"r":5}}},"flowControl":{"acquireCount":1,"timeAcquiringMicros":1},"storage":{},"protocol":"op_msg","durationMillis":154}}
{"t":{"$date":"2020-12-25T22:53:51.107-07:00"},"s":"I",  "c":"INDEX",    "id":20438,   "ctx":"conn7","msg":"Index build: registering","attr":{"buildUUID":{"uuid":{"$uuid":"b6078aa6-eb62-4eae-9baa-65cd921bdd56"}},"namespace":"arctic_test.tickstore","collectionUUID":{"uuid":{"$uuid":"3eeb4bde-b400-461d-acbb-3125486bfff0"}},"indexes":1,"firstIndex":{"name":"s_1"}}}
{"t":{"$date":"2020-12-25T22:53:51.138-07:00"},"s":"I",  "c":"-",        "id":20883,   "ctx":"conn1","msg":"Interrupted operation as its client disconnected","attr":{"opId":13}}
{"t":{"$date":"2020-12-25T22:53:51.172-07:00"},"s":"I",  "c":"INDEX",    "id":20345,   "ctx":"conn7","msg":"Index build: done building","attr":{"buildUUID":null,"namespace":"arctic_test.tickstore","index":"s_1","commitTimestamp":{"$timestamp":{"t":0,"i":0}}}}
{"t":{"$date":"2020-12-25T22:53:51.172-07:00"},"s":"I",  "c":"INDEX",    "id":20440,   "ctx":"conn7","msg":"Index build: waiting for index build to complete","attr":{"buildUUID":{"uuid":{"$uuid":"b6078aa6-eb62-4eae-9baa-65cd921bdd56"}},"deadline":{"$date":{"$numberLong":"9223372036854775807"}}}}
{"t":{"$date":"2020-12-25T22:53:51.172-07:00"},"s":"I",  "c":"INDEX",    "id":20447,   "ctx":"conn7","msg":"Index build: completed","attr":{"buildUUID":{"uuid":{"$uuid":"b6078aa6-eb62-4eae-9baa-65cd921bdd56"}}}}
{"t":{"$date":"2020-12-25T22:53:51.172-07:00"},"s":"I",  "c":"STORAGE",  "id":20320,   "ctx":"conn7","msg":"createCollection","attr":{"namespace":"arctic_test.tickstore.metadata","uuidDisposition":"generated","uuid":{"uuid":{"$uuid":"94ae3c40-c0d4-4220-b969-3e2534c07490"}},"options":{}}}
{"t":{"$date":"2020-12-25T22:53:51.240-07:00"},"s":"I",  "c":"-",        "id":20883,   "ctx":"conn3","msg":"Interrupted operation as its client disconnected","attr":{"opId":16}}
{"t":{"$date":"2020-12-25T22:53:51.416-07:00"},"s":"I",  "c":"INDEX",    "id":20345,   "ctx":"conn7","msg":"Index build: done building","attr":{"buildUUID":null,"namespace":"arctic_test.tickstore.metadata","index":"_id_","commitTimestamp":{"$timestamp":{"t":0,"i":0}}}}
{"t":{"$date":"2020-12-25T22:53:51.416-07:00"},"s":"I",  "c":"INDEX",    "id":20345,   "ctx":"conn7","msg":"Index build: done building","attr":{"buildUUID":null,"namespace":"arctic_test.tickstore.metadata","index":"sy_1","commitTimestamp":{"$timestamp":{"t":0,"i":0}}}}
{"t":{"$date":"2020-12-25T22:53:51.416-07:00"},"s":"I",  "c":"COMMAND",  "id":51803,   "ctx":"conn7","msg":"Slow query","attr":{"type":"command","ns":"arctic_test.tickstore.metadata","command":{"createIndexes":"tickstore.metadata","indexes":[{"background":true,"unique":true,"name":"sy_1","key":{"sy":1}}],"lsid":{"id":{"$uuid":"12337b82-dc05-4bae-a9b8-73aa0d5a0ba0"}},"$db":"arctic_test","$readPreference":{"mode":"primary"}},"numYields":0,"reslen":114,"locks":{"ParallelBatchWriterMode":{"acquireCount":{"r":5}},"ReplicationStateTransition":{"acquireCount":{"w":5}},"Global":{"acquireCount":{"r":2,"w":3}},"Database":{"acquireCount":{"r":2,"w":3}},"Collection":{"acquireCount":{"r":4,"w":2}},"Mutex":{"acquireCount":{"r":5}}},"flowControl":{"acquireCount":1,"timeAcquiringMicros":1},"storage":{},"protocol":"op_msg","durationMillis":244}}
--------------------------------------------------- Captured log setup ---------------------------------------------------
DEBUG    pytest_shutil.workspace:workspace.py:52 
DEBUG    pytest_shutil.workspace:workspace.py:53 =======================================================
DEBUG    pytest_shutil.workspace:workspace.py:56 pytest_shutil created workspace /tmp/tmpqaj3l650
DEBUG    pytest_shutil.workspace:workspace.py:64 This workspace will delete itself on teardown
DEBUG    pytest_shutil.workspace:workspace.py:65 =======================================================
DEBUG    pytest_shutil.workspace:workspace.py:66 
DEBUG    pytest_server_fixtures.serverclass.thread:thread.py:77 Launching thread server.
DEBUG    pytest_server_fixtures.serverclass.thread:thread.py:89 Running server: mongod --bind_ip=127.150.242.244 --port=25867 --nounixsocket --syncdelay=0 --nojournal --quiet --dbpath=/tmp/tmpqaj3l650
DEBUG    pytest_server_fixtures.serverclass.thread:thread.py:90 CWD: /home/cwm/git/bb.FLXSA/quant/arctic_venv36
DEBUG    pytest_server_fixtures.base2:base2.py:226 sleeping for 0.1 before retrying (1 of 28)
INFO     pytest_server_fixtures.mongo:mongo.py:128 Connecting to Mongo at 127.150.242.244:25867
DEBUG    pytest_server_fixtures.base2:base2.py:226 sleeping for 0.1 before retrying (2 of 28)
INFO     pytest_server_fixtures.mongo:mongo.py:128 Connecting to Mongo at 127.150.242.244:25867
DEBUG    pytest_server_fixtures.base2:base2.py:226 sleeping for 0.1 before retrying (3 of 28)
INFO     pytest_server_fixtures.mongo:mongo.py:128 Connecting to Mongo at 127.150.242.244:25867
DEBUG    pytest_server_fixtures.base2:base2.py:229 waited 0:00:01.212167 for server to start successfully
DEBUG    pytest_server_fixtures.base2:base2.py:69 Server now awake
INFO     arctic.fixtures.arctic:arctic.py:23 arctic.fixtures: arctic init(mongo_server.api=MongoClient(host=['127.150.242.244:25867'], document_class=dict, tz_aware=False, connect=True))
--------------------------------------------------- Captured log call ----------------------------------------------------
DEBUG    arctic.tickstore.tickstore:tickstore.py:612 3 buckets in 0.000704: approx 4261 ticks/sec
INFO     arctic.tickstore.tickstore:tickstore.py:232 No end provided.  Loading a month for: SYM:None
INFO     arctic.tickstore.tickstore:tickstore.py:355 Got data in 0.002837 secs, creating DataFrame...
INFO     arctic.tickstore.tickstore:tickstore.py:364 2 rows in 0.003672 secs: 544 ticks/sec
INFO     arctic.tickstore.tickstore:tickstore.py:232 No end provided.  Loading a month for: SYM:None
INFO     arctic.tickstore.tickstore:tickstore.py:355 Got data in 0.004317 secs, creating DataFrame...
INFO     arctic.tickstore.tickstore:tickstore.py:364 2 rows in 0.005413 secs: 369 ticks/sec
INFO     arctic.tickstore.tickstore:tickstore.py:232 No end provided.  Loading a month for: SYM:None
INFO     arctic.tickstore.tickstore:tickstore.py:355 Got data in 0.004132 secs, creating DataFrame...
INFO     arctic.tickstore.tickstore:tickstore.py:364 1 rows in 0.005008 secs: 199 ticks/sec
------------------------------------------------- Captured log teardown --------------------------------------------------
DEBUG    pytest_server_fixtures.serverclass.thread:thread.py:54 Killing process tree for 5735 (total_procs_to_kill=1)
DEBUG    pytest_server_fixtures.serverclass.thread:thread.py:35 Killing 1 processes with signal Signals.SIGKILL
DEBUG    pytest_server_fixtures.serverclass.thread:thread.py:39 Waiting for 1 processes to die
DEBUG    pytest_server_fixtures.serverclass.thread:thread.py:43 All processes are terminated
DEBUG    pytest_shutil.workspace:workspace.py:140 
DEBUG    pytest_shutil.workspace:workspace.py:141 =======================================================
DEBUG    pytest_shutil.workspace:workspace.py:142 pytest_shutil deleting workspace /tmp/tmpqaj3l650
DEBUG    pytest_shutil.workspace:workspace.py:143 =======================================================
DEBUG    pytest_shutil.workspace:workspace.py:144
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
------------------------------------------------- Captured stdout setup --------------------------------------------------
{"t":{"$date":"2020-12-25T22:54:18.521-07:00"},"s":"I",  "c":"CONTROL",  "id":23285,   "ctx":"main","msg":"Automatically disabling TLS 1.0, to force-enable TLS 1.0 specify --sslDisabledProtocols 'none'"}
{"t":{"$date":"2020-12-25T22:54:18.522-07:00"},"s":"W",  "c":"ASIO",     "id":22601,   "ctx":"main","msg":"No TransportLayer configured during NetworkInterface startup"}
{"t":{"$date":"2020-12-25T22:54:18.522-07:00"},"s":"I",  "c":"NETWORK",  "id":4648601, "ctx":"main","msg":"Implicit TCP FastOpen unavailable. If TCP FastOpen is required, set tcpFastOpenServer, tcpFastOpenClient, and tcpFastOpenQueueSize."}
{"t":{"$date":"2020-12-25T22:54:18.523-07:00"},"s":"I",  "c":"STORAGE",  "id":4615611, "ctx":"initandlisten","msg":"MongoDB starting","attr":{"pid":6632,"port":16952,"dbPath":"/tmp/tmphg8x27sg","architecture":"64-bit","host":"flxsa02"}}
{"t":{"$date":"2020-12-25T22:54:18.523-07:00"},"s":"I",  "c":"CONTROL",  "id":23403,   "ctx":"initandlisten","msg":"Build Info","attr":{"buildInfo":{"version":"4.4.2","gitVersion":"15e73dc5738d2278b688f8929aee605fe4279b0e","openSSLVersion":"OpenSSL 1.0.2g  1 Mar 2016","modules":[],"allocator":"tcmalloc","environment":{"distmod":"ubuntu1604","distarch":"x86_64","target_arch":"x86_64"}}}}
{"t":{"$date":"2020-12-25T22:54:18.523-07:00"},"s":"I",  "c":"CONTROL",  "id":51765,   "ctx":"initandlisten","msg":"Operating System","attr":{"os":{"name":"Ubuntu","version":"16.04"}}}
{"t":{"$date":"2020-12-25T22:54:18.523-07:00"},"s":"I",  "c":"CONTROL",  "id":21951,   "ctx":"initandlisten","msg":"Options set by command line","attr":{"options":{"net":{"bindIp":"127.150.242.244","port":16952,"unixDomainSocket":{"enabled":false}},"storage":{"dbPath":"/tmp/tmphg8x27sg","journal":{"enabled":false},"syncPeriodSecs":0.0},"systemLog":{"quiet":true}}}}
{"t":{"$date":"2020-12-25T22:54:18.524-07:00"},"s":"I",  "c":"STORAGE",  "id":22297,   "ctx":"initandlisten","msg":"Using the XFS filesystem is strongly recommended with the WiredTiger storage engine. See http://dochub.mongodb.org/core/prodnotes-filesystem","tags":["startupWarnings"]}
{"t":{"$date":"2020-12-25T22:54:18.524-07:00"},"s":"I",  "c":"STORAGE",  "id":22315,   "ctx":"initandlisten","msg":"Opening WiredTiger","attr":{"config":"create,cache_size=11497M,session_max=33000,eviction=(threads_min=4,threads_max=4),config_base=false,statistics=(fast),log=(enabled=true,archive=true,path=journal,compressor=snappy),file_manager=(close_idle_time=100000,close_scan_interval=10,close_handle_minimum=250),statistics_log=(wait=0),verbose=[recovery_progress,checkpoint_progress,compact_progress],,log=(enabled=false),"}}
{"t":{"$date":"2020-12-25T22:54:19.059-07:00"},"s":"I",  "c":"STORAGE",  "id":22430,   "ctx":"initandlisten","msg":"WiredTiger message","attr":{"message":"[1608962059:59822][6632:0x7f7647244a80], txn-recover: [WT_VERB_RECOVERY | WT_VERB_RECOVERY_PROGRESS] Set global recovery timestamp: (0, 0)"}}
{"t":{"$date":"2020-12-25T22:54:19.059-07:00"},"s":"I",  "c":"STORAGE",  "id":22430,   "ctx":"initandlisten","msg":"WiredTiger message","attr":{"message":"[1608962059:59875][6632:0x7f7647244a80], txn-recover: [WT_VERB_RECOVERY | WT_VERB_RECOVERY_PROGRESS] Set global oldest timestamp: (0, 0)"}}
{"t":{"$date":"2020-12-25T22:54:19.107-07:00"},"s":"I",  "c":"STORAGE",  "id":4795906, "ctx":"initandlisten","msg":"WiredTiger opened","attr":{"durationMillis":583}}
{"t":{"$date":"2020-12-25T22:54:19.107-07:00"},"s":"I",  "c":"RECOVERY", "id":23987,   "ctx":"initandlisten","msg":"WiredTiger recoveryTimestamp","attr":{"recoveryTimestamp":{"$timestamp":{"t":0,"i":0}}}}
{"t":{"$date":"2020-12-25T22:54:19.165-07:00"},"s":"I",  "c":"STORAGE",  "id":4366408, "ctx":"initandlisten","msg":"No table logging settings modifications are required for existing WiredTiger tables","attr":{"loggingEnabled":true}}
{"t":{"$date":"2020-12-25T22:54:19.166-07:00"},"s":"I",  "c":"STORAGE",  "id":22262,   "ctx":"initandlisten","msg":"Timestamp monitor starting"}
{"t":{"$date":"2020-12-25T22:54:19.186-07:00"},"s":"W",  "c":"CONTROL",  "id":22120,   "ctx":"initandlisten","msg":"Access control is not enabled for the database. Read and write access to data and configuration is unrestricted","tags":["startupWarnings"]}
{"t":{"$date":"2020-12-25T22:54:19.186-07:00"},"s":"W",  "c":"CONTROL",  "id":22184,   "ctx":"initandlisten","msg":"Soft rlimits too low","attr":{"currentValue":1024,"recommendedMinimum":64000},"tags":["startupWarnings"]}
{"t":{"$date":"2020-12-25T22:54:19.186-07:00"},"s":"I",  "c":"STORAGE",  "id":20320,   "ctx":"initandlisten","msg":"createCollection","attr":{"namespace":"admin.system.version","uuidDisposition":"provided","uuid":{"uuid":{"$uuid":"51ca9848-e47e-4f0a-8362-7de819c1277f"}},"options":{"uuid":{"$uuid":"51ca9848-e47e-4f0a-8362-7de819c1277f"}}}}
{"t":{"$date":"2020-12-25T22:54:19.250-07:00"},"s":"I",  "c":"INDEX",    "id":20345,   "ctx":"initandlisten","msg":"Index build: done building","attr":{"buildUUID":null,"namespace":"admin.system.version","index":"_id_","commitTimestamp":{"$timestamp":{"t":0,"i":0}}}}
{"t":{"$date":"2020-12-25T22:54:19.250-07:00"},"s":"I",  "c":"COMMAND",  "id":20459,   "ctx":"initandlisten","msg":"Setting featureCompatibilityVersion","attr":{"newVersion":"4.4"}}
{"t":{"$date":"2020-12-25T22:54:19.250-07:00"},"s":"I",  "c":"STORAGE",  "id":20536,   "ctx":"initandlisten","msg":"Flow Control is enabled on this deployment"}
{"t":{"$date":"2020-12-25T22:54:19.250-07:00"},"s":"I",  "c":"STORAGE",  "id":20320,   "ctx":"initandlisten","msg":"createCollection","attr":{"namespace":"local.startup_log","uuidDisposition":"generated","uuid":{"uuid":{"$uuid":"e0c902bc-6567-4ff1-94d6-e210a752c381"}},"options":{"capped":true,"size":10485760}}}
{"t":{"$date":"2020-12-25T22:54:19.314-07:00"},"s":"I",  "c":"INDEX",    "id":20345,   "ctx":"initandlisten","msg":"Index build: done building","attr":{"buildUUID":null,"namespace":"local.startup_log","index":"_id_","commitTimestamp":{"$timestamp":{"t":0,"i":0}}}}
{"t":{"$date":"2020-12-25T22:54:19.314-07:00"},"s":"I",  "c":"FTDC",     "id":20625,   "ctx":"initandlisten","msg":"Initializing full-time diagnostic data capture","attr":{"dataDirectory":"/tmp/tmphg8x27sg/diagnostic.data"}}
{"t":{"$date":"2020-12-25T22:54:19.315-07:00"},"s":"I",  "c":"NETWORK",  "id":23015,   "ctx":"listener","msg":"Listening on","attr":{"address":"127.150.242.244"}}
{"t":{"$date":"2020-12-25T22:54:19.315-07:00"},"s":"I",  "c":"NETWORK",  "id":23016,   "ctx":"listener","msg":"Waiting for connections","attr":{"port":16952,"ssl":"off"}}
{"t":{"$date":"2020-12-25T22:54:19.315-07:00"},"s":"I",  "c":"CONTROL",  "id":20712,   "ctx":"LogicalSessionCacheReap","msg":"Sessions collection is not set up; waiting until next sessions reap interval","attr":{"error":"NamespaceNotFound: config.system.sessions does not exist"}}
{"t":{"$date":"2020-12-25T22:54:19.316-07:00"},"s":"I",  "c":"STORAGE",  "id":20320,   "ctx":"LogicalSessionCacheRefresh","msg":"createCollection","attr":{"namespace":"config.system.sessions","uuidDisposition":"generated","uuid":{"uuid":{"$uuid":"5e21c0a2-08b0-4ed6-a25b-cfbdf406ea59"}},"options":{}}}
{"t":{"$date":"2020-12-25T22:54:19.410-07:00"},"s":"I",  "c":"INDEX",    "id":20345,   "ctx":"LogicalSessionCacheRefresh","msg":"Index build: done building","attr":{"buildUUID":null,"namespace":"config.system.sessions","index":"_id_","commitTimestamp":{"$timestamp":{"t":0,"i":0}}}}
{"t":{"$date":"2020-12-25T22:54:19.410-07:00"},"s":"I",  "c":"INDEX",    "id":20345,   "ctx":"LogicalSessionCacheRefresh","msg":"Index build: done building","attr":{"buildUUID":null,"namespace":"config.system.sessions","index":"lsidTTLIndex","commitTimestamp":{"$timestamp":{"t":0,"i":0}}}}
{"t":{"$date":"2020-12-25T22:54:19.593-07:00"},"s":"I",  "c":"NETWORK",  "id":51800,   "ctx":"conn1","msg":"client metadata","attr":{"remote":"127.0.0.1:51794","client":"conn1","doc":{"driver":{"name":"PyMongo","version":"3.11.2"},"os":{"type":"Linux","name":"Linux","architecture":"x86_64","version":"4.15.0-128-generic"},"platform":"CPython 3.6.12.final.0"}}}
{"t":{"$date":"2020-12-25T22:54:19.594-07:00"},"s":"I",  "c":"NETWORK",  "id":51800,   "ctx":"conn2","msg":"client metadata","attr":{"remote":"127.0.0.1:51796","client":"conn2","doc":{"driver":{"name":"PyMongo","version":"3.11.2"},"os":{"type":"Linux","name":"Linux","architecture":"x86_64","version":"4.15.0-128-generic"},"platform":"CPython 3.6.12.final.0"}}}
{"t":{"$date":"2020-12-25T22:54:19.695-07:00"},"s":"I",  "c":"NETWORK",  "id":51800,   "ctx":"conn3","msg":"client metadata","attr":{"remote":"127.0.0.1:51798","client":"conn3","doc":{"driver":{"name":"PyMongo","version":"3.11.2"},"os":{"type":"Linux","name":"Linux","architecture":"x86_64","version":"4.15.0-128-generic"},"platform":"CPython 3.6.12.final.0"}}}
{"t":{"$date":"2020-12-25T22:54:19.697-07:00"},"s":"I",  "c":"NETWORK",  "id":51800,   "ctx":"conn4","msg":"client metadata","attr":{"remote":"127.0.0.1:51800","client":"conn4","doc":{"driver":{"name":"PyMongo","version":"3.11.2"},"os":{"type":"Linux","name":"Linux","architecture":"x86_64","version":"4.15.0-128-generic"},"platform":"CPython 3.6.12.final.0"}}}
{"t":{"$date":"2020-12-25T22:54:19.697-07:00"},"s":"I",  "c":"NETWORK",  "id":51800,   "ctx":"conn5","msg":"client metadata","attr":{"remote":"127.0.0.1:51802","client":"conn5","doc":{"driver":{"name":"PyMongo","version":"3.11.2"},"os":{"type":"Linux","name":"Linux","architecture":"x86_64","version":"4.15.0-128-generic"},"platform":"CPython 3.6.12.final.0"}}}
{"t":{"$date":"2020-12-25T22:54:19.700-07:00"},"s":"I",  "c":"NETWORK",  "id":51800,   "ctx":"conn6","msg":"client metadata","attr":{"remote":"127.0.0.1:51804","client":"conn6","doc":{"driver":{"name":"PyMongo","version":"3.11.2"},"os":{"type":"Linux","name":"Linux","architecture":"x86_64","version":"4.15.0-128-generic"},"platform":"CPython 3.6.12.final.0"}}}
{"t":{"$date":"2020-12-25T22:54:19.703-07:00"},"s":"I",  "c":"NETWORK",  "id":51800,   "ctx":"conn7","msg":"client metadata","attr":{"remote":"127.0.0.1:51806","client":"conn7","doc":{"driver":{"name":"PyMongo","version":"3.11.2"},"os":{"type":"Linux","name":"Linux","architecture":"x86_64","version":"4.15.0-128-generic"},"platform":"CPython 3.6.12.final.0"}}}
{"t":{"$date":"2020-12-25T22:54:19.704-07:00"},"s":"I",  "c":"NETWORK",  "id":51800,   "ctx":"conn8","msg":"client metadata","attr":{"remote":"127.0.0.1:51808","client":"conn8","doc":{"driver":{"name":"PyMongo","version":"3.11.2"},"os":{"type":"Linux","name":"Linux","architecture":"x86_64","version":"4.15.0-128-generic"},"platform":"CPython 3.6.12.final.0"}}}
{"t":{"$date":"2020-12-25T22:54:19.708-07:00"},"s":"I",  "c":"STORAGE",  "id":20320,   "ctx":"conn8","msg":"createCollection","attr":{"namespace":"meta_db.cache","uuidDisposition":"generated","uuid":{"uuid":{"$uuid":"ce012ec6-e49a-4f4d-9eaa-51c4822919a0"}},"options":{}}}
{"t":{"$date":"2020-12-25T22:54:19.772-07:00"},"s":"I",  "c":"INDEX",    "id":20345,   "ctx":"conn8","msg":"Index build: done building","attr":{"buildUUID":null,"namespace":"meta_db.cache","index":"_id_","commitTimestamp":{"$timestamp":{"t":0,"i":0}}}}
{"t":{"$date":"2020-12-25T22:54:19.773-07:00"},"s":"I",  "c":"INDEX",    "id":20438,   "ctx":"conn8","msg":"Index build: registering","attr":{"buildUUID":{"uuid":{"$uuid":"d9a021d5-9e1c-4e32-a76e-076945b1436e"}},"namespace":"meta_db.cache","collectionUUID":{"uuid":{"$uuid":"ce012ec6-e49a-4f4d-9eaa-51c4822919a0"}},"indexes":1,"firstIndex":{"name":"date_1"}}}
{"t":{"$date":"2020-12-25T22:54:19.802-07:00"},"s":"I",  "c":"INDEX",    "id":20345,   "ctx":"conn8","msg":"Index build: done building","attr":{"buildUUID":null,"namespace":"meta_db.cache","index":"date_1","commitTimestamp":{"$timestamp":{"t":0,"i":0}}}}
{"t":{"$date":"2020-12-25T22:54:19.802-07:00"},"s":"I",  "c":"INDEX",    "id":20440,   "ctx":"conn8","msg":"Index build: waiting for index build to complete","attr":{"buildUUID":{"uuid":{"$uuid":"d9a021d5-9e1c-4e32-a76e-076945b1436e"}},"deadline":{"$date":{"$numberLong":"9223372036854775807"}}}}
{"t":{"$date":"2020-12-25T22:54:19.802-07:00"},"s":"I",  "c":"INDEX",    "id":20447,   "ctx":"conn8","msg":"Index build: completed","attr":{"buildUUID":{"uuid":{"$uuid":"d9a021d5-9e1c-4e32-a76e-076945b1436e"}}}}
{"t":{"$date":"2020-12-25T22:54:19.803-07:00"},"s":"I",  "c":"STORAGE",  "id":20320,   "ctx":"conn8","msg":"createCollection","attr":{"namespace":"arctic_test.tickstore.ARCTIC","uuidDisposition":"generated","uuid":{"uuid":{"$uuid":"061e5772-64eb-46a9-811f-77d626261f2e"}},"options":{}}}
{"t":{"$date":"2020-12-25T22:54:19.866-07:00"},"s":"I",  "c":"INDEX",    "id":20345,   "ctx":"conn8","msg":"Index build: done building","attr":{"buildUUID":null,"namespace":"arctic_test.tickstore.ARCTIC","index":"_id_","commitTimestamp":{"$timestamp":{"t":0,"i":0}}}}
{"t":{"$date":"2020-12-25T22:54:19.867-07:00"},"s":"I",  "c":"STORAGE",  "id":20320,   "ctx":"conn8","msg":"createCollection","attr":{"namespace":"arctic_test.tickstore","uuidDisposition":"generated","uuid":{"uuid":{"$uuid":"ba940acc-32b3-4410-9899-80ba53f2cd71"}},"options":{}}}
{"t":{"$date":"2020-12-25T22:54:19.991-07:00"},"s":"I",  "c":"INDEX",    "id":20345,   "ctx":"conn8","msg":"Index build: done building","attr":{"buildUUID":null,"namespace":"arctic_test.tickstore","index":"_id_","commitTimestamp":{"$timestamp":{"t":0,"i":0}}}}
{"t":{"$date":"2020-12-25T22:54:19.991-07:00"},"s":"I",  "c":"INDEX",    "id":20345,   "ctx":"conn8","msg":"Index build: done building","attr":{"buildUUID":null,"namespace":"arctic_test.tickstore","index":"sy_1_s_1","commitTimestamp":{"$timestamp":{"t":0,"i":0}}}}
{"t":{"$date":"2020-12-25T22:54:19.991-07:00"},"s":"I",  "c":"COMMAND",  "id":51803,   "ctx":"conn8","msg":"Slow query","attr":{"type":"command","ns":"arctic_test.tickstore","command":{"createIndexes":"tickstore","indexes":[{"background":true,"name":"sy_1_s_1","key":{"sy":1,"s":1}}],"lsid":{"id":{"$uuid":"f535f3e7-8fa5-47bd-a64e-2ba89399e0ae"}},"$db":"arctic_test","$readPreference":{"mode":"primary"}},"numYields":0,"reslen":114,"locks":{"ParallelBatchWriterMode":{"acquireCount":{"r":5}},"ReplicationStateTransition":{"acquireCount":{"w":5}},"Global":{"acquireCount":{"r":2,"w":3}},"Database":{"acquireCount":{"r":2,"w":3}},"Collection":{"acquireCount":{"r":4,"w":2}},"Mutex":{"acquireCount":{"r":5}}},"flowControl":{"acquireCount":1,"timeAcquiringMicros":1},"storage":{},"protocol":"op_msg","durationMillis":123}}
{"t":{"$date":"2020-12-25T22:54:19.992-07:00"},"s":"I",  "c":"INDEX",    "id":20438,   "ctx":"conn8","msg":"Index build: registering","attr":{"buildUUID":{"uuid":{"$uuid":"54a6b642-7e25-4845-b7e5-e1f0a1946cbb"}},"namespace":"arctic_test.tickstore","collectionUUID":{"uuid":{"$uuid":"ba940acc-32b3-4410-9899-80ba53f2cd71"}},"indexes":1,"firstIndex":{"name":"s_1"}}}
{"t":{"$date":"2020-12-25T22:54:20.027-07:00"},"s":"I",  "c":"INDEX",    "id":20345,   "ctx":"conn8","msg":"Index build: done building","attr":{"buildUUID":null,"namespace":"arctic_test.tickstore","index":"s_1","commitTimestamp":{"$timestamp":{"t":0,"i":0}}}}
{"t":{"$date":"2020-12-25T22:54:20.027-07:00"},"s":"I",  "c":"INDEX",    "id":20440,   "ctx":"conn8","msg":"Index build: waiting for index build to complete","attr":{"buildUUID":{"uuid":{"$uuid":"54a6b642-7e25-4845-b7e5-e1f0a1946cbb"}},"deadline":{"$date":{"$numberLong":"9223372036854775807"}}}}
{"t":{"$date":"2020-12-25T22:54:20.027-07:00"},"s":"I",  "c":"INDEX",    "id":20447,   "ctx":"conn8","msg":"Index build: completed","attr":{"buildUUID":{"uuid":{"$uuid":"54a6b642-7e25-4845-b7e5-e1f0a1946cbb"}}}}
{"t":{"$date":"2020-12-25T22:54:20.028-07:00"},"s":"I",  "c":"STORAGE",  "id":20320,   "ctx":"conn8","msg":"createCollection","attr":{"namespace":"arctic_test.tickstore.metadata","uuidDisposition":"generated","uuid":{"uuid":{"$uuid":"33ca2c9c-48ba-4755-b62c-807f7891cbd2"}},"options":{}}}
{"t":{"$date":"2020-12-25T22:54:20.094-07:00"},"s":"I",  "c":"-",        "id":20883,   "ctx":"conn1","msg":"Interrupted operation as its client disconnected","attr":{"opId":13}}
{"t":{"$date":"2020-12-25T22:54:20.121-07:00"},"s":"I",  "c":"INDEX",    "id":20345,   "ctx":"conn8","msg":"Index build: done building","attr":{"buildUUID":null,"namespace":"arctic_test.tickstore.metadata","index":"_id_","commitTimestamp":{"$timestamp":{"t":0,"i":0}}}}
{"t":{"$date":"2020-12-25T22:54:20.121-07:00"},"s":"I",  "c":"INDEX",    "id":20345,   "ctx":"conn8","msg":"Index build: done building","attr":{"buildUUID":null,"namespace":"arctic_test.tickstore.metadata","index":"sy_1","commitTimestamp":{"$timestamp":{"t":0,"i":0}}}}
--------------------------------------------------- Captured log setup ---------------------------------------------------
DEBUG    pytest_shutil.workspace:workspace.py:52 
DEBUG    pytest_shutil.workspace:workspace.py:53 =======================================================
DEBUG    pytest_shutil.workspace:workspace.py:56 pytest_shutil created workspace /tmp/tmphg8x27sg
DEBUG    pytest_shutil.workspace:workspace.py:64 This workspace will delete itself on teardown
DEBUG    pytest_shutil.workspace:workspace.py:65 =======================================================
DEBUG    pytest_shutil.workspace:workspace.py:66 
DEBUG    pytest_server_fixtures.serverclass.thread:thread.py:77 Launching thread server.
DEBUG    pytest_server_fixtures.serverclass.thread:thread.py:89 Running server: mongod --bind_ip=127.150.242.244 --port=16952 --nounixsocket --syncdelay=0 --nojournal --quiet --dbpath=/tmp/tmphg8x27sg
DEBUG    pytest_server_fixtures.serverclass.thread:thread.py:90 CWD: /home/cwm/git/bb.FLXSA/quant/arctic_venv36
DEBUG    pytest_server_fixtures.base2:base2.py:226 sleeping for 0.1 before retrying (1 of 28)
INFO     pytest_server_fixtures.mongo:mongo.py:128 Connecting to Mongo at 127.150.242.244:16952
DEBUG    pytest_server_fixtures.base2:base2.py:226 sleeping for 0.1 before retrying (2 of 28)
INFO     pytest_server_fixtures.mongo:mongo.py:128 Connecting to Mongo at 127.150.242.244:16952
DEBUG    pytest_server_fixtures.base2:base2.py:226 sleeping for 0.1 before retrying (3 of 28)
INFO     pytest_server_fixtures.mongo:mongo.py:128 Connecting to Mongo at 127.150.242.244:16952
DEBUG    pytest_server_fixtures.base2:base2.py:229 waited 0:00:01.215995 for server to start successfully
DEBUG    pytest_server_fixtures.base2:base2.py:69 Server now awake
INFO     arctic.fixtures.arctic:arctic.py:23 arctic.fixtures: arctic init(mongo_server.api=MongoClient(host=['127.150.242.244:16952'], document_class=dict, tz_aware=False, connect=True))
--------------------------------------------------- Captured log call ----------------------------------------------------
DEBUG    arctic.tickstore.tickstore:tickstore.py:612 1 buckets in 0.000555: approx 180180180 ticks/sec
INFO     arctic.tickstore.tickstore:tickstore.py:232 No end provided.  Loading a month for: SYM:None
INFO     arctic.tickstore.tickstore:tickstore.py:355 Got data in 0.002723 secs, creating DataFrame...
INFO     arctic.tickstore.tickstore:tickstore.py:364 5 rows in 0.003711 secs: 1347 ticks/sec
WARNING  arctic.tickstore.tickstore:tickstore.py:706 NB treating all values as 'exists' - no longer sparse
DEBUG    arctic.tickstore.tickstore:tickstore.py:612 1 buckets in 0.000516: approx 193798449 ticks/sec
INFO     arctic.tickstore.tickstore:tickstore.py:232 No end provided.  Loading a month for: SYM:None
INFO     arctic.tickstore.tickstore:tickstore.py:355 Got data in 0.001944 secs, creating DataFrame...
INFO     arctic.tickstore.tickstore:tickstore.py:364 5 rows in 0.002679 secs: 1866 ticks/sec
------------------------------------------------- Captured log teardown --------------------------------------------------
DEBUG    pytest_server_fixtures.serverclass.thread:thread.py:54 Killing process tree for 6632 (total_procs_to_kill=1)
DEBUG    pytest_server_fixtures.serverclass.thread:thread.py:35 Killing 1 processes with signal Signals.SIGKILL
DEBUG    pytest_server_fixtures.serverclass.thread:thread.py:39 Waiting for 1 processes to die
DEBUG    pytest_server_fixtures.serverclass.thread:thread.py:43 All processes are terminated
DEBUG    pytest_shutil.workspace:workspace.py:140 
DEBUG    pytest_shutil.workspace:workspace.py:141 =======================================================
DEBUG    pytest_shutil.workspace:workspace.py:142 pytest_shutil deleting workspace /tmp/tmphg8x27sg
DEBUG    pytest_shutil.workspace:workspace.py:143 =======================================================
DEBUG    pytest_shutil.workspace:workspace.py:144
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
--------------------------------------------------- Captured log call ----------------------------------------------------
WARNING  arctic.tickstore.tickstore:tickstore.py:706 NB treating all values as 'exists' - no longer sparse
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

============== 17 failed, 1273 passed, 29 skipped, 19 xfailed, 1 xpassed, 24 warnings in 1964.26s (0:32:44) ==============
(.venv36) cwm@flxsa02:~/git/bb.FLXSA/quant/arctic_venv36$ 
```