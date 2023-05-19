"""
This module/file contains all logic pertaining to handling errors.
"""


def handle_install_error(error: Exception) -> int:
    """
    Handles an install error. This function is called when the application
    cannot create the storage directory or files.

    Returns:
        int: The exit code of the application.

    Examples:
        >>> handle_install_error()
        Install Error [1]: Could not create storage directory or files.
        Please report this issue to the developer.
        [returns] 1
    """
    print(error)
    print("Install Error [1]: Could not create storage directory or files.")
    print("Please report this issue to the developer.")
    return 1


def handle_json_error(error: Exception) -> int:
    """
    Handles a json error. This function is called when the application cannot
    read or write a json file.

    Returns:
        int: The exit code of the application.

    Examples:
        >>> handle_json_error()
        JSON Error [2]: Please report this issue to the developer.
        [returns] 2
    """
    print(error)
    print("JSON Error [2]: Please report this issue to the developer.")
    return 2
