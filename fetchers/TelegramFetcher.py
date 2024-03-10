# @ author: vladddd46
# @ date:   10.03.2024
# @ brief:  Telegram fetcher class.
#           Implements fetching posts from telegram
import asyncio
from datetime import datetime
from typing import List

from adaptors.TelethonAdaptors import convert_telethon_post
from config import SESSION
from entities.Post import Post
from telethon import TelegramClient, events
from tmp.creds import api_hash, api_id

from fetchers.FetcherInterface import FetcherInterface


class TelegramFetcher(FetcherInterface):
    service_name = "telegram"  # override

    def __str__(self):
        return f"Fetcher for service {self.service_name}: addr={id(self)}"

    def __repr__(self):
        return f"Fetcher for service {self.service_name}: addr={id(self)}"

    def __init__(self):
        self.client = None

    async def __retrieve_posts(self, channel_username: str, limit: int):
        chat = await self.client.get_entity(channel_username)
        # TODO: make implementation here

    # overrride
    async def setup(self):
        self.client = await TelegramClient(SESSION, api_id, api_hash).start()

    # overrride
    async def cleanup(self):
        try:
            await self.client.disconnect()
        except Exception as e:
            print(f"Error during Telethon client disconnect: {e}")  # TODO: add logger
            exit(1)

    # overrride
    async def get_last_post(self, channel_username: str):
        print("get_last_post=", channel_username)

    # overrride
    async def get_last_n_posts(self, channel_username: str, num: int):
        print("get_last_n_posts=", channel_username)

    # overrride
    async def get_posts_by_date_range(
        self, channel_username: str, from_date: datetime, to_date: datetime
    ):
        print("get_posts_by_date_range=", channel_username)

    # overrride
    async def get_posts_by_date(self, channel_username: str, date: datetime):
        print("get_posts_by_date=", channel_username)

    # overrride
    async def get_post_by_id(self, channel_username: str, pid: int):
        print("get_post_by_id=", channel_username)
