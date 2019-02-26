import logging
import pandas as pd
import numpy as np
import io
from contextlib import contextmanager


logger = logging.getLogger(__name__)


@contextmanager
def _dummy_open(file_like, _):
    yield file_like


class ParquetStore(object):

    TYPE = 'parquet'

    @classmethod
    def initialize_library(cls, *args, **kwargs):
        pass

    def can_delete(self, version, symbol):
        return self.can_read(version, symbol)

    def can_read(self, version, symbol):
        return version['type'] == self.TYPE

    def can_write(self, version, symbol, data):
        if isinstance(data, pd.DataFrame):
            if np.any(data.dtypes.values == 'object'):
                # TODO to a proper check to see if we can convert to parquet
                pass
            return True
        return False

    def get_info(self, version):
        ret = {'type': self.TYPE, 'handler': self.__class__.__name__}
        return ret

    def read(self, backing_store, library_name, version, symbol, **kwargs):
        segment_keys = version['segment_keys']
        assert len(segment_keys) == 1, "should only be one segment for parquet"
        parquet_path = backing_store._make_segment_path(library_name, symbol, version['_id'])
        return pd.read_parquet(parquet_path, engine='fastparquet')

    def write(self, backing_store, library_name, version, symbol, item, previous_version):
        output = io.BytesIO()
        item.to_parquet(output, engine='fastparquet', open_with=_dummy_open,
                        compression='LZ4', file_scheme='simple')
        data = [output.getvalue()]

        if previous_version:
            previous_segment_keys = previous_version['segment_keys']
        else:
            previous_segment_keys = set()

        segment_keys = []
        for segment_data in data:
            segment_key = backing_store.write_segment(library_name, symbol,
                                                      segment_data, previous_segment_keys,
                                                      version['_id'])
            segment_keys.append(segment_key)
        version['segment_keys'] = segment_keys
        version['type'] = self.TYPE

        #TODO Check written?
