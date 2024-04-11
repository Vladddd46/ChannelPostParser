# @ author: vladddd46
# @ date:   11.04.2024
# @ brief:  Queue implementation
import json
import time

import boto3
from config import QUEUE_READ_SLEEP_TIME, USE_PREDEFINED_REQUESTS
from src.utils.Logger import logger
from tmp.creds import QUEUE_URL


class Queue:
    def __init__(self):
        self.sqs_client = boto3.client("sqs", region_name="us-east-1")
        if (
            USE_PREDEFINED_REQUESTS == False
            and self.__validate_queue(QUEUE_URL) == False
        ):
            exit(1)

    def __validate_queue(self, queue):
        # @brief: check if queue exist.
        # @return: bool
        ret = True
        response = self.sqs_client.list_queues()
        if "QueueUrls" not in response.keys():
            logger.error("No 'QueueUrls' key in queues list.")
            ret = False
        allAvailableQueues = response["QueueUrls"]
        if queue not in allAvailableQueues:
            logger.error(f"queue={queue} was not found in available queues list")
            ret = False
        return ret

    def __read_queue(self):
        # Waits until the message appears in queue.
        # Reads message from queue, deletes message after read,
        # returns message body.
        while True:
            response = self.sqs_client.receive_message(
                QueueUrl=QUEUE_URL,
                MaxNumberOfMessages=1,
                VisibilityTimeout=10,
                WaitTimeSeconds=5,
            )

            if "Messages" in response:
                messages = response["Messages"]
                if len(messages) == 0:
                    logger.info(f"Queue is empty", only_debug_mode=True)
                else:
                    message = messages[0]
                    message_body = message["Body"]

                    # Delete the message from the queue once processed
                    receipt_handle = message["ReceiptHandle"]
                    self.sqs_client.delete_message(
                        QueueUrl=QUEUE_URL, ReceiptHandle=receipt_handle
                    )

                    logger.info(
                        f"Received message_body={message_body}", only_debug_mode=True
                    )
                    return message_body
            else:
                logger.info(f"No messages available in the queue", only_debug_mode=True)
            time.sleep(QUEUE_READ_SLEEP_TIME)

    def __validate_message(self, message):
        # brief: check if message is convertable in json and
        #        has a proper format.
        try:
            json_object = json.loads(message)
            if isinstance(json_object, dict):
                return True
            else:
                return False
        except ValueError:
            return False

    def get_message_from_queue(self):
        message = None
        while True:
            data = self.__read_queue()
            if self.__validate_message(data) == True:
                message = json.loads(data)
            if message != None:
                break
        return message
