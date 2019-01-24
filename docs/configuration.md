# Configuration variables

Arctic has several tuning knobs under [arctic/_config.py](https://github.com/manahl/arctic/blob/master/arctic/_config.py) which affect the functionality of certain modules.

Most of these variables are initialized via environment variables, which are explained in the rest of this section.


## VersionStore

### STRICT_WRITE_HANDLER_MATCH

Controls if Arctic can only match the intended handlers for the data type. If set to true it prevents falling back to pickling if the matching handler (based on the type of data) can't serialize without objects.

```
export STRICT_WRITE_HANDLER_MATCH=1
```

When strict match is enabled and handler fails to serialize without objects, users will receive the the following error:

```
Traceback (most recent call last):
  File "<ipython-input-2-f8740688f9bf>", line 1, in <module>
    library.write('SymbolA', df)
  File "/projects/git/arctic/arctic/decorators.py", line 49, in f_retry
    return f(*args, **kwargs)
  File "/projects/git/arctic/arctic/store/version_store.py", line 671, in write
    handler = self._write_handler(version, symbol, data, **kwargs)
  File "/projects/git/arctic/arctic/store/version_store.py", line 340, in _write_handler
    raise ArcticException("Not falling back to default handler for %s" % symbol)
arctic.exceptions.ArcticException: Not falling back to default handler for SymbolA
```


## NdArrayStore

### CHECK_CORRUPTION_ON_APPEND

Enables more thorough sanity checks for detecting data corruption when issuing appends. The checks will introduce a 5-7% performance hit. This is disabled by default.

```
export CHECK_CORRUPTION_ON_APPEND=1
```



## Serialization

### ARCTIC_AUTO_EXPAND_CHUNK_SIZE

If a row is too large, then auto-expand the data chunk size from the default _CHUNK_SIZE (it is 2MB). It is disabled by default, and the written DataFrame in its serialized Numpy array form shouldn't exceed 2MB.

This setting is effective only when using the incremental serializer.

```
export ARCTIC_AUTO_EXPAND_CHUNK_SIZE=1
```


### MAX_DOCUMENT_SIZE

This configuration variable is used only when ARCTIC_AUTO_EXPAND_CHUNK_SIZE is set and the user writes a DataFrame which has extremely large number of columns (exceed 2MB serialized).

This value must be less than 16MB which is the maximum document size of MongoDB, taking into account the size of other fields, serialized as a BSON object.

It is set with the following default value:

```
In[8]: pymongo.common.MAX_BSON_SIZE * 0.8
Out[8]: 13421772.8
```


### FAST_CHECK_DF_SERIALIZABLE

Optional optimisation feature. When set, it applies a fast check for the *can_write()* of the Pandas-specific store implementations. This check takes place to decide the right write handler, among the registered ones, applied on the data provided by the user to be written/appended. It has a significant impact for large DataFrames, which have columns with object dtype. The benefits are even more evident if the number of object columns is proportionally small to the total number of columns.

```
export FAST_CHECK_DF_SERIALIZABLE=1
```


## Forward pointers

### <span style="color:orange">ARCTIC_FORWARD_POINTERS_CFG</span> (**EPXERIMENTAL**)

This feature flag controls the mode of operation for the data segment references model.

The original implementation of Arctic stores the *_id* values of version document inside the data segment documents (parent references). Therefore, even small updates (i.e. writes where data change very little) cause a large number of documents to be updated, and trigger fetches in the WiredTiger cache (e.g. when appending).

Since Arctic version *1.73.0* the segment referencing model of VersionStore has included a new implementation, named as *forward pointers*. In this model, the segments no longer hold information about the versions which reference/use them, but instead, the list of segment SHAs is stored in the version document itself. This is beneficial in many ways. First, small updates result in updates/writes only for the new data segments, reducing dramatically the number of affected documents by the update queries (faster execution). Second, the WiredTiger cache gets less polluted utilizing the necessary indexes, not fetching existing large data segments in cache. Finally, all the data information is now in one place, the version document itself, making the debugging of data integrity issues easier.

Variable *ARCTIC_FORWARD_POINTERS_CFG* controls the three modes of operation as described below:

```
# This is the default mode of operation (i.e. same as not setting the variable).
# Arctic operates identically to previous versions (<1.73.0).
export ARCTIC_FORWARD_POINTERS_CFG=DISABLED

# This mode of operation maintains both forward pointers and parent references in segments.
# For reads the forward pointer segment references are preferred if they exist.
# This mode is a performance regression, so should be transitional, before switching to ENABLED.
export ARCTIC_FORWARD_POINTERS_CFG=HYBRID

# In this mode of operation, only forward pointers are used, and the created versions are not
# backwards compatible with older (< v1.73.0) Arctic versions.
# Note that it is still possible to read versions written with older Arctic versions
export ARCTIC_FORWARD_POINTERS_CFG=ENABLED
```

The following table documents the compatibility for reading and writing data for all possible combinations of *ARCTIC_FORWARD_POINTERS_CFG*.

```
|                                                  |   Version written with    | Version written with | Version written with |
|                                                  | legacy Arctic / DISABLED  |        HYBRID        |       ENABLED        |
| ------------------------------------------------ | ------------------------- | -------------------- | -------------------- |
|            Read with Arctic < v1.73.0            |            Y              |          Y           |          -           |
|  Read with ARCTIC_FORWARD_POINTERS_CFG=DISABLED  |            Y              |          Y           |          Y           |
|  Read with ARCTIC_FORWARD_POINTERS_CFG=HYBRID    |            Y              |          Y           |          Y           |
|  Read with ARCTIC_FORWARD_POINTERS_CFG=ENABLED   |            Y              |          Y           |          Y           |
|                                                  |                           |                      |                      |
|          Update with Arctic < v1.73.0            |            Y              |          Y           |          -           |
| Update with ARCTIC_FORWARD_POINTERS_CFG=DISABLED |            Y              |          Y           |          Y(*)        |
| Update with ARCTIC_FORWARD_POINTERS_CFG=HYBRID   |            Y              |          Y           |          Y(*)        |
| Update with ARCTIC_FORWARD_POINTERS_CFG=ENABLED  |            Y              |          Y           |          Y           |

(*) appends will be converted to a full write

```

It is recommended to make a full write for all symbols in HYBRID mode when switching for ENABLED to DISABLED.

**Migration plan**

After a certain time under test, the *ARCTIC_FORWARD_POINTERS_CFG=ENABLED* will become the default configuration for future versions of Arctic.
When this happens, the users shouldn't notice any issues, because the transition from DISABLED/HYBRID to ENABLED is safe
for reads and writes per the compatibility table above.

We strongly recommend however, to always transit to configurations via the HYBRID mode:  "DISABLED->HYBRID->ENABLED", and test thoroughly while in HYBRID mode.

When the user desires to switch back to DISABLED it is required to apply the following steps:

1. Drop all snapshots.
2. Switch to HYBRID
3. Force a full read/write for all symbols.
4. Switch to DISABLED


### ARCTIC_FORWARD_POINTERS_RECONCILE

When enabled, the number of segments will be cross-verified between forward and legacy (parent) pointers. It is mostly used to verify the correct functionality of forward pointers as long as it is in experimental state.

It has an effect only when *ARCTIC_FORWARD_POINTERS_CFG=HYBRID* and affects writes/appends.

```
export ARCTIC_FORWARD_POINTERS_RECONCILE=1
```



## Compression settings

### DISABLE_PARALLEL

This flag disables the parallel compression (multiple-threads) for the data segments. The parallel LZ4 compression is enabled by default.

```
export DISABLE_PARALLEL=1
```


### LZ4_HIGH_COMPRESSION

Use the high-compression configuration for LZ4 (trade runtime speed for better compression ratio).


```
export LZ4_HIGH_COMPRESSION=1
```


### LZ4_WORKERS

Configures the size of the compression thread pool (size of 2 by default).

For a guide on how to tune the following parameters, read: arctic/benchmarks/lz4_tuning/README.txt

A rough rule of thumb is to use 2 for non HC (VersionStore/NDarrayStore/PandasStore, and 8 for HC (TickStore).

```
export LZ4_WORKERS=4
```


### LZ4_N_PARALLEL

This setting controls the minimum number of chunks required to use the parallel compression. The default value is 16, derived from benchmark results.

```
export LZ4_N_PARALLEL=4
```


### LZ4_MINSZ_PARALLEL

This setting controls the minimum data size required to use the parallel compression. The default value is 524288 (0.5 MB), derived from benchmark results.

```
export LZ4_MINSZ_PARALLEL=1048576
```
