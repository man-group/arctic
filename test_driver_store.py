'''
@author: Amol Kapoor
@date: 6-22-15
@version: 0.1

Test driver for arctic wrapper.py storage functions
'''
import time

import pandas as pd
import numpy as np

from arctic import Arctic
import arctic

import arctic_wrapper

import pytz

import datetime

def getSentimentData(path):
     '''
     Gets the sentiment data, stores it in a pandas dataframe, converts the dataframe to an object with each column as a list (chunked by day)
     and passes to tweetlibrary to store to mongo

     @param: path; type: string; the filepath of the sentiment data being read
     @param: subject; type: string; the ticker for the sentiment data
     @param: version; type: string; the version num of the NLP 
     @param: collection; type: mongo collection; where to store the data
     '''

     df = pd.read_csv(path, engine='c', index_col = 0, parse_dates = True)

     return df


def getPriceData(path):
     '''
     Gets the sentiment data, stores it in a pandas dataframe, converts the dataframe to an object with each column as a list (chunked by day)
     and passes to tweetlibrary to store to mongo

     @param: path; type: string; the filepath of the sentiment data being read
     @param: subject; type: string; the ticker for the sentiment data
     @param: version; type: string; the version num of the NLP 
     @param: collection; type: mongo collection; where to store the data
     '''

     df = pd.read_csv(path, engine='c', header=None, index_col = 0, names=['date', 'time', 'open', 'high', 'low', 'close', 'cvol', 'vol'], parse_dates = [['date', 'time']])
     
     return df



def main():
#     pd.options.display.max_rows = 10000000

     path = "/var/data/prices/"

     #setup mongo connection
     store = Arctic('10.13.0.38')

     library_name = "test_lib_ticks"

     store.delete_library(library_name)

     # Create a library
     store.initialize_library(library_name, arctic.TICK_STORE)

     library = store[library_name]

     start_time = time.time()
     
     #post = getSentimentData(path + '/_dollar_spy.csv')

     post = getPriceData(path + '/SPY.csv')

     #print post

     subject = 'spy_data'

     print 'get data:'
     print time.time() - start_time
     start_time = time.time()

     arctic_wrapper.write(post, subject, library)

     print 'Upload:'
     print time.time() - start_time
     start_time = time.time()

     print "|"
     print "|"
     print "|"

     start = None
     end = datetime.datetime(2015, 8, 30)
     data = arctic_wrapper.read(subject=subject, library=library, startdate = start, enddate = end)
     print len(data)
     print 'Download All:'
     print time.time() - start_time
     start_time = time.time()

     print "|"
     print "|"
     print "|"


     start = datetime.datetime(2013, 1, 2)
     end = datetime.datetime(2013, 1, 3)

     data = arctic_wrapper.read(subject=subject, library=library, startdate=start, enddate=end)
     print len(data)
     print 'Download One Day:'
     print time.time() - start_time
     start_time = time.time()
     
     print "|"
     print "|"
     print "|"

     data = arctic_wrapper.read(subject=subject,library=library, fields=[])
     print len(data)
     print 'Download No Fields:'
     print time.time() - start_time
     start_time = time.time()

     print "|"
     print "|"
     print "|" 

     daterange = pd.date_range('6/25/15', periods=100, freq='H')
     ts = pd.DataFrame({'open': np.random.randn(len(daterange)), 
                        'high': np.random.randn(len(daterange)),
                        'low': np.random.randn(len(daterange)),
                        'close': np.random.randn(len(daterange)), 
                        'cvol': np.random.randn(len(daterange)),
                        'vol': np.random.randn(len(daterange))}, index = daterange)

     #open high low close cvol vol
     ts.index = ts.index.to_datetime()

     arctic_wrapper.append(ts, subject, library)

     print 'Append 100:'
     print time.time() - start_time
     start_time = time.time()

     print "|"
     print "|"
     print "|"
     
     start = None
     end = datetime.datetime(2016, 1, 1)

     data = arctic_wrapper.read(subject=subject, library=library, startdate = start, enddate = end)
     
     print len(data)
     print 'Download All:'
     print time.time() - start_time
     start_time = time.time()

     print "|"
     print "|"
     print "|"

main()
