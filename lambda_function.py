import json
from datetime import datetime
from ESLambdaLog import *

def lambda_handler(event, context):
    print("In lambda_handler " + str(datetime.now()))
    print("Event:")
    print(json.dumps(event, indent=True))


    es = ESLambdaLog("aws_lnkchk_cache_stream")
    
    print("Logging to ES")
    es.log_event(event)

    print("Finished.")
 