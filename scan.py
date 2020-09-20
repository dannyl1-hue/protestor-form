import boto3 
from boto3.dynamodb.conditions import Attr

def scan_protestors(event):
    """
    Returns a dictionary of the number of people who went to protests in certain month
    
    Inputs: event
    
    Output: dictionary with key = month and value = number of people who participated
    that month 
    
    """
    months = ["01","02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]
    month_frequency = {}
    dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
    # table = dynamodb.Table('Books')
    table = dynamodb.Table('ProtestorTbl')
    
    # When making a Query API call, we use the KeyConditionExpression parameter to specify the hash key on which we want to query.
    # We're using the Key object from the Boto3 library to specify that we want the attribute name ("Author")
    # to equal "John Grisham" by using the ".eq()" method.
    for mon in months:
        count = 0
        resp = table.scan(FilterExpression=Attr('protestdate').begins_with(mon))
        print("The query returned the following items:")
        for item in resp['Items']:
            # print(item)
            count += 1
        month_frequency[mon] = count
    
    print(month_frequency)
    return month_frequency
    
def lambda_handler(event, context):
    scan_protestors(event) 
