import boto3
import json

def lambda_handler(event, context):
    TableName = "WH_Trip"
    Primary_Column_Name = 'Trip_id'

    client = boto3.client('dynamodb')
    DB = boto3.resource('dynamodb')

    table = DB.Table(TableName)

    result = []

    # Iterate through the Consumer_id objects in the event
    for Trip_record in event:
        Tripid = Trip_record['Trip_id']
        
        response = table.get_item(
            Key={
                Primary_Column_Name: Tripid
            }
        )
        
        item = response.get("Item")
        result.append(item)  # Append the retrieved item to the result list

    return result
