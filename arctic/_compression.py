import logging
from multiprocessing.pool import ThreadPool

try:
    from lz4.block import compress as lz4_compress, decompress as lz4_decompress
    lz4_compressHC = lambda _str: lz4_compress(_str, mode='high_compression')
except ImportError as e:
    from lz4 import compress as lz4_compress, compressHC as lz4_compressHC, decompress as lz4_decompress

# ENABLE_PARALLEL mutated in global_scope. Do not remove.
from ._config import ENABLE_PARALLEL, LZ4_HIGH_COMPRESSION, LZ4_WORKERS, LZ4_N_PARALLEL, LZ4_MINSZ_PARALLEL, \
    BENCHMARK_MODE  # noqa # pylint: disable=unused-import

logger = logging.getLogger(__name__)


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
    logger.info("Setting parallelisation mode to {}".format("multi-threaded" if mode else "single-threaded"))


def set_compression_pool_size(pool_size):
    """
    Set the size of the compression workers thread pool.
    If the pool is already created, it waits until all jobs are finished, and then proceeds with setting the new size.

    Parameters
    ----------
        pool_size : `int`
            The size of the pool (must be a positive integer)

    Returns
    -------
    `None`
    """
    pool_size = int(pool_size)
    if pool_size < 1:
        raise ValueError("The compression thread pool size cannot be of size {}".format(pool_size))

    global _compress_thread_pool
    if _compress_thread_pool is not None:
        _compress_thread_pool.close()
        _compress_thread_pool.join()
    _compress_thread_pool = ThreadPool(pool_size)


def compress_array(str_list, withHC=LZ4_HIGH_COMPRESSION):
    """
    Compress an array of strings

    Parameters
    ----------
        str_list: `list[str]`
            The input list of strings which need to be compressed.
        withHC: `bool`
            This flag controls whether lz4HC will be used.

    Returns
    -------
    `list[str`
    The list of the compressed strings.
    """
    global _compress_thread_pool

    if not str_list:
        return str_list

    do_compress = lz4_compressHC if withHC else lz4_compress

    def can_parallelize_strlist(strlist):
        return len(strlist) > LZ4_N_PARALLEL and len(strlist[0]) > LZ4_MINSZ_PARALLEL

    use_parallel = (ENABLE_PARALLEL and withHC) or can_parallelize_strlist(str_list)

    if BENCHMARK_MODE or use_parallel:
        if _compress_thread_pool is None:
            _compress_thread_pool = ThreadPool(LZ4_WORKERS)
        return _compress_thread_pool.map(do_compress, str_list)

    return [do_compress(s) for s in str_list]


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
    return lz4_compressHC(_str)


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
    global _compress_thread_pool

    if not str_list:
        return str_list

    if not ENABLE_PARALLEL or len(str_list) <= LZ4_N_PARALLEL:
        return [lz4_decompress(chunk) for chunk in str_list]

    if _compress_thread_pool is None:
        _compress_thread_pool = ThreadPool(LZ4_WORKERS)
    return _compress_thread_pool.map(lz4_decompress, str_list)
