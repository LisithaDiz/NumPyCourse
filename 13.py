import numpy as np

B = np.array([[1, 2, 3, 4, 5],
              [6, 7, 8, 9, 10],
              [11, 12, 13, 14, 15],
              [16, 17, 18, 19, 20]])
#
# print(B.flatten())
# print(B.ravel())

print(B.transpose())
print(B.T) # Both equal

print(B.swapaxes(0,1))

