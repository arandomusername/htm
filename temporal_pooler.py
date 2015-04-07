import numpy as np


class temporal_pooler:
    activation_percentage = .3

    def __init__(self, reg):
        self.region = reg

    def __set_region(self, region):
        self.region = region

    def run(self, region):
        self.__set_region(region)
        self.select_activated()

    def select_activated(self):
        activation_array = self.region.get_activation_matrix()
        pass

    def learn(self):
        pass
