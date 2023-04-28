"""
This module will contain all logic pertaining to the configuration of the application.
"""

from todo_cli.helpers.json_helper import write_json_file, read_json_file
from todo_cli.helpers.os_helper import create_directory, get_config_directory

def install_config_directory():
    """
    This will install the config directory for the application.
    """
    config_directory = get_config_directory()
    create_directory(config_directory)
    return config_directory


def install_config_file():
    """
    This will install the config file for the application.
    """
    config_directory = install_config_directory()
    write_json_file(f"{config_directory}/config.json", {"data_storage": ""})


def read_config_file() -> str:
    """
    This function will read the json file contents.

    Returns:
        str: Contents of .json file.

    Examples:
        >>> read_config_file()
        '/home/username/.todo/config.json.
    """
    config_directory = get_config_directory()
    file_path = f"{config_directory}/config.json"
    config = read_json_file(file_path)
    return config


def write_config_file(content: dict):
    """
    This function will write to the config file.

    Args:
        content (dict): Content to write to config file.
    """
    config_directory = get_config_directory()
    file_path = f"{config_directory}/config.json"
    write_json_file(file_path, content)
