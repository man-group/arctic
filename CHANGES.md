## Changelog

### 1.47 (2017-06-19)
  * Feature: Re-introduce #363 `concat` flag, essentially undo-ing 1.45
  * BugFix: #377 Fix broken `replace_one` on BSONStore and add `bulk_write`

### 1.46 (2017-06-13)
  * Feature: #374 Shard BSONStore on `_id` rather than `symbol`

### 1.45 (2017-06-09)
  * BugFix: Rollback #363, which can cause ordering issues on append

### 1.44 (2017-06-08)
  * Feature: #364 Expose compressHC from internal arctic LZ4 and remove external LZ4 dependency
  * Feature: #363 Appending older data (compare to what's exist in library) will raise. Use `concat=True` to append only the
             new bits
  * Feature: #371 Expose more functionality in BSONStore
  
### 1.43 (2017-05-30)
  * Bugfix:  #350 remove deprecated pandas calls
  * Bugfix:  #360 version incorrect in empty append in VersionStore
  * Feature: #365 add generic BSON store

### 1.42 (2017-05-12)
  * Bugfix: #346 fixed daterange subsetting error on very large dataframes in version store
  * Bugfix: #351 $size queries can't use indexes, use alternative queries

### 1.41 (2017-04-20)
  * Bugfix: #334 Chunk range param with pandas object fails in chunkstore.get_chunk_ranges
  * Bugfix: #339 Depending on lz4<=0.8.2 to fix build errors
  * Bugfix: #342 fixed compilation errors on Mac OSX
  * Bugfix: #344 fixed data corruption problem with concurrent appends

### 1.40 (2017-03-03)
  * BugFix: #330 Make Arctic._lock reentrant 

### 1.39 (2017-03-03)
  * Feature:  #329 Add reset() method to Arctic 

### 1.38 (2017-02-22)
  * Bugfix:  #324 Datetime indexes must be sorted in chunkstore
  * Feature: #290 improve performance of tickstore column reads

### 1.37 (2017-1-31)
  * Bugfix:  #300 to_datetime deprecated in pandas, use to_pydatetime instead
  * Bugfix:  #309 formatting change for DateRange ```__str__```
  * Feature: #313 set and read user specified metadata in chunkstore
  * Feature: #319 Audit log support in ChunkStor
  * Bugfix:  #216 Tickstore write fails with named index column


### 1.36 (2016-12-13)
  
  * Feature: Default to hashed based sharding
  * Bugfix: retry socket errors during VersionStore snapshot operations

### 1.35 (2016-11-29)

  * Bugfix:  #296 Cannot compress/decompress empty string

### 1.34 (2016-11-29)

  * Feature: #294 Move per-chunk metadata for chunkstore to a separate collection
  * Bugfix:  #292 Account for metadata size during size chunking in ChunkStore
  * Feature: #283 Support for all pandas frequency strings in ChunkStore DateChunker
  * Feature: #286 Add has_symbol to ChunkStore and support for partial symbol matching in list_symbols

### 1.33 (2016-11-07)
  
  * Feature:    #275 Tuple range object support in DateChunker
  * Bugfix:     #273 Duplicate columns breaking serializer
  * Feature:    #267 Tickstore.delete returns deleted data
  * Dependency: #266 Remove pytest-dbfixtures in favor of pytest-server-fixtures

### 1.32 (2016-10-25)
  
  * Feature: #260 quota support on Chunkstore
  * Bugfix: #259 prevent write of unnamed columns/indexes
  * Bugfix: #252 pandas 0.19.0 compatibility fixes
  * Bugfix: #249 open ended range reads on data without index fail
  * Bugfix: #262 VersionStore.append must check data is written correctly during repack
  * Bugfix: #263 Quota: Improve the error message when near soft-quota limit
  * Perf:   #265 VersionStore.write / append don't aggressively add indexes on each write
  
### 1.31 (2016-09-29)
  
  * Bugfix: #247 segmentation read fix in chunkstore
  * Feature: #243 add get_library_type method
  * Bugfix: more cython changes to handle LZ4 errors properly
  * Feature: #239 improve chunkstore's get_info method

### 1.30 (2016-09-26)

  * Feature: #235 method to return chunk ranges on a symbol in ChunkStore
  * Feature: #234 Iterator access to ChunkStore
  * Bugfix: #236 Cython not handling errors from LZ4 function calls
  
### 1.29 (2016-09-20)

  * Bugfix: #228 Mongo fail-over during append can leave a Version in an inconsistent state
  * Feature: #193 Support for different Chunkers and Serializers by symbol in ChunkStore
  * Feature: #220 Raise exception if older version of arctic attempts to read unsupported pickled data
  * Feature: #219 and #220 Support for pickling large data (>2GB)
  * Feature: #204 Add support for library renaming
  * Feature: #209 Upsert capability in ChunkStore's update method
  * Feature: #207 Support DatetimeIndexes in DateRange chunker
  * Bugfix:  #232 Don't raise during VersionStore #append(...) if the previous append failed

### 1.28 (2016-08-16)

  * Bugfix: #195 Top level tickstore write with list of dicts now works with timezone aware datetimes

### 1.27 (2016-08-05)

  * Bugfix: #187 Compatibility with latest version of pytest-dbfixtures
  * Feature: #182 Improve ChunkStore read/write performance
  * Feature: #162 Rename API for ChunkStore
  * Feature: #186 chunk_range on update
  * Bugfix: #189 range delete does not update symbol metadata

### 1.26 (2016-07-20)

  * Bugfix: Faster TickStore querying for multiple symbols simultaneously
  * Bugfix: TickStore.read now respects `allow_secondary=True`
  * Bugfix: #147 Add get_info method to ChunkStore
  * Bugfix: Periodically re-cache the library.quota to pick up any changes
  * Bugfix: #166 Add index on SHA for ChunkStore
  * Bugfix: #169 Dtype mismatch in chunkstore updates
  * Feature: #171 allow deleting of values within a date range in ChunkStore
  * Bugfix: #172 Fix date range bug when querying dates in the middle of chunks
  * Bugfix: #176 Fix overwrite failures in Chunkstore
  * Bugfix: #178 - Change how start/end dates are populated in the DB, also fix append so it works as expected.
  * Bugfix: #43 - Remove dependency on hardcoded Linux timezone files

### 1.25 (2016-05-23)

  * Bugfix: Ensure that Tickstore.write doesn't allow out of order messages
  * Bugfix: VersionStore.write now allows writing 'None' as a value

### 1.24 (2016-05-10)
  
  * Bugfix: Backwards compatibility reading/writing documents with previous versions of Arctic

### 1.22 (2016-05-09)
  
  * Bugfix: #109 Ensure stable sort during Arctic read
  * Feature: New benchmark suite using ASV
  * Bugfix: #129 Fixed an issue where some chunks could get skipped during a multiple-symbol TickStore read
  * Bugfix: #135 Fix issue with different datatype returned from pymongo in python3
  * Feature: #130 New Chunkstore storage type

### 1.21 (2016-03-08)

  * Bugfix: #106 Fix Pandas Panel storage for panels with different dimensions

### 1.20 (2016-02-03)

  * Feature: #98 Add initial_image as optional parameter on tickstore write()
  * Bugfix: #100 Write error on end field when writing with pandas dataframes

### 1.19 (2016-01-29)

  * Feature: Add python 3.3/3.4 support
  * Bugfix: #95 Fix raising NoDataFoundException across multiple low level libraries

### 1.18 (2016-01-05)

  * Bugfix: #81 Fix broken read of multi-index DataFrame written by old version of Arctic
  * Bugfix: #49 Fix strifying tickstore

### 1.17 (2015-12-24)

  * Feature: Add timezone suppport to store multi-index dataframes
  * Bugfix:  Fixed broken sdist releases

### 1.16 (2015-12-15)

  * Feature: ArticTransaction now supports non-audited 'transactions': `audit=False`
             ```
             with ArcticTransaction(Arctic('hostname')['some_library'], 'symbol', audit=False) as at:
                   ...
             ```
             This is useful for batch jobs which read-modify-write and don't want to clash with
             concurrent writers, and which don't require keeping all versions of a symbol.

### 1.15 (2015-11-25)

  * Feature: get_info API added to version_store.

### 1.14 (2015-11-25)
### 1.12 (2015-11-12)

  * Bugfix: correct version detection for Pandas >= 0.18.
  * Bugfix: retrying connection initialisation in case of an AutoReconnect failure.

### 1.11 (2015-10-29)

  * Bugfix: Improve performance of saving multi-index Pandas DataFrames
    by 9x
  * Bugfix: authenticate should propagate non-OperationFailure exceptions
    (e.g. ConnectionFailure) as this might be indicative of socket failures
  * Bugfix: return 'deleted' state in VersionStore.list_versions() so that
    callers can pick up on the head version being the delete-sentinel.

### 1.10 (2015-10-28)

  * Bugfix: VersionStore.read(date_range=...) could do the wrong thing with
    TimeZones (which aren't yet supported for date_range slicing.).

### 1.9 (2015-10-06)

  * Bugfix: fix authentication race condition when sharing an Arctic
    instance between multiple threads.

### 1.8 (2015-09-29)

  * Bugfix: compatibility with both 3.0 and pre-3.0 MongoDB for
    querying current authentications

### 1.7 (2015-09-18)

  * Feature: Add support for reading a subset of a pandas DataFrame
    in VersionStore.read by passing in an arctic.date.DateRange
  * Bugfix: Reauth against admin if not auth'd against a library a
    specific library's DB.  Sometimes we appear to miss admin DB auths.
    This is to workaround that until we work out what the issue is.

### 1.6 (2015-09-16)

  * Feature: Add support for multi-index Bitemporal DataFrame storage.
    This allows persisting data and changes within the DataFrame making it
    easier to see how old data has been revised over time.
  * Bugfix: Ensure we call the error logging hook when exceptions occur

### 1.5 (2015-09-02)

  * Always use the primary cluster node for 'has_symbol()', it's safer

### 1.4 (2015-08-19)

  * Bugfixes for timezone handling, now ensures use of non-naive datetimes
  * Bugfix for tickstore read missing images

### 1.3 (2015-08-011)

  * Improvements to command-line control scripts for users and libraries
  * Bugfix for pickling top-level Arctic object

### 1.2 (2015-06-29)

  * Allow snapshotting a range of versions in the VersionStore, and
    snapshot all versions by default.

### 1.1 (2015-06-16)

  * Bugfix for backwards-compatible unpickling of bson-encoded data
  * Added switch for enabling parallel lz4 compression

### 1.0 (2015-06-14)

  *  Initial public release
