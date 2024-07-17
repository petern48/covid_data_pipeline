import pandas as pd
from constants import RDS_ENDPOINT, RDS_PORT, RDS_USERNAME, RDS_PASSWORD, JDBC_URL


def s3_read_to_spark(url, spark):
    df = pd.read_csv(url)  # seemed simpler to read s3 into pandas then spark
    df = spark.createDataFrame(df)
    return df


jdbc_properties = {'user': RDS_USERNAME, 'password': RDS_PASSWORD, 'driver': 'org.postgresql.Driver'}

def spark_write_to_rds(spark_df, table_name):
    spark_df.write.jdbc(url=JDBC_URL, table=table_name, properties=jdbc_properties)

def spark_read_from_rds(spark, table_name):
    df = spark.read.jdbc(url=JDBC_URL, table=table_name, properties=jdbc_properties)
    return df
