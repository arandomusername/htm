from htm import cla_column


class Region():
    def __init__(self, size):
        self.columns = [[]]
        self.max_size = size
        self.neuron_quantity = (size**2) * cla_column.Column.size
        self.add_columns()
        self.initialize_proximale_dendrites()

    def get_columns_by_overlap(self, overlap):
        overlap_columns = [column for column in self.all_columns() if column.dendrite_segment.overlap == overlap]
        return overlap_columns

    def get_active_neurons(self):
        actives = []
        for col in self.all_columns():
            actives.extend(col.active_cells())
        return actives

    def set_overlap(self):
        for column in self.all_columns():
            column.dendrite_segment.set_overlap()

    def add_columns(self):
        self.columns = [[cla_column.Column((x, y)) for x in xrange(self.max_size)]for y in xrange(self.max_size)]

    def all_neurons(self):
        for column in self.all_columns():
            for neuron in column.neurons:
                yield neuron

    def all_columns(self):
        for y in range(self.max_size):
            for x in range(self.max_size):
                yield self.columns[x][y]

    def get_column_by_position(self, pos):
        x_position = pos[0]
        y_position = pos[1]
        column = self.columns[x_position][y_position]
        return column

    def reset_overlaps(self):
        for neuron in self.all_neurons():
            neuron.dendrite_segment.overlap = 0

    def reset_activity(self):
        for column in self.all_columns():
            column.reset_activity()

    def connect_to_inputregion(self, input_region):
        for column in self.all_columns():
            column.dendrite_segment.init_dendrites(input_region, 2)


    def initialize_proximale_dendrites(self):
        for neuron in self.all_neurons():
            neuron.dendrite_segment.init_dendrites(self, 3)