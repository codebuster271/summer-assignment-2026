import numpy as np
from collections import Counter


arr1 = np.array([3, 4])
arr2 = np.array([1, 0])

avg = (arr1 + arr2) / 2
print("Average of NumPy arrays:")
print(avg)
print()

first_2d = np.array([[1, 2, 3], [4, 5, 6]])
second_2d = np.array([[6, 5, 4], [3, 2, 1]])

combined = np.concatenate((first_2d.ravel(), second_2d.ravel()))

print("First 2D array:")
print(first_2d)
print()
print("Second 2D array:")
print(second_2d)
print()
print("Mean of both 2D arrays combined:", np.mean(combined))
print("Median of both 2D arrays combined:", np.median(combined))
print("Mode of both 2D arrays combined:", Counter(combined).most_common(1)[0][0])