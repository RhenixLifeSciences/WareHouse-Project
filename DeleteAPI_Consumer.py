import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('WH_Consumers')

def lambda_handler(event, context):
    for consumer_record in event:
        # Extract the Consumer_id from the request payload
        Consumer_id =consumer_record['Consumer_id']

        # Delete the item from the table based on the Consumer_id
        table.delete_item(
            Key={
                 'Consumer_id': Consumer_id
            }
         )

    return {
        'statusCode': 200,
        'body': json.dumps('Item deleted successfully')
        }
		