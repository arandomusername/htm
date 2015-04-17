import numpy as np


class dendrite_segment:
    cutoff = 0.4
    learning_rate = 0.1  # currently everything is linear

    def __init__(self, input_shape):
        self.shape        = input_shape
        self.pot_synapses = np.zeros(self.shape)
        self.per_synapses = np.zeros(self.shape)

    def connect_to_input(self, input_positions):
        for pos in input_positions:
            self.pot_synapses[pos] = 1

    def connect_to_all(self):
        self.pot_synapses.fill(1)

    def set_potential_synapses(self, matrix):
        self.pot_synapses = matrix

    def random_permanence(self):
        rand_arr = np.random.random(self.shape)
        self.per_synapses = np.multiply(rand_arr, self.pot_synapses)

    def get_active_synapses(self):
        actives = np.zeros(self.shape)
        actives[self.per_synapses > dendrite_segment.cutoff] = 1
        actives[self.per_synapses <= dendrite_segment.cutoff] = 0
        return actives

    def get_activity_score(self, active_input):
        actives = self.get_active_synapses()
        return np.count_nonzero(np.multiply(actives, active_input))

    def learn(self, active_input):
        overlap_pot = np.multiply(self.pot_synapses, active_input)
        perm_inc    = overlap_pot * self.learning_rate * 2
        self.per_synapses = self.per_synapses - self.learning_rate
        self.per_synapses = self.per_synapses + perm_inc
