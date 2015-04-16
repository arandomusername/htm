import numpy as np


class temporal_pooler:
    def __init__(self):
        self.region = 0

    def __set_region(self, region):
        self.region = region

    def run(self, reg):
        self.__set_region(reg)
        self.get_active_neurons()
        self.get_predicited_neurons()
        self.learn()

    def get_active_neurons(self):
        pass

    def get_predicited_neurons(self):
        pass

    def learn(self):
        pass
