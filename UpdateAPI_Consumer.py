import boto3
import json
from boto3.dynamodb.conditions import Key

def lambda_handler(event, context):
    dynamodb=boto3.resource('dynamodb')
    table=dynamodb.Table('WH_Consumers')
    for update_consumer in event:

        print(update_consumer)
        table.put_item(Item=update_consumer)
    return {
            'statusCode': 200,
            'body': "item Updated successfully"
}