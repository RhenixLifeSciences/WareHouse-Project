import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('WH_Trip')

def lambda_handler(event, context):
    for Trip_record in event:
        # Extract the Trip_id from the request payload
        Trip_id =Trip_record['Trip_id']

        # Delete the item from the table based on the Trip_id
        table.delete_item(
            Key={
                 'Trip_id': Trip_id
            }
         )

    return {
        'statusCode': 200,
        'body': json.dumps('Item deleted successfully')
        }
		

		