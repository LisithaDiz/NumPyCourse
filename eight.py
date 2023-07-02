import numpy as np

l1 = [1, 2, 3, 4, 55]
l2 = [6, 6, 45, 85, 2]

a1 = np.array(l1)
a2 = np.array(l2)

print(a1)
print(a2)

print(l1 * 5)  # just repeat in python list
print(l2 * 5)
print(l1 + l2)  # concatenate python array

print(a1 * 5)  # multiply in numpy array
print(a2 * 5)
print(a1 + a2)
