# Emulates scheduler.
# writes messages in queue

import json
from datetime import date, datetime, timedelta

import boto3

from tmp.creds import REQUEST_QUEUE_URL

# defines
year = 365
two_years = year * 2
hundred_days = 100

fromtime = hundred_days
_current_date = datetime.now().date()
_from_date = _current_date - timedelta(days=fromtime)
#######################################################


# encodes date in json.
class CustomJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, date):
            return obj.isoformat()  # Convert date to ISO format
        return super().default(obj)


sqs = boto3.client("sqs", region_name="us-east-1")  # Create SQS client
response = sqs.list_queues()


allAvailableQueues = response["QueueUrls"]
queueUrl = REQUEST_QUEUE_URL

# write in queue
predefined_requests = []
channels = ["russvolcorps", "ded_shinibi"]#, "ssternenko"]
for i in channels:
    cfg1 = {
        "telegram_channel_id": i,
        "from_date": _from_date,
        "to_date": _current_date,
        "is_backfill": False,
    }
    predefined_requests.append(cfg1)

for req in predefined_requests:
    json_string = json.dumps(req, cls=CustomJSONEncoder)
    response = sqs.send_message(QueueUrl=queueUrl, MessageBody=json_string)
    print("response:", response)
