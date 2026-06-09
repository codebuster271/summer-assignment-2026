import numpy as np


array = np.arange(1, 49).reshape(4, 4, 3)
value = array[1, 0, 2]

print("4x4x3 array:")
print(array)
print()
print("Value at second set, first row, last column:")
print(value)