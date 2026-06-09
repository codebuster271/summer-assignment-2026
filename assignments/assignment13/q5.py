"""Assignment 13 - Question 5."""

import numpy as np
from collections import Counter


def describe_array(name, array):
	print(f"{name}:")
	print(array)
	print()


def main():
	arr1 = np.array([3, 4])
	arr2 = np.array([1, 0])
	avg = (arr1 + arr2) / 2

	first_2d = np.array([[1, 2, 3], [4, 5, 6]])
	second_2d = np.array([[6, 5, 4], [3, 2, 1]])
	combined = np.concatenate((first_2d.ravel(), second_2d.ravel()))

	print("Element-wise average of two 1D arrays:")
	print(avg)
	print()

	describe_array("First 2D array", first_2d)
	describe_array("Second 2D array", second_2d)

	print("Statistics for both 2D arrays combined:")
	print("Mean:", np.mean(combined))
	print("Median:", np.median(combined))
	print("Mode:", Counter(combined).most_common(1)[0][0])


if __name__ == "__main__":
	main()