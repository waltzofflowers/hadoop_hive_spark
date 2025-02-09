# -*- coding: utf-8 -*-
import os
from pyspark.sql import SparkSession

# Initialize Spark session
spark = SparkSession.builder.master("spark://spark-master:7077").appName("SaveToWindows").getOrCreate()

# Read CSV from HDFS
df = spark.read.option("header", "true").csv("hdfs://namenode:9000/user/hadoop/last_one3.csv")

# You can mess with the data using spark here.


# Save data to HDFS
hdfs_path = "hdfs://namenode:9000/user/hadoop/output1_csv"

# Write data to HDFS
df.write.mode("overwrite").option("header", "true").csv(hdfs_path)

# Force Spark to complete the write operation
df.count()  # Ensures Spark writes data before proceeding

spark.stop()
