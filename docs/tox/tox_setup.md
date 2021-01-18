# [tox](https://tox.readthedocs.io/en/latest/) Setup

The following steps were used to setup an Ubuntu 16.04 development system.  

## Install Python 3.6

Ubuntu 16.04 should come with Python 2.7 and 3.5 already installed.  PyCharm 
has already dropped Python 3.5 so what follows jumps to >= 3.6.

Here are the commands 
```shell
$ sudo apt install python3.6
$ sudo apt install python3.6-dev
$ sudo apt install python3.6-venv
$ python3.6 --version            # 3.6.12
```
The same steps are used to install 3.7, 3.8, and 3.9 by simply changing the 
version number.
```shell
$ sudo apt install python3.7       | python3.8         | python3.9
$ sudo apt install python3.7-dev   | python3.8-dev     | python3.9-dev
$ sudo apt install python3.7-venv  | python3.8-venv    | python3.9-venv
$ python3.7 --version  # 3.7.9     | 3.8.7             | 3.9.1
```

We can now reset the alias (symbolic link) `python3` to point to the new  
Python 3.6.12 installation.
```shell
$ sudo ln -s /usr/bin/python3.6 /usr/local/bin/python3
````

## Install tox
The following strategy is to have a `.venv` virtual environment that only 
has `tox` installed.  This is used to run `tox` (i.e., as defined in `tox.ini`) 
which will then create all the development and test environments (e.g., dev 
in py3.6 and test in py2.7, py3.6, ...).

Install the virtual environment (Python 3.6)
```shell
$ cd <root of arctic project directory>
$ python3 -m venv .venv
```

Activate the virtual environment
```shell
$ source .venv/bin/activate
```

Update the pip
```shell
$ cd <root of arctic project directory>
$ cp -i docs/tox/get-pip.py get-pip.py
(.venv) $ python get-pip.py
(.venv) $ pip install tox
```

### Optional - use the `setpath.sh` script to find the `tox` virtual environment
By doing this the `python` command will now be using the python3.6 you installed 
in `.venv`. 

```shell
(.venv) $ deactivate         # get out of the virtual environment
$ cd <root of arctic project directory>
$ cp -i docs/issue878/setpath.sh setpath.sh
$ source ./setpath.sh        # set terminal path and echo to verify paths

Display executable path and version
~~~~~ pip ~~~~~~~
.venv/bin/pip
pip 20.3.3 from /.venv/lib/python3.
6/site-packages/pip (python 3.6)
~~~~~ python ~~~~
.venv/bin/python
Python 3.6.12
~~~~~ tox ~~~~~~~
.venv/bin/tox
3.21.0 imported from /.venv/lib/python3.

```
## Run `tox`
The initial version of [`tox.ini`](../../tox.ini) for this project is 
formulated to mimic the manual steps outlined in the [contributing]() 
document.  The major benefit is that tox more easily automates the setup 
for all virtual environments needed for development and testing across 
multiple python versions.

Here is the abridged terminal output from setting up the development 
environment:
```shell
(.venv) $ cd <root of arctic project directory>
(.venv) $ tox -e dev

dev create: arctic/.tox/dev
dev installdeps: pytest, pycodestyle
dev develop-inst: arctic
dev installed: -e git+https://.../arctic.git=arctic,
  attrs==20.3.0,
  decorator==4.4.2,
  enum-compat==0.0.3,
  importlib-metadata==3.4.0,
  iniconfig==1.1.1,
  lz4==3.1.1,
  mockextras==1.0.2,
  numpy==1.19.5,
  packaging==20.8,
  pandas==1.1.5,
  pluggy==0.13.1,
  py==1.10.0,
  pycodestyle==2.6.0,
  pymongo==3.11.2,
  pyparsing==2.4.7,
  pytest==6.2.1,
  python-dateutil==2.8.1,
  pytz==2020.5,
  six==1.15.0,
  toml==0.10.2,
  typing-extensions==3.7.4.3,
  tzlocal==2.1,
  zipp==3.4.0
dev run-test-pre: PYTHONHASHSEED='4287678907'
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
testenv:dev
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Package            Version Location
------------------ ------- ---------------------------------------
arctic             1.80.0  /arctic_878
attrs              20.3.0
decorator          4.4.2
enum-compat        0.0.3
importlib-metadata 3.4.0
iniconfig          1.1.1
lz4                3.1.1
mockextras         1.0.2
numpy              1.19.5
packaging          20.8
pandas             1.1.5
pip                20.3.3
pluggy             0.13.1
py                 1.10.0
pycodestyle        2.6.0
pymongo            3.11.2
pyparsing          2.4.7
pytest             6.2.1
python-dateutil    2.8.1
pytz               2020.5
setuptools         51.0.0
six                1.15.0
toml               0.10.2
typing-extensions  3.7.4.3
tzlocal            2.1
wheel              0.36.2
zipp               3.4.0
________________________________________________________________ summary _________________________________________________________________
  dev: commands succeeded
  congratulations :)
$ 
```
`tox.ini` only specified pytest and pycodestyle, all the other packages 
were based on what is defined in the [`setup.py`](../../setup.py) file.

## Cleanup After Running `tox`
Rerunning tox becomes much faster because of the cache created by the first 
run.  The only way to delete this cache is to manually delete all the 
artifact directories and files.  This is a deterministic process simplified 
by running the `clean_after_tox.sh` script from the root directory.

```shell
(.venv) $ cd <root of arctic project directory>
(.venv) $ cd <root of arctic project directory>
(.venv) $ cp -i docs/tox_setup/clean_after_tox.sh clean_after_tox.sh
(.venv) $ sh ./clean_after_tox.sh
```
