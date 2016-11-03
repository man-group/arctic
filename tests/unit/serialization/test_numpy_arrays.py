import pandas as pd
import numpy as np
import pytest
from pandas.util.testing import assert_frame_equal

from arctic.serialization.numpy_arrays import FrameConverter, FrametoArraySerializer


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
    n = FrametoArraySerializer()
    a = n.serialize(df)
    assert_frame_equal(df, n.deserialize(a))


def test_with_index():
    df = pd.DataFrame(np.random.randint(0, 100, size=(100, 4)),
                      columns=list('ABCD'))
    df = df.set_index(['A'])
    n = FrametoArraySerializer()
    a = n.serialize(df)
    assert_frame_equal(df, n.deserialize(a))


def test_with_nans():
    df = pd.DataFrame(np.random.randint(0, 100, size=(100, 4)),
                      columns=list('ABCD'))
    df['A'] = np.NaN
    n = FrametoArraySerializer()
    a = n.serialize(df)
    assert_frame_equal(df, n.deserialize(a))


def test_empty_dataframe():
    df = pd.DataFrame()
    n = FrametoArraySerializer()
    a = n.serialize(df)
    assert_frame_equal(df, n.deserialize(a))


def test_empty_columns():
    df = pd.DataFrame(data={'A': [], 'B': [], 'C': []})
    n = FrametoArraySerializer()
    a = n.serialize(df)
    assert_frame_equal(df, n.deserialize(a))


def test_string_cols_with_nans():
    f = FrameConverter()
    df = pd.DataFrame(data={'one': ['a', 'b', 'c', np.NaN]})

    assert(df.equals(f.objify(f.docify(df))))


def test_multi_column_fail():
    df = pd.DataFrame(data={'A': [1, 2, 3], 'B': [2, 3, 4], 'C': [3, 4, 5]})
    df = df.set_index(['A'])
    n = FrametoArraySerializer()
    a = n.serialize(df)

    with pytest.raises(Exception) as e:
        n.deserialize(a, columns=['A', 'B'])
    assert('Duplicate' in str(e))
