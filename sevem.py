import numpy as np

print(np.nan)
print(np.inf)

print(np.isnan(np.nan))
print(np.isinf(np.inf))

print(np.isnan(np.sqrt(-1)))
print(np.isinf(np.array([10])/0))
