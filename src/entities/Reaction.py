# @ author: vladddd46
# @ date:   09.03.2024
# @ brief:  representation of reaction on post/message.
from enum import Enum


class ReactionType(Enum):
    POSITIVE = "POSITIVE"
    NEGATIVE = "NEGATIVE"
    UNDEFINED = "UNDEFINED"


def _determineReactionTypeFromEmoticon(emoticon: str):
    # TODO: add more reactions.
    reaction_type = ReactionType.UNDEFINED
    if emoticon == "🥳":
        reaction_type = ReactionType.POSITIVE
    elif emoticon == "🤢":
        reaction_type = ReactionType.NEGATIVE
    return reaction_type


class Reaction:
    def __init__(
        self,
        count: int,
        emoticon: str = "",
        is_custom: bool = False,
        document_id: int = -1,
    ):
        self._emoticon = emoticon
        self._rtype = (
            _determineReactionTypeFromEmoticon(emoticon)
            if is_custom == False
            else ReactionType.UNDEFINED
        )
        self._count = count
        self._is_custom = is_custom
        self._document_id = document_id

    def __eq__(self, other):
        if not isinstance(other, Reaction):
            return False
        if self._is_custom == True:
            return self.document_id == other.document_id
        return self._emoticon == other.emoticon

    def __hash__(self):
        if self._is_custom == True:
            return hash(self.document_id)
        return hash(self.emoticon)

    @property
    def emoticon(self) -> str:
        return self._emoticon

    @emoticon.setter
    def emoticon(self, value: str):
        self._emoticon = value

    @property
    def document_id(self) -> int:
        return self._document_id

    @document_id.setter
    def document_id(self, value: int):
        self._document_id = value

    @property
    def is_custom(self) -> bool:
        return self._is_custom

    @is_custom.setter
    def is_custom(self, value: bool):
        self._is_custom = value

    @property
    def count(self) -> int:
        return self._count

    @count.setter
    def count(self, value: int):
        self._count = value

    @property
    def rtype(self) -> str:
        return self._rtype

    @emoticon.setter
    def rtype(self, value: str):
        self._rtype = value

    def to_json(self) -> dict:
        comment_json = {
            "emoticon": self._emoticon,
            "rtype": self._rtype.name,
            "count": self._count,
            "is_custom": self.is_custom,
            "document_id": self.document_id,
        }
        return comment_json

    def __str__(self):
        return f"Reaction: emoticon={self._emoticon}, count={self._count}, type={self._rtype.name}, is_custom={self.is_custom}"

    def __repr__(self):
        return f"Reaction: emoticon={self._emoticon}, count={self._count}, type={self._rtype.name}, is_custom={self.is_custom}"
