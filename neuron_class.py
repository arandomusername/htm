__author__ = 'Martin'


class Neuron(object):
    def __init__(self, reference_neuron):
        self.activity  = NeuronState()
        self.prognosis = NeuronState()
        self.connection = reference_neuron #remove later (only for testing)

    def turn_off(self):
        self.activity.turn_off()
        self.prognosis.turn_off()

    def turn_on(self):
        self.activity.turn_on()
        self.prognosis.turn_on()

    def get_state(self):
        state = (self.activity.get_state(), self.prognosis.get_state())
        return state

class NeuronState(object):
    def __init__(self):
        self.state = False

    def get_state(self):
        return self.state

    def turn_on(self):
        self.state = True

    def turn_off(self):
        self.state = False

class Connection