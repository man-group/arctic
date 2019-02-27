import arctic.asynchronous as aasync


def test_async_arctic():
    print(aasync.ASYNC_ARCTIC.total_alive_tasks())
