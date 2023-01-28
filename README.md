# aws-cloudwatch-dashboards-creation

This script creates a CloudWatch dashboards for monitoring various metrics of AWS services.

## Prerequisites

* AWS account with access to CloudWatch and respective AWS service for which you are creating dashboard
* AWS CLI configured with credentials for the above account

## Usage

1. Create the environment variables `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY` and `REGION` with your AWS credentials and desired region.
    - Windows:
    ```
    setx AWS_ACCESS_KEY_ID <your_access_key_id>
    setx AWS_SECRET_ACCESS_KEY <your_secret_access_key>
    setx REGION <your_region>
    ```
    - Linux/Mac:
    ```
    export AWS_ACCESS_KEY_ID=<your_access_key_id>
    export AWS_SECRET_ACCESS_KEY=<your_secret_access_key>
    export REGION=<your_region>
    ```

2. Run the script:
    ```
    python scriptname.py
    ```

3. The dashboard should now be available in the CloudWatch console.