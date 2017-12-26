# Chunkstore Overview

(note: current doc is based on arctic-1.31.0)

Chunkstore serializes and store Pandas Dataframes and Series into user defined chunks in MongoDB. Retrieving specific chunks, or ranges of chunks, is very fast and efficient. Chunkstore is optimized more for reading than for writing, and is ideal for use cases when very large datasets need to be accessed by 'chunk'.

Chunkstore supports pluggable serializers. A Serializer is used to convert the Pandas datatype into something that can be efficiently stored by Mongo. Chunkstore's default serializer is the [FrameConverter](https://github.com/manahl/arctic/blob/master/arctic/serialization/numpy_arrays.py#L22) which works by converting each column in the dataframe to a compressed Numpy array. Columns can be retrieved individually this way, without deserializing the other columns in the dataframe. 

Chunkstore also supports pluggable chunkers. A chunker takes the dataframe and converts it into chunks. Chunks are stored individually in Mongo for easy retrieval by chunk. Chunkstore currently has two chunkers: [DateRange Chunker](https://github.com/manahl/arctic/blob/master/arctic/chunkstore/date_chunker.py) and [PassThrough Chunker](https://github.com/manahl/arctic/blob/master/arctic/chunkstore/passthrough_chunker.py). The DateRange chunker chunks a dataframe by a datetime index or column. Currently it must be called 'date'. It chunks by a period, Daily, Monthly, or Yearly. The data can be retrieved from Mongo for any date range, so for DateRange chunked data, its important that the chunking period (or size) be selected appropriately. If data will frequently be read in daily increments, choosing a Year chunk size doesn't really make sense and will be slower than data access of daily chunked data. The PassThrough chunker simply takes the dataframe and writes it to mongo. It does not chunk the data.


# Reading and Writing Data Chunkstore

```
from arctic import CHUNK_STORE, Arctic

a = Arctic(‘localhost’)
a.initialize_library(‘chunkstore', lib_type=CHUNK_STORE)
lib = a[‘chunkstore’]
```

At this point you have an empty Chunkstore library. You can write data to it several ways. The most basic is to use the `write` method. [Write](https://github.com/manahl/arctic/blob/master/arctic/chunkstore/chunkstore.py#L230) takes the following arguments:

`symbol, item, chunker=DateChunker(), **kwargs`

`symbol` is the name that is used to store/retrieve the data in Arctic. `item` is the dataframe/series. If you wish to change the chunker type, you can use the keyword arg `chunker` to specify a new chunker. Optional keyword args are passed on to the chunker. For the case of DateRange chunker, you can specify a `chunk_size` (D, M, or Y).

`write` is designed to write and replace data. If you write symbol `test` with one dataset and write it again with another, the original data will be overwritten.


```
>>> from pandas import DataFrame, MultiIndex
>>> from datetime import datetime as dt


>>> df = DataFrame(data={'data': [1, 2, 3]},
                   index=MultiIndex.from_tuples([(dt(2016, 1, 1), 1),
                                                 (dt(2016, 1, 2), 1),
                                                 (dt(2016, 1, 3), 1)],
                                                names=['date', 'id']))
>>> lib.write('test', df)
>>> lib.read('test')
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

We've also introduced the `read` method here. Read takes the following arguments:

`symbol, chunk_range=None, filter_data=True, **kwargs`

`symbol` is the key for the data you wish to retrieve, `chunk_range` varies by chunker. For DateRange chunker, the chunk_range can be a Pandas DatetimeIndex or it can be an Arctic [DateRange](https://github.com/manahl/arctic/blob/master/arctic/date/_daterange.py#L15) object. DateRange allows you to specify a date range ('2016-01-01', '2016-09-30') with start and end dates, as well as open ended ranges (None, '2016-09-30'). Ranges can be open at either end. A chunk range allows you to limit the data retrieved. Without specifying a chunk_range, you will retrieve all the data for the symbol. `filter_data` is not something you'd commonly want to modify. By default, if you give it a chunk_range you'll ONLY receive data included in that range, even if the range is smaller than a chunk size. `filter_data` tells Chunkstore to filter the data from the chunk(s) by the chunk_range even further (if possible). For example: if data is stored monthly, but you give it a range of a single day, with filter_data enabled, you'll only get the data for that single day. With it disabled, you'll get all the data in the chunks that the chunk_range overlaps.

```
>>> df = DataFrame(data={'data': [100, 200, 300]},
                   index=MultiIndex.from_tuples([(dt(2016, 1, 1), 1),
                                                 (dt(2016, 1, 2), 1),
                                                 (dt(2016, 1, 3), 1)],
                                                names=['date', 'id']))



>>> lib.write('test', df, chunk_size='M')
>>> lib.read('test', chunk_range=pd.date_range('2016-01-01', '2016-01-01'))
               data
date       id      
2016-01-01 1    100


>>> lib.read('test', chunk_range=pd.date_range('2016-01-01', '2016-01-01'), filter_data=False)
               data
date       id      
2016-01-01 1    100
2016-01-02 1    200
2016-01-03 1    300

```

There are other ways to write data. Chunkstore supports `append` and `update` as well. The main difference between the two is that update is idempotent while append is not. If you continually append the same data N times, you'll get N copies of that data in the dataframe. Append only allows you to add data, it will not modify any data already written. Update is idempotent, and does allow you to modify already written data. Whereas append simply finds a chunk, and adds new data to it, update finds a chunk and replaces data in it with the new data. Let's take a look at some examples.


```
>>> df = DataFrame(data={'data': [100, 200, 300]},
                  index=MultiIndex.from_tuples([(dt(2016, 1, 1), 1),
                                                (dt(2016, 1, 2), 1),
                                                (dt(2016, 1, 3), 1)],
                                               names=['date', 'id']))


>>> lib.write('test', df, chunk_size='M')
>>> lib.read('test')
               data
date       id      
2016-01-01 1    100
2016-01-02 1    200
2016-01-03 1    300

```

If we take the above symbol, `test` and append data, we should see the data replicated as many times as we append


```
>>> lib.append('test', df)
>>> lib.append('test', df)
>>> lib.read('test')
               data
date       id      
2016-01-01 1    100
           1    100
           1    100
2016-01-02 1    200
           1    200
           1    200
2016-01-03 1    300
           1    300
           1    300

```

As expected, we have the data from the original write, and then two more copies of the data. If we do the same exercise with update, you'll notice a big difference.


```
>>> lib.write('test', df, chunk_size='M')
>>> lib.read('test')
               data
date       id      
2016-01-01 1    100
2016-01-02 1    200
2016-01-03 1    300


>>> lib.update('test', df)
>>> lib.update('test', df)
>>> lib.read('test')
               data
date       id      
2016-01-01 1    100
2016-01-02 1    200
2016-01-03 1    300

```

Lets try that again,  but update with different data

```

>>> lib.read('test')
               data
date       id      
2016-01-01 1    100
2016-01-02 1    200
2016-01-03 1    300


>>> df2 = DataFrame(data={'data': [15]},
                   index=MultiIndex.from_tuples([(dt(2016, 1, 15), 1)],
                                                names=['date', 'id']))
>>> lib.update('test', df2)
>>> lib.read('test')
               data
date       id      
2016-01-15 1     15

```

In its most basic form, `update` replaces chunks in Mongo with chunks in the new data. All the old chunks are deleted and replaced.

Let's take a look at the arguments that `append` and `update` take.

`append: symbol, item`

Append is quite simple - it takes a symbol name to append to, and item to append.

`update: symbol, item, chunk_range=None, upsert=False, **kwargs`

Update similarly takes a symbol and item, but has several optional arguments. `chunk_range` allows you to subset a part of the chunk to overwrite. In the previous example, we overwrote the entire monthly chunk, but you can overwrite a subset of a chunk with chunk_range.

```

>>> lib.read('test')
               data
date       id      
2016-01-01 1    100
2016-01-02 1    200
2016-01-03 1    300


>>> df2 = DataFrame(data={'data': [15]},
                    index=MultiIndex.from_tuples([(dt(2016, 1, 2), 1)],
                                                 names=['date', 'id']))


>>> lib.update('test', df2, chunk_range=pd.date_range('2016-01-02', '2016-01-03'))
>>> lib.read('test')
               data
date       id      
2016-01-01 1    100
2016-01-02 1     15

```

Note that the `chunk_range` specified on the update did not match all the datetimeindex of `df2`. We essentially are telling Chunkstore to replace all the data in `chunk_range` with the data in `df2`.


The other optional arguments, `upsert` and `**kwargs` are only used when `upsert` is true. If `upsert` is false, and `symbol` does not exist, an exception will be raised. If `upsert` is true, and a symbol does not exist, `write` will be called with `symbol`, `item` and `**kwargs`. This means you can specify the same args in `**kwargs` that you would for a write (`chunker`, etc).


# Renaming and Deleting Data in Chunkstore

You can also `delete` and `rename` symbols in Chunkstore. `rename` works as you might expect - You give it a symbol name that you want to rename, and you give it the new symbol name.

```
>>> lib.rename('test', 'new_name')
>>> lib.read('new_name')
               data
date       id      
2016-01-01 1    100
2016-01-02 1     15


>>> lib.read('test')
---------------------------------------------------------------------------
NoDataFoundException                      
Traceback (most recent call last)
----> 1 lib.read('test')

arctic/chunkstore/chunkstore.py in read(self, symbol, chunk_range, filter_data, **kwargs)
    199         sym = self._get_symbol_info(symbol)
    200         if not sym:
--> 201             raise NoDataFoundException('No data found for %s' % (symbol))
    202 
    203         spec = {SYMBOL: symbol,

NoDataFoundException: No data found for test

```

Once a symbol is renamed, the old symbol ceases to exist. Delete also works as you might expect, except it also allows you to delete data within a chunk_range as opposed to deleting an entire symbol.

```
>>> lib.delete('new_name')
>>> lib.write('new_name', df)
>>> lib.read('new_name')
               data
date       id      
2016-01-01 1    100
2016-01-02 1    200
2016-01-03 1    300


>>> lib.delete('new_name', pd.date_range('2016-01-02', '2016-01-02'))
>>> lib.read('new_name')
               data
date       id      
2016-01-01 1    100
2016-01-03 1    300

```


# Other Chunkstore Operations
Other methods on Chunkstore include:
   * `list_symbols()`
   * `get_info(symbol)`
   * `get_chunk_ranges(symbol, chunk_range=None, reverse=False)`
   * `iterator(symbol, chunk_range=None)`
   * `reverse_iterator(symbol, chunk_range=None)`

`list_symbols` list all the symbols in the current library.

```
>>> lib.list_symbols()
[u'new_name']

```

`get_info` returns a dictionary of metadata and information about the symbol, without having to read back any of the chunked data.

```
>>> lib.get_info('new_name')
{'chunk_count': 2,
 'chunk_size': u'D',
 'chunker': u'date',
 'len': 2,
 'metadata': {u'columns': [u'date', u'id', u'data']},
 'serializer': u'FrameToArray'}

```

`chunk_count` is the number of chunks in MongoDB, `len` is the number of rows in the dataframe, and `metadata` contains the column information. The rest of the keys should be self explanatory.

`get_chunk_ranges` returns a generator that produces all the chunk_ranges for the symbol. You can use the optional argument `chunk_rage` to subset the data, and `reverse` to produce the list in reverse order.

```
>>> list(lib.get_chunk_ranges('new_name'))
[('2016-01-01', '2016-01-01'), ('2016-01-03', '2016-01-03')]

```

The two iterator methods also produce generators that allow you to traverse the entire symbol, one chunk at a time. Both take an optional argument, chunk_range that allows you to subset the chunks that the generator will traverse. `iterator` goes in order from start to end, `reverse iterator` goes from end to start.

```

>>> for chunk in lib.reverse_iterator('new_name'):
        print("Chunk is: ")
        print(chunk)

Chunk is:
               data
date       id      
2016-01-03 1    300

Chunk is:
               data
date       id      
2016-01-01 1    100

```
