from dendrite_segment import dendrite_segment as dendrites


class neuron:
    def __init__(self, input_shape, cutoff):
        self.dendrites = dendrites(input_shape, cutoff)

    def get_activity(self):
        return self.active

    def get_prognosis(self):
        return self.prognosis

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

    def set_prognosis(self, prog):
        self.prognosis = prog
