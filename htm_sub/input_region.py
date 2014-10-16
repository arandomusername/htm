from htm_sub import region

class InputRegion(region.Region):
    def __init__(self, input_size):
        region.Region.__init__(self, input_size, 1)
        self.columns = []
        self.max_size = input_size
        self.row_quantity = 1
        self.input_size = input_size
        self.neuron_quantity = input_size

        for x in range(0, self.max_size):
            self.add_columns()

    def new_input(self, input_array):
        self.reset_activity()

        for x in range(len(input_array)):
            if input_array[x] == 1:
                self.columns[x].neurons[0].activate()
1
