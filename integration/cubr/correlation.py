# Contains array which correlates the camera/face and the coordinates to the cube position.

# TODO NB currently it is designed to iterate through the positions and check the coordinates:
# This is done to require a smaller array, rather using pixel coords.

# TODO For the first robot iteration, 8,9 and 20 require larger areas as they are viewed through the motor posts
# Perhaps this can use the "spare" member, which would also be used for the orientation in the second robot

# TODO at some point, this will probably be used for adjusting/displaying the "Regions of interest" in a preview menu

import numpy as np

correlation = np.zeros((3,54), dtype=np.ndarray)

# RUF camera
#correlation[0, 38] = (35 , 125)
#correlation[0, 37] = (40 , 195)
#correlation[0, 41] = (95 , 160)
#correlation[0, 39] = (100, 300)
#correlation[0, 44] = (155, 200)
#correlation[0, 43] = (160, 290)
#correlation[0, 42] = (165, 350)
#correlation[0, 27] = (225, 200)
#correlation[0, 30] = (225, 290)
#correlation[0, 33] = (225, 350)
#correlation[0, 28] = (295, 170)
#correlation[0, 34] = (280, 310)
#correlation[0, 29] = (355, 125)
#correlation[0, 32] = (345, 195)
#correlation[0, 18] = (55 , 75 )
#correlation[0, 21] = (120, 100)
#correlation[0, 24] = (190, 135)
#correlation[0, 19] = (125, 40 )
#correlation[0, 25] = (260, 100)
#correlation[0, 20] = (195, 15 )
#correlation[0, 23] = (260, 40 )
#correlation[0, 26] = (330, 70 )

correlation[0, 38] = (83 , 93)
correlation[0, 37] = (85 , 128)
correlation[0, 41] = (113 , 110)
correlation[0, 39] = (115 , 180)
correlation[0, 44] = (143 , 130)
correlation[0, 43] = (145 , 175)
correlation[0, 42] = (148 , 205)
correlation[0, 27] = (178, 130)
correlation[0, 30] = (178, 175)
correlation[0, 33] = (178, 205)
correlation[0, 28] = (213, 115)
correlation[0, 34] = (205, 185)
correlation[0, 29] = (243, 93)
correlation[0, 32] = (238, 128)
correlation[0, 18] = (92 , 68 )
correlation[0, 21] = (125 , 80)
correlation[0, 24] = (150 , 98)
correlation[0, 19] = (128 , 50 )
correlation[0, 25] = (195, 80)
correlation[0, 20] = (163 ,  37)
correlation[0, 23] = (195, 50)
correlation[0, 26] = (230, 65)



# BRD camera
#correlation[1, 45] = (35 , 125)
#correlation[1, 48] = (40 , 195)
#correlation[1, 46] = (95 , 160)
#correlation[1, 52] = (100, 300)
#correlation[1, 47] = (155, 200)
#correlation[1, 50] = (160, 290)
#correlation[1, 53] = (165, 350)
#correlation[1, 36] = (225, 200)
#correlation[1, 39] = (225, 290)
#correlation[1, 42] = (225, 350)
#correlation[1, 37] = (295, 170)
#correlation[1, 43] = (280, 310)
#correlation[1, 38] = (355, 125)
#correlation[1, 41] = (345, 195)
#correlation[1, 2 ] = (55 , 75 )
#correlation[1, 1 ] = (120, 100)
#correlation[1, 0 ] = (190, 135)
#correlation[1, 5 ] = (125, 40 )
#correlation[1, 3 ] = (260, 100)
#correlation[1, 8 ] = (195,  15)
#correlation[1, 7 ] = (260,  40)
#correlation[1, 6 ] = (330,  70)

correlation[1, 45] = (88 , 83)
correlation[1, 48] = (90 , 118)
correlation[1, 46] = (118 , 100)
correlation[1, 52] = (120 , 170)
correlation[1, 47] = (148 , 120)
correlation[1, 50] = (150 , 165)
correlation[1, 53] = (153 , 195)
correlation[1, 36] = (183, 120)
correlation[1, 39] = (183, 165)
correlation[1, 42] = (183, 195)
correlation[1, 37] = (218, 105)
correlation[1, 43] = (210, 175)
correlation[1, 38] = (248, 83)
correlation[1, 41] = (243, 118)
correlation[1, 2 ] = (97 , 58 )
correlation[1, 1 ] = (130 , 70)
correlation[1, 0 ] = (155 , 88)
correlation[1, 5 ] = (133 , 40 )
correlation[1, 3 ] = (200, 70)
correlation[1, 8 ] = (168 ,  27)
correlation[1, 7 ] = (200, 40)
correlation[1, 6 ] = (235, 55)



# UBL camera
#correlation[2, 29] =  (35 , 125)
#correlation[2, 28] =  (40 , 195)
#correlation[2, 32] =  (95 , 160)
#correlation[2, 30] =  (100, 300)
#correlation[2, 35] =  (155, 200)
#correlation[2, 34] =  (160, 290)
#correlation[2, 33] =  (165, 350)
#correlation[2, 51] =  (225, 200)
#correlation[2, 52] =  (225, 290)
#correlation[2, 53] =  (225, 350)
#correlation[2, 48] =  (295, 170)
#correlation[2, 50] =  (280, 310)
#correlation[2, 45] =  (355, 125)
#correlation[2, 46] =  (345, 195)
#correlation[2, 15] =  (55 , 75 )
#correlation[2, 16] =  (120, 100)
#correlation[2, 17] =  (190, 135)
#correlation[2, 12] =  (125, 40 )
#correlation[2, 14] =  (260, 100)
#correlation[2, 9 ] =  (195, 15 )
#correlation[2, 10] =  (260, 40 )
#correlation[2, 11] =  (330, 70 )



correlation[2, 29] =  (83 , 83)
correlation[2, 28] =  (85 , 118)
correlation[2, 32] =  (113 , 100)
correlation[2, 30] =  (115 , 170)
correlation[2, 35] =  (143 , 120)
correlation[2, 34] =  (145 , 165)
correlation[2, 33] =  (148 , 195)
correlation[2, 51] =  (178, 120)
correlation[2, 52] =  (178, 165)
correlation[2, 53] =  (178, 195)
correlation[2, 48] =  (213, 105)
correlation[2, 50] =  (205, 175)
correlation[2, 45] =  (243, 83)
correlation[2, 46] =  (238, 118)
correlation[2, 15] =  (92 , 58 )
correlation[2, 16] =  (125 , 70)
correlation[2, 17] =  (150 , 88)
correlation[2, 12] =  (128 , 40 )
correlation[2, 14] =  (195, 70)
correlation[2, 9 ] =  (163 ,  27)
correlation[2, 10] =  (195, 40)
correlation[2, 11] =  (230, 55)
