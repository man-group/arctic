import logging

from bson.binary import Binary
from datetime import datetime as dt, timedelta
import lz4
import numpy as np
import pandas as pd
from pandas.core.frame import _arrays_to_mgr
import pymongo
from pymongo.errors import OperationFailure

from ..date import DateRange, to_pandas_closed_closed, mktz, datetime_to_ms, CLOSED_CLOSED, to_dt
from ..decorators import mongo_retry
from ..exceptions import OverlappingDataException, NoDataFoundException, UnhandledDtypeException, ArcticException

logger = logging.getLogger(__name__)

# Example-Schema:
# --------------
# {ID: ObjectId('52b1d39eed5066ab5e87a56d'),
#  SYMBOL: u'symbol'
#  INDEX: Binary('...', 0),
#  IMAGE_DOC: { IMAGE:  {
#                          'ASK': 10.
#                          ...
#                        }
#              's': <sequence_no>
#              't': DateTime(...)
#             }
#  COLUMNS: {
#   'ACT_FLAG1': {
#        DATA: Binary('...', 0),
#        DTYPE: u'U1',
#        ROWMASK: Binary('...', 0)},
#   'ACVOL_1': {
#        DATA: Binary('...', 0),
#        DTYPE: u'float64',
#        ROWMASK: Binary('...', 0)},
#               ...
#    }
#  START: DateTime(...),
#  END: DateTime(...),
#  END_SEQ: 31553879L,
#  SEGMENT: 1386933906826L,
#  SHA: 1386933906826L,
#  VERSION: 3,
# }

TICK_STORE_TYPE = 'TickStoreV3'

ID = '_id'
SYMBOL = 'sy'
INDEX = 'i'
START = 's'
END = 'e'
START_SEQ = 'sS'
END_SEQ = 'eS'
SEGMENT = 'se'
SHA = 'sh'
IMAGE_DOC = 'im'
IMAGE = 'i'

COLUMNS = 'cs'
DATA = 'd'
DTYPE = 't'
ROWMASK = 'm'

COUNT = 'c'
VERSION = 'v'

CHUNK_VERSION_NUMBER = 3


class TickStore(object):

    chunk_size = 100000

    @classmethod
    def initialize_library(cls, arctic_lib, **kwargs):
        TickStore(arctic_lib)._ensure_index()

    @mongo_retry
    def _ensure_index(self):
        collection = self._collection
        collection.create_index([(SYMBOL, pymongo.ASCENDING),
                                 (START, pymongo.ASCENDING)], background=True)
        collection.create_index([(START, pymongo.ASCENDING)], background=True)

    def __init__(self, arctic_lib):
        self._arctic_lib = arctic_lib

        # Do we allow reading from secondaries
        self._allow_secondary = self._arctic_lib.arctic._allow_secondary

        # The default collections
        self._collection = arctic_lib.get_top_level_collection()

    def __getstate__(self):
        return {'arctic_lib': self._arctic_lib}

    def __setstate__(self, state):
        return TickStore.__init__(self, state['arctic_lib'])

    def __str__(self):
        return """<%s at %s>
%s""" % (self.__class__.__name__, hex(id(self)), indent(str(self._arctic_lib), 4))

    def __repr__(self):
        return str(self)

    def delete(self, symbol, date_range=None):
        """
        Delete all chunks for a symbol.

        Which are, for the moment, fully contained in the passed in
        date_range.

        Parameters
        ----------
        symbol : `str`
            symbol name for the item
        date_range : `date.DateRange`
            DateRange to delete ticks in
        """
        query = {SYMBOL: symbol}
        date_range = to_pandas_closed_closed(date_range)
        if date_range is not None:
            assert date_range.start and date_range.end
            query[START] = {'$gte': date_range.start}
            query[END] = {'$lte': date_range.end}
        self._collection.delete_many(query)

    def list_symbols(self, date_range=None):
        return self._collection.distinct(SYMBOL)

    def _mongo_date_range_query(self, symbol, date_range):
        # Handle date_range
        if not date_range:
            date_range = DateRange()

        # We're assuming CLOSED_CLOSED on these Mongo queries
        assert date_range.interval == CLOSED_CLOSED

        # Find the start bound
        start_range = {}
        first = last = None
        if date_range.start:
            assert date_range.start.tzinfo
            start = date_range.start
            startq = self._symbol_query(symbol)
            startq.update({START: {'$lte': start}})
            first = self._collection.find_one(startq,
                                              # Service entirely from the index
                                              projection={START: 1, ID: 0},
                                              sort=[(START, pymongo.DESCENDING)])
        if first:
            start_range['$gte'] = first[START]

        # Find the end bound
        if date_range.end:
            assert date_range.end.tzinfo
            end = date_range.end
            endq = self._symbol_query(symbol)
            endq.update({START: {'$gt': end}})
            last = self._collection.find_one(endq,
                                              # Service entirely from the index
                                              projection={START: 1, ID: 0},
                                              sort=[(START, pymongo.ASCENDING)])
        else:
            logger.info("No end provided.  Loading a month for: {}:{}".format(symbol, first))
            if not first:
                first = self._collection.find_one(self._symbol_query(symbol),
                                                  projection={START: 1, ID: 0},
                                                  sort=[(START, pymongo.ASCENDING)])
                if not first:
                    raise NoDataFoundException()
            last = first[START]
            last = {START: last + timedelta(days=30)}
        if last:
            start_range['$lt'] = last[START]

        # Return chunks in the specified range
        if not start_range:
            return {}
        return {START: start_range}

    def _symbol_query(self, symbol):
        if isinstance(symbol, basestring):
            query = {SYMBOL: symbol}
        elif symbol is not None:
            query = {SYMBOL: {'$in': symbol}}
        else:
            query = {}
        return query

    def read(self, symbol, date_range=None, columns=None, include_images=False, _target_tick_count=0):
        """
        Read data for the named symbol.  Returns a VersionedItem object with
        a data and metdata element (as passed into write).

        Parameters
        ----------
        symbol : `str`
            symbol name for the item
        date_range : `date.DateRange`
            Returns ticks in the specified DateRange
        columns : `list` of `str`
            Columns (fields) to return from the tickstore
        include_images : `bool`
            Should images (/snapshots) be included in the read
        Returns
        -------
        pandas.DataFrame of data
        """
        perf_start = dt.now()
        rtn = {}
        column_set = set()

        multiple_symbols = not isinstance(symbol, basestring)

        date_range = to_pandas_closed_closed(date_range)
        query = self._symbol_query(symbol)
        query.update(self._mongo_date_range_query(symbol, date_range))

        if columns:
            projection = dict([(SYMBOL, 1),
                           (INDEX, 1),
                           (START, 1),
                           (VERSION, 1),
                           (IMAGE_DOC, 1)] +
                          [(COLUMNS + '.%s' % c, 1) for c in columns])
            column_set.update([c for c in columns if c != 'SYMBOL'])
        else:
            projection = dict([(SYMBOL, 1),
                           (INDEX, 1),
                           (START, 1),
                           (VERSION, 1),
                           (COLUMNS, 1),
                           (IMAGE_DOC, 1)])

        column_dtypes = {}
        ticks_read = 0
        for b in self._collection.find(query, projection=projection).sort([(START, pymongo.ASCENDING)],):
            data = self._read_bucket(b, column_set, column_dtypes,
                                     multiple_symbols or (columns is not None and 'SYMBOL' in columns),
                                     include_images, columns)
            for k, v in data.iteritems():
                try:
                    rtn[k].append(v)
                except KeyError:
                    rtn[k] = [v]
            # For testing
            ticks_read += len(data[INDEX])
            if _target_tick_count and ticks_read > _target_tick_count:
                break

        if not rtn:
            raise NoDataFoundException("No Data found for {} in range: {}".format(symbol, date_range))
        rtn = self._pad_and_fix_dtypes(rtn, column_dtypes)

        index = pd.to_datetime(np.concatenate(rtn[INDEX]), utc=True, unit='ms')
        if columns is None:
            columns = [x for x in rtn.keys() if x not in (INDEX, 'SYMBOL')]
        if multiple_symbols and 'SYMBOL' not in columns:
            columns = ['SYMBOL', ] + columns

        if len(index) > 0:
            arrays = [np.concatenate(rtn[k]) for k in columns]
        else:
            arrays = [[] for k in columns]

        if multiple_symbols:
            sort = np.argsort(index)
            index = index[sort]
            arrays = [a[sort] for a in arrays]

        t = (dt.now() - perf_start).total_seconds()
        logger.info("Got data in %s secs, creating DataFrame..." % t)
        mgr = _arrays_to_mgr(arrays, columns, index, columns, dtype=None)
        rtn = pd.DataFrame(mgr)
        # Present data in the user's default TimeZone
        rtn.index.tz = mktz()

        t = (dt.now() - perf_start).total_seconds()
        ticks = len(rtn)
        logger.info("%d rows in %s secs: %s ticks/sec" % (ticks, t, int(ticks / t)))
        if not rtn.index.is_monotonic:
            logger.error("TimeSeries data is out of order, sorting!")
            rtn = rtn.sort_index()
        if date_range:
            # FIXME: support DateRange.interval...
            rtn = rtn.ix[date_range.start:date_range.end]
        return rtn

    def _pad_and_fix_dtypes(self, cols, column_dtypes):
        # Pad out Nones with empty arrays of appropriate dtypes
        rtn = {}
        index = cols[INDEX]
        full_length = len(index)
        for k, v in cols.iteritems():
            if k != INDEX and k != 'SYMBOL':
                col_len = len(v)
                if col_len < full_length:
                    v = ([None, ] * (full_length - col_len)) + v
                    assert len(v) == full_length
                for i, arr in enumerate(v):
                    if arr is None:
                        #  Replace Nones with appropriate-length empty arrays
                        v[i] = self._empty(len(index[i]), column_dtypes.get(k))
                    else:
                        # Promote to appropriate dtype only if we can safely cast all the values
                        # This avoids the case with strings where None is cast as 'None'.
                        # Casting the object to a string is not worthwhile anyway as Pandas changes the
                        # dtype back to objectS
                        if (i == 0 or v[i].dtype != v[i - 1].dtype) and np.can_cast(v[i].dtype, column_dtypes[k],
                                                                                    casting='safe'):
                            v[i] = v[i].astype(column_dtypes[k], casting='safe')

            rtn[k] = v
        return rtn

    def _set_or_promote_dtype(self, column_dtypes, c, dtype):
        existing_dtype = column_dtypes.get(c)
        if existing_dtype is None or existing_dtype != dtype:
            # Promote ints to floats - as we can't easily represent NaNs
            if np.issubdtype(dtype, int):
                dtype = np.dtype('f8')
            column_dtypes[c] = np.promote_types(column_dtypes.get(c, dtype), dtype)

    def _prepend_image(self, document, im, rtn_length, column_dtypes, column_set, columns):
        image = im[IMAGE]
        first_dt = im['t']
        if not first_dt.tzinfo:
            first_dt = first_dt.replace(tzinfo=mktz('UTC'))
        document[INDEX] = np.insert(document[INDEX], 0, np.uint64(datetime_to_ms(first_dt)))
        for field in image:
            if field == INDEX:
                continue
            if columns and field not in columns:
                continue
            if field not in document or document[field] is None:
                col_dtype = np.dtype(str if isinstance(image[field], basestring) else 'f8')
                document[field] = self._empty(rtn_length, dtype=col_dtype)
                column_dtypes[field] = col_dtype
                column_set.add(field)
            val = image[field]
            document[field] = np.insert(document[field], 0, document[field].dtype.type(val))
        # Now insert rows for fields in document that are not in the image
        for field in set(document).difference(set(image)):
            if field == INDEX:
                continue
            logger.debug("Field %s is missing from image!", field)
            if document[field] is not None:
                val = np.nan
                document[field] = np.insert(document[field], 0, document[field].dtype.type(val))
        return document

    def _read_bucket(self, doc, column_set, column_dtypes, include_symbol, include_images, columns):
        rtn = {}
        if doc[VERSION] != 3:
            raise ArcticException("Unhandled document version: %s" % doc[VERSION])
        rtn[INDEX] = np.cumsum(np.fromstring(lz4.decompress(doc[INDEX]), dtype='uint64'))
        doc_length = len(rtn[INDEX])
        rtn_length = len(rtn[INDEX])
        if include_symbol:
            rtn['SYMBOL'] = [doc[SYMBOL], ] * rtn_length
        column_set.update(doc[COLUMNS].keys())
        for c in column_set:
            try:
                coldata = doc[COLUMNS][c]
                dtype = np.dtype(coldata[DTYPE])
                values = np.fromstring(lz4.decompress(str(coldata[DATA])), dtype=dtype)
                self._set_or_promote_dtype(column_dtypes, c, dtype)
                rtn[c] = self._empty(rtn_length, dtype=column_dtypes[c])
                rowmask = np.unpackbits(np.fromstring(lz4.decompress(str(coldata[ROWMASK])),
                                                      dtype='uint8'))[:doc_length].astype('bool')
                rtn[c][rowmask] = values
            except KeyError:
                rtn[c] = None

        if include_images and doc.get(IMAGE_DOC, {}).get(IMAGE, {}):
            rtn = self._prepend_image(rtn, doc[IMAGE_DOC], rtn_length, column_dtypes, column_set, columns)
        return rtn

    def _empty(self, length, dtype):
        if dtype is not None and dtype == np.float64:
            rtn = np.empty(length, dtype)
            rtn[:] = np.nan
            return rtn
        else:
            return np.empty(length, dtype=np.object_)

    def stats(self):
        """
        Return storage statistics about the library

        Returns
        -------
        dictionary of storage stats
        """
        res = {}
        db = self._collection.database
        conn = db.connection
        res['sharding'] = {}
        try:
            sharding = conn.config.databases.find_one({'_id': db.name})
            if sharding:
                res['sharding'].update(sharding)
            res['sharding']['collections'] = list(conn.config.collections.find(
                                                  {'_id': {'$regex': '^' + db.name + "\..*"}}))
        except OperationFailure:
            # Access denied
            pass
        res['dbstats'] = db.command('dbstats')
        res['chunks'] = db.command('collstats', self._collection.name)
        res['totals'] = {'count': res['chunks']['count'],
                         'size': res['chunks']['size'],
                         }
        return res

    def _assert_nonoverlapping_data(self, symbol, start, end):
        #
        # Imagine we're trying to insert a tick bucket like:
        #      |S------ New-B -------------- E|
        #  |---- 1 ----| |----- 2 -----| |----- 3 -----|
        #
        # S = New-B Start
        # E = New-B End
        # New-B overlaps with existing buckets 1,2,3
        #
        # All we need to do is find the bucket who's start is immediately before (E)
        # If that document's end is > S, then we know it overlaps
        # with this bucket.
        doc = self._collection.find_one({SYMBOL: symbol,
                                         START: {'$lt': end}
                                         },
                                        projection={START: 1,
                                                END: 1,
                                                '_id': 0},
                                        sort=[(START, pymongo.DESCENDING)])
        if doc:
            if not doc[END].tzinfo:
                doc[END] = doc[END].replace(tzinfo=mktz('UTC'))
            if doc[END] > start:
                raise OverlappingDataException("Document already exists with start:{} end:{} in the range of our start:{} end:{}".format(
                                                            doc[START], doc[END], start, end))

    def write(self, symbol, data):
        """
        Writes a list of market data events.

        Parameters
        ----------
        symbol : `str`
            symbol name for the item
        data : list of dicts
            List of ticks to store to the tick-store.
        """
        pandas = False
        # Check for overlapping data
        if isinstance(data, list):
            start = data[0]['index']
            end = data[-1]['index']
        elif isinstance(data, pd.DataFrame):
            start = data.index[0].to_datetime()
            end = data.index[-1].to_datetime()
            pandas = True
        else:
            raise UnhandledDtypeException("Can't persist type %s to tickstore" % type(data))
        self._assert_nonoverlapping_data(symbol, to_dt(start), to_dt(end))

        if pandas:
            buckets = self._pandas_to_buckets(data, symbol)
        else:
            buckets = self._to_buckets(data, symbol)
        self._write(buckets)

    def _write(self, buckets):
        start = dt.now()
        mongo_retry(self._collection.insert_many)(buckets)
        t = (dt.now() - start).total_seconds()
        ticks = len(buckets) * self.chunk_size
        print "%d buckets in %s: approx %s ticks/sec" % (len(buckets), t, int(ticks / t))

    def _pandas_to_buckets(self, x, symbol):
        rtn = []
        for i in range(0, len(x), self.chunk_size):
            rtn.append(self._pandas_to_bucket(x[i:i + self.chunk_size], symbol))
        return rtn

    def _to_buckets(self, x, symbol):
        rtn = []
        for i in range(0, len(x), self.chunk_size):
            rtn.append(self._to_bucket(x[i:i + self.chunk_size], symbol))
        return rtn

    def _to_ms(self, date):
        if isinstance(date, dt):
            if not date.tzinfo:
                logger.warn('WARNING: treating naive datetime as London in write path')
            return datetime_to_ms(date)
        return date

    def _str_dtype(self, dtype):
        """
        Represent dtypes without byte order, as earlier Java tickstore code doesn't support explicit byte order.
        """
        assert dtype.byteorder != '>'
        if (dtype.kind) == 'i':
            assert dtype.itemsize == 8
            return 'int64'
        elif (dtype.kind) == 'f':
            assert dtype.itemsize == 8
            return 'float64'
        elif (dtype.kind) == 'U':
            return 'U%d' % (dtype.itemsize / 4)
        else:
            raise UnhandledDtypeException("Bad dtype '%s'" % dtype)


    def _ensure_supported_dtypes(self, array):
        # We only support these types for now, as we need to read them in Java
        if (array.dtype.kind) == 'i':
            array = array.astype('<i8')
        elif (array.dtype.kind) == 'f':
            array = array.astype('<f8')
        elif (array.dtype.kind) in ('U', 'S'):
            array = array.astype(np.unicode_)
        else:
            raise UnhandledDtypeException("Unsupported dtype '%s' - only int64, float64 and U are supported" % array.dtype)
        # Everything is little endian in tickstore
        if array.dtype.byteorder != '<':
            array = array.astype(array.dtype.newbyteorder('<'))
        return array

    def _pandas_to_bucket(self, df, symbol):
        start = to_dt(df.index[0].to_datetime())
        end = to_dt(df.index[0].to_datetime())
        rtn = {START: start, END: end, SYMBOL: symbol}
        rtn[VERSION] = CHUNK_VERSION_NUMBER
        rtn[COUNT] = len(df)
        rtn[COLUMNS] = {}

        logger.warn("NB treating all values as 'exists' - no longer sparse")
        rowmask = Binary(lz4.compressHC(np.packbits(np.ones(len(df), dtype='uint8'))))

        recs = df.to_records(convert_datetime64=False)
        for col in df:
            array = self._ensure_supported_dtypes(recs[col])
            col_data = {}
            col_data[DATA] = Binary(lz4.compressHC(array.tostring()))
            col_data[ROWMASK] = rowmask
            col_data[DTYPE] = self._str_dtype(array.dtype)
            rtn[COLUMNS][col] = col_data
        rtn[INDEX] = Binary(lz4.compressHC(np.concatenate(([recs['index'][0].astype('datetime64[ms]').view('uint64')],
                                                           np.diff(recs['index'].astype('datetime64[ms]').view('uint64')))
                                                          ).tostring()))
        return rtn

    def _to_bucket(self, ticks, symbol):
        data = {}
        rowmask = {}
        start = to_dt(ticks[0]['index'])
        end = to_dt(ticks[-1]['index'])
        for i, t in enumerate(ticks):
            for k, v in t.iteritems():
                try:
                    if k != 'index':
                        rowmask[k][i] = 1
                    else:
                        v = self._to_ms(v)
                    data[k].append(v)
                except KeyError:
                    if k != 'index':
                        rowmask[k] = np.zeros(len(ticks), dtype='uint8')
                        rowmask[k][i] = 1
                    data[k] = [v]

        rowmask = dict([(k, Binary(lz4.compressHC(np.packbits(v).tostring())))
                        for k, v in rowmask.iteritems()])

        rtn = {START: start, END: end, SYMBOL: symbol}
        rtn[VERSION] = CHUNK_VERSION_NUMBER
        rtn[COUNT] = len(ticks)
        rtn[COLUMNS] = {}
        for k, v in data.iteritems():
            if k != 'index':
                v = np.array(v)
                v = self._ensure_supported_dtypes(v)
                rtn[COLUMNS][k] = {DATA: Binary(lz4.compressHC(v.tostring())),
                                   DTYPE: self._str_dtype(v.dtype),
                                   ROWMASK: rowmask[k]}

        rtn[INDEX] = Binary(lz4.compressHC(np.concatenate(([data['index'][0]], np.diff(data['index']))).tostring()))
        return rtn

    def max_date(self, symbol):
        """
        Return the maximum datetime stored for a particular symbol

        Parameters
        ----------
        symbol : `str`
            symbol name for the item
        """
        res = self._collection.find_one({SYMBOL: symbol}, projection={ID: 0, END: 1},
                                        sort=[(START, pymongo.DESCENDING)])
        return res[END]
