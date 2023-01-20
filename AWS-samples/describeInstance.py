import boto3
client = boto3.client('ec2')
response = client.describe_instances(Filters=[{
    'Name':'instance-state-name',
    'Values':['running']
}])
for reservation in response['Reservations']:
    for instance in reservation['Instances']:
        print('The instance with id {} is running'.format(instance['InstanceId']))
