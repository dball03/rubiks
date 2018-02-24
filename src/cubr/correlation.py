# Contains array which correlates the camera/face and the coordinates to the cube position.

import numpy as np

correlation = np.zeros((6,54), dtype=np.ndarray)

# TODO work out the proper coordinates
# Down face
correlation[0, 27] = (1 , 1)
correlation[0, 28] = (1 , 1)
correlation[0, 29] = (1 , 1)
correlation[0, 30] = (1 , 1)
correlation[0, 31] = (1 , 1)
correlation[0, 32] = (1 , 1)
correlation[0, 33] = (1 , 1)
correlation[0, 34] = (1 , 1)
correlation[0, 35] = (1 , 1)

# Back face
correlation[1, 45] = ( 1, 1)
correlation[1, 46] = ( 1, 1)
correlation[1, 47] = ( 1, 1)
correlation[1, 48] = ( 1, 1)
correlation[1, 49] = ( 1, 1)
correlation[1, 50] = ( 1, 1)
correlation[1, 51] = ( 1, 1)
correlation[1, 52] = ( 1, 1)
correlation[1, 53] = ( 1, 1)

# Right face
correlation[2, 9] = ( 1, 1)
correlation[2, 10] = ( 1, 1)
correlation[2, 11] = ( 1, 1)
correlation[2, 12] = ( 1, 1)
correlation[2, 13] = ( 1, 1)
correlation[2, 14] = ( 1, 1)
correlation[2, 15] = ( 1, 1)
correlation[2, 16] = ( 1, 1)
correlation[2, 17] = ( 1, 1)

# Front face
correlation[3, 18] = ( 1, 1)
correlation[3, 19] = ( 1, 1)
correlation[3, 20] = ( 1, 1)
correlation[3, 21] = ( 1, 1)
correlation[3, 22] = ( 1, 1)
correlation[3, 23] = ( 1, 1)
correlation[3, 24] = ( 1, 1)
correlation[3, 25] = ( 1, 1)
correlation[3, 26] = ( 1, 1)

# Up face
correlation[4, 0] = ( 1, 1)
correlation[4, 1] = ( 1, 1)
correlation[4, 2] = ( 1, 1)
correlation[4, 3] = ( 1, 1)
correlation[4, 4] = ( 1, 1)
correlation[4, 5] = ( 1, 1)
correlation[4, 6] = ( 1, 1)
correlation[4, 7] = ( 1, 1)
correlation[4, 8] = ( 1, 1)

# Left face
correlation[5, 36] = ( 1, 1)
correlation[5, 37] = ( 1, 1)
correlation[5, 38] = ( 1, 1)
correlation[5, 39] = ( 1, 1)
correlation[5, 40] = ( 1, 1)
correlation[5, 41] = ( 1, 1)
correlation[5, 42] = ( 1, 1)
correlation[5, 43] = ( 1, 1)
correlation[5, 44] = ( 1, 1)
