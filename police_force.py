import boto3
from boto3.dynamodb.conditions import Attr

def police_force(event):
    """
    Returns a dictionary showing the frequencies of each force used 
    
    Inputs: event
    
    Output: dictionary
    
    """
    #{"force1" : "teargas", "force2" : "rubberbullets", "force3" : "bruteforce", "force4" : "otherforce"}
    forces = ['force1', 'force2', 'force3', 'force4']
    force_frequency = {}
    dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
    table = dynamodb.Table('ProtestorTbl')
    
       for force in forces:
        count = 0
        resp = table.scan(FilterExpression=Attr(force).begins_with("1"))
        print("The query returned the following items:")
        for item in resp['Items']:
            # print(item)
            count += 1
        force_frequency[force] = count
    
    print(force_frequency)
    return force_frequency
    
def lambda_handler(event,context):
    police_force(event)
