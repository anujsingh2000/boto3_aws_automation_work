# import boto3

# #Create S3 client
# s3_client=boto3.client('s3')

# #list of bucket
# buckets=s3_client.list_buckets()['Buckets']

# if not buckets:
#     print("No available bucket in aws account")
# else:
#     #Check for first available bucket in aws account
#     bucket_name=buckets[0]['Name']
#     print(f"Using {bucket_name} for file uploading")
#     file_name=r'C:\Users\Anuj Rathore\Desktop\Me\my_app.log' #Replace filename or path with actual file
#     object_name = "uploaded_test.txt"

#     try:
#         s3_client.upload_file(file_name,bucket_name, object_name)
#         print(f"{file_name} uploaded to {bucket_name} as {object_name}")
#     except Exception as ee:
#         print("Getting error while uplaoding file ", ee)


##_________________________________________________________________________________

# #S3 object download

# import boto3

# s3_client=boto3.client('s3')

# #Params
# bucket_name='my-boto3-demo-bucket-2025-72511'
# object='list_ec2.py'
# download_path='C:\\Users\\Anuj Rathore\\Desktop\\Me\\downloaded_my_app.txt'


# response=s3_client.list_objects(Bucket=bucket_name)
# for obj in response.get('Contents', []):
#     print(obj['Key'])

# def object_downlaod(bucket_name,object_key,download_path):
#     s3_client.download_file(bucket_name,object_key,download_path)
#     print(f"Object {object_key} downloaded successfully from {bucket_name} bucket.")


# object_downlaod(bucket_name,object,download_path)

##_________________________________________________________________________________________

##List Object in a S3 Bucket 

# import boto3

# s3_client=boto3.client('s3')

# bucket_name='my-boto3-demo-bucket-2025-72511'

# response=s3_client.list_objects(Bucket=bucket_name)
# for objects in response.get('Contents',[]):
#     print(objects['Key'])

##_____________________________________________________

## Delete object from S3 bucket

# import boto3
# s3_client=boto3.client('s3')

# bucket_name='my-boto3-demo-bucket-2025-72511'
# object_key='list_ec2.py'

# response=s3_client.delete_object(Bucket=bucket_name,Key=object_key)
# print(f"Deleted {object_key}")

##____________________________________________________________________

## Upload object with metadata

# import boto3

# s3_client = boto3.client('s3')

# bucket_name ='my-boto3-demo-bucket-2025-72511'
# object_key = 'config.txt'
# file_path = 'C:\\Users\\Anuj Rathore\\Desktop\\Me\\data.json'  # Local file

# # Upload with metadata
# s3_client.upload_file(
#     Filename=file_path,
#     Bucket=bucket_name,
#     Key=object_key,
#     ExtraArgs={"Metadata": {"project": "healthcheck", "env": "dev"}}
# )
# print("Uploaded with metadata!")