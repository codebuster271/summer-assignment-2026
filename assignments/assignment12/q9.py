import numpy as np


array = np.arange(1, 49).reshape(4, 4, 3)

print("Original 4x4x3 array:")
print(array)
print()
print("First two rows and first two columns of second set:")
print(array[1, :2, :2])