# [#878: v1.80 test failures - are these expected?](https://github.com/man-group/arctic/issues/878) 

The following steps were taken to address issue #878:

1. Previous work was done using a manually configured Python 3.6 virtual 
   environment.  
2. Some errors and warnings were thought to come from package version 
   differences in the manually configured py36 environment.
3. A basic tox implementation was added to this current work to automate 
   the creation of virtual environments and run the tests.   
4. Running `tox` as configured will install `setup.py develop` and run 
   `setup.py tests` for both `dev27` and `dev36`.
   > Note: the setup.py file indicates that Python 3.4 and 3.5 are also 
   > supported, but they were not tested in this work.
5. PyCharm was used as the IDE.  It complained about missing packages so 
   both additional packages were installed per PyCharm auto-detect of 
   what was missing (see [requirements_dev27_and_dev36](requirements_dev27_and_dev36.md)).

## Test Results
* `/before` directory logs the tox test run - before code changes.
* `/after` directory logs the tox test run - after code changes.

| venv  |            tox test run              |
|:-----:|:------------------------------------:|
| dev36 | /.tox/dev36/bin/python setup.py test |
| dev27 | /.tox/dev27/bin/python setup.py test |

### Python 3.6 (dev36) Test Pareto
|    Status |  before |   after |   delta |
|----------:|--------:|--------:|--------:|
|    failed |      84 |      30 |     -54 |
|    passed |    1232 |    1286 |     +54 |
|   skipped |       3 |       3 |       0 |
|   xfailed |      19 |      19 |       0 |
|   xpassed |       1 |       1 |       0 |
|  warnings |   60836 |   60735 |    -101 |
| test time | 1:21:35 | 1:16:46 | -0:4:49 |

### Python 2.7 (dev27) Test Pareto
|    Status |  before |   after |   delta |
|----------:|--------:|--------:|--------:|
|    failed |      27 |      28 |      +1 |
|    passed |    1290 |    1289 |      -1 |
|   skipped |       3 |       3 |       0 |
|   xfailed |       7 |       7 |       0 |
|   xpassed |      12 |      12 |       0 |
|  warnings |      26 |      26 |       0 |
| test time | 1:28:36 | 1:35:23 | +0:6:47 |
