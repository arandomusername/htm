import cla_dendrite


class Neuron():
    min_overlap = 3

    def __init__(self, pos):
        self.active = False
        self.predicted = False
        self.position = pos
        self.dendrit_segment = cla_dendrite.DendritSegment(pos)

    def status(self):
        if self.active is True:
            return "active"
        elif self.predicted is True:
            return "predicted"
        else:
            return "not active"

    def is_active(self):
        return self.active

    def is_predicted(self):
        return self.predicted

    def check_overlap(self):
        self.dendrit_segment.set_overlap()

    def check_prediction(self):
        self.dendrit_segment.set_overlap()
        if self.dendrit_segment.overlap > Neuron.min_overlap:
            self.predicted = True


class Column():
    size = 4

    def __init__(self, position):
        self.active = False
        self.position = position
        self.neurons = []
        self.add_neurones(self.size)
        self.dendrit_segment = cla_dendrite.DendritSegment(position)
        self.last_activation = 0

    def add_neurones(self, neur_quantity):
        """
        add neurones and gives them a position
        :param neur_quantity:
        """
        for x in range(0, neur_quantity):
            pos = (x, self.position)
            neuron = Neuron(pos)
            self.neurons.append(neuron)

    def get_active_cells(self):
        actives = []
        for cell in self.neurons:
            if cell.is_active():
                actives.append(cell)

    def get_predicted_cells(self):
        """
        returns a list of the cells which are in the "predicted"-state
        :return:
        """
        predicted_cells = []
        for cell in self.neurons:
            if cell.predicted is True:
                predicted_cells.append(cell)
        return predicted_cells

    def increase_last_activation(self):
        self.last_activation += 1

    def reset_last_activation(self):
        self.last_activation = 0

    def activate_cells(self):
        """
        activates cells based on their prediction-state
        """
        predicted_cells = self.get_predicted_cells()
        if len(predicted_cells) == 0:
            for cell in self.neurons:
                cell.active = True
        else:
            for cell in predicted_cells:
                cell.active = True
                cell.predicted = False