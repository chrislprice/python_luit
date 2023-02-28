import boto3

client = boto3.client('sns') 

sns = client.create_topic(Name='SQS_Alert')