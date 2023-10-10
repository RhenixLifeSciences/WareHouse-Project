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
    if delivery_status == "order_confirmation":
        message = "Thank you for your order! Your shipment is on its way."
    elif delivery_status == "out_for_delivery":
        message = "Your shipment is out for delivery. It will arrive soon."
    elif delivery_status == "delayed":
        message = "Your shipment is delayed. We apologize for the inconvenience."
    elif delivery_status == "delivered":
        message = "Your shipment has been successfully delivered. Enjoy your products!"
    elif delivery_status == "in_transit":
        message = "Your shipment is currently in transit to its destination."
    elif delivery_status == "return_requested":
        message = "A return request has been initiated for your shipment."
    elif delivery_status == "on_hold":
        message = "Your shipment is currently on hold. Please contact customer support for assistance."
    elif delivery_status == "canceled":
        message = "Your shipment has been canceled. If you have any questions, please contact us."
        
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