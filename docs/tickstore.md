# Tickstore

As the name suggests, tickstore is used for storing stream of ticks from
financial exchanges. For example, this could be the bid/offers to an exchange.

It's designed for read heavy loads and realtime, continuous ticks of data and you are
expected to do the batching on your side, generally done with a message queue
like kafka / redis queue etc.

## Reading and Writing data with Tickstore

Sample tick:

```python
    sample_ticks = [
    {
            'ASK': 1545.25,
            'ASKSIZE': 1002.0,
            'BID': 1545.0,
            'BIDSIZE': 55.0,
            'CUMVOL': 2187387.0,
            'DELETED_TIME': 0,
            'INSTRTYPE': 'FUT',
            'PRICE': 1545.0,
            'SIZE': 1.0,
            'TICK_STATUS': 0,
            'TRADEHIGH': 1561.75,
            'TRADELOW': 1537.25,
            'index': 1185076787070
        },
        {
            'CUMVOL': 354.0,
            'DELETED_TIME': 0,
            'PRICE': 1543.75,
            'SIZE': 354.0,
            'TRADEHIGH': 1543.75,
            'TRADELOW': 1543.75,
            'index': 1185141600600
        }
    ]

```

### Writing and reading to tickstore

 tickstore_lib.write('FEED::SYMBOL', sample_ticks)

 df = tickstore_lib.read('FEED::SYMBOL', columns=['BID', 'ASK', 'PRICE'])

Another example with datetime index with tz_info
```python
    data = [{'A': 120, 'D': 1}, {'A': 122, 'B': 2.0}, {'A': 3, 'B': 3.0, 'D': 1}]
    tick_index = [dt(2013, 6, 1, 12, 00, tzinfo=mktz('UTC')),
                  dt(2013, 6, 1, 11, 00, tzinfo=mktz('UTC')),  # Out-of-order
                  dt(2013, 6, 1, 13, 00, tzinfo=mktz('UTC'))]
    data = pd.DataFrame(data, index=tick_index)

    tickstore_lib._chunk_size = 3
    tickstore_lib.write('SYM', data)
    tickstore_lib.read('SYM', columns=None)
```

## Usecases

* Storing billions of ticks in a compressed way with fast querying by date ranges.
* Customizable chunk sizes. The default is 100k, which should fit easily in a single mongo doc for fast reads.
* Structured to work with financial tick data stored on a per symbol basis. Generally used with kafka / redis queue or
some sort of message broker for streaming data.

See [James's talk](https://vimeo.com/showcase/3660528/video/145842301) for more details