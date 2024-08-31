import boto3
import kubernetes
from kubernetes.client.rest import ApiException
import os
import base64
from eks_token import get_token 
import json, yaml


def get_k8s_client(cluster_name, region, role_arn):
    # Retrieve cluster configurations
    eks_client = boto3.client('eks', region_name=region)
    cluster_description = eks_client.describe_cluster(name=cluster_name)
    cluster_endpoint = cluster_description['cluster']['endpoint']
    ca_cert = cluster_description['cluster']['certificateAuthority']['data']
    eks_token = get_token(cluster_name=cluster_name, role_arn=role_arn)['status']['token']

    with open('/tmp/certificate.crt', 'wb') as f:
        f.write(base64.b64decode(ca_cert))

    # Configure Kubernetes client
    configuration = kubernetes.client.Configuration()
    configuration.host = cluster_endpoint
    configuration.verify_ssl = True
    configuration.ssl_ca_cert = '/tmp/certificate.crt'
    configuration.api_key = {"authorization": "Bearer " + eks_token}
    api_client = kubernetes.client.ApiClient(configuration=configuration)
    core_v1 = kubernetes.client.CoreV1Api(api_client)
    
    return core_v1


def update_config_map(k8s_client, action, username, iam_role_arn, mapping_type):
    try:
        # Fetch the aws-auth ConfigMap
        config_map = k8s_client.read_namespaced_config_map('aws-auth', 'kube-system')

        data = config_map.data[mapping_type]

        # Convert YAML to Python dictionary
        map_roles = yaml.safe_load(data)
        
        if action == 'add':
            if username in data:
                return {
                    'statusCode': 400,
                    'body': json.dumps(f"User {username}, Already Exists!")
                }

            # Add user to aws-auth config map
            new_entry = {
                "rolearn": iam_role_arn,
                "username": username,
                "groups": ["system:masters"]
            }
            map_roles.append(new_entry)
        
        elif action == 'remove':
            # Remove user from aws-auth config map
            map_roles = [entry for entry in map_roles if entry['username'] != username]
        
        # Convert Python dictionary back to YAML
        config_map.data[mapping_type] = yaml.safe_dump(map_roles)
        
        # Update the ConfigMap
        k8s_client.patch_namespaced_config_map('aws-auth', 'kube-system', config_map)
        
        return {
            'statusCode': 200,
            'body': json.dumps(f"Successfully {action}ed user {username}.")
        }

    except ApiException as e:
        print(f"Exception when managing aws-auth ConfigMap: {e}")
        return {
            'statusCode': 500,
            'body': json.dumps(f"Error managing user: {e}")
        }
    

def lambda_handler(event, context):
    action = event.get('action')
    username = event.get('username')
    iam_role_arn = event.get('iam_role_arn')
    mapping_type = event.get('type')
    
    if action not in ['add', 'remove']:
        return {
            'statusCode': 400,
            'body': json.dumps('Invalid action. Must be "add" or "remove".')
        }
    
    if mapping_type not in ['mapRoles', 'mapUsers']:
        return {
            'statusCode': 400,
            'body': json.dumps('Invalid Type. Must be "mapRoles" or "mapUsers".')
        }
    
    # Get cluster configuration
    cluster_name = os.environ["CLUSTER_NAME"]
    region = os.environ["REGION"]
    # Assume role in remote account that allow lambda's execution role to assume. This role needs to be grant RBAC permission in K8s cluster
    role_arn = os.environ["CLUSTER_LAMBDA_ROLE"] 

    # Create K8s client
    k8s_client = get_k8s_client(cluster_name, region, role_arn)

    # Update ConfigMap
    return_status = update_config_map(k8s_client, action, username, iam_role_arn, mapping_type)

    print(return_status)
