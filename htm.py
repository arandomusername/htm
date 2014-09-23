import region
import Cognition

class HierachicalTemporalMemory(object):
    def __init__(self, region_quantity, region_size, input_size):
        self.input_region = region.InputRegion(input_size)
        self.cognitor = Cognition.Cognitor

        self.regions  = []
        self.add_regions(region_quantity, region_size)
        self.connect_regions(self)

    def add_regions(self, region_quantity, region_size):
        for x in range(region_quantity):
            self.regions.append(region.Region(region_size, region_size))


    def connect_regions(self):
        self.regions[0].connect_to_inputregion(self.input_region)
        for x in range(len(self.regions)-1):
            self.region[x].connect_to_inputregion(self.regions[x+1])

    def