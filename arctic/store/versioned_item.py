from collections import namedtuple


class VersionedItem(namedtuple('VersionedItem', ['symbol', 'library', 'data', 'version', 'metadata', 'info'])):
    """
    Class representing a Versioned object in VersionStore.
    """
    def metadata_dict(self):
        return {'symbol': self.symbol, 'library': self.library, 'version': self.version,
                'info': self.info}

    def __repr__(self):
        return str(self)

    def __str__(self):
        return "VersionedItem(symbol=%s,library=%s,data=%s,version=%s,metadata=%s,info=%s" % \
            (self.symbol, self.library, type(self.data), self.version, self.metadata, self.info)


ChangedItem = namedtuple('ChangedItem', ['symbol', 'orig_version', 'new_version', 'changes'])
