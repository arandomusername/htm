import numpy as np
import random


class dendrite_segment:
    cutoff = 0.5
    learning_rate = 0.1  # currently everything is linear

    def __init__(self, input_shape):
        self.shape        = input_shape
        self.pot_synapses = np.empty(self.shape)
        self.per_synapses = np.empty(self.shape)

    def connect_to_input(self, input_positions):
        for xy in input_positions:
            self.pot_synapses[xy] = 1

    def set_potential_synapses(self, matrix):
        self.pot_synapses = matrix

    def random_permanence(self):
        pass

    def get_active_synapses(self):
        actives = np.zeros(self.shape)
        actives[self.synapse_perm > dendrite_segment.cutoff] = 1
        actives[self.synapse_perm <= dendrite_segment.cutoff] = 0
        return actives

    def get_activity_score(self, active_input):
        actives = self.get_active_synapses()
        return np.count_nonzero(np.multiply(actives, active_input))

    def learn(self, active_input):
        overlap_pot = np.multiply(self.pot_synapses, active_input)
        perm_inc    = overlap_pot * self.learning_rate * 2
        self.per_synapses = self.per_synapses - self.learning_rate
        self.per_synapses = self.per_synapses + perm_inc
