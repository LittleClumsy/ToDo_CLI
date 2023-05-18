"""
This module contains functions to help with file paths and directories.
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


def create_directory(folder_path: str) -> bool:
    """
    Creates the directory at the given path.

    Args:
        folder_path (str): The path to the directory to create.

    Returns:
        bool: True if the directory was created, otherwise False.

    Examples:
        >>> create_directory("/home/username/.todo")
        True
    """
    if not path_exists(folder_path):
        makedirs(folder_path)
        return True
    return False


def join_paths(directory_one: str, directory_two: str) -> str:
    """
    Joins two file paths into one if possible. 

    Args:
        directory_one (str): The first path given. 
        directory_two (str): The second path given.

    Returns: 
        str: Two paths joined together.

    Examples:
        >>> join_paths("/home/username", ".todo")
        '/home/username/.todo'
    """
    return path.join(directory_one, directory_two)


def path_exists(directory: str) -> bool:
    """
    This will be used to test if the given path already exists.

    Args: 
        directory (str): Path to check if it exists.

    Returns:
        bool: Will return True if path exists, otherwise False. 

    Examples:
        >>> path_exists("/home/username/.todo")
        True
    """
    return path.exists(directory)
