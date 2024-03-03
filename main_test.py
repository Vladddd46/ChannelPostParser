from telethon import TelegramClient
from telethon.tl.types import PeerUser, PeerChannel
import asyncio
from creds import api_id, api_hash # create file creds.py with your own creds.

with TelegramClient('anon', api_id, api_hash) as client:
    chat = '@ssternenko'

    messages = []

    for message in client.iter_messages(chat, limit=10):
        messages.append(message)

    messages.reverse()

    # Print the messages and their comments
    for message in messages:
        text = message.text
        datetime = message.date
        reactions = message.reactions
        print("POST | datetime=" + str(datetime))
        for i in reactions.results:
        	print(type(i.reaction.emoticon.encode('unicode_escape').decode('utf-8')))
        print("media=", "not empty" if message.media else "empty")
        print(text, "\n\n")

