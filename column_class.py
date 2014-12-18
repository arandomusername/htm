from neuron_class import Neuron, NeuronState

class Column(object):
    neuron_quantity = 5

    def __init__(self, pos):
        self.neuron_quantity = Neuron.neuron_quantity
        self.activity        = NeuronState()
        self.neurons         = [Neuron(x) for x in range(Neuron.neuron_quantity)]
        self.dendrites       = []
        self.position        = pos

    def update_dendrites(self, dendrites):
        self.dendrites = [x for x in dendrites if self == x.start]

    def set_neuron_quantity(self, quantity):
        self.neuron_quantity = quantity