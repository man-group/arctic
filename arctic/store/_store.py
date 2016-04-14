class BaseStore(object):
    def can_delete(self, version, symbol):
        pass

    def can_read(self, version, symbol):
        pass

    def can_write(self, version, symbol, data, **kwargs):
        pass

    def can_update(self, version, symbol, data, **kwargs):
        pass
