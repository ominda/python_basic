import boto3
import os

ec2 = boto3.client('ec2', 
                   aws_access_key_id=os.environ['AWS_ACCESS_KEY_ID'],
                   aws_secret_access_key=os.environ['AWS_SECRET_ACCESS_KEY'],
                   aws_session_token=os.environ['AWS_SESSION_TOKEN'])
response = ec2.describe_instances()
stopped_instances = []
running_instances = []
# print(type(response), response)
# for i in range(len(response['Reservations'])):
# print(len((response['Reservations'][0]['Instances'][0])))
# print((response['Reservations'][0]['Instances'][0]['KeyName']))
for item in range(len(response['Reservations'])):
    for instance in response['Reservations'][item]['Instances']:
        if instance.get('State')['Name'] == "running":
            running_instances.append(instance.get('InstanceId'))
        elif instance.get('State')['Name'] == "stopped":
            stopped_instances.append(instance.get('InstanceId'))
        # print(instance.get('KeyName') , " -> " , instance.get('InstanceId'))

print("Running instances : ", running_instances)
print("Stopped instances : ", stopped_instances)
    