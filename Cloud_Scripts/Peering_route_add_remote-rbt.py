import boto3
import json
import urllib3

http = urllib3.PoolManager()

def lambda_handler(event, context):
    """
    Adds a route to a specified route table.

    Parameters
    ----------
    event: dict
        A dictionary containing the route table ID, destination CIDR block, and target.
    context: object
        Lambda context object.

    Returns
    -------
    dict
        A dictionary containing the response from the EC2 client.
    """
    try:
        # Get parameters from the event
        request_type = event['RequestType']
        route_table_id = event['ResourceProperties']['RouteTableId']
        destination_cidr_block = event['ResourceProperties']['DestinationCidrBlock']
        target_id = event['ResourceProperties']['TargetId']
        role_arn = event['ResourceProperties']['RoleArn']
        is_route_exists = False

        # Assume the role in Account DTE account
        sts_client = boto3.client('sts')
        assumed_role = sts_client.assume_role(
            RoleArn=role_arn,
            RoleSessionName="AssumeRoleSession"
        )
        
        # Get temporary credentials
        credentials = assumed_role['Credentials']


        ec2 = boto3.client('ec2', 
                        aws_access_key_id=credentials['AccessKeyId'],
                        aws_secret_access_key=credentials['SecretAccessKey'],
                        aws_session_token=credentials['SessionToken']
                        )
        
        routes = ec2.describe_route_tables( RouteTableIds = [ route_table_id, ],)['RouteTables'][0]['Routes']
        for route in routes:
            if route.get('DestinationCidrBlock') == destination_cidr_block:
                is_route_exists = True

        if request_type == 'Create' or request_type == 'Update':
            if is_route_exists:
                print(f"This Route already exists:  {route_table_id} ->  {destination_cidr_block}")
                send_response(event, context, "SUCCESS", {"Message": "Route already exists"})
            else:
                response = ec2.create_route(
                    RouteTableId=route_table_id,
                    DestinationCidrBlock=destination_cidr_block,
                    GatewayId=target_id,
                )
                print(f"Successfully created/updated route: {response}")
                send_response(event, context, "SUCCESS", {"Message": "Route created successfully"})
        elif request_type == 'Delete':
            if is_route_exists:
                # Delete the route
                response = ec2.delete_route(
                    RouteTableId=route_table_id,
                    DestinationCidrBlock=destination_cidr_block
                )
                print(f"Successfully deleted route: {response}")
                send_response(event, context, "SUCCESS", {"Message": "Route deleted successfully"})
            else:
                print(f"Route Not available: {response}")
                send_response(event, context, "SUCCESS", {"Message": "Route not available"})

    except Exception as e:
        print(f"Error processing request: {str(e)}")
        # Send failure response back to CloudFormation
        send_response(event, context, "FAILED", {"Message": str(e)})

def send_response(event, context, response_status, response_data, physical_resource_id=None, no_echo=False):
    response_url = event['ResponseURL']

    response_body = {
        'Status': response_status,
        'Reason': f'See the details in CloudWatch Log Stream: {context.log_stream_name}',
        'PhysicalResourceId': physical_resource_id or context.log_stream_name,
        'StackId': event['StackId'],
        'RequestId': event['RequestId'],
        'LogicalResourceId': event['LogicalResourceId'],
        'NoEcho': no_echo,
        'Data': response_data
    }

    json_response_body = json.dumps(response_body)

    headers = {
        'content-type': '',
        'content-length': str(len(json_response_body))
    }

    try:
        response = http.request('PUT', response_url, body=json_response_body, headers=headers)
        print(f"Response status: {response.status}")
    except Exception as e:
        print(f"send_response failed: {str(e)}")
