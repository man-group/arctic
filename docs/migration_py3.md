# Python 3 Migration Gotchas

The aim of this document is to help with possible migration issues with Arctic when moving to python3.

## Trying to store numpy types with bson

Currently if you try and store (say) a numpy integer in BSONStore you will get an encoding failure:  
`In [14]:  lib.insert_one({'a': np.int64(1)})`

```python
    101     request_id, msg, size = message.query(flags, ns, 0, -1, spec,
--> 102                                           None, codec_options, check_keys)
    103 
    104     if (max_bson_size is not None

InvalidDocument: Cannot encode object: 1
```
This is because in python3, numpy types are not json / bson serializable anymore and it throws a rather confusing 
error message which is fixed in py3.7: https://jira.mongodb.org/browse/PYTHON-1664

Arctic does not do the conversion to int from numpy.int types and you should ensure you convert it before passing
the parameters to insert / update functions in BSONStore or wherever there is a bson.encode involved

## Storing pickle in py3 and reading back in py2 fails.

This could be because the default protocol for pickling in py3 is 4 which is not supported in py2 (max supported in python2 = 2).

## Strings in column/index names are converted to bytes in py3

As mentioned here: https://github.com/manahl/arctic/blob/master/arctic/serialization/numpy_records.py#L277 this can
break the workflow of people migrating and you should be using unicode in py2 to avoid running into this or you can use
`from __future__ import unicode_literals` to always use unicode instead of bytes by default in py2.

If you hit this issue, a workaround is to set: [FORCE_BYTES_TO_UNICODE](https://github.com/manahl/arctic/blob/master/arctic/_config.py#L92)
which will explicitly convert stuff to unicode, but keep in mind it's not very efficient and is basically doing
a linear conversion. 
