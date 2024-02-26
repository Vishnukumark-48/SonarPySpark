from pyspark.sql import SparkSession

# Create a SparkSession
spark = SparkSession.builder \
    .appName("DiabetesAnalysis") \
    .getOrCreate()

# Read CSV file into a DataFrame
url = 'https://raw.githubusercontent.com/Vishnukumark-48/SonarPySpark/main/flavors_of_cocoa.csv'
df = spark.read.csv(url, header=True, inferSchema=True)

# Perform some basic operations
df.show()

# Stop the SparkSession
spark.stop()
