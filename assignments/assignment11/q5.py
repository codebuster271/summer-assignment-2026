import numpy as np


array_3d = np.array(
    [
        [[1, 2], [3, 4]],
        [[5, 6], [7, 8]],
    ]
)

print("3D array:")
print(array_3d)
print()

print("Iterating using nested for loops:")
for matrix in array_3d:
    for row in matrix:
        for value in row:
            print(value, end=" ")
    print()
print()

print("Iterating using nditer:")
for value in np.nditer(array_3d):
    print(int(value), end=" ")