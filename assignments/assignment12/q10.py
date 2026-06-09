import numpy as np


array = np.array([[23, 56, 78, 93], [71, 82, 13, 24]])

print("Original array:")
print(array)
print()

for row_index in range(array.shape[0]):
    for col_index in range(array.shape[1]):
        if array[row_index, col_index] % 2 != 0:
            array[row_index, col_index] = -1

print("Odd numbers replaced with -1:")
print(array)