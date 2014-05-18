import cla_colloumn


class Region():
    def __init__(self, groesse):
        self.coll_groesse = 4
        self.overlap_range = 3
        self.inhibition_radius = 4
        self.min_overlap = 3

        self.colloums = []
        self.max_groesse = groesse

        for x in range(0, self.max_groesse):
            for y in range(0, self.max_groesse):
                pos = (x, y)
                self.add_colloum(pos)

    def raeumliche_wahrnehmung(self):
        """
        starts the regional learning
        :param
        """
        self.set_overlap()
        winner = self.check_inhibition()
        self.spacial_learning(winner)
        print winner
        self.reset_overlaps()

    def temporale_wahrnehmung(self, winner):
        self.activate_cells(winner)
        self.predict_activation()

    def activate_cells(self, winners):
        """
        activate cells in the winnercoloum based on their prediction state
        :param winners:
        """
        for winner in winners:
            column = self.get_column(winner)
            column.activate_cells()

    def check_inhibition(self):
        """
        checks if a coloum "wins" based on his own overlap score and the score of its neighbours and returns a list of
        said winners

        :return:
        """
        winner = []
        for coll in self.colloums:
            min_local_activity = self.n_smallest_overlap(coll)
            if coll.dendrit_segment.overlap > 0 and coll.dendrit_segment.overlap > min_local_activity:
                winner.append(coll.position)
        return winner

    def add_colloum(self, pos):
        """
        add a coloumn at a certain position and initializes a dendrit_segment for each colloum
        :param pos:
        """
        coll = cla_colloumn.Column(self.coll_groesse, pos)
        self.colloums.append(coll)

    def get_column(self, pos):
        """
        returns a colloum by its position
        :param pos:
        :return:
        """
        x_position = pos[0]
        y_position = pos[1]

        one_dimension = x_position*self.max_groesse + y_position
        column = self.colloums[one_dimension]
        return column

    def reset_overlaps(self):
        """
        resets the overlap score of the colloums

        """
        for coll in self.colloums:
            coll.dendrit_segment.overlap = 0

    def initialize_dendrites(self, input_region):
        for col in self.colloums:
            col.dendrit_segment.initialize_dendriten(input_region, 2)
            for neuron in col.neurons:
                neuron.dendrit_segment.initialize_dendriten(self, 4)

    def spacial_learning(self, winners):
        """
# lets the winnercolloumn learn from their connections
        :param winners:
        """
        for pos in winners:
            coll = self.get_column(pos)
            coll.dendrit_segment.learning()

    def n_smallest_overlap(self, column):
        """
        searches the neighbours of a coloumn for the n-te overlap score
        :param column:
        :return:
        """
        nachbar_liste = self.nachbaren(column.position)
        overlap_measures = []
        for position in nachbar_liste:
            coll = self.get_column(position)
            overlap_measures.append(coll.dendrit_segment.overlap)
        overlap_measures.sort(key=int)
        return overlap_measures[len(overlap_measures) - self.overlap_range]

    def predict_activation(self):
        for coll in self.colloums:
            for neuron in coll.neurons:
                neuron.check_prediction()

    def nachbaren(self, pos):
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

        if x2 > self.max_groesse:
            x2 = self.max_groesse
        if y2 > self.max_groesse:
            y2 = self.max_groesse

        for x in range(x1, x2):
            for y in range(y1, y2):
                position = (x, y)
                nachbar_list.append(position)

        return nachbar_list

    def set_overlap(self):
        """
      sets the overlap score for each colloumn

        """
        for coll in self.colloums:
            coll.dendrit_segment.set_overlap()