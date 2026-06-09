import pandas as pd


data = [[1, "Aman"], [2, "Priya"], [3, "Rahul"]]
df = pd.DataFrame(data, columns=["Id", "Name"])

print(df)