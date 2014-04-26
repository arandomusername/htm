class InputRegion():
    def __init__(self, input_groesse):
        self.colloums = []
        self.max_groesse = input_groesse
        self.coll_groesse = 1

        for x in range(0, self.max_groesse):
            self.add_colloum()

    def new_input(self, input_array):
        self.reset_region()
        for single_input in input_array:
            self.colloums[single_input].neurons[0].active = True

    def reset_region(self):
        for coll in self.colloums:
            coll.neurons[0].active = False

    def add_colloum(self):
        coll = Colloum()
        self.colloums.append(coll)


class Colloum():
    def __init__(self):
        self.neurons = []
        self.neurons.append(Neuron())


class Neuron():
    def __init__(self):
        self.active = False