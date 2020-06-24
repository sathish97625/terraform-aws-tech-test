
import json
import boto3
dynamodb = boto3.resource('dynamodb')

def lambda_handler(event, context):
 
# For every hour, get the status, keep it in a variable and insert in dynamodb which is already been created
    ec2 = boto3.resource('ec2')
    for status in ec2.meta.client.describe_instance_status()['InstanceStatuses']:
        print(status)


    for instance in ec2.instances.all():
        print (instance.id , instance.state)
        
    # insert 25 rows in dynamodb    
    table = dynamodb.Table('ec2-state')
    table.put_item(
        Item={
             'ec2-state': ' ',
             'ec2-id': ' ',
        
            }
    )
    
    # check 25 row every hour in dynamodb and delete it if not null
    
    # additionally get instances with running status from dynamo db
    response = table.scan(
    FilterExpression=Attr('ec2-state').eq('running')
        
        
