from collections import namedtuple
from datetime import datetime as dt

from arctic.multi_index import fancy_group_by
import pandas as pd

from .version_store import VersionStore


BITEMPORAL_STORE_TYPE = 'BitemporalStore'

BitemporalItem = namedtuple('BitemporalItem', 'symbol, library, data, metadata')


class BitemporalStore(VersionStore):

    def __init__(self, arctic_lib, observe_column='observed_dt', sample_column='sample_dt'):
        super(BitemporalStore, self).__init__(arctic_lib)
        self.observe_column = observe_column
        self.sample_column = sample_column

    def read(self, symbol, as_of=None, **kwargs):
        # TODO: shall we block from_version from getting into super.read?
        item = super(BitemporalStore, self).read(symbol, **kwargs)

        result = BitemporalItem(symbol=symbol, library=self._arctic_lib.get_name(),
                                data=fancy_group_by(item.data, grouping_level=self.observe_column,
                                                    aggregate_level=self.sample_column, max_=as_of),
                                metadata=item.metadata)
        return result

    def append(self, symbol, data, metadata=None, upsert=True, as_of=None, **kwargs):
        data = self._preprocess_incoming_data(data, as_of)
        if upsert and not self.has_symbol(symbol):
            df = data
        else:
            df = super(BitemporalStore, self).read(symbol, **kwargs).data.append(data)
        super(BitemporalStore, self).write(symbol, df, metadata=metadata, prune_previous_version=True)

    def write(self, *args, **kwargs):
        # TODO: may be diff + append?
        raise NotImplementedError('Direct write for BitemporalStore is not supported. Use append instead'
                                  'to add / modify timeseries.')

    def _preprocess_incoming_data(self, df, as_of):
        if self.sample_column not in df:
            # TODO: Move this to multi_index
            if not as_of:
                as_of = dt.now()
            df = pd.concat([df, pd.DataFrame([as_of] * len(df), index=df.index, columns=[self.sample_column])], axis=1)
            df.set_index(self.sample_column, append=True, inplace=True)
        return df
