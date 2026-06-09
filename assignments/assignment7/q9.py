import pandas as pd


df = pd.DataFrame(
    {"Name": ["Aman", "Priya", "Rahul"], "Age": [20, 21, 22], "City": ["Jaipur", "Bhopal", "Indore"]}
)

print(df.iterrows())
for index, row in df.iterrows():
    print(index, row["Name"], row["City"])

print()
for row in df.itertuples(index=False):
    print(row)

print()
for row in df.to_dict("records"):
    print(row)