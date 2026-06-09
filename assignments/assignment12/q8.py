import numpy as np


array = np.arange(1, 17).reshape(4, 4)

print("Original 4x4 array:")
print(array)
print()
print("Odd rows and even columns:")
print(array[::2, 1::2])