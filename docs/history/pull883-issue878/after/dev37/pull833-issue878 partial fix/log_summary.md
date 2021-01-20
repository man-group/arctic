
File "/home/travis/build/man-group/arctic/arctic/__init__.py", line 6, in <module>
    from .store._pandas_ndarray_store import PandasDataFrameStore, PandasSeriesStore, PandasPanelStore
  File "/home/travis/build/man-group/arctic/arctic/store/_pandas_ndarray_store.py", line 6, in <module>
    from pandas import DataFrame, Series, Panel

File "/home/travis/build/man-group/arctic/arctic/__init__.py", line 6, in <module>
    from .store._pandas_ndarray_store import PandasDataFrameStore, PandasSeriesStore, PandasPanelStore

File "/home/travis/build/man-group/arctic/arctic/store/_pandas_ndarray_store.py", line 6, in <module>
    from pandas import DataFrame, Series, Panel

ImportError: Error importing plugin "arctic.fixtures.arctic": cannot import name 'Panel' from 'pandas'
