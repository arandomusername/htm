__author__ = 'Martin'
import neuron_class

class Column():
    def __init__(self, neuron_quantity):
        self.activity = neuron_class.NeuronState()
        self.neurons  = [neuron_class.Neuron() for x in range(neuron_quantity)]