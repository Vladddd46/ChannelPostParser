# @ author: vladddd46
# @ date:   16.03.2024
# @ brief:  Ftp server connection entrypoint.
#           Is used for doing manipulations in ftp server.

import json
from datetime import datetime
from typing import Union

import paramiko
from config import INDENT_FOR_SAVED_JSON_DATA


class FtpServer:
    def __init__(self, hostname: str, port: int, username: str, password: str):
        self.transport = paramiko.Transport((hostname, port))
        self.transport.connect(username=username, password=password)
        self.sftp = paramiko.SFTPClient.from_transport(self.transport)

    def ls(self, path: str = "."):
        files = self.sftp.listdir(path)
        return files

    def pwd(self):
        pwd = self.sftp.getcwd()
        return pwd

    def cd(self, path: str):
        self.sftp.chdir(path)

    def save_json(self, data: Union[list, dict], path: str, filename: str):
        datetime_serializer = (
            lambda obj: obj.isoformat() if isinstance(obj, datetime) else None
        )
        json_data = json.dumps(
            data,
            indent=INDENT_FOR_SAVED_JSON_DATA,
            default=datetime_serializer,
            ensure_ascii=False,
        )
        with self.sftp.open(path + filename, "w") as file:
            file.write(json_data)

    def directory_exists(self, path: str) -> bool:
        try:
            # Try to retrieve information about the directory
            self.sftp.stat(path)
            return True
        except FileNotFoundError:
            # If the directory does not exist, FileNotFoundError will be raised
            return False
        except Exception as e:
            return False

    def create_directory(self, path: str, mode: int = 0o755) -> bool:
        try:
            self.sftp.mkdir(path, mode)
            return True
        except Exception as e:
            return False

    def __del__(self):
        self.sftp.close()
        self.transport.close()
