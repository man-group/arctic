# Getting started with Arctic for Dev

This is a step-by-step guide to get Arctic along with a development environment.


## Linux (Debian based)


### Step 1: Install the python version of your preference and virtualenvwrapper
```
apt-get install virtualenvwrapper
```


### Step 2: Install mongodb server
```
# this will also install mongodb-server
apt-get install mongodb
```
You can also follow the official instructions for the linux distribution of your preference:
[Install MongoDB on Linux](https://docs.mongodb.com/manual/administration/install-on-linux/)


### Step 3: Clone the arctic project locally
```
git clone https://github.com/manahl/arctic.git
```

You can also install it from github:
```
pip install git+https://github.com/manahl/arctic.git
```


### Step 4: Create a new venv
```
mkvirtualenv my_arctic
```


### Step 5: Install mtools
Mtools will help you to launch with one line a personal mongo cluster (with multiple shards, replica sets).



### Step 6: Start/stop a mongodb instance or cluster
Start a simple mongo instance
```
mlaunch init --single --port 27017 --binarypath /your/path/to/mongodb/bin/directory --dir /mnt/mongo/my_single --name my_single
```

Start a cluster
```
mlaunch init --shards 2 --config 1 --mongos 1 --port 27017 --binarypath /your/path/to/mongodb/bin/directory --dir /mnt/mongo/my_cluster --name my_cluster
```

Stop the mongo cluster/instance
```
mlaunch stop --dir /mnt/mongo/my_single

# You can also issue a kill signal
mlaunch kill --dir /mnt/mongo/my_single
```



### Step 7: Start using Arctic
Launch a Python console and type:
```
from arctic import Arctic
import quandl

# Connect to Local MONGODB
store = Arctic('localhost')

# Create the library - defaults to VersionStore
store.initialize_library('NASDAQ')
```

