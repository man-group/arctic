import logging
import pandas as pd
import io
from contextlib import contextmanager


logger = logging.getLogger(__name__)


@contextmanager
def _dummy_open(file_like, _):
    yield file_like


class ParquetStore(object):

    @classmethod
    def initialize_library(cls, *args, **kwargs):
        pass

    def get_info(self, version):
        ret = {'type': 'parquet', 'handler': self.__class__.__name__}
        return ret

    def read(self, backing_store, library_name, version, symbol, **kwargs):
        segment_keys = version['segment_keys']
        assert len(segment_keys) == 1, "should only be one segment for parquet"
        # TODO this is S3 functionality bleeding out of the backing store.
        # Currently reading a Pandas dataframe from a parquet bytes array fails as it only takes a file path.
        # Need a PR for Pandas and/or Parquet to fix this.
        s3_path = "s3://{bucket}/{segment_key}".format(bucket=backing_store.bucket, segment_key=segment_keys[0])
        return pd.read_parquet(s3_path, engine='fastparquet')

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
                                                      segment_data, previous_segment_keys)
            segment_keys.append(segment_key)
        version['segment_keys'] = segment_keys

        #TODO Check written?
