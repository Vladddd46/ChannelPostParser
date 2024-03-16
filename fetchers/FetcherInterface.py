# @ author: vladddd46
# @ date:   10.03.2024
# @ brief:  Interface to Fetcher class.
#           It is responsible for fetching data from services.
#           Each service fetcher (telegram fetcher) should inherit this interface.
#           data_saver - function, that do further processing of fetched data.
#                        the purpose of passing it to Fetchers: if there are a lot of
#                        fetched data, it is more efficent to process it further (save)
#                        instead of having it in memory.
from abc import ABC, abstractmethod
from datetime import datetime
from typing import Callable

from entities.Channel import Channel


class FetcherInterface:
    service_name = None  # must be overridden in child class.

    @abstractmethod
    async def setup(self):
        pass

    @abstractmethod
    async def cleanup(self):
        pass

    @abstractmethod
    async def get_last_post(
        self, channel_username: str, data_saver: Callable[[Channel], None]
    ):
        pass

    @abstractmethod
    async def get_last_n_posts(
        self, channel_username: str, num: int, data_saver: Callable[[Channel], None]
    ):
        pass

    @abstractmethod
    async def get_posts_by_date_range(
        self,
        channel_username: str,
        from_date: datetime,
        to_date: datetime,
        data_saver: Callable[[Channel], None],
    ):
        pass

    @abstractmethod
    async def get_posts_by_date(
        self,
        channel_username: str,
        date: datetime,
        data_saver: Callable[[Channel], None],
    ):
        pass

    @abstractmethod
    async def get_post_by_id(
        self, channel_username: str, pid: int, data_saver: Callable[[Channel], None]
    ):
        pass
