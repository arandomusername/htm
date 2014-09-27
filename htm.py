import htm_sub
import Cognition

class HTM(object):
    def __init__(self, region_quantity, region_size, input_size):
        self.input_region = htm_sub.input_region.InputRegion(input_size)
        self.cognitor = Cognition.main_cognition.Cognitor()
        self.regions = []

        self.add_regions(region_quantity, region_size)
        self.connect_regions()

    def add_regions(self, region_quantity, region_size):
        for x in range(region_quantity):
            self.regions.append(htm_sub.region.Region(region_size, region_size))

    def connect_regions(self):
        self.regions[0].connect_to_inputregion(self.input_region)
        for x in range(len(self.regions)-1):
            self.regions[x].connect_to_inputregion(self.regions[x+1])

    def process(self, input_array):
        self.input_region.new_input(input_array)
        for region in self.regions:
            self.cognitor.execute(region)