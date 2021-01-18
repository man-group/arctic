(.venv) cwm@flxsa02:~/git/bb.FLXSA/quant/arctic_878$ tox -e benchmark27

benchmark27 create: /home/cwm/git/bb.FLXSA/quant/arctic_878/.tox/benchmark27
benchmark27 installdeps: -r/home/cwm/git/bb.FLXSA/quant/arctic_878/asv/requirements-dev.txt
benchmark27 develop-inst: /home/cwm/git/bb.FLXSA/quant/arctic_878
benchmark27 installed: DEPRECATION: Python 2.7 reached the end of its life on January 1st, 2020. Please upgrade your Python as Python 2.7 is no longer maintained. pip 21.0 will drop support for Python 2.7 in January 2021. More details about Python 2 support in pip can be found at https://pip.pypa.io/en/latest/development/release-process/#python-2-support pip 21.0 will remove support for this functionality.,apipkg==1.5,appdirs==1.4.4,-e git+https://github.com/c-w-m/arctic.git@8ddd83138995fefce54fa3812dfdc59929a9a2c8#egg=arctic,atomicwrites==1.4.0,attrs==20.3.0,backports.functools-lru-cache==1.6.1,configparser==4.0.2,contextlib2==0.6.0.post1,decorator==4.4.2,distlib==0.3.1,enum-compat==0.0.3,enum34==1.1.10,execnet==1.7.1,feedparser==5.2.1,filelock==3.0.12,funcsigs==1.0.2,future==0.18.2,futures==3.3.0,importlib-metadata==2.1.1,importlib-resources==3.3.1,lz4==2.2.1,mock==3.0.5,mockextras==1.0.2,more-itertools==5.0.0,numpy==1.16.6,packaging==20.8,pandas==0.24.2,pathlib2==2.3.5,pluggy==0.13.1,py==1.10.0,pymongo==3.11.2,pyparsing==2.4.7,pytest==4.6.11,pytest-faulthandler==2.0.1,pytest-forked==1.3.0,pytest-rerunfailures==9.0,pytest-timeout==1.4.2,pytest-xdist==1.34.0,python-dateutil==2.8.1,python-hglib==2.6.2,pytz==2020.5,scandir==1.10.0,scipy==1.2.3,selenium==3.141.0,singledispatch==3.4.0.3,six==1.15.0,typing==3.7.4.3,tzlocal==2.1,urllib3==1.26.2,virtualenv==20.3.1,wcwidth==0.2.5,zipp==1.2.0
benchmark27 run-test-pre: PYTHONHASHSEED='1160331743'
benchmark27 run-test: commands[0] | python -c 'print((80*"~")+"\ntestenv:benchmark-python2.7\n"+(80*"~"))'
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
testenv:benchmark-python2.7
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
benchmark27 run-test: commands[1] | python setup.py develop
/home/cwm/git/bb.FLXSA/quant/arctic_878/.tox/benchmark27/lib/python2.7/site-packages/setuptools/dist.py:485: UserWarning: The version specified (u'0.5.dev0+') is an invalid version, this may not work as expected with newer versions of setuptools, pip, and PyPI. Please see PEP 440 for more details.
  "details." % self.metadata.version
running develop
running egg_info
writing entry points to asv.egg-info/entry_points.txt
writing requirements to asv.egg-info/requires.txt
writing asv.egg-info/PKG-INFO
writing dependency_links to asv.egg-info/dependency_links.txt
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
copying build/lib.linux-x86_64-2.7/asv/_rangemedian.so -> asv
Creating /home/cwm/git/bb.FLXSA/quant/arctic_878/.tox/benchmark27/lib/python2.7/site-packages/asv.egg-link (link to .)
Adding asv 0.5.dev0- to easy-install.pth file
Installing asv script to /home/cwm/git/bb.FLXSA/quant/arctic_878/.tox/benchmark27/bin

Installed /home/cwm/git/bb.FLXSA/quant/arctic_878/asv
Processing dependencies for asv===0.5.dev0-
Searching for six==1.15.0
Best match: six 1.15.0
Adding six 1.15.0 to easy-install.pth file

Using /home/cwm/git/bb.FLXSA/quant/arctic_878/.tox/benchmark27/lib/python2.7/site-packages
Finished processing dependencies for asv===0.5.dev0-
benchmark27 run-test: commands[2] | python -m pip list --format=columns
DEPRECATION: Python 2.7 reached the end of its life on January 1st, 2020. Please upgrade your Python as Python 2.7 is no longer maintained. pip 21.0 will drop support for Python 2.7 in January 2021. More details about Python 2 support in pip can be found at https://pip.pypa.io/en/latest/development/release-process/#python-2-support pip 21.0 will remove support for this functionality.
Package                       Version     Location
----------------------------- ----------- -------------------------------------------
apipkg                        1.5
appdirs                       1.4.4
arctic                        1.80.0      /home/cwm/git/bb.FLXSA/quant/arctic_878
asv                           0.5.dev0-   /home/cwm/git/bb.FLXSA/quant/arctic_878/asv
atomicwrites                  1.4.0
attrs                         20.3.0
backports.functools-lru-cache 1.6.1
configparser                  4.0.2
contextlib2                   0.6.0.post1
decorator                     4.4.2
distlib                       0.3.1
enum-compat                   0.0.3
enum34                        1.1.10
execnet                       1.7.1
feedparser                    5.2.1
filelock                      3.0.12
funcsigs                      1.0.2
future                        0.18.2
futures                       3.3.0
importlib-metadata            2.1.1
importlib-resources           3.3.1
lz4                           2.2.1
mock                          3.0.5
mockextras                    1.0.2
more-itertools                5.0.0
numpy                         1.16.6
packaging                     20.8
pandas                        0.24.2
pathlib2                      2.3.5
pip                           20.3.3
pluggy                        0.13.1
py                            1.10.0
pymongo                       3.11.2
pyparsing                     2.4.7
pytest                        4.6.11
pytest-faulthandler           2.0.1
pytest-forked                 1.3.0
pytest-rerunfailures          9.0
pytest-timeout                1.4.2
pytest-xdist                  1.34.0
python-dateutil               2.8.1
python-hglib                  2.6.2
pytz                          2020.5
scandir                       1.10.0
scipy                         1.2.3
selenium                      3.141.0
setuptools                    44.1.1
singledispatch                3.4.0.3
six                           1.15.0
typing                        3.7.4.3
tzlocal                       2.1
urllib3                       1.26.2
virtualenv                    20.3.1
wcwidth                       0.2.5
wheel                         0.36.2
zipp                          1.2.0

benchmark27 run-test: commands[3] | python -c 'print(r'"'"'/home/cwm/git/bb.FLXSA/quant/arctic_878/.tox/benchmark27/bin/python'"'"')'
/home/cwm/git/bb.FLXSA/quant/arctic_878/.tox/benchmark27/bin/python

benchmark27 run-test: commands[4] | pip freeze

DEPRECATION: Python 2.7 reached the end of its life on January 1st, 2020. Please upgrade your Python as Python 2.7 is no longer maintained. pip 21.0 will drop support for Python 2.7 in January 2021. More details about Python 2 support in pip can be found at https://pip.pypa.io/en/latest/development/release-process/#python-2-support pip 21.0 will remove support for this functionality.
apipkg==1.5
appdirs==1.4.4
-e git+https://github.com/c-w-m/arctic.git@8ddd83138995fefce54fa3812dfdc59929a9a2c8#egg=arctic
-e git+https://github.com/airspeed-velocity/asv.git@35251cd5ca3964c96287db79bc08881201a619d2#egg=asv&subdirectory=../../asv
atomicwrites==1.4.0
attrs==20.3.0
backports.functools-lru-cache==1.6.1
configparser==4.0.2
contextlib2==0.6.0.post1
decorator==4.4.2
distlib==0.3.1
enum-compat==0.0.3
enum34==1.1.10
execnet==1.7.1
feedparser==5.2.1
filelock==3.0.12
funcsigs==1.0.2
future==0.18.2
futures==3.3.0
importlib-metadata==2.1.1
importlib-resources==3.3.1
lz4==2.2.1
mock==3.0.5
mockextras==1.0.2
more-itertools==5.0.0
numpy==1.16.6
packaging==20.8
pandas==0.24.2
pathlib2==2.3.5
pluggy==0.13.1
py==1.10.0
pymongo==3.11.2
pyparsing==2.4.7
pytest==4.6.11
pytest-faulthandler==2.0.1
pytest-forked==1.3.0
pytest-rerunfailures==9.0
pytest-timeout==1.4.2
pytest-xdist==1.34.0
python-dateutil==2.8.1
python-hglib==2.6.2
pytz==2020.5
scandir==1.10.0
scipy==1.2.3
selenium==3.141.0
singledispatch==3.4.0.3
six==1.15.0
typing==3.7.4.3
tzlocal==2.1
urllib3==1.26.2
virtualenv==20.3.1
wcwidth==0.2.5
zipp==1.2.0

_____________________________________________________________ summary ______________________________________________________________
  benchmark27: commands succeeded
  congratulations :)
