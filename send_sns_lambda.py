import json
import boto3


def lambda_handler(event, context):
    sns=boto3.client('sns')
    #print(event)
    records = event["Records"]
    
    for record in records:
        key=record["body"]
        key_string=str(key)
        print(key_string)
        
    sns.publish(TopicArn="arn:aws:sns:us-east-1:725447884883:SQS_Alert", Message=key_string)

    return {
        'statusCode': 200,
        'body': json.dumps(key_string)
    }
