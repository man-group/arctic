class BaseStore(object):
    def read(self, lib, version, symbol, **kwargs):
        pass

    def write(self, lib, version, symbol, item, previous_version):
        pass

    def get_info(self, lib, version, symbol, **kwargs):
        pass

