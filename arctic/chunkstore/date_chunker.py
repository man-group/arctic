import calendar
from datetime import datetime as dt

from ._chunker import Chunker
from ..date import DateRange


class DateChunker(Chunker):
    def _get_date_range(self, df, chunk_size):
        """
        get minx/max dates for the chunk

        returns
        -------
        A tuple (start date, end date)
        """
        date = df.index.get_level_values('date')[0]

        if chunk_size == 'M':
            _, end_day = calendar.monthrange(date.year, date.month)
            return dt(date.year, date.month, 1), dt(date.year, date.month, end_day)
        elif chunk_size == 'Y':
            return dt(date.year, 1, 1), dt(date.year, 12, 31)
        else:
            return date, date

    def to_chunks(self, df, chunk_size):
        """
        chunks the dataframe/series by dates

        returns
        -------
        generator that produces tuples: (start dt, end dt, dataframe/series)
        """
        if chunk_size not in ('D', 'M', 'Y'):
            raise Exception("Chunk size must be one of D, M, Y")

        if 'date' not in df.index.names:
            raise Exception("Data must be datetime indexed and have an index column named 'date'")

        for _, g in df.groupby(df.index.get_level_values('date').to_period(chunk_size)):
            start, end = self._get_date_range(g, chunk_size)
            yield start, end, g

    def to_range(self, start, end):
        return DateRange(start, end)

    def to_mongo(self, range_obj):
        if range_obj.start and range_obj.end:
            return {'$and': [{'start': {'$lte': range_obj.end}}, {'end': {'$gte': range_obj.start}}]}
        elif range_obj.start:
            return {'end': {'$gte': range_obj.start}}
        elif range_obj.end:
            return {'start': {'$lte': range_obj.end}}
        else:
            return {}

    def filter(self, data, range_obj):
        return data[range_obj.start:range_obj.end]

    def exclude(self, data, range_obj):
        return data[(data.index.get_level_values('date') < range_obj.start) | (data.index.get_level_values('date') > range_obj.end)]
