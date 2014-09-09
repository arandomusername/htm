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
        [column.activate_cells() for column in self.winner]

    def set_overlap(self):
        for column in self.winner:
            for neuron in column.neurons:
                neuron.set_overlap()

    def predict_cells(self):
        for column in self.winner:
            for neuron in column.neurons:
                neuron.set_overlap()


    def select_predicted(self):
        for column in self.winner:
            highest_overlap = 0

            for neuron in column.neurons:
                current_overlap = neuron.dendrite_segment.overlap
                highest_overlap = current_overlap if current_overlap > highest_overlap else highest_overlap

            self.set_prediction(highest_overlap, column)

    def set_prediction(self, highest_overlap, column):
        if highest_overlap == 0:  # if nothing is predicted all get activated
            [neuron.predict() for neuron in column.neurons]
        else:                               # else neurons with the highest overlap get predicted
            for neuron in column.neurons:
                if neuron.dendrite_segment.overlap == highest_overlap:
                    neuron.predict()

    def learning(self):
        for column in self.winner:
            for neuron in column.neurons:
                neuron.learn()
