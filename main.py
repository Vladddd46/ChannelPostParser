import asyncio
from datetime import datetime

from entrypoints.PostsFetcher import PostsFetcher, get_posts_fetcher


async def posts_retriever(channels):
	posts_fetcher = await get_posts_fetcher()

	tasks = [posts_fetcher.get_last_post(channel) for channel in channels]
	results = await asyncio.gather(*tasks)
	for channel, result in zip(channels, results):
		print(f"Result for {channel}: {result}")

	await posts_fetcher.cleanup()

if __name__ == "__main__":
	# TODO: create global posts container, where posts_fetcher will store posts.
	# TODO: create 'saver' thread, which takes posts from container and saves it further in db service
	# TODO: create functionality, that getts info about channels need to be monitored.

	# tmp solution: list of channels, from which script will retrieve posts.
	channels = ["ssternenko", "channel1", "channel2"]
	asyncio.run(posts_retriever(channels))