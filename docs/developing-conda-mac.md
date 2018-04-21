# Running on Mac OS X - tested on 10.13.4

## Install XCode from the Mac App Store

## Install the Mac OS X headers

```
xcode-select --install
```

## Install conda - create env - install anaconda

https://conda.io/miniconda.html

```
~/Downloads/Miniconda3-latest-MacOSX-x86_64-2.sh
```

## Build and activate conda env

```
conda create -n 201804 python
source activate 201804
```

## Install packages in the env

```
conda install anaconda
conda install pymongo
```

## Build and install arctic

```
git clone git@github.com:manahl/arctic.git
cd arctic
python setup.py develop
```

## Run MongoD

```
mongod --dbpath mongo_tmp/
```

## Connect and test arctic

```
ipython
from arctic import Arctic
a = Arctic('localhost')
a.initialize_library('test')
l = a['test']
l.write('thing', object())
```

## Issues

### tzlocal issue with pytz == 1.5.1

```
  ```File "<frozen importlib._bootstrap>", line 441, in spec_from_loader
  File "<frozen importlib._bootstrap_external>", line 544, in spec_from_file_location
  File "/Users/james/miniconda3/envs/201804/lib/python3.6/site-packages/tzlocal-1.5.1-py3.6.egg/tzlocal/unix.py", line 77
SyntaxError: invalid escape sequence \s
```

`pip install pytz==1.4`

### Mongo not finding mongod

```
>               raise child_exception_type(errno_num, err_msg, err_filename)
E               FileNotFoundError: [Errno 2] No such file or directory: '/usr/bin/mongod': '/usr/bin/mongod'
```

Point at the directory that contains the `mongod` command

```
export SERVER_FIXTURES_MONGO_BIN=/Users/james/bin/
```

### Tests hanging 

This is a pytest-server-fixtures issue compatibility with MongoDB 3.6. 
Use MongoDB 3.4...

### lz4 compression issue

```
>   [lz4.decompress(y) for y in [lz4.compressHC(x) for x in _strarr]]
E   AttributeError: module 'lz4' has no attribute 'compressHC'
```

Fix the integration test to be compatible with new lz4 `lz4.compress` /