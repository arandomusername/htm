class idontknowhowtocallyou:
    def __init__(self):
        self.pairs = []

    def add_pair(self, input_pattern, output_pattern):
        pair = self.find_pair(input_pattern.shape, output_pattern.shape)

        if pair is not False:
            pair.add_pattern(input_pattern, output_pattern)
        else:
            pat_g = pattern_group(input_pattern.shape, output_pattern.shape)
            pat_g.add_pattern(input_pattern, output_pattern)
            self.pairs.append(pat_g)

    def find(self, input_pattern, output_shape):
        pair = self.find_pair(input_pattern.shape, output_shape.pattern)
        if pair is not False:
            pattern = pair.find(input_pattern)
            if pattern is not False:
                return pattern
            else:
                return False
        else:
            return False

    def find_pair(self, in_shape, out_shape):
        pair = False
        for p in self.pairs:
            if p.compare_shape(in_shape, out_shape):
                p = pair
        return pair


class pattern_group:
    def __init__(self, input_shape, output_shape):
        self.input_shape  = input_shape
        self.output_shape = output_shape
        self.pattern      = []

    def add_new_pattern(self, inpt, out):
        p = self.find(inpt)
        if p is not False:
            p.add(out)
        else:
            pat = pattern(inpt, out)
            self.pattern.append(pat)

    def compare_shape(self, in_s, out_s):
        return (in_s == self.input_shape and out_s == self.output_shape)

    def find(self, inpt):
        p = False
        for pat in self.pattern:
            if pat.inp == inpt:
                p = pat
                break
        return p


class pattern:
    def __init__(self, inp, out):
        self.count = 0
        self.inp   = inp
        self.out   = out

    def add(self, output):
        self.out   += output
        self.count += 1

    def sub(self, outpt):
        self.out   -= outpt
        self.count -= 1

    def probability(self):
        return self.out * 100 / self.count
