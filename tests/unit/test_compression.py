from mock import patch, Mock, sentinel, call
from arctic._compression import compress, compress_array, decompress, decompress_array, enable_parallel_lz4


def test_compress():
    assert len(compress(b'foobar')) > 0


def test_compress_LZ4():
    cfn = Mock()
    with patch('arctic._compression.clz4.compress', cfn):
        compress(b"foo")
        assert cfn.call_count == 1


def test_compressarr():
    assert len(compress_array([b"foobar"*10])) > 0
    assert isinstance(compress_array([b"foobar"*10]), list)


def test_compress_array_usesLZ4():
    cfn = Mock()
    with patch('arctic._compression.clz4.compressarr', cfn):
        compress_array([b"foo"] * 100)
        assert cfn.call_count == 1


def test_compress_array_LZ4_sequential():
    cfn = Mock()
    with patch('arctic._compression.clz4.compress', cfn):
        compress_array([b"foo"] * 49)
        assert cfn.call_count == 49


def test_decompress():
    assert decompress(compress(b"foo")) == b"foo"


def test_decompress_array():
    ll = [('foo%s' % i).encode('ascii') for i in range(100)]
    assert decompress_array(compress_array(ll)) == ll


def test_compression_equal_regardless_parallel_mode():
    a = [b'spam '] * 666
    with patch('arctic._compression.ENABLE_PARALLEL', True):
        parallel = compress_array(a)
    with patch('arctic._compression.ENABLE_PARALLEL', False):
        serial = compress_array(a)
    assert serial == parallel


def test_enable_parallel_lz4():
    enable_parallel_lz4(True)
    from arctic._compression import ENABLE_PARALLEL
    assert(ENABLE_PARALLEL is True)
    enable_parallel_lz4(False)
    from arctic._compression import ENABLE_PARALLEL
    assert(ENABLE_PARALLEL is False)


def test_compress_empty_string():
    assert(decompress(compress(b'')) == b'')
