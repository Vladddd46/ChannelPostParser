# @ author: vladddd46
# @ date:   04.03.2024
# @ brief:  representation of user.


class User:
    def __init__(
        self,
        uid: int,
        username: str,
        first_name: str,
        last_name: str,
        is_premium: bool,
        is_verified: bool,
        is_scam: bool,
    ):
        self._uid = uid
        self._username = username
        self._first_name = first_name
        self._last_name = last_name
        self._is_premium = is_premium
        self._is_verified = is_verified
        self._is_scam = is_scam
        # self._photo = user_avatar // TODO: add this feature.

    def __eq__(self, other):
        if not isinstance(other, User):
            return False
        return self.uid == other.uid

    def __hash__(self):
        return hash(self.uid)

    @property
    def uid(self) -> int:
        return self._uid

    @uid.setter
    def uid(self, value: int):
        self._uid = value

    @property
    def username(self) -> str:
        return self._username

    @username.setter
    def username(self, value: str):
        self._username = value

    @property
    def first_name(self) -> str:
        return self._first_name

    @first_name.setter
    def first_name(self, value: str):
        self._first_name = value

    @property
    def last_name(self) -> str:
        return self._last_name

    @last_name.setter
    def last_name(self, value: str):
        self._last_name = value

    @property
    def is_premium(self) -> bool:
        return self._is_premium

    @is_premium.setter
    def is_premium(self, value: bool):
        self._is_premium = value

    @property
    def is_verified(self) -> bool:
        return self._is_verified

    @is_verified.setter
    def is_verified(self, value: bool):
        self._is_verified = value

    @property
    def is_scam(self) -> bool:
        return self._is_scam

    @is_scam.setter
    def is_scam(self, value: bool):
        self._is_scam = value

    def to_json(self):
        user_json = {
            "uid": self.uid,
            "username": self.username,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "is_premium": self.is_premium,
            "is_verified": self.is_verified,
            "is_scam": self.is_scam,
        }
        return user_json

    def __str__(self):
        return f"User: id={self._uid}, username={self._username}, name={self._first_name} {self._last_name}, is_premium={self._is_premium}"

    def __repr__(self):
        return f"User: id={self._uid}, username={self._username}, name={self._first_name} {self._last_name}, is_premium={self._is_premium}"
