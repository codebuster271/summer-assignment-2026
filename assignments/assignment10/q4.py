import numpy as np


array_with_negatives = np.array([12, -4, 0, -18, 25, -1, 7])

print("Original array:")
print(array_with_negatives)
print()

replaced_array = np.where(array_with_negatives < 0, 0, array_with_negatives)
print("Negative values replaced with 0:")
print(replaced_array)