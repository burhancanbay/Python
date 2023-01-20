import boto3
client = boto3.client('ec2')
resp = client.run_instances(ImageId='ami-0ac8ec06ffedcd1b5',
                               InstanceType='t2.micro',
                               MinCount=1,
                               MaxCount=1)
for instance in resp['Instances']:
    print(instance['InstanceId'])