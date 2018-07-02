import json
from datetime import datetime
from ESLambdaLog import *

def lambda_handler(event, context):
    print("In lambda_handler " + str(datetime.now()))
    print("Event:")
    print(json.dumps(event, indent=True))


    es = ESLambdaLog("aws_lnkchk_cache_stream")

    esraw = ESLambdaLog("aws_lnkchk_cache_stream_raw")
    esraw.log_event(event)
    
    print("Logging to ES")
    for record in event["Records"]:
        event_name = record["eventName"]
        url = record["dynamodb"]["Keys"]["url"]["S"]
        image = "NewImage"
        if event_name == "REMOVE":
            image = "OldImage"
        http_response = record["dynamodb"][image]["http_response"]["S"]
        print("\t" + event_name + " " + url)
        es_event = {"event" : event_name, "url" : url, "http_response" : http_response}
        es.log_event(es_event)

    print("Finished.")
 