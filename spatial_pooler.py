import numpy as np


class temporal_pooler:
    activ_percent = .3

    def __init__(self, reg):
        self.region = reg

    def __set_region(self, region):
        self.region = region

    def run(self, region):
        self.__set_region(region)
        region.update_activation(self.select_activated())

    def select_activated(self):
        activation = self.region.get_activation_matrix()
        inhibition_x = int(activation.shape()[0] * self.activ_percent)
        inhibition_y = int(activation.shape()[1] * self.activ_percent)
        max_list     = []

        for x in range(activation.shape()[0] - inhibition_x):
            x_max = x + inhibition_x
            for y in range(activation.shape()[1] - inhibition_y):

                y_max = y + inhibition_y
                sub_ar = activation[x:x_max, y:y_max]
                coor_max = np.unravel_index(sub_ar.argmax(), sub_ar.shape)
                if coor_max != 0:
                    coor_max[0] += x
                    coor_max[1] += y
                    max_list.append(coor_max)

        return max_list

    def learn(self):
        self.region.learn()
