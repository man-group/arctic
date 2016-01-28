import logging
import bisect
from collections import namedtuple
from datetime import datetime as dt, date, time, timedelta
import re
from timeit import itertools

import pandas as pd
import pymongo

from ..date import mktz, DateRange, OPEN_OPEN, CLOSED_CLOSED
from ..exceptions import (NoDataFoundException, UnhandledDtypeException, OverlappingDataException,
                          LibraryNotFoundException)

logger = logging.getLogger(__name__)

TickStoreLibrary = namedtuple("TickStoreLibrary", ["library", "date_range"])

TICK_STORE_TYPE = 'TopLevelTickStore'

PATTERN = "^%s_\d{4}.%s"
YEAR_REGEX = re.compile("\d{4}")

end_time_min = (dt.combine(date.today(), time.min) - timedelta(milliseconds=1)).time()


class DictList(object):
    def __init__(self, lst, key):
        self.lst = lst
        self.key = key

    def __len__(self):
        return len(self.lst)

    def __getitem__(self, idx):
        return self.lst[idx][self.key]


class TopLevelTickStore(object):

    @classmethod
    def initialize_library(cls, arctic_lib, **kwargs):
        tl = TopLevelTickStore(arctic_lib)
        tl._add_libraries()
        tl._ensure_index()

    def _ensure_index(self):
        collection = self._collection
        collection.create_index([('start', pymongo.ASCENDING)], background=True)

    def _add_libraries(self):
        name = self.get_name()
        db_name, tick_type = name.split('.', 1)
        regex = re.compile(PATTERN % (db_name, tick_type))
        libraries = [lib for lib in self._arctic_lib.arctic.list_libraries() if regex.search(lib)]
        for lib in libraries:
            year = int(YEAR_REGEX.search(lib).group())
            date_range = DateRange(dt(year, 1, 1), dt(year + 1, 1, 1) - timedelta(milliseconds=1))
            self.add(date_range, lib)

    def __init__(self, arctic_lib):
        self._arctic_lib = arctic_lib

        # The default collections
        self._collection = arctic_lib.get_top_level_collection()

    def add(self, date_range, library_name):
        """
        Adds the library with the given date range to the underlying collection of libraries used by this store.
        The underlying libraries should not overlap as the date ranges are assumed to be CLOSED_CLOSED by this function
        and the rest of the class.

        Arguments:

        date_range: A date range provided on the assumption that it is CLOSED_CLOSED. If for example the underlying
        libraries were split by year, the start of the date range would be datetime.datetime(year, 1, 1) and the end
        would be datetime.datetime(year, 12, 31, 23, 59, 59, 999000). The date range must fall on UTC day boundaries,
        that is the start must be add midnight and the end must be 1 millisecond before midnight.

        library_name: The name of the underlying library. This must be the name of a valid Arctic library
        """
        # check that the library is valid
        try:
            self._arctic_lib.arctic[library_name]
        except Exception as e:
            logger.error("Could not load library")
            raise e
        assert date_range.start and date_range.end, "Date range should have start and end properties {}".format(date_range)
        start = date_range.start.astimezone(mktz('UTC')) if date_range.start.tzinfo is not None else date_range.start.replace(tzinfo=mktz('UTC'))
        end = date_range.end.astimezone(mktz('UTC')) if date_range.end.tzinfo is not None else date_range.end.replace(tzinfo=mktz('UTC'))
        assert start.time() == time.min and end.time() == end_time_min, "Date range should fall on UTC day boundaries {}".format(date_range)
        # check that the date range does not overlap
        library_metadata = self._get_library_metadata(date_range)
        if len(library_metadata) > 1 or (len(library_metadata) == 1 and library_metadata[0] != library_name):
            raise OverlappingDataException("""There are libraries that overlap with the date range:
library: {}
overlapping libraries: {}""".format(library_name, [l.library for l in library_metadata]))
        self._collection.update_one({'library_name': library_name},
                                    {'$set': {'start': start, 'end': end}}, upsert=True)

    def read(self, symbol, date_range, columns=['BID', 'ASK', 'TRDPRC_1', 'BIDSIZE', 'ASKSIZE', 'TRDVOL_1'], include_images=False):
        libraries = self._get_libraries(date_range)
        dfs = []
        for l in libraries:
            try:
                df = l.library.read(symbol, l.date_range.intersection(date_range), columns,
                                    include_images=include_images)
                dfs.append(df)
            except NoDataFoundException as e:
                continue
        if len(dfs) == 0:
            raise NoDataFoundException("No Data found for {} in range: {}".format(symbol, date_range))
        return pd.concat(dfs)

    def write(self, symbol, data):
        # get the full set of date ranges that we have
        cursor = self._collection.find()
        for res in cursor:
            library = self._arctic_lib.arctic[res['library_name']]
            dslice = self._slice(data, res['start'], res['end'])
            if len(dslice) != 0:
                library.write(symbol, dslice)

    def list_symbols(self, date_range):
        libraries = self._get_libraries(date_range)
        return sorted(list(set(itertools.chain(*[l.library.list_symbols() for l in libraries]))))

    def get_name(self):
        name = self._arctic_lib.get_name()
        if name.startswith(self._arctic_lib.DB_PREFIX + '_'):
            name = name[len(self._arctic_lib.DB_PREFIX) + 1:]
        return name

    def _get_libraries(self, date_range):
        libraries = self._get_library_metadata(date_range)

        rtn = [TickStoreLibrary(self._arctic_lib.arctic[library.library], library.date_range)
               for library in libraries]
        current_start = rtn[-1].date_range.end if rtn else dt(1970, 1, 1, 0, 0)  # epoch
        if date_range.end is None or current_start < date_range.end:
            name = self.get_name()
            db_name, tick_type = name.split('.', 1)
            current_lib = "{}_current.{}".format(db_name, tick_type)
            try:
                rtn.append(TickStoreLibrary(self._arctic_lib.arctic[current_lib],
                                            DateRange(current_start, None, OPEN_OPEN)))
            except LibraryNotFoundException:
                pass  # No '_current', move on.

        if not rtn:
            raise NoDataFoundException("No underlying libraries exist for the given date range")
        return rtn

    def _slice(self, data, start, end):
        if isinstance(data, list):
            dictlist = DictList(data, 'index')
            slice_start = bisect.bisect_left(dictlist, start)
            slice_end = bisect.bisect_right(dictlist, end)
            return data[slice_start:slice_end]
        elif isinstance(data, pd.DataFrame):
            return data[start:end]
        else:
            raise UnhandledDtypeException("Can't persist type %s to tickstore" % type(data))

    def _get_library_metadata(self, date_range):
        """
        Retrieve the libraries for the given date range, the assumption is that the date ranges do not overlap and
        they are CLOSED_CLOSED.

        At the moment the date range is mandatory
        """
        if date_range is None:
            raise Exception("A date range must be provided")
        if not (date_range.start and date_range.end):
            raise Exception("The date range {0} must contain a start and end date".format(date_range))

        start = date_range.start if date_range.start.tzinfo is not None else date_range.start.replace(tzinfo=mktz())
        end = date_range.end if date_range.end.tzinfo is not None else date_range.end.replace(tzinfo=mktz())
        query = {'$or': [{'start': {'$lte': start}, 'end': {'$gte': start}},
                         {'start': {'$gte': start}, 'end': {'$lte': end}},
                         {'start': {'$lte': end}, 'end': {'$gte': end}}]}
        return [TickStoreLibrary(res['library_name'], DateRange(res['start'], res['end'], CLOSED_CLOSED))
                for res in self._collection.find(query,
                                                 projection={'library_name': 1,
                                                             'start': 1, 'end': 1},
                                                 sort=[('start', pymongo.ASCENDING)])]
