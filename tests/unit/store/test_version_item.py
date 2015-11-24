import pandas as pd

from arctic.store.versioned_item import VersionedItem


def test_versioned_item_str():
    item = VersionedItem(symbol="sym",
                         library="ONEMINUTE",
                         data=pd.DataFrame(),
                         version=1.0,
                         metadata={'metadata': 'foo'},
                         info=None)

    expected = "VersionedItem(symbol=sym,library=ONEMINUTE," + \
               "data=<class 'pandas.core.frame.DataFrame'>,version=1.0,metadata={'metadata': 'foo'},info=None"
    assert str(item) == expected
    assert repr(item) == expected


def test_versioned_item_str_handles_none():
    item = VersionedItem(symbol=None,
                         library=None,
                         data=None,
                         version=None,
                         metadata=None,
                         info=None)

    assert str(item)
