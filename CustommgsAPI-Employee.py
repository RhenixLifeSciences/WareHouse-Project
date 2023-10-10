import logging
import boto3

# Initialize logger and set log level
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Initialize SNS client for the appropriate region
session = boto3.Session(region_name="ap-south-1")
sns_client = session.client('sns')

def lambda_handler(event, context):
    delivery_status = event.get("delivery_status", "unknown")
    if delivery_status == "Attempted_Delivery":
        message = "Initial delivery attempt unsuccessful. Kindly follow up as needed."
    elif delivery_status == "out_for_delivery":
        message = "You are currently in active delivery mode."
    elif delivery_status == "delayed":
        message = "Sometimes, delays happen. Your delivery is experiencing a slight delay due to unforeseen circumstances"
    elif delivery_status == "delivered":
        message = "Delivery successfully completed"
    elif delivery_status == "Rescheduled":
        message = "Delivery rescheduled for a more suitable time."
  
    elif delivery_status == "on_hold":
        message = "For now, your delivery is on pause. Await further instructions, and we'll have it back on track soon"
    elif delivery_status == "Returned_to_Sender":
        message = "The delivery has made its way back to us. Let's connect with support for a solution."
    elif delivery_status == "Pending_Confirmation":
        message = "We're in a holding pattern, awaiting the recipient's confirmation for this delivery."  
    elif delivery_status == "In_Transit":
        message = "You're on the move, ensuring a smooth transit for the delivery"  
    elif delivery_status == "Arrived_at_Destination":
        message = "You've reached the delivery destination. Exciting times ahead."
    elif delivery_status == "Warehouse_Processing":
        message = "At the moment, your delivery is going through some important processing at the warehouse."
    elif delivery_status == "Out_for_Pickup":
        message = "You're en route to pick up the delivery for its next adventure."   
        
    # Send the custom message
    response = sns_client.publish(
        PhoneNumber=event["countrycode"] + event["phone_number"],
        Message=message,
        MessageAttributes={
            'AWS.SNS.SMS.SenderID': {
                'DataType': 'String',
                'StringValue': 'SENDERID'
            },
            'AWS.SNS.SMS.SMSType': {
                'DataType': 'String',
                'StringValue': 'Transactional'
            }
        }
    )

    logger.info(response)

    return {
        'statusCode': 200,
        'body': 'Message sent successfully'
    }