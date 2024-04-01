import boto3

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


# Receive messages from the queue
response = sqs.receive_message(
    QueueUrl=queueUrl,
    MaxNumberOfMessages=1,  # Maximum number of messages to retrieve (adjust as needed)
    VisibilityTimeout=10,  # The duration (in seconds) that the received messages are hidden from subsequent retrieve requests
    WaitTimeSeconds=5,  # The duration (in seconds) for which the call waits for a message to arrive in the queue before returning.
)

# Check if messages are received
if "Messages" in response:
    messages = response["Messages"]
    for message in messages:
        message_body = message["Body"]
        print("Received message:", message_body)
        print(message)
        # Delete the message from the queue once processed
        receipt_handle = message["ReceiptHandle"]
        sqs.delete_message(QueueUrl=queueUrl, ReceiptHandle=receipt_handle)
else:
    print("No messages available in the queue.")
