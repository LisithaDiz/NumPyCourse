import numpy as np

a = np.array([[1, 2, 3, 4, 5],
              [6, 7, 8, 9, 10]])

b = np.array([[11, 12, 13, 14, 15],
              [16, 17, 18, 19, 20]])

c = np.concatenate((a, b), axis=0)

d = np.stack((a, b))

v = np.vstack((a, b))
h = np.hstack((a, b))

print(c)
print(r)
print(d)