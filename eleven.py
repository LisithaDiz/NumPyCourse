import numpy as np

a = np.array([[1, 2, 3],
              [4, 5, 6]])

print(np.delete(a, 1))
print(np.delete(a, 3))
print(np.delete(a, 4))

a = np.array([[1, 2, 3],
              [4, 5, 6]])

print(np.delete(a, 1, 0))
print(np.delete(a, 1, 1))

print('Array B\n')

B = np.array([[1, 2, 3, 4, 5],
              [6, 7, 8, 9, 10],
              [11, 12, 13, 14, 15],
              [16, 17, 18, 19, 20]])

print(B.ndim)

print(np.delete(B, 1))
print(np.delete(B, 2, axis=0))
print(np.delete(B, 1, axis=0))
print(np.delete(B, 3, axis=1))


