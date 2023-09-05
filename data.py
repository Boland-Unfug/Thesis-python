import numpy as np
import pandas as pd
import os

class Data():
    def __init__(self,game, name):
        self.game = game
        self.name = name
        self.make_file(name)
        self.data = pd.DataFrame()


    def make_file(self, name):
        if not os.path.exists(name):
            os.makedirs(name)

    def write_to_file(self):
        #create the file if it doesn't exist
        self.makefile(self.name)
        #load the data
        self.data = pd.read_csv(self.name, index_col=0)
        #add the new data
        self.data = self.data.append(data, ignore_index=True)
        #save the data
        self.data.to_csv(name)

    def save(self, name, data):
        np.save(name, data)

    def load(self, name):
        return np.load(name)

    def get_data(self):
        return self.data

    def get_name(self):
        return self.name