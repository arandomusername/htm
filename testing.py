from spatial_pooler import spatial_pooler
from region import region
import numpy as np

if __name__ == "__main__":
    input_shape = (2, 2)
    reg_size     = 4
    reg1 = region(reg_size, input_shape)
    reg2 = region(reg_size, (reg_size, reg_size))
    sp  = spatial_pooler()
    for x in range(100):
        active_input = np.random.randint(2, size=input_shape)
        print(active_input)
        sp.run(reg1, active_input)
        sp.run(reg2, reg1.active_columns)
        print(reg2.active_columns)
