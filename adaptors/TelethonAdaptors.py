# @ author: vladddd46
# @ date:   09.03.2024
# @ brief:  adaptors, that convert telethon objects into entities.

import pytz
from config import TIMEZONE
from entities.Channel import Channel
from entities.Comment import Comment
from entities.Post import Post
from entities.Reaction import Reaction
from entities.User import User

_timezone = pytz.timezone(TIMEZONE)


def convert_telethon_channel(channel) -> Channel:
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


def convert_telethon_comment(comment, from_user: User) -> Comment:
    txt = comment.message if comment.message != None else ""
    views = comment.views if comment.views != None else -1
    reactions = []
    if comment.reactions != None:
        for reaction in comment.reactions.results:
            reactions.append(convert_telethon_reaction(reaction))
    contains_media = True if comment.media else False
    timezone_adobted_date = comment.date.astimezone(_timezone)
    tmp_comment = Comment(
        comment.id,
        comment.text,
        timezone_adobted_date,
        from_user,
        reactions,
        views,
        comment.is_reply,
        contains_media,
    )
    return tmp_comment


def convert_telethon_post(post) -> Post:
    tmp_contains_media = True if post.media else False
    tmp_reactions = []
    if post.reactions != None:
        for reaction in post.reactions.results:
            tmp_reactions.append(convert_telethon_reaction(reaction))
    tmp_views = post.views if post.views else -1
    timezone_adobted_date = post.date.astimezone(_timezone)
    tmp_post = Post(
        post_id=post.id,
        datetime=timezone_adobted_date,
        text=post.message,
        pinned=post.pinned,
        views=tmp_views,
        reactions=tmp_reactions,
        is_reply=post.is_reply,
        contains_media=tmp_contains_media,
    )
    return tmp_post


def convert_telethon_user(user):
    pass


def convert_telethon_reaction(reaction) -> Reaction:
    if hasattr(reaction.reaction, "document_id"):
        # ReactionCustomEmoji(document_id=int) class
        ret = Reaction(count=reaction.count, document_id=reaction.reaction.document_id)
    else:
        ret = Reaction(count=reaction.count, emoticon=reaction.reaction.emoticon)
    return ret
