import numpy as np


array_2d = np.array([[6, -8, 73, -110], [np.nan, -8, 0, 94]], dtype=float)

print("Original array:")
print(array_2d)
print()

array_without_nan = np.nan_to_num(array_2d, nan=0)
print("NaN replaced with 0:")
print(array_without_nan)
print()

print("Interchanged rows and columns (transpose):")
print(array_without_nan.T)