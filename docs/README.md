# Arctic Documentation

Arctic is a tickstore database that sits atop MongoDB. Arctic supports serialization of a number of datatypes for storage in the mongo document model.

Arctic provides a [wrapper](https://github.com/manahl/arctic/blob/docs/arctic/arctic.py) for handling connections to Mongo. The `Arctic` class is what actually connects to Arctic. 

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

Wtih this handle to the library, we can begin to store and retrieve data from Arctic.

(note, most of the storage engines support the same basic methods (read, write, etc), but each have their own set of unique methods as well)






...
...
...
...






Arctic is designed to be very extensible and currently supports a numer of different use cases. To understand what Arctic is capable of, one must understand the storage models it uses. Arctic currently supports three storage engines

* TickStore
* VersionStore
* [Chunkstore](chunkstore.md)