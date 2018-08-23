from datetime import datetime as dt, timedelta as dtd

import bson
import numpy as np
import numpy.testing as npt
import pytest
from mock import patch
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


def test_multiple_write(version_store):
    df = pd.DataFrame({'a': range(1000), 'b': range(2000, 3000)})
    df.index.name = 'index'
    version_store.write('MYARR', df)
    v1 = version_store.read('MYARR').version
    version_store.write('MYARR', df.iloc[:900])
    v2 = version_store.read('MYARR').version
    version_store.write('MYARR', df.iloc[:950])
    v3 = version_store.read('MYARR').version

    assert np.all(df == version_store.read('MYARR', version_id=v1).data)
    assert np.all(df.iloc[:900] == version_store.read('MYARR', version_id=v2).data)
    assert np.all(df.iloc[:950] == version_store.read('MYARR', version_id=v3).data)
    assert np.all(df.iloc[:950] == version_store.read('MYARR').data)

