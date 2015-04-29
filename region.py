from column import column
from util import pattern_group
import numpy as np


class region(object):
    def __init__(self, size, input_shape):
        self.input_shape    = input_shape
        self.size           = size
        self.columns        = [[]]
        self.pattern        = pattern_group(input_shape, (self.size, self.size))
        self.active_columns = np.zeros((self.size, self.size))
        self.active_neurons = np.zeros((self.size, self.size,
                                        column.neuron_num))

        self.__add_columns()
        self.connect_to_input(input_shape)

    def __add_columns(self):
        self.columns = np.array([[column(self.input_shape, self.size)
                                  for x in range(self.size)]
                                  for y in range(self.size)])

    def get_activation_scores(self, active_input):
        act_arr = np.zeros(shape=(self.size, self.size))
        for x in range(self.size):
            for y in range(self.size):
                act_arr[x, y] = self.columns[x][y].get_activity_score(active_input)
        return act_arr

    def get_column_activation(self):
        return self.active_neurons

    def get_neuron_activation(self):
        return self.active_columns

    def get_columns(self):
        for x in range(self.size):
            for y in range(self.size):
                yield self.columns[x][y]

    def update_column_activation(self, active_list):
        self.active_columns.fill(0)
        for coor in active_list:
            self.active_columns[coor[0], coor[1]] = 1

    def update_neuron_activation(self):
        for pos, value in np.ndemurate(self.columns):
            col = self.columns[pos].get_active_neurons()
            self.active_columns[pos] = col

    def learn(self, active_input):
        for x in range(self.size):
            for y in range(self.size):
                if self.active_columns[x, y] == 1:
                    self.columns[x][y].dendrites.learn(active_input)
                    self.columns[x][y].reset_boost()
                else:
                    self.columns[x][y].increase_boost()

    def connect_to_input(self, input_shape):
        for col in self.get_columns():
            connections = np.random.randint(2, size=input_shape)
            col.dendrites.set_potential_synapses(connections)
            col.dendrites.random_permanence()

    def add_pattern(self, input_pattern):
        self.pattern.add_pattern(input_pattern, self.active_columns)
