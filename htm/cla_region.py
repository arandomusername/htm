from htm import cla_column


class Region():
    def __init__(self, size):
        self.columns = []
        self.max_size = size
        self.neuron_quantity = (size**2) * cla_column.Column.size
        self.add_column()
        self.initialize_proximale_dendrites()

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
        return actives

    def set_overlap(self):
        for coll in self.columns:
            coll.dendrit_segment.set_overlap()

    def add_column(self):
        for x in range(self.max_size):
            for y in range(self.max_size):
                pos = (x, y)
                coll = cla_column.Column(pos)
                self.columns.append(coll)

    def get_column_by_position(self, pos):
        x_position = pos[0]
        y_position = pos[1]

        one_dimension = x_position * self.max_size + y_position
        column = self.columns[one_dimension]
        return column

    def reset_overlaps(self):
        for coll in self.columns:
            coll.dendrit_segment.overlap = 0
            for neuron in coll.neurons:
                neuron.dendrit_segment.overlap = 0


    def reset_activity(self):
        for col in self.columns:
            col.reset_activity()

    def connect_to_inputregion(self, input_region):
        for col in self.columns:
            col.dendrit_segment.init_dendrites(input_region, 2)


    def initialize_proximale_dendrites(self):
        for column in self.columns:
            for neuron in column.neurons:
                neuron.dendrit_segment.init_dendrites(self, 3)
                neuron.dendrit_segment.reset_dendrites()