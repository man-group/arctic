# Frequently Asked Questions

## What is arctic?

Arctic is a high performance datastore for numeric data. It supports [Pandas](http://pandas.pydata.org/),
[numpy](http://www.numpy.org/) arrays and pickled objects out-of-the-box, with pluggable support for
other data types and optional versioning.

## What are advantages of Arctic?

Arctic can query millions of rows per second per client, achieves ~10x compression on network bandwidth,
~10x compression on disk, and scales to hundreds of millions of rows per second per
[MongoDB](https://www.mongodb.org/) instance.

## Differences between VersionStore and TickStore?

tickstore is for constant streams of data, version store is for working with data
(i.e. playing around with it). It keeps versions so you can 'undo' changes and keep
track of updates.

## Which Store should I use?

* VersionStore: when ..
* ChunkStore: when ..
* TickStore: when ..

## Why Mongo?

This [video](https://vimeo.com/album/3660528/video/145842301) goes into why we
chose Mongo as the backend for Arctic.

... Work in Progress.
