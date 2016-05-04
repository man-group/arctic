import pandas as pd
from pandas import Timestamp

from ._chunker import Chunker
from ..date import DateRange


class DateChunker(Chunker):
    def _get_date_chunk(self, date, chunk_size):
        '''
        format date appropriately for the chunk size

        returns
        -------
        Formatted date string
        '''
        if chunk_size == 'Y':
            return date.strftime('%Y')
        elif chunk_size == 'M':
            return date.strftime('%Y-%m')
        elif chunk_size == 'D':
            return date.strftime('%Y-%m-%d')

    def _get_date_range(self, df):
        """
        get minx/max dates in the index of the dataframe

        returns
        -------
        A tuple (start date, end date)
        """
        dates = df.index.get_level_values('date')
        start = dates.min()
        end = dates.max()
        if isinstance(start, Timestamp):
            start = start.to_pydatetime()
        if isinstance(end, Timestamp):
            end = end.to_pydatetime()
        return start, end

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
            raise Exception("Data must be datetime indexed and have an index colum named 'date'")

        dates = [pd.to_datetime(d) for d in df.index.get_level_values('date').drop_duplicates()]
        key_array = [self._get_date_chunk(d, chunk_size) for d in dates]

        for date in set(key_array):
            if df.index.nlevels > 1:
                '''
                can't slice with partial date on multi-index. Support coming in
                pandas 0.18.1
                '''
                ret = df.xs(slice(date, date), level='date', drop_level=False)
            else:
                ret = df[date: date]
            start, end = self._get_date_range(ret)
            yield start, end, ret

    def to_range(self, start, end):
        return DateRange(start, end)

    def to_start_end(self, data):
        return self._get_date_range(data)

    def to_mongo(self, range_obj):
        return range_obj.mongo_query()

    def filter(self, data, range_obj):
        return data.ix[range_obj[0]:range_obj[1]]
