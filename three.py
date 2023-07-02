import numpy as np
# https://numpy.org/doc/stable/user/basics.types.html
d = {"1":'A'}

a = np.array([[1223,2,4],
              [4,d,7],
              [6.54,8,'Hello']])

b = np.array([[1223,2,4],
              [4,d,7],
              [6.54,8,7]], dtype="<U7")

print(a.dtype)
print(type(a[1][0]))