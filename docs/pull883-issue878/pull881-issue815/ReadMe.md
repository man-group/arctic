# [#815: Remove Panel reference](https://github.com/man-group/arctic/issues/815)

pull request: [#881: Fix for issue #815 ](https://github.com/man-group/arctic/pull/881)

* /arctic/store/_pandas_ndarray_store.py
```python
from pandas import DataFrame, Series
try:
    from pandas import Panel		# FIXME pull881
except ImportError:
    pass
```