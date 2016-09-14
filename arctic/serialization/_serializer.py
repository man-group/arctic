class Serializer(object):
    def serialize(self, data, **kwargs):
        raise NotImplementedError

    def deserialize(self, data, **kwargs):
        raise NotImplementedError

    def combine(self, a, b):
        raise NotImplementedError
