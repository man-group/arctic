# Arctic Documentation

Arctic is a timeseries / dataframe database that sits atop MongoDB. Arctic supports serialization of a number of datatypes for storage in the mongo document model.

Arctic provides a [wrapper](../arctic/arctic.py) for handling connections to Mongo. The `Arctic` class is what actually connects to Arctic. 

```
>>> conn = Arctic('127.0.0.1')
```

There are a number of operations that are possible with just this connection handle. The most basic ones are `list_libraries` and `initiailize_library`.

Arctic divides data into different libraries. These could be different users, different markets, different geographic regions, etc. Library names are strings and are entirely user defined. 

```
>>> conn.list_libraries()
    []
```

In this case, there are no libraries on the system, so one can be initialized.

```
>>> conn.initialize_library('library_name')
>>> conn.list_libraries()
    [u'library_name']
```

`initialize_library` has an optional named arg, `lib_type` that defaults to `VersionStore` (more on Arctic storage engine types later).

Once a library is initialized, you can access it like so:

```
>>> lib = conn['library_name']
```

With this handle to the library, we can begin to store and retrieve data from Arctic.

(note, most of the storage engines support the same basic methods (`read`, `write`, etc), but each have their own set of unique methods as well)

`write` in its most basic form takes an Arctic `symbol` and the data. The `symbol` is a user defined key that is used to store/retrieve the data. The `data` in most cases is a Pandas DataFrame, though some storage engines support other types (all support dataframes, and some support dicts and pickleable objects). 

`read` as you might expect takes the `symbol` to read back the data. The different storage engines have different parameters that allow you to subset the data (more on this later).

```
>>> data = pd.DataFrame(.....)
>>> lib.write('symbolname', data)
>>> df = lib.read('symbolname')
>>> df
                data
date             
2016-01-01       1
2016-01-02       2
2016-01-03       3
```


Other basic methods:

* `library.list_symbols()`
    - Does what you might expect - lists all the symbols in the given library
      ```
      >>> lib.list_symbols()

      ['US_EQUITIES', 'EUR_EQUITIES', ...]
      ```
* `arctic.get_quota(library_name)`, `arctic.set_quota(library_name, quota_in_bytes)`
   - Arctic internally sets quotas on libraries so they do not consume too much space.    You can check and set quotas with these two methods. Note these operate on the       `Arctic` object, not on libraries  



### Arctic Storage Engines

Arctic is designed to be very extensible and currently supports a numer of different use cases. To understand what Arctic is capable of, one must understand the storage models it uses. Arctic currently supports three storage engines

* [TickStore](tickstore.md)
* [VersionStore](versionstore.md)
* [Chunkstore](chunkstore.md)

Each one has various features and is designed to support specific and general use cases. 
