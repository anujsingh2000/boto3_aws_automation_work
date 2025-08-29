#   Creating AMI backup of instance

import boto3
import time
import sys

#Create client to access service
ec2_client = boto3.client('ec2')
instance_id=sys.argv[1]
AMI_NAME = f"Backup-{instance_id}-{int(time.time())}"

#Taking backup of instance
response=ec2_client.create_image(
    InstanceId=instance_id,
    Description= f"AMI backup of instance {instance_id} ",
    Name=AMI_NAME,
    NoReboot=True
)

ami_id=response['ImageId']
print(f"AMI creation initiated for {instance_id} and its AMI ID is {ami_id}")
print("Waiting for AMI creation completion ")
ec2_client.get_waiter('image_available').wait(ImageIds=[ami_id])
print("AMI created successfully.")


#Get details of AMI linked ebs snapshot

ami_details=ec2_client.describe_images(ImageIds=[ami_id])['Images'][0]
snapshots=[]

for snapshot in ami_details['BlockDeviceMappings']:
    if snapshot['Ebs']['SnapshotId']:
        snapshots.append(snapshot['Ebs']['SnapshotId'])

print(f"Linked snapshots for AMI {ami_id} are {snapshots}")


## Applying tag to resources created using create_tags method and passing declared value in paramteres.

ami_tags = [
    {"Key": "Name", "Value": AMI_NAME},
    {"Key": "InstanceId", "Value": instance_id},
    {"Key": "BackupType", "Value": "AMI"},
    {"Key": "BackupDate", "Value": time.strftime("%Y-%m-%d")}
]
ec2_client.create_tags(Resources=[ami_id], Tags=ami_tags)

# Step 5: Apply tags to Snapshots
snapshot_tags = [
    {"Key": "Name", "Value": f"Backup-{instance_id}-{int(time.time())}"},
    {"Key": "InstanceId", "Value": instance_id},
    {"Key": "BackupType", "Value": "Snapshot"},
    {"Key": "BackupDate", "Value": time.strftime("%Y-%m-%d")}
]
if snapshots:  # avoid error if no snapshots
    ec2_client.create_tags(Resources=snapshots, Tags=snapshot_tags)

print("✅ Tags applied to AMI and snapshots successfully!")


