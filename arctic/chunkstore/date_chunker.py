import pandas as pd

from ._chunker import Chunker, START, END
from ..date import DateRange


class DateChunker(Chunker):
    TYPE = 'date'

    def to_chunks(self, df, chunk_size='D', **kwargs):
        """
        chunks the dataframe/series by dates

        returns
        -------
        generator that produces tuples: (start date, end date,
                  chunk_size, dataframe/series)
        """
        if chunk_size not in ('D', 'M', 'Y', 'A'):
            raise Exception("Chunk size must be one of D, M, Y, A")

        if 'date' in df.index.names:
            dates = df.index.get_level_values('date')
        elif 'date' in df.columns:
            dates = pd.DatetimeIndex(df.date)
        else:
            raise Exception("Data must be datetime indexed or have a column named 'date'")

        for period, g in df.groupby(dates.to_period(chunk_size)):
            start, end = period.start_time.to_pydatetime(warn=False), period.end_time.to_pydatetime(warn=False)
            yield start, end, chunk_size, g

    def to_range(self, start, end):
        """
        takes start, end from to_chunks and returns a "range" that can be used
        as the argument to methods require a chunk_range

        returns
        -------
        A range object (dependent on type of chunker)
        """
        return DateRange(start, end)

    def chunk_to_str(self, chunk_id):
        """
        Converts parts of a chunk range (start or end) to a string. These
        chunk ids/indexes/markers are produced by to_chunks.
        (See to_chunks)

        returns
        -------
        string
        """
        return chunk_id.strftime("%Y-%m-%d").encode('ascii')

    def to_mongo(self, range_obj):
        """
        takes the range object used for this chunker type
        and converts it into a string that can be use for a
        mongo query that filters by the range

        returns
        -------
        dict
        """
        if isinstance(range_obj, pd.DatetimeIndex):
            range_obj = DateRange(range_obj.min(), range_obj.max())
        if range_obj.start and range_obj.end:
            return {'$and': [{START: {'$lte': range_obj.end}}, {END: {'$gte': range_obj.start}}]}
        elif range_obj.start:
            return {END: {'$gte': range_obj.start}}
        elif range_obj.end:
            return {START: {'$lte': range_obj.end}}
        else:
            return {}

    def filter(self, data, range_obj):
        """
        ensures data is properly subset to the range in range_obj.
        (Depending on how the chunking is implemented, it might be possible
        to specify a chunk range that reads out more than the actual range
        eg: date range, chunked monthly. read out 2016-01-01 to 2016-01-02.
        This will read ALL of January 2016 but it should be subset to just
        the first two days)

        returns
        -------
        data, filtered by range_obj
        """
        if isinstance(range_obj, pd.DatetimeIndex):
            range_obj = DateRange(range_obj.min(), range_obj.max())
        if 'date' in data.index.names:
            return data[range_obj.start:range_obj.end]
        elif 'date' in data.columns:
            if range_obj.end:
                return data[(data.date >= range_obj.start) & (data.date <= range_obj.end)]
            else:
                return data[(data.date >= range_obj.start)]
        else:
            return data

    def exclude(self, data, range_obj):
        """
        Removes data within the bounds of the range object (inclusive)

        returns
        -------
        data, filtered by range_obj
        """
        if isinstance(range_obj, pd.DatetimeIndex):
            range_obj = DateRange(range_obj.min(), range_obj.max())
        if 'date' in data.index.names:
            return data[(data.index.get_level_values('date') < range_obj.start) | (data.index.get_level_values('date') > range_obj.end)]
        elif 'date' in data.columns:
            return data[(data.date < range_obj.start) | (data.date > range_obj.end)]
        else:
            return data
