import pandas as pd


rows = [["Aman", 20, "Jaipur"], ["Priya", 21, "Bhopal"], ["Rahul", 22, "Indore"]]
df = pd.DataFrame(rows, columns=["Name", "Age", "City"])

print(df)