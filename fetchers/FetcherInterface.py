# @ author: vladddd46
# @ date:   10.03.2024
# @ brief:  Interface to Fetcher class.
#           It is responsible for fetching data from services.
# 			Each service fetcher (telegram fetcher) should inherit this interface.
from datetime import datetime
from abc import ABC, abstractmethod

class FetcherInterface:
    service_name = None # must be overriden in child class.

    @abstractmethod
    async def get_last_post(self, channel_username: str):
        pass

    @abstractmethod
    async def get_last_n_posts(self, channel_username: str, num: int):
        pass

    @abstractmethod
    async def get_posts_by_date_range(self, channel_username: str, from_date: datetime, to_date: datetime):
        pass

    @abstractmethod
    async def get_posts_by_date(self, channel_username: str, date: datetime):
        pass

    @abstractmethod
    async def get_post_by_id(self, channel_username: str, pid: int):
        pass
