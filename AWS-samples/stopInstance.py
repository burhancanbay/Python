import boto3
client = boto3.client('ec2')
response = client.stop_instances(InstanceIds=['i-05ce2f8e16475ea45'])
for instance in response['StoppingInstances']:
    print('The instance with id {} has stopped'.format(instance['InstanceId']))