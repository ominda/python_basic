import boto3
import os
s3 = boto3.client('s3', aws_access_key_id=os.environ['AWS_ACCESS_KEY_ID'],
                  aws_secret_access_key=os.environ['AWS_SECRET_ACCESS_KEY'],
                  aws_session_token=os.environ['AWS_SESSION_TOKEN'])

response = s3.list_buckets()
# print(response)
buckets = [bucket['Name'] for bucket in response['Buckets']]

print("Bucket List: %s" % buckets)