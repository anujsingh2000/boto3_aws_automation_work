# Creating S3 bucket

import boto3
import time

s3_client = boto3.client('s3')

def create_S3_bucket(bucket_name,region=None):
    try:
        if region is None:
            response=s3_client.create_bucket(Bucket=bucket_name)
        else:
            response=s3_client.create_bucket(Bucket=bucket_name,CreateBucketConfiguration={'LocationConstraint': region}
        )
        print(f"Bucket {bucket_name} created successfully in region {region or 'us-east-1'}")
    
    except Exception as ee:
        print("Error occured: ",ee)

bucket_name=f"my-boto3-demo-bucket-2025-{int(time.strftime("%H%M%S"))}"
region='ap-south-1'
create_S3_bucket(bucket_name,region)

