import numpy as np
import pandas as pd


def test_save_read_simple_df(parquet_version_store):
    df = pd.DataFrame({'a': [1,2], 'b': ['foo', 'bar']})
    parquet_version_store.write('MYARR', df)
    saved_df = parquet_version_store.read('MYARR').data
    assert np.all(df == saved_df)


def test_multiple_write(parquet_version_store):
    df = pd.DataFrame({'a': range(1000), 'b': range(2000, 3000)})
    parquet_version_store.write('MYARR', df)
    v1 = parquet_version_store.read('MYARR').version
    parquet_version_store.write('MYARR', df.iloc[:900])
    v2 = parquet_version_store.read('MYARR').version
    parquet_version_store.write('MYARR', df.iloc[:950])
    v3 = parquet_version_store.read('MYARR').version

    assert np.all(df == parquet_version_store.read('MYARR', version_id=v1).data)
    assert np.all(df.iloc[:900] == parquet_version_store.read('MYARR', version_id=v2).data)
    assert np.all(df.iloc[:950] == parquet_version_store.read('MYARR', version_id=v3).data)
    assert np.all(df.iloc[:950] == parquet_version_store.read('MYARR').data)

