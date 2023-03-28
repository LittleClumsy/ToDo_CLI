"""
This module contains all logic pertaining to reading and writing json files.
"""

from json import dump

def write_json_file(file_path: str, content: dict | list):
    """
    This will write the content to the json file at the specified path.

    Args:
        file_path (str): The path to the json file.
        content (dict | list): The content to write to the json file.
    """
    with open(file_path, "w") as file:
        dump(content, file, indent=4)
