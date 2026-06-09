"""Assignment 13 - Question 1."""

import numpy as np


def print_section(title, value):
	print(f"{title}:")
	print(value)
	print()


def main():
	array_2d = np.array([[6, -8, 73, -110], [np.nan, -8, 0, 94]], dtype=float)

	print_section("Original array", array_2d)

	array_without_nan = np.nan_to_num(array_2d, nan=0)
	print_section("NaN replaced with 0", array_without_nan)
	print_section("Transpose of the cleaned array", array_without_nan.T)


if __name__ == "__main__":
	main()