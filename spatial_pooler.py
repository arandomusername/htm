import numpy as np
import math


class spatial_pooler:
    active_percent = .1515
    inhibition_rad = 3

    def __init__(self):
        self.region = 0

    def __set_region(self, region):
        self.region = region

    def run(self, region, active_input):
        self.__set_region(region)
        inhibited = self.select_activated_gauss(active_input)
        region.update_column_activation(inhibited)
        self.learn(active_input)
        self.region.pattern.add_pattern(active_input, region.active_columns)

    def select_activated(self, active_input):
        activation = self.region.get_activation_scores(active_input)
        inhibition_x = int(activation.shape[0] * self.active_percent)
        inhibition_y = int(activation.shape[1] * self.active_percent)
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

    def select_activated_gauss(self, active_input):
        # initialize necesarry aid matrizes
        activation = self.region.get_activation_scores(active_input)
        gauss_m    = gauss_matrix(spatial_pooler.inhibition_rad, 2)
        it         = np.nditer(activation, flags=['multi_index'])
        inhibition = np.zeros(activation.shape)

        # calculate the number of activated neurons
        active_field = np.count_nonzero(active_input) * 1.0 / active_input.size
        active_num   = math.floor(activation.size * (self.active_percent *
                                                     (active_field + 1)))

        # iterate over every position calculate its local inhibition with gauss
        while not it.finished:
            local_pos  = [[] for x in range(2)]
            global_pos = [[] for x in range(2)]
            # [0] --> start
            # [1] --> end

            local_inhibition = it[0] * gauss_m
            max_distance     = (spatial_pooler.inhibition_rad - 1) / 2

            for n in range(2):
                local_pos[0].append(0)
                local_pos[1].append(spatial_pooler.inhibition_rad - 1)

                global_pos[0].append(it.multi_index[n] - max_distance)
                global_pos[1].append(it.multi_index[n] + max_distance)

                if global_pos[0][n] < 0:
                    local_pos[0][n] = -global_pos[0][n]
                    global_pos[0][n]   = 0

                if global_pos[1][n] >= activation.shape[n]:
                    local_pos[1][n]  = activation.shape[n] - global_pos[1][n]
                    global_pos[1][n] = activation.shape[n] - 1

            local_pos = np.array(local_pos).transpose()
            global_pos = np.array(global_pos).transpose()

            inhibition[np.ix_(*global_pos)] += local_inhibition[np.ix_(*local_pos)]
            it.iternext()

        inhibited = activation - inhibition
        return self.get_biggest_indices(inhibited, active_num)

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


def gauss_matrix(size, dim):
    shape   = ()
    mid_pos = ()
    for x in range(dim):
        shape   = shape   + (size,)
        mid_pos = mid_pos + ((size - 1) / 2.,)

    m = np.zeros(shape)
    for pos, value  in np.ndenumerate(m):
        distance = 0
        for x in range(dim):
            distance += (pos[x] - mid_pos[x]) ** 2
        distance = math.sqrt(distance)
        m[pos]   = gauss(distance)
    return np.array(m)
