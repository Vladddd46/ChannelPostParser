import asyncio
import time
from datetime import datetime

from data_processors.data_processors import get_data_processor
from entrypoints.PostsFetcher import get_posts_fetcher
from utils.Logger import logger


async def posts_retriever(channels):
    posts_fetcher = await get_posts_fetcher()  # object for retriving data from service.
    data_processor = get_data_processor()

    data_saver = lambda channel: data_processor(
        channel
    )  # further processing of fetched data.

    ########### TODO
    # date = datetime(2024, 3, 16)
    # tasks = [
    #     posts_fetcher.get_posts_by_date(channel, date, data_saver) for channel in channels
    # ]

    start_data = datetime(2024, 3, 14)
    end_data = datetime(2024, 3, 15)
    tasks = [
        posts_fetcher.get_posts_by_date_range(channel, start_data, end_data, data_saver)
        for channel in channels
    ]

    # tasks = [
    #     posts_fetcher.get_last_n_posts(channel, 20, data_saver) for channel in channels
    # ]
    ########################

    print("Data is fetching... It may take some time.")
    results = await asyncio.gather(*tasks)

    ## No need to process results as it is already processed
    # for channel, result in zip(channels, results):
    #     print(f"Result for {channel}: {result}")

    await posts_fetcher.cleanup()


async def main():
    # TODO: Create functionality that gets info about channels needed to be monitored.
    # Temporary solution: List of channels from which the script will retrieve posts.
    channels = ["ssternenko"]

    # Create tasks for both coroutines
    tasks = [posts_retriever(channels)]
    await asyncio.gather(*tasks)


if __name__ == "__main__":
    logger.info("=Program started=")
    start_time = time.time()
    asyncio.run(main())
    end_time = time.time()
    logger.info(f"Program time={end_time-start_time} seconds")
    print("===Complete===")
