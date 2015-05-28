from mock import patch, Mock

from arctic._compression import use_lz4hc, _should_use_lz4hc, _is_interactive_mode, compress, compress_array, decompress, decompress_array
from arctic import _compression


def teardown_function(function):
    _compression.USE_LZ4HC = True


def test_use_lz4hc():
    use_lz4hc(True)
    assert _compression.USE_LZ4HC is True
    use_lz4hc(False)
    assert _compression.USE_LZ4HC is False


def test_use_lz4hc_True():
    use_lz4hc(True)
    assert _should_use_lz4hc() is True


def test_use_lz4hc_False():
    use_lz4hc(False)
    assert _should_use_lz4hc() is False


def test__is_interactive_mode():
    assert _is_interactive_mode() is False  # in a test!


def test_compress():
    assert len(compress("foobar")) > 0


def test_compress_LZ4HC():
    use_lz4hc(True)
    cfn = Mock()
    with patch('arctic._compression.clz4.compressHC', cfn):
        compress("foo")
        assert cfn.call_count == 1


def test_compress_LZ4():
    use_lz4hc(False)
    cfn = Mock()
    with patch('arctic._compression.clz4.compress', cfn):
        compress("foo")
        assert cfn.call_count == 1


def test_compressarr():
    assert len(compress_array(["foobar"*10])) > 0
    assert isinstance(compress_array(["foobar"*10]), list)


def test_compressarr_LZ4HC():
    assert len(compress_array(["foobar"*10])) > 0
    assert isinstance(compress_array(["foobar"*10]), list)


def test_compress_array_usesLZ4HC():
    use_lz4hc(True)
    cfn = Mock()
    with patch('arctic._compression.clz4.compressarrHC', cfn):
        compress_array(["foo"] * 100)
        assert cfn.call_count == 1


def test_compress_array_usesLZ4():
    use_lz4hc(False)
    cfn = Mock()
    with patch('arctic._compression.clz4.compressarr', cfn):
        compress_array(["foo"] * 100)
        assert cfn.call_count == 1


def test_compress_array_LZ4HC_sequential():
    use_lz4hc(True)
    cfn = Mock()
    with patch('arctic._compression.clz4.compressHC', cfn):
        compress_array(["foo"] * 4)
        assert cfn.call_count == 4


def test_compress_array_LZ4_sequential():
    use_lz4hc(False)
    cfn = Mock()
    with patch('arctic._compression.clz4.compress', cfn):
        compress_array(["foo"] * 49)
        assert cfn.call_count == 49


def test_decompress():
    assert decompress(compress("foo")) == "foo"


def test_decompress_array():
    ll = ['foo%s' % i for i in range(100)]
    assert decompress_array(compress_array(ll)) == ll

