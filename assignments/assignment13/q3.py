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
filled = array_with_nan.copy()
nan_rows, nan_cols = np.where(np.isnan(filled))

for row_index, col_index in zip(nan_rows, nan_cols):
    filled[row_index, col_index] = column_means[col_index]

print("NaN replaced with column averages:")
print(filled)