import pandas as pd


rows = [(1, "Python"), (2, "Java"), (3, "C++")]
df = pd.DataFrame(rows, columns=["Id", "Language"])

print(df)