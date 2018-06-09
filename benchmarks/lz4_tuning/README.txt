Use the following benchmark script to tune the following parameters against specific hardware:
     arctic/benchmarks/lz4_tuning/benchmark_lz4.py

Execute it on the server hardware you intend to run your application, and based on the results, you can tune arctic/_compression.py parameters:
  - When using High Compression, it is recommended to use a large value (scales linearly)
    Think always the overhead of context switching on a loaded machine.
    LZ4_WORKERS = os.environ.get('LZ4_WORKERS', 4)
  - Minimum data size to use parallel compression in LZ4 mode
    For non-HighCompression, we get 20-30% increase, when chunks are > 0.5MB and their number is >16
    Higher thread counts don't help, especially for small sized data
    LZ4_N_PARALLEL = os.environ.get('LZ4_N_PARALLEL', 16)
    LZ4_MINSZ_PARALLEL = os.environ.get('LZ4_MINSZ_PARALLEL', 0.5*1024**2)  # 0.5 MB
