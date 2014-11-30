__author__ = 'Martin'

class Dendrites(object):
    def __init__(self):
        self.list = []


class SingleDendrite(object):
    strength_step = 0.2              #some random value for now

    def __init__(self, start, end):
        self.strength = 0            #some default-value between 0-1
        self.start    = start
        self.end      = end

    def increase_strength(self):
        self.strength += SingleDendrite.strength_step
        self.__check_strength__()
    
    def decrease_strength(self):
        self.strength -= SingleDendrite.strength_step
        self.__check_strength__()

    def _check_strength__(self):
        if self.strength > 1:
            self.strength = 1
        if self.strength < 0:
            self.strength = 0