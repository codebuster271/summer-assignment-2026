import pandas as pd


dates = ["2024-01-05", "2025-07-14", "2026-06-09", "2026-12-31"]
series = pd.to_datetime(pd.Series(dates))

print("Original datetime series:")
print(series)
print()
print("Year:")
print(series.dt.year.tolist())
print("Month:")
print(series.dt.month.tolist())
print("Day:")
print(series.dt.day.tolist())
print("Day name:")
print(series.dt.day_name().tolist())
print()

print("Date range:")
print(pd.date_range(start="2026-01-01", periods=5, freq="7D"))
print()

print("Timedelta example:")
print(pd.Timestamp("2026-06-09") + pd.Timedelta(days=10))
print()

print("Period index by month:")
print(pd.PeriodIndex(series, freq="M"))
print()

print("Normalize, floor, and ceil examples:")
dt_series = pd.to_datetime(pd.Series(["2026-06-09 10:15:30", "2026-06-09 22:45:10"]))
print("normalize:")
print(dt_series.dt.normalize())
print("floor to hour:")
print(dt_series.dt.floor("h"))
print("ceil to hour:")
print(dt_series.dt.ceil("h"))
print()

print("Resample example:")
sample = pd.DataFrame(
    {"date": pd.date_range("2026-01-01", periods=6, freq="D"), "sales": [10, 15, 13, 18, 21, 25]}
).set_index("date")
print(sample.resample("3D").sum())