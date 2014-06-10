import random

min_connection = 0.2
perm_schritt = 0.02


class Dendrit():
    def __init__(self, neuron, permanenz):
        self.neuron = neuron
        self.permanenz = permanenz

    #checks if a dendrite transfers a signal
    def uebertraegt_signal(self):
        if self.permanenz > min_connection and self.neuron.active is True:
            return True
        else:
            return False

    def update_permanence(self):
        if self.neuron.active is True:
            self.permanenz_erhoehen()
        else:
            self.permanenz_senken()

    def permanenz_erhoehen(self):
        self.permanenz += perm_schritt

        if self.permanenz > 1:
            self.permanenz = 1

    def permanenz_senken(self):
        self.permanenz -= perm_schritt

        if self.permanenz < 0:
            self.permanenz = 0


class DendritSegment():
    def __init__(self, ur_pos):
        self.ursprungs_position = ur_pos
        self.dendrite = []
        self.input_groesse = 0
        self.overlap = 0

    def initialize_dendriten(self, region, divisor):

        anzahl_dendrite = (region.neuron_quantity / divisor) - (region.neuron_quantity % divisor)
        list_of_neurons = []

        for column in region.columns:
            list_of_neurons.extend(column.neurons)

        for x in range(anzahl_dendrite):
            neuron = random.choice(list_of_neurons)
            list_of_neurons.remove(neuron)
            self.add_dendrite(neuron)

    # adds dendrites
    def add_dendrite(self, neuron):
        perm = zufalls_permanenz()
        den = Dendrit(neuron, perm)
        self.dendrite.append(den)

    # calculates the overlap-score of a specif segment
    def set_overlap(self):
        overlap = 0
        for dendrit in self.dendrite:
            if dendrit.uebertraegt_signal():
                overlap += 1
        self.overlap = overlap


# sets a random permanent-score in a certain radius
def zufalls_permanenz():
    z1 = random.randrange(0, 20)
    z2 = random.randrange(0, 20)
    z3 = z1 * perm_schritt
    z4 = z2 * perm_schritt
    perm = min_connection - z3 + z4
    return perm
