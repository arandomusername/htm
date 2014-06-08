import cla_column


class Region():
    def __init__(self, size):
        self.search_range = 5        # at which radius winners are searched.
        self.inhibition_radius = 4   #
        self.columns = []
        self.max_size = size
        self.neuron_quantity = (size**2) * cla_column.Column.size

        for x in range(self.max_size):
            for y in range(self.max_size):
                pos = (x, y)
                self.add_column(pos)

    def spacial_cognition(self):
        """
        starts the spacial learning
        :param
        """
        self.set_overlap()
        winner = self.get_global_winner()                                                       # In order to be biologically correct one would use get_local_winner but this way is much faster and hasnt much difference
        self.booster(winner)
        self.update_activation(winner)
        self.spacial_learning(winner)
        print len(winner)
        self.reset_overlaps()

    def booster(self, winners):
        quantity_needed = len((self.columns)*5)/100                                             # at least 5% of all columns must be active and then adds

        while len(winners) < quantity_needed:
            smallest_overlap = 0
            boosted_columns = []

            for column in winners:
                if smallest_overlap > column.dendrit_segment.overlap or smallest_overlap==0:
                    smallest_overlap = column.dendrit_segment.overlap                           #gets the smallest overlap from the list winners

            boosted_columns = self.get_columns_by_overlap(smallest_overlap)                     # <----- ANSCHAUEN WASN LOS HIER


            boosted_columns.sort(key=lambda x: x.last_activation, reverse=True)
            winners.append(boosted_columns.pop(0))                                              #adds the one coloumn with the latest activation time.

    def get_columns_by_overlap(self,overlap):
        overlap_columns = []
        for column in self.columns:
            if column.dendrit_segment.overlap == overlap:
                overlap_columns.append(column)
        return overlap_columns

    def update_activation(self, winners):
        for column in self.columns:
            if column in winners:
                column.last_activation = 0
            else:
                column.last_activation += 1

    def set_overlap(self):
        """
        sets the overlap score for each column
        """
        for coll in self.columns:
            coll.dendrit_segment.set_overlap()

    def activate_cells(self, winners):
        """
        activate cells in the winnercoloum based on their prediction state
        :param winners:
        """
        for winner in winners:
            column = self.get_column(winner)
            column.activate_cells()

    def get_global_winner(self):
        """
        return a list with n objects of columns with the highest overlap score

        :return:winners
        """
        overlap_list = []
        winners = []

        for column in self.columns:
            overlap_list.append(column.dendrit_segment.overlap)

        overlap_list.sort()
        overlap_list.reverse()
        overlap_threshold = overlap_list[self.inhibition_radius]
        overlap_counter = overlap_list[0]

        while overlap_counter >= overlap_threshold:
            winners.extend(self.get_columns_by_overlap(overlap_counter))
            overlap_counter -= 1

        return winners

    def get_local_winner(self):
        """
        checks if a coloum "wins" based on his own overlap score and the score of its neighbours and returns a list of
        said winners

        :return:
        """
        winner = []
        for column in self.columns:
            min_local_activity = self.n_smallest_overlap(column)
            if column.dendrit_segment.overlap > 0 and column.dendrit_segment.overlap > min_local_activity:
                winner.append(column.position)
        return winner

    def add_column(self, pos):
        """
        add a coloumn at a certain position and initializes a dendrit_segment for each colloum
        :param pos:
        """
        coll = cla_column.Column(pos)
        self.columns.append(coll)

    def get_column(self, pos):
        """
        returns a colloum by its position
        :param pos:
        :return:
        """
        x_position = pos[0]
        y_position = pos[1]

        one_dimension = x_position * self.max_size + y_position
        column = self.columns[one_dimension]
        return column

    def reset_overlaps(self):
        """
        resets the overlap score of the colloums

        """
        for coll in self.columns:
            coll.dendrit_segment.overlap = 0

    def initialize_dendrites(self, input_region):
        for col in self.columns:
            col.dendrit_segment.initialize_dendriten(input_region, 2)
            for neuron in col.neurons:
                neuron.dendrit_segment.initialize_dendriten(self, 4)

    def spacial_learning(self, winners):
        """
        lets the winner-column learn from their connections
        :param winners:
        """
        for column in winners:
            for single_dendrit in column.dendrit_segment.dendrite:
                if single_dendrit.neuron.active is True:
                    single_dendrit.permanenz_erhoehen()
                else:
                    single_dendrit.permanenz_senken()

    def n_smallest_overlap(self, column):
        """
        searches the neighbours of a coloumn for the n-te overlap score
        :param column:
        :return:
        """
        nachbar_liste = self.neighbors(column.position)
        overlap_list = []

        #fills the list
        for x in range(0, self.search_range):
            overlap_list.append(0)

        #search for the biggest overlap-scores in a specific range
        for position in nachbar_liste:
            column = self.get_column(position)
            if column.dendrit_segment.overlap > overlap_list[self.search_range]:
                overlap_list.remove(overlap_list[self.search_range])
                overlap_list.append(column.dendrit_segment.overlap)
                overlap_list.sort()
                overlap_list.reverse()

        return overlap_list[self.search_range]

    def predict_activation(self):
        for coll in self.columns:
            for neuron in coll.neurons:
                neuron.check_prediction()

    def neighbors(self, pos):
        """
        returns position of coll in the radius (the radius is a square not a circle)
        :param pos:
        :return:
        """
        nachbar_list = []
        pos_x = pos[0]
        pos_y = pos[1]

        x1 = pos_x - self.inhibition_radius
        x2 = pos_x + self.inhibition_radius
        y1 = pos_y - self.inhibition_radius
        y2 = pos_y + self.inhibition_radius

        if x1 < 0:
            x1 = 0
        if y1 < 0:
            y1 = 0

        if x2 > self.max_size:
            x2 = self.max_size
        if y2 > self.max_size:
            y2 = self.max_size

        for x in range(x1, x2):
            for y in range(y1, y2):
                position = (x, y)
                nachbar_list.append(position)

        return nachbar_list