import random

min_connection = 0.2
perm_schritt = 0.01


class Dendrit():
    def __init__(self, neuron, permanenz):
        self.neuron = neuron
        self.permanenz = permanenz

    #checks if a dendrite transfers a signal
    def uebertraegt_signal(self):
        if self.permanenz > min_connection:
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

    def learning(self):
        """
        lets the dendrites learn based on the aktiver input.

        """
        for single_dendrit in self.dendrite:
            if single_dendrit.neuron.active:
                single_dendrit.permanenz_erhoehen()
            else:
                single_dendrit.permanenz_senken()

    def initialize_dendriten(self, region, divisor):
        coloum_groesse = len(region.colloums)

        gesamt_anzahl_neuronen = coloum_groesse * region.coll_groesse
        anzahl_dendrite = (gesamt_anzahl_neuronen / divisor) - (gesamt_anzahl_neuronen % divisor)
        test_liste = []

        for x in range(0, anzahl_dendrite):
            test = False
            while not test:
                x_pos = random.randrange(0, coloum_groesse)
                z_pos = random.randrange(0, region.coll_groesse)
                pos = (x_pos, z_pos)
                if pos not in test_liste:
                    test = True
                    test_liste.append(pos)
                    neuron = region.colloums[x_pos].neurons[z_pos]
                    self.dendrit_hinzufuegen(neuron)

    # adds dendrites
    def dendrit_hinzufuegen(self, neuron):
        perm = zufalls_permanenz()
        den = Dendrit(neuron, perm)
        self.dendrite.append(den)

    # calculates the overlap-score of a specif segment
    def set_overlap(self, input_array):
        overlap = 0
        for dendrit in self.dendrite:
            if dendrit.neuron.position in input_array:
                if dendrit.uebertraegt_signal():
                    overlap +=  1
        self.overlap = overlap


# sets a random permanent-score in a certain radius
def zufalls_permanenz():
    z1 = random.randrange(0, 20)
    z2 = random.randrange(0, 20)
    z3 = z1 * perm_schritt
    z4 = z2 * perm_schritt
    perm = min_connection - z3 + z4
    return perm
