# @ author: vladddd46
# @ date:   16.03.2024
# @ brief:  Is responsible for returning Request of
# 			 1. what channels to monitor.
# 			 2. which method to use for monitoring. get_posts_by_date, get_last_n_posts.
# 			It can get info from external service as well as predefined data.
# 			The way ExternalConfigurator gets info depends on configuration in config.py
import json
import time
from datetime import datetime

import boto3
from config import USE_PREDEFINED_REQUESTS
from src.entrypoints.config_posts_fetcher import predefined_config
from src.entrypoints.Queue import Queue
from src.utils.Logger import logger
from src.adaptors.RequestFormatAdaptors import (
    convert_predefined_config_to_request,
    convert_message_to_request,
)
from src.entities import Request


class PostsFetcherConfigurator:
    def __init__(self):
        self.queue = None
        if USE_PREDEFINED_REQUESTS == False:
            self.queue = Queue()

    def get_request(self) -> Request:
        logger.info(
            f"Getting request from queue | use_predefined_data={USE_PREDEFINED_REQUESTS}",
            only_debug_mode=True,
        )
        req = None
        if USE_PREDEFINED_REQUESTS == True:
            req = convert_predefined_config_to_request(predefined_config)
        else:
            message = self.queue.get_message_from_queue()
            req = convert_message_to_request(message)
        return req
