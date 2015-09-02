
## Changelog

### 1.5

  * Always use the primary cluster node for 'has_symbol()', it's safer

### 1.4

  * Bugfixes for timezone handling, now ensures use of non-naive datetimes
  * Bugfix for tickstore read missing images

### 1.3

  * Improvements to command-line control scripts for users and libraries
  * Bugfix for pickling top-level Arctic object

### 1.2

  * Allow snapshotting a range of versions in the VersionStore, and 
    snapshot all versions by default.

### 1.1

  * Bugfix for backwards-compatible unpickling of bson-encoded data
  * Added switch for enabling parallel lz4 compression

### 1.0

  *  Initial public release