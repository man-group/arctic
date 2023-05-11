import functools
import hashlib
import logging
import pickle

import numpy as np
import pandas as pd
import pymongo
from bson import Binary
from pandas.compat import pickle_compat
from pymongo.errors import OperationFailure

from arctic._config import FW_POINTERS_REFS_KEY, FW_POINTERS_CONFIG_KEY, FwPointersCfg
from arctic._util import mongo_count, get_fwptr_config


def _split_arrs(array_2d, slices):
    """
    Equivalent to numpy.split(array_2d, slices),
    but avoids fancy indexing
    """
    if len(array_2d) == 0:
        return np.empty(0, dtype=object)

    rtn = np.empty(len(slices) + 1, dtype=object)
    start = 0
    for i, s in enumerate(slices):
        rtn[i] = array_2d[start:s]
        start = s
    rtn[-1] = array_2d[start:]
    return rtn


def checksum(symbol, doc):
    """
    Checksum the passed in dictionary
    """
    sha = hashlib.sha1()
    sha.update(symbol.encode('ascii'))
    for k in sorted(iter(doc.keys()), reverse=True):
        v = doc[k]
        if isinstance(v, bytes):
            sha.update(doc[k])
        else:
            sha.update(str(doc[k]).encode('ascii'))
    return Binary(sha.digest())


def get_symbol_alive_shas(symbol, versions_coll):
    return set(Binary(x) for x in versions_coll.distinct(FW_POINTERS_REFS_KEY, {'symbol': symbol}))


def _cleanup_fw_pointers(collection, symbol, version_ids, versions_coll, shas_to_delete, do_clean=True):
    shas_to_delete = set(shas_to_delete) if shas_to_delete else set()

    if not version_ids or not shas_to_delete:
        return shas_to_delete

    symbol_alive_shas = get_symbol_alive_shas(symbol, versions_coll)

    # This is the set of shas which are not referenced by any FW pointers
    shas_safe_to_delete = shas_to_delete - symbol_alive_shas

    if do_clean and shas_safe_to_delete:
        collection.delete_many({'symbol': symbol, 'sha': {'$in': list(shas_safe_to_delete)}})

    return shas_safe_to_delete


def _cleanup_parent_pointers(collection, symbol, version_ids):
    for v in version_ids:
        # Remove all documents which only contain the parent
        collection.delete_many({'symbol': symbol,
                               'parent': [v]})
        # Pull the parent from the parents field
        collection.update_many({'symbol': symbol,
                                'parent': v},
                               {'$pull': {'parent': v}})

    # Now remove all chunks which aren't parented - this is unlikely, as they will
    # have been removed by the above
    collection.delete_one({'symbol': symbol, 'parent': []})


def _cleanup_mixed(symbol, collection, version_ids, versions_coll):
    # Pull the deleted version IDs from the the parents field
    collection.update_many({'symbol': symbol, 'parent': {'$in': version_ids}}, {'$pullAll': {'parent': version_ids}})

    # All-inclusive set of segments which are pointed by at least one version (SHA fw pointers)
    symbol_alive_shas = get_symbol_alive_shas(symbol, versions_coll)

    spec = {'symbol': symbol, 'parent': []}
    if symbol_alive_shas:
        # This query unfortunately, while it hits the index (symbol, sha) to find the documents, in order to filter
        # the documents by "parent: []" it fetches at server side, and pollutes the cache of WiredTiger
        # TODO: add a new index for segments collection: (symbol, sha, parent)
        spec['sha'] = {'$nin': list(symbol_alive_shas)}
    collection.delete_many(spec)


def _get_symbol_pointer_cfgs(symbol, versions_coll):
    return set(get_fwptr_config(v)
               for v in versions_coll.find({'symbol': symbol}, projection={FW_POINTERS_CONFIG_KEY: 1}))


def cleanup(arctic_lib, symbol, version_ids, versions_coll, shas_to_delete=None, pointers_cfgs=None):
    """
    Helper method for cleaning up chunks from a version store
    """
    pointers_cfgs = set(pointers_cfgs) if pointers_cfgs else set()
    collection = arctic_lib.get_top_level_collection()
    version_ids = list(version_ids)

    # Iterate versions to check if they are created only with fw pointers, parent pointers (old), or mixed
    # Keep in mind that the version is not yet inserted.
    all_symbol_pointers_cfgs = _get_symbol_pointer_cfgs(symbol, versions_coll)
    all_symbol_pointers_cfgs.update(pointers_cfgs)

    # All the versions of the symbol have been created with old arctic or with disabled forward pointers.
    # Preserves backwards compatibility and regression for old pointers implementation.
    if all_symbol_pointers_cfgs == {FwPointersCfg.DISABLED} or not all_symbol_pointers_cfgs:
        _cleanup_parent_pointers(collection, symbol, version_ids)
        return

    # All the versions of the symbol we wish to delete have been created with forward pointers
    if FwPointersCfg.DISABLED not in all_symbol_pointers_cfgs:
        _cleanup_fw_pointers(collection, symbol, version_ids, versions_coll,
                             shas_to_delete=shas_to_delete, do_clean=True)
        return

    # Reaching here means the symbol has versions with mixed forward pointers and legacy/parent pointer configurations
    _cleanup_mixed(symbol, collection, version_ids, versions_coll)


def version_base_or_id(version):
    return version.get('base_version_id', version['_id'])


def _define_compat_pickle_load():
    """Factory function to initialise the correct Pickle load function based on
    the Pandas version.
    """
    if pd.__version__.startswith("0.14"):
        return pickle.load
    return pickle_compat.load


def analyze_symbol(instance, sym, from_ver, to_ver, do_reads=False):
    """
    This is a utility function to produce text output with details about the versions of a given symbol.
    It is useful for debugging corruption issues and to mark corrupted versions.
    Parameters
    ----------
    instance : `arctic.store.version_store.VersionStore`
        The VersionStore instance against which the analysis will be run.
    sym : `str`
        The symbol to analyze
    from_ver : `int` or `None`
        The lower bound for the version number we wish to analyze. If None then start from the earliest version.
    to_ver : `int` or `None`
        The upper bound for the version number we wish to analyze. If None then stop at the latest version.
    do_reads : `bool`
        If this flag is set to true, then the corruption check will actually try to read the symbol (slower).
    """
    logging.info('Analyzing symbol {}. Versions range is [v{}, v{}]'.format(sym, from_ver, to_ver))
    prev_rows = 0
    prev_n = 0
    prev_v = None

    logging.info('\nVersions for {}:'.format(sym))
    for v in instance._versions.find({'symbol': sym, 'version': {'$gte': from_ver, '$lte': to_ver}},
                                     sort=[('version', pymongo.ASCENDING)]):
        n = v.get('version')

        is_deleted = v.get('metadata').get('deleted', False) if v.get('metadata') else False

        if is_deleted:
            matching = 0
        else:
            spec = {'symbol': sym, 'parent': v.get('base_version_id', v['_id']), 'segment': {'$lt': v.get('up_to', 0)}}
            matching = mongo_count(instance._collection, filter=spec) if not is_deleted else 0

        base_id = v.get('base_version_id')
        snaps = ['/'.join((str(x), str(x.generation_time))) for x in v.get('parent')] if v.get('parent') else None

        added_rows = v.get('up_to', 0) - prev_rows

        meta_match_with_prev = v.get('metadata') == prev_v.get('metadata') if prev_v else False

        delta_snap_creation = (min([x.generation_time for x in v.get('parent')]) - v['_id'].generation_time).total_seconds() / 60.0 if v.get('parent') else 0.0

        prev_v_diff = 0 if not prev_v else v['version'] - prev_v['version']

        corrupted = not is_deleted and (is_corrupted(instance, sym, v) if do_reads else fast_is_corrupted(instance, sym, v))

        logging.info(
            "v{: <6} "
            "{: <6} "
            "{: <5} "
            "({: <20}):   "
            "expected={: <6} "
            "found={: <6} "
            "last_row={: <10} "
            "new_rows={: <10} "
            "append count={: <10} "
            "append_size={: <10} "
            "type={: <14} {: <14} "
            "base={: <24}/{: <28} "
            "snap={: <30}[{:.1f} mins delayed] "
            "{: <20} "
            "{: <20}".format(
                n,
                prev_v_diff,
                'DEL' if is_deleted else 'ALIVE',
                str(v['_id'].generation_time),
                v.get('segment_count', 0),
                matching,
                v.get('up_to', 0),
                added_rows,
                v.get('append_count'),
                v.get('append_size'),
                v.get('type'),
                'meta-same' if meta_match_with_prev else 'meta-changed',
                str(base_id),
                str(base_id.generation_time) if base_id else '',
                str(snaps),
                delta_snap_creation,
                'PREV_MISSING' if prev_n < n - 1 else '',
                'CORRUPTED VERSION' if corrupted else '')
        )
        prev_rows = v.get('up_to', 0)
        prev_n = n
        prev_v = v

    logging.info('\nSegments for {}:'.format(sym))
    for seg in instance._collection.find({'symbol': sym}, sort=[('_id', pymongo.ASCENDING)]):
        logging.info("{: <32}  {: <7}  {: <10} {: <30}".format(
            hashlib.sha1(seg['sha']).hexdigest(),
            seg.get('segment'),
            'compressed' if seg.get('compressed', False) else 'raw',
            str([str(p) for p in seg.get('parent', [])])
        ))


def _fast_check_corruption(collection, sym, v, check_count, check_last_segment, check_append_safe):
    if v is None:
        logging.warning("Symbol {} with version {} not found, so can't be corrupted.".format(sym, v))
        return False

    if not check_count and not check_last_segment:
        raise ValueError("_fast_check_corruption must be called with either of "
                         "check_count and check_last_segment set to True")

    # If version marked symbol as deleted, it will force writes/appends to start from a new base: non corrupted.
    if isinstance(v.get('metadata'), dict) and v['metadata'].get('deleted'):
        return False

    if check_append_safe:
        # Check whether appending to the symbol version can potentially corrupt the data (history branch).
        # Inspect all segments, don't limit to v['up_to']. No newer append segments after v should exist.
        spec = {'symbol': sym, 'parent': v.get('base_version_id', v['_id'])}
    else:
        # Only verify segment count for current symbol version, don't check corruptability of future appends.
        spec = {'symbol': sym, 'parent': v.get('base_version_id', v['_id']), 'segment': {'$lt': v['up_to']}}

    try:
        # Not that commands sequence (a) is slower than (b)
        # (a) curs = collection.find(spec, {'segment': 1}, sort=[('segment', pymongo.DESCENDING)])
        #     curs.count()
        #     curs.next()
        # (b) collection.find(spec, {'segment': 1}).count()
        #     collection.find_one(spec, {'segment': 1}, sort=[('segment', pymongo.DESCENDING)])

        if check_count:
            total_segments = mongo_count(collection, filter=spec)
            # Quick check: compare segment count
            if total_segments != v.get('segment_count', 0):
                return True  # corrupted, don't proceed with fetching from mongo the first hit
            # Quick check: Segment counts agree and size is zero
            if total_segments == 0:
                return False

        if check_last_segment:
            # Quick check: compare the maximum segment's up_to number. It has to verify the version's up_to.
            max_seg = collection.find_one(spec, {'segment': 1}, sort=[('segment', pymongo.DESCENDING)])
            max_seg = max_seg['segment'] + 1 if max_seg else 0
            if max_seg != v.get('up_to'):
                return True  # corrupted, last segment and version's up_to don't agree
    except OperationFailure as e:
        logging.warning("Corruption checks are skipped (sym={}, version={}): {}".format(sym, v['version'], str(e)))

    return False


def is_safe_to_append(instance, sym, input_v):
    """
    This method hints whether the symbol/version are safe for appending in two ways:
    1. It verifies whether the symbol is already corrupted (fast, doesn't read the data)
    2. It verifies that the symbol is safe to append, i.e. there are no subsequent appends,
       or dangling segments from a failed append.
    Parameters
    ----------
    instance : `arctic.store.version_store.VersionStore`
        The VersionStore instance against which the analysis will be run.
    sym : `str`
        The symbol to test if is corrupted.
    input_v : `int` or `arctic.store.version_store.VersionedItem`
        The specific version we wish to test if is appendable. This argument is mandatory.

    Returns
    -------
    `bool`
        True if the symbol is safe to append, False otherwise.
    """
    input_v = instance._versions.find_one({'symbol': sym, 'version': input_v}) if isinstance(input_v, int) else input_v
    return not _fast_check_corruption(instance._collection, sym, input_v,
                                      check_count=True, check_last_segment=True, check_append_safe=True)


def fast_is_corrupted(instance, sym, input_v):
    """
    This method can be used for a fast check (not involving a read) for a corrupted version.
    Users can't trust this as may give false negatives, but it this returns True, then symbol is certainly broken (no false positives)
    Parameters
    ----------
    instance : `arctic.store.version_store.VersionStore`
        The VersionStore instance against which the analysis will be run.
    sym : `str`
        The symbol to test if is corrupted.
    input_v : `int` or `arctic.store.version_store.VersionedItem`
        The specific version we wish to test if is corrupted. This argument is mandatory.

    Returns
    -------
    `bool`
        True if the symbol is found corrupted, False otherwise.
    """
    input_v = instance._versions.find_one({'symbol': sym, 'version': input_v}) if isinstance(input_v, int) else input_v
    return _fast_check_corruption(instance._collection, sym, input_v,
                                  check_count=True, check_last_segment=True, check_append_safe=False)


def is_corrupted(instance, sym, input_v):
    """
        This method can be used to check for a corrupted version.
        Will continue to a full read (slower) if the internally invoked fast-detection does not locate a corruption.

        Parameters
        ----------
        instance : `arctic.store.version_store.VersionStore`
            The VersionStore instance against which the analysis will be run.
        sym : `str`
            The symbol to test if is corrupted.
        input_v : `int` or `arctic.store.version_store.VersionedItem`
            The specific version we wish to test if is corrupted. This argument is mandatory.

        Returns
        -------
        `bool`
            True if the symbol is found corrupted, False otherwise.
        """
    # If version is just a number, read the version document
    input_v = instance._versions.find_one({'symbol': sym, 'version': input_v}) if isinstance(input_v, int) else input_v
    if not _fast_check_corruption(instance._collection, sym, input_v,
                                  check_count=True, check_last_segment=True, check_append_safe=False):
        try:
            # Done with the fast checks, proceed to a full read if instructed
            instance.read(sym, as_of=input_v['version'])
            return False
        except Exception:
            pass
    return True


# Initialise the pickle load function and delete the factory function.
pickle_compat_load = _define_compat_pickle_load()
del _define_compat_pickle_load
