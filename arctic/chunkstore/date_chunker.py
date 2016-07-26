import pandas as pd

from ._chunker import Chunker
from ..date import DateRange


class DateChunker(Chunker):
    def to_chunks(self, df, chunk_size):
        """
        chunks the dataframe/series by dates

        returns
        -------
        generator that produces tuples: (start date, end date,
                  dataframe/series)
        """
        if chunk_size not in ('D', 'M', 'Y'):
            raise Exception("Chunk size must be one of D, M, Y")

        if 'date' in df.index.names:
            dates = df.index.get_level_values('date')
        elif 'date' in df.columns:
            dates = pd.DatetimeIndex(df.date)
        else:
            raise Exception("Data must be datetime indexed or have a column named 'date'")

        for period, g in df.groupby(dates.to_period(chunk_size)):
            start, end = period.start_time.to_pydatetime(warn=False), period.end_time.to_pydatetime(warn=False)
            yield start, end, g

    def to_range(self, start, end):
        return DateRange(start, end)

    def chunk_to_str(self, chunk_id):
        return chunk_id.strftime("%Y-%m-%d")

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
        if 'date' in data.index.names:
            return data[range_obj.start:range_obj.end]
        elif 'date' in data.columns:
            return data[(data.date >= range_obj.start) & (data.date <= range_obj.end)]
        else:
            return data

    def exclude(self, data, range_obj):
        if 'date' in data.index.names:
            return data[(data.index.get_level_values('date') < range_obj.start) | (data.index.get_level_values('date') > range_obj.end)]
        elif 'date' in data.columns:
            return data[(data.date < range_obj.start) | (data.date > range_obj.end)]
        else:
            return data
