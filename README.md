# [![arctic](https://raw.githubusercontent.com/man-group/arctic/master/logo/arctic_50.png?raw=true)](https://github.com/man-group/arctic) [Arctic TimeSeries and Tick store](https://github.com/man-group/arctic)


[![Documentation Status](https://readthedocs.org/projects/arctic/badge/?version=latest)](https://arctic.readthedocs.io/en/latest/?badge=latest)
[![CircleCI](https://circleci.com/gh/man-group/arctic/tree/master.svg?style=shield)](https://app.circleci.com/pipelines/github/man-group/arctic?branch=master)
[![PyPI](https://img.shields.io/pypi/v/arctic)](https://pypi.org/project/arctic)
[![Python](https://img.shields.io/badge/Python-3.6|3.7|3.8-green.svg)](https://github.com/man-group/arctic)
[![Join the chat at https://gitter.im/man-group/arctic](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/man-group/arctic?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

Arctic is a high performance datastore for numeric data. It supports [Pandas](http://pandas.pydata.org/),
[numpy](http://www.numpy.org/) arrays and pickled objects out-of-the-box, with pluggable support for
other data types and optional versioning.

Arctic can query millions of rows per second per client, achieves ~10x compression on network bandwidth,
~10x compression on disk, and scales to hundreds of millions of rows per second per
[MongoDB](https://www.mongodb.org/) instance.

Arctic has been under active development at [Man Group](https://www.man.com/) since 2012.

---

## :mega: ArcticDB coming soon! :mega:

[ArcticDB](https://www.man.com/man-group-brings-powerful-dataframe-database-product-arcticdb-to-market-with-bloomberg), Man Group's high-performance Python-native DataFrame database will soon be available on GitHub. ArcticDB is the next generation of Arctic and is designed to be a drop-in replacement for Arctic, providing a platform that is:

* **Fast**: Capable of processing billions of rows in seconds
* **Flexible**: Designed to handle complex real-world datasets
* **Familiar**: Built for the modern Python Data Science ecosystem - Pandas In/Pandas Out!

This repository **does not contain the code for ArcticDB**, but instead contains the older (first) version of the Arctic platform. Please note that this repository is now in maintenance mode and all ongoing development efforts will be focused on ArcticDB.

If you would like information on ArcticDB prior to the public release, please get in touch with us at arcticdb@man.com. 

---

Information on how to set up, install and use Arctic has been migrated to [README-arctic.md](README-arctic.md). 

Note that as explained in the above message, this repository is in maintenance mode as ongoing development has migrated to **ArcticDB**, our next-generation high-performance DataFrame database.
