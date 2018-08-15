# VersionStore

# Chunkstore Overview

(note: current doc is based on arctic-1.68.0)

VersionStore serializes and stores Pandas objects, numpy arrays as well as other python types in MongoDB. Objects are `versioned` and new versions are created when a `symbol` is modified. 


# Reading and Writing Data with VersionStore

```
from arctic import Arctic

a = Arctic(‘localhost’)
a.initialize_library('vstore')
lib = a[‘vstore’]
```

At this point you have an empty VersionStore library. You do not need to specify the storage type because VersionStore is the default library type in Arctic. You can write data to it several ways. The most basic is to use the `write` method. [Write](https://github.com/manahl/arctic/blob/master/arctic/store/version_store.py#L563) takes the following arguments:

`symbol, data, metadata=None, prune_previous_version=True, **kwargs`

`symbol` is the name that is used to store/retrieve the data in Arctic. `data` is the data to be stored in MongoDB. `metadata` is optional user defined metadata. It must be a `dict`. `prune_previous_versions` will prune/remove previous versions of the data (provided they have not been included in a snapshot). `kwargs` are passed on to the individual write handler. There are write handlers for different data types.

`write` is designed to write and replace data. If you write symbol `test` with one dataset and write it again with another, the original data will be replace with a new version of the data. 


```
>>> from pandas import DataFrame, MultiIndex
>>> from datetime import datetime as dt


>>> df = DataFrame(data={'data': [1, 2, 3]},
                   index=MultiIndex.from_tuples([(dt(2016, 1, 1), 1),
                                                 (dt(2016, 1, 2), 1),
                                                 (dt(2016, 1, 3), 1)],
                                                names=['date', 'id']))
>>> lib.write('test', df)
>>> lib.read('test').data
               data
date       id      
2016-01-01 1      1
2016-01-02 1      2
2016-01-03 1      3


>>> df = DataFrame(data={'data': [100, 200, 300]},
                   index=MultiIndex.from_tuples([(dt(2016, 1, 1), 1),
                                                 (dt(2016, 1, 2), 1),
                                                 (dt(2016, 1, 3), 1)],
                                               names=['date', 'id']))

>>> lib.write('test', df)
>>> lib.read('test')
               data
date       id      
2016-01-01 1    100
2016-01-02 1    200
2016-01-03 1    300

```

`write` returns a `VersionedItem` object. `VersionedItem` contains the following members:

* symbol
* library
* version
* metadata
* data
* host
