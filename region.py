from column import column
import numpy as np


class region(object):
    def __init__(self, size):
        self.size = size
        self.columns = [[]]

        self.__add_columns()

    def __add_columns(self):
        self.columns = [[column([x, y]) for x in range(self.size)]
                                        for y in range(self.size)]

    def get_activation_matrix(self):
        act_arr = np.zeros(shape=(self.size, self.size))
        for x in range(self.size):
            for y in range(self.size):
                act_arr[x, y] = self.columns[x][y].get_activity_score()
        return act_arr

    def get_active_column_matrix(self):
        act_arr = np.zeros(shape=(self.size, self.size))
        for x in range(self.size):
            for y in range(self.size):
                act_arr[x, y] = self.columns[x][y].get_activity
        return act_arr

    def get_active_neuron_matrix(self):
        arr_shape = (self.size, self.size, column.neuron_num)
        act_arr   = np.zeros(shape=arr_shape)
        for x in range(self.size):
            for y in range(self.size):
                neur_arr = self.column[x][y].get_neur_arr()
