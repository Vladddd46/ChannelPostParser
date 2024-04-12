# @ author: vladddd46
# @ date:   10.03.2024
# @ brief:  Entrypoint class, that provides
# 			API for getting posts from service
from datetime import datetime
from typing import List

from config import SERVICE_NAME
from src.entities.Post import Post
from src.fetchers.FetcherInterface import FetcherInterface
from src.fetchers.TelegramFetcher import TelegramFetcher
from typing import Callable
from src.entities.Channel import Channel
from src.utils.Logger import logger


class PostsFetcher:
    def __init__(self, fetcher: FetcherInterface):
        self._fetcher = fetcher
        self._is_setup = False
        self._is_cleanup = True

    def __del__(self):
        if self._is_cleanup == False:
            logger.error(
                f"PostsFetcher was not cleaned up... You have to always cleanup fetcher after using it...",
                only_debug_mode=True,
            )
            exit(1)

    def __str__(self):
        return str(self._fetcher)

    def __repr__(self):
        return str(self._fetcher)

    def validate_setup(func):
        def wrapper(self, *args, **kwargs):
            if not self._is_setup:
                logger.error(f"Operation cannot be done, PostaFetcher is not set up")
                exit(1)
            return func(self, *args, **kwargs)

        return wrapper

    async def setup(self):
        if self._is_setup == True:
            logger.error(f"Cannot setup: Posts fetcher is already setted up.")
            exit(1)

        await self._fetcher.setup()
        self._is_setup = True
        self._is_cleanup = False

    async def cleanup(self):
        if self._is_setup == False:
            logger.error(f"Cannot cleanup: Posts fetcher is not setted up.")
            exit(1)
        await self._fetcher.cleanup()
        self._is_setup = False
        self._is_cleanup = True

    @validate_setup
    async def get_last_post(
        self, channel_username: str, data_saver: Callable[[Channel], None]
    ) -> List[Channel]:
        logger.info(
            f"Request=get_last_post, params: channel_username={channel_username}",
            only_debug_mode=True,
        )
        res = await self._fetcher.get_last_post(channel_username, data_saver)
        return res

    @validate_setup
    async def get_last_n_posts(
        self, channel_username: str, num: int, data_saver: Callable[[Channel], None]
    ) -> List[Channel]:
        logger.info(
            f"Request=get_last_n_posts, params: channel_username={channel_username}, num={num}",
            only_debug_mode=True,
        )
        data = await self._fetcher.get_last_n_posts(channel_username, num, data_saver)
        return data

    @validate_setup
    async def get_posts_by_date_range(
        self,
        channel_username: str,
        from_date: datetime,
        to_date: datetime,
        data_saver: Callable[[Channel], None],
    ) -> List[Channel]:
        logger.info(
            f"Request=get_posts_by_date_range, params: channel_username={channel_username}, from_date={from_date}, to_date={to_date}",
            only_debug_mode=True,
        )
        data = await self._fetcher.get_posts_by_date_range(
            channel_username, from_date, to_date, data_saver
        )
        return data

    @validate_setup
    async def get_posts_by_date(
        self,
        channel_username: str,
        date: datetime,
        data_saver: Callable[[Channel], None],
    ) -> List[Channel]:
        logger.info(
            f"Request=get_posts_by_date, params: channel_username={channel_username}, date={date}",
            only_debug_mode=True,
        )
        data = await self._fetcher.get_posts_by_date(channel_username, date, data_saver)
        return data

    @validate_setup
    async def get_post_by_id(
        self, channel_username: str, pid: int, data_saver: Callable[[Channel], None]
    ) -> List[Channel]:
        logger.info(f"Request=get_post_by_id, params: pid={pid}", only_debug_mode=True)
        data = await self._fetcher.get_post_by_id(channel_username, pid, data_saver)
        return data


# Constructs PostsFetcher, which is responsible
#  for getting posts from service(s).
async def get_posts_fetcher() -> PostsFetcher:
    fetcher = None
    if SERVICE_NAME == "telegram":
        fetcher = TelegramFetcher()
    else:
        logger.error(f"Not supported SERVICE_NAME={SERVICE_NAME} in config.py")
        exit(1)
    logger.info(f"Selected service SERVICE_NAME={SERVICE_NAME}")
    pf = PostsFetcher(fetcher)
    await pf.setup()
    return pf
