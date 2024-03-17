# @ author: vladddd46
# @ date:   09.03.2024
# @ brief:  representation of post.
from datetime import datetime
from typing import List

from src.entities.Comment import Comment
from src.entities.Reaction import Reaction


class Post:
    def __init__(
        self,
        post_id: int,
        datetime: datetime,
        text: str,
        pinned: bool,
        views: int,
        reactions: List[Reaction],
        is_reply: bool,
        contains_media: bool,
        comments: List[Comment] = None,
    ):
        self._post_id = post_id
        self._datetime = datetime
        self._text = text
        # self._media = [media]  # TODO: add this feature
        self._pinned = pinned
        self._views = views
        self._reactions = reactions
        self._is_reply = is_reply
        self._contains_media = contains_media
        self._comments = comments if comments != None else []

    def add_comment(self, comment: Comment):
        self._comments.append(comment)

    @property
    def post_id(self) -> int:
        return self._post_id

    @post_id.setter
    def post_id(self, value: int):
        self._post_id = value

    @property
    def comments(self) -> List[Comment]:
        return self._comments

    @comments.setter
    def comments(self, value: List[Comment]):
        self._comments = value

    @property
    def contains_media(self) -> int:
        return self._contains_media

    @contains_media.setter
    def contains_media(self, value: int):
        self._contains_media = value

    @property
    def is_reply(self) -> bool:
        return self._is_reply

    @is_reply.setter
    def is_reply(self, value: bool):
        self._is_reply = value

    @property
    def datetime(self) -> datetime:
        return self._datetime

    @datetime.setter
    def datetime(self, value: datetime):
        self._datetime = value

    @property
    def text(self) -> str:
        return self._text

    @text.setter
    def text(self, value: str):
        self._text = value

    @property
    def pinned(self) -> bool:
        return self._pinned

    @pinned.setter
    def pinned(self, value: bool):
        self._pinned = value

    @property
    def views(self) -> int:
        return self._views

    @views.setter
    def views(self, value: int):
        self._views = value

    @property
    def reactions(self) -> List[Reaction]:
        return self._reactions

    @reactions.setter
    def reactions(self, value: List[Reaction]):
        if not all(isinstance(reaction, Reaction) for reaction in value):
            raise ValueError(
                "All elements in 'reactions' must be instances of the Reaction class."
            )
        self._reactions = value

    def __eq__(self, other):
        if not isinstance(other, Post):
            return False
        return self._post_id == other.post_id

    def __hash__(self):
        return hash(self._post_id)

    def to_json(self) -> dict:
        post_json = {
            "post_id": self.post_id,
            "datetime": self.datetime,
            "text": self.text,
            # "media": [media.to_json() for media in self._media],  # TODO Uncomment when the Media class is defined
            "pinned": self.pinned,
            "views": self.views,
            "reactions": [reaction.to_json() for reaction in self._reactions],
            "is_reply": self.is_reply,
            "media_in_post": self.contains_media,
            "comments": [cmnt.to_json() for cmnt in self._comments],
        }
        return post_json

    def __str__(self):
        return f"Post: id={self._post_id} | {self._datetime} | text={self._text} | views={self._views}"

    def __repr__(self):
        return f"Post: id={self._post_id} | {self._datetime} | text={self._text} | views={self._views}"
