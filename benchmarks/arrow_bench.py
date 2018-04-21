import cPickle
from io import BytesIO
import itertools
import logging
import numpy as np
import os
import pandas as pd
import pickle
import pyarrow as pa
import pyarrow.parquet as pq
import random
import sys
import time
import math
from collections import namedtuple
from mock import patch, MagicMock, sentinel, create_autospec, Mock, call


from arctic._compression import compress_array, decompress
from arctic.serialization.numpy_records import SeriesSerializer, DataFrameSerializer
from arctic.tickstore.tickstore import TickStore


logger = logging.getLogger(__name__)


BenchResult = namedtuple('BenchResult', 'id mean std min max data_size rows columns')

SERIALIZER = DataFrameSerializer()

CACHED_DF = {}

ARROW_COMPRESSION_CODECS = {'snappy', 'gzip', 'brotli', 'zstd', 'lz4'}
PARQUET_COMPRESSION_CODECS = {'NONE', 'SNAPPY', 'GZIP'}


def get_random_df(nrows, ncols):
    ret_df = pd.DataFrame(np.random.randn(nrows, ncols),
                          index=pd.date_range('20170101',
                                              periods=nrows, freq='S'),
                          columns=["".join([chr(random.randint(ord('A'), ord('Z'))) for _ in range(8)]) for _ in
                                   range(ncols)])
    ret_df.index.name = 'index'
    ret_df.index = ret_df.index.tz_localize('UTC')
    return ret_df


def generate_test_frames(nrows, ncols, step_pct=0.1):
    if step_pct < 0 or step_pct > 1:
        raise ValueError("Bad step_pct value {}".format(step_pct))
    nrow_reduce_per_step = int(math.ceil(nrows * step_pct))  # avoid 0 steps decr
    while nrows > 0:
        # Create a cache entry if not there
        if (nrows, ncols) not in CACHED_DF:
            CACHED_DF[(nrows, ncols)] = get_random_df(nrows, ncols)
        yield CACHED_DF[(nrows, ncols)]
        nrows = nrows-nrow_reduce_per_step


def get_df_size_gb(df, do_print=False):
    if df is None or df.empty:
        size = 0
    else:
        size = sys.getsizeof(df) / (1024.0 ** 3)
    if do_print:
        print("Size of dataframe is: %3.3f GB" % size)
    return size


def run_experiment(f2bench, name, df, iterations=1, **kwargs):
    times = list()
    for i in range(iterations):
        t_start = time.time()
        try:
            log.info('Running {} ({})'.format(f2bench.__name__, kwargs))
            assert f2bench(df, **kwargs) is not None
        except Exception as ex:
            log.exception(ex)
            #print("EXCEPTION: %s -- -- -- -- %s %s %s" % (name, get_df_size_gb(df), df.shape[0], df.shape[1]))
            continue
        t_stop = time.time()
        times.append(t_stop-t_start)
    result = BenchResult(id=name,
                         mean=np.mean(times) if times else '--',
                         std=np.std(times) if times else '--',
                         min=min(times) if times else '--',
                         max=max(times) if times else '--',
                         data_size=get_df_size_gb(df),
                         rows=df.shape[0], columns=df.shape[1])
    #return ("%s %3.9f %3.9f %3.9f %3.9f %3.3f %s %s" % (name, np.mean(times), np.std(times), min(times), max(times), get_df_size_gb(df), df.shape[0], df.shape[1]))
    log.info(result)
    return result


def pickle_serialize(df, pickle_impl, do_deserialize=True, **kwargs):
    data = pickle_impl.dumps(df, **kwargs)
    if do_deserialize:
        return pickle_impl.loads(data)
    return data


def pickle_serialize_np(df, pickle_impl, do_deserialize=True, **kwargs):
    objects = []
    for c in df.columns:
        objects.append(pickle_impl.dumps(df[c].values, **kwargs))
    if do_deserialize:
        deserialized = []
        for ser_o in objects:
            deserialized.append(pickle_impl.loads(ser_o))
        return deserialized
    return objects


def arctic_versionstore_serialize(df, do_deserialize=True, compression=False, chunk_size=None):
    if chunk_size and int(chunk_size) < 1:
        raise ValueError("Bad chunk size: {}".format(chunk_size))
    chunk = None
    chunks = list()
    serialized_data, md = SERIALIZER.serialize(df)
    chunk_size = len(serialized_data) if chunk_size is None or chunk_size > len(serialized_data) else int(chunk_size)
    for i in range(0, len(serialized_data), chunk_size):
        chunk = serialized_data[i:i+chunk_size].tostring()
        chunks.append(chunk)
    if compression:
        chunks = compress_array(chunks)
        for i in range(len(chunks)):
            chunks[i] = decompress(chunks[i])
    if do_deserialize:
        data = b''.join(chunks)
        np_arr = np.fromstring(data, dtype=md)
        df = SERIALIZER.deserialize(np_arr)
        #print df
    return chunk


def arctic_tickstore_serialize(df, do_deserialize=True, chunk_size=None):
    if chunk_size and int(chunk_size) < 1:
        raise ValueError("Bad chunk size: {}".format(chunk_size))
    chunk_size = 100000 if not chunk_size else int(chunk_size)
    with patch('arctic.arctic.ArcticLibraryBinding', return_value=Mock(), autospec=True) as ML:
        ML.arctic = Mock()
        tstore = TickStore(ML, chunk_size=chunk_size)
        buckets = tstore._pandas_to_buckets(df, 'SYM_A', None)
        rtn = list()
        if do_deserialize:
            for b in buckets:
                column_set = set()
                column_dtypes = {}
                data = tstore._read_bucket(b, column_set, column_dtypes, False, False, None)
                rtn.append(data)
            return rtn
        return buckets


def _verify_input_arrow(nthreads, compression, chunk_size):
    if compression and compression not in ARROW_COMPRESSION_CODECS:
        raise ValueError("Compression type is not supported by Arrow: {}".format(compression))
    if chunk_size and int(chunk_size) < 1:
        raise ValueError("Bad chunk size: {}".format(chunk_size))
    if nthreads < 1:
        raise ValueError("Bad threads count: {}".format(nthreads))


def arrow_serialize(df, do_deserialize=True, nthreads=1, compression=None, chunk_size=None):
    _verify_input_arrow(nthreads, compression, chunk_size)
    chunk = None
    chunks = list()
    chunk_size = len(df) if chunk_size is None else int(chunk_size)
    for i in range(0, len(df), chunk_size):
        chunk = df[i:i+chunk_size]
        chunk = pa.serialize_pandas(chunk)
        len_uncompressed_chunk = len(chunk)
        if compression:
            chunk = pa.compress(chunk, codec=compression)
        chunks.append((chunk, len_uncompressed_chunk))
    # Now deserialize if user requested this
    if do_deserialize:
        for chunk, len_uncompressed_chunk in chunks:
            if compression:
                chunk = pa.decompress(chunk, len_uncompressed_chunk, codec=compression)
            chunk = pa.deserialize_pandas(chunk, nthreads=nthreads)
            #print chunk
    return chunk


def arrow_serialize_np(df, do_deserialize=True, nthreads=1, compression=None, chunk_size=None):
    _verify_input_arrow(nthreads, compression, chunk_size)
    chunk = None
    chunks_by_column = list()
    chunk_size = len(df) if chunk_size is None else int(chunk_size)
    for c in df.columns:
        col_chunks = list()
        col_arr = df[c].values
        for i in range(0, len(df), chunk_size):
            chunk = col_arr[i:i+chunk_size]
            chunk = pa.serialize(chunk).to_buffer(nthreads=nthreads)
            len_uncompressed_chunk = len(chunk)
            if compression:
                chunk = pa.compress(chunk, codec=compression)
            col_chunks.append((chunk, len_uncompressed_chunk))
        chunks_by_column.append(col_chunks)
    # Now deserialize if user requested this
    if do_deserialize:
        for col_chunks in chunks_by_column:
            for chunk, len_uncompressed_chunk in col_chunks:
                if compression:
                    chunk = pa.decompress(chunk, len_uncompressed_chunk, codec=compression)
                chunk = pa.deserialize(chunk)
                #print chunk
    return chunk


def pandas_to_arrow(df, do_deserialize=True, nthreads=1):
    data = pa.Table.from_pandas(df)
    if do_deserialize:
        return data.to_pandas(nthreads=nthreads)
    return data


def persist_feather(df, dest_file='test.feather', do_read=True, nthreads=1):
    last_mod = os.path.getmtime(dest_file) if isinstance(dest_file, basestring) else None
    pa.feather.write_feather(df, dest_file)
    if last_mod is not None and os.path.getmtime(dest_file) == last_mod:
        raise Exception('file {} not written/updated'.format(dest_file))
    if do_read:
        return pa.feather.read_feather(dest_file, columns=None, nthreads=nthreads)
    return dest_file


def persist_parquet(df, dest_file='test.parquet', do_read=True, nthreads=1, compression=None, chunk_size=None):
    if isinstance(df, pd.DataFrame):
        df = pa.Table.from_pandas(df)
    compression = 'NONE' if compression is None else compression
    if compression not in PARQUET_COMPRESSION_CODECS:
        raise ValueError("Bad compression codec was supplied: {}".format(compression))
    last_mod = os.path.getmtime(dest_file) if os.path.isfile(dest_file) else None
    # Write to file.
    # row_group_size controls the slice length across columns,
    # which is persisted incrementally. May result in large file.
    pq.write_table(df, dest_file, row_group_size=chunk_size, compression=compression, version='2.0')
    if not os.path.isfile(dest_file) or os.path.getmtime(dest_file) == last_mod:
        raise Exception('file {} not written/updated'.format(dest_file))
    if do_read:
        return pq.read_table(dest_file, columns=None, nthreads=nthreads, metadata=None, use_pandas_metadata=False)
    return dest_file


def persist_pickled_file(df, pickle_impl, dest_file='test.parquet', do_read=True, **kwargs):
    last_mod = os.path.getmtime(dest_file) if isinstance(dest_file, basestring) else None
    with open(dest_file, "wb") as f:
        pickle_impl.dump(df, f, **kwargs)
    if not os.path.isfile(dest_file) or os.path.getmtime(dest_file) == last_mod:
        raise Exception('file {} not written/updated'.format(dest_file))
    if do_read:
        with open(dest_file, 'rb') as f:
            return pickle_impl.load(dest_file)
    return dest_file


def persist_localhost_arctic(df):
    pass


def persist_hdf5(df):
    pass


def ipc_queue_pickle(df):
    pass


def ipc_plasma_cache(df):
    pass


def run_pickle(df, iterations, results):
    implementations = (pickle, cPickle)
    protocols = (None, pickle.HIGHEST_PROTOCOL)
    deserialize = (True, False)
    bench_data_type = (pickle_serialize, pickle_serialize_np)
    for c in itertools.product(implementations, protocols, deserialize, bench_data_type):
        pickle_impl, protocol, deser, bench_dtype = c
        bench_id = "_".join((str(pickle_impl.__name__),
                             'High' if protocol == pickle.HIGHEST_PROTOCOL else 'Default',
                             'SerDes' if deser else 'Ser',
                             'np' if bench_dtype.__name__.endswith('_np') else 'df'))
        results[bench_id] = run_experiment(bench_dtype, bench_id, df, iterations,
                                           protocol=0 if protocol is None else protocol,
                                           pickle_impl=pickle_impl,
                                           do_deserialize=deser)


def run_arctic_versionstore(df, iterations, chunk_sizes, results):
    deserialize = (True, False)
    with_compression = (True, False)
    chunk_sizes = set([None] + chunk_sizes)
    for c in itertools.product(deserialize, with_compression, chunk_sizes):
        deser, compr, chsz = c
        bench_id = "_".join(('arctic_versionstore',
                             'SerDes' if deser else 'Ser',
                             'lz4Compression' if with_compression else 'noCompression',
                             (str(chsz) + 'Chunk') if chsz else 'Whole'))
        results[bench_id] = run_experiment(arctic_versionstore_serialize, bench_id, df, iterations,
                                           do_deserialize=deser,
                                           compression=compr,
                                           chunk_size=chsz)


def run_arctic_tickstore(df, iterations, rows_fraction, results):
    deserialize = (True, False)
    rows = df.shape[0]
    chunk_sizes = range(rows / rows_fraction, rows, rows / rows_fraction)
    for c in itertools.product(deserialize, chunk_sizes):
        deser, chsz = c
        bench_id = "_".join(('arctic_tickstore',
                             'SerDes' if deser else 'Ser',
                             (str(chsz) + 'Rows') if chsz else 'Rows'))
        results[bench_id] = run_experiment(arctic_tickstore_serialize, bench_id, df, iterations,
                                           do_deserialize=deser,
                                           chunk_size=chsz)


def run_arrow_serialize(df, iterations, rows_fraction, threads, results):
    deserialize = (True, False)
    compressions = [None] + list(ARROW_COMPRESSION_CODECS)
    rows = df.shape[0]
    chunk_sizes = range(rows / rows_fraction, rows, rows / rows_fraction)
    for c in itertools.product(deserialize, threads, compressions, chunk_sizes):
        deser, t, compr, chsz = c
        bench_id = "_".join(('arrow_serialize',
                             'SerDes' if deser else 'Ser',
                             "x{}threads".format(t),
                             "{}Compression".format(compr),
                             (str(chsz) + 'Rows') if chsz else 'Rows'))
        results[bench_id] = run_experiment(arrow_serialize, bench_id, df, iterations,
                                           do_deserialize=deser,
                                           nthreads=t,
                                           compression=compr,
                                           chunk_size=chsz)


def run_arrow_serialize_np(df, iterations, rows_fraction, threads, results):
    deserialize = (True, False)
    compressions = [None] + list(ARROW_COMPRESSION_CODECS)
    rows = df.shape[0]
    chunk_sizes = range(rows / rows_fraction, rows, rows / rows_fraction)
    for c in itertools.product(deserialize, threads, compressions, chunk_sizes):
        deser, t, compr, chsz = c
        bench_id = "_".join(('arrow_serialize',
                             'SerDes' if deser else 'Ser',
                             "x{}threads".format(t),
                             "{}Compression".format(compr),
                             (str(chsz) + 'Rows') if chsz else 'Rows'))
        results[bench_id] = run_experiment(arrow_serialize_np, bench_id, df, iterations,
                                           do_deserialize=deser,
                                           nthreads=t,
                                           compression=compr,
                                           chunk_size=chsz)


def run_pandas_to_arrow(df, iterations, threads, results):
    deserialize = (True, False)
    for c in itertools.product(deserialize, threads):
        deser, t = c
        bench_id = "_".join(('pandas_to_arrow',
                             'SerDes' if deser else 'Ser',
                             "x{}threads".format(t)))
        results[bench_id] = run_experiment(pandas_to_arrow, bench_id, df, iterations,
                                           do_deserialize=deser,
                                           nthreads=t)


def main():
    rows = 1024 * 1024    # the initial size of the reference DataFrame
    columns = 8           # columns are static
    iterations = 5        # times to run each experiemnt
    reduce_step = 0.25    # progressively try with smaller dataframes
    rows_fraction = 4     # controls chunking
    threads = [1, 4, 12]  # controls rounds with varying number of threads

    results = dict()

    for df in generate_test_frames(rows, columns, reduce_step):
        # Run the pickle pandas benchmarks
        run_pickle(df, iterations, results)

        # Run: arctic_versionstore_serialize(df, do_deserialize=True, compression=False, chunk_size=None)
        run_arctic_versionstore(df, iterations, [256 * 1024, 2 * 256 * 1024, 1024 * 1024, 5 * 1024 * 1024], results)

        # Run: arctic_tickstore_serialize(df, do_deserialize=True, chunk_size=100000)
        run_arctic_tickstore(df, iterations, rows_fraction, results)

        # Run: arrow_serialize(df, do_deserialize=True, nthreads=1, compression=None, chunk_size=None)
        run_arrow_serialize(df, iterations, rows_fraction, threads, results)

        # Run: arrow_serialize_np(df, do_deserialize=True, nthreads=1, compression=None, chunk_size=None)
        run_arrow_serialize_np(df, iterations, rows_fraction, threads, results)

        # Run: pandas_to_arrow(df, do_deserialize=True, nthreads=1):
        run_pandas_to_arrow(df, iterations, threads, results)

    import pprint
    pprint.pprint(results)


if __name__ == '__main__':
    main()
