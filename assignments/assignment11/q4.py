import numpy as np


array = np.array([[1, 2, 3], [4, 5, 6]])

print("Array:")
print(array)
print()

print("Maximum value:", np.max(array))
print("Minimum value:", np.min(array))
print("Rows:", array.shape[0])
print("Columns:", array.shape[1])
print()

print("Each element:")
for value in np.nditer(array):
    print(int(value), end=" ")
print()
print()

print("Specific element at row 1, column 2:", array[1, 2])
print()

total = 0
for row in array:
    for value in row:
        total += value
print("Sum of values using for loop:", total)
print()

array_a = np.array([1, 2, 3])
array_b = np.array([4, 5, 6])
print("Addition:", array_a + array_b)
print("Subtraction:", array_a - array_b)
print("Multiplication:", array_a * array_b)
print("Division:", array_b / array_a)