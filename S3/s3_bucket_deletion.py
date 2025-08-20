import boto3

#Create S3 client

s3_client = boto3.client('s3')
s3_resource=boto3.resource('s3')


def delete_bucket_with_objects(region=None):
        #List all bucket
        response=s3_client.list_buckets()
        buckets=response["Buckets"]

        for bucket in buckets:
            bucket_name=bucket['Name']
            print(f"Checking bucket {bucket_name}")

            #Creating one resource for fetching bucket data
            b=s3_resource.Bucket(bucket_name)

            #Check if bucket has object
            objects=list(b.objects.all())

            if objects:
                print(f"Found {len(objects)} objects, deleting them...{objects['Name']}")

                #Delete all objects in bucket
                b.objects.all().delete()
                print("Objects deleted successfully ")
            
            try:
                b.delete()  #b variable contains bucket name of current iteration
                print(f"Bucket {bucket_name} deleted successfully")
            except Exception as ee:
                 print(f"Unable to delete bucket '{bucket_name}' : {ee}")

#Calling function
delete_bucket_with_objects()

    


