# @ author: vladddd46
# @ date:   10.03.2024
# @ brief:  Telegram fetcher class.
#           Implements fetching posts from telegram
import asyncio
from datetime import datetime
from typing import Callable, List

from adaptors.TelethonAdaptors import (convert_telethon_channel,
                                       convert_telethon_comment,
                                       convert_telethon_post)
from config import SESSION
from entities.Post import Post
from entities.User import User
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

    async def __retrieve_posts(
        self, channel_username: str, limit: int, message_filter: Callable[[], bool]
    ):
        try:
            telethon_channel = await self.client.get_entity(channel_username)
            channel = convert_telethon_channel(telethon_channel)

            async for message in self.client.iter_messages(
                telethon_channel, limit=limit
            ):
                if message_filter(message):
                    post = convert_telethon_post(message)
                    try:
                        async for comment in self.client.iter_messages(
                            telethon_channel, reply_to=message.id
                        ):
                            if hasattr(comment.from_id, "user_id"):
                                from_user = User(comment.from_id.user_id)
                            else:
                                from_user = User(-1)
                            tmp_comment = convert_telethon_comment(comment, from_user)
                            post.add_comment(tmp_comment)
                    except:
                        pass
                    channel.add_post(post)
            return channel
        except Exception as e:
            print("Exception:", e)  # TODO: add logger

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
        # TODO: add logger
        mfilter = lambda message: True
        data = await self.__retrieve_posts(
            channel_username=channel_username, limit=1, message_filter=mfilter
        )
        return data

    # overrride
    async def get_last_n_posts(self, channel_username: str, num: int):
        # TODO: add logger
        mfilter = lambda message: True
        data = await self.__retrieve_posts(
            channel_username=channel_username, limit=num, message_filter=mfilter
        )
        return data

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
        # TODO: add logger
        mfilter = lambda message: message.id == pid
        data = await self.__retrieve_posts(
            channel_username=channel_username, message_filter=mfilter
        )
        return data
