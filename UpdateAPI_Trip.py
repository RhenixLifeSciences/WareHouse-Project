import boto3
import json
from boto3.dynamodb.conditions import Key

def lambda_handler(event, context):
    dynamodb=boto3.resource('dynamodb')
    table=dynamodb.Table('WH_Trip')
    for update_Trip in event:

        print(update_Trip)
        table.put_item(Item=update_Trip)
    return {
            'statusCode': 200,
            'body': "item Updated successfully"
}