import boto3
import os

ec2 = boto3.client('ec2', 
                   aws_access_key_id=os.environ['AWS_ACCESS_KEY_ID'],
                   aws_secret_access_key=os.environ['AWS_SECRET_ACCESS_KEY'],
                   aws_session_token=os.environ['AWS_SESSION_TOKEN'])
response = ec2.describe_instances()
instance_ids = []
for reservation in response['Reservations']:
    for instance in reservation['Instances']:
        if instance['State']['Name'] == 'running':
            instance_ids.append(instance['InstanceId'])

print(f"Running Instances : {instance_ids}")

#########################################################
# # Write a program to list all the EC2 instances in the AWS account.
# import boto3, os
# session = boto3.Session(region_name='ap-southeast-1',
#                    aws_access_key_id=os.environ['AWS_ACCESS_KEY_ID'],
#                    aws_secret_access_key=os.environ['AWS_SECRET_ACCESS_KEY'],
#                    aws_session_token=os.environ['AWS_SESSION_TOKEN'])

# ec2 = session.resource('ec2')

# def list_instance_ids():
#     instances = ec2.instances.all()
#     instance_ids = []
#     for instance in instances:
#         instance_ids.append(instance.id)
#     return instance_ids

# if __name__ == '__main__':
#     instance_ids = list_instance_ids()
#     print(f"EC2 instances in the account: {instance_ids}")

###########################################################