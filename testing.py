from spatial_pooler import spatial_pooler
from region import region
import numpy as np
import matplotlib.pyplot as plt


if __name__ == "__main__":
    input_shape = (2, 2)
    reg_size     = 4
    reg1 = region(reg_size, input_shape)
    sp  = spatial_pooler()
    for x in range(100):
        active_input = np.random.randint(2, size=input_shape)
        print(active_input)
        sp.run(reg1, active_input)
        print(np.count_nonzero(reg1.active_columns))

    for x in range(10):
        active_input = np.random.randint(2, size=input_shape)
        print(active_input)
        reg1.pattern.show(active_input)


