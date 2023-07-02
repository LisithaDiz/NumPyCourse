import numpy as np

B = np.array([[1, 2, 3, 4, 5],
              [6, 7, 8, 9, 10],
              [11, 12, 13, 14, 15],
              [16, 17, 18, 19, 20]])

print(B.shape)
print(B.reshape((5, 4)))
print(B.reshape((20, )))
print(B.reshape((2, 10)))
print(B.reshape((2, 2, 5)))

B.resize((10,2))
print(B)
