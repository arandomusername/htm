from htm_sub import dendrite


class Neuron():

    def __init__(self, pos):
        self.active = False
        self.prediction = False
        self.position = pos
        self.dendrite_segment = dendrite.DendriteSegment(pos)

    def is_active(self):
        return self.active

    def is_predicted(self):
        return self.prediction

    def set_overlap(self):
        self.dendrite_segment.set_overlap()

    def learn(self):
        self.dendrite_segment.learn()

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

    def predict(self):
        self.prediction = True

    def unpredict(self):
        self.prediction = False

    def reset(self):
        self.deactivate()
        self.unpredict()

    def update(self):
        if self.is_predicted():
            self.unpredict()
            self.activate()
        else:
            self.reset()

    def status(self):
        if self.active is True:
            return "active"
        elif self.prediction is True:
            return "predicted"
        else:
            return "not active"
