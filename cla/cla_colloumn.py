import cla_dendrite


class neuron():
    min_overlap = 3

    def __init__(self, pos, region):
        self.active = False
        self.predicted = False
        self.position = pos
        self.dendrit_segment = cla_dendrite.dendrit_segment(pos)
        self.dendrit_segment.initialize_dendriten(region, 4)

    def check_overlap(self, active_cells):
        self.dendrit_segment.set_overlap(active_cells)

    def is_active(self):
        return self.active

    def check_prediction(self, list_of_active_cells):
        self.dendrit_segment.set_overlap(list_of_active_cells)
        if self.dendrit_segment.overlap > neuron.min_overlap:
            self.predicted = True

class colloum():
    def __init__(self, coll_groesse, position):
        self.active = False
        self.position = position
        self.neurons = []
        self.add_neurones(coll_groesse, self.neurons)
        self.dendrit_segment = cla_dendrite.dendrit_segment(position)


    # add neurones and gives them a position
    def add_neurones(self, neur_quantity):
        for x in range(0, neur_quantity):
            pos = (x, self.position)
            neur = neuron(pos)
            self.neurons.append(neur)

    # returns a list of the cells which are in the "predicted"-state
    def get_predicted_cells(self):
        predicted_cells = []
        for neuron in self.neurons:
            if neuron.predicted == True:
                predicted_cells.append(neuron)
        return predicted_cells

    # activates cells based on ther prediction-state
    def activate_cells(self):
        predicted_cells = self.get_predicted_cells()
        if len(predicted_cells) == 0:
            for neuron in self.neurons:
                neuron.active = True
        else:
            for neuron in predicted_cells:
                neuron.active = True
                neuron.predicted = False
		
