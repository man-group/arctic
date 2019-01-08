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
