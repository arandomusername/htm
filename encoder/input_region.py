class InputRegion():
    def __init__(self, input_groesse):
        self.columns = []
        self.max_groesse = input_groesse
        self.coll_groesse = 1
        self.neuron_quantity = input_groesse

        for x in range(0, self.max_groesse):
            self.add_column()

    def new_input(self, input_array):
        self.reset_region()
        for single_input in input_array:
            self.columns[single_input].neurons[0].active = True

    def reset_region(self):
        for coll in self.columns:
            coll.neurons[0].active = False

    def add_column(self):
        coll = Column()
        self.columns.append(coll)


class Column():
    def __init__(self):
        self.neurons = []
        self.neurons.append(Neuron())


class Neuron():
    def __init__(self):
        self.active = False
        self.position = 0