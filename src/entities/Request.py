# @ author: vladddd46
# @ date:   10.04.2024
# @ brief:  Representation of request for fetching data.
from typing import List, Dict, Any
from enum import Enum


class RequestCode(Enum):
    OK = "OK"
    ERROR = "ERROR"
    UNDEFINED = "UNDEFINED"


class RequestData:
    def __init__(self, channels: List[Any], name: str, params: Dict, is_backfill: bool):
        self._channels = channels
        self._name = name
        self._params = params
        self._is_backfill = is_backfill

    @property
    def channels(self) -> List:
        return self._channels

    @channels.setter
    def channels(self, channels: List) -> None:
        self._channels = channels

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        self._name = name

    @property
    def params(self) -> Dict:
        return self._params

    @params.setter
    def params(self, params: Dict) -> None:
        self._params = params

    @property
    def is_backfill(self) -> bool:
        return self._is_backfill

    @is_backfill.setter
    def is_backfill(self, is_backfill: bool) -> None:
        self._is_backfill = is_backfill

    def to_json(self) -> Dict:
        return {
            "channels": self._channels,
            "name": self._name,
            "params": self._params,
            "is_backfill": self._is_backfill,
        }

    def __str__(self):
        return f"{str(self.to_json())}"

    def __repr__(self):
        return f"{str(self.to_json())}"


class Request:
    def __init__(self, code: RequestCode, data: RequestData, rid: int, error_msg: str):
        self._code = code
        self._data = data
        self._rid = rid
        self._error_msg = error_msg

    @property
    def code(self) -> RequestCode:
        return self._code

    @code.setter
    def code(self, code: RequestCode) -> None:
        self._code = code

    @property
    def data(self) -> RequestData:
        return self._data

    @data.setter
    def data(self, data: RequestData) -> None:
        self._data = data

    @property
    def rid(self) -> int:
        return self._rid

    @rid.setter
    def rid(self, rid: int) -> None:
        self._rid = rid

    @property
    def error_msg(self) -> str:
        return self._error_msg

    @error_msg.setter
    def error_msg(self, error_msg: str) -> None:
        self._error_msg = error_msg

    def __str__(self):
        return f"Request {self.rid}: data={self.data}"

    def __repr__(self):
        return f"Request {self.rid}: data={self.data}"
