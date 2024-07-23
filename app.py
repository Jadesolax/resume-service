import json
import boto3
from botocore.exceptions import ClientError
import os

def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(os.environ['TABLE_NAME'])
    
    try:
        response = table.scan()
        data = response.get('Items', [])
        return {
            'statusCode': 200,
            'body': json.dumps(data)
        }
    except ClientError as e:
        return {
            'statusCode': 500,
            'body': json.dumps(e.response['Error']['Message'])
        }
