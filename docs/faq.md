# Frequently Asked Questions

## What is arctic?

Arctic is a high performance datastore for numeric data. It supports [Pandas](http://pandas.pydata.org/),
[numpy](http://www.numpy.org/) arrays and pickled objects out-of-the-box, with pluggable support for
other data types and optional versioning.

## What are advantages of Arctic?

Arctic can query millions of rows per second per client, achieves ~10x compression on network bandwidth,
~10x compression on disk, and scales to hundreds of millions of rows per second per
[MongoDB](https://www.mongodb.org/) instance.

Other benefits are:-
* Serializes a number of data types eg. Pandas DataFrames, Numpy arrays, Python objects via pickling etc. so you don't have to handle different datatypes manually.
* Uses LZ4 compression by default on the client side to get big savings on network / disk.
* Allows you to version different stages of an object and snapshot the state (In some ways similar to git), and allows you to freely experiment and then just revert back the snapshot. [VersionStore only]
* Does the chunking (breaking a Dataframe to smaller part* for you.
* Adds a concept of Users and per User Libraries which can build on Mongo's auth.
* Has different types of Stores, each with it's own benefits. Eg. Versionstore allows you to version and snapshot stuff, TickStore is for storage and highly efficient retrieval of streaming data, ChunkStore allows you to chunk and efficiently retrieve ranges of chunks. If nothing suits you, feel free to use vanilla Mongo commands with BSONStore.
* Restricts data access to Mongo and thus prevents ad hoc queries on unindexed / unsharded collections


## Differences between VersionStore and TickStore?

Tickstore is for tick style data generally via streaming, VersionStore is for playing around with data. It keeps versions so you can 'undo' changes and keep track of updates.

## Which Store should I use?

* VersionStore: This is the default Store type. This gives you the ability to Version and Snapshot your objects while doing the serialization, compression etc alongside it. This is useful as you can basically play with your data and revert back to an older state if needed
* ChunkStore: Use ChunkStore when you don't care about versioning, and want to store DataFrames into user defined chunks with fast reads.
* TickStore: When you are storing constant tick data (eg. buy / sell info from exchanges). This generally plays well with Kafka / other message brokers.
* BSONStore: For basically using raw Mongo operations via arctic. Can be used for storing ad-hoc data.

## Why Mongo?

This [video](https://vimeo.com/album/3660528/video/145842301) goes into why we
chose Mongo as the backend for Arctic.

## I'm running Mongo in XXXX setup - what performance should I expect?
We're constantly asked what the expected performance of Arctic is/should be for given configurations and Mongo cluster setups. Its hard to know for sure given the enormous number of ways Mongo, networks, machines, workstations, etc can be configured. MongoDB performance tuning is outside the scope of this library, but countless tutorials and examples are available via a quick search of the Internet.


## Thread safety

VersionStore is thread safe, and operations that are interrupted should never corrupt the data, based on us writing the data segments first and then the pointers to it. This could leak data in cases though.
