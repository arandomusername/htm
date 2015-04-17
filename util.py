import matplotlib.pyplot as plt


class pattern_group:
    def __init__(self, input_shape, output_shape):
        self.input_shape  = input_shape
        self.output_shape = output_shape
        self.pattern      = []

    def add_pattern(self, inpt, out):
        p = self.find(inpt)
        if p is not False:
            p.add(out)
        else:
            pat = pattern(inpt, out)
            self.pattern.append(pat)

    def compare_shape(self, in_s, out_s):
        return (in_s == self.input_shape and out_s == self.output_shape)

    def find(self, inpt):
        for pat in self.pattern:
            if (pat.inp == inpt).all():
                return pat
                break
        else:
            return False

    def show(self, inpt):
        pat = self.find(inpt)
        if pat is not False:
            plt.imshow(pat.out, cmap='gray',  interpolation="nearest")
            plt.colorbar()
            plt.show()
        else:
            print("couldn't find that pattern")

    def prt(self, inpt):
        pat = self.find(inpt)
        if pat is not False:
            print(pat)
        else:
            print(0)


class pattern:
    def __init__(self, inp, out):
        self.count = 1
        self.inp   = inp
        self.out   = out

    def add(self, output):
        self.out   = self.out + output
        self.count += 1

    def sub(self, outpt):
        self.out   -= outpt
        self.count -= 1

    def probability(self):
        return self.out * 100 / self.count
