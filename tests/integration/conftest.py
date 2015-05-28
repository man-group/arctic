from contextlib import contextmanager
from mock import patch
import pytest
from pymongo.collection import Collection
from pymongo.errors import OperationFailure
import random
import traceback


# @contextmanager
# def poisonous_mongo(name, orig_function):
#     """
#     Poison the update command by raising 2.5% of the time
#     """
#     def new_function(*args, **kwargs):
#         if random.random() < 0.025:
#             raise OperationFailure('something went wrong ' + "\n".join(traceback.format_stack()))
#         return orig_function(*args, **kwargs)
#     with patch(name, new_function):
#         yield
#
#
# @pytest.yield_fixture(autouse=True)
# def poison_fixture():
#     with poisonous_mongo("pymongo.collection.Collection.update", Collection.update), \
#          poisonous_mongo("pymongo.collection.Collection.find", Collection.find), \
#          poisonous_mongo("pymongo.collection.Collection.insert", Collection.insert):
#         yield


pytest_plugins = ['arctic.fixtures.arctic'
                  ]
