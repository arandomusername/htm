from neuron_class import Neuron, NeuronState


class Column(object):
    neuron_quantity = 5

    def __init__(self, pos):
        self.neuron_quantity = Column.neuron_quantity
        self.activity        = NeuronState()
        self.neurons         = [Neuron(x) for x in range(Column.neuron_quantity)]
        self.dendrites       = []
        self.position        = pos

    def __repr__(self):
        if self.activity:
            act = "active"
        else:
            act = "non-active"
        return "{0}.{1} - {2}".format(self.position, self.__class__.__name__, act)

    def update_dendrites(self, dendrites):
        self.dendrites = [x for x in dendrites if self == x.start]
