from collections import namedtuple


class VersionedItem(namedtuple('VersionedItem', ['symbol', 'library', 'data', 'version', 'metadata', 'host'])):
    """
    Class representing a Versioned object in VersionStore.
    """

    def __new__(cls, symbol, library, data, version, metadata, host=None):
        return super(VersionedItem, cls).__new__(cls, symbol, library, data, version, metadata, host)

    def metadata_dict(self):
        return {'symbol': self.symbol, 'library': self.library, 'version': self.version}

    def __repr__(self):
        return str(self)

    def __str__(self):
        return "VersionedItem(symbol=%s,library=%s,data=%s,version=%s,metadata=%s,host=%s)" % \
            (self.symbol, self.library, type(self.data), self.version, self.metadata, self.host)


ChangedItem = namedtuple('ChangedItem', ['symbol', 'orig_version', 'new_version', 'changes'])
