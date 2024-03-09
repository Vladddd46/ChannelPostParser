from telethon import TelegramClient, events
from tmp.creds import api_id, api_hash
import asyncio

CHANNEL = "@ssternenko"
SESSION = "./tmp/anon"
POSTS_LIMIT = 1  # number of posts will be fetched from channel.


async def main(api_id, api_hash):
    async with TelegramClient(SESSION, api_id, api_hash) as client:
        chat_name = CHANNEL
        chat = await client.get_entity(chat_name)
        async for message in client.iter_messages(chat, limit=POSTS_LIMIT):
            posts[message.id] = {"post": message, "comments": []}

            if message.reply_to_msg_id:
                async for comment in client.iter_messages(chat, reply_to=message.id):
                    posts[message.id]["comments"].append(comment)


if __name__ == "__main__":
    posts = {}
    asyncio.run(main(api_id, api_hash))

    for msg_id in posts:
        msg = posts[msg_id]["post"]
        comments = posts[msg_id]["comments"]

        text = msg.text
        datetime = msg.date
        reactions = []
        for reaction in msg.reactions.results:
            tmp_reaction = {}
            tmp_reaction["emoticon"] = reaction.reaction.emoticon
            tmp_reaction["count"] = reaction.count
            reactions.append(tmp_reaction)
        msg_comments = []
        for comment in comments:
            tmp_comment = {}
            tmp_comment["text"] = comment.message
            tmp_comment["date"] = comment.date
            tmp_comment["from_userid"] = comment.from_id
            msg_comments.append(tmp_comment)

        print("=====POST=====")
        print("text=", text)
        print("datetime=", datetime)
        print("reactions:")
        for reaction in reactions:
            print(
                "\treaction="
                + str(reaction["emoticon"])
                + " count="
                + str(reaction["count"])
            )
        print("comments:")
        for cmnt in msg_comments:
            print(
                "\tcomment="
                + cmnt["text"]
                + " date="
                + str(cmnt["date"])
                + " from_userid"
                + str(cmnt["from_userid"])
            )
        print("========================\n")
