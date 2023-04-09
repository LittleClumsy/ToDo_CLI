"""
This module contains all logic pertaining to reading and writing json files.
"""

from json import dump, load, JSONDecodeError


def write_json_file(file_path: str, content: dict | list):
    """
    This will write the content to the json file at the specified path.

    Args:
        file_path (str): The path to the json file.
        content (dict | list): The content to write to the json file.
    """
    with open(file_path, "w", encoding="UTF-8") as file:
        dump(content, file, indent=4)


def read_json_file(file_path: str) -> dict | list:
    """
    This will read the content from the json file at the specified path.

    Args:
        file_path (str): The path to the json file.

    Returns:
        dict | list: Returns content of json file.

    Raises:
        FileNotFoundError: If the file does not exist.
        ValueError: If the file is not a valid json file.
    """
    try:
        with open(file_path, "r", encoding="UTF-8") as file:
            return load(file)
    except JSONDecodeError:
        raise ValueError(f"File at {file_path} is not a valid json file.")
