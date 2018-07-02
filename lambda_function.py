import json
from datetime import datetime

def lambda_handler(event, context):
    print("In lambda_handler " + str(datetime.now()))
    print("Event:")
    print(json.dumps(event, indent=True))
 