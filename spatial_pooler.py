import numpy as np
import math


class spatial_pooler:
    active_percent = .2
    inhibition_rad = 3

    def __init__(self):
        self.region = 0

    def __set_region(self, region):
        self.region = region

    def run(self, region, active_input):
        self.__set_region(region)
        inhibited = self.select_activated_gauss(active_input)
        print(inhibited)
        print(self.select_activated_gauss_v2(active_input))
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
        activation = self.region.get_activation_scores(active_input)
        gauss_m    = gauss_matrix(spatial_pooler.inhibition_rad,
                                  len(activation.shape))
        it         = np.nditer(activation, flags=['multi_index'])
        inhibition = np.zeros(activation.shape)

        activ_field = np.count_nonzero(active_input) * 1.0 / active_input.size
        number_activated = math.floor(activation.size * (self.active_percent *
                                                         (activ_field + 1)))
        while not it.finished:
            inh = it[0] * gauss_m
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
                x1      = 0

            if y1 < 0:
                temp_y1 = -y1
                y1      = 0

            if x2 > activation.shape[0]:
                temp_x2 = activation.shape[0] - x2
                x2      = activation.shape[0]

            if y2 > activation.shape[1]:
                temp_y2 = activation.shape[1] - y2
                y2      = activation.shape[1]

            inhibition[x1:x2, y1:y2] += inh[temp_x1: temp_x2, temp_y1: temp_y2]
            it.iternext()

        inhibited = activation - inhibition
        return self.get_biggest_indices(inhibited, number_activated)

    def select_activated_gauss_v2(self, active_input):
        # initialize necesarry aid matrizes
        dim        = len(active_input.shape)
        activation = self.region.get_activation_scores(active_input)
        gauss_m    = gauss_matrix(spatial_pooler.inhibition_rad, dim)
        it         = np.nditer(activation, flags=['multi_index'])
        inhibition = np.zeros(activation.shape)

        # calculate the number of activated neurons
        active_field = np.count_nonzero(active_input) * 1.0 / active_input.size
        active_num   = math.floor(activation.size * (self.active_percent *
                                                     (active_field)))

        # iterate over every position calculate its local inhibition with gauss
        while not it.finished:
            local_pos        = [[] for x in range(2)]
            inh_pos          = [[] for x in range(2)]
            local_inhibition = it[0] * gauss_m
            max_distance     = (spatial_pooler.inhibition_rad - 1) / 2


            for n in range(dim):
                local_pos[0].append(0)
                local_pos[1].append(spatial_pooler.inhibition_rad)

                inh_pos[0].append(it.multi_index[n] - max_distance)
                inh_pos[1].append(it.multi_index[n] + max_distance + 1)

                if inh_pos[0][n] < 0:
                    local_pos[0][n] = -inh_pos[0][n]
                    inh_pos[0][n]   = 0

                if inh_pos[1][n] > activation.shape[n]:
                    local_pos[1][n] = activation.shape[n] - inh_pos[1][n]
                    inh_pos[1][n]   = activation.shape[n]

            self.add_inhibited(dim, inhibition, local_inhibition, local_pos,
                               inh_pos)
            it.iternext()

        inhibited = activation - inhibition
        return self.get_biggest_indices(inhibited, active_num)

    def add_inhibited(self, dim, global_inhibition, local_inhibition,
                      local_pos, inh_pos):
        local_pos  = np.array(local_pos).transpose()
        global_pos = np.array(inh_pos).transpose()
        count = len(local_pos)

        import pdb; pdb.set_trace()  # XXX BREAKPOINT
        for x in range(count):
            global_inhibition[global_pos[x]] = global_inhibition[global_pos[x]] + local_inhibition[local_pos[x]]

    def get_biggest_indices(self, arr, n):
        indices = (-arr).argpartition(n, axis=None)[:n]
        indices = np.vstack(np.unravel_index(indices, arr.shape)).transpose()
        return indices

    def learn(self, active_input):
        self.region.learn(active_input)


def create_perms(n, dim, pos, old_list):
    #  create list of permutations in given dimension
    if n < dim:
        new_list = []
        if len(old_list) == 0:
            for x in range(pos[0][n], pos[1][n]):
                new_list.append([x])
        else:
            for element in old_list:
                for x in range(pos[0][n], pos[1][n]):
                    new_list.append(element + [x])

        return create_perms(n+1, dim, pos, new_list)

    else:
        return old_list


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
