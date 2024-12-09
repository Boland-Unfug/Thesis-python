import numpy as np
import pandas as pd
import os

class Data():
    def __init__(self,history, name):
        self.history = history
        self.name = name
        self.make_file(name)
        self.data = pd.DataFrame()



    def write_to_file(self):
        #create the file if it doesn't exist
        if not os.path.exists(name):
            file = open(name, "x")
            file.write(str(self.history))
            file.close()
        #load the data
        self.data = pd.read_csv(self.name, index_col=0)

    def save(self, name, data):
        np.save(name, data)

    def load(self, name):
        return np.load(name)

    def get_data(self):
        return self.data

    def get_name(self):
        return self.name