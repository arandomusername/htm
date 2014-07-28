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

    def assign_and_execute(self, region, winner_columns):
        self.assign(region, winner_columns)
        self.do()

    def deactivate(self):
        self.region.reset_activity()

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
                overlap_list.append(neuron.dendrite_segment.overlap)

            overlap_list.sort()
            overlap_list.reverse()
            check = self.check_list(overlap_list)
            self.set_prediction(overlap_list, check, column)

    def set_prediction(self, overlap_list, check, column):
        if check and overlap_list[0] == 0:  # if nothing is predicted all get activated
            for neuron in column.neurons:
                    neuron.predicted = True

        elif check:  # if all are equally predicted the first element is preferred
            column.neurons[0].predicted = True

        else:                               # else all neurons with the highest overlap get predicted
            for neuron in column.neurons:
                if neuron.dendrite_segment.overlap == overlap_list[0]:
                    neuron.predicted = True

    def check_list(self, list):
        return len(set(list)) <= 1

    def learning(self):
        for column in self.winner:
            for neuron in column.neurons:
                neuron.learn()
