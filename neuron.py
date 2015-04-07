from dendrite_segment import dendrite_segment as dendrites


class neuron:
    def __init__(self, input_shape, cutoff):
        self.dendrites = dendrites(input_shape, cutoff)
