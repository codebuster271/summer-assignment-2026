from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("PartitioningAssignment") \
    .master("local[*]") \
    .getOrCreate()

df = spark.range(0, 5000000)

print(f"Initial number of partitions: {df.rdd.getNumPartitions()}")

df_repartitioned = df.repartition(12)
print(f"Number of partitions after repartition(): {df_repartitioned.rdd.getNumPartitions()}")

df_coalesced = df_repartitioned.coalesce(3)
print(f"Number of partitions after coalesce(): {df_coalesced.rdd.getNumPartitions()}")

spark.stop()