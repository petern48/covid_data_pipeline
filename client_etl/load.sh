#!/bin/bash

source ../.env

snapshot_name="covid-stock-db-snapshot"
iam_role="covid-pipeline"
# amazon resource names
source_arn="arn:aws:rds:$AWS_REGION:$AWS_ACCOUNT_ID:snapshot:$snapshot_name"
date=$(date -I)
export_name="covid-stock-db-export-$date"

echo "Creating snapshot of RDS database: $RDS_INSTANCE"
aws rds create-db-snapshot \
    --db-instance-identifier $RDS_INSTANCE \
    --db-snapshot-identifier $snapshot_name 

echo "Exporting snapshot of RDS to S3"
aws rds start-export-task \
    --export-task-identifier $export_name \
    --source-arn $source_arn \
    --s3-bucket-name $S3_BUCKET \
    --iam-role-arn $iam_role \

    # --kms-key-id my-key
#       # --source-arn arn:aws:rds:AWS_Region:123456789012:snapshot:snapshot-name \
#     # --iam-role-arn iam-role \
