import cla_colloumn


class region():
    def __init__(self, groesse, input_region):
        self.coll_groesse = 4
        self.overlap_range = 7
        self.inhibition_radius = 10
        self.min_overlap = 3

        self.colloums = []
        self.max_groesse = groesse

        for x in range(0, self.max_groesse):
            for y in range(0, self.max_groesse):
                pos = (x, y)
                self.add_colloum(pos,input_region)

    def raeumliche_wahrnehmung(self, Input):
        """
        starts the regional learning
        :param Input:
        """
        self.set_overlap(Input)
        winner = self.check_inhibition()
        self.learning(winner)
        self.reset_overlaps()

    def activate_cells(self, winners):
        """
        activate cells in the winnercoloum based on their prediction state
        :param winners:
        """
        for winner in winners:
            coloumn = self.coll_by_position(winner)
            coloumn.activate_cells()


    def check_inhibition(self):
        """
        checks if a coloum "wins" based on his own overlap score and the score of its neighbours and returns a list of said winners

        :return:
        """
        winner = []
        for coll in self.colloums:
            nachbar_liste = self.nachbaren(coll.position)
            min_local_activity = self.n_smallest_overlap(nachbar_liste)
            if coll.dendrit_segment.overlap > 0 and coll.dendrit_segment.overlap > min_local_activity:
                winner.append(coll.position)
        return winner

    def add_colloum(self, pos,input_region):
        """
        add a coloumn at a certain position and initializes a dendrit_segment for each colloum
        :param pos:
        """
        coll = cla_colloumn.colloum(self.coll_groesse, pos)
        coll.dendrit_segment.initialize_dendriten(input_region,2)
        self.colloums.append(coll)

    def neuron_by_position(self,pos):
        x_pos,z_pos = pos
        coll = self.colloums[x_pos]
        neuron = coll.neurons(z_pos)
        return neuron

    def coll_by_position(self, pos):
        """
        returns a colloum by its position
        :param pos:
        :return:
        """
        for coll in self.colloums:
            if coll.position == pos:
                return coll

    # resets the overlap score of the colloums
    def reset_overlaps(self):
        for coll in self.colloums:
            coll.dendrit_segment.overlap = 0
            coll.dendrit_segment.reset_aktivitaet()

    # returns a list of which cells are in the active state
    def get_active_cells(self):
        active_cells = []
        for coll in self.colloums:
            for neuron in coll.neurons:
                if neuron.is_active():
                    active_cells.append(neuron.pos)
        return active_cells

    # lets the winnercolloumn learn from their connections
    def learning(self, winners):
        for pos in winners:
            coll = self.coll_by_position(pos)
            coll.dendrit_segment.learning()

    #searches the neighbours of a coloumn for the n-te overlap score
    def n_smallest_overlap(self, nachbarliste):
        overlap_measures = []
        for position in nachbarliste:
            coll = self.coll_by_position(position)
            overlap_measures.append(coll.dendrit_segment.overlap)
        overlap_measures.sort(key=int)
        return overlap_measures[len(overlap_measures) - region.overlap_range]

    def predict_activation(self):
        list_of_active_cells = self.get_active_cells()
        active_cells = self.get_active_cells()
        for coll in self.colloums:
            for neuron in coll.neurons:
                neuron.check_prediction(list_of_active_cells)


    # returns position of coll in the radius (the radius is a square not a circle)
    def nachbaren(self, pos):
        nachbarlist = []
        pos_x = pos[0]
        pos_y = pos[1]

        x1 = pos_x - region.inhibition_radius
        x2 = pos_x + region.inhibition_radius
        y1 = pos_y - region.inhibition_radius
        y2 = pos_y + region.inhibition_radius

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
                nachbarlist.append(position)

        return nachbarlist

    # sets the overlap score for each colloumn
    def set_overlap(self, Input):
        for coll in self.colloums:
            coll.dendrit_segment.set_overlap(Input)