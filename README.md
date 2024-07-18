# covid_data_pipeline

Here's the general outline of the project:
- Gather data sources from online
- Design the data model: both for database and datawarehouse (for efficient analytics)
- Load the raw data files into cloud storage (AWS S3)
- Preprocess the data a tiny bit and load the data files into a structured relational database. (AWS RDS)
- Using Airflow on an AWS EC2 instance, automate the process of Extracting, Transforming, and Loading (ETL) the data into a datawarehouse
    - Transformations are done to clean the data, improve the data quality, and restructure the tables for the DW for analytics
- Write unit tests to ensure the transformations act properly and ensure data quality 
- Visualize the trends between covid and stocks using Power Bi loaded with the data from the datawarehouse

README.md is currently in development, but it will soon be updated with further details and visuals, once I'm back from my short vacation.

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