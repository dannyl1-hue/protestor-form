import boto3
from boto3.dynamodb.conditions import Attr
def percent_injured(event):
    """
    Returns a float with the percentage of people injured 
    
    Inputs: event
    
    Output: number of people injured / total number of people
    
    """
    injuries = ["injured","notinjured"]
    injury_frequency = {}
    dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
    table = dynamodb.Table('ProtestorTbl')
    
    # When making a Query API call, we use the KeyConditionExpression parameter to specify the hash key on which we want to query.
    # We're using the Key object from the Boto3 library to specify that we want the attribute name ("Author")
    # to equal "John Grisham" by using the ".eq()" method.
    for injure in injuries:
        count = 0
        resp = table.scan(FilterExpression=Attr('injury').begins_with(injure))
        print("The query returned the following items:")
        for item in resp['Items']:
            # print(item)
            count += 1
        injury_frequency[injure] = count
        
    num_injured = injury_frequency["injured"]
    num_notinjured = injury_frequency["notinjured"]
    print(num_injured)
    percentage_injured = num_injured / (num_injured + num_notinjured)
    print(injury_frequency)
    print(percentage_injured)
    return percentage_injured

def lambda_handler(event, context):
    percent_injured(event)
