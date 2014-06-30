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
        self.temporal.assign_and_execute(self.region, self.winner)
        self.print_actives()

    def assign_to(self, region):
        self.region = region
        self.winner = []
        self.spacial.assign(region)

    def execute(self, region):
        self.assign_to(region)
        self.do()

    def print_actives(self):
        actives = self.region.get_active_neurons()
        list = []
        for neuron in actives:
            list.append(neuron.position)
        print list

    def print_winners(self):
        position_list = []
        for each in self.winner:
            position_list.append(each.position)
        print position_list