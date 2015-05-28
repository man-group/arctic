#
#  Arctic Key-Value store
#

from arctic import Arctic
from datetime import datetime as dt
import pandas as pd


# Connect to the mongo-host / cluster
store = Arctic(mongo_host)

# Data is grouped into 'libraries'.
# Users may have one or more named libraries:
store.list_libraries()

# Create a library
store.initialize_library('username.scratch')

# Get a library
# library = m['username.<library>']
library = store['username.scratch']

# Store some data in the library
df = pd.DataFrame({'prices': [1, 2, 3]},
                  [dt(2014, 1, 1), dt(2014, 1, 2), dt(2014, 1, 3)])
library.write('SYMBOL', df)

# Read some data from the library
# (Note the returned object has an associated version number and metadata.)
library.read('SYMBOL')

# Store some data into the library
library.write('MY_DATA', library.read('SYMBOL').data)

# What symbols (keys) are stored in the library
library.list_symbols()

# Delete the data item
library.delete('MY_DATA')


# Other library functionality

# Store 'metadata' alongside a data item
library.write('MY_DATA', library.read('SYMBOL').data, metadata={'some_key': 'some_value'})

# Query avaialable symbols based on metadata
library.list_symbols(some_key='some_value')

# Find available versions of a symbol
list(library.list_versions('SYMBOL'))

# Snapshot a library
#  (Point-in-time named reference for all symbols in a library.) 
library.snapshot('snapshot_name')
library.list_snapshots()

# Get an old version of a symbol
library.read('SYMBOL', as_of=1)
# Geta version given a snapshot name
library.read('SYMBOL', as_of='snapshot_name')

# Delete a snapshot
library.delete_snapshot('snapshot_name')
