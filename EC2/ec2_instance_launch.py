
# Script for launching an ec2 instance

import boto3

ec2_creation_object=boto3.resource('ec2')


#Launch an ec2 instance
ec2_instance=ec2_creation_object.create_instances(
    ImageId='ami-0d0ad8bb301edb745',
    MinCount=1,
    MaxCount=1,
    InstanceType='t2.micro',
    KeyName='ec2_key_pair',
    SecurityGroupIds=['sg-00e3df713930f0d01'],
    TagSpecifications=[
        {
            'ResourceType':'instance',
            'Tags':[{'Key':'Name','Value':'MyFirstServer'}]}
    ]
)

print("Launching ec2 instance... ")

#Adding waiter object to wait till instance get created

instance_id = ec2_instance[0].id

#Creating a client object to call waiter method
ec2_client=boto3.client('ec2')
waiter=ec2_client.get_waiter('instance_running')
waiter.wait(InstanceIds=[instance_id])

for instance in ec2_instance:
    print(f"Instance ID Created ",{instance.id})
