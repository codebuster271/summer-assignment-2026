import pandas as pd


df1 = pd.DataFrame(
    {
        "ID": [1, 2],
        "Name": ["Aman", "Priya"],
        "Score": [85, 92],
    }
)

df2 = pd.DataFrame(
    {
        "ID": [3, 4],
        "Name": ["Rahul", "Sneha"],
        "Score": [76, 88],
    }
)

df3 = pd.DataFrame(
    {
        "ID": [1, 2, 3, 4],
        "City": ["Jaipur", "Bhopal", "Indore", "Delhi"],
        "Grade": ["A", "A", "B", "A"],
    }
)

combined = pd.concat([df1, df2], ignore_index=True)
final_result = pd.merge(combined, df3, on="ID", how="inner")

print("First DataFrame:")
print(df1)
print()
print("Second DataFrame:")
print(df2)
print()
print("Third DataFrame:")
print(df3)
print()
print("Vertically concatenated DataFrame:")
print(combined)
print()
print("Merged with third DataFrame on ID:")
print(final_result)