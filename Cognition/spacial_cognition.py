class SpacialCognitor():

    def __init__(self, region):
        self.region = region
        self.winner = []
        self.inhibition_radius = 4

    def do(self):
        self.set_overlap()
        self.get_global_winner()
        self.booster()
        self.check_winners()
        self.update_activation()
        self.spacial_learning()
        self.region.reset_overlaps()
        return self.winner

    def set_overlap(self):
        """
        sets the overlap score for each column
        """
        for coll in self.region.columns:
            coll.dendrit_segment.set_overlap()

    def check_winners(self): # used for debugging
        if len(self.winner)!=len(set(self.winner)):
            print("soso")

    def get_global_winner(self):
        """
        return a list with n objects of columns with the highest overlap score
        :return:winners
        """
        overlap_list = []
        winners = []

        for column in self.region.columns:
            overlap_list.append(column.dendrit_segment.overlap)

        overlap_list.sort()
        overlap_list.reverse()
        overlap_threshold = overlap_list[self.inhibition_radius]
        overlap_counter = overlap_list[0]

        while overlap_counter >= overlap_threshold and overlap_counter > 0:
            winners.extend(self.region.get_columns_by_overlap(overlap_counter))
            overlap_counter -= 1
        self.winner = winners

    def booster(self):
        # at least 5% of all columns must be active and then adds
        quantity_needed = (len(self.region.columns)*5)/100
        smallest_overlap = None
        boosted_columns = []

        while len(self.winner) < quantity_needed:
            if smallest_overlap is None or len(boosted_columns) == 0:
                smallest_overlap = self.get_smallest_overlap() - 1
                boosted_columns = self.region.get_columns_by_overlap(smallest_overlap)

            boosted_columns.sort(key=lambda x: x.last_activation, reverse=True)
            self.winner.append(boosted_columns.pop(0))

    def update_activation(self):
        for column in self.region.columns:
            if column in self.winner:
                column.reset_last_activation()
            else:
                column.increase_last_activation()

    def get_smallest_overlap(self):
        overlap = None

        for column in self.winner:
            if column.dendrit_segment.overlap < overlap or overlap is None:
                overlap = column.dendrit_segment.overlap

        if overlap is None:
            overlap = 1

        return overlap

    def spacial_learning(self):
        """
        lets the winner-column learn from their connections
        """
        for column in self.winner:
            for single_dendrit in column.dendrit_segment.dendrites:
                single_dendrit.update_permanence()

    def print_winners(self):
        position_list = []
        for each in self.winner:
            position_list.append(each.position)
        print position_list