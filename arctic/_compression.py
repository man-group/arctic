import os
import logging
from . import _compress as clz4


logger = logging.getLogger(__name__)

# switch to parallel LZ4 compress (and potentially other parallel stuff), Default True
ENABLE_PARALLEL = not os.environ.get('DISABLE_PARALLEL')
LZ4_N_PARALLEL = 50  # No. of elements to use parellel compression in LZ4 mode


def enable_parallel_lz4(mode):
    """
    Set the global multithread compression mode

    Parameters
    ----------
        mode: `bool`
            True: Use parallel compression. False: Use sequential compression
    """
    global ENABLE_PARALLEL
    ENABLE_PARALLEL = mode
    logger.info("Setting parallelisation mode to {}".format("multithread" if mode else "singlethread"))


def compress_array(str_list):
    """
    Compress an array of strings
    """
    if not ENABLE_PARALLEL:
        return [clz4.compress(s) for s in str_list]

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
    return clz4.compress(_str)


def decompress(_str):
    """
    Decompress a string
    """
    return clz4.decompress(_str)


def decompress_array(str_list):
    """
    Decompress a list of strings
    """
    if ENABLE_PARALLEL:
        return clz4.decompressarr(str_list)
    return [clz4.decompress(chunk) for chunk in str_list]


def compressHC(_str):
    """
    HC compression
    """
    return clz4.compressHC(_str)

