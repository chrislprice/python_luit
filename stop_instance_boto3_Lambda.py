import boto3
ec2 = boto3.resource('ec2')

def lambda_handler():
    instances2=ec2.instances.all()
    results=[]
    instances = ec2.instances.filter(Filters=[{'Name':'tag:Environment','Values':['Dev']}])#,{'Name': 'instance-state-name', 'Values': ['running']}])
   # print(instances)
   # print(instances2)

    for instance in instances:
        #results.append(instance)
       # print(instance.id)
     #   instance_id = instance.id
       # print("Stopping Instance:", instance.id)
      #  ec2.instances.filter(InstanceIds=instance_id).stop()
         instance.stop()
        #instance.stop()
        #ec2.instances(instance_id).stop()
    
    return results
    
print(lambda_handler())


