import numpy as np


array_with_nan = np.array(
    [
        [10, np.nan, 30],
        [20, 25, np.nan],
        [np.nan, 35, 45],
    ],
    dtype=float,
)

print("Original array:")
print(array_with_nan)
print()

column_means = np.nanmean(array_with_nan, axis=0)
row_indices, col_indices = np.where(np.isnan(array_with_nan))
array_filled = array_with_nan.copy()

for row_index, col_index in zip(row_indices, col_indices):
    array_filled[row_index, col_index] = column_means[col_index]

print("NaN replaced with column averages:")
print(array_filled)