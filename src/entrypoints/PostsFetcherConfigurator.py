# @ author: vladddd46
# @ date:   16.03.2024
# @ brief:  Is responsible for returning configuration of
# 			 1. what channels to monitor.
# 			 2. which method to use for monitoring. get_posts_by_date, get_last_n_posts.
# 			It can get info from external service as well as predefined data.
# 			The way ExternalConfigurator gets info depends on configuration in config.py
import json
import time
from datetime import datetime

import boto3
from config import QUEUE_READ_SLEEP_TIME, USE_PREDEFINED_REQUESTS
from src.entrypoints.config_posts_fetcher import predefined_config
from src.utils.Logger import logger
from tmp.creds import QUEUE_URL
from src.adaptors.RequestFormatAdaptors import adopt_request_to_task_format

class PostsFetcherConfigurator:
    def __validate_queue(self, queue):
        # check if queue exist.
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

    def __init__(self):
        self.sqs_client = boto3.client("sqs", region_name="us-east-1")
        if (
            USE_PREDEFINED_REQUESTS == False
            and self.__validate_queue(QUEUE_URL) == False
        ):
            exit(1)

    def __read_queue(self):
        # Waits until the message appears in queue.
        # Reads message from queue, deletes messeage after read,
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

                    # TODO: maybe add confirming mechanism, when requests from queue will be deleted,
                    #       only after success data retrieval.
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

    def __validate_request(self, request):
        # check if request has the proper format.
        try:
            json_object = json.loads(request)
            if isinstance(json_object, dict):
                return True
            else:
                return False
        except ValueError:
            return False

    def __convert_message_in_request(self, message):
        req = None
        if self.__validate_request(message) == True:
            tmp_req = json.loads(message)
            try:
                if "from_date" in tmp_req.keys() and "to_date" in tmp_req.keys():
                    _from_date_str = tmp_req["from_date"]
                    _to_date_str = tmp_req["to_date"]
                    _from_date = datetime.strptime(_from_date_str, "%Y-%m-%d")
                    _to_date = datetime.strptime(_to_date_str, "%Y-%m-%d")
                    tmp_req["from_date"] = _from_date
                    tmp_req["to_date"] = _to_date
                req = tmp_req
            except Exception as e:
                logger.error(f"Error occured during date conversation: {e}")
        return req

    def __get_request_from_queue(self):
        req = None
        while True:
            data = self.__read_queue()
            req = self.__convert_message_in_request(data)
            if req != None:
                break
        return req

    def get_request(self):
        logger.info(
            f"Getting request from queue | use_predefined_data={USE_PREDEFINED_REQUESTS}"
        )
        ret = None
        if USE_PREDEFINED_REQUESTS == True:
            ret = predefined_config
        else:
            req = self.__get_request_from_queue()
            ret = adopt_request_to_task_format(req)
        return ret
