import cla_dendrite

class Neuron():

    def __init__(self, pos):
        self.active = False
        self.predicted = False
        self.position = pos
        self.dendrite_segment = cla_dendrite.DendritSegment(pos)

    def status(self):
        if self.active is True:
            return "active"
        elif self.predicted is True:
            return "predicted"
        else:
            return "not active"

    def is_active(self):
        return self.active

    def is_predicted(self):
        return self.predicted

    def set_overlap(self):
        self.dendrite_segment.set_overlap()

    def learn(self):
        self.dendrite_segment.learn()
