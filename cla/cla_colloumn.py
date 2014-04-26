import cla_dendrite


class Neuron():
    min_overlap = 3

    def __init__(self, pos, region):
        self.active = False
        self.predicted = False
        self.position = pos
        self.dendrit_segment = cla_dendrite.DendritSegment(pos)
        self.dendrit_segment.initialize_dendriten(region, 4)

    def check_overlap(self, active_cells):
        self.dendrit_segment.set_overlap(active_cells)

    def is_active(self):
        return self.active

    def check_prediction(self, list_of_active_cells):
        self.dendrit_segment.set_overlap(list_of_active_cells)
        if self.dendrit_segment.overlap > Neuron.min_overlap:
            self.predicted = True


class Column():
    def __init__(self, coll_groesse, position, input_region):
        self.active = False
        self.position = position
        self.neurons = []
        self.add_neurones(coll_groesse, input_region)
        self.dendrit_segment = cla_dendrite.DendritSegment(position)

    # add neurones and gives them a position
    def add_neurones(self, neur_quantity, input_region):
        for x in range(0, neur_quantity):
            pos = (x, self.position)
            neur = Neuron(pos, input_region)
            self.neurons.append(neur)

    # returns a list of the cells which are in the "predicted"-state
    def get_predicted_cells(self):
        predicted_cells = []
        for cell in self.neurons:
            if cell.predicted is True:
                predicted_cells.append(cell)
        return predicted_cells

    # activates cells based on ther prediction-state
    def activate_cells(self):
        predicted_cells = self.get_predicted_cells()
        if len(predicted_cells) == 0:
            for cell in self.neurons:
                cell.active = True
        else:
            for cell in predicted_cells:
                cell.active = True
                cell.predicted = False