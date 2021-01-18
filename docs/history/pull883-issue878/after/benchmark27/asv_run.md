(.venv) cwm@flxsa02:~/git/bb.FLXSA/quant/arctic_878$ source .tox/benchmark27/bin/activate
(benchmark27) cwm@flxsa02:~/git/bb.FLXSA/quant/arctic_878$ clear

(benchmark27) cwm@flxsa02:~/git/bb.FLXSA/quant/arctic_878$ asv run

· No executable found for python 3,7
· Creating environments....................
· Discovering benchmarks.
·· Uninstalling from virtualenv-py2.7-Cython-decorator-enum34-lz4-mockextras-numpy-pandas-pymongo-python-dateutil-pytz-tzlocal.
·· Building 8ddd8313 for virtualenv-py2.7-Cython-decorator-enum34-lz4-mockextras-numpy-pandas-pymongo-python-dateutil-pytz-tzlocal...
·· Installing 8ddd8313 into virtualenv-py2.7-Cython-decorator-enum34-lz4-mockextras-numpy-pandas-pymongo-python-dateutil-pytz-tzlocal.
·· Error running /home/cwm/git/bb.FLXSA/quant/arctic_878/.asv/env/b8a89d02ecf8cf65a0ce1bec4918bbdf/bin/python /home/cwm/git/bb.FLXSA/quant/arctic_878/asv/asv/benchmark.py discover /home/cwm/git/bb.FLXSA/quant/arctic_878/benchmarks /tmp/tmpaU8Zbc/result.json (exit status 1)
   STDOUT -------->
   
   STDERR -------->
   Traceback (most recent call last):
     File "/home/cwm/git/bb.FLXSA/quant/arctic_878/asv/asv/benchmark.py", line 1435, in <module>
       main()
     File "/home/cwm/git/bb.FLXSA/quant/arctic_878/asv/asv/benchmark.py", line 1428, in main
       commands[mode](args)
     File "/home/cwm/git/bb.FLXSA/quant/arctic_878/asv/asv/benchmark.py", line 1103, in main_discover
       list_benchmarks(benchmark_dir, fp)
     File "/home/cwm/git/bb.FLXSA/quant/arctic_878/asv/asv/benchmark.py", line 1088, in list_benchmarks
       for benchmark in disc_benchmarks(root):
     File "/home/cwm/git/bb.FLXSA/quant/arctic_878/asv/asv/benchmark.py", line 985, in disc_benchmarks
       for module in disc_modules(root_name, ignore_import_errors=ignore_import_errors):
     File "/home/cwm/git/bb.FLXSA/quant/arctic_878/asv/asv/benchmark.py", line 967, in disc_modules
       for item in disc_modules(name, ignore_import_errors=ignore_import_errors):
     File "/home/cwm/git/bb.FLXSA/quant/arctic_878/asv/asv/benchmark.py", line 950, in disc_modules
       module = import_module(module_name)
     File "/usr/lib/python2.7/importlib/__init__.py", line 37, in import_module
       __import__(name)
     File "/home/cwm/git/bb.FLXSA/quant/arctic_878/benchmarks/fast_serializable_check.py", line 4, in <module>
       from tests.unit.serialization.serialization_test_data import _mixed_test_data as input_test_data
   ImportError: No module named tests.unit.serialization.serialization_test_data

·· Failed: trying different commit/environment..
·· Uninstalling from virtualenv-py3.6-Cython-decorator-enum34-lz4-mockextras-numpy-pandas-pymongo-python-dateutil-pytz-tzlocal.
·· Building 8ddd8313 for virtualenv-py3.6-Cython-decorator-enum34-lz4-mockextras-numpy-pandas-pymongo-python-dateutil-pytz-tzlocal....
·· Installing 8ddd8313 into virtualenv-py3.6-Cython-decorator-enum34-lz4-mockextras-numpy-pandas-pymongo-python-dateutil-pytz-tzlocal.
·· Error running /home/cwm/git/bb.FLXSA/quant/arctic_878/.asv/env/037f0f3d3f2754d08b4ac4fdc939e172/bin/python /home/cwm/git/bb.FLXSA/quant/arctic_878/asv/asv/benchmark.py discover /home/cwm/git/bb.FLXSA/quant/arctic_878/benchmarks /tmp/tmprRj7Cq/result.json (exit status 1)
   STDOUT -------->
   
   STDERR -------->
   Traceback (most recent call last):
     File "/home/cwm/git/bb.FLXSA/quant/arctic_878/.asv/env/037f0f3d3f2754d08b4ac4fdc939e172/lib/python3.6/site-packages/pandas/core/internals/managers.py", line 1693, in create_block_manager_from_arrays
       mgr = BlockManager(blocks, axes)
     File "/home/cwm/git/bb.FLXSA/quant/arctic_878/.asv/env/037f0f3d3f2754d08b4ac4fdc939e172/lib/python3.6/site-packages/pandas/core/internals/managers.py", line 149, in __init__
       self._verify_integrity()
     File "/home/cwm/git/bb.FLXSA/quant/arctic_878/.asv/env/037f0f3d3f2754d08b4ac4fdc939e172/lib/python3.6/site-packages/pandas/core/internals/managers.py", line 329, in _verify_integrity
       raise construction_error(tot_items, block.shape[1:], self.axes)
   ValueError: Shape of passed values is (1000, 5), indices imply (1, 5)
   
   During handling of the above exception, another exception occurred:
   
   Traceback (most recent call last):
     File "/home/cwm/git/bb.FLXSA/quant/arctic_878/asv/asv/benchmark.py", line 1435, in <module>
       main()
     File "/home/cwm/git/bb.FLXSA/quant/arctic_878/asv/asv/benchmark.py", line 1428, in main
       commands[mode](args)
     File "/home/cwm/git/bb.FLXSA/quant/arctic_878/asv/asv/benchmark.py", line 1103, in main_discover
       list_benchmarks(benchmark_dir, fp)
     File "/home/cwm/git/bb.FLXSA/quant/arctic_878/asv/asv/benchmark.py", line 1088, in list_benchmarks
       for benchmark in disc_benchmarks(root):
     File "/home/cwm/git/bb.FLXSA/quant/arctic_878/asv/asv/benchmark.py", line 985, in disc_benchmarks
       for module in disc_modules(root_name, ignore_import_errors=ignore_import_errors):
     File "/home/cwm/git/bb.FLXSA/quant/arctic_878/asv/asv/benchmark.py", line 967, in disc_modules
       for item in disc_modules(name, ignore_import_errors=ignore_import_errors):
     File "/home/cwm/git/bb.FLXSA/quant/arctic_878/asv/asv/benchmark.py", line 950, in disc_modules
       module = import_module(module_name)
     File "/usr/lib/python3.6/importlib/__init__.py", line 126, in import_module
       return _bootstrap._gcd_import(name[level:], package, level)
     File "<frozen importlib._bootstrap>", line 994, in _gcd_import
     File "<frozen importlib._bootstrap>", line 971, in _find_and_load
     File "<frozen importlib._bootstrap>", line 955, in _find_and_load_unlocked
     File "<frozen importlib._bootstrap>", line 665, in _load_unlocked
     File "<frozen importlib._bootstrap_external>", line 678, in exec_module
     File "<frozen importlib._bootstrap>", line 219, in _call_with_frames_removed
     File "/home/cwm/git/bb.FLXSA/quant/arctic_878/benchmarks/benchmarks.py", line 40, in <module>
       df_random = [gen_dataframe_random(5, rows) for rows in TEST_SIZES]
     File "/home/cwm/git/bb.FLXSA/quant/arctic_878/benchmarks/benchmarks.py", line 40, in <listcomp>
       df_random = [gen_dataframe_random(5, rows) for rows in TEST_SIZES]
     File "/home/cwm/git/bb.FLXSA/quant/arctic_878/benchmarks/benchmarks.py", line 14, in gen_dataframe_random
       return pd.DataFrame(data=c, index=index)
     File "/home/cwm/git/bb.FLXSA/quant/arctic_878/.asv/env/037f0f3d3f2754d08b4ac4fdc939e172/lib/python3.6/site-packages/pandas/core/frame.py", line 468, in __init__
       mgr = init_dict(data, index, columns, dtype=dtype)
     File "/home/cwm/git/bb.FLXSA/quant/arctic_878/.asv/env/037f0f3d3f2754d08b4ac4fdc939e172/lib/python3.6/site-packages/pandas/core/internals/construction.py", line 283, in init_dict
       return arrays_to_mgr(arrays, data_names, index, columns, dtype=dtype)
     File "/home/cwm/git/bb.FLXSA/quant/arctic_878/.asv/env/037f0f3d3f2754d08b4ac4fdc939e172/lib/python3.6/site-packages/pandas/core/internals/construction.py", line 93, in arrays_to_mgr
       return create_block_manager_from_arrays(arrays, arr_names, axes)
     File "/home/cwm/git/bb.FLXSA/quant/arctic_878/.asv/env/037f0f3d3f2754d08b4ac4fdc939e172/lib/python3.6/site-packages/pandas/core/internals/managers.py", line 1697, in create_block_manager_from_arrays
       raise construction_error(len(arrays), arrays[0].shape, axes, e)
   ValueError: Shape of passed values is (1000, 5), indices imply (1, 5)

·· Failed to build the project and import the benchmark suite.
(benchmark27) cwm@flxsa02:~/git/bb.FLXSA/quant/arctic_878$ 
