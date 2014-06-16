__author__ = 'root'
import spacial_cognition
import temporal_cognition

class Cognitor:
    def __init__(self):
        self.region = None
        self.winner = []

    def do(self):
        spa_cog = spacial_cognition.SpacialCognitor(self.region)
        self.winner = spa_cog.do()
        spa_cog.print_winners()

        tem_cog = temporal_cognition.TemporalCognitor(self.region, self.winner)
        tem_cog.do()

    def assign_to(self, region):
        self.region = region
        self.winner = []

    def assign_and_execute(self,region):
        self.assign_to(region)
        self.do()