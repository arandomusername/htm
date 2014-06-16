__author__ = 'root'
import spacial_cognition
import temporal_cognition


class Cognitor:
    def __init__(self):
        self.region = None
        self.winner = []
        self.spacial = spacial_cognition.SpacialCognitor()
        self.temporal = temporal_cognition.TemporalCognitor()

    def do(self):
        self.winner = self.spacial.do()
        self.spacial.print_winners()

        self.temporal.assign(self.region, self.winner)
        self.temporal.do()

    def assign_to(self, region):
        self.region = region
        self.winner = []
        self.spacial.assign(region)

    def assign_and_execute(self, region):
        self.assign_to(region)
        self.do()