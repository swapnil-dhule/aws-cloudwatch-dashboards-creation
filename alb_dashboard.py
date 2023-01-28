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
dashboard_name = 'ALBDashboard'
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
                    [ 'AWS/ApplicationELB', 'RequestCount', 'LoadBalancer', 'my-alb' ]
                ],
                'period': 300,
                'stat': 'Sum',
                'region': 'us-west-2',
                'title': 'ALB Request Count'
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
                    [ 'AWS/ApplicationELB', 'HTTPCode_Target_2XX_Count', 'LoadBalancer', 'my-alb' ]
                ],
                'period': 300,
                'stat': 'Sum',
                'region': 'us-west-2',
                'title': 'ALB 2XX Responses'
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
                    [ 'AWS/ApplicationELB', 'HTTPCode_Target_3XX_Count', 'LoadBalancer', 'my-alb' ]
                ],
                'period': 300,
                'stat': 'Sum',
                'region': 'us-west-2',
                'title': 'ALB 3XX Responses'
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
                    [ 'AWS/ApplicationELB', 'HTTPCode_Target_4XX_Count', 'LoadBalancer', 'my-alb' ]
                ],
                'period': 300,
                'stat': 'Sum',
                'region': 'us-west-2',
                'title': 'ALB 4XX Responses'
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
                    [ 'AWS/ApplicationELB', 'HTTPCode_Target_5XX_Count', 'LoadBalancer', 'my-alb' ]
                ],
                'period': 300,
                'stat': 'Sum',
                'region': 'us-west-2',
                'title': 'ALB 5XX Responses'
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
                    [ 'AWS/ApplicationELB', 'TargetResponseTime', 'LoadBalancer', 'my-alb' ]
                ],
                'period': 300,
                'stat': 'Average',
                'region': 'us-west-2',
                'title': 'ALB Target Response Time'
            }
        }

    ]
}

# Create the dashboard
response = cloudwatch.put_dashboard(DashboardName=dashboard_name, DashboardBody=json.dumps(dashboard_properties))

print(response)
