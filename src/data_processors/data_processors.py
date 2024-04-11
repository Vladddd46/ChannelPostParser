# @ author: vladddd46
# @ date:   12.03.2024
# @ brief:  Implementation of data processor, that
# 			saves fetched data into json file.

import json
from datetime import datetime
from ftplib import FTP
from typing import Callable

from config import (
    DATA_PROCESSOR,
    FTP_SAVE_DIR_PATH,
    INDENT_FOR_SAVED_JSON_DATA,
    RETRIVED_DATA_STORAGE_PATH,
)
from src.entities.Channel import Channel
from src.entrypoints.FtpServer import FtpServer
from tmp.creds import FTP_HOSTNAME, FTP_PASSWORD, FTP_PORT, FTP_USERNAME
from src.utils.Logger import logger
from src.utils.Utils import generate_filename


def _dump_data_to_json(channel: Channel):
    fname = generate_filename(tag=str(channel.channel_id))
    path = RETRIVED_DATA_STORAGE_PATH + fname

    datetime_serializer = (
        lambda obj: obj.isoformat() if isinstance(obj, datetime) else None
    )
    new_format = [channel.to_json()]
    with open(path, "w", encoding="utf-8") as file:
        json.dump(
            new_format,
            file,
            indent=INDENT_FOR_SAVED_JSON_DATA,
            default=datetime_serializer,
            ensure_ascii=False,
        )
    return fname


# Define global variable _serv in order it initialize only once.
# Connecting to ftp is time-consumine action, so we do not want
# to do it many time.
_serv = None
if DATA_PROCESSOR == "ftp":
    _serv = FtpServer(FTP_HOSTNAME, FTP_PORT, FTP_USERNAME, FTP_PASSWORD)


def _dump_data_to_ftp(channel: Channel):
    fname = generate_filename(tag=str(channel.channel_id))
    _serv.save_json(data=channel.to_json(), path=FTP_SAVE_DIR_PATH, filename=fname)
    return fname


def get_data_processor():
    if DATA_PROCESSOR == "json":
        return _dump_data_to_json
    elif DATA_PROCESSOR == "ftp":
        return _dump_data_to_ftp
    else:
        logger.error(f"Not supported DATA_PROCESSOR={DATA_PROCESSOR} in config.py")
        exit(1)
    logger.info(f"Selected DATA_PROCESSOR={DATA_PROCESSOR}")
