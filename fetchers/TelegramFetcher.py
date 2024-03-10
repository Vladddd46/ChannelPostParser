# @ author: vladddd46
# @ date:   10.03.2024
# @ brief:  Telegram fetcher class.
#           Implements fetching posts from telegram
from fetchers.FetcherInterface import FetcherInterface


class TelegramFetcher(FetcherInterface):
	# override
	def get_last_post(self):
		pass

	# override
	def get_last_n_posts(self, num: int):
		pass

	# override
	def get_posts_by_date_range(self, from_date: datetime, to_date: datetime):
		pass

	# override
	def get_posts_by_date(self, date: datetime):
		pass

	# override
	def get_post_by_id(self, pid: int):
		pass

