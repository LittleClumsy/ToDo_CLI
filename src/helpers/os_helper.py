"""
This module will contain all logic pertaining to the operating system.
"""

from os import path, makedirs


def get_home_directory() -> str:
    """
    Returns the home directory of the current user.

    Returns:
        str: The home directory of the current user.

    Examples:
        >>> get_home_directory()
        '/home/username'
    """
    return path.expanduser("~")


def get_config_directory() -> str:
    """
    Returns the config directory of the application.

    Returns:
        str: The config directory of the application.

    Examples:
        >>> get_config_directory()
        '/home/username/.todo'
    """
    return path.join(get_home_directory(), ".todo")


def create_directory(folder_path: str) -> None:
    """
    Creates the directory at the given path.

    Args:
        folder_path (str): The path to the directory to create.
    """
    if not path.exists(folder_path):
        makedirs(folder_path)


def join_paths(directory_one: str, directory_two: str) -> str:
    """
    Joins two file paths into one if possible. 

    Args:
        directory_one (str): The first path given. 
        directory_two (str): The second path given.

    Returns: 
        str: Two paths joined together.
    """

    return path.join(directory_one, directory_two)


def path_exists(directory: str) -> bool:
    """
    This will be used to test if the given path already exists.

    Args: 
        directory (str): Path to check if it exists.

    Returns:
        bool: Will return True if path exists, otherwise False. 
    """
    return path.exists(directory)

