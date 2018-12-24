from itertools import groupby

import pymongo

from arctic.chunkstore.chunkstore import SYMBOL, SEGMENT, START


def segment_id_repair(library, symbol=None):
    """
    Ensure that symbol(s) have contiguous segment ids

    Parameters
    ----------
    library: arctic library
    symbol: None, str, list of str
        None: all symbols
        str: single symbol
        list: list of symbols

    Returns
    -------
    list of str - Symbols 'fixed'
    """
    ret = []

    if symbol is None:
        symbol = library.list_symbols()
    elif not isinstance(symbol, list):
        symbol = [symbol]

    by_segment = [(START, pymongo.ASCENDING),
                  (SEGMENT, pymongo.ASCENDING)]

    for sym in symbol:
        cursor = library._collection.find({SYMBOL: sym}, sort=by_segment)
        # group by chunk
        for _, segments in groupby(cursor, key=lambda x: (x[START], x[SYMBOL])):
            segments = list(segments)
            # if the start segment is not 0, we need to fix this symbol
            if segments[0][SEGMENT] == -1:
                # since the segment is part of the index, we have to clean up first
                library._collection.delete_many({SYMBOL: sym, START: segments[0][START]})
                # map each segment in the interval to the correct segment
                for index, seg in enumerate(segments):
                    seg[SEGMENT] = index
                library._collection.insert_many(segments)
                ret.append(sym)

    return ret
