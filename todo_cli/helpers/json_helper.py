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

    Raises:
        TypeError: If the content is not of type dict or list.

    Examples:
        >>> write_json_file("test.json", {"test": "test"})
        None
        >>> write_json_file("test.json", ["test", "test"])
        None
        >>> write_json_file("test.json", "test")
        TypeError: Content must be of type dict or list, not <class 'str'>.
    """
    if not isinstance(content, (dict, list)):
        raise TypeError(
            f"Content must be of type dict or list, not {type(content)}.")

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
        TypeError: If the file is not a valid json file.

    Examples:
        >>> read_json_file("test.json")
        {"test": "test"}
        >>> read_json_file("test.json")
        ["test", "test"]
        >>> read_json_file("test.json")
        TypeError: File at test.json is not a valid json file.
    """
    content = None

    try:
        with open(file_path, "r", encoding="UTF-8") as file:
            content = load(file)
    except JSONDecodeError as decode_error:
        raise TypeError(
            f"File at {file_path} is not a valid json file.") from decode_error

    if (content is None or not isinstance(content, (dict, list))):
        raise TypeError(
            f"File at {file_path} is not a valid json file.")

    return content
