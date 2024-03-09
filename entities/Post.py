# @ author: vladddd46
# @ date:   09.03.2024
# @ brief:  representation of telegram post.
from entities.Channel import Channel
from entities.Reaction import Reaction
from datetime import datetime
from typing import List


class Post:
    def __init__(
        self,
        post_id: int,
        channel: Channel,
        datetime: datetime,
        text: str,
        pinned: bool,
        views: int,
        reactions: List[Reaction],
    ):
        self._post_id = post_id
        self._channel = channel
        self._datetime = datetime
        self._text = text
        # self._media = [media]  # TODO: add this feature
        self._pinned = pinned
        self._views = views
        self._reactions = reactions

    @property
    def post_id(self) -> int:
        return self._post_id

    @post_id.setter
    def post_id(self, value: int):
        self._post_id = value

    @property
    def channel(self) -> Channel:
        return self._channel

    @channel.setter
    def channel(self, value: Channel):
        if not isinstance(value, Channel):
            raise ValueError("The 'channel' must be an instance of the Channel class.")
        self._channel = value

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
            "channel": self.channel.to_json(),
            "datetime": self.datetime,
            "text": self.text,
            # "media": [media.to_json() for media in self._media],  # TODO Uncomment when the Media class is defined
            "pinned": self.pinned,
            "views": self.views,
            "reactions": [reaction.to_json() for reaction in self._reactions],
        }
        return post_json

    def __str__(self):
        return f"Post: id={self._post_id} | {self._channel} | {self._datetime} | text={self._text} | views={self._views}"

    def __repr__(self):
        return f"Post: id={self._post_id} | {self._channel} | {self._datetime} | text={self._text} | views={self._views}"
