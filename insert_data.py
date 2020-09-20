#Uploads data from a form to a DynamoDB table 
import json
import logging
import os
import time
import uuid

import boto3
dynamodb = boto3.resource('dynamodb')


def create(event, context):
    data = json.loads(event['body']) 
    
    print(data)
    
    if 'phone' not in data:
        logging.error("Validation Failed")
        raise Exception("Couldn't create the protest item.")
    
    timestamp = str(time.time())

    table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])

    item = {
        'current_city': data['current_city'],
        'current_state': data['current_state'],
        'protestdate': data['protestdate'],
        'protestduration': data['protestduration'],
        'medicalcost': data['medicalcost'],
        'phone': data['phone'],
        'injured': data['injured'],
        'force1': data['force1'],
        'force2': data['force2'],
        'force3': data['force3'],
        'force4': data['force4']
    }

    # write the todo to the database
    table.put_item(Item=item)

    # create a response
    response = {
        "statusCode": 200,
        "headers": { 
            "Access-Control-Allow-Origin": "*" 
        },    
        "body": json.dumps(item)
    }

    return response
