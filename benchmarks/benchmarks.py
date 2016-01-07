from arctic import Arctic
import pandas as pd
from datetime import datetime as dt

class TimeSuite:
    def setup(self):
        self.store = Arctic("127.0.0.1")
        self.store.initalize_library('test.lib')
        self.lib = self.store['test.lib']

    def time_add_data(self):
       df =  pd.DataFrame({'prices': [1, 2, 3]}, [dt(2014, 1, 1), dt(2014, 1, 2), dt(2014, 1, 3)])
       self.lib.write('TEST', df) 

