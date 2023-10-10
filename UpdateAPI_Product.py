import boto3
import json
from boto3.dynamodb.conditions import Key

def lambda_handler(event, context):
    dynamodb=boto3.resource('dynamodb')
    table=dynamodb.Table('WH_Products')
    for update_product in event:

        print(update_product)
        table.put_item(Item=update_product)
    return {
            'statusCode': 200,
            'body': "item Updated successfully"
}
