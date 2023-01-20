import boto3
client = boto3.client('ec2')
response = client.terminate_instances(InstanceIds=['i-0d92916626b4f8ca2'])
for instance in response['TerminatingInstances']:
    print('The instance with id {} has terminated'.format(instance['InstanceId']))