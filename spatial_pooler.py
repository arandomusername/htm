import numpy as np
import math


class spatial_pooler:
    activ_percent = .5
    inhibition_rad = 3

    def __init__(self):
        self.region = 0

    def __set_region(self, region):
        self.region = region

    def run(self, region, active_input):
        self.__set_region(region)
        region.update_activation(self.select_activated_v2(active_input))
        self.learn(active_input)

    def select_activated(self, active_input):
        activation = self.region.get_activation_scores(active_input)
        inhibition_x = int(activation.shape[0] * self.activ_percent)
        inhibition_y = int(activation.shape[1] * self.activ_percent)
        max_list     = []

        for x in range(activation.shape[0] - inhibition_x):
            x_max = x + inhibition_x
            for y in range(activation.shape[1] - inhibition_y):

                y_max = y + inhibition_y
                sub_ar = activation[x:x_max, y:y_max]
                coor_max = np.unravel_index(sub_ar.argmax(), sub_ar.shape)
                if coor_max != 0:
                    coor_max = (coor_max[0] + x, coor_max[1] + y)
                    max_list.append(coor_max)

        return max_list

    def select_activated_v2(self, active_input):
        activation = self.region.get_activation_scores(active_input)
        gauss_m    = gauss_matrix(spatial_pooler.inhibition_rad)
        it         = np.nditer(activation, flags=['multi_index'])
        inhibition = np.zeros(activation.shape)

        while not it.finished:
            temp = it[0] * gauss_m
            max_distance = (spatial_pooler.inhibition_rad - 1) / 2

            x1 = it.multi_index[0] - max_distance
            y1 = it.multi_index[1] - max_distance
            x2 = it.multi_index[0] + max_distance + 1
            y2 = it.multi_index[1] + max_distance + 1

            temp_x1 = 0
            temp_y1 = 0
            temp_x2 = spatial_pooler.inhibition_rad
            temp_y2 = spatial_pooler.inhibition_rad

            if x1 < 0:
                temp_x1 = -x1
                x1 = 0

            if y1 < 0:
                temp_y1 = -y1
                y1 = 0

            if x2 > activation.shape[0]:
                temp_x2 = activation.shape[0] - x2
                x2      = activation.shape[0]

            if y2 > activation.shape[1]:
                temp_y2 = activation.shape[1] - y2
                y2      = activation.shape[1]

            inhibition[x1:x2, y1:y2] += temp[temp_x1: temp_x2, temp_y1: temp_y2]
            it.iternext()

        inhibited = activation - inhibition
        return self.get_biggest_indices(inhibited, 7)

    def get_biggest_indices(self, arr, n):
        indices = (-arr).argpartition(n, axis=None)[:n]
        indices = np.vstack(np.unravel_index(indices, arr.shape)).transpose()
        return indices

    def learn(self, active_input):
        self.region.learn(active_input)


def gauss(x):
    if x == 0:
        return 0
    else:
        d = np.exp(-np.power(x, 2.) / 2 * np.power(1 + 1./x, 2.))
        return d


def gauss_matrix(size):
    m = np.zeros((size, size))
    for x in range(size):
        for y in range(size):
            distance = math.sqrt((x - (size - 1) / 2) ** 2 +
                                 (y - (size - 1) / 2) ** 2)
            m[x, y]  = gauss(distance)
    return m
