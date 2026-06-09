import numpy as np


array_3d = np.arange(24).reshape(2, 3, 4)

print("Original 3D array:")
print(array_3d)
print()

print("Move axes from (0, 1, 2) to (2, 0, 1):")
print(np.moveaxis(array_3d, source=(0, 1, 2), destination=(2, 0, 1)))
print()

print("Swap axis 0 and axis 2:")
print(np.swapaxes(array_3d, 0, 2))