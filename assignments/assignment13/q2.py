"""Assignment 13 - Question 2."""

import numpy as np


def main():
	array_3d = np.arange(24).reshape(2, 3, 4)
	moved_axes = np.moveaxis(array_3d, source=(0, 1, 2), destination=(2, 0, 1))

	print("Original 3D array (shape: 2x3x4):")
	print(array_3d)
	print()
	print("Array after moving axes to (2, 0, 1):")
	print(moved_axes)


if __name__ == "__main__":
	main()