import numpy as np


class util:
    def __init__(self):
        self.pair = []

    def add_pair(self, input_shape, output_shape):
        pass


class p_list:
    def __init__(self, input_shape, output_shape):
        self.input_shape  = input_shape
        self.output_shape = output_shape
        self.shapes       = []

    def add_pattern(self, in, out):
        test = True
        for shape in self.shapes:
            if shape.in == in:
                shape.add(out)
                test = False
                break
        if test:
            pat = pattern(in, out)
            self.append(pat)

    def compare_shape(self, in_s, out_s):
        return in_s == self.input_shape and out_s = self.output_shape


class pattern:
    def __init__(self, inp, out):
       self.count = 0
       self.in    = inp
       self.out   = out

    def add(self, output):
       self.out   += output
       self.count += 1
