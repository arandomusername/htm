import random


class Dendrite():

    connection_threshold = 0.5
    connection_strength_step = 0.1

    def __init__(self, neuron, strength):
        self.neuron = neuron
        self.connection_strength = strength

    #checks if a dendrite transfers a signal
    def forwards_signal(self):
        if self.connection_strength >= Dendrite.connection_threshold and self.neuron.active:
            return True
        else:
            return False

    def is_connected(self):
        return self.connection_strength >= Dendrite.connection_threshold

    def update_permanence(self):
        if self.neuron.active is True:
            self.increase_threshold()
        else:
            self.decrease_threshold()

    def increase_threshold(self):
        self.connection_strength += Dendrite.connection_strength_step
        if self.connection_strength > 1:
            self.connection_strength = 1

    def decrease_threshold(self):
        self.connection_strength -= Dendrite.connection_strength_step
        if self.connection_strength < 0:
            self.connection_strength = 0

    def reset_threshold(self):
        self.connection_strength = 0


class DendriteSegment():
    def __init__(self, origin):
        self.origin = origin
        self.dendrites = []
        self.input_size = 0
        self.overlap = 0

    def init_dendrites(self, region, divisor):
        number_of_dendrites = (region.neuron_quantity / divisor)
        list_of_neurons = []

        for column in region.all_columns():
            list_of_neurons.extend(column.neurons)

        for x in range(number_of_dendrites):
            neuron = random.choice(list_of_neurons)
            list_of_neurons.remove(neuron)
            self.add_dendrite(neuron)

    # adds dendrites
    def add_dendrite(self, neuron):
        strength = random_connection_strength()
        den = Dendrite(neuron, strength)
        self.dendrites.append(den)

    # calculates the overlap-score of a specif segment
    def set_overlap(self):
        overlap = 0
        for dendrit in self.dendrites:
            if dendrit.forwards_signal():
                overlap += 1
        self.overlap = overlap

    def potential_actives(self):
        n = 0
        for dendrite in self.dendrites:
            if dendrite.is_connected():
                n += 1
        return n

    def learn(self):
        for dendrite in self.dendrites:
            dendrite.update_permanence()

    def reset_dendrites(self):
        for dendrite in self.dendrites:
            dendrite.reset_threshold()


# sets a random permanent-score in a certain radius
def random_connection_strength():
    z1 = random.randrange(0, 20)
    z2 = random.randrange(0, 20)
    z3 = z1 * Dendrite.connection_strength_step
    z4 = z2 * Dendrite.connection_strength_step
    perm = Dendrite.connection_threshold - z3 + z4
    return perm
