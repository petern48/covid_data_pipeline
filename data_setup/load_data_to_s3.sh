#!/bin/bash

aws s3 cp data/covid/epidemiology.csv s3://covid-pipeline-raw-us-west-1-dev/covid/
aws s3 cp data/covid/hospitalizations.csv s3://covid-pipeline-raw-us-west-1-dev/covid/
### aws s3 cp data/covid/weather.csv s3://covid-pipeline-raw-us-west-1-dev/covid/

aws s3 cp data/NASDAQ-historial.csv s3://covid-pipeline-raw-us-west-1-dev/stocks/
aws s3 cp data/SP500-historical.csv s3://covid-pipeline-raw-us-west-1-dev/stocks/
### included aws s3 cp data/stocks s3://covid-pipeline-raw-us-west-1-dev/stocks/
