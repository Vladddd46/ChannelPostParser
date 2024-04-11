import asyncio
import time
from datetime import datetime
from typing import Callable

from config import SLEEP_TIME_AFTER_FETCHING, USE_PREDEFINED_REQUESTS
from src.data_processors.data_processors import get_data_processor
from src.entities.Channel import Channel
from src.entities.Request import Request, RequestCode
from src.entrypoints.PostsFetcher import PostsFetcher, get_posts_fetcher
from src.entrypoints.PostsFetcherConfigurator import PostsFetcherConfigurator
from src.entrypoints.Queue import Queue
from src.utils.Logger import logger
from src.utils.Utils import create_response
from tmp.creds import RESPONSE_QUEUE_URL


# Determines, which tasks should be run based on request
def determine_tasks_to_run(
    req: Request, data_saver: Callable[[Channel], None], fetcher: PostsFetcher
):
    request_data = req.data
    channels = request_data.channels

    tasks = []
    if request_data.name == "get_last_n_posts":
        num = int(request_data.params["num"])
        tasks = [
            fetcher.get_last_n_posts(channel, num, data_saver) for channel in channels
        ]
    elif request_data.name == "get_last_post":
        tasks = [fetcher.get_last_post(channel, data_saver) for channel in channels]
    elif request_data.name == "get_posts_by_date_range":
        from_date = request_data.params["from_date"]
        to_date = request_data.params["to_date"]
        tasks = [
            fetcher.get_posts_by_date_range(channel, from_date, to_date, data_saver)
            for channel in channels
        ]
    elif request_data.name == "get_posts_by_date":
        date = request_data.params["date"]
        tasks = [
            fetcher.get_posts_by_date(channel, date, data_saver) for channel in channels
        ]

    elif request_data.name == "get_post_by_id":
        pid = request_data.params["pid"]
        tasks = [
            fetcher.get_posts_by_date(channel, pid, data_saver) for channel in channels
        ]
    else:
        logger.error(f"Unknown function={request_data.name}")
    return tasks


async def posts_retriever():
    # object for posts fetcher configuration
    posts_fetcher_configurator = PostsFetcherConfigurator()

    # object for retriving data from service.
    posts_fetcher = await get_posts_fetcher()

    # object for further processing of fetched data.
    data_processor = get_data_processor()
    data_saver = lambda channel: data_processor(channel)

    # queue for sending response
    response_queue = Queue(RESPONSE_QUEUE_URL)

    while True:
        try:
            request_to_handle = posts_fetcher_configurator.get_request()
            logger.info(
                f"Request {request_to_handle.rid} | {request_to_handle.data} | msg={request_to_handle.error_msg}"
            )
            start_time = time.time()
            if request_to_handle.code == RequestCode.OK:
                tasks = determine_tasks_to_run(request_to_handle, data_saver, posts_fetcher)
                if len(tasks) > 0:
                    print("Data is fetching... It may take some time.")
                    results = await asyncio.gather(*tasks)
                    response = create_response(req=request_to_handle, filenames=results)
                    response = response.to_json()
                    response_queue.send_message(response)
                else:
                    print("No task for fetching. Maybe some error occured")
            end_time = time.time()
            logger.info(f"Fetching time={end_time-start_time} seconds")
        except Exception as e:
            logger.error(f"Unknown error occured: {e}")

    await posts_fetcher.cleanup()


if __name__ == "__main__":
    logger.info("=Program started=", only_debug_mode=True)
    asyncio.run(posts_retriever())
    logger.info("===Complete===", only_debug_mode=True)
