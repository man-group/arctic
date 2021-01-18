(.venv) cwm@flxsa02:~/git/bb.FLXSA/quant/arctic_878$ tox -e benchmark36

benchmark36 create: /home/cwm/git/bb.FLXSA/quant/arctic_878/.tox/benchmark36
benchmark36 installdeps: -r/home/cwm/git/bb.FLXSA/quant/arctic_878/asv/requirements-dev.txt
benchmark36 develop-inst: /home/cwm/git/bb.FLXSA/quant/arctic_878
benchmark36 installed: apipkg==1.5,appdirs==1.4.4,-e git+https://github.com/c-w-m/arctic.git@8ddd83138995fefce54fa3812dfdc59929a9a2c8#egg=arctic,attrs==20.3.0,decorator==4.4.2,distlib==0.3.1,enum-compat==0.0.3,execnet==1.7.1,feedparser==6.0.2,filelock==3.0.12,importlib-metadata==3.4.0,importlib-resources==5.0.0,iniconfig==1.1.1,lz4==3.1.2,mockextras==1.0.2,numpy==1.19.5,packaging==20.8,pandas==1.1.5,pluggy==0.13.1,py==1.10.0,pymongo==3.11.2,pyparsing==2.4.7,pytest==6.2.1,pytest-faulthandler==2.0.1,pytest-forked==1.3.0,pytest-rerunfailures==9.1.1,pytest-timeout==1.4.2,pytest-xdist==2.2.0,python-dateutil==2.8.1,python-hglib==2.6.2,pytz==2020.5,scipy==1.5.4,selenium==3.141.0,sgmllib3k==1.0.0,six==1.15.0,toml==0.10.2,typing-extensions==3.7.4.3,tzlocal==2.1,urllib3==1.26.2,virtualenv==20.3.1,zipp==3.4.0
benchmark36 run-test-pre: PYTHONHASHSEED='1995300836'
benchmark36 run-test: commands[0] | python -c 'print((80*"~")+"\ntestenv:benchmark-python3.6\n"+(80*"~"))'
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
testenv:benchmark-python3.6
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
benchmark36 run-test: commands[1] | python setup.py develop
/home/cwm/git/bb.FLXSA/quant/arctic_878/.tox/benchmark36/lib/python3.6/site-packages/setuptools/dist.py:470: UserWarning: The version specified ('0.5.dev0+') is an invalid version, this may not work as expected with newer versions of setuptools, pip, and PyPI. Please see PEP 440 for more details.
  "details." % version
running develop
running egg_info
writing asv.egg-info/PKG-INFO
writing dependency_links to asv.egg-info/dependency_links.txt
writing entry points to asv.egg-info/entry_points.txt
writing requirements to asv.egg-info/requires.txt
writing top-level names to asv.egg-info/top_level.txt
reading manifest file 'asv.egg-info/SOURCES.txt'
reading manifest template 'MANIFEST.in'
warning: no files found matching 'pip_requirements.txt'
warning: no files found matching '*.txt' under directory 'docs'
no previously-included directories found matching 'docs/build'
no previously-included directories found matching 'build'
warning: no previously-included files matching '*.pyc' found anywhere in distribution
warning: no previously-included files matching '*.o' found anywhere in distribution
warning: no previously-included files matching '__pycache__' found anywhere in distribution
writing manifest file 'asv.egg-info/SOURCES.txt'
running build_ext
copying build/lib.linux-x86_64-3.6/asv/_rangemedian.cpython-36m-x86_64-linux-gnu.so -> asv
Creating /home/cwm/git/bb.FLXSA/quant/arctic_878/.tox/benchmark36/lib/python3.6/site-packages/asv.egg-link (link to .)
Adding asv 0.5.dev0- to easy-install.pth file
Installing asv script to /home/cwm/git/bb.FLXSA/quant/arctic_878/.tox/benchmark36/bin

Installed /home/cwm/git/bb.FLXSA/quant/arctic_878/asv
Processing dependencies for asv===0.5.dev0-
Searching for six==1.15.0
Best match: six 1.15.0
Adding six 1.15.0 to easy-install.pth file

Using /home/cwm/git/bb.FLXSA/quant/arctic_878/.tox/benchmark36/lib/python3.6/site-packages
Finished processing dependencies for asv===0.5.dev0-

benchmark36 run-test: commands[2] | python -m pip list --format=columns

Package              Version   Location
-------------------- --------- -------------------------------------------
apipkg               1.5
appdirs              1.4.4
arctic               1.80.0    /home/cwm/git/bb.FLXSA/quant/arctic_878
asv                  0.5.dev0- /home/cwm/git/bb.FLXSA/quant/arctic_878/asv
attrs                20.3.0
decorator            4.4.2
distlib              0.3.1
enum-compat          0.0.3
execnet              1.7.1
feedparser           6.0.2
filelock             3.0.12
importlib-metadata   3.4.0
importlib-resources  5.0.0
iniconfig            1.1.1
lz4                  3.1.2
mockextras           1.0.2
numpy                1.19.5
packaging            20.8
pandas               1.1.5
pip                  20.3.3
pluggy               0.13.1
py                   1.10.0
pymongo              3.11.2
pyparsing            2.4.7
pytest               6.2.1
pytest-faulthandler  2.0.1
pytest-forked        1.3.0
pytest-rerunfailures 9.1.1
pytest-timeout       1.4.2
pytest-xdist         2.2.0
python-dateutil      2.8.1
python-hglib         2.6.2
pytz                 2020.5
scipy                1.5.4
selenium             3.141.0
setuptools           51.1.2
sgmllib3k            1.0.0
six                  1.15.0
toml                 0.10.2
typing-extensions    3.7.4.3
tzlocal              2.1
urllib3              1.26.2
virtualenv           20.3.1
wheel                0.36.2
zipp                 3.4.0

benchmark36 run-test: commands[3] | python -c 'print(r'"'"'/home/cwm/git/bb.FLXSA/quant/arctic_878/.tox/benchmark36/bin/python'"'"')'
/home/cwm/git/bb.FLXSA/quant/arctic_878/.tox/benchmark36/bin/python

benchmark36 run-test: commands[4] | pip freeze

apipkg==1.5
appdirs==1.4.4
-e git+https://github.com/c-w-m/arctic.git@8ddd83138995fefce54fa3812dfdc59929a9a2c8#egg=arctic
-e git+https://github.com/airspeed-velocity/asv.git@35251cd5ca3964c96287db79bc08881201a619d2#egg=asv&subdirectory=../../asv
attrs==20.3.0
decorator==4.4.2
distlib==0.3.1
enum-compat==0.0.3
execnet==1.7.1
feedparser==6.0.2
filelock==3.0.12
importlib-metadata==3.4.0
importlib-resources==5.0.0
iniconfig==1.1.1
lz4==3.1.2
mockextras==1.0.2
numpy==1.19.5
packaging==20.8
pandas==1.1.5
pluggy==0.13.1
py==1.10.0
pymongo==3.11.2
pyparsing==2.4.7
pytest==6.2.1
pytest-faulthandler==2.0.1
pytest-forked==1.3.0
pytest-rerunfailures==9.1.1
pytest-timeout==1.4.2
pytest-xdist==2.2.0
python-dateutil==2.8.1
python-hglib==2.6.2
pytz==2020.5
scipy==1.5.4
selenium==3.141.0
sgmllib3k==1.0.0
six==1.15.0
toml==0.10.2
typing-extensions==3.7.4.3
tzlocal==2.1
urllib3==1.26.2
virtualenv==20.3.1
zipp==3.4.0

_____________________________________________________________ summary ______________________________________________________________
  benchmark36: commands succeeded
  congratulations :)
