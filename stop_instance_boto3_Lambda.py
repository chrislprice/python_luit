import boto3
ec2 = boto3.resource('ec2')

def lambda_handler(event,context):
    instances = ec2.instances.filter(Filters=[{'Name:': 'tag:Environment','Values': ['Dev']},{'Name': 'instance-state-name', 'Values': ['running']}])
    #print(instances)

    for instance in instances:
        instance_id = instance.id
       # print("Stopping Instance:", instance.id)
        ec2.instances.filter(InstanceIds=instance_id).stop()
        #instance.stop()
        #ec2.instances(instance_id).stop()
    
    return "completed!"