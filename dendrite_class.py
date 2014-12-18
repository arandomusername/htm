import random


class Dendrites(object):
    def __init__(self):
        self.list = []

    def __contains__(self, item):
        if item in self.list:
            return True
        else:
            return False

    def __iter__(self):
        return self.list

    def __repr__(self):
        return "{0}-{1}".format(self.__class__.__name__, len(self.list))

    def add_dendrites(self, start, end):
        if type(start) == list and type(end) == object:
            for x in start:
                self.list.append(SingleDendrite(x, end))

        elif type(start) == object and type(end) == list:
            for x in end:
                self.list.append(SingleDendrite(start, x))

        elif type(start) == list and type(end) == list:
            for x in start:
                for y in end:
                    self.list.append(SingleDendrite(x, y))


class SingleDendrite(object):
    strength_step = 0.01  # some random value for now

    def __init__(self, start, end):
        self.strength = 0  # some default-value between 0-1
        self.start    = start
        self.end      = end

    def __repr__(self):
        return "{0} {1} - {2}: {3}".format(self.__class__.__name__, self.start, self.end, self.strength)

    def __cmp__(self, other):
        if other.strength < self.strength:
            return 1
        elif other.strength > self.strength:
            return -1
        else:
            return 0

    def increase_strength(self):
        self.strength += SingleDendrite.strength_step
        self.__check_strength__()

    def decrease_strength(self):
        self.strength -= SingleDendrite.strength_step
        self.__check_strength__()

    def __check_strength__(self):
        if self.strength > 1.:
            self.strength = 1.
        elif self.strength < 0.:
            self.strength = 0.

    def init_random_strength(self):
        self.strength = random.randrange(0, 100) / 100