from column_class import Column
from dendrite_class import Dendrites, SingleDendrite

class Region(object):
    def __init__(self):
        self.columns   = []
        self.dendrites = []

    def __repr__(self):
        return "Region: {0}".format(len(self.columns))

    def add_columns(self, col_quantity):
        self.columns = [Column(x) for x in range(col_quantity)]
