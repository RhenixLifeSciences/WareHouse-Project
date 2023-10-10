import boto3
import json
from boto3.dynamodb.conditions import Key

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('WH_Products')

def lambda_handler(event, context):
    response_messages = []
    for item in event:
         table.put_item(Item=item)
    print(item)
    return {
        'statusCode': 200,
        'body': "Item added successfully"
    }

