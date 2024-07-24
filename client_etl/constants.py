import os
from dotenv import load_dotenv

load_dotenv("../.env")

DATA_DIR = "data"
COVID_ECONOMY_FILE = f"{DATA_DIR}/economy.csv"
COVID_WEATHER_FILE = f"{DATA_DIR}/weather.csv"


S3_BUCKET = os.getenv('S3_BUCKET')
COVID_EPIDEMIOLOGY_FILE = f"s3://{S3_BUCKET}/covid/epidemiology.csv"
COVID_HOSPITALIZATIONS_FILE = f"s3://{S3_BUCKET}/covid/hospitalizations.csv"
SP500_FILE = f"s3://{S3_BUCKET}/stocks/SP500-historical.csv"
NASDAQ_FILE = f"s3://{S3_BUCKET}/stocks/NASDAQ-historial.csv"

RDS_ENDPOINT = os.getenv('RDS_ENDPOINT')  # hostname
RDS_PORT = os.getenv('RDS_PORT')
RDS_USERNAME = os.getenv('RDS_USERNAME')
RDS_PASSWORD = os.getenv('RDS_PASSWORD')
RDS_DB_NAME = 'postgres'

JDBC_DRIVER = "../driver/postgresql-42.7.3.jar"
# https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/java-rds.html
JDBC_URL = f"jdbc:postgresql://{RDS_ENDPOINT}:{RDS_PORT}/{RDS_DB_NAME}?user={RDS_USERNAME}&password={RDS_PASSWORD}"  # endpoint = hostname

MONGO_URI = os.getenv('MONGO_URI')


START_DATE = "2018-01-01"
END_DATE = "2024-01-01"