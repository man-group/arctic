```shell
(.venv) cwm@flxsa02:~/git/bb.FLXSA/quant/arctic_878$ tox -e bm36
bm36 develop-inst-noop: /home/cwm/git/bb.FLXSA/quant/arctic_878
bm36 installed: apipkg==1.5,appdirs==1.4.4,-e git+https://github.com/c-w-m/arctic.git@b6848c27c5ab8161fefe47a0653b74b1ccc949ff#egg=arctic,asv==0.4.2,attrs==20.3.0,certifi==2020.12.5,chardet==4.0.0,contextlib2==0.6.0.post1,coverage==5.3.1,decorator==4.4.2,distlib==0.3.1,enum-compat==0.0.3,enum34==1.1.10,execnet==1.7.1,filelock==3.0.12,future==0.18.2,idna==2.10,importlib-metadata==3.4.0,importlib-resources==5.0.0,iniconfig==1.1.1,lz4==3.1.2,mock==4.0.3,mockextras==1.0.2,numpy==1.19.5,packaging==20.8,pandas==1.1.5,path==15.0.1,path.py==12.5.0,pluggy==0.13.1,psutil==5.8.0,py==1.10.0,pycodestyle==2.6.0,pymongo==3.11.2,pyparsing==2.4.7,pytest==6.2.1,pytest-cov==2.11.0,pytest-fixture-config==1.7.0,pytest-forked==1.3.0,pytest-server-fixtures==1.7.0,pytest-shutil==1.7.0,pytest-timeout==1.4.2,pytest-xdist==1.26.0,python-dateutil==2.8.1,pytz==2020.5,requests==2.25.1,retry==0.9.2,setuptools-git==1.2,six==1.15.0,termcolor==1.1.0,toml==0.10.2,typing-extensions==3.7.4.3,tzlocal==2.1,urllib3==1.26.2,virtualenv==20.3.1,zipp==3.4.0
bm36 run-test-pre: PYTHONHASHSEED='2809068001'
bm36 run-test: commands[0] | python -c 'print((80*"~")+"\nbm36: pip install asv\n"+(80*"~"))'
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
bm36: pip install asv
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
bm36 run-test: commands[1] | pip install asv
Requirement already satisfied: asv in ./.tox/bm36/lib/python3.6/site-packages (0.4.2)
Requirement already satisfied: six>=1.4 in ./.tox/bm36/lib/python3.6/site-packages (from asv) (1.15.0)
bm36 run-test: commands[2] | python -c 'print((80*"~")+"\nbm36: asv run --show-stderr --python=2.7 (for arctic)\n"+(80*"~"))'
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
bm36: asv run --show-stderr --python=3.5 (for arctic)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
bm36 run-test: commands[3] | asv run --show-stderr --python=3.6
· Creating environments
· Discovering benchmarks
·· Error running /home/cwm/git/bb.FLXSA/quant/arctic_878/.asv/env/037f0f3d3f2754d08b4ac4fdc939e172/bin/python /home/cwm/git/bb.FLXSA/quant/arctic_878/.tox/bm36/lib/python3.6/site-packages/asv/benchmark.py discover /home/cwm/git/bb.FLXSA/quant/arctic_878/benchmarks /tmp/tmpmhdvlhku/result.json (exit status 1)
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
     File "/home/cwm/git/bb.FLXSA/quant/arctic_878/.tox/bm36/lib/python3.6/site-packages/asv/benchmark.py", line 1315, in <module>
       main()
     File "/home/cwm/git/bb.FLXSA/quant/arctic_878/.tox/bm36/lib/python3.6/site-packages/asv/benchmark.py", line 1308, in main
       commands[mode](args)
     File "/home/cwm/git/bb.FLXSA/quant/arctic_878/.tox/bm36/lib/python3.6/site-packages/asv/benchmark.py", line 1004, in main_discover
       list_benchmarks(benchmark_dir, fp)
     File "/home/cwm/git/bb.FLXSA/quant/arctic_878/.tox/bm36/lib/python3.6/site-packages/asv/benchmark.py", line 989, in list_benchmarks
       for benchmark in disc_benchmarks(root):
     File "/home/cwm/git/bb.FLXSA/quant/arctic_878/.tox/bm36/lib/python3.6/site-packages/asv/benchmark.py", line 887, in disc_benchmarks
       for module in disc_modules(root_name, ignore_import_errors=ignore_import_errors):
     File "/home/cwm/git/bb.FLXSA/quant/arctic_878/.tox/bm36/lib/python3.6/site-packages/asv/benchmark.py", line 869, in disc_modules
       for item in disc_modules(name, ignore_import_errors=ignore_import_errors):
     File "/home/cwm/git/bb.FLXSA/quant/arctic_878/.tox/bm36/lib/python3.6/site-packages/asv/benchmark.py", line 857, in disc_modules
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
ERROR: InvocationError for command /home/cwm/git/bb.FLXSA/quant/arctic_878/.tox/bm36/bin/asv run --show-stderr --python=3.6 (exited with code 1)
_________________________________________________________________ summary _________________________________________________________________
ERROR:   bm36: commands failed
(.venv) cwm@flxsa02:~/git/bb.FLXSA/quant/arctic_878$ 
```