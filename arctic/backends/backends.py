"""
Generic/Shared backend code and data
"""
from arctic.store import version_store, bson_store, metadata_store
from arctic.tickstore import tickstore, toplevel
from arctic.chunkstore import chunkstore


APPLICATION_NAME = 'arctic'

VERSION_STORE = version_store.VERSION_STORE_TYPE
METADATA_STORE = metadata_store.METADATA_STORE_TYPE
TICK_STORE = tickstore.TICK_STORE_TYPE
CHUNK_STORE = chunkstore.CHUNK_STORE_TYPE
LIBRARY_TYPES = {version_store.VERSION_STORE_TYPE: version_store.VersionStore,
                 tickstore.TICK_STORE_TYPE: tickstore.TickStore,
                 toplevel.TICK_STORE_TYPE: toplevel.TopLevelTickStore,
                 chunkstore.CHUNK_STORE_TYPE: chunkstore.ChunkStore,
                 bson_store.BSON_STORE_TYPE: bson_store.BSONStore,
                 metadata_store.METADATA_STORE_TYPE: metadata_store.MetadataStore
                 }