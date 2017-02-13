# [![arctic](logo/arctic_50.png)](https://github.com/manahl/arctic) [Arctic TimeSeries and Tick store](https://github.com/manahl/arctic)


[![Circle CI](https://circleci.com/gh/manahl/arctic.svg?style=shield)](https://circleci.com/gh/manahl/arctic)
[![Travis CI](https://travis-ci.org/manahl/arctic.svg?branch=master)](https://travis-ci.org/manahl/arctic)
[![Coverage Status](https://coveralls.io/repos/github/manahl/arctic/badge.svg?branch=master)](https://coveralls.io/github/manahl/arctic?branch=master)
[![Join the chat at https://gitter.im/manahl/arctic](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/manahl/arctic?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

Arctic is a high performance datastore for numeric data. It supports [Pandas](http://pandas.pydata.org/),
[numpy](http://www.numpy.org/) arrays and pickled objects out-of-the-box, with pluggable support for
other data types and optional versioning.

Arctic can query millions of rows per second per client, achieves ~10x compression on network bandwidth,
~10x compression on disk, and scales to hundreds of millions of rows per second per
[MongoDB](https://www.mongodb.org/) instance.

Arctic has been under active development at [Man AHL](http://www.ahl.com/) since 2012.

## Quickstart

### Install Arctic

```
pip install git+https://github.com/manahl/arctic.git
```

### Run a MongoDB

```
mongod --dbpath <path/to/db_directory>
```

### Using VersionStore

```
from arctic import Arctic
import quandl

# Connect to Local MONGODB
store = Arctic('localhost')

# Create the library - defaults to VersionStore
store.initialize_library('NASDAQ')

# Access the library
library = store['NASDAQ']

# Load some data - maybe from Quandl
aapl = quandl.get("WIKI/AAPL", authtoken="your token here")

# Store the data in the library
library.write('AAPL', aapl, metadata={'source': 'Quandl'})

# Reading the data
item = library.read('AAPL')
aapl = item.data
metadata = item.metadata
```

VersionStore supports much more: [See the HowTo](howtos/how_to_use_arctic.py)!


### Adding your own storage engine

Plugging a custom class in as a library type is straightforward. [This example
shows how.](howtos/how_to_custom_arctic_library.py)



## Concepts

### Libraries

Arctic provides namespaced *libraries* of data.  These libraries allow
bucketing data by *source*, *user* or some other metric (for example frequency:
End-Of-Day; Minute Bars; etc.).

Arctic supports multiple data libraries per user.  A user (or namespace)
maps to a MongoDB database (the granularity of mongo authentication).  The library
itself is composed of a number of collections within the database. Libraries look like:

  * user.EOD
  * user.ONEMINUTE

A library is mapped to a Python class.  All library databases in MongoDB are prefixed with 'arctic_'

### Storage Engines

Arctic includes three storage engines:

  * [VersionStore](arctic/store/version_store.py): a key-value versioned TimeSeries store. It supports:
      * Pandas data types (other Python types pickled)
      * Multiple versions of each data item. Can easily read previous versions.
      * Create point-in-time snapshots across symbols in a library
      * Soft quota support
      * Hooks for persisting other data types
      * Audited writes: API for saving metadata and data before and after a write.
      * a wide range of TimeSeries data frequencies: End-Of-Day to Minute bars
      * [See the HowTo](howtos/how_to_use_arctic.py)
  * [TickStore](arctic/tickstore/tickstore.py): Column oriented tick database.  Supports
    dynamic fields, chunks aren't versioned. Designed for large continuously ticking data.
  * [Chunkstore](https://github.com/manahl/arctic/wiki/Chunkstore): A storage type that allows data to be stored in customizable chunk sizes. Chunks
    aren't versioned, and can be appended to and updated in place. 

Arctic storage implementations are **pluggable**.  VersionStore is the default.


## Requirements

Arctic currently works with:

 * Python 2.7, 3.4, 3.5, 3.6
 * pymongo >= 3.0
 * Pandas
 * MongoDB >= 2.4.x


## Acknowledgements

Arctic has been under active development at [Man AHL](http://www.ahl.com/) since 2012.

It wouldn't be possible without the work of the AHL Data Engineering Team including:

 * [Richard Bounds](https://github.com/richardbounds)
 * [James Blackburn](https://github.com/jamesblackburn)
 * [Vlad Mereuta](https://github.com/vmereuta)
 * [Tom Taylor](https://github.com/TomTaylorLondon)
 * Tope Olukemi
 * [Drake Siard](https://github.com/drakesiard)
 * [Slavi Marinov](https://github.com/slavi)
 * [Wilfred Hughes](https://github.com/wilfred)
 * [Edward Easton](https://github.com/eeaston)
 * [Bryant Moscon](https://github.com/bmoscon)
 * ... and many others ...

Contributions welcome!

## License

Arctic is licensed under the GNU LGPL v2.1.  A copy of which is included in [LICENSE](LICENSE)
