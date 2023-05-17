"""
This module will contain all the logic with regards to the storage directory of the application.
"""

from todo_cli.helpers.path_helper import (
    join_paths,
    path_exists,
    get_home_directory,
    create_directory
)


def get_storage_directory() -> str:
    """
    Returns the storage directory of the application.

    Returns:
        str: The storage directory of the application.

    Examples:
        >>> get_storage_directory()
        '/home/username/.todo'
    """
    return join_paths(get_home_directory(), ".todo")


def create_storage_directory() -> bool:
    """
    Creates the storage directory of the application.

    Returns:
        bool: True if the directory was created, False if the directory already exists.

    Examples:
        >>> create_storage_directory()
        True

        >>> create_storage_directory()
        False
    """
    storage_directory = get_storage_directory()
    if not path_exists(storage_directory):
        create_directory(storage_directory)
        return True
    return False
