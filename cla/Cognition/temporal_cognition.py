
class TemporalCognitor:

    def __init__(self, region, winner_columns):
        self.region = region
        self.winner = winner_columns
        self.actives = region.get_active_neurons()

    def do(self):
        self.predict_cells()
        self.region.reset_activity()

    def predict_cells(self):
        for each in self.winner:
            for neuron in each.neurons:
                neuron.set_overlap()