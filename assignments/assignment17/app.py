import os
import glob
from pyspark.sql import SparkSession
from pyspark.sql.functions import col

spark = SparkSession.builder \
    .appName("SalesDataProcessing") \
    .master("local[*]") \
    .getOrCreate()

df = spark.read.csv("sales.csv", header=True, inferSchema=True)

print("--- Original DataFrame Schema ---")
df.printSchema()

print("--- All Products Sorted by Sales (Descending) ---")
sorted_df = df.orderBy(col("sales").desc())
sorted_df.show()

print("--- Top 3 Highest Selling Products ---")
top_3_products = sorted_df.limit(3)
top_3_products.show()

print("--- Filtering Products with Sales > 80,000 ---")
filtered_df = df.filter(col("sales") > 80000)
filtered_df.show()

temp_dir = "temp_output"
filtered_df.coalesce(1).write.mode("overwrite").csv(temp_dir, header=True)

try:
    csv_file = glob.glob(f"{temp_dir}/part-*.csv")[0]
    os.rename(csv_file, "high_sales_output.csv")
    print("--- Successfully saved clean output to 'high_sales_output.csv' ---")
except IndexError:
    print("Error: Spark output file not found.")

spark.stop()