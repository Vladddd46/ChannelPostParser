import asyncio
import time
from datetime import datetime
from typing import Callable
from src.data_processors.data_processors import get_data_processor
from src.entrypoints.PostsFetcher import get_posts_fetcher, PostsFetcher
from src.utils.Logger import logger
from src.entrypoints.PostsFetcherConfigurator import PostsFetcherConfigurator
from src.entities.Channel import Channel


# Determines, which tasks should be run based on config
# from PostFetcherConfigurator
def determine_tasks_to_run(
    cnfg: dict, data_saver: Callable[[Channel], None], fetcher: PostsFetcher
):
    # check if needed keys are presented in configuration data
    keys_to_check = ["function", "channels", "params"]
    for k in keys_to_check:
        if k not in cnfg.keys():
            logger.error(f"No '{k}' key in cnfg.keys()")
            return []
    if len(cnfg["channels"]) == 0:
        logger.warning(f"No channel to monitor: list is empty")
        return []
    channels = cnfg["channels"]

    tasks = []
    if cnfg["function"] == "get_last_n_posts":
        if "num" in cnfg["params"]:
            num = int(cnfg["params"]["num"])
            tasks = [
                fetcher.get_last_n_posts(channel, num, data_saver)
                for channel in channels
            ]
        else:
            logger.error(f"No 'num' key in cnfg['params']")
    elif cnfg["function"] == "get_last_post":
        tasks = [fetcher.get_last_post(channel, data_saver) for channel in channels]
    elif cnfg["function"] == "get_posts_by_date_range":
        if "from_date" in cnfg["params"] and "to_date" in cnfg["params"]:
            from_date = cnfg["params"]["from_date"]
            to_date = cnfg["params"]["to_date"]
            tasks = [
                fetcher.get_posts_by_date_range(channel, from_date, to_date, data_saver)
                for channel in channels
            ]
        else:
            logger.error(f"No 'from_date'/'to_date' key in cnfg['params']")
    elif cnfg["function"] == "get_posts_by_date":
        if "date" in cnfg["params"]:
            date = cnfg["params"]["date"]
            tasks = [
                fetcher.get_posts_by_date(channel, date, data_saver)
                for channel in channels
            ]
        else:
            logger.error(f"No 'date' key in cnfg['params']")
    elif cnfg["function"] == "get_post_by_id":
        if "pid" in cnfg["params"]:
            pid = cnfg["params"]["pid"]
            tasks = [
                fetcher.get_posts_by_date(channel, pid, data_saver)
                for channel in channels
            ]
        else:
            logger.error(f"No 'pid' key in cnfg['params']")
    else:
        logger.error(f"Unknown function={cnfg['function']}")
    return tasks


async def posts_retriever():
    # object for retriving data from service.
    posts_fetcher = await get_posts_fetcher()

    # object for further processing of fetched data.
    data_processor = get_data_processor()
    data_saver = lambda channel: data_processor(channel)

    # object for posts fetcher configuration
    posts_fetcher_configurator = PostsFetcherConfigurator()
    posts_fetcher_config = posts_fetcher_configurator.get_posts_fetcher_configuration()

    tasks = []
    try:
        tasks = determine_tasks_to_run(posts_fetcher_config, data_saver, posts_fetcher)
    except Exception as e:
        logger.warning(f"Some exception occured: {e}")

    if len(tasks) > 0:
        print("Data is fetching... It may take some time.")
        results = await asyncio.gather(*tasks)
    else:
        print("No task for fetching. Maybe some error occured. Check logs: ./logs")

    ## No need to process results as it is already processed
    # for channel, result in zip(channels, results):
    #     print(f"Result for {channel}: {result}")

    await posts_fetcher.cleanup()


if __name__ == "__main__":
    logger.info("=Program started=")
    start_time = time.time()
    asyncio.run(posts_retriever())
    end_time = time.time()
    logger.info(f"Program time={end_time-start_time} seconds")
    print("===Complete===")
