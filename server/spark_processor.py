from pyspark.sql import SparkSession
from pyspark.sql.functions import col, lower

spark = SparkSession.builder \
    .appName("CrimeDataQuery") \
    .getOrCreate()

def query_crime_data(city=None, crime_code=None, crime_type=None):

    df = spark.read.csv("../data/crimes.csv", header=True, inferSchema=True)
    
    if city:
        df = df.filter(lower(col("City")).like(f"%{city.lower()}%"))
    if crime_code:
        try:
            df = df.filter(col("Crime Code") == int(crime_code))
        except ValueError:
            pass
    if crime_type:
        df = df.filter(lower(col("Crime Description")).like(f"%{crime_type.lower()}%"))


    return df.limit(10).toPandas()
