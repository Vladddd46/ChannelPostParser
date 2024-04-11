# @ author: vladddd46
# @ date:   17.03.2024
# @ brief:  Contains helper functions
import os
from typing import List
from datetime import datetime
from src.entities.Request import Request
from src.entities.Response import Response


def create_folder_if_not_exists(folder_path):
    res = False
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        res = True
    return res


def create_folders_if_not_exist(folders_list: List[str]):
    for folder_path in folders_list:
        create_folder_if_not_exists(folder_path)


def generate_filename(tag: str) -> str:
    current_datetime = datetime.now().strftime("%Y-%m-%d_%H-%M-%S-%f")
    filename = f"{tag}_{current_datetime}.json"
    return filename


def create_response(req: Request, filenames: List[List[str]]) -> Response:
    files = []
    for file_list in filenames:
        for filename in file_list:
            files.append(filename)
    date = datetime.now()
    response = Response(
        channels=req.data.channels,
        is_backfill=req.data.is_backfill,
        fetched_at=date,
        files=files,
    )
    return response
