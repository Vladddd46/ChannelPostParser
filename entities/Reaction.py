# @ author: vladddd46
# @ date:   09.03.2024
# @ brief:  representation of telegram reaction on post/message.
from enum import Enum


class ReactionType(Enum):
    POSITIVE = "POSITIVE"
    NEGATIVE = "NEGATIVE"
    UNDEFINED = "UNDEFINED"


def __determineReactionTypeFromEmoticon(emoticon: str):
    # TODO: add more reactions.
    reaction_type = ReactionType.UNDEFINED
    if emoticon == "🥳":
        reaction_type = ReactionType.POSITIVE
    elif emoticon == "🤢":
        reaction_type = ReactionType.NEGATIVE
    return reaction_type


class Reaction:
    def __init__(self, emoticon: str):
        self._emoticon = emoticon
        self._rtype = __determineReactionTypeFromEmoticon(emoticon)

    def __eq__(self, other):
        if not isinstance(other, Reaction):
            return False
        return self._emoticon == other.emoticon

    def __hash__(self):
        return hash(self.emoticon)

    @property
    def emoticon(self) -> str:
        return self._emoticon

    @emoticon.setter
    def emoticon(self, value: str):
        self._emoticon = value

    @property
    def rtype(self) -> str:
        return self._rtype

    @emoticon.setter
    def rtype(self, value: str):
        self._rtype = value

    def to_json(self) -> dict:
        comment_json = {
            "emoticon": self._emoticon,
            "rtype": self._rtype,
        }
        return comment_json
