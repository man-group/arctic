"""
Helper functions that are not 'core' to chunkstore
"""


def read_apply(lib, symbol, func, chunk_range=None):
    """
    Apply `func` to each chunk in lib.symbol

    Parameters
    ----------
    lib: arctic library
    symbol: str
        the symbol for the given item in the DB
    chunk_range: None, or a range object
        allows you to subset the chunks by range

    Returns
    -------
    generator
    """
    for chunk in lib.iterator(symbol, chunk_range=chunk_range):
        yield func(chunk)
