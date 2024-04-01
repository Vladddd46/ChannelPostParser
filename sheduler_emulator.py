# Emulates scheduler.
# writes messages in queue

import boto3
from datetime import datetime, timedelta, date
import json

year = 365
two_years = year * 2

_current_date = datetime.now().date()
_from_date = _current_date - timedelta(days=two_years)


# encodes date in json.
class CustomJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, date):
            return obj.isoformat()  # Convert date to ISO format
        return super().default(obj)


sqs = boto3.client("sqs", region_name="us-east-1")  # Create SQS client
response = sqs.list_queues()

if "QueueUrls" not in response.keys():
    print("No 'QueueUrls' key")
    exit(1)
allAvailableQueues = response["QueueUrls"]

if len(allAvailableQueues) > 0:
    queueUrl = allAvailableQueues[0]
else:
    print("No queue found")
    exit(1)

# write in queue
predefined_config = {
    "channels": ["ssternenko", "russvolcorps", "ded_shinibi"],
    "function": "get_posts_by_date_range",
    "params": {"from_date": _from_date, "to_date": _current_date},
}
json_string = json.dumps(predefined_config, cls=CustomJSONEncoder)
response = sqs.send_message(QueueUrl=queueUrl, MessageBody=json_string)

print("response:", response)
