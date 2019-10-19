# VersionStore


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
VersionedItem(symbol=test,library=arctic.vstore,data=<class 'NoneType'>,version=1,metadata=None,host=127.0.0.1)

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
VersionedItem(symbol=test,library=arctic.vstore,data=<class 'NoneType'>,version=2,metadata=None,host=127.0.0.1)

>>> lib.read('test').data
               data
date       id
2016-01-01 1    100
2016-01-02 1    200
2016-01-03 1    300

```

`write` returns a `VersionedItem` object. `VersionedItem` contains the following members:

* symbol
* library
* version - version number of the data written
* metadata - metadata if exists, or None
* data (for writes this is None, for reads it contains the data read from the database).
* host

You should also note that VersionStore's `write` effectively overwrites already written data. In the above example, the second `write` replaced the data in symbol `test` with the new dataframe. The original data (version 1) is still available, but must be referenced by its version number in order to retrieve it. The `read` method takes the following arguments:

```
symbol, as_of=None, date_range=None, from_version=None, allow_secondary=None, **kwargs
```

`as_of` allows you to retrieve the data as it was at a specific point in time. You can define that point in time in a number of ways.

* the name of a snapshot (string)
* a version number (int)
* a datetime (`datetime.datetime`)

`date_range` lets you subset the data via an Arctic [DateRange](https://github.com/manahl/arctic/blob/master/arctic/date/_daterange.py#L15) object. `DateRange`s allows you to specify a date range ('2016-01-01', '2016-09-30') with start and end dates, as well as open ended ranges (None, '2016-09-30'). Ranges can be open at either end. `allow_secondary` lets you override the default behavior to allow or disallow reading from secondary members of the mongo cluster.


```
>>> lib.read('test').data
               data
date       id
2016-01-01 1    100
2016-01-02 1    200
2016-01-03 1    300

>>> lib.read('test', as_of=1).data

date       id  data
2016-01-01 1      1
2016-01-02 1      2
2016-01-03 1      3


>>> from arctic.date import DateRange
>>> lib.read('test', date_range=DateRange('2016-01-01', '2016-01-01')).data

date       id  data
2016-01-01 1    100

```

DateRange's only apply to pandas DataFrames, and the dataframe must have a datetime index present.

Another way to write data is with the [`append`](https://github.com/manahl/arctic/blob/master/arctic/store/version_store.py#L473) method. `append` takes the following arguments:

```
symbol, data, metadata=None, prune_previous_version=True, upsert=True, **kwargs
```

`upsert` is the only new argument. `upsert` means that if the symbol does not exist, it will create it. If `upsert` were `False` an error would be raised as there would be no existing data to append to.

```

>>> lib.append('new', df, upsert=False)
~/arctic/arctic/store/version_store.py in append(self, symbol, data, metadata, prune_previous_version, upsert, **kwargs)
    505             return self.write(symbol=symbol, data=data, prune_previous_version=prune_previous_version, metadata=metadata)
    506
--> 507         assert previous_version is not None
    508         dirty_append = False
    509

AssertionError:


>>> lib.append('new', df, upsert=True)
VersionedItem(symbol=new,library=arctic.vstore,data=<class 'NoneType'>,version=1,metadata=None,host=127.0.0.1)

```

# Utility Methods

A number of other utility methods are available:

* delete
* has_symbol
* list_versions
* read_metadata
* write_metadata
* restore_version


`delete` does what you might expect - it deletes a symbol from the library. It takes a single argument, `symbol`. `has_symbol` and `list_symbols` will return information about the current state of symbols in the library. Their signatures are:

```
list_symbols(self, all_symbols=False, snapshot=None, regex=None, **kwargs)

def has_symbol(self, symbol, as_of=None)
```

for `list_symbols`, `all_symbols` if set to `true` will return all symbols, from all snapshots, even if the symbol has been deleted in the current version (but is saved in a snapshot). `snapshot` allows you to list symbols under a specified `snapshot`. `regex` allows you to supply a regular expression to further restrict the list of symbols returned from the query. Arctic uses MongoDB's `$regex` functionality. Mongo supports PERL syntax regex; more information is available [here](https://docs.mongodb.com/manual/reference/operator/query/regex/)

`has_symbol` returns `True` or `False` based on whether the symbol exists or not. You can restrict this check to a specific `version` via `as_of`.


```

>>> lib.delete('new')

>>> lib.list_symbols()
['test']

>>> lib.has_symbol('new')
False

>>> lib.write('test2', df)

>>> lib.list_symbols(regex=".*2")
['test2']

```

`read_metadata` and `write_metadata` allow you to read/set the user defined metadata directly for a given symbol.


```

>>> lib.read_metadata('test2')
VersionedItem(symbol=test2,library=arctic.vstore,data=<class 'NoneType'>,version=1,metadata=None,host=127.0.0.1)

>>> lib.read_metadata('test2').metadata

>>> lib.write_metadata('test2', {'meta': 'data'})
VersionedItem(symbol=test2,library=arctic.vstore,data=<class 'NoneType'>,version=2,metadata={'meta': 'data'},host=127.0.0.1)

>>> lib.read_metadata('test2').metadata
{'meta': 'data'}

```

`restore_version` lets you set the latest version to an older version. You can use `list_versions` to see information about the current state of the versions.

```

>>> lib.list_versions('test')
[{'symbol': 'test',
  'version': 3,
  'deleted': False,
  'date': datetime.datetime(2018, 8, 16, 17, 59, 47, tzinfo=tzfile('/usr/share/zoneinfo/America/New_York')),
  'snapshots': []},
 {'symbol': 'test',
  'version': 2,
  'deleted': False,
  'date': datetime.datetime(2018, 8, 15, 18, 0, 33, tzinfo=tzfile('/usr/share/zoneinfo/America/New_York')),
  'snapshots': []}]


>>> lib.restore_version('test', 2)
VersionedItem(symbol=test,library=arctic.vstore,data=<class 'NoneType'>,version=4,metadata=None,host=127.0.0.1)

>>> lib.read('test').data
               data
date       id
2016-01-01 1    100
2016-01-02 1    200
2016-01-03 1    300

>>> lib.list_versions('test')
[{'symbol': 'test',
  'version': 4,
  'deleted': False,
  'date': datetime.datetime(2018, 8, 16, 18, 54, 10, tzinfo=tzfile('/usr/share/zoneinfo/America/New_York')),
  'snapshots': []},
 {'symbol': 'test',
  'version': 3,
  'deleted': False,
  'date': datetime.datetime(2018, 8, 16, 17, 59, 47, tzinfo=tzfile('/usr/share/zoneinfo/America/New_York')),
  'snapshots': []},
 {'symbol': 'test',
  'version': 2,
  'deleted': False,
  'date': datetime.datetime(2018, 8, 15, 18, 0, 33, tzinfo=tzfile('/usr/share/zoneinfo/America/New_York')),
  'snapshots': []}]

```

Using `restore_version` did not delete the latest version, it simply created a new version with the data referenced by the user supplied version.



# Snapshots

VersionStore allows you to create a snapshot of data and assign it a name. Data that is part of a snapshot that is deleted is still contained in a snapshot. The snapshot methods are:

* snapshot
* delete_snapshot
* list_snapshots

`snapshot` allows you to create a snapshot. Its signature is very simple

```
snap_name, metadata=None, skip_symbols=None, versions=None
```

`snap_name` is the name of the snap shot being created. `metadata` allows you to supply user defined metadata to the snapshot. `skip_symbols` allows you to exclude symbols from the snapshot. `versions` allows you to specify specific versions to include in the snapshot.

`delete_snapshot` and `list_snapshot` function similarly to `delete` and `list_versions` respectively. `list_snapshots` returns a dictionary of `snapshot` names that map to the `metadata` for the snapshot.


```

>>> lib.list_symbols()
['test', 'test2']

>>> lib.snapshot('backup')

>>> lib.list_snapshots()
{'backup': None}

>>> lib.list_symbols(snapshot='backup')
['test', 'test2']

>>> lib.delete('test')

>>> lib.delete('test2')

>>> lib.list_symbols()
[]

>>> lib.list_symbols(snapshot='backup')
['test', 'test2']

>>> lib.read('test')
~/arctic/arctic/store/version_store.py in _read_metadata(self, symbol, as_of, read_preference)
    455         metadata = _version.get('metadata', None)
    456         if metadata is not None and metadata.get('deleted', False) is True:
--> 457             raise NoDataFoundException("No data found for %s in library %s" % (symbol, self._arctic_lib.get_name()))
    458
    459         return _version

NoDataFoundException: No data found for test in library arctic.vstore


>>> lib.read('test', as_of='backup')
VersionedItem(symbol=test,library=arctic.vstore,data=<class 'pandas.core.frame.DataFrame'>,version=4,metadata=None,host=127.0.0.1)

>>> lib.read('test', as_of='backup').data
               data
date       id
2016-01-01 1    100
2016-01-02 1    200
2016-01-03 1    300

```
