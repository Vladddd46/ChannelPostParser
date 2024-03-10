# @ author: vladddd46
# @ date:   10.03.2024
# @ brief:  Telegram fetcher class.
#           Implements fetching posts from telegram
from fetchers.FetcherInterface import FetcherInterface
from tmp.creds import api_id, api_hash
from config import SESSION
from entities.Post import Post
from typing import List

class TelegramFetcher(FetcherInterface):
	service_name = "telegram" # override

	def __init__(self, ):
		self.client = TelegramClient(SESSION, api_id, api_hash)
		self.client.start()

	def __del__(self):
		self.client.disconnect()

	async def __retrieve_posts(self, channel_username: str, limit: int):
		chat = await client.get_entity(channel_username)
		async for message in client.iter_messages(chat, limit=limit):
			# message object, that represents post

			if message.reply_to_msg_id:
				async for comment in client.iter_messages(chat, reply_to=message.id):
					# message(comment) object, that represents post
		# return List of Posts

	# overrride
	async def get_last_post(self, channel_username: str):
		res = await self.__retrieve_posts(channel_username, 1)
		return res

	# overrride
	async def get_last_n_posts(self, channel_username: str, num: int):
		pass

	# overrride
	async def get_posts_by_date_range(self, channel_username: str, from_date: datetime, to_date: datetime):
		pass

	# overrride
	async def get_posts_by_date(self, channel_username: str, date: datetime):
		pass

	# overrride
	async def get_post_by_id(self, channel_username: str, pid: int):
		pass

