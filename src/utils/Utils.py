# @ author: vladddd46
# @ date:   17.03.2024
# @ brief:  Contains helper functions
import os
from typing import List


def create_folder_if_not_exists(folder_path):
    res = False
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        res = True
    return res


def create_folders_if_not_exist(folders_list: List[str]):
    for folder_path in folders_list:
        create_folder_if_not_exists(folder_path)
