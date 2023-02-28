import boto3

#Retrieve the sqs client
sqs = boto3.client('sqs', region_name = 'us-east-1')

#Create the queue
my_queue = sqs.create_queue(QueueName='SQS_Week15_Project')
#print queue definition results
print(my_queue)
