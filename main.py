import asyncio
import time
from datetime import datetime

from src.data_processors.data_processors import get_data_processor
from src.entities.Channel import Channel
from src.entities.Request import Request, RequestCode
from src.entrypoints.PostsFetcher import PostsFetcher, get_posts_fetcher
from src.entrypoints.PostsFetcherConfigurator import PostsFetcherConfigurator
from src.entrypoints.Queue import Queue
from src.utils.Logger import logger
from src.utils.Utils import create_response, determine_tasks_to_run
from src.adaptors.RequestFormatAdaptors import convert_str_to_date
from tmp.creds import RESPONSE_QUEUE_URL, AWS_REGION_NAME
import config

async def posts_retriever():
    # object for getting fetcher configuration
    posts_fetcher_configurator = PostsFetcherConfigurator()

    # object for retriving data from service.
    posts_fetcher = await get_posts_fetcher()

    # object for further processing of fetched data.
    data_processor = get_data_processor()
    data_saver = lambda channel: data_processor(channel)

    # queue for sending response
    response_queue = Queue(RESPONSE_QUEUE_URL, region_name=AWS_REGION_NAME)
    live_response_queue = Queue(RESPONSE_QUEUE_URL, region_name=AWS_REGION_NAME)

    while True:
        try:
            request_to_handle = posts_fetcher_configurator.get_request()

            # TODO Crutch
            config.IS_BACKFILL = request_to_handle.data.is_backfill
            # END OF CRUTCH

            logger.info(
                f"Request {request_to_handle.rid} | {request_to_handle.data} | msg={request_to_handle.error_msg}"
            )

            start_time = time.time()

            # Fetching process
            if request_to_handle.code == RequestCode.OK:
                tasks = determine_tasks_to_run(
                    request_to_handle, data_saver, posts_fetcher
                )
                if len(tasks) > 0:
                    logger.info(
                        "Data is fetching... It may take some time.",
                        only_debug_mode=True,
                    )
                    results = await asyncio.gather(*tasks)
                    response = create_response(req=request_to_handle, filenames=results)
                    if response != None:
                        response = response.to_json()
                        response_queue.send_message(response)
                        live_response_queue.send_message(response)
                        logger.info(f"Response | {response}")
                    else:
                        logger.info(f"Response | None")
                else:
                    logger.info("No task for fetching. Maybe some error occured")
            else:
                logger.error(f"Error during getting the request: {request_to_handle.error_msg}")

            end_time = time.time()
            logger.info(f"Fetching time={end_time-start_time} seconds")
        except Exception as e:
            logger.error(f"Unknown error occured: {e}")

    await posts_fetcher.cleanup()


if __name__ == "__main__":
    logger.info("=Program started=", only_debug_mode=True)
    asyncio.run(posts_retriever())
    logger.info("===Complete===", only_debug_mode=True)
