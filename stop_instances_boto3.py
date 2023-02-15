import boto3

ec2 = boto3.client('ec2')


#ec2_filter=[{'Name': 'tag:Dev Team', 'Values': ['dev']}, {'Name': 'instance-state-name', 'Values': ['running']}]
instances = ec2.describe_instances(
    Filters=[
        {
            'Name': 'tag:Environment',
            'Values': ['Dev']
        },
    ]
)
print(instances)

for reservation in instances['Reservations']:
    for instance in reservation['Instances']:
        instance_id = instance["InstanceId"]
        ec2.stop_instances(InstanceIds=[instance['InstanceId']])
    
print(instance_id)

#https://lepczynski.it/en/aws_en/how-to-stop-all-ec2-in-all-aws-regions-at-the-same-time/