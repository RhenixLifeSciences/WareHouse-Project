import boto3
import json

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('WH_Trip')

def lambda_handler(event, context):
    response_messages = []
    for item in event:
        #try:
            table.put_item(Item=item)
            #response_messages.append(f"Item added successfully for payload: {item}")
        #except Exception as e:
            #response_messages.append(f"Failed to add item for payload: {item}, Error: {str(e)}")
            #print(f"Added item: {item}")
    
    return {
        'statusCode': 200,
        'body': 'Item added successfully'    #json.dumps(response_messages)
    }
