import numpy as np
from pandas.util.testing import assert_frame_equal
import pandas as pd

# Tests parameterised to use multiple backends.
# Tests are quite generic as they must apply only to commonalities between backends


def test_save_read_simple_df(version_store):
    df = pd.DataFrame({'a': [1, 2], 'b': [3.5, 4]})
    df.index.name = 'index'
    version_store.write('MYARR', df)
    saved_df = version_store.read('MYARR').data
    assert_frame_equal(df, saved_df)


def test_save_read_big_df(version_store):
    df = pd.DataFrame(np.random.rand(5326, 6020), columns=map(str, range(6020)))
    df.index.name = 'index'
    version_store.write('MYARR', df)
    saved_df = version_store.read('MYARR').data
    assert_frame_equal(df, saved_df)


def test_save_read_dict(version_store):
    d = {'a': 'hello', 'b': (1, 2, 3), 'c': [7, 8, 9]}
    version_store.write('my_dict', d)
    saved_d = version_store.read('my_dict').data
    assert d == saved_d


def test_handles_missing_symbols(version_store):
    assert version_store.has_symbol('my_dict_sdfsdf') is False


def test_has_symbol(version_store):
    df = pd.DataFrame({'a': [1, 2], 'b': [3.5, 4]})
    version_store.write('MYARR', df)
    assert version_store.has_symbol('MYARR')


def test_multiple_write(version_store):
    df = pd.DataFrame({'a': range(1000), 'b': range(2000, 3000)})
    df.index.name = 'index'
    version_store.write('MYARR', df)
    v1 = version_store.read('MYARR').version
    version_store.write('MYARR', df.iloc[:900])
    v2 = version_store.read('MYARR').version
    version_store.write('MYARR', df.iloc[:950])
    v3 = version_store.read('MYARR').version

    assert_frame_equal(df, version_store.read('MYARR', version_id=v1).data)
    assert_frame_equal(df.iloc[:900], version_store.read('MYARR', version_id=v2).data)
    assert_frame_equal(df.iloc[:950], version_store.read('MYARR', version_id=v3).data)
    aassert_frame_equal(df.iloc[:950], version_store.read('MYARR').data)

