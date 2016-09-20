START = 's'
END = 'e'


class Chunker(object):

    def to_chunks(self, data, **kwargs):
        """
        Chunks data. keyword args passed in from write API

        returns
        -------
        generator that produces 4-tuples
            (chunk start index/marker/key,
            chunk end index/marker/key,
            chunk_size,
            chunked data)
        """
        raise NotImplementedError

    def to_range(self, start, end):
        """
        takes start, end from to_chunks and returns a "range" that can be used
        as the argument to methods require a chunk_range

        returns
        -------
        A range object (dependent on type of chunker)
        """
        raise NotImplementedError

    def to_mongo(self, range_obj):
        """
        takes the range object used for this chunker type
        and converts it into a string that can be use for a
        mongo query that filters by the range

        returns
        -------
        dict
        """
        raise NotImplementedError

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
        raise NotImplementedError

    def exclude(self, data, range_obj):
        """
        Removes data within the bounds of the range object (inclusive)

        returns
        -------
        data, filtered by range_obj
        """
        raise NotImplementedError

    def chunk_to_str(self, chunk_id):
        """
        Converts parts of a chunk range (start or end) to a string. These
        chunk ids/indexes/markers are produced by to_chunks.
        (See to_chunks)

        returns
        -------
        string
        """
        raise NotImplementedError
