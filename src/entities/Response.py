# @ author: vladddd46
# @ date:   10.04.2024
# @ brief:  Representation of response after fetching data.

from datetime import datetime
from typing import List


class Response:
    def __init__(
        self,
        channels,
        is_backfill: bool,
        fetched_at: datetime,
        files: List[str],
        is_error: bool=False
    ):
        self._channels = channels
        self._is_backfill = is_backfill
        self._fetched_at = fetched_at
        self._files = files
        self._is_error = is_error

    @property
    def channels(self):
        return self._channels

    @channels.setter
    def channels(self, channels) -> None:
        self._channels = channels

    @property
    def is_backfill(self) -> bool:
        return self._is_backfill

    @is_backfill.setter
    def is_backfill(self, is_backfill: bool) -> None:
        self._is_backfill = is_backfill

    @property
    def fetched_at(self) -> datetime:
        return self._fetched_at

    @fetched_at.setter
    def fetched_at(self, fetched_at: datetime) -> None:
        self._fetched_at = fetched_at

    @property
    def files(self) -> List[str]:
        return self._files

    @files.setter
    def files(self, files: List[str]) -> None:
        self._files = files

    @property
    def is_error(self) -> bool:
        return self._is_error

    @is_error.setter
    def is_error(self, is_error: bool) -> None:
        self._is_error= is_error


    def to_json(self) -> dict:
        return {
            "channels": self.channels,
            "is_backfill": self.is_backfill,
            "fetched_at": self.fetched_at,
            "files": self.files,
        }

    def __str__(self):
        return f"Response | channels={self.channels}, is_backfill={self.is_backfill}, files={self.files}"

    def __repr__(self):
        return f"Response | channels={self.channels}, is_backfill={self.is_backfill}, files={self.files}"
