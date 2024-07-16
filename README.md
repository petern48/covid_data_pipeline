# covid_data_pipeline

Here's the general outline of the project:
- Gather data sources
- Load the raw data files into cloud storage (AWS S3)
- Preprocess the data a tiny bit and load the data files into a structured relational database. (AWS RDS)
- Apply transformations to the data to clean and ensure data quality
- Using Airflow on AWS EC2, automate the process of Extracting, Transforming, and Loading (ETL) the data into a datawarehouse
- Visualize the trends between covid and stocks using Power Bi and the datawarehouse


Currently in development. Currently have 1-3 done and am wrapping up on 4:

<!-- Data Sources:

Google: https://health.google.com/covid-19/open-data/
- epidemiology.csv
- economy.csv
- weather.csv

stock data files from nasdaq

covid-19 and financial markets tweets dataset. https://data.mendeley.com/datasets/4cncz8dk9f/3
- jan 21, 2020 to june 9, 2020
- paper: https://www.sciencedirect.com/science/article/pii/S2352340922006254 -->

<!-- mobile device usage: https://github.com/aliannejadi/LSApp
- lsapp.tsv.gz -->

<!-- Youtube: https://www.youtube.com/watch?v=yZKJFKu49Dk
- for setting up AWS (CLI, etc) -->