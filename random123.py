import numpy as np

numbers = np.random.randint(2, size=(2,3,4))
print(numbers)

numbers = np.random.binomial(10, p=0.5, size=(5,10))
print(numbers)

numbers = np.random.normal(loc=170, scale=15, size=(5, 10))
print(numbers)

numbers = np.random.choice([10,40,50,20,51,20,2],  size=(5, 3))
print(numbers)
