"""
Copyright (C) 2020 Man Group
For a list of authors, see README.md; for the license, see file LICENSE in project root directory.
"""
import arctic.asynchronous as aasync


def test_async_arctic():
    print(aasync.ASYNC_ARCTIC.total_alive_tasks())
