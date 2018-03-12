# Contains array which correlates the camera/face and the coordinates to the cube position.

import numpy as np

correlation = np.zeros((6,54), dtype=np.ndarray)

# TODO work out the proper coordinates
# Down face
correlation[0, 27] = (100 , 100)
correlation[0, 28] = (150 , 100)
correlation[0, 29] = (200 , 100)
correlation[0, 30] = (100 , 150)
correlation[0, 31] = (150 , 150)
correlation[0, 32] = (200 , 150)
correlation[0, 33] = (100 , 200)
correlation[0, 34] = (150 , 200)
correlation[0, 35] = (200 , 200)

# Back face
correlation[1, 45] = (200, 200)
correlation[1, 46] = (150, 200)
correlation[1, 47] = (100, 200)
correlation[1, 48] = (200, 150)
correlation[1, 49] = (150, 150)
correlation[1, 50] = (100, 150)
correlation[1, 51] = (200, 100)
correlation[1, 52] = (150, 100)
correlation[1, 53] = (100, 100)

# Right face
correlation[2, 9] =  (200, 200)
correlation[2, 10] = (150, 200)
correlation[2, 11] = (100, 200)
correlation[2, 12] = (200, 150)
correlation[2, 13] = (150, 150)
correlation[2, 14] = (100, 150)
correlation[2, 15] = (200, 100)
correlation[2, 16] = (150, 100)
correlation[2, 17] = (100, 100)

# Front face
correlation[3, 18] = (200, 200)
correlation[3, 19] = (150, 200)
correlation[3, 20] = (100, 200)
correlation[3, 21] = (200, 150)
correlation[3, 22] = (150, 150)
correlation[3, 23] = (100, 150)
correlation[3, 24] = (200, 100)
correlation[3, 25] = (150, 100)
correlation[3, 26] = (100, 100)

# Up face
correlation[4, 0] = (200, 200)
correlation[4, 1] = (150, 200)
correlation[4, 2] = (100, 200)
correlation[4, 3] = (200, 150)
correlation[4, 4] = (150, 150)
correlation[4, 5] = (100, 150)
correlation[4, 6] = (200, 100)
correlation[4, 7] = (150, 100)
correlation[4, 8] = (100, 100)

# Left face
correlation[5, 36] = (100, 200)
correlation[5, 37] = (100, 150)
correlation[5, 38] = (100, 100)
correlation[5, 39] = (150, 200)
correlation[5, 40] = (150, 150)
correlation[5, 41] = (150, 100)
correlation[5, 42] = (200, 200)
correlation[5, 43] = (200, 150)
correlation[5, 44] = (200, 100)
