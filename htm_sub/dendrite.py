import random


class Dendrite():

    connection_threshold = 0.5
    connection_strength_step = 0.1

    def __init__(self, neuron, strength):
        self.neuron = neuron
        self.connection_strength = strength

    #checks if a dendrite transfers a signal
    def forwards_signal(self):
        return self.connection_strength >= Dendrite.connection_threshold and self.neuron.active

    def is_connected(self):
        return self.connection_strength >= Dendrite.connection_threshold

    def update_permanence(self):
        if self.neuron.active is True:
            self.increase_threshold()
        else:
            self.decrease_threshold()

    def increase_threshold(self):
        self.connection_strength = 1 if self.connection_strength > 1 else self.connection_strength + Dendrite.connection_strength_step

    def decrease_threshold(self):
        self.connection_strength = 0 if self.connection_strength < 0 else self.connection_strength - Dendrite.connection_strength_step

    def reset_threshold(self):
        self.connection_strength = 0


class DendriteSegment():
    def __init__(self, origin):
        self.origin = origin
        self.dendrites = []
        self.input_size = 0
        self.overlap = 0

    def init_dendrites(self, region, divisor):
        number_of_dendrites = int(region.neuron_quantity / divisor)
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
        dendrite = Dendrite(neuron, strength)
        self.dendrites.append(dendrite)

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
        [dendrite.update_permanence() for dendrite in self.dendrites]


    def reset_dendrites(self):
        [dendrite.reset_threshold() for dendrite in self.dendrites]

# sets a random permanent-score in a certain radius
def random_connection_strength():
    z1 = random.randrange(0, 20)
    z2 = random.randrange(0, 20)
    z3 = z1 * Dendrite.connection_strength_step
    z4 = z2 * Dendrite.connection_strength_step
    perm = Dendrite.connection_threshold - z3 + z4
    return perm
