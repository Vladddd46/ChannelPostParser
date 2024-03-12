# @ author: vladddd46
# @ date:   12.03.2024
# @ brief:  Implementation of data processor, that
# 			saves fetched data into json file.

from datetime import datetime
import json

from entities.Channel import Channel
from config import RETRIVED_DATA_STORAGE_PATH


def datetime_serializer(obj):
    if isinstance(obj, datetime):
        return obj.isoformat()


def dump_data_to_json(channel: Channel):
    current_datetime = datetime.now().strftime("%Y-%m-%d_%H-%M-%S-%f")
    filename = f"{channel.channel_id}_{current_datetime}.json"
    path = RETRIVED_DATA_STORAGE_PATH + filename

    with open(path, "w", encoding="utf-8") as file:
        json.dump(
            channel.to_json(),
            file,
            indent=4,
            default=datetime_serializer,
            ensure_ascii=False,
        )
