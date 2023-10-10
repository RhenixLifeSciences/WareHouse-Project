import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('WH_Products')

def lambda_handler(event, context):
    for product_record in event:
        # Extract the  Product id from the request payload
        Product_id = product_record['Product_id']

        # Delete the item from the table based on the Product id
        table.delete_item(
            Key={
                'Product_id': Product_id
                }
        )

    return {
        'statusCode': 200,
        'body': json.dumps('Item deleted successfully')
        }

		