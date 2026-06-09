"""Assignment 13 - Question 4."""

import numpy as np


def main():
    array = np.array([[23, -56, 78, -93], [71, -82, 13, 24]])
    cleaned = np.where(array < 0, 0, array)

    print("Original array:")
    print(array)
    print()
    print("Negative values replaced with 0:")
    print(cleaned)


if __name__ == "__main__":
    main()