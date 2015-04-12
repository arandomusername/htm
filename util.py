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
