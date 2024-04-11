# Emulates scheduler.
# writes messages in queue

import boto3
from datetime import datetime, timedelta, date
import json

year = 365
two_years = year * 2
two_days = 2

fromtime = two_days
_current_date = datetime.now().date()
_from_date = _current_date - timedelta(days=fromtime)


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
predefined_config = []
# channels = ["ssternenko", "russvolcorps", "ded_shinibi"]
channels = ["russvolcorps"]
for i in channels:
    cfg1 = {
        "telegram_channel_id": i,
        "from_date": _from_date,
        "to_date": _current_date,
        "is_backfill": False,
    }
    predefined_config.append(cfg1)


for req in predefined_config:
    json_string = json.dumps(req, cls=CustomJSONEncoder)
    response = sqs.send_message(QueueUrl=queueUrl, MessageBody=json_string)
    print("response:", response)
