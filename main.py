import asyncio
import time
from datetime import datetime
from typing import Callable
from src.data_processors.data_processors import get_data_processor
from src.entrypoints.PostsFetcher import get_posts_fetcher, PostsFetcher
from src.utils.Logger import logger
from src.entrypoints.PostsFetcherConfigurator import PostsFetcherConfigurator
from src.entities.Channel import Channel
from src.entities.Request import RequestCode, Request
from config import USE_PREDEFINED_REQUESTS, SLEEP_TIME_AFTER_FETCHING


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

    while True:
        request_to_handle = posts_fetcher_configurator.get_request()
        logger.info(
            f"Request {request_to_handle.rid} | {request_to_handle.data} | msg={request_to_handle.error_msg}"
        )
        if request_to_handle.code == RequestCode.OK:
            tasks = determine_tasks_to_run(request_to_handle, data_saver, posts_fetcher)
            if len(tasks) > 0:
                print("Data is fetching... It may take some time.")
                results = await asyncio.gather(*tasks)
            else:
                print("No task for fetching. Maybe some error occured")

    await posts_fetcher.cleanup()


if __name__ == "__main__":
    while True:
        try:
            logger.info("=Program started=")
            start_time = time.time()
            asyncio.run(posts_retriever())
            end_time = time.time()
            logger.info(f"Program time={end_time-start_time} seconds")
            print("===Complete===")

            # If we use predefined configuration instead of reading from queue,
            #  then we need to define sleep time between each fetching.
            # If we use queue, we gonna do fetching each time,
            #  there is message in queue
            if USE_PREDEFINED_REQUESTS == True:
                logger.info(
                    f"Program going to sleep for time={SLEEP_TIME_AFTER_FETCHING} seconds"
                )
                time.sleep(SLEEP_TIME_AFTER_FETCHING)
        except Exception as e:
            logger.error(e, only_debug_mode=True)
