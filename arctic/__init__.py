""" The Arctic TimeSeries and Tick store."""

from .arctic import Arctic, register_library_type
from .arctic import VERSION_STORE, TICK_STORE, CHUNK_STORE
from .store.version_store import register_versioned_storage
from .store._pandas_ndarray_store import PandasDataFrameStore, PandasSeriesStore, PandasPanelStore
from .store._ndarray_store import NdarrayStore

try:
    from pkg_resources import get_distribution
    str_version = get_distribution(__name__).version.strip()
    int_parts = tuple(int(x) for x in str_version.split('.'))
except Exception:
    __version__ = None
    __version_parts__ = tuple()
else:
    __version__ = str_version
    __version_parts__ = int_parts


register_versioned_storage(PandasDataFrameStore)
register_versioned_storage(PandasSeriesStore)
register_versioned_storage(PandasPanelStore)
register_versioned_storage(NdarrayStore)

