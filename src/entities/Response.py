# @ author: vladddd46
# @ date:   10.04.2024
# @ brief:  Representation of response after fetching data.

from datetime import datetime
from typing import List


class Response:
    def __init__(
        self,
        channel,
        is_backfill: bool,
        fetched_at: datetime.datetime,
        files: List[str],
    ):
        self._channel = channel
        self._is_backfill = is_backfill
        self._fetched_at = fetched_at
        self._files = files

    @property
    def channel(self):
        return self._channel

    @channel.setter
    def channel(self, channel) -> None:
        self._channel = channel

    @property
    def is_backfill(self) -> bool:
        return self._is_backfill

    @is_backfill.setter
    def is_backfill(self, is_backfill: bool) -> None:
        self._is_backfill = is_backfill

    @property
    def fetched_at(self) -> datetime.datetime:
        return self._fetched_at

    @fetched_at.setter
    def fetched_at(self, fetched_at: datetime.datetime) -> None:
        self._fetched_at = fetched_at

    @property
    def files(self) -> List[str]:
        return self._files

    @files.setter
    def files(self, files: List[str]) -> None:
        self._files = files

    def to_json(self) -> dict:
        return {
            "channel": self.channel,
            "is_backfill": self.is_backfill,
            "fetched_at": self.fetched_at,
            "files": self.files,
        }
