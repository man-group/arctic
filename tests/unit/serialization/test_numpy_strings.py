import pandas as pd
import numpy as np
import pytest
from pandas.util.testing import assert_frame_equal
from arctic.chunkstore.date_chunker import DateChunker

from arctic.serialization.numpy_strings import FrameConverter


def test_frame_converter():
    f = FrameConverter()
    df = pd.DataFrame(np.random.randint(0, 100, size=(100, 4)),
                      columns=list('ABCD'))

    print f.docify(df)

    assert_frame_equal(f.objify(f.docify(df)), df)


def test_with_strings():
    f = FrameConverter()
    df = pd.DataFrame(data={'one': ['a', 'b', 'c']})

    assert_frame_equal(f.objify(f.docify(df)), df)


def test_with_objects_raises():
    f = FrameConverter()
    df = pd.DataFrame(data={'one': [DateChunker()]})

    with pytest.raises(ValueError) as e:
        f.docify(df)
    assert('Cannot store arrays' in str(e))

