from dedrite_segment import

class column(object):

    input_size = 0
    neuron_num = 5                                    # Number of Neurons
    synapse_cutoff = 0.5                              # Pot Synapses Threshold
    boost_step     = 0.1

    def __init__(self, pos, reg_s):
        # Position of Synapses and their resp. Weight
        self.dendrites = dendrites([column.input_size, column.input_size],
                                   column.synapse_cutoff)
        self.neurons  = []
        self.activity = False
        self.position = pos                     # Position inside the Region
        self.boost    = 1

        self.__add_neurons(reg_s)

    def __repr__(self):
        return '{0} at {1}'.format(self.activity, self.position)

    def __add_neurons(self, region_size):
        pass

    def get_activity(self):
        return self.activity

    def get_activity_score(self, active_input):
        return self.dendrites.get_activity_score() * self.boost

    def increase_boost(self):
        self.boost += column.boost_step

    def decrease_boost(self):
        self.boost -= column.boost_step
        if(self.boost < 1):
            self.boost = 1

    def get_act_neuron_matrix(self):
        pass
