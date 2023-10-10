import boto3
import json

def lambda_handler(event, context):
    TableName ="WH_Products"
    Primary_Column_Name = 'Product_id'

    client = boto3.client('dynamodb')
    DB = boto3.resource('dynamodb') 

    table = DB.Table(TableName)
    
    result = []

    # Iterate through the Consumer_id objects in the event
    for Product_record in event:   
        Productid = Product_record['Product_id']
    
        response = table.get_item(
            Key={
                 Primary_Column_Name: Productid
                }
        )
     
        item = response.get("Item")
        result.append(item) 
        
    return result