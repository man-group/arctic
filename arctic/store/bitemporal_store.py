from collections import namedtuple
from datetime import datetime as dt

from arctic.multi_index import fancy_group_by
import pandas as pd

from .version_store import VersionStore


BITEMPORAL_STORE_TYPE = 'BitemporalStore'

BitemporalItem = namedtuple('BitemporalItem', 'data, metadata')


class BitemporalStore(VersionStore):

    def __init__(self, arctic_lib, observe_column='observed_dt', sample_column='sample_dt'):
        super(BitemporalStore, self).__init__(arctic_lib)
        self.observe_column = observe_column
        self.sample_column = sample_column

    def read(self, symbol, as_of=None, from_version=None, **kwargs):
        item = super(BitemporalStore, self).read(symbol, from_version=from_version, **kwargs)

        result = BitemporalItem(data=fancy_group_by(item.data, grouping_level=self.observe_column,
                                                    aggregate_level=self.sample_column, max_=as_of),
                                metadata=item.metadata)
        return result

    def append(self, symbol, data, metadata=None, upsert=True, **kwargs):
        data = self._preprocess_incoming_data(data)
        if upsert and not self.has_symbol(symbol):
            df = data
        else:
            df = super(BitemporalStore, self).read(symbol, **kwargs).data.append(data)
        super(BitemporalStore, self).write(symbol, df, metadata=metadata, prune_previous_version=True)

    def write(self, *args, **kwargs):
        # TODO: may be diff + append?
        raise NotImplementedError('Direct write for BitemporalStore is not supported. Use append instead'
                                  'to add / modify timeseries.')

    def _preprocess_incoming_data(self, df):
        if self.sample_column not in df:
            # TODO: Move this to multi_index
            now = dt.now()
            df = pd.concat([df, pd.DataFrame([now] * len(df), index=df.index, columns=[self.sample_column])], axis=1)
            df.set_index(self.sample_column, append=True, inplace=True)
        return df
            
        
