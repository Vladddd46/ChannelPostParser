# @ author: vladddd46
# @ date:   09.03.2024
# @ brief:  adaptors, that convert telethon objects into entities.

from entities.Channel import Channel
from entities.Comment import Comment
from entities.Post import Post
from entities.Reaction import Reaction
from entities.User import User


def convert_telethon_channel(channel):
    num_of_subscribers = (
        -1 if channel.participants_count == None else channel.participants_count
    )
    user_name = channel.username if channel.username != None else ""
    title = channel.title if channel.title != None else ""
    ch = Channel(
        num_of_subscribers=num_of_subscribers,
        channel_id=channel.id,
        title=title,
        verified=channel.verified,
        scam=channel.scam,
        user_name=user_name,
    )
    return ch


def convert_telethon_comment(comment):
    txt = comment.message if comment.message != None else ""
    views = comment.views if comment.views != None else -1
    reactions = []
    if comment.reactions != None:
        for reaction in comment.reactions.results:
            reactions.append(convert_telethon_reaction(reaction))
    # self._from_user = from_user
    # ret = Comment(text=txt, datetime=comment.date, views=views, m_id=comment.id, reactions=reactions)
    # return ret


def convert_telethon_post(post):
    pass


def convert_telethon_user(user):
    pass


def convert_telethon_reaction(reaction):
    ret = Reaction(emoticon=reaction.reaction.emoticon, count=reaction.count)
    return ret
