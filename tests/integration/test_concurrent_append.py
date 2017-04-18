from arctic.exceptions import OptimisticLockException
from datetime import datetime, timedelta
from pandas.core.frame import DataFrame
import time
import random
from multiprocessing import Process, Semaphore
from arctic.arctic import Arctic


class Appender(object):

    def __init__(self, mongo_server, library_name, sem, counter_init, runtime=30):
        super(Appender, self).__init__()
        self.lib = Arctic(mongo_server)[library_name]
        self.sem = sem
        self.begin = counter_init
        self.last = counter_init
        self.timeout = datetime.now() + timedelta(seconds=runtime)

    def run(self):
        self.sem.acquire()
        while datetime.now() < self.timeout:
            try:
                # Randomy length dataframe to keep appending to
                df = DataFrame({'v': [self.last]}, [datetime.now()])
                for i in range(random.randint(1, 10)):
                    df = df.append(DataFrame({'v': [self.last + i]}, [datetime.now()]))
                self.last + i
                df.index.name = 'index'
                self.lib.append('symbol', df)
                assert self.last in self.lib.read('symbol').data['v'].tolist()
                self.last += 2
            except OptimisticLockException:
                # Concurrent write, not successful
                pass
#             time.sleep(self.begin)

    def check_written_data_exists(self):
        values = self.lib.read('symbol').data['v'].tolist()
        assert len(set(values)) == len(values), "Written: %s" % values
        i = self.begin
        while i < self.last:
            assert i in values, "Missing %s in %s" % (i, values)
            i += 2


def test_append_kill(library, mongo_host, library_name):
    # Empty DF to start
    df = DataFrame({'v': []}, [])
    df.index.name = 'index'
    library.write('symbol', df)

    sem = Semaphore(0)

    def run_append(end):
        app_1 = Appender(mongo_host, library_name, sem, 0, end)
        proc = Process(target=app_1.run)
        proc.start()
        sem.release()
        return proc

    def check_written():
        sym = library.read('symbol')
        print("Checking written %d" % len(sym.data))

    # time how long it takes to do an append operation
    start = datetime.now()
    proc = run_append(1)
    proc.join()
    check_written()
    time_taken = (datetime.now() - start).total_seconds()

    for i in range(100):
        print("Loop %d" % i)
        proc = run_append(100)
        # kill it randomly
        time.sleep(2 * (random.random() * time_taken))
        # Forcibly kill it
        proc.terminate()
        # Check we can read the data
        check_written()
