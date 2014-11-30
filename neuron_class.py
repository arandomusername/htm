__author__ = 'Martin'


class Neuron(object):
    def __init__(self, reference_neuron):
        self.activity  = NeuronState()
        self.prognosis = NeuronState()
        self.connection = reference_neuron

    def turn_off(self):
        self.activity.turn_off()
        self.prognosis.turn_off()

    def turn_on(self):
        self.activity.turn_on()
        self.activity.turn_on()


class NeuronState(object):
    def __init__(self):
        self.state = False

    def get_state(self):
        return self.state

    def turn_on(self):
        self.state = True

    def turn_off(self):
        self.state = False