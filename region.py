from column import column
import numpy as np


class region(object):
    def __init__(self, size, input_shape):
        self.input_shape = input_shape
        self.size = size
        self.columns = [[]]
        self.active_columns = np.zeros((self.size, self.size))
        self.__add_columns()
        self.connect_to_input(input_shape)

    def __add_columns(self):
        self.columns = [[column(self.input_shape) for x in range(self.size)]
                                        for y in range(self.size)]

    def gen_columns(self):
        for col in self.columns:
            for row in col:
                yield row

    def get_activation_scores(self, active_input):
        act_arr = np.zeros(shape=(self.size, self.size))
        for x in range(self.size):
            for y in range(self.size):
                act_arr[x, y] = self.columns[x][y].get_activity_score(active_input)
        return act_arr

    def update_activation(self, active_list):
        self.active_columns.fill(0)
        for coor in active_list:
            self.active_columns[coor[0], coor[1]] = 1

    def get_activation(self):
        return self.active_columns

    def learn(self, active_input):
        for x in range(self.size):
            for y in range(self.size):
                if self.active_columns[x, y] == 1:
                    self.columns[x][y].dendrites.learn(active_input)
                else:
                    self.columns[x][y].increase_boost()

    def connect_to_input(self, input_shape):
        for col in self.gen_columns():
            connections = np.random.randint(2, size=input_shape)
            col.dendrites.set_potential_synapses(connections)
            col.dendrites.random_permanence()
