import boto3

ec2 = boto3.resource('ec2')

def lambda_handler(event,context):
    instances2 = ec2.instances
    instances = ec2.instances.filter(Filters=[{'Name:': 'Environment','Values': ['Dev']},{'Name': 'instance-state-name', 'Values': ['running']}])

    print(instances2)
    for instance in instances:
        instance_id = instance.id
        print("Stopping Instance: ", instance_id)
        ec2.instances('instance_id').stop()
    
    return "completed!"