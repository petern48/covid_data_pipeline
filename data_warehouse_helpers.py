from pyspark.sql import functions as F
from pyspark.sql.window import Window
import re

def special_char_remover(s):
    s = re.sub(r'\$', '', s)
    return re.sub(r'%', '', s)

special_char_udf = F.udf(lambda s: special_char_remover(s))


def create_company_dim_df(spark):
    nasdaq_companies_file = "data/stocks/nasdaq_companies.csv"
    df = spark.read.option('header', True).csv(nasdaq_companies_file)
    for column in df.columns:
        new_name = column.lower()
        new_name = re.sub(' ', '_', new_name)
        new_name = re.sub('%', 'percent', new_name)
        df = df.withColumnRenamed(column, new_name)

    df = df.withColumn('last_sale', special_char_udf('last_sale'))
    df = df.withColumn('percent_change', special_char_udf('percent_change'))
    # for col in ['last_sale', 'net_change', 'percent_change']:
        # df = df.withColumn(col, df[col].cast('float'))
    # df = df.withColumn('market_cap', df['market_cap'].cast('double'))
    df = df.withColumn('ipo_year', df['ipo_year'].cast('smallint'))
    df = df.withColumn('volume', df['volume'].cast('bigint'))

    # df.select('sector').distinct().show()  # visually inspect that all diff vals are actually diff

    df = df.drop('last_sale', 'net_change', 'percent_change', 'market_cap')

    w = Window.orderBy(df.symbol)
    df = df.withColumn('company_id', F.row_number().over(w))
    # reorder columns
    df = df.select('company_id', 'symbol', 'name', 'country', 'ipo_year', 'volume', 'sector', 'industry')
    return df



def create_date_dim_df(spark):
    date_df = spark.createDataFrame([(1,)], ["date_id"])
    date_df = date_df.withColumn('date',F.explode(F.expr("sequence(to_date('2018-01-01'), to_date('2023-12-31'), interval 1 day)"))) \
        
    w = Window.orderBy(date_df.date)
    date_df = date_df\
        .withColumn('date_id', F.row_number().over(w)) \
        .withColumn('date', date_df['date'].cast('date')) \
        .withColumn('day',F.date_format('date', 'd')) \
        .withColumn("day_name_abbr",F.date_format('date', 'EE')) \
        .withColumn("month",F.month("date")) \
        .withColumn("month_name_abbr",F.date_format('date', 'MMM')) \
        .withColumn("year",F.year("date")) \
        .withColumn("quarter",F.quarter("date"))
        # .withColumn("date_description",F.date_format('date', 'MMMM d, yyyy')) \
        # .withColumn('date',F.to_date('date_timestamp')) \
        # .withColumn("day_name",F.date_format('date_timestamp', 'EEEE')) \
        # .withColumn("day_2",F.date_format('date_timestamp', 'dd')) \
        # .withColumn("month_2",F.date_format('date_timestamp', 'MM')) \
        # .withColumn("month_name",F.date_format('date_timestamp', 'MMMM')) \
        # .withColumn("week_of_year",F.weekofyear("date_timestamp")) \
    return date_df