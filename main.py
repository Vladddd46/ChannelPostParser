import asyncio
from datetime import datetime

from APIentrypoint.PostsFetcher import PostsFetcher, get_posts_fetcher


async def posts_retriever():
    posts_fetcher = await get_posts_fetcher()
    await posts_fetcher.get_last_post("ssternenko")
    await posts_fetcher.get_last_n_posts("ssternenko", 1)
    await posts_fetcher.get_posts_by_date_range("ssternenko", datetime.now(), datetime.now())
    await posts_fetcher.get_posts_by_date("ssternenko", datetime.now())
    await posts_fetcher.get_post_by_id("ssternenko", 123)
    await posts_fetcher.cleanup()

if __name__ == "__main__":
	# TODO: create global posts container, where posts_fetcher will store posts.
	# TODO: create 'saver' thread, which takes posts from container and saves it further in db service
	asyncio.run(posts_retriever())