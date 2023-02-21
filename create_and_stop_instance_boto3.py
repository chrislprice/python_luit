import boto3
import time

ec2 = boto3.client('ec2')

instance = ec2.run_instances(
    ImageId='ami-0dfcb1ef8550277af',
    MinCount=1,
    MaxCount=1,
    InstanceType='t2.micro',
    TagSpecifications=[{'ResourceType': 'instance','Tags':[ {'Key': 'Environment','Value': 'Dev'}]}]
)
#print(instance)    

time.sleep(600)

instances = ec2.describe_instances(
    Filters=[
        {
            'Name': 'tag:Environment',
            'Values': ['Dev']
        },
        {'Name': 'instance-state-name', 'Values': ['running']}
        
    ]
)
#print(instances)

for reservation in instances['Reservations']:
    for instance in reservation['Instances']:
        instance_id = instance["InstanceId"]
        ec2.stop_instances(InstanceIds=[instance['InstanceId']])
    
print(instance_id)