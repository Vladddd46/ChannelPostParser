# @ author: vladddd46
# @ date:   09.03.2024
# @ brief:  representation of channel.


class Channel:
    def __init__(
        self,
        channel_id: int,
        title: str,
        num_of_subscribers: int,
        verified: bool,
        scam: bool,
        user_name: str,
    ):
        self._num_of_subscribers = num_of_subscribers
        self._channel_id = channel_id
        self._title = title
        # self._photo = Photo // TODO: add avatar of the group | not forget to add getters/setters
        self._verified = verified
        self._scam = scam
        self._user_name = user_name

    @property
    def num_of_subscribers(self) -> int:
        return self._num_of_subscribers

    @num_of_subscribers.setter
    def num_of_subscribers(self, value: int):
        self._num_of_subscribers = value

    @property
    def channel_id(self) -> int:
        return self._channel_id

    @channel_id.setter
    def channel_id(self, value: int):
        self._channel_id = value

    @property
    def title(self) -> str:
        return self._title

    @title.setter
    def title(self, value: str):
        self._title = value

    @property
    def verified(self) -> bool:
        return self._verified

    @verified.setter
    def verified(self, value: bool):
        self._verified = value

    @property
    def scam(self) -> bool:
        return self._scam

    @scam.setter
    def scam(self, value: bool):
        self._scam = value

    @property
    def user_name(self) -> str:
        return self._user_name

    @user_name.setter
    def user_name(self, value: str):
        self._user_name = value

    def __eq__(self, other):
        if not isinstance(other, Channel):
            return False
        return self._channel_id == other.channel_id

    def __hash__(self):
        return hash(self.channel_id)

    def to_json(self) -> dict:
        channel_json = {
            "num_of_subscribers": self.num_of_subscribers,
            "channel_id": self.channel_id,
            "title": self.title,
            # "photo": self.photo.to_json()  # TODO: Uncomment when the Photo class is defined
            "verified": self.verified,
            "scam": self.scam,
            "user_name": self.user_name,
        }
        return channel_json

    def __str__(self):
        return f"Channel : {self._channel_id} | {self._title} | subscribers={self._num_of_subscribers}"

    def __repr__(self):
        return f"Channel : {self._channel_id} | {self._title} | subscribers={self._num_of_subscribers}"
