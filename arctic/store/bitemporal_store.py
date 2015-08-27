from collections import namedtuple
from datetime import datetime as dt

from arctic.multi_index import fancy_group_by
import pandas as pd

from .version_store import VersionStore


BITEMPORAL_STORE_TYPE = 'BitemporalStore'

BitemporalItem = namedtuple('BitemporalItem', 'symbol, library, data, metadata')


class BitemporalStore(VersionStore):
    """ A versioned pandas DataFrame store. (currently only supports single index df)

    As the name hinted, this holds versions of DataFrame by maintaining an extra 'insert time' index internally.
    """

    def __init__(self, arctic_lib, sample_column='sample_dt', observe_column='observed_dt'):
        """
        Parameters
        ----------
        arctic_lib : `ArcticLibraryBinding`
        sample_column : `str`
            Column name for the datetime index that represents that samaple time of the data.
        observe_column : `str`
            Column name for the datetime index that represents the insertion time of a row of data. This column is
            internal to this store.
        """
        super(BitemporalStore, self).__init__(arctic_lib)
        self.observe_column = observe_column
        self.sample_column = sample_column

    def read(self, symbol, as_of=None, raw=False, **kwargs):
        # TODO: shall we block from_version from getting into super.read?
        """Read data for the named symbol. Returns a BitemporalItem object with
        a data and metdata element (as passed into write).

        Parameters
        ----------
        symbol : `str`
            symbol name for the item
        as_of : `datetime.datetime`
            Return the data as it was as_of the point in time.
        raw : `bool`
            If True, will return the full bitemporal dataframe (i.e. all versions of the data). This also means as_of is
            ignored.

        Returns
        -------
        BitemporalItem namedtuple which contains a .data and .metadata element
        """
        item = super(BitemporalStore, self).read(symbol, **kwargs)
        if raw:
            return BitemporalItem(symbol=symbol, library=self._arctic_lib.get_name(), data=item.data,
                                    metadata=item.metadata)
        else:
            return BitemporalItem(symbol=symbol, library=self._arctic_lib.get_name(),
                                  data=fancy_group_by(item.data, grouping_level=self.sample_column,
                                                      aggregate_level=self.observe_column, max_=as_of),
                                  metadata=item.metadata)

    def append(self, symbol, data, metadata=None, upsert=True, as_of=None, **kwargs):
        """ Append 'data' under the specified 'symbol' name to this library.

        Parameters
        ----------
        symbol : `str`
            symbol name for the item
        data : `pd.DataFrame`
            to be persisted
        metadata : `dict`
            An optional dictionary of metadata to persist along with the symbol. If None and there are existing
            metadata, current metadata will be maintained
        upsert : `bool`
            Write 'data' if no previous version exists.
        as_of : `datetime.datetime`
            The "insert time". Default to datetime.now()t
        """
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
