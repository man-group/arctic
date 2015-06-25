'''
@author: Amol Kapoor
@date: 6-22-15
@version: 0.1


Description: Program designed to grab all price  data and store to mongo. Note that this deletes the original library;
meant for a full update
'''
import time

import pandas as pd
import numpy as np

from arctic import Arctic
import arctic

import arctic_wrapper

import pytz

import datetime

import os

def getPriceData(path):
     '''
     Gets the sentiment data, stores it in a pandas dataframe, converts the dataframe to an object with each column as a list (chunked by day)
     and passes to arctic to store to mongo

     @param: path; type: string; the filepath of the sentiment data being read
     '''

     df = pd.read_csv(path, engine='c', header=None, index_col = 0, names=['date', 'time', 'open', 'high', 'low', 'close', 'cvol', 'vol'], parse_dates = [['date', 'time']])

     return df



def main():

     path = "/var/data/prices/"
     fileList = os.listdir(path)

     #setup mongo connection
     store = Arctic('10.13.0.38')

     library_name = "prices_ticks"

     store.delete_library(library_name)

     # Create a library
     store.initialize_library(library_name, arctic.TICK_STORE)

     library = store[library_name]

     start_time = time.time()
     
     for fname in fileList:
          back = len(".csv")*-1
          subject = fname[:back]
          subject = subject.replace('.', '_dot_')

          print subject

          post = getPriceData(path + fname)

          if len(post) > 0:
               arctic_wrapper.write(post, subject, library)

     print 'Upload:'
     print time.time() - start_time

main()
