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

        if 'date' not in df.index.names:
            raise Exception("Data must be datetime indexed and have an index column named 'date'")

        for period, g in df.groupby(df.index.get_level_values('date').to_period(chunk_size)):
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
        return data[range_obj.start:range_obj.end]

    def exclude(self, data, range_obj):
        return data[(data.index.get_level_values('date') < range_obj.start) | (data.index.get_level_values('date') > range_obj.end)]
