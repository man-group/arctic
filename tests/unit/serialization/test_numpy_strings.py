import pandas as pd
import numpy as np
import pytest
from pandas.util.testing import assert_frame_equal

from arctic.serialization.numpy_strings import FrameConverter, NumpyString


def test_frame_converter():
    f = FrameConverter()
    df = pd.DataFrame(np.random.randint(0, 100, size=(100, 4)),
                      columns=list('ABCD'))

    assert_frame_equal(f.objify(f.docify(df)), df)


def test_with_strings():
    f = FrameConverter()
    df = pd.DataFrame(data={'one': ['a', 'b', 'c']})

    assert_frame_equal(f.objify(f.docify(df)), df)


def test_with_objects_raises():
    class Example(object):
        def __init__(self, data):
            self.data = data

        def get(self):
            return self.data

    f = FrameConverter()
    df = pd.DataFrame(data={'one': [Example(444)]})

    with pytest.raises(Exception):
        f.docify(df)


def test_without_index():
    df = pd.DataFrame(np.random.randint(0, 100, size=(100, 4)),
                      columns=list('ABCD'))
    n = NumpyString()
    a = n.serialize(df)
    assert_frame_equal(df, n.deserialize(a))
