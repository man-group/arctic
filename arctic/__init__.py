""" The Arctic TimeSeries and Tick store."""

import pandas

from .arctic import Arctic, register_library_type
from .arctic import VERSION_STORE, TICK_STORE, CHUNK_STORE
from .store._ndarray_store import NdarrayStore
from .store._pandas_ndarray_store import PandasDataFrameStore, PandasSeriesStore, PandasPanelStore
from .store.version_store import register_versioned_storage, register_version

try:
    from pkg_resources import get_distribution
    str_version = get_distribution(__name__).version.strip()
    int_parts = tuple(int(x) for x in str_version.split('.'))
    num_version = sum([1000 ** i * v for i, v in enumerate(reversed(int_parts))])
    register_version(str_version, num_version)
except Exception:
    __version__ = None
    __version_parts__ = tuple()
    __version_numerical__ = 0
else:
    __version__ = str_version
    __version_parts__ = int_parts
    __version_numerical__ = num_version


register_versioned_storage(PandasDataFrameStore)
register_versioned_storage(PandasSeriesStore)
register_versioned_storage(NdarrayStore)

if pandas.__version__.startswith("0."):
    # Panel is removed in pandas 1
    register_versioned_storage(PandasPanelStore)
