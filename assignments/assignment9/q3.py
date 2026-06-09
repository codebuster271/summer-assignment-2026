import pandas as pd


file_path = r"d:\college-internship\internship-college-2nd-year-end\customers-100.csv"
df = pd.read_csv(file_path)

df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

text_columns = ["first_name", "last_name", "company", "city", "country", "email", "website"]
for column in text_columns:
    df[column] = df[column].astype(str).str.strip()

df["subscription_date"] = pd.to_datetime(df["subscription_date"], errors="coerce")
df["subscription_year"] = df["subscription_date"].dt.year
df["subscription_month"] = df["subscription_date"].dt.to_period("M")
df["full_name"] = df["first_name"] + " " + df["last_name"]
df["email_domain"] = df["email"].str.split("@").str[-1]
df["phone_1"] = df["phone_1"].str.replace(r"[^0-9+]", "", regex=True)

df_clean = df.drop_duplicates(subset=["customer_id"]).copy()

print("Dataset shape:", df_clean.shape)
print()
print("Missing values:")
print(df_clean.isna().sum())
print()

print("Top 5 countries by customer count:")
print(df_clean["country"].value_counts().head())
print()

print("Top 5 cities by customer count:")
print(df_clean["city"].value_counts().head())
print()

print("Customers added by year:")
print(df_clean["subscription_year"].value_counts().sort_index())
print()

print("Customers added by month:")
print(df_clean["subscription_month"].value_counts().sort_index().tail(10))
print()

print("Most common email domains:")
print(df_clean["email_domain"].value_counts().head())
print()

print("Sample cleaned rows:")
print(df_clean[["customer_id", "full_name", "city", "country", "subscription_date", "email_domain"]].head())