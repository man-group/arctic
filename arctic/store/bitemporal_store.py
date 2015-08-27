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
                                data=fancy_group_by(item.data, grouping_level=self.sample_column,
                                                    aggregate_level=self.observe_column, max_=as_of),
                                metadata=item.metadata)
        return result

    def append(self, symbol, data, metadata=None, upsert=True, as_of=None, **kwargs):
        assert self.observe_column not in data
        if not as_of:
            as_of = dt.now()
        data = self._add_observe_dt_index(data, as_of)
        if upsert and not self.has_symbol(symbol):
            df = data
        else:
            existing_item = super(BitemporalStore, self).read(symbol, **kwargs)
            if metadata is None:
                metadata = existing_item.metadata
            df = existing_item.data.append(data)
        super(BitemporalStore, self).write(symbol, df, metadata=metadata, prune_previous_version=True)

    def write(self, *args, **kwargs):
        # TODO: may be diff + append?
        raise NotImplementedError('Direct write for BitemporalStore is not supported. Use append instead'
                                  'to add / modify timeseries.')

    def _add_observe_dt_index(self, df, as_of):
        df = df.set_index(pd.MultiIndex.from_product([df.index, as_of],
                                                     names=[self.sample_column, self.observe_column]),
                          inplace=False)
        return df
