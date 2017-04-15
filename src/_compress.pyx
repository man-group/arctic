# cython: profile=True

#
# LZ4 code was copied from: https://github.com/steeve/python-lz4/ r8ac9cf9df8fb8d51f40a3065fa538f8df1c8a62a 22/4/2015 [tt]
#

cdef extern from "lz4.h":
    cdef int LZ4_compress(char* source, char* dest, int inputSize) nogil
    cdef int LZ4_compressBound(int isize) nogil
    cdef int LZ4_decompress_safe(const char* source, char* dest, int compressedSize, int maxOutputSize) nogil

cdef extern from "lz4hc.h":
    cdef int LZ4_compressHC(char* source, char* dest, int inputSize) nogil

cimport cython
cimport cpython
cimport libc.stdio
cimport openmp

from libc.stdlib cimport malloc, free, realloc
ctypedef unsigned char  uint8_t
ctypedef unsigned int   uint32_t

from libc.stdio cimport printf
from cython.view cimport array as cvarray
from cython.parallel import prange
from cython.parallel import threadid
from cython.parallel cimport parallel

cdef void store_le32(char *c, uint32_t x) nogil:
    c[0] = x & 0xff
    c[1] = (x >> 8) & 0xff
    c[2] = (x >> 16) & 0xff
    c[3] = (x >> 24) & 0xff

cdef uint32_t load_le32(char *c) nogil:
    cdef uint8_t *d = <uint8_t *>c
    return d[0] | (d[1] << 8) | (d[2] << 16) | (d[3] << 24)


cdef int hdr_size = sizeof(uint32_t)

cdef char ** to_cstring_array(list_str):
    """ Convert a python string list to a **char 
        Note: Performs a malloc. You must free the array once created.
    """ 
    cdef char **ret = <char **>malloc(len(list_str) * sizeof(char *))
    for i in xrange(len(list_str)):
        ret[i] = list_str[i]
    return ret


@cython.boundscheck(False)
@cython.wraparound(False)
@cython.nonecheck(False)
@cython.cdivision(True)
def compress(pString):
    return _compress(pString, LZ4_compress)


@cython.boundscheck(False)
@cython.wraparound(False)
@cython.nonecheck(False)
@cython.cdivision(True)
def compressHC(pString):
    return _compress(pString, LZ4_compressHC)


cdef _compress(pString, int (*Fnptr_LZ4_compress)(const char *, char *, int)):
    # sizes
    cdef uint32_t compressed_size
    cdef uint32_t original_size = len(pString)

    # buffers
    cdef char *cString =  pString
    cdef char *result     # destination buffer
    cdef bytes pyResult   # python wrapped result

    # calc. estaimted compresed size
    compressed_size = LZ4_compressBound(original_size)
    # alloc memory
    result = <char*>malloc(compressed_size + hdr_size)
    # store original size
    store_le32(result, original_size);
    # compress & update size
    compressed_size = Fnptr_LZ4_compress(cString, result + hdr_size, original_size)
    # cast back into a python sstring
    pyResult = result[:compressed_size + hdr_size]

    free(result)

    return pyResult


@cython.boundscheck(False)
@cython.wraparound(False)
@cython.nonecheck(False)
@cython.cdivision(True)
def decompress(pString):

    # sizes
    cdef uint32_t compressed_size = len(pString)
    cdef uint32_t original_size

    # buffers
    cdef char *cString    # *char pStr
    cdef char *result     # destination buffer
    cdef bytes pyResult   # python wrapped result
    cdef int ret

    # convert to char*
    cString = pString
    # find original size
    original_size = <uint32_t>load_le32(cString)
    # malloc 
    result = <char*>malloc(original_size)
    # decompress
    ret = LZ4_decompress_safe(cString + hdr_size, result, compressed_size - hdr_size, original_size)
    if ret != original_size:
        free(result)
        raise Exception("Error decompressing")
    # cast back into python string
    pyResult = result[:original_size]

    free(result)
    return pyResult


@cython.boundscheck(False)
@cython.wraparound(False)
@cython.nonecheck(False)
@cython.cdivision(True)
def compressarr(pStrList):
    return _compressarr(pStrList, LZ4_compress)

@cython.boundscheck(False)
@cython.wraparound(False)
@cython.nonecheck(False)
@cython.cdivision(True)
def compressarrHC(pStrList):
    return _compressarr(pStrList, LZ4_compressHC)


cdef _compressarr(pStrList, int (*Fnptr_LZ4_compress)(const char *, char *, int) nogil):
    
    if len(pStrList) == 0:
        return []

    cdef char **cStrList = to_cstring_array(pStrList)
    cdef Py_ssize_t n = len(pStrList)

    # loop parameters
    cdef char *cString
    cdef int original_size
    cdef uint32_t compressed_size
    cdef char *result
    cdef Py_ssize_t i

    # output parameters
    cdef char **cResult = <char **>malloc(n * sizeof(char *))
    cdef int[:] lengths = cvarray(shape=(n,), itemsize=sizeof(int), format="i")
    cdef int[:] orilengths = cvarray(shape=(n,), itemsize=sizeof(int), format="i")
    cdef bytes pyResult

    # store original string lengths
    for i in range(n):
        orilengths[i] = len(pStrList[i])

    with nogil, parallel():
        for i in prange(n, schedule='static'):
            cString = cStrList[i]
            original_size = orilengths[i]
            # calc. estaimted compresed size
            compressed_size = LZ4_compressBound(original_size)
            # alloc memory
            result = <char*>malloc(compressed_size + hdr_size)
            # store original size
            store_le32(result, original_size)
            # compress & update size
            compressed_size = Fnptr_LZ4_compress(cString, result + hdr_size, original_size)
            # assign to result
            lengths[i] = compressed_size + hdr_size
            cResult[i] = result

    # cast back to python
    result_list = []
    for i in range(n):
        pyResult = cResult[i][:lengths[i]]
        free(cResult[i])
        result_list.append(pyResult)

    free(cResult)
    free(cStrList)

    return result_list


@cython.boundscheck(False)
@cython.wraparound(False)
@cython.nonecheck(False)
@cython.cdivision(True)
def decompressarr(pStrList):
    
    if len(pStrList) == 0:
        return []

    cdef char **cStrList = to_cstring_array(pStrList)
    cdef Py_ssize_t n = len(pStrList)

    # loop parameters
    cdef char *cString
    cdef uint32_t original_size
    cdef uint32_t compressed_size
    cdef char *result
    cdef Py_ssize_t i
    cdef int ret
    cdef int error = 0

    # output parameters
    cdef char **cResult = <char **>malloc(n * sizeof(char *))
    cdef int[:] clengths = cvarray(shape=(n,), itemsize=sizeof(int), format="i")
    cdef int[:] lengths = cvarray(shape=(n,), itemsize=sizeof(int), format="i")
    cdef bytes pyResult

    for i in range(n):
        clengths[i] = len(pStrList[i])

    with nogil, parallel():
        for i in prange(n, schedule='static'):
            cString = cStrList[i]
            # get compressed size
            compressed_size = clengths[i]
            # find original size
            original_size = <uint32_t>load_le32(cString)
            # malloc 
            result = <char*>malloc(original_size)
            # decompress
            ret = LZ4_decompress_safe(cString + hdr_size, result, compressed_size - hdr_size, original_size)
            if ret <= 0 or ret != original_size:
                error = -1
            # assign to result
            cResult[i] = result
            lengths[i] = original_size

    # cast back to python
    result_list = []
    for i in range(n):
        pyResult = cResult[i][:lengths[i]]
        free(cResult[i])
        result_list.append(pyResult)

    free(cResult)
    free(cStrList)

    if error == -1:
        raise Exception("Error decompressing array")

    return result_list
