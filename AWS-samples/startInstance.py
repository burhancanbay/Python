import boto3
client = boto3.client('ec2')
response = client.start_instances(InstanceIds=['i-05ce2f8e16475ea45'])
for instance in response['StartingInstances']:
    print('The instance with id {} has started'.format(instance['InstanceId']))