# Tickstore

As the name suggests, tickstore is used for storing stream of ticks from
financial exchanges. For example, this could be the bid/offers to an exchange.

It's designed for read heavy loads and realtime, continous ticks of data and you are
expected to do the batching on your side, generally done with a message queue
like kafka / redis queue etc.

## Reading and Writing data with Tickstore

TBD.
