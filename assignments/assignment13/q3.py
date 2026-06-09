"""Assignment 13 - Question 3."""

import numpy as np


def main():
    array_with_nan = np.array(
        [
            [10, np.nan, 30],
            [20, 25, np.nan],
            [np.nan, 35, 45],
        ],
        dtype=float,
    )

    column_means = np.nanmean(array_with_nan, axis=0)
    filled = np.where(np.isnan(array_with_nan), column_means, array_with_nan)

    print("Original array:")
    print(array_with_nan)
    print()
    print("Column means used for filling NaN values:")
    print(column_means)
    print()
    print("Array after filling NaN values with column averages:")
    print(filled)


if __name__ == "__main__":
    main()