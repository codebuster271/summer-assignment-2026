import pandas as pd


series = pd.Series([100, 200, 300, 400], index=["a", "b", "c", "d"])

print(series["b"])
print(series.iloc[2])