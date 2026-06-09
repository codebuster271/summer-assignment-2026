import numpy as np


arr1d = np.array([1, 2, 3, 4])
arr2d = np.array([[5, 6, 7, 8], [9, 10, 11, 12]])

print("1D array:")
print(arr1d)
print()
print("2D array:")
print(arr2d)
print()

combined_row = np.concatenate((arr1d.reshape(1, -1), arr2d), axis=0)
print("Combined by converting 1D array into a row and stacking it with the 2D array:")
print(combined_row)