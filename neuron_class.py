class Neuron(object):
    def __init__(self, pos=0):
        self.activity  = NeuronState()
        self.prognosis = NeuronState()
        self.position  = pos

    def __repr__(self):
        return "Neuronn: {0}, {1}".format(self.activity, self.prognosis)

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

    def __repr__(self):
        return "{0}".format(self.get_state())

    def get_state(self):
        return self.state

    def turn_on(self):
        self.state = True

    def turn_off(self):
        self.state = False
