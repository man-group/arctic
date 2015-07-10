'''
@author: Amol Kapoor
@date: 6-22-15
@version: 0.1

Wrapper over the arctic tick_store library to provide a few additional functions in addition to what arctic can already do
'''

from arctic import Arctic
from arctic.tickstore.tickstore import TickStore
from arctic.date import DateRange
import arctic

import datetime
import dateutil

import pytz
import tzlocal

import pandas as pd

import time

def addTZ(date):
     '''
     Adds the local timezone to a datetime request if there is no datetime

     @param: date; datetime; the datetime to convert 

     @return: datetime object with timezone or None if datetime not passed
     '''
     if date and not date.tzinfo:
          date = date.replace(tzinfo = tzlocal.get_localzone())
     return date

#--------------------------------------------------------------------------------------------------------

def append(df, subject, library):
     '''
     Gets the latest bucket, pulls it down, uncompresses it, reads it, appends new data, and rewrites it

     @param: df; pandas dataframe; the new data that will be added to the latest bucket
     @param: subject; string; the subject to change
     @param: library; Arctic lib; where to make changes
     '''
     df.index.names = ['index']

     if df.index[0].tzinfo is None:
          df.index = df.index.tz_localize(tzlocal.get_localzone())
    
     df.index = df.index.tz_convert(pytz.utc)

     bucket_data = library.read_latest(subject)

     bucket_data.index = bucket_data.index.tz_localize(pytz.utc)

     last_date = bucket_data.index[len(bucket_data) - 1]

     if last_date > df.index[0]:
          print('Newly appended data cannot have datetime before last update: {} before {}. Appending new data only.'.format(df.index[0], last_date))
          df = df[df.index > last_date]
          if len(df) == 0:
              return
     
     for col in df:
         library._ensure_supported_dtypes(df[col])

     daterange = arctic.date.DateRange(bucket_data.index[0], df.index[0])

     bucket_data = bucket_data.append(df)

     library.write_replace(subject, bucket_data)

def write(df, subject, library):
     '''
     Takes in a pandas dataframe representing tick data, converts the timezones to timezone aware (Eastern), 
     and uploads to arctic under a given subject

     Assumes incoming datetimes without tzinfos are in local time, and converts them accordingly

     Assumes that the format of the first index is the same as the format for the rest of the indices (with regards to tzinfo)

     Arctic auto-stores in UTC

     @param: df; pandas dataframe; tick-data to store to arctic. Index must be type datetime. 
     @param: subject; string; what to call the data
     @param: library; where to store it
     '''
     if isinstance(type(df.index), pd.DatetimeIndex):
          raise ValueError('Dataframe Index is not of type datetime')

     #make sure the dataframe is compatabile with arctic
     df.index.names = ['index']

     #Assume that if the first date does not have tzinfo, the rest don't too (and vice versa)
     #returns errors on dst - look into this
     if df.index[0].tzinfo is None:
          df.index = df.index.tz_localize(tzlocal.get_localzone())

     df.index = df.index.tz_convert(pytz.utc)

     library.write(subject, df)

def read(subject, library, startdate=None, enddate=None, fields=None):
     '''
     Searches for data requested by params. Returns data as a pandas dataframe, with datetimes as localzone

     With no datetimes provided, will return first 100000 results. With startdate only, will provide 100000 results from 
     the starttdate. With enddate, will provide everything up to enddate. 

     @param: startdate; datetime; start date to query
     @param: enddate; datetime; end date to query
     @param: subject; string; what data to query
     @param: fields; [str]; fields to return
     @param: library; where to store it

     @return: data of 'subject' from 'daterange' with timezones converted to local
     '''
     
     startdate = addTZ(startdate)
     enddate = addTZ(enddate)

     date_range = DateRange(startdate, enddate)

     df = library.read(subject, date_range, fields)

     df.index = df.index.tz_localize(pytz.utc).tz_convert(tzlocal.get_localzone())

     return df
