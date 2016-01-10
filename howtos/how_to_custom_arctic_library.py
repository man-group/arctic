from __future__ import print_function
from datetime import datetime as dt
from bson.binary import Binary
from six.moves import cPickle    
from arctic import Arctic, register_library_type
from arctic.decorators import mongo_retry


#
# Arctic maps a library, e.g. 'jblackburn.stuff' to a class instance
# which implements whatever API you like.
#
# Arctic provides a standard switching layer for:
#    - Registering custom storage types (e.g. CustomArcticLibType)
#    - Mapping data libraries to a storage type (e.g. 'jblackburn.stuff' -> CustomArcticLibType)
#    - Handling Authentication
#    - Maintaining per-library metadata
#    - Quota
#


class Stuff(object):
    """
    Some custom class persisted by our CustomArcticLibType Library Type
    """
    def __init__(self, field1, date_field, stuff):
        # Some string field
        self.field1 = field1
        # Some date field
        self.date_field = date_field
        # Arbitrary other stuff
        self.stuff = stuff

    def __str__(self):
        return str(self.field1) + " " + str(self.date_field) + " " + str(self.stuff)


class CustomArcticLibType(object):
    """
    Custom Arctic Library for storing 'Stuff' items
    """

    # Choose a library type name that's unique; e.g. <sector>.DataType
    _LIBRARY_TYPE = 'test.CustomArcticLibType'

    def __init__(self, arctic_lib):
        self._arctic_lib = arctic_lib

        # Arctic_lib gives you a root pymongo.Collection just-for-you:
        # You may store all your data in here ...
        self._collection = arctic_lib.get_top_level_collection()
        # ... or you can create 'sub-collections', e.g.
        self._sub_collection = self._collection.sub_collection

        # The name of this library
        print("My name is %s" % arctic_lib.get_name())

        # Fetch some per-library metadata for this library
        self.some_metadata = arctic_lib.get_library_metadata('some_metadata')

    @classmethod
    def initialize_library(cls, arctic_lib, **kwargs):
        # Persist some per-library metadata in this arctic_lib
        arctic_lib.set_library_metadata('some_metadata', 'some_value')
        CustomArcticLibType(arctic_lib)._ensure_index()

    def _ensure_index(self):
        """
        Index any fields used by your queries.
        """
        collection = self._collection
        # collection.add_indexes
        collection.create_index('field1')

    ###########################################
    # Create your own API below!
    ###########################################

    @mongo_retry
    def query(self, *args, **kwargs):
        """
        Generic query method.

        In reality, your storage class would have its own query methods,

        Performs a Mongo find on the Marketdata index metadata collection.
        See:
        http://api.mongodb.org/python/current/api/pymongo/collection.html
        """
        for x in self._collection.find(*args, **kwargs):
            x['stuff'] = cPickle.loads(x['stuff'])
            del x['_id'] # Remove default unique '_id' field from doc 
            yield Stuff(**x)

    @mongo_retry
    def stats(self):
        """
        Database usage statistics. Used by quota.
        """
        res = {}
        db = self._collection.database
        res['dbstats'] = db.command('dbstats')
        res['data'] = db.command('collstats', self._collection.name)
        res['totals'] = {'count': res['data']['count'],
                         'size': res['data']['size']
                         }
        return res

    @mongo_retry
    def store(self, thing):
        """
        Simple persistence method
        """
        to_store = {'field1': thing.field1,
                    'date_field': thing.date_field,
                    }
        to_store['stuff'] = Binary(cPickle.dumps(thing.stuff))
        # Respect any soft-quota on write - raises if stats().totals.size > quota 
        self._arctic_lib.check_quota()
        self._collection.insert_one(to_store)

    @mongo_retry
    def delete(self, query):
        """
        Simple delete method
        """
        self._collection.delete_one(query)


# Hook the class in for the type string 'CustomArcticLibType'
register_library_type(CustomArcticLibType._LIBRARY_TYPE, CustomArcticLibType)

# Create a Arctic instance pointed at a mongo host
if 'mongo_host' not in globals():
    mongo_host = 'localhost'
store = Arctic(mongo_host)

### Initialize the library
# Map username.custom_lib -> CustomArcticLibType
store.initialize_library('username.custom_lib', CustomArcticLibType._LIBRARY_TYPE)

# Now pull our username.custom_lib ; note that it has the:
#   - query(...)
#   - store(...)
#   - delete(...)
# API we defined above
lib = store['username.custom_lib']


# Store some items in the custom library type
lib.store(Stuff('thing', dt(2012, 1, 1), object()))
lib.store(Stuff('thing2', dt(2013, 1, 1), object()))
lib.store(Stuff('thing3', dt(2014, 1, 1), object()))
lib.store(Stuff(['a', 'b', 'c'], dt(2014, 1, 1), object()))


# Do some querying via our library's query method.
# You would have your own methods for querying here... (which use your index(es), of course)
for e in list(lib.query()): # list everything
    print(e)
list(lib.query({'field1': 'thing'})) # just get by name
list(lib.query({'field1': 'a'}))     # Can query lists
list(lib.query({'field1': 'b'}))
list(lib.query({'date_field': {'$lt': dt(2013, 2, 2)}}))
list(lib.query({'field1':'thing',
                  'date_field': {'$lt': dt(2013, 2, 2)} }))

# Remove everything
lib.delete({})
