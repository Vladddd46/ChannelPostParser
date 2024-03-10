# @ author: vladddd46
# @ date:   10.03.2024
# @ brief:  Entrypoint class, that provides
# 			API for getting posts from service
from fetchers.FetcherInterface import FetcherInterface
from entities.Post import Post
from typing import List

class PostsFetcher:

	def __init__(self, fetcher: FetcherInterface):
		self._fetcher = fetcher

	async def get_last_post(self): # TODO: return type -> Post
		pass

	async def get_last_n_posts(self, num: int): # TODO: return type -> List[Post]
		pass

	async def get_posts_by_date_range(self, from_date: datetime, to_date: datetime): # TODO: return type -> List[Post]
		pass

	async def get_posts_by_date(self, date: datetime): # TODO: return type -> List[Post]
		pass

	async def get_post_by_id(self, pid: int): # TODO: return type -> List[Post]
		pass