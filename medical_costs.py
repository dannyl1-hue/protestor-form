import boto3

def medical_cost(event):
    """
    Returns a dictionary of medical cost ranges and their frequencies
    
    Inputs: event
    
    Output: dictionary
    
    """
   
    medical_costs = ["0","10000","20000", "30000","40000","50000","60000","70000","80000","90000","100000"]
    medical_frequency = {}
    dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
    table = dynamodb.Table('ProtestorTbl')
    
    for index in range(len(medical_costs) - 1):
        resp = table.scan()
        count = 0
        # check each item to access individual item cost and compare it with medical_costs
        for item in resp['Items']:
            # print(item)
            
            cost = int(item["medicalcost"])
            lower = int(medical_costs[index])
            upper = int(medical_costs[index + 1])
            # print("cost " + str(cost) + " lower" + str(lower) + " upper" + str(upper))
            if cost > lower and cost <= upper:
                count += 1
                print("count: " + str(count))
        medical_frequency[medical_costs[index] + " to " + medical_costs[index+1]] = count
    
    print(medical_frequency) 
    return medical_frequency

def lambda_handler(event, context):
    medical_cost(event)