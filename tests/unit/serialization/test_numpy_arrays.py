import numpy as np
import pandas as pd
import pytest
from pandas.util.testing import assert_frame_equal

from arctic.serialization.numpy_arrays import FrameConverter, FrametoArraySerializer
from tests.util import assert_frame_equal_


def test_frame_converter():
    f = FrameConverter()
    df = pd.DataFrame(np.random.randint(0, 100, size=(100, 4)),
                      columns=list('ABCD'))

    assert_frame_equal_(f.objify(f.docify(df)), df)


def test_with_strings():
    f = FrameConverter()
    df = pd.DataFrame(data={'one': ['a', 'b', 'c']})

    assert_frame_equal_(f.objify(f.docify(df)), df)


def test_frame_converter_with_all_valid_column_subset():
    f = FrameConverter()
    df = pd.DataFrame(np.random.randint(0, 100, size=(100, 4)),
                      columns=list('ABCD'))

    assert_frame_equal_(f.objify(f.docify(df), columns=['A', 'B']), df[['A', 'B']])


def test_frame_converter_with_some_invalid_column_subset():
    f = FrameConverter()
    df = pd.DataFrame(np.random.randint(0, 100, size=(100, 4)),
                      columns=list('ABCD'))
    expected = pd.DataFrame({'A': df['A'], 'N': np.nan})
    assert_frame_equal_(f.objify(f.docify(df), columns=['A', 'N']), expected[['A', 'N']])


def test_frame_converter_with_no_valid_column_subset():
    f = FrameConverter()
    df = pd.DataFrame(np.random.randint(0, 100, size=(100, 4)),
                      columns=list('ABCD'))
    assert f.objify(f.docify(df), columns=['N']).empty


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
    assert_frame_equal_(df, n.deserialize(a))


def test_with_index():
    df = pd.DataFrame(np.random.randint(0, 100, size=(100, 4)),
                      columns=list('ABCD'))
    df = df.set_index(['A'])
    n = FrametoArraySerializer()
    a = n.serialize(df)
    assert_frame_equal_(df, n.deserialize(a))


def test_invalid_column_subset_with_index():
    df = pd.DataFrame(np.random.randint(0, 100, size=(100, 4)),
                      columns=list('ABCD'))
    df = df.set_index(['A'])
    n = FrametoArraySerializer()
    a = n.serialize(df)
    expected = pd.DataFrame({'N': np.nan}, index=df.index)
    assert_frame_equal(expected, n.deserialize(a, columns=['N']))


@pytest.mark.parametrize('index', [True, False])
@pytest.mark.parametrize('columns', [None, ['B', 'D'], ['D', 'B']])
def test_multiple_data_input_different_columns(columns, index):
    df = pd.DataFrame(np.random.randint(0, 100, size=(100, 4)),
                      columns=list('ABCD'))
    if index:
        df = df.set_index(['A'])
    n = FrametoArraySerializer()
    a = n.serialize(df[['B']])
    b = n.serialize(df[['D']])
    expected = df[['B']].append(df[['D']], ignore_index=not index)
    assert_frame_equal(expected, n.deserialize([a, b], columns=columns))


@pytest.mark.parametrize('column', [['B'], ['D']])
def test_multiple_data_input_with_no_index_and_invalid_column(column):
    df = pd.DataFrame(np.random.randint(0, 100, size=(100, 4)),
                      columns=list('ABCD'))
    n = FrametoArraySerializer()
    a = n.serialize(df[['B']])
    b = n.serialize(df[['D']])
    assert_frame_equal(df[column], n.deserialize([a, b], columns=column))


def test_with_nans():
    df = pd.DataFrame(np.random.randint(0, 100, size=(100, 4)),
                      columns=list('ABCD'))
    df['A'] = np.NaN
    n = FrametoArraySerializer()
    a = n.serialize(df)
    assert_frame_equal_(df, n.deserialize(a))


def test_empty_dataframe():
    df = pd.DataFrame()
    n = FrametoArraySerializer()
    a = n.serialize(df)
    assert_frame_equal(df, n.deserialize(a))


def test_empty_columns():
    df = pd.DataFrame(data={'A': [], 'B': [], 'C': []})
    n = FrametoArraySerializer()
    a = n.serialize(df)
    assert_frame_equal_(df, n.deserialize(a))


def test_string_cols_with_nans():
    f = FrameConverter()
    df = pd.DataFrame(data={'one': ['a', 'b', 'c', np.NaN]})

    assert(df.equals(f.objify(f.docify(df))))


def test_objify_with_missing_columns():
    f = FrameConverter()
    df = pd.DataFrame(data={'one': ['a', 'b', 'c', np.NaN]})
    res = f.objify(f.docify(df), columns=['one', 'two'])
    assert res['one'].equals(df['one'])
    assert all(res['two'].isnull())


def test_multi_column_fail():
    df = pd.DataFrame(data={'A': [1, 2, 3], 'B': [2, 3, 4], 'C': [3, 4, 5]})
    df = df.set_index(['A'])
    n = FrametoArraySerializer()
    a = n.serialize(df)

    with pytest.raises(Exception) as e:
        n.deserialize(a, columns=['A', 'B'])
    assert('Duplicate' in str(e.value))


def test_dataframe_writable_after_objify():
    f = FrameConverter()
    df = pd.DataFrame(data={'one': [5, 6, 2]})
    df = f.objify(f.docify(df))
    df['one'] = 7

    assert np.all(df['one'].values == np.array([7, 7, 7]))
