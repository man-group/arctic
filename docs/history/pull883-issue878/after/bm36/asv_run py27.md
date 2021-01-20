```shell
(.venv) cwm@flxsa02:~/git/bb.FLXSA/quant/arctic_878$ tox -e bm36
bm36 develop-inst-noop: /home/cwm/git/bb.FLXSA/quant/arctic_878
bm36 installed: apipkg==1.5,appdirs==1.4.4,-e git+https://github.com/c-w-m/arctic.git@b6848c27c5ab8161fefe47a0653b74b1ccc949ff#egg=arctic,asv==0.4.2,attrs==20.3.0,certifi==2020.12.5,chardet==4.0.0,contextlib2==0.6.0.post1,coverage==5.3.1,decorator==4.4.2,distlib==0.3.1,enum-compat==0.0.3,enum34==1.1.10,execnet==1.7.1,filelock==3.0.12,future==0.18.2,idna==2.10,importlib-metadata==3.4.0,importlib-resources==5.0.0,iniconfig==1.1.1,lz4==3.1.2,mock==4.0.3,mockextras==1.0.2,numpy==1.19.5,packaging==20.8,pandas==1.1.5,path==15.0.1,path.py==12.5.0,pluggy==0.13.1,psutil==5.8.0,py==1.10.0,pycodestyle==2.6.0,pymongo==3.11.2,pyparsing==2.4.7,pytest==6.2.1,pytest-cov==2.11.0,pytest-fixture-config==1.7.0,pytest-forked==1.3.0,pytest-server-fixtures==1.7.0,pytest-shutil==1.7.0,pytest-timeout==1.4.2,pytest-xdist==1.26.0,python-dateutil==2.8.1,pytz==2020.5,requests==2.25.1,retry==0.9.2,setuptools-git==1.2,six==1.15.0,termcolor==1.1.0,toml==0.10.2,typing-extensions==3.7.4.3,tzlocal==2.1,urllib3==1.26.2,virtualenv==20.3.1,zipp==3.4.0
bm36 run-test-pre: PYTHONHASHSEED='314853791'
bm36 run-test: commands[0] | python -c 'print((80*"~")+"\nbm36: pip install asv\n"+(80*"~"))'
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
bm36: pip install asv
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
bm36 run-test: commands[1] | pip install asv
Requirement already satisfied: asv in ./.tox/bm36/lib/python3.6/site-packages (0.4.2)
Requirement already satisfied: six>=1.4 in ./.tox/bm36/lib/python3.6/site-packages (from asv) (1.15.0)
bm36 run-test: commands[2] | python -c 'print((80*"~")+"\nbm36: pip list\n"+(80*"~"))'
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
bm36: asv run --show-stderr --python=2.7 (for arctic)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
bm36 run-test: commands[5] | asv run --show-stderr --python=2.7
· Creating environments
· Discovering benchmarks
· Running 6 total benchmarks (1 commits * 1 environments * 6 benchmarks)
[  0.00%] · For Arctic commit b6848c27:
[  0.00%] ·· Benchmarking virtualenv-py2.7-Cython-decorator-enum34-lz4-mockextras-numpy-pandas-pymongo-python-dateutil-pytz-tzlocal
[  8.33%] ··· Running (benchmarks.TimeSuiteAppend.time_append_dataframe--)..
[ 25.00%] ··· Running (benchmarks.TimeSuiteWrite.time_write_dataframe_compressible--)..
[ 41.67%] ··· Running (benchmarks.TimeSuiteWrite.time_write_series_compressible--)..
[ 58.33%] ··· benchmarks.TimeSuiteAppend.time_append_dataframe                                                                           ok
[ 58.33%] ··· ========== ============
               5K * 10^              
              ---------- ------------
                  0       7.48±0.4ms 
                  1        12.0±1ms  
                  2        93.4±3ms  
                  3        868±30ms  
              ========== ============

[ 58.33%] ···· For parameters: 0
               No handlers could be found for logger "arctic.store.version_store"
               
               For parameters: 1
               No handlers could be found for logger "arctic.store.version_store"
               
               For parameters: 2
               No handlers could be found for logger "arctic.store.version_store"
               
               For parameters: 3
               No handlers could be found for logger "arctic.store.version_store"

[ 66.67%] ··· benchmarks.TimeSuiteRead.time_read_dataframe                                                                               ok
[ 66.67%] ··· ========== ============
               5K * 10^              
              ---------- ------------
                  0       5.52±0.2ms 
                  1       7.15±0.2ms 
                  2        22.5±2ms  
                  3        206±2ms   
              ========== ============

[ 66.67%] ···· For parameters: 0
               No handlers could be found for logger "arctic.store.version_store"
               
               For parameters: 1
               No handlers could be found for logger "arctic.store.version_store"
               
               For parameters: 2
               No handlers could be found for logger "arctic.store.version_store"
               
               For parameters: 3
               No handlers could be found for logger "arctic.store.version_store"

[ 75.00%] ··· benchmarks.TimeSuiteWrite.time_write_dataframe_compressible                                                                ok
[ 75.00%] ··· ========== ============
               5K * 10^              
              ---------- ------------
                  0       26.2±0.8ms 
                  1       30.0±0.5ms 
                  2        78.5±2ms  
                  3        631±6ms   
              ========== ============

[ 75.00%] ···· For parameters: 0
               No handlers could be found for logger "arctic.store.version_store"
               
               For parameters: 1
               No handlers could be found for logger "arctic.store.version_store"
               
               For parameters: 2
               No handlers could be found for logger "arctic.store.version_store"
               
               For parameters: 3
               No handlers could be found for logger "arctic.store.version_store"

[ 83.33%] ··· benchmarks.TimeSuiteWrite.time_write_dataframe_random                                                                      ok
[ 83.33%] ··· ========== ==========
               5K * 10^            
              ---------- ----------
                  0       28.0±1ms 
                  1       34.7±2ms 
                  2       104±4ms  
                  3       712±20ms 
              ========== ==========

[ 83.33%] ···· For parameters: 0
               No handlers could be found for logger "arctic.store.version_store"
               
               For parameters: 1
               No handlers could be found for logger "arctic.store.version_store"
               
               For parameters: 2
               No handlers could be found for logger "arctic.store.version_store"
               
               For parameters: 3
               No handlers could be found for logger "arctic.store.version_store"

[ 91.67%] ··· benchmarks.TimeSuiteWrite.time_write_series_compressible                                                                   ok
[ 91.67%] ··· ========== ==========
               5K * 10^            
              ---------- ----------
                  0       19.2±2ms 
                  1       21.0±1ms 
                  2       39.6±2ms 
                  3       146±4ms  
              ========== ==========

[ 91.67%] ···· For parameters: 0
               No handlers could be found for logger "arctic.store.version_store"
               
               For parameters: 1
               No handlers could be found for logger "arctic.store.version_store"
               
               For parameters: 2
               No handlers could be found for logger "arctic.store.version_store"
               
               For parameters: 3
               No handlers could be found for logger "arctic.store.version_store"

[100.00%] ··· benchmarks.TimeSuiteWrite.time_write_series_random                                                                         ok
[100.00%] ··· ========== ============
               5K * 10^              
              ---------- ------------
                  0        26.8±1ms  
                  1        39.8±3ms  
                  2        140±5ms   
                  3       1.12±0.02s 
              ========== ============

[100.00%] ···· For parameters: 0
               No handlers could be found for logger "arctic.store.version_store"
               
               For parameters: 1
               No handlers could be found for logger "arctic.store.version_store"
               
               For parameters: 2
               No handlers could be found for logger "arctic.store.version_store"
               
               For parameters: 3
               No handlers could be found for logger "arctic.store.version_store"

bm36 run-test: commands[6] | python -c 'print((80*"~")+"\nbm36: complete\n"+(80*"~"))'
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
bm36: complete
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
_________________________________________________________________ summary _________________________________________________________________
  bm36: commands succeeded
  congratulations :)

```