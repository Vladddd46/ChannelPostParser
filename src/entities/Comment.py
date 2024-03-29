# @ author: vladddd46
# @ date:   09.03.2024
# @ brief:  representation of channel`s comment.
from datetime import datetime
from typing import List

from src.entities.Reaction import Reaction
from src.entities.User import User


class Comment:
    def __init__(
        self,
        m_id: int,
        text: str,
        datetime: datetime,
        from_user: User,
        reactions: List[Reaction],
        views: int,
        is_reply: bool,
        contains_media: bool,
    ):
        self._text = text
        self._datetime = datetime
        self._from_user = from_user
        self._reactions = reactions
        self._views = views
        self._m_id = m_id
        self._is_reply = is_reply
        self._contains_media = contains_media
        # self._media = [Media] // TODO: add this feature

    @property
    def text(self) -> str:
        return self._text

    @text.setter
    def text(self, value: str):
        self._text = value

    @property
    def contains_media(self) -> str:
        return self._contains_media

    @contains_media.setter
    def contains_media(self, value: str):
        self._contains_media = value

    @property
    def is_reply(self) -> bool:
        return self._is_reply

    @is_reply.setter
    def is_reply(self, value: bool):
        self._is_reply = value

    @property
    def m_id(self):
        return self._m_id

    @m_id.setter
    def m_id(self, value: str):
        self._m_id = value

    @property
    def datetime(self) -> datetime:
        return self._datetime

    @datetime.setter
    def datetime(self, value: datetime):
        self._datetime = value

    @property
    def from_user(self) -> User:
        return self._from_user

    @from_user.setter
    def from_user(self, value: User):
        if not isinstance(value, User):
            raise ValueError("The 'from_user' must be an instance of the User class.")
        self._from_user = value

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

    @property
    def views(self) -> int:
        return self._views

    @views.setter
    def views(self, value: int):
        self._views = value

    def to_json(self) -> dict:
        comment_json = {
            "text": self.text,
            "id": self.m_id,
            "datetime": self.datetime,
            "from_user": self.from_user.to_json(),
            "reactions": [reaction.to_json() for reaction in self._reactions],
            "views": self.views,
            "is_reply": self.is_reply,
            "contains_media": self.contains_media,
        }
        return comment_json

    def __str__(self):
        return f"{self._m_id}| {self._datetime} | {self.from_user}='{self.text}'"

    def __repr__(self):
        return f"{self._m_id}| {self._datetime} | {self.from_user}='{self.text}'"
