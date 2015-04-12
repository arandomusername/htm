import numpy as np


class util:
    def __init__(self):
        pair = []

    def add_pair(self, input_shape, output_shape):
        dt = np.dtype({'names': ['input', 'output','count'],
                       'formats':[(input_shape)np.int,
                                  (output_shape)np.int,
                                  np.int]
                       })

class pattern:
    def __init__(self, input_shape, output_shape):
       self.count = 0
       self.in    = input_shape
       self.out   = out

    def add(self, output):
       self.out   += output
       self.count += 1

    def increase_patter(self, input, output ):
        pass
