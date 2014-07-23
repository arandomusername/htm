import random


class Dendrit():

    min_connection = 0.5
    perm_schritt = 0.02

    def __init__(self, neuron, permanenz):
        self.neuron = neuron
        self.permanenz = permanenz

    #checks if a dendrite transfers a signal
    def uebertraegt_signal(self):
        if self.permanenz >= Dendrit.min_connection and self.neuron.active is True:
            return True
        else:
            return False

    def is_connected(self):
        return self.permanenz >= Dendrit.min_connection

    def update_permanence(self):
        if self.neuron.active is True:
            self.permanenz_erhoehen()
        else:
            self.permanenz_senken()

    def permanenz_erhoehen(self):
        self.permanenz += Dendrit.perm_schritt
        if self.permanenz > 1:
            self.permanenz = 1

    def permanenz_senken(self):
        self.permanenz -= Dendrit.perm_schritt
        if self.permanenz < 0:
            self.permanenz = 0

    def reset_permanenz(self):
        self.permanenz = 0


class DendritSegment():
    def __init__(self, ur_pos):
        self.ursprungs_position = ur_pos
        self.dendrites = []
        self.input_groesse = 0
        self.overlap = 0

    def init_dendrites(self, region, divisor):
        anzahl_dendrite = (region.neuron_quantity / divisor) - (region.neuron_quantity % divisor)/divisor
        list_of_neurons = []

        for column in region.all_columns():
            list_of_neurons.extend(column.neurons)

        for x in range(anzahl_dendrite):
            neuron = random.choice(list_of_neurons)
            list_of_neurons.remove(neuron)
            self.add_dendrite(neuron)

    # adds dendrites
    def add_dendrite(self, neuron):
        perm = zufalls_permanenz()
        den = Dendrit(neuron, perm)
        self.dendrites.append(den)

    # calculates the overlap-score of a specif segment
    def set_overlap(self):
        overlap = 0
        for dendrit in self.dendrites:
            if dendrit.uebertraegt_signal():
                overlap += 1
        self.overlap = overlap

    def potential_actives(self):
        n = 0
        for dendrite in self.dendrites:
            if dendrite.is_connected:
                n += 1
        return n

    def learn(self):
        for dendrite in self.dendrites:
            dendrite.update_permanence()

    def reset_dendrites(self):
        for dendrite in self.dendrites:
            dendrite.reset_permanenz()

# sets a random permanent-score in a certain radius
def zufalls_permanenz():
    z1 = random.randrange(0, 20)
    z2 = random.randrange(0, 20)
    z3 = z1 * Dendrit.perm_schritt
    z4 = z2 * Dendrit.perm_schritt
    perm = Dendrit.min_connection - z3 + z4
    return perm
