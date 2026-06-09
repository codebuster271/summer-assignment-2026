import pandas as pd


df1 = pd.DataFrame(
    {
        "ID": [1, 2, 3, 4],
        "Name": ["Aman", "Priya", "Rahul", "Sneha"],
        "City": ["Jaipur", "Bhopal", "Indore", "Delhi"],
    }
)

df2 = pd.DataFrame(
    {
        "ID": [2, 3, 4, 5],
        "Department": ["HR", "IT", "Sales", "Finance"],
        "Salary": [30000, 45000, 40000, 38000],
    }
)

print("Inner merge on ID:")
inner_result = pd.merge(df1, df2, on="ID", how="inner")
print(inner_result)
print()

print("Left join on ID:")
left_result = pd.merge(df1, df2, on="ID", how="left")
print(left_result)
print()
print("Missing values in left join appear as NaN for rows in df1 that do not have a matching ID in df2.")
print()

print("Right join on ID:")
right_result = pd.merge(df1, df2, on="ID", how="right")
print(right_result)
print()

print("Index-based join using df.join():")
df1_indexed = df1.set_index("ID")
df2_indexed = df2.set_index("ID")
index_join_result = df1_indexed.join(df2_indexed, how="inner")
print(index_join_result)
print()
print("Comparison:")
print("- merge() matches on a column key and can do inner, left, right, outer joins directly.")
print("- join() is index-based by default, so both DataFrames were first aligned by ID as the index.")