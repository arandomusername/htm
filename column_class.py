import neuron_class

class Column(object,):
    def __init__(self, neuron_quantity):
        self.neuron_quantity = neuron_quantity
        self.activity        = neuron_class.NeuronState()
        self.neurons         = [neuron_class.Neuron() for x in range(neuron_quantity)]
        self.dendrites       = []

    def inti_dendrites(self, dendrites):
        self.dendrites.clear()
        for x in dendrites.list:
            if self == x.start:
                self.dendrites.append(x)

    def update_dendrites(self, dendrites):
        for x in dendrites.list:
            if self == x.start and not self.dendrites.__contains__(x):
                self.dendrites.append(x)