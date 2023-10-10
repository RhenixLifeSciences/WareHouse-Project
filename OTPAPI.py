import logging
import boto3
import random

# Initialize logger and set log level
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Initialize SNS client for Ireland region
session = boto3.Session(
    region_name="ap-south-1"
)
sns_client = session.client('sns')


def lambda_handler(event, context):
    min=1000;
    max=9999;
    otp=random.randint(min,max);
    print(otp);

    # Send message
    response = sns_client.publish(
        PhoneNumber=event["countrycode"]+event["phone_number"],
        Message="Your otp is " + str(otp),
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
        'body': otp
    }