[![Documentation Status](https://readthedocs.org/projects/arctic/badge/?version=latest)](https://arctic.readthedocs.io/en/latest/?badge=latest)
[![CircleCI](https://circleci.com/gh/man-group/arctic/tree/master.svg?style=shield)](https://app.circleci.com/pipelines/github/man-group/arctic?branch=master)
[![PyPI](https://img.shields.io/pypi/v/arctic)](https://pypi.org/project/arctic)
[![Python](https://img.shields.io/badge/Python-3.6|3.7|3.8-green.svg)](https://github.com/man-group/arctic)

## Quickstart

### Install Arctic

``
pip install git+https://github.com/man-group/arctic.git
``

### Run a MongoDB

``
mongod --dbpath <path/to/db_directory>
``

## Using VersionStore
``
from arctic import Arctic
import quandl
``
### Connect to Local MONGODB
``
store = Arctic('localhost')
``

### Create the library - defaults to VersionStore
``
store.initialize_library('NASDAQ')
``

### Access the library
``
library = store['NASDAQ']
``

### Load some data - maybe from Quandl
``
aapl = quandl.get("WIKI/AAPL", authtoken="your token here")
``

### Store the data in the library
``
library.write('AAPL', aapl, metadata={'source': 'Quandl'})
``

### Reading the data
``
item = library.read('AAPL')
aapl = item.data
metadata = item.metadata
``

VersionStore supports much more: [See the HowTo](howtos/how_to_use_arctic.py)!


### Adding your own storage engine

Plugging a custom class in as a library type is straightforward. [This example
shows how.](howtos/how_to_custom_arctic_library.py)

## Documentation

You can find complete documentation at [Arctic docs](https://arctic.readthedocs.io/en/latest/)

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

A library is mapped to a Python class.  All library databases in MongoDB are prefixed with 'arctic\_'

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
      * [Documentation](docs/versionstore.md)
  * [TickStore](arctic/tickstore/tickstore.py): Column oriented tick database.  Supports
    dynamic fields, chunks aren't versioned. Designed for large continuously ticking data.
  * [Chunkstore](https://github.com/man-group/arctic/wiki/Chunkstore): A storage type that allows data to be stored in customizable chunk sizes. Chunks
    aren't versioned, and can be appended to and updated in place. 
    * [Documentation](docs/chunkstore.md)

Arctic storage implementations are **pluggable**.  VersionStore is the default.


## Requirements

Arctic currently works with:

 * python 3.6, 3.7, 3.8
 * pymongo >= 3.6.0 <= 3.11.0
 * pandas >= 0.22.0 < 2
 * MongoDB >= 2.4.x <= 4.4.18


Operating Systems:
 * Linux
 * macOS
 * Windows 10

## Acknowledgements

Arctic has been under active development at [Man Group](https://www.man.com/) since 2012.

It wouldn't be possible without the work of the Man Data Engineering Team including:

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
 * [Dimosthenis Pediaditakis](https://github.com/dimosped)
 * [Shashank Khare](https://github.com/shashank88)
 * [Duncan Kerr](https://github.com/dunckerr)
 * ... and many others ...

Contributions welcome!

## License

Arctic is licensed under the GNU LGPL v2.1.  A copy of which is included in [LICENSE](LICENSE)
