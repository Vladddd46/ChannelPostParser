# @ author: vladddd46
# @ date:   10.03.2024
# @ brief:  Entrypoint class, that provides
# 			API for getting posts from service
from fetchers.FetcherInterface import FetcherInterface
from entities.Post import Post
from typing import List
from datetime import datetime
from config import SERVICE_NAME
from fetchers.TelegramFetcher import TelegramFetcher


class PostsFetcher:
    def __init__(self, fetcher: FetcherInterface):
        self._fetcher = fetcher

    def __str__(self):
        return str(self._fetcher)

    def __repr__(self):
        return str(self._fetcher)

    async def setup(self):
        await self._fetcher.setup()

    async def cleanup(self):
        await self._fetcher.cleanup()

    async def get_last_post(self, channel_username: str):  # TODO: return type -> Post
        res = await self._fetcher.get_last_post(channel_username)
        return res

    async def get_last_n_posts(
        self, channel_username: str, num: int
    ):  # TODO: return type -> List[Post]
        res = await self._fetcher.get_last_n_posts(channel_username, num)
        return res

    async def get_posts_by_date_range(
        self, channel_username: str, from_date: datetime, to_date: datetime
    ):  # TODO: return type -> List[Post]
        res = await self._fetcher.get_posts_by_date_range(
            channel_username, from_date, to_date
        )
        return res

    async def get_posts_by_date(
        self, channel_username: str, date: datetime
    ):  # TODO: return type -> List[Post]
        res = await self._fetcher.get_posts_by_date(channel_username, date)
        return res

    async def get_post_by_id(
        self, channel_username: str, pid: int
    ):  # TODO: return type -> List[Post]
        res = await self._fetcher.get_post_by_id(channel_username, pid)
        return res


# Constructs PostsFetcher, which is responsible
#  for getting posts from service(s).
async def get_posts_fetcher():
    fetcher = None
    if SERVICE_NAME == "telegram":
        fetcher = TelegramFetcher()
    else:
        print("Unknown service name")  # TODO: logger
        exit(1)
    pf = PostsFetcher(fetcher)
    await pf.setup()
    return pf
