# @ author: vladddd46
# @ date:   10.03.2024
# @ brief:  Telegram fetcher class.
#           Implements fetching posts from telegram
import asyncio
from datetime import datetime, timedelta, timezone
from typing import Callable, List

import pytz
from config import NUMBER_OF_MESSAGES_TO_SAVE, SESSION, TIMEZONE
from src.adaptors.TelethonAdaptors import (
    convert_telethon_channel,
    convert_telethon_comment,
    convert_telethon_post,
    convert_telethon_user,
)
from src.entities.Channel import Channel
from src.entities.Post import Post
from src.entities.User import User
from src.fetchers.FetcherInterface import FetcherInterface
from src.utils.Logger import logger
from telethon import TelegramClient, events
from tmp.creds import api_hash, api_id


class TelegramFetcher(FetcherInterface):
    service_name = "telegram"  # override

    def __str__(self):
        return f"Fetcher for service {self.service_name}: addr={id(self)}"

    def __repr__(self):
        return f"Fetcher for service {self.service_name}: addr={id(self)}"

    def __init__(self):
        self.client = None

    # @ brief: main logic of retrieves posts from telegram channel.
    # @ params:
    #           channel_username - TODO: should be renamed (because it may take channel_username or channel_id)
    #           limit - max. number of posts will be retrieved
    #           message_filter - labmda filter, that filters posts.
    #           offset_date - date from which starts posts retrieval (from newer posts to older)
    #
    async def __retrieve_posts(
        self,
        channel_username: str,
        limit: int,
        message_filter: Callable[[], bool],
        data_saver: Callable[[Channel], None],
        offset_date: datetime = datetime.now(pytz.utc).date(),
    ):
        offset_date = offset_date + timedelta(days=1)
        number_of_retrieved_messages = 0
        logger.info(
            f"Requested to retrieve posts from \n\tchannel={channel_username}\n\tlimit={limit}"
        )

        # empty channel
        # TODO: this is not the best solution. Think what should return this func in case of exception or any error.
        #       should it return anything at all? because datasaver do further data processing.
        channel = Channel(-1)
        try:
            telethon_channel = await self.client.get_entity(channel_username)
            channel = convert_telethon_channel(telethon_channel)
            logger.info(
                f"Retrieved channel={channel_username} entity: id={channel.channel_id}, subscribers={channel.num_of_subscribers}"
            )
            async for message in self.client.iter_messages(
                telethon_channel, limit=limit
            ):
                if message_filter(message):
                    post = convert_telethon_post(message)
                    number_of_retrieved_messages += 1
                    try:
                        async for comment in self.client.iter_messages(
                            telethon_channel, reply_to=message.id
                        ):
                            if hasattr(comment.from_id, "user_id"):
                                user_entity = await self.client.get_entity(
                                    comment.from_id
                                )
                                from_user = convert_telethon_user(user_entity)
                            else:
                                from_user = User(-1, "UNKNOWN_USER")
                            tmp_comment = convert_telethon_comment(comment, from_user)
                            post.add_comment(tmp_comment)
                            number_of_retrieved_messages += 1
                    except Exception as e:
                        logger.warning(
                            f"Exception in comments section of message.id={message.id}: {e}"
                        )

                    channel.add_post(post)

                    # periodically dump/save data and reload variables.
                    # this approach is used in order not to load memory with
                    # big amount of data.
                    if number_of_retrieved_messages > NUMBER_OF_MESSAGES_TO_SAVE:
                        data_saver(channel)
                        number_of_retrieved_messages = 0
                        channel.posts = []
            if len(channel.posts) != 0:
                data_saver(channel)
        except Exception as e:
            logger.error(
                f"Exception while retrieving posts from chat={channel.channel_id}: {e}"
            )
        return channel  # Exception occured.

    # overrride
    async def setup(self):
        self.client = await TelegramClient(SESSION, api_id, api_hash).start()

    # overrride
    async def cleanup(self):
        try:
            await self.client.disconnect()
        except Exception as e:
            logger.error(f"Error during Telethon client disconnect: {e}")
            exit(1)

    # overrride
    async def get_last_post(
        self, channel_username: str, data_saver: Callable[[Channel], None]
    ):
        mfilter = lambda message: True
        data = await self.__retrieve_posts(
            channel_username=channel_username,
            limit=1,
            message_filter=mfilter,
            data_saver=data_saver,
        )
        return data

    # overrride
    async def get_last_n_posts(
        self, channel_username: str, num: int, data_saver: Callable[[Channel], None]
    ):
        mfilter = lambda message: True
        data = await self.__retrieve_posts(
            channel_username=channel_username,
            limit=num,
            message_filter=mfilter,
            data_saver=data_saver,
        )
        return data

    # overrride
    async def get_posts_by_date_range(
        self,
        channel_username: str,
        from_date: datetime,
        to_date: datetime,
        data_saver: Callable[[Channel], None],
    ):
        from_date_with_timezone = from_date.replace(tzinfo=timezone.utc)
        to_date_with_timezone = to_date.replace(tzinfo=timezone.utc)
        mfilter = lambda message: not message.date < from_date_with_timezone
        data = await self.__retrieve_posts(
            channel_username=channel_username,
            message_filter=mfilter,
            data_saver=data_saver,
            offset_date=to_date_with_timezone,
        )
        return data

    # overrride
    async def get_posts_by_date(
        self,
        channel_username: str,
        date: datetime,
        data_saver: Callable[[Channel], None],
    ):
        data = await self.get_posts_by_date_range(
            channel_username=channel_username,
            from_date=date,
            to_date=date,
            data_saver=data_saver,
        )
        return data

    # overrride
    async def get_post_by_id(
        self, channel_username: str, pid: int, data_saver: Callable[[Channel], None]
    ):
        mfilter = lambda message: message.id == pid
        data = await self.__retrieve_posts(
            channel_username=channel_username,
            message_filter=mfilter,
            data_saver=data_saver,
        )
        return data
