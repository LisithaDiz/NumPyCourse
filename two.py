import numpy as np


a = np.array([[1, 2, 3],
              [2, "Hello", 6],
              [7, 7, 8]])

print(a.dtype) # str
print(type(a[0][0]))  # str

b = np.array([[1, 2, 3],
              [2, 4, 6],
              [7, 7, 8]])

print(b.dtype) # int
print(type(b[0][0])) # int


c = np.array([[1, 2, 3],
              [2, "5", 6],
              [7, 7, 8]], dtype=np.float32)

print(c.dtype) # int
print(type(c[0][0])) # int
