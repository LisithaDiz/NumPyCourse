import numpy as np
#
# a = np.array([[1, 2, 3, 4, 5,6],
#               [6, 7, 8, 9, 10,12],
#               [11, 12, 13, 14, 15,1],
#               [16, 17, 18, 19, 20,1]])
#
# np.save("array123.npy", a)
a = np.load("array123.npy")
print(a)