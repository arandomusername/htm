from htm_sub import column


class Region(object):
    def __init__(self, row_quantity, column_quantity):
        self.columns = [[]]
        self.column_quantity = column_quantity
        self.row_quantity = row_quantity
        self.max_size = row_quantity * column_quantity
        self.neuron_quantity = self.max_size * column.Column.size
        self.add_columns()
        self.initialize_proximale_dendrites()

    def get_columns_by_overlap(self, overlap):
        overlap_columns = [col for col in self.all_columns() if col.dendrite_segment.overlap == overlap]
        return overlap_columns

    def get_active_neurons(self):
        actives = []
        for column in self.all_columns():
            actives.extend(column.active_cells())
        return actives

    def set_overlap(self):
        for column in self.all_columns():
            column.dendrite_segment.set_overlap()

    def add_columns(self):
        self.columns = [[column.Column((x, y)) for x in range(self.row_quantity)]for y in range(self.column_quantity)]

    def all_neurons(self):
        list_of_neurons = []
        for col in self.all_columns():
            for neuron in col.neurons:
                list_of_neurons.append(neuron)
        return list_of_neurons

    def all_columns(self):
        columns = []
        for y in range(self.column_quantity):
            for x in range(self.row_quantity):
                columns.append(self.columns[y][x])
        return columns

    def get_column_by_position(self, pos):
        x_position = pos[0]
        y_position = pos[1]

        return self.columns[x_position][y_position]

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