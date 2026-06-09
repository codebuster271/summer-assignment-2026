import numpy as np
from collections import Counter


array1 = np.array([[1, 2, 3], [4, 5, 6]])
array2 = np.array([[6, 5, 4], [3, 2, 1]])

print("Array 1:")
print(array1)
print()
print("Array 2:")
print(array2)
print()

average_array = (array1 + array2) / 2
print("Element-wise average of two NumPy 2D arrays:")
print(average_array)
print()

combined_values = np.concatenate((array1.ravel(), array2.ravel()))

mean_value = np.mean(combined_values)
median_value = np.median(combined_values)
mode_value = Counter(combined_values).most_common(1)[0][0]

print("Mean of both arrays combined:", mean_value)
print("Median of both arrays combined:", median_value)
print("Mode of both arrays combined:", mode_value)