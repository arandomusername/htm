from dendrite_segment import dendrite_segment as dendrites


class neuron:
    def __init__(self, input_shape):
        self.dendrites = dendrites(input_shape)
