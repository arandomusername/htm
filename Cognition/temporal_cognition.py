class TemporalCognitor:
    min_overlap = 3

    def __init__(self):
        self.region = None
        self.winner = None

    def assign(self, region, winner_columns):
        self.region = region
        self.winner = winner_columns

    def do(self):
        self.set_overlap()
        self.select_predicted()
        self.learning()
        self.deactivate()
        self.activate()

    def deactivate(self):
        for column in self.winner:
            column.deactivate_cells()

    def activate(self):
        for column in self.winner:
            column.activate_cells()

    def set_overlap(self):
        for column in self.winner:
            for neuron in column.neurons:
                neuron.set_overlap()

    def predict_cells(self):
        for each in self.winner:
            for neuron in each.neurons:
                neuron.set_overlap()

    def select_predicted(self):
        for column in self.winner:
            overlap_list = []

            for neuron in column.neurons:
                overlap_list.append(neuron.dendrit_segment.overlap)

            overlap_list.reverse()
            overlap_list.reverse()
            if self.check_list(overlap_list) and overlap_list[0] == 0:  # if nothing is predicted all get activated
                for neuron in column.neurons:
                    neuron.predicted = True

            elif self.check_list(overlap_list):  # if all are equaly predicted the first element is preferred
                column.neurons[0].predicted = True

            else:                               # else all neurons with the highest overlap get predicted
                for neuron in column.neurons:
                    if neuron.dendrit_segment.overlap == overlap_list[0]:
                        neuron.predicted = True

    def check_list(self, list):
        return len(set(list)) <= 1

    def learning(self):
        for column in self.winner:
            for neuron in column.neurons:
                neuron.learn()