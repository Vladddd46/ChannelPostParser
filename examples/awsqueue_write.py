# Example of writing messages in queue
import boto3
from datetime import datetime

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
current_datetime = datetime.now()
data = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
response = sqs.send_message(QueueUrl=queueUrl, MessageBody=data)

print("response:", response)
