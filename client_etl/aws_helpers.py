import pandas as pd
from constants import RDS_ENDPOINT, RDS_PORT, RDS_USERNAME, RDS_PASSWORD, JDBC_URL
import boto3


def s3_read_to_spark(url, spark):
    df = pd.read_csv(url)  # seemed simpler to read s3 into pandas then spark
    df = spark.createDataFrame(df)
    return df

jdbc_properties = {'user': RDS_USERNAME, 'password': RDS_PASSWORD, 'driver': 'org.postgresql.Driver'}

def spark_write_to_rds(spark_df, table_name, append_mode=False):
    if append_mode:
        spark_df.write.mode('append').jdbc(url=JDBC_URL, table=table_name, properties=jdbc_properties)
    else:
        spark_df.write.jdbc(url=JDBC_URL, table=table_name, properties=jdbc_properties)

def spark_read_from_rds(spark, table_name):
    df = spark.read.jdbc(url=JDBC_URL, table=table_name, properties=jdbc_properties)
    return df


# untested
def write_file_to_s3(local_file, bucket_name, remote_path):
    s3 = boto3.resource('s3')
    # obj = s3.Object(bucket_name, remote_path)
    # obj.put(Body=open(local_file, 'r'))
    s3.Bucket(bucket_name).upload_file(local_file, remote_path)
    # could use .upload_fileobj()   for 'in-memory files'

