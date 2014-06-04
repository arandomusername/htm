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

        anzahl_dendrite = (region.neuron_quantity/ divisor) - (region.neuron_quantity % divisor)
        test_list = []

        for x in range(anzahl_dendrite):
            test = False
            while not test:
                column = random.choice(region.columns)
                neuron = random.choice(column.neurons)

                if neuron not in test_list:
                    test = True
                    test_list.append(neuron)
                    self.dendrit_hinzufuegen(neuron)

    # adds dendrites
    def dendrit_hinzufuegen(self, neuron):
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
