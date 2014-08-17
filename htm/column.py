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

    def add_neurones(self, neur_quantity):
        """
        add neurones and gives them a position
        :param neur_quantity:
        """
        for x in range(0, neur_quantity):
            pos = []
            pos.extend(self.position)
            pos.append(x)
            neuron = neuron.Neuron(pos)
            self.neurons.append(neuron)

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
        for neuron in self.neurons:
            neuron.active = False

    def deactivate_cells(self):
        for neuron in self.active_cells():
            neuron.active = False

    def activate_cells(self):
        """
        activates cells based on their prediction-state
        """

        for neuron in self.predicted_cells():
            neuron.predicted = False
            neuron.active = True

    def learn(self):
        self.dendrite_segment.learn()