from mock import patch, Mock, sentinel, call
from arctic._compression import compress, compress_array, decompress, decompress_array
import lz4


def test_compress():
    assert len(compress("foobar")) > 0



def test_compress_LZ4():
    cfn = Mock()
    with patch('arctic._compression.clz4.compress', cfn):
        compress("foo")
        assert cfn.call_count == 1


def test_compressarr():
    assert len(compress_array(["foobar"*10])) > 0
    assert isinstance(compress_array(["foobar"*10]), list)


def test_compress_array_usesLZ4():
    cfn = Mock()
    with patch('arctic._compression.clz4.compressarr', cfn):
        compress_array(["foo"] * 100)
        assert cfn.call_count == 1

def test_compress_array_LZ4_sequential():
    cfn = Mock()
    with patch('arctic._compression.clz4.compress', cfn):
        compress_array(["foo"] * 49)
        assert cfn.call_count == 49


def test_decompress():
    assert decompress(compress("foo")) == "foo"


def test_decompress_array():
    ll = ['foo%s' % i for i in range(100)]
    assert decompress_array(compress_array(ll)) == ll

def test_compression_equal_regardless_parallel_mode():
    a = ['spam '] * 666
    with patch('arctic._compression.ENABLE_PARALLEL', True):
        parallel = compress_array(a)
    with patch('arctic._compression.ENABLE_PARALLEL', False):
        serial = compress_array(a)
    assert serial == parallel


def test_compress_decompress_no_parallel():
    with patch('arctic._compression.clz4', sentinel.clz4), \
         patch('arctic._compression.ENABLE_PARALLEL', False), \
         patch('arctic._compression.lz4', wraps=lz4) as patch_lz4:
        # patching clz4 with sentinel will make accessing any clz4 function explode
        assert decompress(compress('Foo')) == 'Foo' 
        assert patch_lz4.compress.call_args_list == [call('Foo')]
        assert patch_lz4.decompress.call_args_list == [call(compress('Foo'))]


def test_compress_array_no_parallel():
    a = ['spam', 'egg', 'spamm', 'spammm']
    with patch('arctic._compression.clz4', sentinel.clz4), \
         patch('arctic._compression.ENABLE_PARALLEL', False), \
         patch('arctic._compression.lz4', wraps=lz4) as patch_lz4:
        assert decompress_array(compress_array(a)) == a
        assert patch_lz4.compress.call_args_list == [call(x) for x in a]
        assert patch_lz4.decompress.call_args_list == [call(compress(x)) for x in a]
