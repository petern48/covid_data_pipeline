from pyspark import SparkContext, SparkConf
from pyspark.sql import SparkSession
from constants import JDBC_DRIVER, MONGO_URI

def get_spark_session_and_context():
    # Creating a spark session
    conf = SparkConf()  # create the configuration
    conf.set("spark.jars", JDBC_DRIVER)  # set the spark.jars
    conf.set('spark.executor.memory', '5gb')  # 2 Gb instead of 1
    conf.set("spark.mongodb.read.connection.uri", MONGO_URI)  #"mongodb://127.0.0.1/test.coll")
    conf.set("spark.mongodb.write.connection.uri", MONGO_URI)  #"mongodb://127.0.0.1/test.coll")

    spark = SparkSession.builder.appName('pySparkSetup')\
        .config(conf=conf)\
        .getOrCreate()

    sc = spark.sparkContext

    return spark, sc