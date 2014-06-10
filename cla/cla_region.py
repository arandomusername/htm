import cla_column
import cla_cognition

class Region():
    def __init__(self, size):
        self.search_range = 5        # at which radius winners are searched.
        self.inhibition_radius = 4   #
        self.columns = []
        self.max_size = size
        self.neuron_quantity = (size**2) * cla_column.Column.size
        self.add_column()


    def spacial_cognition(self):
        """
        starts the spacial learning
        :param
        """
        cognitor = cla_cognition.SpacialCognitor(self)
        winner = cognitor.do()
        print(len(winner))

    def get_columns_by_overlap(self,overlap):
        overlap_columns = []
        for column in self.columns:
            if column.dendrit_segment.overlap == overlap:
                overlap_columns.append(column)
        return overlap_columns

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

    def add_column(self):
        """
        add a coloumn at a certain position and initializes a dendrit_segment for each colloum
        :param pos:
        """
        for x in range(self.max_size):
            for y in range(self.max_size):
                pos = (x, y)
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