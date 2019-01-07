# [append](https://github.com/manahl/arctic/blob/master/arctic/chunkstore/chunkstore.py#L376)
```
append(symbol, item)
    Appends data from item to symbol's data in the database.

    Is not idempotent

    Parameters
    ----------
    symbol: str
        the symbol for the given item in the DB
    item: DataFrame or Series
        the data to append
```

Example usage:

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

# [delete](https://github.com/manahl/arctic/blob/master/arctic/chunkstore/chunkstore.py#L102)
```
delete(symbol, chunk_range=None)
    Delete all chunks for a symbol, or optionally, chunks within a range

    Parameters
    ----------
    symbol : str
        symbol name for the item
    chunk_range: range object
        a date range to delete
```
Example usage:

```
>>> lib.read('test')
               data
date       id
2016-01-01 1    100
2016-01-03 1    300

>>> lib.delete('test', chunk_range=pd.date_range('2016-01-01', '2016-01-01'))
>>> lib.read('test')
               data
date       id
2016-01-03 1    300

```

# [get_chunk_ranges](https://github.com/manahl/arctic/blob/master/arctic/chunkstore/chunkstore.py#L452)
```
get_chunk_ranges(symbol, chunk_range=None, reverse=False)
    Returns a generator of (Start, End) tuples for each chunk in the symbol

    Parameters
    ----------
    symbol: str
        the symbol for the given item in the DB
    chunk_range: None, or a range object
        allows you to subset the chunks by range
    reverse: boolean

    Returns
    -------
    generator
```

Example usage:

```
>>> list(lib.get_chunk_ranges('new_name'))
[('2016-01-01', '2016-01-01'), ('2016-01-03', '2016-01-03')]

```


# [get_info](https://github.com/manahl/arctic/blob/master/arctic/chunkstore/chunkstore.py#L431)
```
get_info(symbol)
    Returns information about the symbol, in a dictionary

    Parameters
    ----------
    symbol: str
        the symbol for the given item in the DB

    Returns
    -------
    dictionary
```

# [iterator](https://github.com/manahl/arctic/blob/master/arctic/chunkstore/chunkstore.py#L477)
```
iterator(symbol, chunk_range=None):
    Returns a generator that accesses each chunk in ascending order

    Parameters
    ----------
    symbol: str
        the symbol for the given item in the DB
    chunk_range: None, or a range object
        allows you to subset the chunks by range

    Returns
    -------
    generator
```

# [list_symbols](https://github.com/manahl/arctic/blob/master/arctic/chunkstore/chunkstore.py#L138)
```
list_symbols()
    Returns all symbols in the library

    Returns
    -------
    list of str

```

# [read](https://github.com/manahl/arctic/blob/master/arctic/chunkstore/chunkstore.py#L176)

```
read(symbol, chunk_range=None, filter_data=True, **kwargs)
    Reads data for a given symbol from the database.

    Parameters
    ----------
    symbol: str
        the symbol to retrieve
    chunk_range: object
        corresponding range object for the specified chunker (for
        DateChunker it is a DateRange object or a DatetimeIndex,
        as returned by pandas.date_range
    filter_data: boolean
        perform chunk level filtering on the data (see filter in _chunker)
        only applicable when chunk_range is specified
    kwargs: ?
        values passed to the serializer. Varies by serializer

    Returns
    -------
    DataFrame or Series
```

Example usage:

```

>>> dr = pd.date_range(start='2010-01-01', periods=1000, freq='D')
>>> df = DataFrame(data={'data': np.random.randint(0, 100, size=1000),
                         'date': dr
                        })

>>> lib.write('symbol_name', df, chunk_size='M')
>>> lib.read('symbol_name', chunk_range=pd.date_range('2012-09-01', '2016-01-01'))
    data       date
0     61 2012-09-01
1     69 2012-09-02
2     96 2012-09-03
3     23 2012-09-04
4     66 2012-09-05
5     54 2012-09-06
6     21 2012-09-07
7     92 2012-09-08
8     95 2012-09-09
9     24 2012-09-10
10    87 2012-09-11
11    33 2012-09-12
12    59 2012-09-13
13    54 2012-09-14
14    48 2012-09-15
15    67 2012-09-16
16    73 2012-09-17
17    72 2012-09-18
18     6 2012-09-19
19    24 2012-09-20
20     8 2012-09-21
21    50 2012-09-22
22    40 2012-09-23
23    45 2012-09-24
24     8 2012-09-25
25    73 2012-09-26

```


# [rename](https://github.com/manahl/arctic/blob/master/arctic/chunkstore/chunkstore.py#L151)
```
rename(from_symbol, to_symbol)
    Rename a symbol

    Parameters
    ----------
    from_symbol: str
        the existing symbol that will be renamed
    to_symbol: str
        the new symbol name
```

# [reverse_iterator](https://github.com/manahl/arctic/blob/master/arctic/chunkstore/chunkstore.py#L498)
```
reverse_iterator(symbol, chunk_range=None):
    Returns a generator that accesses each chunk in descending order

    Parameters
    ----------
    symbol: str
        the symbol for the given item in the DB
    chunk_range: None, or a range object
        allows you to subset the chunks by range

    Returns
    -------
    generator
```


# [update](https://github.com/manahl/arctic/blob/master/arctic/chunkstore/chunkstore.py#L394)
```
update(symbol, item, chunk_range=None, upsert=False, **kwargs)
    Overwrites data in DB with data in item for the given symbol.

    Is idempotent

    Parameters
    ----------
    symbol: str
        the symbol for the given item in the DB
    item: DataFrame or Series
        the data to update
    chunk_range: None, or a range object
        If a range is specified, it will clear/delete the data within the
        range and overwrite it with the data in item. This allows the user
        to update with data that might only be a subset of the
        original data.
    upsert: bool
        if True, will write the data even if the symbol does not exist.
    kwargs:
        optional keyword args passed to write during an upsert. Includes:
        chunk_size
        chunker
```


# [write](https://github.com/manahl/arctic/blob/master/arctic/chunkstore/chunkstore.py#L230)
```
write(symbol, item, chunker=DateChunker(), **kwargs)
    Writes data from item to symbol in the database

    Parameters
    ----------
    symbol: str
        the symbol that will be used to reference the written data
    item: Dataframe or Series
        the data to write the database
    chunker: Object of type Chunker
        A chunker that chunks the data in item
    kwargs:
        optional keyword args that are passed to the chunker. Includes:
        chunk_size:
            used by chunker to break data into discrete chunks.
            see specific chunkers for more information about this param.
```

Example usage:

```
>>> dr = pd.date_range(start='2010-01-01', periods=1000, freq='D')
>>> df = DataFrame(data={'data': np.random.randint(0, 100, size=1000),
                         'date': dr
                        })

>>> lib.write('symbol_name', df, chunk_size='M')

```

