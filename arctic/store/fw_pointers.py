WITH_ID = 'fw_pointers_with_id'
WITH_SHA = 'fw_pointers_with_sha'
LEGACY = 'legacy'


def get_fw_pointers_type(version):
    fw_pointers_type = LEGACY
    if WITH_ID in version:
        fw_pointers_type = WITH_ID
    elif WITH_SHA in version:
        fw_pointers_type = WITH_SHA
    return fw_pointers_type


from collections import namedtuple

IndexSpec = namedtuple('IndexSpec', 'keys unique background')


def do_create_index(collection, index_spec):
    """
    :type index_spec: IndexSpec
    :type collection: pymongo.collection.Collection
    """
    collection.create_index(keys=index_spec.keys, unique=index_spec.unique, background=index_spec.background)


def do_drop_index(collection, index_spec):
    """
    :type index_spec: IndexSpec
    :type collection: pymongo.collection.Collection
    """
    matched = None
    for idx_name, idx_rec in collection.index_information().iteritems():
        if index_spec.keys == idx_rec.get('key') and \
                index_spec.unique == idx_rec.get('unique') and \
                index_spec.background == idx_rec.get('background'):
            matched = idx_name
            break
    if matched:
        collection.drop_index(matched)
