import boto3
import json
import os

# Retrieve the AWS credentials from environment variables
aws_access_key_id = os.environ['AWS_ACCESS_KEY_ID']
aws_secret_access_key = os.environ['AWS_SECRET_ACCESS_KEY']
region_name = os.environ['REGION']

# Set mock AWS credentials
boto3.setup_default_session(aws_access_key_id=aws_access_key_id,
                            aws_secret_access_key=aws_secret_access_key)

# Connect to the CloudWatch service
cloudwatch = boto3.client('cloudwatch', region_name=region_name)

# Define the dashboard name and properties
dashboard_name = 'RDSDashboard'
dashboard_properties = {
    'widgets': [
        {
            'type': 'metric',
            'x': 0,
            'y': 0,
            'width': 12,
            'height': 6,
            'properties': {
                'metrics': [
                    [ 'AWS/RDS', 'CPUUtilization', 'DBInstanceIdentifier', 'my-rds-instance' ]
                ],
                'period': 300,
                'stat': 'Average',
                'region': region_name,
                'title': 'RDS CPU Utilization'
            }
        },
        {
            'type': 'metric',
            'x': 12,
            'y': 0,
            'width': 12,
            'height': 6,
            'properties': {
                'metrics': [
                    [ 'AWS/RDS', 'FreeStorageSpace', 'DBInstanceIdentifier', 'my-rds-instance' ]
                ],
                'period': 300,
                'stat': 'Average',
                'region': region_name,
                'title': 'RDS Free Storage Space'
            }
        },
        {
            'type': 'metric',
            'x': 0,
            'y': 6,
            'width': 12,
            'height': 6,
            'properties': {
                'metrics': [
                    [ 'AWS/RDS', 'ReadIOPS', 'DBInstanceIdentifier', 'my-rds-instance' ]
                ],
                'period': 300,
                'stat': 'Average',
                'region': region_name,
                'title': 'RDS Read IOPS'
            }
        },
        {
            'type': 'metric',
            'x': 12,
            'y': 6,
            'width': 12,
            'height': 6,
            'properties': {
                'metrics': [
                    [ 'AWS/RDS', 'WriteIOPS', 'DBInstanceIdentifier', 'my-rds-instance' ]
                ],
                'period': 300,
                'stat': 'Average',
                'region': region_name,
                'title': 'RDS Write IOPS'
            }
        },
        {
            'type': 'metric',
            'x': 0,
            'y': 12,
            'width': 12,
            'height': 6,
            'properties': {
                'metrics': [
                    [ 'AWS/RDS', 'ReadLatency', 'DBInstanceIdentifier', 'my-rds-instance' ]
                ],
                'period': 300,
                'stat': 'Average',
                'region': region_name,
                'title': 'RDS Read Latency'
            }
        },
        {
            'type': 'metric',
            'x': 12,
            'y': 12,
            'width': 12,
            'height': 6,
            'properties': {
                'metrics': [
                    [ 'AWS/RDS', 'WriteLatency', 'DBInstanceIdentifier', 'my-rds-instance' ]
                ],
                'period': 300,
                'stat': 'Average',
                'region': region_name,
                'title': 'RDS Write Latency'
            }
        }

    ]
}

# Create the dashboard
response = cloudwatch.put_dashboard(DashboardName=dashboard_name, DashboardBody=json.dumps(dashboard_properties))

print(response)
