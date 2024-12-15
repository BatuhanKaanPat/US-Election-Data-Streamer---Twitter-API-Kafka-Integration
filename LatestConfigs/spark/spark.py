from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import StructType, StructField, StringType, TimestampType
import os

# Kafka settings
kafka_topic = 'twitter_data'
kafka_servers = os.getenv('KAFKA_BOOTSTRAP_SERVERS', 'localhost:9092')

# MySQL settings
mysql_host = os.getenv('MYSQL_HOST', 'mysql')
mysql_port = os.getenv('MYSQL_PORT', '3306')
mysql_db = os.getenv('MYSQL_DATABASE', 'twitter_data')
mysql_user = os.getenv('MYSQL_USER', 'mysqluser')
mysql_password = os.getenv('MYSQL_PASSWORD', 'mysqlpassword')

# Spark session
spark = SparkSession.builder.appName("TwitterDataProcessing").getOrCreate()

# Define schema for incoming Kafka data
schema = StructType([
    StructField("text", StringType(), True),
    StructField("created_at", TimestampType(), True),
    StructField("user", StringType(), True)
])

# Read from Kafka
df = spark \
    .readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", kafka_servers) \
    .option("subscribe", kafka_topic) \
    .load()

# Convert value to String and parse JSON
df = df.selectExpr("CAST(value AS STRING) as json") \
    .select(from_json("json", schema).alias("data")) \
    .select("data.*")

# Write to MySQL
df.writeStream \
    .foreachBatch(lambda batch_df, batch_id: batch_df.write.format('jdbc')
                  .option('url', f'jdbc:mysql://{mysql_host}:{mysql_port}/{mysql_db}')
                  .option('user', mysql_user)
                  .option('password', mysql_password)
                  .option('dbtable', 'tweets')
                  .mode('append')
                  .save()) \
    .start() \
    .awaitTermination()