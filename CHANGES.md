
## Changelog

### 1.7 (2015-09-18)

  * Feature: Add support for reading a subset of a pandas DataFrame
    in VersionStore.read by passing in an arctic.date.DateRange

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