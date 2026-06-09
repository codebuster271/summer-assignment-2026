import pandas as pd


date_strings = ["2026-01-01", "2026-01-05", "2026-01-10", "2026-01-15"]
series = pd.Series(pd.to_datetime(date_strings))
series = series.sort_values().reset_index(drop=True)

print("Datetime Series:")
print(series)
print()
print("Timeseries with datetime index:")
timeseries = pd.Series([100, 120, 140, 160], index=series)
print(timeseries)