import boto3
import os
import random

aws_region = os.environ['AWS_REGION']
s3_client = boto3.client('s3',
                         aws_access_key_id=os.environ['AWS_ACCESS_KEY_ID'],
                         aws_secret_access_key=os.environ['AWS_SECRET_ACCESS_KEY'],
                         aws_session_token=os.environ['AWS_SESSION_TOKEN'],
                         region_name=aws_region)

def create_s3_bucket(name, region):
    s3_client.create_bucket(Bucket=name, 
                            CreateBucketConfiguration={'LocationConstraint': region},
                            ACL='private'
                            )
    print(f"Bucket {name} created successfully")
    return True

if __name__ == "__main__":
    bucket_name = "my-testing-bucket" + str(random.randint(1, 100000))
    create_s3_bucket(bucket_name, aws_region)
