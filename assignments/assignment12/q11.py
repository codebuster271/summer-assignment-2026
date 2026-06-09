import numpy as np


array = np.array([1, 0, 2, 0, 3, 0, 4])
indices = np.nonzero(array)

print("Array:")
print(array)
print()
print("Indices of non-zero elements:")
print(indices)