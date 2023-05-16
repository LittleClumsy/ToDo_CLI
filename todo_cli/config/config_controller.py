"""
This module will contain all logic pertaining to the configuration of the application.
"""

# File Imports
from todo_cli.helpers.json_helper import write_json_file, read_json_file
from todo_cli.helpers.os_helper import create_directory, get_config_directory, path_exists


def install_config_file() -> bool:
    """
    This will install the config file for the application.
    The config file will be located at ~/.todo/config.json.
    If the file already exists, it will not be overwritten.

    Returns:
        bool: True if the file was created, False if the file already exists.

    Examples:
        >>> install_config_file()
        True

        >>> install_config_file()
        False
    """
    config_directory = get_config_directory()
    if not path_exists(f"{config_directory}/config.json"):
        create_directory(config_directory)
        write_json_file(f"{config_directory}/config.json", {})
        return True
    return False


def read_config_file() -> dict | list:
    """
    This function will read the json file contents.

    Returns:
        dict | list: The contents of the json file.

    Raises:
        FileNotFoundError: If the file does not exist.
        ValueError: If the file is not valid json.

    Examples:
        >>> read_config_file()
        {"key": "value"}
    """
    try:
        config_directory = get_config_directory()
        file_path = f"{config_directory}/config.json"
        config = read_json_file(file_path)
    except FileNotFoundError as file_not_found_error:
        raise FileNotFoundError(
            f"Config file not found at {file_path}.") from file_not_found_error
    except ValueError as value_error:
        raise ValueError(
            f"Config file at {file_path} is not valid json.") from value_error
    return config


def write_config_file(content: dict) -> None:
    """
    This function will write to the config file.

    Args:
        content (dict): Content to write to config file.

    Raises:
        FileNotFoundError: If the directory does not exist.

    Examples:
        >>> write_config_file({"key": "value"})
    """
    config_directory = get_config_directory()
    file_path = f"{config_directory}/config.json"
    write_json_file(file_path, content)
