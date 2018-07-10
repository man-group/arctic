import functools
import hashlib
import logging
import pickle
import six

import numpy as np
import pandas as pd
import pymongo
from bson import Binary
from pandas.compat import pickle_compat
from pymongo.errors import OperationFailure


def _split_arrs(array_2d, slices):
    """
    Equivalent to numpy.split(array_2d, slices),
    but avoids fancy indexing
    """
    if len(array_2d) == 0:
        return np.empty(0, dtype=np.object)

    rtn = np.empty(len(slices) + 1, dtype=np.object)
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
        if isinstance(v, six.binary_type):
            sha.update(doc[k])
        else:
            sha.update(str(doc[k]).encode('ascii'))
    return Binary(sha.digest())


def cleanup(arctic_lib, symbol, version_ids):
    """
    Helper method for cleaning up chunks from a version store
    """
    collection = arctic_lib.get_top_level_collection()

    # Remove any chunks which contain just the parents, at the outset
    # We do this here, because $pullALL will make an empty array: []
    # and the index which contains the parents field will fail the unique constraint.
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
    collection.delete_one({'symbol':  symbol, 'parent': []})


def version_base_or_id(version):
    return version.get('base_version_id', version['_id'])


def _define_compat_pickle_load():
    """Factory function to initialise the correct Pickle load function based on
    the Pandas version.
    """
    if pd.__version__.startswith("0.14"):
        return pickle.load
    return functools.partial(pickle_compat.load, compat=True)


def analyze_symbol(l, sym, from_ver, to_ver, do_reads=False):
    """
    This is a utility function to produce text output with details about the versions of a given symbol.
    It is useful for debugging corruption issues and to mark corrupted versions.
    Parameters
    ----------
    l : `arctic.store.version_store.VersionStore`
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
    for v in l._versions.find({'symbol': sym, 'version': {'$gte': from_ver, '$lte': to_ver}},
                              sort=[('version', pymongo.ASCENDING)]):
        n = v.get('version')

        is_deleted = v.get('metadata').get('deleted', False) if v.get('metadata') else False

        if is_deleted:
            matching = 0
        else:
            spec = {'symbol': sym, 'parent': v.get('base_version_id', v['_id']), 'segment': {'$lt': v.get('up_to', 0)}}
            matching = l._collection.find(spec).count() if not is_deleted else 0

        base_id = v.get('base_version_id')
        snaps = ['/'.join((str(x), str(x.generation_time))) for x in v.get('parent')] if v.get('parent') else None

        added_rows = v.get('up_to', 0) - prev_rows

        meta_match_with_prev = v.get('metadata') == prev_v.get('metadata') if prev_v else False

        delta_snap_creation = (min([x.generation_time for x in v.get('parent')]) - v['_id'].generation_time).total_seconds() / 60.0 if v.get('parent') else 0.0

        prev_v_diff = 0 if not prev_v else v['version'] - prev_v['version']

        corrupted = not is_deleted and (is_corrupted(l, sym, v) if do_reads else fast_is_corrupted(l, sym, v))

        logging.info(
            "v{: <6} {: <6} {: <5} ({: <20}):   expected={: <6} found={: <6} last_row={: <10} new_rows={: <10} append count={: <10} append_size={: <10} type={: <14} {: <14} base={: <24}/{: <28} snap={: <30}[{:.1f} mins delayed] {: <20} {: <20}".format(
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
                snaps,
                delta_snap_creation,
                'PREV_MISSING' if prev_n < n - 1 else '',
                'CORRUPTED VERSION' if corrupted else '')
            )
        prev_rows = v.get('up_to', 0)
        prev_n = n
        prev_v = v

    logging.info('\nSegments for {}:'.format(sym))
    for seg in l._collection.find({'symbol': sym}, sort=[('_id', pymongo.ASCENDING)]):
        logging.info("{: <32}  {: <7}  {: <10} {: <30}".format(
            hashlib.md5(seg['sha']).hexdigest(),
            seg.get('segment'),
            'compressed' if seg.get('compressed', False) else 'raw',
            [str(p) for p in seg.get('parent', [])]
        ))


def _fast_check_corruption(collection, sym, v, check_count=True, check_last_segment=True, check_append_safe=False):
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
            total_segments = collection.find(spec, {'segment': 1}).count()
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
        logging.warning("Corruption checks are skipped (sym={}, version={}): {}", sym, v['version'], str(e))

    return False


def is_safe_to_append(l, sym, input_v):
    """
    This method hints whether the symbol/version are safe for appending in two ways:
    1. It verifies whether the symbol is already corrupted (fast, doesn't read the data)
    2. It verififes that the symbol is safe to append, i.e. there are no subsequent appends,
       or dangling segments from a failed append.
    Parameters
    ----------
    l : `arctic.store.version_store.VersionStore`
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
    input_v = l._versions.find_one({'symbol': sym, 'version': input_v}) if isinstance(input_v, int) else input_v
    return not _fast_check_corruption(l._collection, sym, input_v, check_append_safe=True)


def fast_is_corrupted(l, sym, input_v):
    """
    This method can be used for a fast check (not involving a read) for a corrupted version.
    Users can't trust this as may give false negatives, but it this returns True, then symbol is certainly broken (no false positives)
    Parameters
    ----------
    l : `arctic.store.version_store.VersionStore`
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
    input_v = l._versions.find_one({'symbol': sym, 'version': input_v}) if isinstance(input_v, int) else input_v
    return _fast_check_corruption(l._collection, sym, input_v)


def is_corrupted(l, sym, input_v):
    """
        This method can be used to check for a corrupted version.
        Will resort to a regular read (slower) if the internally invoked fast-detection gives hint for a corruption.

        Parameters
        ----------
        l : `arctic.store.version_store.VersionStore`
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
    input_v = l._versions.find_one({'symbol': sym, 'version': input_v}) if isinstance(input_v, int) else input_v
    if not _fast_check_corruption(l._collection, sym, input_v):
        try:
            # Done with the fast checks, proceed to a full read if instructed
            l.read(sym, as_of=input_v['version'])
            return False
        except Exception:
            pass
    return True





# Initialise the pickle load function and delete the factory function.
pickle_compat_load = _define_compat_pickle_load()
del _define_compat_pickle_load
