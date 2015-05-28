from .logging import logger
import _compress as clz4


USE_LZ4HC = True  # switch to use LZ4HC. Default True
LZ4HC_N_PARALLEL = 5  # No. of elements to use parellel compression in LZ4HC mode
LZ4_N_PARALLEL = 50  # No. of elements to use parellel compression in LZ4 mode


def use_lz4hc(mode):
    """
    Set the global LZ4HC mode

    Parameters
    ----------
        mode: `bool`
            True: Use LZ4HC False: Use LZ4
    """
    global USE_LZ4HC
    USE_LZ4HC = mode
    logger.info("Setting compression mode to %s" % ("LZ4HC" if mode else "LZ4 (no HC)"))


def _should_use_lz4hc():
    return USE_LZ4HC


def _is_interactive_mode():
    # http://stackoverflow.com/questions/2356399/tell-if-python-is-in-interactive-mode
    # currently unused - but could in-future flip to LZ4 if in interactive mode
    import __main__ as main
    return not hasattr(main, '__file__')


def compress_array(str_list):
    """
    Compress an array of strings

    By default LZ4 mode is standard in interactive mode,
    and high compresion in applications/scripts
    """
    if _should_use_lz4hc():
        # Less than 5 chunks its quicker to compress sequentially..
        if len(str_list) > LZ4HC_N_PARALLEL:
            return clz4.compressarrHC(str_list)
        else:
            return [clz4.compressHC(s) for s in str_list]
    else:
        # Less than 50 chunks its quicker to compress sequentially..
        if len(str_list) > LZ4_N_PARALLEL:
            return clz4.compressarr(str_list)
        else:
            return [clz4.compress(s) for s in str_list]


def compress(_str):
    """
    Compress a string

    By default LZ4 mode is standard in interactive mode,
    and high compresion in applications/scripts
    """
    compressfn = clz4.compressHC if _should_use_lz4hc() else clz4.compress
    return compressfn(_str)


def decompress(_str):
    """
    Decompress a string
    """
    return clz4.decompress(_str)


def decompress_array(str_list):
    """
    Decompress a list of strings
    """
    return clz4.decompressarr(str_list)
