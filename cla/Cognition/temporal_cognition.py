
class TemporalCognitor:
    def __init__(self, region, winner_columns):
        self.region = region
        self.winner = winner_columns
        self.actives = region.get_active_neurons()