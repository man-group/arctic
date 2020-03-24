"""
Copyright (C) 2020 Man Group
For a list of authors, see README.md; for the license, see file LICENSE in project root directory.
"""
class Serializer(object):
    def serialize(self, data, **kwargs):
        raise NotImplementedError

    def deserialize(self, data, **kwargs):
        raise NotImplementedError

    def combine(self, a, b):
        raise NotImplementedError
