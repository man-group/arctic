## Changelog

### 1.25

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
