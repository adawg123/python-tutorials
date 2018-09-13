import boto3


def create_instance():
    ec2_resource = boto3.resource('ec2',region_name="us-east-1")
    instances = ec2_resource.create_instances(ImageId='ami-6871a115',
                MinCount=1, MaxCount=1,InstanceType='t2.micro',
                SecurityGroupIds=['launch-wizard-3'],KeyName='fullstack')
    for instance in instances:
        print instance
    ec2_client = boto3.client('ec2')
    waiter=ec2_client.get_waiter('instance_running')
    waiter.wait(InstanceIds=[instances[0].id])
    print ("Instance is Running now!")

create_instance()
