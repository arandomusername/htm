import dendrite
import neuron


class Column():
    size = 4

    def __init__(self, position):
        self.active = False
        self.position = position
        self.neurons = []
        self.add_neurones(self.size)
        self.dendrite_segment = dendrite.DendriteSegment(position)
        self.last_activation = 0

    def add_neurones(self, quantity):
        """
        add neurones and gives them a position
        :param neur_quantity:
        """
        for x in range(0, quantity):
            pos = []
            pos.extend(self.position)
            pos.append(x)
            self.neurons.append(neuron.Neuron(pos))

    def active_cells(self):
        actives = [cell for cell in self.neurons if cell.is_active()]
        return actives

    def predicted_cells(self):
        """
        returns a list of the cells which are in the "predicted"-state
        :return:
        """

        predicted_cells = [cell for cell in self.neurons if cell.is_predicted()]
        return predicted_cells

    def increase_last_activation(self):
        self.last_activation += 1

    def reset_last_activation(self):
        self.last_activation = 0

    def reset_activity(self):
        [cell.reset() for cell in self.neurons]

    def deactivate_cells(self):
        [cell.activate() for cell in self.active_cells()]

    def activate_cells(self):
        """
        activates cells based on their prediction-state
        """

        [cell.update() for cell in self.predicted_cells()]

    def learn(self):
        self.dendrite_segment.learn()