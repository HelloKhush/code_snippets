import boto3
import json
from botocore.exceptions import ClientError


client = boto3.client('ec2', region_name='us-west-2')

def get_default_vpc(client):
        """Returns a default VPC."""
        res = client.describe_vpcs(Filters=[{'Name': 'isDefault', 'Values': ['true']}])
        vpc_id = res.get('Vpcs', [{}])[0].get('VpcId', '')
        if len(vpc_id):
            print(vpc_id)
            
             
        else:
             return None
