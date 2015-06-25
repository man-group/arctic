'''
@author: Amol Kapoor
@date: 6-25-15
@version: 0.1

Description: A arctic_wrapper driver that stores all new data from sentiments/prices (files) and writes them to mongo
'''

import time

import pandas as pd

import os

from arctic import Arctic
import arctic

import arctic_wrapper

def getSentimentData(path):
     '''
     Gets the sentiment data, stores it in a pandas dataframe, converts the dataframe to an object with each column as a list (chunked by day)
     and passes to arctic to store to mongo

     @param: path; type: string; the filepath of the sentiment data being read
     '''

     df = pd.read_csv(path, engine='c', index_col = 0, parse_dates = True)
     df.index = df.index.tz_localize('UTC')

     return df




def getPriceData(path):
     '''
     Gets the sentiment data, stores it in a pandas dataframe, converts the dataframe to an object with each column as a list (chunked by day)
     and passes to arctic to store to mongo

     @param: path; type: string; the filepath of the sentiment data being read
     '''

     df = pd.read_csv(path, engine='c', header=None, index_col = 0, names=['date', 'time', 'open', 'high', 'low', 'close', 'cvol', 'vol'], parse_dates = [['date', 'time']])

     return df




def main():
     #setup mongo connection
     store = Arctic('10.13.0.38')

     version = "ts_20"
     path = "/var/data/sentiments/" + version
     fileList = os.listdir(path)

     library_name = version + "_ticks"

     store.initialize_library(library_name, arctic.TICK_STORE)

     library = store[library_name]

     print "Starting ts_20"
     start_time = time.time()

     for fname in fileList:
          if 'dollar' not in fname:
               continue

          back = len(".csv")*-1
          subject = fname[:back]
          subject = subject.replace('.', '_dot_')

          print subject

          post = getSentimentData(path + '/' + fname)

          max_date = library.max_date(subject)

          if max_date:
               post = post[post.index > max_date]
               if len(post) > 0:
                    print 'hi'
                    #arctic_wrapper.append(post, subject, library)
          else:
               if len(post) > 0:
                    print 'stuff'
                    #arctic_wrapper.write(post, subject, library)

     print "Ending ts_20"
     print time.time() - start_time
     start_time = time.time()



     #----------------------------------------------------------
     
     version = "ts_28"
     path = "/var/data/sentiments/" + version
     fileList = os.listdir(path)

     library_name = version + "_ticks"

     store.initialize_library(library_name, arctic.TICK_STORE)

     library = store[library_name]

     print "Starting ts_28"
     start_time = time.time()

     for fname in fileList:
          if 'dollar' not in fname:
               continue

          back = len(".csv")*-1
          subject = fname[:back]
          subject = subject.replace('.', '_dot_')

          print subject

          post = getSentimentData(path + '/' + fname)

          max_date = library.max_date(subject)

          if max_date:
               post = post[post.index > max_date]
               if len(post) > 0:
                    print 'hi'
                    #arctic_wrapper.append(post, subject, library)
          else:
               if len(post) > 0:
                    print 'stuff'
                    #arctic_wrapper.write(post, subject, library)

     print "Ending ts_28"
     print time.time() - start_time
     start_time = time.time()

     #---------------------------------------------------

     path = "/var/data/prices/"
     fileList = os.listdir(path)

     library_name = "prices_ticks"

     # Create a library
     store.initialize_library(library_name, arctic.TICK_STORE)

     library = store[library_name]

     start_time = time.time()

     print "Starting price data"
     
     for fname in fileList:
          back = len(".csv")*-1
          subject = fname[:back]
          subject = subject.replace('.', '_dot_')

          print subject

          post = getPriceData(path + fname)

          max_date = library.max_date(subject)

          if max_date:
               post = post[post.index > max_date]
               if len(post) > 0:
                    print 'hi'
                    #arctic_wrapper.append(post, subject, library)
          else:
               if len(post) > 0:
                    print 'stuff'
                    #arctic_wrapper.write(post, subject, library)

     print 'Ending price data:'
     print time.time() - start_time



main()
