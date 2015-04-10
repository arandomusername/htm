from dendrite_segment import dendrite_segment as dendrites
import numpy as np


class column(object):

    neuron_num = 5                                    # Number of Neurons
    synapse_cutoff = 0.5                              # Pot Synapses Threshold
    boost_step     = 0.1

    def __init__(self, input_shape, region_size):
        self.dendrites = dendrites(input_shape)
        self.neurons  = []
        self.boost    = 1
        self.__add_neurons(region_size)
        self.neuron_activation = np.zeros(column.neuron_num)
        self.neuron_prognosis  = np.zeros(column.neuron_num)

    def __add_neurons(self, region_size):
        for x in range(column.neuron_num):
            self.neurons.append((region_size, region_size, column.neuron_num))

    def get_activity_score(self, active_input):
        return (self.dendrites.get_activity_score(active_input) * self.boost +
                self.boost)

    def increase_boost(self):
        self.boost += column.boost_step

    def decrease_boost(self):
        self.boost -= column.boost_step
        if(self.boost < 1):
            self.boost = 1

    def get_act_neuron_matrix(self):
        # This is incomplete. The activity equals the regions activity.
        # get_activity needs and input.
        act_arr = np.zeros(column.neuron_num)
        for n in range(column.neuron_num):
            act_arr[n] = self.neurons[n].get_activity()
