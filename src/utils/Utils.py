# @ author: vladddd46
# @ date:   17.03.2024
# @ brief:  Contains helper functions
import os
from datetime import datetime
from typing import List

from src.entities.Request import Request
from src.entities.Response import Response
from src.entities.Channel import Channel
from typing import Callable
from src.entrypoints.PostsFetcher import PostsFetcher


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
    # @brief: creates response from request data and list of filenames.
    # @param: filenames - filesnames, where data was saved.
    files = []
    for file_list in filenames:
        for filename in file_list:
            files.append(filename)
    if len(files) == 0:
        return None
    date = datetime.now()
    response = Response(
        channels=req.data.channels,
        is_backfill=req.data.is_backfill,
        fetched_at=date,
        files=files,
    )
    return response


def determine_tasks_to_run(
    req: Request, data_saver: Callable[[Channel], None], fetcher: PostsFetcher
):
    # @brief: Determines, which tasks should be run based on request.
    # @return: list of task, which should be run.
    request_data = req.data
    channels = request_data.channels

    tasks = []
    if request_data.name == "get_last_n_posts":
        num = int(request_data.params["num"])
        tasks = [
            fetcher.get_last_n_posts(channel, num, data_saver) for channel in channels
        ]
    elif request_data.name == "get_last_post":
        tasks = [fetcher.get_last_post(channel, data_saver) for channel in channels]
    elif request_data.name == "get_posts_by_date_range":
        from_date = request_data.params["from"]
        to_date = request_data.params["to"]
        tasks = [
            fetcher.get_posts_by_date_range(channel, from_date, to_date, data_saver)
            for channel in channels
        ]
    elif request_data.name == "get_posts_by_date":
        date = request_data.params["date"]
        tasks = [
            fetcher.get_posts_by_date(channel, date, data_saver) for channel in channels
        ]

    elif request_data.name == "get_post_by_id":
        pid = request_data.params["pid"]
        tasks = [
            fetcher.get_posts_by_date(channel, pid, data_saver) for channel in channels
        ]
    else:
        logger.error(f"Unknown function in request={request_data.name}")
    return tasks
