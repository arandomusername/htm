import cla.Cognition
from cla import cla_column


class Region():
    def __init__(self, size):
        self.search_range = 5        # at which radius winners are searched.
        self.inhibition_radius = 4   #
        self.columns = []
        self.max_size = size
        self.neuron_quantity = (size**2) * cla_column.Column.size
        self.add_column()

    def cognition(self):
        """
        starts the spacial learning
        :param
        """
        sp_cognitor = cla.Cognition.SpacialCognitor(self)
        winner = sp_cognitor.do()

        te_cognitor = cla.Cognition.TemporalCognitor(self, winner)
        te_cognitor.do()

    def get_columns_by_overlap(self, overlap):
        overlap_columns = []
        for column in self.columns:
            if column.dendrit_segment.overlap == overlap:
                overlap_columns.append(column)
        return overlap_columns

    def get_active_neurons(self):
        actives = []
        for col in self.columns:
            actives.extend(col.get_active_cells())

    def set_overlap(self):
        """
        sets the overlap score for each column
        """
        for coll in self.columns:
            coll.dendrit_segment.set_overlap()

    def add_column(self):
        """
        add a coloumn at a certain position and initializes a dendrit_segment for each colloum
        """
        for x in range(self.max_size):
            for y in range(self.max_size):
                pos = (x, y)
                coll = cla_column.Column(pos)
                self.columns.append(coll)

    def get_column_by_position(self, pos):
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

    def reset_activity(self):
        for col in self.columns:
            col.reset_activity()

    def initialize_dendrites(self, input_region):
        for col in self.columns:
            col.dendrit_segment.initialize_dendriten(input_region, 2)
            for neuron in col.neurons:
                neuron.dendrit_segment.initialize_dendriten(self, 4)