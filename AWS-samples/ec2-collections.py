import boto3
ec2 = boto3.resource('ec2')
for instance in ec2.instances.all():
    print('The instance {} has {} instance type'.format(instance.instance_id,instance.instance_type))