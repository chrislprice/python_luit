import boto3
import os
import json
import datetime


# Lambda function
def lambda_handler(event, context):
    #retrieve sqs client service
    sqs = boto3.client('sqs', region_name = 'us-east-1') 
    #retrieves current time
    current_time = datetime.datetime.now() #https://docs.python.org/3/library/datetime.html#datetime.datetime.tzinfo
    #converts currrent_time to a string, https://www.programiz.com/python-programming/datetime/strftime
    current_time_string = current_time.strftime("%c")#("%m/%d/%Y, %H:%M:%S")
    #Send Message to queue
    sqs.send_message(QueueUrl = "https://sqs.us-east-1.amazonaws.com/725447884883/SQS_Week15_Project", MessageBody = current_time_string) 
    return {
        'statusCode': 200,
        'body': json.dumps(current_time_string)
    }