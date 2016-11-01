import pytest
from pandas import DataFrame, Series
from arctic.chunkstore.passthrough_chunker import PassthroughChunker
import six


def test_pass_thru():
    p = PassthroughChunker()
    with pytest.raises(StopIteration):
        six.next(p.to_chunks([]))

    assert(p.to_range(None, None) == b'NA')
    assert(p.chunk_to_str(None) == b'NA')
    assert(p.to_mongo(None) == {})
    assert(p.filter(None, None) is None)
    assert(p.exclude(DataFrame(data=[1, 2, 3]), None).equals(DataFrame()))
    assert(p.exclude(Series([1, 2, 3]), None).equals(Series()))
