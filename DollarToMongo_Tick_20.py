'''
 @author: Amol Kapoor
 @date: 6-1-15
 @version: 1.0

 Description: Program designed to grab tweet data from tweets2 database in mysql and convert it to lz4 compressed JSON data stored
 in Mongo

 Note: missed _dollar_inqd.csv because added after the fact
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
     and passes to tweetlibrary to store to mongo

     @param: path; type: string; the filepath of the sentiment data being read
     @param: subject; type: string; the ticker for the sentiment data
     @param: version; type: string; the version num of the NLP 
     @param: collection; type: mongo collection; where to store the data
     '''

     df = pd.read_csv(path, engine='c', index_col = 0, parse_dates = True)
     df.index = df.index.tz_localize('UTC')

     return df


def main():

     version = "ts_20"
     path = "/var/data/sentiments/" + version
     fileList = os.listdir(path)

     #setup mongo connection
     store = Arctic('10.13.0.38')

     library_name = version + "_ticks"

     store.delete_library(library_name)

     # Create a library
     store.initialize_library(library_name, arctic.TICK_STORE)

     library = store[library_name]

     start_time = time.time()

     for fname in fileList:
          if 'dollar' not in fname:
               continue

          back = len(".csv")*-1
          subject = fname[:back]
          subject = subject.replace('.', '_dot_')

          print subject

          post = getSentimentData(path + '/' + fname)
          arctic_wrapper.write(post, subject, library)

     print time.time() - start_time

main()
