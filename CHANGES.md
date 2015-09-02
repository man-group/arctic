
## Changelog

### 1.6

  * Always use the primary cluster node for 'has_symbol()', it's safer

### 1.5

  * Bugfixes for timezone handling, now ensures use of non-naive datetimes
  * Bugfix for tickstore read missing images

### 1.4

  * Improvements to command-line control scripts for users and libraries
  * Bugfix for pickling top-level Arctic object

### 1.3

  * Allow snapshotting a range of versions in the VersionStore, and 
    snapshot all versions by default.

### 1.2

  * Bugfix for backwards-compatible unpickling of bson-encoded data
  * Added switch for enabling parallel lz4 compression

### 1.1

  * Added hook for registering auth provider
  * Tickstore reads now include all fields when prepending images
  * Added 'allow_secondary' argument to VersionStore read methods

### 1.0

  *  Initial public release