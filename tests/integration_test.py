# Emulates scheduler.
# writes messages in queue

import json
from datetime import date, datetime, timedelta
import boto3
from tmp.creds import REQUEST_QUEUE_URL
import os
import time

_current_date = datetime.now().date()
_from_date = _current_date - timedelta(days=10)
#######################################################


def count_files_by_path(directory):
    file_count = 0
    for root, dirs, files in os.walk(directory):
        file_count += len(files)
    return file_count


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
FILE_PATH = "/tmp/retrieved_data"

num_of_files_while_start = count_files_by_path(FILE_PATH)


# write in queue
predefined_requests = []
channels = ["ded_shinibi"]
for i in channels:
    cfg1 = {
        "telegram_channel_id": i,
        "from": _from_date,
        "to": _current_date,
        "is_backfill": False,
    }
    predefined_requests.append(cfg1)

for req in predefined_requests:
    json_string = json.dumps(req, cls=CustomJSONEncoder)
    response = sqs.send_message(QueueUrl=queueUrl, MessageBody=json_string)
    print("response:", response)

time.sleep(10)
num_of_files_while_end = count_files_by_path(FILE_PATH)

if num_of_files_while_start<num_of_files_while_end:
    print("OK")
else:
    print("DATA RETRIEVE FAILED")