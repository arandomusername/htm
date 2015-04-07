import numpy as np
import random
import util


class dendrite_segment:
    cutoff = 0.5
    def __init__(self, input_shape):
        self.shape        = input_shape

        self.pot_synapses = np.empty(self.shape)
        self.per_synapses = np.empty(self.shape)

    def connect_to_input(self, input_positions):
        for xy in input_positions:
            self.pot_synapses[xy[0], xy[1]] = 1

    def random_permanence(self):
        arr = np.transpose(np.nonzero(self.pot_synapses))
        for x in arr:
            self.synapse_perm[x] = random.random()

    def get_active_synapses(self):
        actives = util.empty_array(self.shape)
        actives[self.synapse_perm > dendrite_segment.cutoff] = 1
        actives[self.synapse_perm <= dendrite_segment.cutoff] = 0
        return actives

    def get_activity_score(self, active_input):
        actives = self.get_active_synapses()
        return np.count_nonzero(np.multiply(actives, active_input))
