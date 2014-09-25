from Cognition import spacial_cognition
from Cognition import temporal_cognition


class Cognitor:
    def __init__(self):
        self.region = None
        self.winner = []
        self.spacial = spacial_cognition.SpacialCognitor()
        self.temporal = temporal_cognition.TemporalCognitor()

    def assign_to(self, region):
        self.region = region
        self.winner = []
        self.spacial.assign(region)

    def execute(self, region):
        self.assign_to(region)
        self.winner = self.spacial.assign_and_do(region)
        self.temporal.assign_and_execute(self.region, self.winner)
        self.print_actives()

    def print_actives(self):
        print([neuron.position for neuron in self.region.get_active_neurons()])

    def print_winners(self):
        print([winner.position for winner in self.winner])