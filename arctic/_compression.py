import os
import logging
from multiprocessing.pool import ThreadPool

from lz4.block import compress as lz4_compress, decompress as lz4_decompress

logger = logging.getLogger(__name__)

# switch to parallel LZ4 compress (and potentially other parallel stuff), Default True
ENABLE_PARALLEL = not os.environ.get('DISABLE_PARALLEL')
LZ4_N_PARALLEL = os.environ.get('LZ4_N_PARALLEL', 50)  # No. of elements to use parallel compression in LZ4 mode
LZ4_WORKERS = os.environ.get('COMPRESSION_WORKERS', 4)

_compress_thread_pool = None


def enable_parallel_lz4(mode):
    """
    Set the global multithread compression mode

    Parameters
    ----------
        mode: `bool`
            True: Use parallel compression. False: Use sequential compression
    """
    global ENABLE_PARALLEL
    ENABLE_PARALLEL = bool(mode)
    logger.info("Setting parallelisation mode to {}".format("multithread" if mode else "singlethread"))


def compress_array(str_list, withHC=False):
    """
    Compress an array of strings
    """
    if not str_list:
        return str_list

    if not ENABLE_PARALLEL or len(str_list) <= LZ4_N_PARALLEL:
        # Less than 50 chunks its quicker to compress sequentially..
        return [lz4_compress(s, mode='high_compression' if withHC else 'default') for s in str_list]
    
    global _compress_thread_pool
    if not _compress_thread_pool:
        _compress_thread_pool = ThreadPool(LZ4_WORKERS)
    
    return _compress_thread_pool.map(lz4_compress, str_list)
    

def compress(_str):
    """
    Compress a string

    By default LZ4 mode is standard in interactive mode,
    and high compresion in applications/scripts
    """
    return lz4_compress(_str)


def compressHC(_str):
    """
    HC compression
    """
    return lz4_compress(_str, mode='high_compression')


def compressHC_array(str_list):
    """
    HC compression
    """
    return compress_array(str_list, withHC=True)


def decompress(_str):
    """
    Decompress a string
    """
    return lz4_decompress(_str)


def decompress_array(str_list):
    """
    Decompress a list of strings
    """
    if not str_list:
        return str_list

    if not ENABLE_PARALLEL or len(str_list) <= LZ4_N_PARALLEL:
        return [lz4_decompress(chunk) for chunk in str_list]

    return _compress_thread_pool.map(lz4_decompress, str_list)
