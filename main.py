import asyncio
import time
from datetime import datetime

from data_processors.dump_data_to_json import dump_data_to_json
from entrypoints.PostsFetcher import get_posts_fetcher


async def posts_retriever(channels):
    posts_fetcher = await get_posts_fetcher()  # object for retriving data from service.
    data_saver = lambda channel: dump_data_to_json(
        channel
    )  # further processing of fetched data.

    tasks = [
        posts_fetcher.get_last_n_posts(channel, 5, data_saver) for channel in channels
    ]
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
    start_time = time.time()
    asyncio.run(main())
    end_time = time.time()
    print(f"Program time={end_time-start_time} seconds")
    print("===Complete===")
