class SpacialCognitor():

    def __init__(self):
        self.region = None
        self.winner = []
        self.inhibition_radius = 4

    def assign(self, region):
        self.region = region
        self.winner = []

    def do(self):
        self.set_overlap()
        self.set_winners()
        self.booster()
        self.update_activation_cycle()
        self.spacial_learning()
        self.region.reset_overlaps()

    def assign_and_do(self, region):
        self.assign(region)
        self.do()
        return self.winner

    def set_overlap(self):
        """
        sets the overlap score for each column
        """

        [column.dendrite_segment.set_overlap() for column in self.region.all_columns()
        ]

    def set_winners(self):
        """
        return a list with n objects of columns with the highest overlap score
        :return:winners
        """
        overlap_list = []
        winners = []

        [overlap_list.append(column.dendrite_segment.overlap) for column in self.region.all_columns()]

        overlap_list.sort()
        overlap_list.reverse()
        overlap_threshold = overlap_list[self.inhibition_radius]
        overlap_counter = overlap_list[0]

        while overlap_counter >= overlap_threshold and overlap_counter > 0:
            winners.extend(self.region.get_columns_by_overlap(overlap_counter))
            overlap_counter -= 1
        self.winner = winners

    def booster(self):
        # at least 5% of all columns must be active. If not some columns get "boosted"
        quantity_needed = len(self.region.columns)*5/100
        boosted_overlap = self.smallest_overlap_from_winner()
        boosted_columns = []

        while quantity_needed > len(self.winner):
            while len(boosted_columns) == 0:
                boosted_overlap -= 1
                boosted_columns = self.region.get_columns_by_overlap(boosted_overlap)
                boosted_columns.sort(key=lambda x: x.last_activation, reverse=True)

            self.winner.append(boosted_columns.pop(0))

    def update_activation_cycle(self):
        for column in self.region.all_columns():
            if column in self.winner:
                column.reset_last_activation()
            else:
                column.increase_last_activation()

    def smallest_overlap_from_winner(self):
        overlap_list = [column.dendrite_segment.overlap for column in self.winner]
        smallest_overlap = min(overlap_list) if overlap_list != [] else 1
        return smallest_overlap

    def biggest_overlap(self):
        biggest_overlap = max([column.dendrite_segment.overlap for column in self.winner])
        return biggest_overlap

    def spacial_learning(self):
        """
        lets the winner-column learn from their connections
        """
        for column in self.winner:
            column.learn()