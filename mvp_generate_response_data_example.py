# @ author: vladddd46
# @ date:   11.03.2024
# @ brief:  generates json file with posts.
import asyncio
import json
import time
from datetime import datetime

from telethon import TelegramClient, events
from tqdm import tqdm

from adaptors.TelethonAdaptors import (convert_telethon_channel,
                                       convert_telethon_comment,
                                       convert_telethon_post)
from config import EXAMPLE_FILES_PATH
from entities.Post import Post
from entities.User import User
from tmp.creds import api_hash, api_id

CHANNEL = "@ssternenko"
SESSION = "./tmp/anon"
POSTS_LIMIT = 100  # number of posts will be fetched from channel.

progress_bar = tqdm(total=POSTS_LIMIT + 1, desc="Processing", unit="iteration")


def datetime_serializer(obj):
    if isinstance(obj, datetime):
        return obj.isoformat()


async def main(api_id, api_hash):
    async with TelegramClient(SESSION, api_id, api_hash) as client:
        chat_name = CHANNEL
        chat = await client.get_entity(chat_name)
        channel = convert_telethon_channel(chat)
        data_to_save = {CHANNEL: []}
        async for message in client.iter_messages(chat, limit=POSTS_LIMIT):
            post = convert_telethon_post(message)

            # if there are comments on post
            if message.reply_to_msg_id:
                try:
                    async for comment in client.iter_messages(
                        chat, reply_to=message.id
                    ):
                        if hasattr(comment.from_id, "user_id"):
                            from_user = User(comment.from_id.user_id)
                        else:
                            from_user = User(-1)
                        tmp_comment = convert_telethon_comment(comment, from_user)
                        post.add_comment(tmp_comment)
                except Exception as e:
                    # this usually occurs when messege.text is empty.
                    print("Exception: ", e)
            data_to_save[chat_name].append(post.to_json())
            progress_bar.update(1)

        with open(EXAMPLE_FILES_PATH, "w", encoding="utf-8") as json_file:
            json.dump(
                data_to_save,
                json_file,
                indent=4,
                default=datetime_serializer,
                ensure_ascii=False,
            )
            progress_bar.update(1)


if __name__ == "__main__":
    start_time = time.time()
    asyncio.run(main(api_id, api_hash))
    progress_bar.close()
    end_time = time.time()
    print(f"Program took time={end_time-start_time} (sec.)")
