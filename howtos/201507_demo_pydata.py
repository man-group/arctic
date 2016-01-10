from __future__ import print_function

################################################
# Getting started
################################################

# Install Arctic
#    pip install git+https://github.com/manahl/arctic.git
# That's it(!)

# Run MongoDB - https://www.mongodb.org/downloads
#    $ mkdir /tmp/pydata-demo
#    $ mongod --dbpath /tmp/pydata-demo

from datetime import datetime
import time
import ystockquote

from arctic import Arctic
import collections
import pandas
import pandas as pd
import pprint


################################################
# Loading data
################################################


def get_stock_history(ticker, start_date, end_date):
    data = ystockquote.get_historical_prices(ticker, start_date, end_date)
    df = pandas.DataFrame(collections.OrderedDict(sorted(data.items()))).T
    df = df.convert_objects(convert_numeric=True)
    return df


################################################
# VersionStore: Storing and updating stock data
################################################



arctic = Arctic('localhost')

# Create a VersionStore library
arctic.delete_library('jblackburn.stocks')
arctic.initialize_library('jblackburn.stocks')
arctic.list_libraries()


stocks = arctic['jblackburn.stocks']

# get some prices
aapl = get_stock_history('aapl', '2015-01-01', '2015-02-01')
aapl

# store them in the library
stocks.write('aapl', aapl, metadata={'source': 'YAHOO'})
stocks.read('aapl').data['Adj Close'].plot()
stocks.read('aapl').metadata
stocks.read('aapl').version


# Append some more prices - imagine doing this once per period
aapl = get_stock_history('aapl', '2015-02-01', '2015-03-01')
stocks.append('aapl', aapl)
stocks.read('aapl').data


# Reading different versions of the symbol
stocks.list_symbols()
stocks.list_versions('aapl')

# Read the different versions separately
stocks.read('aapl', as_of=1).data.ix[-1]
stocks.read('aapl', as_of=2).data.ix[-1]


# And we can snapshot all items in the library
stocks.snapshot('snap')
stocks.read('aapl', as_of='snap').data.ix[-1]



#################################
# Dealing with lots of data
#################################


#NSYE library
lib = arctic['nyse']

def load_all_stock_history_NYSE():
    # Data downloaded from BBG Open Symbology:
    # 
    nyse = pd.read_csv('/users/is/jblackburn/git/arctic/howtos/nyse.csv')
    stocks = [x.split('/')[0] for x in nyse['Ticker']]
    print(len(stocks), " symbols")
    for i, stock in enumerate(stocks):
        try:
            now = datetime.now()
            data = get_stock_history('aapl', '1980-01-01', '2015-07-07')
            lib.write(stock, data)
            print("loaded data for: ", stock, datetime.now() - now)
        except Exception as e:
            print("Failed for ", stock, str(e))


# load_all_stock_history_NYSE()
print(len(lib.list_symbols()), " NYSE symbols loaded")


def read_all_data_from_lib(lib):
    start = time.time()
    rows_read = 0
    for s in lib.list_symbols():
        rows_read += len(lib.read(s).data)
    print("Symbols: %s Rows: %s  Time: %s  Rows/s: %s" % (len(lib.list_symbols()),
                                                          rows_read,
                                                          (time.time() - start),
                                                          rows_read / (time.time() - start)))


read_all_data_from_lib(lib)
# Symbols: 1315 Rows: 11460225   Rows/s: 2,209,909
