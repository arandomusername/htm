from column import column
import numpy as np


class region(object):
    def __init__(self, size):
        self.size = size
        self.columns = [[]]
        self.active_columns = np.zeros((self.size, self.size))
        self.__add_columns()

    def __add_columns(self):
        self.columns = [[column([x, y]) for x in range(self.size)]
                                        for y in range(self.size)]

    def get_activation_scores(self):
        act_arr = np.zeros(shape=(self.size, self.size))
        for x in range(self.size):
            for y in range(self.size):
                act_arr[x, y] = self.columns[x][y].get_activity_score()
        return act_arr

    def update_activation(self, active_list):
        self.active_columns.fill(0)
        for coor in active_list:
            self.active_columns[coor[0], coor[1]] = 1

    def get_activation(self):
        return self.active_columns

    def update_active_neuron_matrix(self):
        pass
