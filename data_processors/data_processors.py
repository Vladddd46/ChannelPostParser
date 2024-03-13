# @ author: vladddd46
# @ date:   12.03.2024
# @ brief:  Implementation of data processor, that
# 			saves fetched data into json file.

import json
from datetime import datetime
from ftplib import FTP
from typing import Callable

from config import (DATA_PROCESSOR, FTP_SAVE_DIR_PATH,
                    INDENT_FOR_SAVED_JSON_DATA, RETRIVED_DATA_STORAGE_PATH)
from entities.Channel import Channel
from entrypoints.FtpServer import FtpServer
from tmp.creds import FTP_HOSTNAME, FTP_PASSWORD, FTP_PORT, FTP_USERNAME


def _dump_data_to_json(channel: Channel):
    current_datetime = datetime.now().strftime("%Y-%m-%d_%H-%M-%S-%f")
    filename = f"{channel.channel_id}_{current_datetime}.json"
    path = RETRIVED_DATA_STORAGE_PATH + filename

    datetime_serializer = (
        lambda obj: obj.isoformat() if isinstance(obj, datetime) else None
    )
    with open(path, "w", encoding="utf-8") as file:
        json.dump(
            channel.to_json(),
            file,
            indent=INDENT_FOR_SAVED_JSON_DATA,
            default=datetime_serializer,
            ensure_ascii=False,
        )


def _dump_data_to_ftp(channel: Channel):
    serv = FtpServer(FTP_HOSTNAME, FTP_PORT, FTP_USERNAME, FTP_PASSWORD)
    serv.save_json(
        data=channel.to_json(), path=FTP_SAVE_DIR_PATH, data_id=channel.channel_id
    )


def get_data_processor():
    if DATA_PROCESSOR == "json":
        # TODO: add logger
        return _dump_data_to_json
    elif DATA_PROCESSOR == "ftp":
        # TODO: add logger
        return _dump_data_to_ftp
    else:
        print("Unknown processor")  # TODO: add logger
        exit(1)
