from telethon import TelegramClient
from telethon.tl.types import PeerUser, PeerChannel
import asyncio
from creds import api_id, api_hash # create file creds.py with your own creds.

with TelegramClient('anon', api_id, api_hash) as client:
	chat = '@ssternenko'

	messages = []
	for message in client.iter_messages(chat, limit=1, reverse=False):
		messages.append(message)
		for comment in client.iter_messages(chat, limit=1, reply_to=message.id):
			print("Comment:", comment.text)
			print("Comment datetime:", comment.date)
			print("Comment from user:", comment.from_id, comment.get_sender())


	# Print the messages and their comments
	# for message in messages:
		# text = message.text
		# datetime = message.date
		# reactions = message.reactions
		# print("POST | datetime=" + str(datetime))
		# for i in reactions.results:
		# 	print(type(i.reaction.emoticon.encode('unicode_escape').decode('utf-8')))
		# print("media=", "not empty" if message.media else "empty")
		# print(text, "\n\n")
	

# example 2
# from telethon import TelegramClient
# from telethon.tl.types import PeerUser
# import asyncio
# from creds import api_id, api_hash  # Import your credentials from creds.py

# async def print_comments(client, chat):
#     async for message in client.iter_messages(chat, limit=1, reverse=False):
#         text = message.text
#         datetime = message.date
#         reactions = message.reactions
#         print("POST | datetime=" + str(datetime))
#         # for i in reactions.results:
#         #   print(i.reaction.emoticon)
#         print("media=", "not empty" if message.media else "empty")
#         print("\n\n")
#         async for comment in client.iter_messages(chat, limit=1, reply_to=message.id):
#             print("Comment:", comment.text)
#             print("Comment datetime:", comment.date)

#             # Get information about the sender of the comment
#             sender = await comment.get_sender()

#             # Print sender details
#             if sender:
#                 print("Sender of the Comment:")
#                 print(f"ID: {sender.id}")
#                 print(f"First Name: {sender.first_name}")
#                 print(f"Last Name: {sender.last_name}")
#                 print(f"Username: {sender.username}" if hasattr(sender, 'username') else "No username")
#             else:
#                 print("Error: Unable to fetch sender information")

#         print("\n")

# async def main():
#     async with TelegramClient('anon', api_id, api_hash) as client:
#         chat = '@ssternenko'
#         await print_comments(client, chat)

# if __name__ == "__main__":
#     asyncio.run(main())
